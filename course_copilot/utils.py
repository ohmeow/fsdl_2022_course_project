# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_utils.ipynb.

# %% ../nbs/00_utils.ipynb 3
from __future__ import annotations

import abc, datetime, random, os
from pathlib import Path

import numpy as np
import torch
from torch.nn import functional as F
from fastai.losses import CrossEntropyLossFlat
from fastai.test_utils import show_install


# %% auto 0
__all__ = ['default_seed', 'run_env', 'detect_env', 'print_dev_environment']

# %% ../nbs/00_utils.ipynb 7
default_seed = int(os.getenv("RANDOM_SEED", 42))


# %% ../nbs/00_utils.ipynb 9
def detect_env():
    """A helper function that detects where you are running code"""
    if os.environ.get("KAGGLE_KERNEL_RUN_TYPE", False):
        run_env = "kaggle"
    elif os.path.isdir("/content"):
        run_env = "colab"
    elif os.path.isdir("../nbs") or os.path.isdir("../../nbs"):
        run_env = "local_nb"
    else:
        run_env = "script"

    return run_env


run_env = detect_env()


# %% ../nbs/00_utils.ipynb 11
def print_dev_environment():
    """Provides details on your development environment including packages installed, cuda/cudnn availability, GPUs, etc."""
    print(show_install())

