# verify exp028c step2 metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp028c_step2_metrics_20260516T000125_result.json`
- **Structured JSON:** [`7968f0278aa38f88ee66.json`](../../sessions/79/7968f0278aa38f88ee66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是交叉验证结果。

---

## exp028c step_2_train 三方交叉验证报告

### 1. Step:2 是否已在日志中出现

**否。** 日志中仅有 2 行 `step:` 记录：
- `step:0` (line 14327) — val before train
- `step:1` (line 14329) — 第一个训练步

日志最后修改时间 `07:50:59 CST`，末尾全是 step 2 rollout 阶段的 "Skipping non-numeric metric 'anchor_obs'" 警告。进程仍在运行（PID 824675, elapsed 2h25m; TaskRunner PID 827923 alive）。Step 2 rollout 正在进行中，summary 行尚未输出。

### 2. 三方对比表

#### Step 1（三源均有数据）

| 指标 | Registry | 日志 (line 14329) | W&B (step 1) | 一致性 |
|------|----------|-------------------|--------------|--------|
| success | 13.3% | 13.28% | 13.28% | **一致**（registry 四舍五入） |
| pass@8 | 37.5% | 37.5% | 37.5% | **一致** |
| action_is_valid | 76.4% | 76.43% | 76.43% | **一致** |
| action_is_effective | 96.4% | 96.37% | 96.37% | **一致** |
| entropy | 0.263 | 0.2634 | 0.2634 | **一致** |
| kl_loss | 0.013 | 0.01280 | 0.01280 | **一致** |
| pg_loss | 0.008 | 0.00828 | 0.00828 | **一致** |
| grad_norm | 16.9 | 16.88 | 16.88 | **一致** |
| num_actions | 45.6 | 45.61 | 45.61 | **一致** |
| response_length | 700.6 | 700.58 (token mean) | 55.33 (metric) | **一致**（registry 用 token-level mean） |

#### Step 2

| 指标 | Registry | 日志 | W&B | 一致性 |
|------|----------|------|------|--------|
| success | 6.25% | **不存在** | **不存在** | **无法验证** |
| pass@8 | 25% | — | — | **无法验证** |
| action_is_valid | 83.2% | — | — | **无法验证** |
| kl_loss | 0.171 | — | — | **无法验证** |
| entropy | 0.247 | — | — | **无法验证** |
| pg_loss | 0.007 | — | — | **无法验证** |
| grad_norm | 17.3 | — | — | **无法验证** |

### 3. 数据一致性结论

- **Step 1: 完全一致。** 三方数据在精度允许范围内完全对齐。
- **Step 2: Registry 数据无法验证。** 日志和 W&B 均只有 step 1 数据。Registry 中的 step_2_train 数据来源不明——可能是之前 Worker 从 W&B streaming API 或中间状态提前提取的，但截至现在 W&B history 正式接口中没有 step 2 记录。

**结论：Registry step_2_train 数据可信度存疑，需等 step 2 完成后重新验证。** 训练进程正在运行，step 2 rollout 收集中，预计还需 30-40 分钟（参考 step 1 耗时 ~54 分钟）。

### 4. 关于 success 下降的初步分析（待验证前提下）

如果 registry 中的 step_2_train 数据最终被确认：

- **KL 从 0.013→0.171（13x 跳升）**：策略偏离 reference policy 过快。`kl_loss_coef=0.01` 可能不足以约束。但 KL 惩罚会抑制 exploration，使模型退回 safe 但无效的行为。
- **Entropy 0.263→0.247（-6%）**：轻微下降，尚未到 collapse 水平，但趋势需监控。
- **action_is_valid 76.4%→83.2%（+6.8pp）**：模型学会了产出更多 valid actions，但 success 反而下降——说明"格式正确 ≠ 任务完成"，可能是 reward shaping 中 invalid_action_penalty 的信号过强，模型优先优化 valid actions 而非 task completion。
- **与 exp027 对比**：exp027 step 1→2 同样有 35.9%→10.16% 的暴跌，KL 从 0.058→0.413（也是 7x 跳升）。**这是 GRPO 训练初期的常见模式**——第一步策略大幅偏移，第二步 KL 惩罚回弹导致 success 骤降。exp027 在 step 3-4 稳定在 ~10-13%。
- **建议**：**继续观察到 step 5**。如果 success 在 step 3-5 回升到 ≥10%，说明是正常波动；如果持续 ≤6%，考虑降低 `kl_loss_coef` 或增大 `entropy_coeff`。

---
