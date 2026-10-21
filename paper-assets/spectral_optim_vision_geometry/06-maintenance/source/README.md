# Spectral Optimization Across Vision Architecture Families

A controlled empirical study comparing spectral optimizers (Muon, SOAP, Shampoo) against AdamW and SGD across vision architectures (ResNet-50, ConvNeXt-T, DeiT-S) and datasets (CIFAR-100, Tiny-ImageNet, ImageNet-100).

## Requirements

See `requirements.txt` for dependencies.

```bash
pip install -r requirements.txt
```

## Training

### Muon (spectral optimizer)
```bash
python muon_train.py --model resnet50 --dataset cifar100 --epochs 20 --seed 42 --gpu 0
```

### Baseline optimizers (AdamW, SGD, SOAP, Shampoo)
```bash
python baseline_train.py --model resnet50 --dataset cifar100 --optimizer adamw --epochs 20 --seed 42 --gpu 0
```

### Supported models
- `resnet50` (ResNet-50)
- `convnext_tiny` (ConvNeXt-T)
- `deit_small` (DeiT-S)

### Supported datasets
- `cifar100` (CIFAR-100)
- `tiny_imagenet` (Tiny-ImageNet)
- `imagenet100` (ImageNet-100)

## Reproduction

To reproduce the main results (Table 1), run each optimizer × architecture × dataset combination with seeds 42, 2, 3:

```bash
# Example: Muon on ResNet-50, CIFAR-100
for seed in 42 2 3; do
    python muon_train.py --model resnet50 --dataset cifar100 --epochs 20 --seed $seed --gpu 0
done

# Example: AdamW on ResNet-50, CIFAR-100
for seed in 42 2 3; do
    python baseline_train.py --model resnet50 --dataset cifar100 --optimizer adamw --epochs 20 --seed $seed --gpu 0
done
```

## License

MIT
