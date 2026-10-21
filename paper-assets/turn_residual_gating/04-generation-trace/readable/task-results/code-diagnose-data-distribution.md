# code diagnose data distribution

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diagnose_data_distribution_20260518T111440_result.json`
- **Structured JSON:** [`d42fb2b70d5454d440f9.json`](../../sessions/d4/d42fb2b70d5454d440f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：数据排除。** 截断后 mean=5.58 assistant turns/sample，100% 样本可触发 GAR loss。L_GAR=0 的根因在 GAR loss 计算或梯度传播路径，不在数据 turn 数不足。

---
