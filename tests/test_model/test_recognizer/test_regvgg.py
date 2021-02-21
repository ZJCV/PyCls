# -*- coding: utf-8 -*-

"""
@date: 2021/2/2 下午5:46
@file: test_regvgg.py
@author: zj
@description: 
"""

import torch

from zcls.config import cfg
from zcls.config.key_word import KEY_OUTPUT
from zcls.model.recognizers.build import build_recognizer
from zcls.model.recognizers.vgg.repvgg import RepVGG
from zcls.model.backbones.vgg.repvgg_backbone import arch_settings
from zcls.model.conv_helper import insert_repvgg_block, insert_acblock, fuse_repvgg_block, fuse_acblock


def test_regvgg():
    data = torch.randn(1, 3, 224, 224)
    for key in arch_settings.keys():
        print('*' * 10, key)
        cfg.merge_from_file('configs/benchmarks/repvgg/repvgg_b2g4_cifar100_224_e100_sgd_calr.yaml')
        model = RepVGG(cfg)
        # print(model)
        outputs = model(data)[KEY_OUTPUT]
        assert outputs.shape == (1, 100)

        print('insert_regvgg_block -> fuse_regvgg_block')
        insert_repvgg_block(model)
        # print(model)
        model.eval()
        outputs_insert = model(data)[KEY_OUTPUT]
        fuse_repvgg_block(model)
        # print(model)
        model.eval()
        outputs_fuse = model(data)[KEY_OUTPUT]

        # print(outputs_insert)
        # print(outputs_fuse)
        print(torch.sqrt(torch.sum((outputs_insert - outputs_fuse) ** 2)))
        print(torch.allclose(outputs_insert, outputs_fuse, atol=1e-8))
        assert torch.allclose(outputs_insert, outputs_fuse, atol=1e-8)

        print('insert_regvgg_block -> insert_acblock -> fuse_acblock -> fuse_regvgg_block')
        insert_repvgg_block(model)
        insert_acblock(model)
        # print(model)
        model.eval()
        outputs_insert = model(data)[KEY_OUTPUT]
        fuse_acblock(model)
        fuse_repvgg_block(model)
        # print(model)
        model.eval()
        outputs_fuse = model(data)[KEY_OUTPUT]

        print(torch.sqrt(torch.sum((outputs_insert - outputs_fuse) ** 2)))
        print(torch.allclose(outputs_insert, outputs_fuse, atol=1e-6))
        assert torch.allclose(outputs_insert, outputs_fuse, atol=1e-6)

        print('insert_acblock -> insert_regvgg_block -> fuse_regvgg_block -> fuse_acblock')
        insert_repvgg_block(model)
        insert_acblock(model)
        # print(model)
        model.eval()
        outputs_insert = model(data)[KEY_OUTPUT]
        fuse_acblock(model)
        fuse_repvgg_block(model)
        # print(model)
        model.eval()
        outputs_fuse = model(data)[KEY_OUTPUT]

        print(torch.sqrt(torch.sum((outputs_insert - outputs_fuse) ** 2)))
        print(torch.allclose(outputs_insert, outputs_fuse, atol=1e-6))
        assert torch.allclose(outputs_insert, outputs_fuse, atol=1e-6)


def test_config_file():
    data = torch.randn(3, 3, 224, 224)

    print('repvgg_b2g4_custom_cifar100_224_e100_sgd')
    config_file = "configs/benchmarks/repvgg/repvgg_b2g4_cifar100_224_e100_sgd_calr.yaml"
    cfg.merge_from_file(config_file)

    device = torch.device('cpu')
    model = build_recognizer(cfg, device)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)
    fuse_repvgg_block(model)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)

    print('repvgg_b2g4_acb_custom_cifar100_224_e100_sgd')
    config_file = "configs/benchmarks/repvgg/repvgg_b2g4_acb_cifar100_224_e100_sgd_calr.yaml"
    cfg.merge_from_file(config_file)

    device = torch.device('cpu')
    model = build_recognizer(cfg, device)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)
    # 注意：如果在RepVGG中嵌入了ACBlock，融合时应该先acb再regvgg
    fuse_acblock(model)
    print(model)
    fuse_repvgg_block(model)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)

    print('acb_repvgg_b2g4_custom_cifar100_224_e100_sgd')
    config_file = "configs/benchmarks/repvgg/acb_repvgg_b2g4_cifar100_224_e100_sgd_calr.yaml"
    cfg.merge_from_file(config_file)

    device = torch.device('cpu')
    model = build_recognizer(cfg, device)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)
    # 注意：如果先嵌入ACBlock再嵌入RepVGGBlock，那么融合时应该先repvgg_block再acblock
    fuse_repvgg_block(model)
    print(model)
    fuse_acblock(model)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)

    print('rxtd50_32x4d_acb_rvb_custom_cifar100_224_e100_sgd')
    config_file = "configs/benchmarks/repvgg/rxtd50_32x4d_acb_rvb_cifar100_224_e100_sgd_calr.yaml"
    cfg.merge_from_file(config_file)

    device = torch.device('cpu')
    model = build_recognizer(cfg, device)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)
    # 注意：如果先嵌入ACBlock再嵌入RepVGGBlock，那么融合时应该先repvgg_block再acblock
    fuse_repvgg_block(model)
    print(model)
    fuse_acblock(model)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)

    print('rxtd50_32x4d_rvb_acb_custom_cifar100_224_e100_sgd')
    config_file = "configs/benchmarks/repvgg/rxtd50_32x4d_rvb_acb_cifar100_224_e100_sgd_calr.yaml"
    cfg.merge_from_file(config_file)

    device = torch.device('cpu')
    model = build_recognizer(cfg, device)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)
    # 注意：如果先嵌入RepVGGBlock再嵌入ACBlock，那么逆序融合
    fuse_acblock(model)
    print(model)
    fuse_repvgg_block(model)
    print(model)
    outputs = model(data)[KEY_OUTPUT]

    assert outputs.shape == (3, 100)


if __name__ == '__main__':
    test_regvgg()
    test_config_file()
