# analysis wandb training progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wandb-training-progress_20260514T212522_result.json`
- **Structured JSON:** [`81878f35e3b6a6c6e8c6.json`](../../sessions/81/81878f35e3b6a6c6e8c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。汇总如下：

---

## 训练状态汇总

### P0 — `grpo_ced_lr5e6_r1` (纯 CED reward)
**进度**: step 56/200 (28%)，运行 ~1h46m

| Step | Reward | CED | F1 | Format | KL | Loss | Reward Std |
|------|--------|-----|-----|--------|-----|------|------------|
| 5 | 0.087 | 0.011 | 0.019 | 0.057 | **2.4e9** | **23.8M** | 0.139 |
| 10 | 0.068 | 0.000 | 0.000 | 0.068 | 0.002 | -0.002 | 0.110 |
| 15 | 0.155 | 0.004 | 0.011 | 0.141 | 0.002 | 0.048 | 0.167 |
| 20 | 0.101 | 0.000 | 0.000 | 0.101 | 1.37 | 0.046 | 0.121 |
| 25 | 0.176 | 0.000 | 0.000 | 0.176 | 0.004 | 0.029 | 0.137 |
| 30 | 0.131 | 0.002 | 0.002 | 0.128 | **7.0e13** | **988B** | 0.140 |
| 35 | 0.194 | 0.015 | 0.010 | 0.168 | 0.157 | 0.053 | 0.188 |
| **40** | **0.318** | **0.079** | **0.038** | **0.201** | 0.006 | 0.023 | **0.345** |

**趋势**: 上升 ↑ — step 40 出现显著突破，CED 从 ~0 跳到 0.079，F1 也达 0.038

### P0+P1 — `grpo_ced_lr5e6_rp_r2` (CED + recall_penalty)
**进度**: step 37/200 (18%)，运行 ~1h20m

| Step | Reward | CED | F1 | Format | KL | Loss |Reward Std |
|------|--------|-----|-----|--------|-----|------|------------|
| 5 | 0.099 | 0.005 | 0.021 | 0.073 | **3.9e10** | **434M** | 0.145 |
| 10 | 0.093 | 0.000 | 0.000 | 0.093 | **6.9e4** | **908** | 0.123 |
| 15 | 0.149 | 0.000 | 0.003 | 0.146 | **1.9e6** | **24650** | 0.143 |
| 20 | 0.147 | 0.001 | 0.002 | 0.145 | **1.4e9** | **13.4M** | 0.141 |

**趋势**: 平稳/微升 → — CED 和 F1 基本为零，格式 reward 主导

---

## 关键发现

**1. Reward 信号（lr=5e-6 验证）**
- P0 ✅ **有效**。Step 35-40 出现 reward 拐点，CED 从 ~0 突升至 0.079，说明模型开始学到有意义的抽取。总 reward 从 0.087 增长到 0.318（3.7x）。
- P0+P1 ⚠️ **尚未起效**。Step 20 时 CED/F1 仍近零，reward 全靠格式分。可能落后 P0 约 15-20 步，需继续观察。

**2. KL 稳定性 — 严重分化**
- P0: 有两次 KL spike（step 5 和 30），但**迅速恢复**（step 35 回到 0.16，step 40 回到 0.006）。
- P0+P1: **每个 step 的 KL 都异常高**（1e4 ~ 1e10），从未恢复到正常水平。Loss 也持续飙高（908 ~ 13M）。recall_penalty 可能造成了持续的梯度不稳定。

**3. Mode Collapse 检测**
- P0: reward_std 从 0.11 **上升**到 0.35，`frac_reward_zero_std` 从 0.1 升至 0.3 — 多样性增加，**无 collapse 迹象**。
- P0+P1: reward_std 稳定在 0.12-0.15，无明显 collapse，但也没有探索到新行为。

**4. Completion 长度**
- P0: mean_length 从 878 下降至 714，clipped_ratio 从 54% 降至 24% — 模型在学习更简洁的输出。

**5. recall_penalty 未体现在日志中**
- P0+P1 的 reward 组件只有 format/f1/ced 三项，没有 recall_penalty 的独立指标。需要确认 recall_penalty 是否正确生效。

---

## 建议关注点
- **P0 是目前更有希望的 run**，step 40 之后的指标（step 45-55 尚未刷出日志）将是关键确认点。
- **P0+P1 的 KL 持续不稳定是最大风险**。如果到 step 40 仍无改善，可能需要降低 recall_penalty 权重或停止该 run。

---
