# analysis wandb extract flatnli metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wandb-extract-flatnli-metrics_20260514T171801_result.json`
- **Structured JSON:** [`e1cd3ecab8d0cca5172c.json`](../../sessions/e1/e1cd3ecab8d0cca5172c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从 checkpoint 的 trainer_state.json 获取到了全部数据。

---

## extract_r4 (Stage 1, extraction-only) — Steps 5–20

| Step | reward | reward_std | frac_zero_std | f1_reward | format_reward | kl | grad_norm | loss | entropy | mean_length |
|------|--------|-----------|--------------|-----------|--------------|-----|----------|------|---------|-------------|
| 5 | 0.187 | 0.133 | 0.20 | 0.016 | 0.170 | 0.013 | 0.297 | 0.046 | 0.071 | 757 |
| 10 | 0.282 | 0.039 | 0.70 | 0.000 | 0.282 | 0.044 | 0.005 | 0.025 | 0.046 | 516 |
| 15 | 0.287 | 0.035 | 0.80 | 0.000 | 0.287 | 0.089 | 0.012 | -0.001 | 0.059 | 464 |
| 20 | 0.293 | 0.027 | 0.80 | 0.000 | 0.293 | 0.093 | 0.198 | 0.030 | 0.069 | 457 |

**健康判断: 不健康 — mode collapse**
- `frac_zero_std` 从 0.2 快速升至 0.8，说明 80% 的 prompt 上所有 generation 得到相同 reward
- `f1_reward` 从 step 10 起持续为 0 — 模型完全没有学到 extraction 能力
- reward 几乎全部来自 `format_reward`（~0.29 ≈ format 满分 0.3）
- KL 偏高 (0.093 at step 20)，增速快于 ced_kl001_r4 同期

**与 ced_kl001_r4 同期对比 (step 5-10):**
- reward: extract_r4 (0.187→0.282) vs ced (0.222→0.253) — 表面相近但 extract_r4 的 reward 几乎全是 format 分
- KL: 0.013→0.044 vs 0.014→0.045 — 几乎一致
- frac_zero_std: 0.2→0.7 vs 0.3→0.8 — 相近，都偏高
- **关键差异**: extract_r4 没有 ced_reward 引导，f1_reward 在 step 10 已归零

---

## flatnli_r5 (Stage 2, flat-NLI reward) — Steps 5–120

注：steps 5–100 继承自 checkpoint-100（之前的 flatnli_r3 训练），steps 105–120 是 r5 新训练的部分。

### 前期 (r3 继承，steps 5–100，无 KL 日志)

| Step | reward | frac_zero_std | f1_reward | flat_nli | format | mean_length |
|------|--------|--------------|-----------|----------|--------|-------------|
| 5 | 0.498 | 0.20 | 0.079 | 0.261 | 0.158 | 692 |
| 10 | 0.725 | 0.05 | 0.040 | 0.442 | 0.243 | 712 |
| 15 | 0.888 | 0.00 | 0.110 | 0.485 | 0.293 | 431 |
| 20 | 1.260 | 0.00 | 0.374 | 0.593 | 0.293 | 419 |
| 50 | 1.314 | 0.00 | 0.108 | 0.906 | 0.300 | 507 |
| 100 | 1.236 | 0.00 | 0.025 | 0.911 | 0.300 | 376 |

### r5 新训练 (steps 105–120，从 checkpoint-100 恢复)

| Step | reward | frac_zero_std | f1_reward | flat_nli | format | kl | grad_norm | loss | entropy | mean_length |
|------|--------|--------------|-----------|----------|--------|----|----------|------|---------|-------------|
| 105 | 0.363 | **0.90** | 0.020 | 0.043 | 0.300 | **0.485** | 0.059 | -0.005 | 0.039 | 264 |
| 110 | 1.082 | 0.70 | 0.533 | 0.249 | 0.300 | 0.435 | 0.313 | -0.002 | 0.024 | 205 |
| 115 | 0.913 | 0.50 | 0.185 | 0.427 | 0.300 | 0.458 | 0.787 | 0.014 | 0.030 | 248 |
| 120 | 0.560 | **0.80** | 0.089 | 0.171 | 0.300 | **0.456** | 0.733 | 0.002 | 0.031 | 225 |

**健康判断: 严重异常**
- **KL 灾难性高**: 0.45–0.49，比 ced_kl001_r4 同期 (0.014–0.045) 高 10 倍
- `frac_zero_std` 剧烈波动 (0.5–0.9)，说明训练极不稳定
- `flat_nli_reward` 从 checkpoint-100 的 0.911 暴跌至 0.043–0.427 — 恢复训练后能力严重退化
- `f1_reward` 也大幅波动
- completion 长度急剧缩短 (376→205–264)，可能出现 degenerate output

**根因推测**: 从 checkpoint-100 恢复时，模型参数已经偏离 reference policy 很远（KL 初始就是 ~0.48），新的 training 在此基础上进一步恶化。这说明 r3 的训练可能在后期已经出现了 KL 漂移但因缺少 KL 日志未被发现。

---

## 总结

| 实验 | 状态 | 主要问题 |
|------|------|---------|
| **extract_r4** | Mode collapse | f1_reward=0, 只学会了 format; frac_zero_std=0.8 |
| **flatnli_r5** | KL 爆炸 + 能力退化 | KL~0.46 (正常<0.1), flat_nli 从 0.91 跌至 0.17 |
| ced_kl001_r4 (参照) | 相对健康 | reward 稳步上升，KL 可控 |

**D020 配置 (kl_coef=0.01, num_gen=8) 对 ced reward type 有效，但对 extract-only 和 flat-NLI 两种 reward type 均失败。** extract_r4 缺少 ced_reward 导致模型没有 extraction 学习信号；flatnli_r5 的 checkpoint-100 已有严重 KL 漂移，恢复训练使问题加剧。

---
