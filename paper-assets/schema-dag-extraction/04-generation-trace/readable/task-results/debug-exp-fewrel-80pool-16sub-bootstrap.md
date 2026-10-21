# debug exp fewrel 80pool 16sub bootstrap

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp_fewrel_80pool_16sub_bootstrap_20260516T021106_result.json`
- **Structured JSON:** [`69e5c91c77b8ca99e080.json`](../../sessions/69/69e5c91c77b8ca99e080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已完成，无需启动。** 诊断结果：

- **extract 阶段**：100/100 batches 全部完成（batch_000 到 batch_099），predictions_incremental.jsonl 有 9600 行，results_incremental.jsonl 有 100 行
- **analyze 阶段**：bootstrap_ci.json 已生成，包含完整统计结果
- **GPU 空闲**是因为任务已跑完退出，不是从未启动

关键结果摘要（bootstrap_ci.json）：

| 指标 | 值 |
|------|-----|
| mean_accuracy | 80.77% |
| mean_bcs | 0.557 |
| Δ_BCS (low−high) | −3.92pp, CI [−7.79, +0.42] |
| Pearson(BCS, acc) | −0.221, p=0.027 |
| Regression slope | −0.401, CI [−0.684, −0.062] |

注意：Δ_BCS 的 95% CI 跨越 0（上界 +0.42），说明 16-sub 条件下 BCS 对 accuracy 的影响在统计上不显著（与 C002 约束一致——BCS amplification 在小 pool 下较弱）。回归斜率 CI 不含 0，方向性趋势存在但效应量小。

---
