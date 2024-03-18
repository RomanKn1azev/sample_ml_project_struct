import os
import torch


from torch.utils.data import Dataset

from pathlib import Path
from typing import Union

from src.utils.file import load_yml_file

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional, Tuple


class BaseDataset(ABC, torch.utils.data.Dataset):
    def __init__(
            self,
            root_path: Union[Path, str], 
            data_transform: Optional[Callable] = None, 
            target_transform: Optional[Callable] = None, 
            device: torch.device = torch.cpu
            ):
        super().__init__()
        
        # Load the data
        self.data = self.load_data(root_path)
        
        self.data_transform = data_transform
        self.target_transform = target_transform

    @abstractmethod
    def load_data(self, root_path: Union[Path, str]):
        pass

    def __len__(self) -> int:
        return len(self.data)

    @abstractmethod
    def __getitem__(self, index: int) -> Tuple[torch.Tensor, torch.Tensor]:
        pass

    def set_data_transform(self, data_transform: Optional[Callable]):
        self.data_transform = data_transform

    def get_data_transform(self) -> Optional[Callable]:
        return self.data_transform
    
    def set_target_transform(self, target_transform: Optional[Callable]):
        self.target_transform = target_transform

    def get_target_transform(self) -> Optional[Callable]:
        return self.target_transform


class DatasetBilder:
    def build(self, config_path: Union[Path, str]) -> Dataset:
        self.config = load_yml_file(config_path)


class TeacherTrainingDataset(BaseDataset):
    def __init__(
            self,
            root_path: Union[Path, str], 
            data_transform: Optional[Callable] = None, 
target_transform: Optional[Callable] = None, 
            device: torch.device = torch.cpu
            ):
        super().__init__(root_path, data_transform, target_transform, device)

    def load_data(self, root_path: Union[Path, str]):
        # Load the data from JSON files
        data_file = os.path.join(root_path, 'data.json')
        target_file = os.path.join(root_path, 'target.json')

        with open(data_file, 'r') as f:
            data = json.load(f)

        with open(target_file, 'r') as f:
            targets = json.load(f)

        # Convert the data and targets to PyTorch tensors
        data = [torch.tensor(item, dtype=torch.float32) for item in data]
        targets = [torch.tensor(item, dtype=torch.long) for item in targets]

        return data, targets

    def __getitem__(self, index: int) -> Tuple[torch.Tensor, torch.Tensor]:
        # Apply the data transform to the input data
        data, target = self.data[index], self.targets[index]
        if self.data_transform:
            data = self.data_transform(data)

        # Apply the target transform to the target data
        if self.target_transform:
            target = self.target_transform(target)

        return data, target

# class SampleDataset(Dataset):
#     def __init__(self, root_dir: str, transform=None) -> None:
#         self.root_dir = root_dir
#         self.transform = transform

#         self.data_paths = [os.path.join(root_dir, f) for f in os.listdir(root_dir)]
        
#         self.labels = [int(os.path.splitext(os.path.basename(f))[0]) for f in self.image_paths]

#     def __len__(self):
#         return len(self.data_paths)
    
#     def  __getitem__(self, idx):
#         ...