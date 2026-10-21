# ssh harvest cka only 15 seed123 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_cka_only_15_seed123_v2_20260521T001619_result.json`
- **Structured JSON:** [`627d775afb7a5677a3f8.json`](../../sessions/62/627d775afb7a5677a3f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job（可能已在之前的 session 中创建，当前 session 无法访问）。

**结果汇总：**

| Metric | Value |
|--------|-------|
| Accuracy | **73.09%** (964/1319) |
| Stderr | ±1.22% |
| EOS rate | 98.79% |
| Truncated | 16/1319 |

**CKA-only 15% 三 seed 对比：**

| Seed | Accuracy |
|------|----------|
| seed42 | 73.09% |
| seed123 | **73.09%** |
| seed456 | 72.10% |
| **Mean** | **72.76% ± 0.57%** |

seed123 完美复现了 seed42 的结果，三 seed 方差极小（σ=0.57pp），CKA-only 15% 的优势非常稳定。Registry 已更新为 DONE/success。

---
