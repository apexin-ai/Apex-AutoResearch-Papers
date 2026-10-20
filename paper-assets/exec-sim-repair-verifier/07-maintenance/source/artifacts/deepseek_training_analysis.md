# DeepSeek-Coder-6.7B Training Analysis

**Date:** 2026-05-16
**Server:** seetacloud-westd-4x5090
**Model:** deepseek-ai/deepseek-coder-6.7b-instruct (LoRA: q/k/v/o_proj, 16.8M params, 0.25% trainable)
**Data:** train=15,290 / val=1,896 (both experiments)

---

## Experiment 1: CWM (deepseek-cwm-func-s123)

**Status: SUCCESS** (EXIT_CODE=0)

| Metric | Epoch 1 | Epoch 2 | Epoch 3 |
|--------|---------|---------|---------|
| eval_loss | 0.04418 | **0.04076** | 0.04513 |

- **Final train_loss (avg):** 0.09762
- **Best eval_loss:** 0.04076 @ epoch 2
- **Training time:** 5244.30s (87.4 min), 3.66 s/it avg
- **Best model:** `/root/autodl-tmp/checkpoints_deepseek_cwm_func_seed123/best`

### Training loss trajectory (sampled)

| epoch | step loss |
|-------|-----------|
| 0.10 | 1.8751 |
| 2.09 | 0.0136 |
| 2.20 | 0.0132 |
| 2.30 | 0.0165 |
| 2.41 | 0.0172 |
| 2.51 | 0.0146 |
| 2.62 | 0.0153 |
| 2.72 | 0.0139 |
| 2.82 | 0.0111 |
| 2.93 | 0.0135 |

### Checkpoints

| Path | Size |
|------|------|
| checkpoint-956 (epoch 2) | dir, 2026-05-16 15:30 |
| checkpoint-1434 (epoch 3) | dir, 2026-05-16 15:59 |
| best (= epoch 2) | adapter_model.safetensors 67MB |

### Log excerpts (原文)

```
Line 453: {'eval_loss': 0.044184453785419464, 'eval_runtime': 55.4884, 'eval_samples_per_second': 34.169, 'eval_steps_per_second': 17.085, 'epoch': 1.0}
Line 884: {'eval_loss': 0.040762994438409805, 'eval_runtime': 55.9899, 'eval_samples_per_second': 33.863, 'eval_steps_per_second': 16.932, 'epoch': 2.0}
Line 1314: 2026-05-16 15:59:59,107 INFO Best model saved to /root/autodl-tmp/checkpoints_deepseek_cwm_func_seed123/best
Line 1315: {'eval_loss': 0.045128293335437775, 'eval_runtime': 55.9636, 'eval_samples_per_second': 33.879, 'eval_steps_per_second': 16.94, 'epoch': 3.0}
Line 1316: {'train_runtime': 5244.2968, 'train_samples_per_second': 8.747, 'train_steps_per_second': 0.273, 'train_loss': 0.0976209527029652, 'epoch': 3.0}
```

---

## Experiment 2: CLS (deepseek-cls-func)

**Status: SUCCESS** (EXIT_CODE=0)

| Metric | Epoch 1 | Epoch 2 | Epoch 3 |
|--------|---------|---------|---------|
| eval_loss | **0.07008** | 0.07268 | 0.07447 |

- **Final train_loss (avg):** 0.09484
- **Best eval_loss:** 0.07008 @ epoch 1
- **Training time:** 5444.83s (90.7 min), 3.80 s/it avg
- **Best model:** `/root/autodl-tmp/checkpoints_deepseek_cls_func/best`

### Training loss trajectory (sampled)

| epoch | step loss |
|-------|-----------|
| 0.10 | 1.4210 |
| 2.09 | 0.0234 |
| 2.20 | 0.0196 |
| 2.30 | 0.0234 |
| 2.41 | 0.0225 |
| 2.51 | 0.0190 |
| 2.62 | 0.0211 |
| 2.72 | 0.0193 |
| 2.82 | 0.0174 |
| 2.93 | 0.0204 |

### Checkpoints

| Path | Size |
|------|------|
| checkpoint-478 (epoch 1) | dir, 2026-05-16 14:58 |
| checkpoint-1434 (epoch 3) | dir, 2026-05-16 15:58 |
| best (= epoch 1) | adapter_model.safetensors 67MB |

### Log excerpts (原文)

```
Line 471: {'eval_loss': 0.07007486373186111, 'eval_runtime': 57.1359, 'eval_samples_per_second': 33.184, 'eval_steps_per_second': 16.592, 'epoch': 1.0}
Line 917: {'eval_loss': 0.07268214225769043, 'eval_runtime': 57.3913, 'eval_samples_per_second': 33.036, 'eval_steps_per_second': 16.518, 'epoch': 2.0}
Line 1363: 2026-05-16 15:58:47,033 INFO Best model saved to /root/autodl-tmp/checkpoints_deepseek_cls_func/best
Line 1364: {'eval_loss': 0.074471615254879, 'eval_runtime': 57.5708, 'eval_samples_per_second': 32.933, 'eval_steps_per_second': 16.467, 'epoch': 3.0}
Line 1365: {'train_runtime': 5444.8276, 'train_samples_per_second': 8.425, 'train_steps_per_second': 0.263, 'train_loss': 0.09484216978194158, 'epoch': 3.0}
```

---

## CWM vs CLS Comparison

| Metric | CWM | CLS | Delta (CWM - CLS) |
|--------|-----|-----|--------------------|
| Best eval_loss | 0.04076 | 0.07008 | **-0.02932** (CWM wins) |
| Final eval_loss (ep3) | 0.04513 | 0.07447 | -0.02934 |
| Final train_loss (avg) | 0.09762 | 0.09484 | +0.00278 |
| Best epoch | 2 | 1 | -- |
| Late-stage step loss (avg ep2.1-2.9) | ~0.014 | ~0.021 | -0.007 |

**Accuracy:** 日志中**无 accuracy 指标**，仅记录 eval_loss。两个实验的 compute_metrics 均未输出 accuracy。

### Observations

1. **CWM eval_loss 显著低于 CLS**（0.041 vs 0.070），CWM 验证损失约为 CLS 的 58%。
2. **CWM 在 epoch 2 达到最优，epoch 3 轻微上升**（0.04076 -> 0.04513, +10.7%）——轻微过拟合。
3. **CLS 从 epoch 1 起就单调上升**（0.07008 -> 0.07268 -> 0.07447）——更早过拟合，best checkpoint 在 epoch 1。
4. **CWM step loss 收敛更低**（~0.014 vs ~0.021），CWM 任务的训练信号更强。
5. **无 error/exception**，两个实验均正常完成。
