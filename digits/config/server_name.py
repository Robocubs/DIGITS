# Copyright (C) 2015-2017, NVIDIA CORPORATION. All rights reserved.
# Copyright (C) 2019, Nicholas Hubbard and contributors.


import os
import platform

from . import option_list

if 'DIGITS_SERVER_NAME' in os.environ:
    value = os.environ['DIGITS_SERVER_NAME']
else:
    value = platform.node()

option_list['server_name'] = value
