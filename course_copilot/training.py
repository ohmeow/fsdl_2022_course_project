# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_training.ipynb.

# %% ../nbs/02_training.ipynb 3
from __future__ import annotations

import abc, inspect, os
from functools import partial
from pathlib import Path
import random

from dotenv import load_dotenv
import optuna
import wandb

from . import utils

# %% auto 0
__all__ = ['TrainConfig', 'get_train_config_props', 'ModelTrainer']

# %% ../nbs/02_training.ipynb 7
load_dotenv()


class TrainConfig:
    """This class defines a base class for each task to implement. Contains class properties relevant to the training process"""

    training_subset = 1.0
    val_pct = 0.25
    random_seed = 2022
    only_seed_splits = True
    preprocess_strategy = None

# %% ../nbs/02_training.ipynb 8
def get_train_config_props(cfg: TrainConfig) -> dict:
    """Returns a dictionary of all the class properties in `cfg`"""
    log_params = {k: v if not callable(v) else v.__name__ for k, v in inspect.getmembers(cfg) if not k.startswith("__")}
    return log_params

# %% ../nbs/02_training.ipynb 11
class ModelTrainer(abc.ABC):
    def __init__(
        self,
        # The ML task to run (e.g., topic_segmentation, summarization)
        task: str,
        # The name of your experiment (e.g., deberta_v3_large). This value is used in conjunction with `task` when
        # logging information with W&B or else saving data releveant to training/evaluation runs
        experiment_name: str,
        # The `TrainConfig` for your task
        train_config: TrainConfig,
        # Where the project's data is stored
        data_path: str = "data",
        # Where exported Learners and other models should stored
        model_output_path: str = "models",
        # Where any logged data should be stored
        log_output_path: str = "logs",
        # Whether predictions should be logged
        log_preds: bool = False,
        # The number of predictions that should be logged. It is left to each subclass to define what that means
        log_n_preds: int = None,
        # Whether or not to log experiments and sweeps to W&B
        use_wandb: bool = False,
        # Whether or not you want to have printed out everything during a training/evaulation run
        verbose: bool = False,
        # Any other kwargs you want to use in your ModelTrainer
        **kwargs,
    ):
        self.task = task
        self.experiment_name = experiment_name
        self.train_config = train_config

        self.data_path = Path(data_path)

        self.model_output_path = Path(model_output_path)
        self.model_output_path.mkdir(parents=True, exist_ok=True)

        self.log_output_path = Path(log_output_path)
        self.log_output_path.mkdir(parents=True, exist_ok=True)
        self.log_preds = log_preds
        self.log_n_preds = log_n_preds

        self.use_wandb = use_wandb
        if self.use_wandb:
            wandb.login()

        self.verbose = verbose

    # --- training ---
    @abc.abstractmethod
    def get_training_data(self, on_the_fly=False, split_type="cross_validation"):
        pass

    def train(self, sweep_config: dict = None):
        if self.use_wandb and sweep_config is None:
            wandb.finish(quiet=not self.verbose)

    # --- inference ---
    def load_learner_or_model(self, model_learner_fpath: str | Path = None, device="cpu", mode="eval"):
        raise NotImplementedError()

    def get_preds(self, model_or_learner, data, **kwargs):
        raise NotImplementedError()

    # --- wandb ---
    def init_wandb_run(self, is_sweep: bool = False):
        run = wandb.init(
            project=f"{os.environ['WANDB_PROJECT_NAME']}-{self.task}",
            entity=os.environ["WANDB_TEAM"],
            group=f"{self.experiment_name}_sweep" if is_sweep else self.experiment_name,
            config=get_train_config_props(self.train_config),
            dir=self.log_output_path,
            reinit=True,
        )

        return run

    def configure_sweep(self, sweep_config: dict = None):
        sweep_id = wandb.sweep(
            sweep=sweep_config,
            project=f"{os.environ['WANDB_PROJECT_NAME']}-{self.task}",
            entity=os.environ["WANDB_TEAM"],
        )
        return sweep_id

    def update_train_config_from_sweep_params(self, params_d: dict):
        pass
        for k, v in params_d.items():
            if hasattr(self.train_config, k):
                setattr(self.train_config, k, wandb.config[k])

    # --- utility ---
    def get_train_config_props(self):
        return get_train_config_props(self.train_config)
