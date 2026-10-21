# ImageNet-100 Prep & Benchmark

## 数据来源

ModelScope [tany0699/mini_imagenet100](https://modelscope.cn/datasets/tany0699/mini_imagenet100)

这是 mini-ImageNet (Vinyals et al., 2016) 的 100 类子集，224×224 分辨率。

## 实际规模

- 100 classes × 600 train + 100 val per class
- 训练集：60,000 张
- 验证集：10,000 张

## 本地路径

`/root/autodl-tmp/imagenet100/{train,val}`

## Files

- `create_imagenet100.py` — **DEPRECATED** 从 ImageNet-1K 创建 100 类子集（与实际使用数据不同，见 D061）
- `benchmark_1ep_walltime.py` — 1-epoch wall-time benchmark
