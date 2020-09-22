"""
EMINST dataset
"""

from ml_project.datasets.dataset import Dataset

class EmnistDataset(Dataset):
    """handwritten EMNIST dataset"""

    def __init__(self):
        self.num_classes = 10

def main():
    print("this is the main function")
    dataset = EmnistDataset()
    print(dataset.num_classes)

if __name__ == "__main__":
    main()