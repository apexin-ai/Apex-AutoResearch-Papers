# ssh harvest all westd evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_all_westd_evals_20260520T181211_result.json`
- **Structured JSON:** [`7b8a419801249bd2199f.json`](../../sessions/7b/7b8a419801249bd2199f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部仍在运行，尚无结果文件输出。

| Eval | GPU | PID | 进度 | 中期 Accuracy | 预计剩余 |
|------|-----|-----|------|--------------|---------|
| **CKA-only 15% SFT** | cuda:1 | 262728 | 1180/1319 (89%) | **72.52%** @1150 | ~7 min |
| **CKA-only 20% SFT** | cuda:2 | 264522 | 932/1319 (71%) | **63.11%** @900 | ~19 min |
| **Standard 20% SFT** | cuda:0 | 266847 | 425/1319 (32%) | **61.50%** @400 | ~44 min |

CKA-only 15% 没完成，但即将结束（~89%），中期准确率 72.52%。CKA-only 20% 和 Standard 20% 分别在 71% 和 32% 进度。

---
