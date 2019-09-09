#!/usr/bin/env python
# Copyright (c) 2016-2017, NVIDIA CORPORATION.  All rights reserved.
# Copyright (C) 2019, Nicholas Hubbard and contributors.

import os.path
import setuptools
from typing import Dict

LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

# Get requirements
requirements = []
with open(os.path.join(LOCAL_DIR, 'requirements.txt'), 'r') as infile:
    for line in infile:
        line = line.strip()
        if line and not line[0] == '#':  # ignore comments
            requirements.append(line)

setuptools.setup(
    name='digits',
    version="7.0.0",
    description="NVIDIA's Deep Learning GPU Training System",
    url='https://developer.nvidia.com/digits',
    author='DIGITS Development Team',
    author_email='digits@nvidia.com',
    license='BSD',
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='nvidia digits',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    scripts=['digits-devserver'],
)
