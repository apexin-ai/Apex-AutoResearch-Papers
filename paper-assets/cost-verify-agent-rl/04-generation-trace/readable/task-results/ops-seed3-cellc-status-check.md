# ops seed3 cellc status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed3-cellc-status-check_20260520T225028_result.json`
- **Structured JSON:** [`e6ecd0779d645cc71d25.json`](../../sessions/e6/e6ecd0779d645cc71d25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### seed3_v2 (exp029)
- **状态：仍在运行** (PID 991448 存活)
- **进度：93% (14/15 steps)**，已运行 5h03m，ETA **~22 分钟**
- **Step 14 指标：** train success = **38.28%**, pass@8 = **93.75%**（从 step 1 的 13.28% 持续上升）
- **Checkpoints：** global_step_5, global_step_10 — **无 global_step_15**
- global_step_15 将在最后一步完成后保存

### Cell C v3 (ScienceWorld)
- **状态：仍在运行** (PID 88226 存活)
- **进度：13% (2/15 steps)**，已运行 4h25m，每步 ~2-3h，极慢
- **Step 0 初始 val：** success = **0.0%**, score = 2.71, final_score = 5.0
- 尚未到 step 5，无法查看 step 5 val metrics
- W&B run `ghswaew5` 查询失败（entity 解析问题），但日志中已有完整指标

### OOD eval
**未启动。** seed3_v2 还剩最后 1 步（~22 分钟），global_step_15 尚未生成。建议 **~30 分钟后再检查**，届时应已完成并可立即启动 OOD eval。

---
