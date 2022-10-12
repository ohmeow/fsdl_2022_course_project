# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_preprocessing.ipynb.

# %% ../nbs/01_preprocessing.ipynb 3
from __future__ import annotations

import argparse, datetime
from pathlib import Path

import pandas as pd

from . import utils

# %% auto 0
__all__ = ['convert_duration_to_seconds', 'build_train_df', 'build_segmentation_train_df', 'build_summarization_train_df',
           'preprocess_data']

# %% ../nbs/01_preprocessing.ipynb 6
def convert_duration_to_seconds(
    # A duration/iterval with the format of "hh:mm:ss"
    v: str,
) -> int:  # The total number of seconds

    hrs, mins, secs = v.split(":")
    return (60 * 60 * int(hrs)) + (60 * int(mins)) + float(secs)

# %% ../nbs/01_preprocessing.ipynb 7
def build_train_df(
    # The path to the data dir
    data_path: str
    | Path = "../data/",
) -> pd.DataFrame:  # A preprocessed DataFrame suitable for both segmentation and summarization training

    sheets_d = pd.read_excel(
        Path(data_path) / "raw/fsdl_2022_project_transcripts.xlsx", sheet_name=["lesson_topics", "lesson_transcripts"]
    )
    topics_df, transcripts_df = [v for k, v in sheets_d.items()]

    topics_df.drop(columns="video_url", inplace=True)
    transcripts_df.drop(columns="video_url", inplace=True)

    topics_df["timestamp"] = topics_df["timestamp"].astype(str)
    transcripts_df["timestamp"] = transcripts_df["timestamp"].astype(str)

    # define the start/end boundaries (in seconds) for each topic in each lesson
    topics_df["start_seconds"] = topics_df["timestamp"].apply(convert_duration_to_seconds)
    topics_df["end_seconds"] = topics_df.groupby(by=["course_title", "lesson_num"])["start_seconds"].shift(
        -1, fill_value=100000
    )

    # define the total number of elapsed seconds at each timestamp in the transcripts dataset
    transcripts_df["elapsed_seconds"] = transcripts_df["timestamp"].apply(convert_duration_to_seconds)

    # build our training data
    merged_df = topics_df[["course_title", "lesson_num", "topic", "start_seconds", "end_seconds"]].merge(
        transcripts_df, on=["course_title", "lesson_num"]
    )

    # keep only the merged records where the transcript lies inbetween the start/end of the topic
    merged_df = merged_df[
        (merged_df.elapsed_seconds >= merged_df.start_seconds) & (merged_df.elapsed_seconds < merged_df.end_seconds)
    ]

    # for both segmentation and summarization tasks, we'll need to group the transcripts by course + lesson + topic
    train_df = (
        merged_df[["course_title", "lesson_num", "topic", "transcript", "start_seconds"]]
        .groupby(by=["course_title", "lesson_num", "start_seconds", "topic"])
        .agg(list)
        .reset_index()
    )

    train_df.sort_values(by=["course_title", "lesson_num", "start_seconds"], inplace=True)

    return train_df

# %% ../nbs/01_preprocessing.ipynb 8
def build_segmentation_train_df(
    # The preprocess training DataFrame
    train_df: pd.DataFrame,
) -> pd.DataFrame:  # A preprocessed DataFrame for segmentation training
    """
    For segmentation, we want to create a dataset of seq, seq +1 examples, but also include the ability to gather negative samples
    from either sequences in that topic or not
    """
    seg_train_df = train_df.copy()

    seg_examples = []

    for example_idx, example in seg_train_df.iterrows():
        is_last_example = len(seg_train_df) == (example_idx + 1)

        for seq_idx, seq in enumerate(example["transcript"]):
            is_last_seq = len(example["transcript"]) == (seq_idx + 1)

            if is_last_seq and is_last_example:
                next_seq = None
                next_topic_begin_seq = None
            elif is_last_seq and not is_last_example:
                next_seq = seg_train_df.iloc[example_idx + 1]["transcript"][0]
                next_topic_begin_seq = next_seq
            else:
                next_seq = str(example["transcript"][seq_idx + 1])
                next_topic_begin_seq = None

            if seq_idx == 0:
                prev_seq = "xxBEGIN_TOPICxx"
            else:
                prev_seq = example["transcript"][seq_idx - 1]

            seg_examples.append(
                {
                    "course_title": example["course_title"],
                    "lesson_num": example["lesson_num"],
                    "topic": example["topic"],
                    "seq": str(seq),
                    "prev_seq": prev_seq,
                    "next_seq": next_seq,
                    "is_topic_end": is_last_seq,
                    "next_topic_begin_seq": next_topic_begin_seq,
                    "other_topic_seqs": [
                        str(txt) for i, txt in enumerate(example["transcript"]) if i != seq_idx and i != seq_idx + 1
                    ],
                }
            )

    seg_train_df = pd.DataFrame(seg_examples)

    return seg_train_df

# %% ../nbs/01_preprocessing.ipynb 9
def build_summarization_train_df(
    # The preprocess training DataFrame
    train_df: pd.DataFrame,
) -> pd.DataFrame:  # A preprocessed DataFrame for summarization training
    """For summarization, we want to concatenate all the sequences in a topic and use the resulting string to predict the topic"""
    summarization_train_df = train_df.copy()

    summarization_train_df["transcript"] = summarization_train_df["transcript"].apply(
        lambda v: " ".join([str(seq) for seq in v])
    )
    return summarization_train_df

# %% ../nbs/01_preprocessing.ipynb 11
def preprocess_data(
    # What dataset do we want to preprocess in the data/raw folder
    ds: str = "train",
    # The path to the data folder
    data_path: str | Path = "../data/",
    # Determines whether or not we save the cleaned Dataframes to data/clean
    return_file: bool = True,
    # Determines whether or not we return the cleaned Dataframes
    save_file: bool = False,
):
    is_train = ds == "train"

    train_df = build_train_df(data_path)
    segmentation_train_df = build_segmentation_train_df(train_df)
    summarization_train_df = build_summarization_train_df(train_df)

    # preprocessing that should only be applied to the training data
    if is_train:
        pass

    # save/return the preprocessed data
    if save_file:
        (Path(data_path) / "clean").mkdir(exist_ok=True)
        segmentation_train_df.to_csv((Path(data_path) / "clean") / f"segmentation_{ds}.csv", index=False)
        summarization_train_df.to_csv((Path(data_path) / "clean") / f"summarization_{ds}.csv", index=False)

    if return_file:
        return segmentation_train_df, summarization_train_df

# %% ../nbs/01_preprocessing.ipynb 16
if __name__ == "__main__" and utils.run_env == "script":
    # instantiate argparser
    parser = argparse.ArgumentParser()

    # define args
    parser.add_argument("--ds", type=str, default="train")
    parser.add_argument("--data_path", type=str, default="./data")
    args = parser.parse_args()

    preprocess_data(
        ds=args.ds,
        data_path=args.data_path,
        return_file=False,
        save_file=True,
    )
