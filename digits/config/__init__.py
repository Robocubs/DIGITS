# Copyright (C) 2015-2017, NVIDIA CORPORATION. All rights reserved.
# Copyright (C) 2019, Nicholas Hubbard and contributors.
from typing import Dict

# Create this object before importing the following imports, since they edit the list
option_list: Dict = {}

from . import (  # noqa
    caffe,
    gpu_list,
    jobs_dir,
    log_file,
    torch,
    server_name,
    store_option,
    tensorflow,
    url_prefix,
)


def config_value(option):
    """
    Return the current configuration value for the given option
    """
    return option_list[option]
