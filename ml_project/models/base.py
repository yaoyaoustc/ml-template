"""abstract model class, to be extended by specific types of model"""
from pathlib import Path

class Model:
    """base class of model, to be subclassed by predictors for specific type of data"""

    def __init__(self):
        self.name = "modelname"

    