# ssh d064 progress check r2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_progress_check_r2_20260519T193956_result.json`
- **Structured JSON:** [`4f402e12f7d15955fb00.json`](../../sessions/4f/4f402e12f7d15955fb00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。摘要：

**已完成 (4/8):**
- Llama greedy unc ✅, greedy con ✅ (21461)
- Qwen beam-4 unc ✅ (21461)
- Llama beam-4 unc ✅ (16980)

**运行中 (3):**
- 16980 GPU1: Llama beam-4 con **901/998 (90%)** → ETA ~04:16 CST（~30min）
- 21461 GPU1: Qwen beam-4 con **667/998 (67%)** → ETA ~05:58 CST（~2h16m）
- 21461 GPU0: Llama beam-4 unc **164/998 (16%)** → ETA ~07:43 CST（cascade 中）

**待运行 (1):**
- 21461 GPU0: Llama beam-4 con（cascade 排队，ETA ~13:30 CST，但 16980 有并行副本快完成）

**⚠️ 需要关注:**
1. **16980 GPU0 已空闲**，无 cascade 脚本。Option C（w5 checkpoint greedy）需手动启动。
2. 16980 GPU1 ~30min 后也将空闲，同样无后续自动任务。
3. 实际瓶颈是 21461 GPU1 的 Qwen beam-4 con（唯一无并行副本），预计 ~06:00 CST 完成。

---
