#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
    Base Ops Definition
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import models.layers as layers


def conv_1x1(inputs, downsample=False):
    """
        conv_1x1
    """
    return conv_base(inputs, (1, 1), downsample=downsample)


def conv_2x2(inputs, downsample=False):
    """
        conv_2x2
    """
    return conv_base(inputs, (2, 2), downsample=downsample)


def conv_3x3(inputs, downsample=False):
    """
        conv_3x3
    """
    return conv_base(inputs, (3, 3), downsample=downsample)


def conv_4x4(inputs, downsample=False):
    """
        conv_4x4
    """
    return conv_base(inputs, (4, 4), downsample=downsample)


def conv_5x5(inputs, downsample=False):
    """
        conv_5x5
    """
    return conv_base(inputs, (5, 5), downsample=downsample)


def dilated_2x2(inputs, downsample=False):
    """
        dilated_2x2
    """
    return conv_base(inputs, (2, 2), (2, 2), downsample)


def dilated_3x3(inputs, downsample=False):
    """
        dilated_3x3
    """
    return conv_base(inputs, (3, 3), (2, 2), downsample)


def conv_1x2_2x1(inputs, downsample=False):
    """
        conv_1x2_2x1
    """
    return pair_base(inputs, 2, downsample)


def conv_1x3_3x1(inputs, downsample=False):
    """
        conv_1x3_3x1
    """
    return pair_base(inputs, 3, downsample)


def conv_1x4_4x1(inputs, downsample=False):
    """
        conv_1x4_4x1
    """
    return pair_base(inputs, 4, downsample)


def conv_1x5_5x1(inputs, downsample=False):
    """
        conv_1x5_5x1
    """
    return pair_base(inputs, 5, downsample)


def sep_2x2(inputs, downsample=False):
    """
        sep_2x2
    """
    return sep_base(inputs, (2, 2), downsample=downsample)


def sep_3x3(inputs, downsample=False):
    """
        sep_3x3
    """
    return sep_base(inputs, (3, 3), downsample=downsample)


def sep_4x4(inputs, downsample=False):
    """
        sep_4x4
    """
    return sep_base(inputs, (4, 4), downsample=downsample)


def sep_5x5(inputs, downsample=False):
    """
        sep_5x5
    """
    return sep_base(inputs, (5, 5), downsample=downsample)


def maxpool_2x2(inputs, downsample=False):
    """
        maxpool_2x2
    """
    return maxpool_base(inputs, (2, 2), downsample)


def maxpool_3x3(inputs, downsample=False):
    """
        maxpool_3x3
    """
    return maxpool_base(inputs, (3, 3), downsample)


def maxpool_4x4(inputs, downsample=False):
    """
        maxpool_4x4
    """
    return maxpool_base(inputs, (4, 4), downsample)


def maxpool_5x5(inputs, downsample=False):
    """
        maxpool_5x5
    """
    return maxpool_base(inputs, (5, 5), downsample)


def avgpool_2x2(inputs, downsample=False):
    """
        avgpool_2x2
    """
    return avgpool_base(inputs, (2, 2), downsample)


def avgpool_3x3(inputs, downsample=False):
    """
        avgpool_3x3
    """
    return avgpool_base(inputs, (3, 3), downsample)


def avgpool_4x4(inputs, downsample=False):
    """
        avgpool_4x4
    """
    return avgpool_base(inputs, (4, 4), downsample)


def avgpool_5x5(inputs, downsample=False):
    """
        avgpool_5x5
    """
    return avgpool_base(inputs, (5, 5), downsample)


def conv_base(inputs, kernel, dilation=None, downsample=False):
    """
        conv_base
    """
    if dilation is None:
        dilation = (1, 1)
    filters = inputs.shape[1]
    if downsample:
        output = layers.conv(inputs, filters * 2, kernel, (2, 2))
    else:
        output = layers.conv(inputs, filters, kernel, dilation=dilation)
    return output


def pair_base(inputs, kernel, downsample=False):
    """
        pair_base
    """
    filters = inputs.shape[1]
    if downsample:
        output = layers.conv(inputs, filters, (1, kernel), (1, 2))
        output = layers.conv(output, filters, (kernel, 1), (2, 1))
        output = layers.conv(output, filters * 2, (1, 1))
    else:
        output = layers.conv(inputs, filters, (1, kernel))
        output = layers.conv(output, filters, (kernel, 1))
    return output


def sep_base(inputs, kernel, dilation=None, downsample=False):
    """
        sep_base
    """
    if dilation is None:
        dilation = (1, 1)
    filters = inputs.shape[1]
    if downsample:
        output = layers.sep(inputs, filters * 2, kernel, (2, 2))
    else:
        output = layers.sep(inputs, filters, kernel, dilation=dilation)
    return output


def maxpool_base(inputs, kernel, downsample=False):
    """
        maxpool_base
    """
    if downsample:
        filters = inputs.shape[1]
        output = layers.maxpool(inputs, kernel, (2, 2))
        output = layers.conv(output, filters * 2, (1, 1))
    else:
        output = layers.maxpool(inputs, kernel)
    return output


def avgpool_base(inputs, kernel, downsample=False):
    """
        avgpool_base
    """
    if downsample:
        filters = inputs.shape[1]
        output = layers.avgpool(inputs, kernel, (2, 2))
        output = layers.conv(output, filters * 2, (1, 1))
    else:
        output = layers.avgpool(inputs, kernel)
    return output
