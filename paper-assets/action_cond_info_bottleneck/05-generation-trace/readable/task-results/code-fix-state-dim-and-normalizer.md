# code fix state dim and normalizer

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_state_dim_and_normalizer_20260515T230057_result.json`
- **Structured JSON:** [`7f824681ea27f982543f.json`](../../sessions/7f/7f824681ea27f982543f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Bug 1: State dim mismatch — 不需要截断

- LIBERO state = **8 维**（7 关节角 + 1 gripper 分量对）
- SmolVLA config 声称 shape=[6]，但 pretrained checkpoint 的 normalizer stats 是 **8 维**，与 LIBERO 完全匹配
- 说明 `smolvla_libero` 实际用全部 8 维训练，config 的 [6] 是从 base 模型继承的未更新值
- `prepare_state` 只 pad 到 max_state_dim=32，不截断 → 8 维直接 pad 到 32 维，和原始训练一致
- **结论**：无需截断。`normalize_batch` 中保留了 `dim = min(data_dim, stats_dim)` 做安全防护

### Bug 2: MEAN_STD normalization — 关键修复

- 原始训练用 `NormalizerProcessorStep` 对 state/action 做 MEAN_STD 归一化
- `train_acib.py` 绕过 lerobot 框架直接调 `policy.forward()`，完全缺失归一化
- 模型看到的是原始量级的数据（state mean~[0.04, 0.03, 0.76, 2.97, ...]），而它期望归一化后的（~0 mean, ~1 std）

**修复**：添加两个函数
- `load_normalization_stats(model_id)` — 从 checkpoint 的 safetensors 加载 mean/std
- `normalize_batch(batch, norm_stats)` — 对 state 和 action 做 `(x - mean) / (std + 1e-8)`

### Dry-run 结果（10 步, batch=64, A100-96GB）

```
Step  1 | loss=0.1224  task=0.1118  ib=0.0720  consist=0.9975
Step  2 | loss=1.3789  task=1.3693  ib=0.0609  consist=0.8924
Step  3 | loss=0.9480  task=0.9447  ib=0.0523  consist=0.2794
Step  4 | loss=0.6304  task=0.6273  ib=0.0448  consist=0.2660
Step  5 | loss=0.5090  task=0.5048  ib=0.0692  consist=0.3489
Step  6 | loss=0.4171  task=0.4141  ib=0.0786  consist=0.2273
Step  7 | loss=0.4800  task=0.4713  ib=0.0637  consist=0.8040
Step  8 | loss=0.3744  task=0.3715  ib=0.0562  consist=0.2307
Step  9 | loss=0.3157  task=0.3088  ib=0.0462  consist=0.6466
Step 10 | loss=0.3597  task=0.3573  ib=0.0290  consist=0.2167
```

- **Loss**: task loss 从 ~1.37 降到 ~0.36，无爆炸，趋势健康
- **β warmup**: 当前 β=0.01（verify 脚本未实现 warmup），正式训练中 step < 1000 时 β=0
- **Peak VRAM**: **14,179 MB (~14GB)**，batch=64 在 96GB A100 上非常宽裕
- **速度**: ~1.3s/step（含 ACIB perturbation scoring）

### 代码改动（`/root/acib/scripts/train_acib.py`）

| 位置 | 改动 |
|------|------|
| Line 85-112 | 新增 `load_normalization_stats()` 和 `normalize_batch()` |
| Line 243-244 | `train()` 中加载 norm_stats |
| Line 285 | 训练循环中 forward 前调用 `normalize_batch(batch, norm_stats)` |

---
