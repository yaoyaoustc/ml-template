"""dataset class to be extended by dataset-specific classes"""
from pathlib import Path
import argparse
import os

class Dataset():
    """abstract class for datasets"""

    @classmethod
    def data_dirname(cls):
        return Path(__file__).resolve().parents[3] / "data"
