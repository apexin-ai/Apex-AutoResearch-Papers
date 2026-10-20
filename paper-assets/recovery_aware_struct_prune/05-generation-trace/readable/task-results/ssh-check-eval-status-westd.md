# ssh check eval status westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_eval_status_westd_20260521T050307_result.json`
- **Structured JSON:** [`b7e2dabeec8dab511955.json`](../../sessions/b7/b7e2dabeec8dab511955.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在跑：

| 实验 | GPU | 进度 | 当前 acc | 速度 | 预计剩余 |
|------|-----|------|---------|------|---------|
| **CKA-only 25% v3** | cuda:0 (99%, 28GB) | 2/1319 (~0%) | — | ~9.5s/it | 刚启动，~3.5h |
| **Random 20% v2** | cuda:1 (93%, 12.6GB) | 136/1319 (~10%) | 0.54 @100 | ~3.7s/it | ~1.2h |

Random 20% 在前 100 样本 acc=54.0%，跑得比 CKA 快不少（模型更小，占显存也少一半）。

---
