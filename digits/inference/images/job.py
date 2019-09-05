# Copyright (c) 2016-2017, NVIDIA CORPORATION.  All rights reserved.
# Copyright (C) 2019, Nicholas Hubbard and contributors.


from ..job import InferenceJob
from digits.utils import subclass, override


@subclass
class ImageInferenceJob(InferenceJob):
    """
    A Job that exercises the forward pass of an image neural network
    """

    @override
    def job_type(self):
        return 'Image Inference'
