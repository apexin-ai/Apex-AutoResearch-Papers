# Collapse Dynamics Update — 2026-05-17

## 状态：两个 run 尚未到 step 50，当前数据到 step 30

### 进度

| Run | 当前 step | 预计到 step 50 | 预计到 step 100 |
|-----|-----------|---------------|----------------|
| grpo_random_20 | 39/100 | ~80 min | ~7.5h |
| grpo_cka_only_20 | 30/100 | ~140 min | ~8h |

### 核心指标趋势（step 10/20/30）

#### grpo_cka_only_20（CKA-only 剪枝 → SFT → GRPO）

| Step | Reward | Frac_zero_std | Grad_norm | KL | Entropy |
|------|--------|---------------|-----------|------|---------|
| 10 | 0.2531 | 0.175 | 1.89 | 0.0012 | 0.083 |
| 20 | 0.2181 | 0.200 | 1.25 | 0.0012 | 0.075 |
| 30 | 0.2500 | 0.200 | 1.10 | 0.0017 | 0.097 |

**判断：稳定，无 collapse 迹象。** Reward 平稳在 0.22-0.25，frac_zero_std 稳定在 0.175-0.200（远低于 0.5 阈值），grad_norm 持续下降。

#### grpo_random_20（随机剪枝 → SFT → GRPO）

| Step | Reward | Frac_zero_std | Grad_norm | KL | Entropy |
|------|--------|---------------|-----------|------|---------|
| 10 | 0.1606 | 0.300 | 3.75 | 0.0042 | 0.231 |
| 20 | 0.1419 | 0.325 | 8.62 | 0.0047 | 0.228 |
| 30 | 0.1663 | 0.325 | 3.67 | 0.0046 | 0.235 |

**判断：稳定，未 collapse。** Reward 在 0.14-0.17 震荡，frac_zero_std 稳定在 0.30-0.33（低于 0.5 但高于 cka_only）。step 20 有一次 grad_norm spike (8.62) 但已恢复。

### 对比参照

#### grpo_stage2_rasp_20_v9（RASP → SFT → GRPO stage1 → GRPO stage2）

| Step | Reward | Frac_zero_std | Grad_norm | Status |
|------|--------|---------------|-----------|--------|
| 10 | 0.0150 | 0.875 | 0.01 | — |
| 20 | 0.0388 | 0.800 | 0.01 | — |
| 30 | 0.0206 | 0.950 | 1.40 | finished |

**已 collapse。** frac_zero_std 0.80-0.95，reward 几乎为零。注意此 run 是 stage2 GRPO（在已 GRPO 过的模型上再训），不是直接对比。

#### grpo_stage2_standard_20_v8（Standard → SFT → GRPO stage1 → GRPO stage2）

| Step | Reward | Frac_zero_std | Grad_norm | Status |
|------|--------|---------------|-----------|--------|
| 10 | 0.0575 | 0.500 | 2.91 | — |
| 20 | 0.0613 | 0.675 | 1.59 | — |
| 30 | 0.0650 | 0.525 | 2.28 | — |
| 40 | 0.0956 | 0.450 | 3.45 | — |
| 50 | 0.0369 | 0.600 | 2.09 | — |
| 60 | 0.0406 | 0.525 | 0.01 | — |
| 70 | 0.0813 | 0.500 | 2.81 | — |
| 80 | 0.0450 | 0.550 | 2.31 | — |
| 90 | 0.0650 | 0.475 | 2.14 | crashed |

**边缘 collapse / 停滞。** frac_zero_std 在 0.45-0.68 振荡，reward 停滞在 0.04-0.10 无上升趋势。

### 当前排序（step 30 快照）

| Rank | Run | Reward@30 | Frac_zero_std@30 | Collapse? |
|------|-----|-----------|-------------------|-----------|
| 1 | cka_only_20 | 0.250 | 0.200 | No |
| 2 | random_20 | 0.166 | 0.325 | No |
| 3 | standard_v8 (stage2) | 0.065 | 0.525 | Borderline |
| 4 | rasp_v9 (stage2) | 0.021 | 0.950 | Yes |

### 关键发现

1. **cka_only 显著优于 random**：reward 高 50%，frac_zero_std 低 38%。CKA 保留的结构对 GRPO 训练有明显正面影响。

2. **两个新 run 都远好于 stage2 对照组**，但注意 stage2 run 是在已 GRPO 过的模型上再训，不是直接 apples-to-apples 对比。

3. **Delayed collapse 尚无法判断**——step 30 的数据不足以排除 step 50-80 区间的 delayed collapse。需要等 step 40+ 数据。

4. **grad_norm 警示信号**：random_20 在 step 20 出现 8.62 的 spike（cka_only 最高仅 1.89），这可能是 delayed collapse 的前兆。

### 下一步

- 等 ~2h 后再查，届时 random_20 应到 step 50+、cka_only_20 应到 step 40+
- step 40 的 metric log 将提供关键的中期趋势数据
- 如果 random_20 在 step 40-50 出现 frac_zero_std 上升趋势 (>0.4)，即为 delayed collapse 信号
