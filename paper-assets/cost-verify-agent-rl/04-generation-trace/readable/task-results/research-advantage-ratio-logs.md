# research advantage ratio logs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_advantage_ratio_logs_20260524T232729_result.json`
- **Structured JSON:** [`027253efac86ceef8adb.json`](../../sessions/02/027253efac86ceef8adb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Here's the assessment:

---

## 结果汇报

### 1. 日志中是否有 advantage 分布数据？

**有。** `/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl`

- 3000 条记录，每条包含：`episode_id`, `window_position`, `step_return`, `advantage`, `uid`
- 代码中 `_n = min(len(advantages), 200)` 限制每步最多记录 200 条，3000 / 200 = **恰好 15 个 training step**
- **无 `training_step` 字段**，但可从顺序位置推断：records 0-199 = step 1, 200-399 = step 2, ..., 2800-2999 = step 15
- 这是 ALFWorld h=2 step-level 的数据（即 Cell A）

### 2. 是否有现成的 advantage 分析脚本？

有两个：`scripts/analyze_advantage_log.py` 和 `scripts/analyze_advantage_log_v2.py`。但它们分析的是 sign-vs-outcome 和 position decay，**未按 training step 拆分**，也**未计算 |Â_correct|/|Â_wrong| ratio**。

已有的 `artifacts/advantage_analysis_summary.json` 是全步聚合结果，不含 per-step breakdown。

### 3. Checkpoint 可用性

bjb1-17606 上**无 Cell A checkpoint**（有 `hsweep-h10-seed2` 但无 `hsweep-h2-seed2`）。不过不需要 checkpoint，日志数据已够用。

### 4. 可行性评估

**可以直接从现有日志提取，无需重跑。** 方法：

- 按每 200 条切分为 15 个 training step
- 每个 step 内，按 `step_return > 0`（correct）vs `step_return ≤ 0`（wrong）分组
- 计算 `mean(|advantage|_correct) / mean(|advantage|_wrong)`
- 取 step 1, 5, 10, 15 四个时间点

**局限**：
- 仅 1 个 seed（seed2），无 error bar
- 仅 ALFWorld，无 ScienceWorld Cell A 数据（config 存在但未跑 `LOG_PER_SAMPLE_ADV=1`）
- 每步仅 200 条（实际 batch 可能更大，部分数据被截断）

---
