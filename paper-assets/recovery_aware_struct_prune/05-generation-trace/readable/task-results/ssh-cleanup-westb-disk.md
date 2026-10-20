# ssh cleanup westb disk

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup_westb_disk_20260520T205901_result.json`
- **Structured JSON:** [`47489f2bc51a77250588.json`](../../sessions/47/47489f2bc51a77250588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

目标达成。

## 清理结果

| 操作 | 释放空间 |
|------|---------|
| pip cache purge | ~2 files |
| conda clean --all | ~107 MB |
| __pycache__ 清理 | 小量 |
| **删除 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`** | **~15G** |

**清理前**: 241G / 250G（97%，9.8G 可用）
**清理后**: 227G / 250G（91%，24G 可用）

`Qwen2.5-Math-7B`（15G）也是可删除的候选（同样是已完成实验的基础模型，可重新下载），如果后续需要更多空间可以继续清理。

---
