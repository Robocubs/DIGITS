# Copyright (C) 2015-2017, NVIDIA CORPORATION. All rights reserved.
# Copyright (C) 2019, Nicholas Hubbard and contributors.


from . import option_list
import digits.device_query


option_list['gpu_list'] = ','.join([str(x) for x in range(len(digits.device_query.get_devices()))])
