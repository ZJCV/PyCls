<div align="right">
  语言:
    🇨🇳
  <a title="英语" href="./README.md">🇺🇸</a>
</div>

 <div align="center"><a title="" href="git@github.com:ZJCV/ZCls.git"><img align="center" src="./imgs/ZCls.png"></a></div>

<p align="center">
  «ZCls»是一个分类模型基准代码库
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
  <a href="https://pypi.org/project/zcls/"><img src="https://img.shields.io/badge/PYPI-zcls-brightgreen"></a>
</p>

当前已实现：

* [[2021]RepVGG](https://arxiv.org/abs/2101.03697)
* [[2020]ResNeSt](https://arxiv.org/abs/2004.08955)
* [[2019]ACNet](https://arxiv.org/abs/1908.03930)
* [[2019]MobileNetV3](https://arxiv.org/abs/1905.02244)
* [[2019]GCNet](https://arxiv.org/abs/1904.11492)
* [[2019]SKNet](https://arxiv.org/abs/1903.06586)
* [[2018]ResNetD](https://arxiv.org/abs/1812.01187)
* [[2018]MNasNet](https://arxiv.org/abs/1807.11626)
* [[2018]ShuffleNetV2](https://arxiv.org/abs/1807.11164)
* [[2018]MobileNetV2](https://arxiv.org/abs/1801.04381)
* [[2017]Non-local](https://arxiv.org/abs/1711.07971)
* [[2017]SENet](https://arxiv.org/abs/1709.01507)
* [[2017]ShuffleNetV1](https://arxiv.org/abs/1707.01083)
* [[2017]MobileNetV1](https://arxiv.org/abs/1704.04861)
* [[2016]ResNeXt](https://arxiv.org/abs/1611.05431)
* [[2015]ResNet](https://arxiv.org/abs/1512.03385)


## 内容列表

- [内容列表](#内容列表)
- [背景](#背景)
- [主要维护人员](#主要维护人员)
- [致谢](#致谢)
- [参与贡献方式](#参与贡献方式)
- [许可证](#许可证)

## 背景

为了进一步提高算法性能，通常需要对已有模型进行改进，不可避免的就涉及到代码重构。创建本仓库，一方面作为新的模型/优化方法的`CodeBase`，另一方面也记录下自定义模型与已有实现（比如`Torchvision Models`）之间的比较

## 主要维护人员

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## 致谢

```
@misc{ding2021repvgg,
      title={RepVGG: Making VGG-style ConvNets Great Again}, 
      author={Xiaohan Ding and Xiangyu Zhang and Ningning Ma and Jungong Han and Guiguang Ding and Jian Sun},
      year={2021},
      eprint={2101.03697},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{fan2020pyslowfast,
  author =       {Haoqi Fan and Yanghao Li and Bo Xiong and Wan-Yen Lo and
                  Christoph Feichtenhofer},
  title =        {PySlowFast},
  howpublished = {\url{https://github.com/facebookresearch/slowfast}},
  year =         {2020}
}

@misc{zhang2020resnest,
      title={ResNeSt: Split-Attention Networks}, 
      author={Hang Zhang and Chongruo Wu and Zhongyue Zhang and Yi Zhu and Haibin Lin and Zhi Zhang and Yue Sun and Tong He and Jonas Mueller and R. Manmatha and Mu Li and Alexander Smola},
      year={2020},
      eprint={2004.08955},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{ding2019acnet,
      title={ACNet: Strengthening the Kernel Skeletons for Powerful CNN via Asymmetric Convolution Blocks}, 
      author={Xiaohan Ding and Yuchen Guo and Guiguang Ding and Jungong Han},
      year={2019},
      eprint={1908.03930},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{howard2019searching,
      title={Searching for MobileNetV3}, 
      author={Andrew Howard and Mark Sandler and Grace Chu and Liang-Chieh Chen and Bo Chen and Mingxing Tan and Weijun Wang and Yukun Zhu and Ruoming Pang and Vijay Vasudevan and Quoc V. Le and Hartwig Adam},
      year={2019},
      eprint={1905.02244},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{cao2019gcnet,
      title={GCNet: Non-local Networks Meet Squeeze-Excitation Networks and Beyond}, 
      author={Yue Cao and Jiarui Xu and Stephen Lin and Fangyun Wei and Han Hu},
      year={2019},
      eprint={1904.11492},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

更多致谢内容，请查看[THANKS](./THANKS)

## 参与贡献方式

欢迎任何人的参与！打开[issue](https://github.com/zjykzj/ZCls/issues)或提交合并请求。

注意:

* `GIT`提交，请遵守[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)规范
* 语义版本化，请遵守[Semantic Versioning 2.0.0](https://semver.org)规范
* `README`编写，请遵守[standard-readme](https://github.com/RichardLitt/standard-readme)规范

## 许可证

[Apache License 2.0](LICENSE) © 2020 zjykzj