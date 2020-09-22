#!/usr/bin/env python
"""script to run ml experiment"""

import argparse
import json
import os

import importlib

def run_experiment(experiment_config: dict):
    """run a training experiment"""
    datasets_module = importlib.import_module("ml_project.datasets")
    dataset_class_ = getattr(datasets_module, experiment_config["dataset"])
    dataset = dataset_class_()
    print(dataset)
    # dataset is ready to input to experiment

def _parse_args():
    """ parse arguments for run experiment"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "experiment_config",
        type=str,
        help='experiment json file (\'{"dataset":"EmnistDataset"}\'',
    )
    args = parser.parse_args()
    return args



def main():
    """run experiment"""
    args = _parse_args()
    print(args.experiment_config)

    experiment_config = json.loads(args.experiment_config)
    print(experiment_config)

    run_experiment(experiment_config)

if __name__ == "__main__":
    main()