# ops sync and integration test

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_and_integration_test_20260519T042455_result.json`
- **Structured JSON:** [`aca1bf09e8701019f331.json`](../../sessions/ac/aca1bf09e8701019f331.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

### 1. 同步验证

| 文件 | 行数 | MD5 |
|---|---|---|
| `turn_utils.py` | 237 | `f8929e61...` |
| `train_phase2.py` | 373 | `0f08186a...` |
| `eval_phase2_gar.py` | 529 | `ee3e4e65...` |
| `test_turn_utils.py` | 421 | `b48acdf7...` |

### 2. Integration Test (真实 tokenizer) — 2/2 passed

**Qwen2.5-7B-Instruct (chatml)**:
- 5 turns detected, roles: `[system, user, assistant, user, assistant]`
- Seq len: 69, Goal tokens (ours): 11, Goal tokens (dongre): 6
- Assistant last token positions: `[38, 66]`
- Boundary positions: 10

**Llama-3.1-8B-Instruct (llama3)**:
- 5 turns detected, roles: `[system, user, assistant, user, assistant]`
- Seq len: 91, Goal tokens (ours): 33, Goal tokens (dongre): 27
- Assistant last token positions: `[61, 89]`
- Boundary positions: 10

### 3. Unit Test (mock-based) — 27/27 passed

所有 27 个测试用例全部通过，0 failures。

---
