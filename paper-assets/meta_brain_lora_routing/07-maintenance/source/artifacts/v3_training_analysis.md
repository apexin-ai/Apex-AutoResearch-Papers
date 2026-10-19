# V3 LoRA Training Analysis (2026-05-16)

## Summary Table

| exp_id | initial_loss | final_loss | loss_ratio | steps | time_min | checkpoints | status |
|--------|-------------|------------|------------|-------|----------|-------------|--------|
| v3_lora_physical_r16 | 1.8865 | 0.5876 | 3.21 | 10000 | ~170 | final + 9 step (142M total) | SUCCESS |
| v3_lora_spatial_r16 | 1.8081 | 0.6126 | 2.95 | 10000 | ~171 | final + 9 step (142M total) | SUCCESS |
| v3_lora_universal_r16 | 1.8050 | 0.6030 | 2.99 | 10000 | ~170 | final + 9 step (142M total) | SUCCESS |

Config (all 3 identical): lora_rank=16, alpha=32, lr=2e-4, batch_size=16, 3.69M trainable params (0.11%), base=pi0_libero_openpi, data=libero_object_image (97 episodes, 66984 frames)

## Per-experiment Details

### v3_lora_physical_r16

**Log excerpt (last 10 lines):**
```
step=9600 loss=0.5900 lr=1.08e-05 grad_norm=5.25
step=9650 loss=0.5840 lr=1.06e-05 grad_norm=5.60
step=9700 loss=0.5873 lr=1.04e-05 grad_norm=4.18
step=9750 loss=0.5675 lr=1.03e-05 grad_norm=7.03
step=9800 loss=0.5820 lr=1.02e-05 grad_norm=4.46
step=9850 loss=0.5779 lr=1.01e-05 grad_norm=7.47
step=9900 loss=0.5793 lr=1.00e-05 grad_norm=5.47
step=9950 loss=0.5813 lr=1.00e-05 grad_norm=4.26
step=9999 loss=0.5876 lr=1.00e-05 grad_norm=6.07
Final adapter saved: .../v3lora_physical_r16/final
EXIT_CODE=0
```

**Checkpoint listing:**
```
final/          (15M: adapter_config.json + adapter_model.safetensors + README.md)
step_1000/ step_2000/ step_3000/ step_4000/ step_5000/
step_6000/ step_7000/ step_8000/ step_9000/
```

**Conclusion:** SUCCESS

### v3_lora_spatial_r16

**Log excerpt (last 10 lines):**
```
step=9600 loss=0.6139 lr=1.08e-05 grad_norm=6.18
step=9650 loss=0.6021 lr=1.06e-05 grad_norm=5.11
step=9700 loss=0.6029 lr=1.04e-05 grad_norm=5.21
step=9750 loss=0.6067 lr=1.03e-05 grad_norm=6.64
step=9800 loss=0.5942 lr=1.02e-05 grad_norm=5.05
step=9850 loss=0.6010 lr=1.01e-05 grad_norm=4.98
step=9900 loss=0.6003 lr=1.00e-05 grad_norm=4.97
step=9950 loss=0.5944 lr=1.00e-05 grad_norm=6.07
step=9999 loss=0.6126 lr=1.00e-05 grad_norm=4.48
Final adapter saved: .../v3lora_spatial_r16/final
EXIT_CODE=0
```

**Checkpoint listing:** same structure as physical (final + step_1000~step_9000, 142M total)

**Conclusion:** SUCCESS

### v3_lora_universal_r16

**Log excerpt (last 10 lines):**
```
step=9600 loss=0.6123 lr=1.08e-05 grad_norm=4.37
step=9650 loss=0.6020 lr=1.06e-05 grad_norm=2.54
step=9700 loss=0.5932 lr=1.04e-05 grad_norm=5.35
step=9750 loss=0.6093 lr=1.03e-05 grad_norm=4.72
step=9800 loss=0.5965 lr=1.02e-05 grad_norm=6.15
step=9850 loss=0.6029 lr=1.01e-05 grad_norm=3.17
step=9900 loss=0.6057 lr=1.00e-05 grad_norm=7.26
step=9950 loss=0.6084 lr=1.00e-05 grad_norm=4.84
step=9999 loss=0.6030 lr=1.00e-05 grad_norm=5.44
Final adapter saved: .../v3lora_universal_r16/final
EXIT_CODE=0
```

**Checkpoint listing:** same structure (final + step_1000~step_9000, 142M total)

**Conclusion:** SUCCESS

## Overall Assessment

### V3 vs Phase 1 对比

| metric | Phase 1 physical | Phase 1 visual | Phase 1 universal_r16 | V3 physical | V3 spatial | V3 universal |
|--------|-----------------|----------------|----------------------|-------------|------------|--------------|
| final_loss | 0.0114 | 0.0107 | 0.0112 | 0.5876 | 0.6126 | 0.6030 |

**V3 final loss (~0.59-0.61) 远高于 Phase 1 (~0.01)。** 这不是收敛失败——loss 从 ~1.8 稳定下降到 ~0.6（约 3x 压缩），且训练曲线在最后几千步已趋于平稳。可能原因：
- V3 使用了不同的 loss 计算方式（perturbation-aware loss vs 原始 action loss）
- V3 的 perturbation 类型不同（spatial 替代了 visual）
- V3 训练代码有本质性改动

### 三个 V3 实验内部对比

- **physical** 最优（0.5876），loss ratio 最高（3.21）
- **universal** 居中（0.6030），loss ratio 2.99
- **spatial** 最差（0.6126），loss ratio 最低（2.95）
- 三者差异不大（0.025 范围内），训练行为高度一致

### 训练效率
- 每个实验 ~170 min（~2h50m），~51s/step
- 每个 final adapter 15MB，总 checkpoint 含 9 个 step 存档共 142MB
- 无 W&B 数据（--no_wandb）
