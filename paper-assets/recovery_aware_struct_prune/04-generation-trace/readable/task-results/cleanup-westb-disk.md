# cleanup westb disk

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_westb_disk_20260521T223801_result.json`
- **Structured JSON:** [`1dffdde68c52a44927cc.json`](../../sessions/1d/1dffdde68c52a44927cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成

| 操作 | 释放空间 |
|------|---------|
| 删 `sft_qwen_math_cka_only_20/`（训练 checkpoint，final 在 `_final`） | ~12G |
| 删 `sft_standard_20_qwen_math/`（训练 checkpoint，final 在 `_final`） | ~12G |
| 清理 `__pycache__`、`*.pyc`、空 `tmp_build/` | ~0 |
| **合计** | **~23G** |

**清理前**: 14G 可用 (95%)  
**清理后**: 37G 可用 (86%)

目标达成，MATH-500 eval 有足够磁盘空间运行。

---
