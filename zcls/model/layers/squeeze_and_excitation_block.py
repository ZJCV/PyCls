# -*- coding: utf-8 -*-

"""
@date: 2020/12/14 下午6:56
@file: squeeze_and_excitation_block.py
@author: zj
@description: 
"""

import torch.nn as nn


class _SqueezeAndExcitationBlockND(nn.Module):
    """
    Squeeze-and-Excitation Block
    参考：
    [se_module.py](https://github.com/moskomule/senet.pytorch/blob/master/senet/se_module.py)
    [如何评价Momenta ImageNet 2017夺冠架构SENet?](https://www.zhihu.com/question/63460684)
    """

    def __init__(self,
                 # 输入通道数
                 in_channels,
                 # 中间层衰减率
                 reduction=16,
                 # 数据维度
                 dimension=2):
        super(_SqueezeAndExcitationBlockND, self).__init__()
        assert dimension in [1, 2, 3]
        assert in_channels % reduction == 0, f'in_channels = {in_channels}, reduction = {reduction}'

        inner_channel = in_channels // reduction
        if dimension == 1:
            self.squeeze = nn.AdaptiveAvgPool1d((1))
        elif dimension == 2:
            self.squeeze = nn.AdaptiveAvgPool2d((1, 1))
        else:
            self.squeeze = nn.AdaptiveAvgPool3d((1, 1, 1))

        self.excitation = nn.Sequential(
            nn.Linear(in_channels, inner_channel, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(inner_channel, in_channels, bias=False),
            nn.Sigmoid()
        )

        self.init_weights()

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)

    def forward(self, x):
        """
        :param x: (N, C, **)
        """
        self._check_input_dim(x)
        N, C = x.shape[:2]

        out = self.squeeze(x)
        out_shape = out.shape
        out = self.excitation(out.view(N, C)).view(out_shape)
        scale = x * out.expand_as(x)
        return scale

    def _check_input_dim(self, input):
        raise NotImplementedError


class SqueezeAndExcitationBlock1D(_SqueezeAndExcitationBlockND):

    def __init__(self, in_channels, reduction=16, dimension=1):
        super().__init__(in_channels, reduction, dimension)

    def _check_input_dim(self, input):
        if input.dim() != 2 and input.dim() != 3:
            raise ValueError('expected 2D or 3D input (got {}D input)'
                             .format(input.dim()))


class SqueezeAndExcitationBlock2D(_SqueezeAndExcitationBlockND):

    def __init__(self, in_channels, reduction=16, dimension=2):
        super().__init__(in_channels, reduction, dimension)

    def _check_input_dim(self, input):
        if input.dim() != 4:
            raise ValueError('expected 4D input (got {}D input)'
                             .format(input.dim()))


class SqueezeAndExcitationBlock3D(_SqueezeAndExcitationBlockND):

    def __init__(self, in_channels, reduction=16, dimension=3):
        super().__init__(in_channels, reduction, dimension)

    def _check_input_dim(self, input):
        if input.dim() != 5:
            raise ValueError('expected 5D input (got {}D input)'
                             .format(input.dim()))
