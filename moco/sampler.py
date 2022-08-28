import random
import torch.utils.data
from collections import OrderedDict
import torch
import copy


def no_processing(data):
    return data


class TrackingSampler(torch.utils.data.Dataset):
    def __init__(self, datasets, processing=no_processing):

        self.datasets = datasets
# If p not provided, sample uniformly from all videos
        self.processing = processing


    def __len__(self):
        return 7872


    def __getitem__(self, index):
        # Select a dataset
        dataset = self.datasets
        # seq_id and frames
        seq_frame = random.randint(0, 7873)
        q = dataset[seq_frame]
        k = dataset[seq_frame + 3]
        q[0][1] = k[0][1]
        return q


class MOCOSampler(TrackingSampler):
""" See TrackingSampler."""
    def __init__(self, datasets, processing=no_processing):
        super().__init__(datasets=datasets, processing=processing)

