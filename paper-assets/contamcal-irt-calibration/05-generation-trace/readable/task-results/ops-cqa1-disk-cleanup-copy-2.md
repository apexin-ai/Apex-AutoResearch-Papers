# ops cqa1 disk cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-disk-cleanup_20260523T031533_result.json`
- **Structured JSON:** [`85ee092da498188d88c1.json`](../../sessions/85/85ee092da498188d88c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 报告

| | 值 |
|---|---|
| **清理前** | 159G / 169G = **95%** |
| **清理后** | 141G / 169G = **83%** |
| **释放空间** | **18G** |

**删除内容：**
- `.hf_cache/Yi-1.5-9B/` — 17G（无引用的 Yi 基模）
- `alfworld_data/` — 2.2G（无关数据集）
- `swe_smith_metadata*.jsonl` — 35M（无关数据）

磁盘使用率 83%，已低于 85% 目标。运行中的 Falcon3 volume_control 训练不受影响。

---
