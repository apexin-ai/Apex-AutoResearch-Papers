# diagnose d112 shard0 exit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d112_shard0_exit_20260519T020829_result.json`
- **Structured JSON:** [`e2c4ee616a7fc2be3e54.json`](../../sessions/e2/e2c4ee616a7fc2be3e54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**Shard 0: 正常完成，非 crash。** 6048 行 = 756 docs × 8 generations，全部生成完毕后进程正常退出。

### 4 Shard 进度概览

| Shard | GPU | Lines | Docs Done | Status |
|-------|-----|-------|-----------|--------|
| 0 | cuda:3 | 6048 | 756/756 | **DONE** |
| 1 | (running) | 4384 | 548 | Running |
| 2 | (running) | 4800 | 600 | Running |
| 3 | (running) | 3824 | 478 | Running |

GPU 0/1/2 各有 python 进程活跃（17-19 GiB），shard 1/2/3 仍在生成中。cuda:3 已空闲。

---
