# Copyright (c) 2016-2017, NVIDIA CORPORATION.  All rights reserved.
# Copyright (C) 2019, Nicholas Hubbard and contributors.


from .upload_pretrained import UploadPretrainedModelTask
from .caffe_upload import CaffeUploadTask
from .torch_upload import TorchUploadTask
from .tensorflow_upload import TensorflowUploadTask

__all__ = [
    'UploadPretrainedModelTask',
    'CaffeUploadTask',
    'TorchUploadTask',
    'TensorflowUploadTask'
]
