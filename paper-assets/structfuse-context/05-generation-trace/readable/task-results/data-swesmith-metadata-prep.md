# data swesmith metadata prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_swesmith_metadata_prep_20260512T123337_result.json`
- **Structured JSON:** [`6461b0c4a4be0e877d5c.json`](../../sessions/64/6461b0c4a4be0e877d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

### 产出

1. **`/root/autodl-tmp/swe_smith_metadata.jsonl`** — 59,136 条 metadata（27.2MB）
2. **`/root/structfuse/extraction/batch_extract.py`** — 全量 CodeQL batch 提取脚本

### Metadata 统计

| 指标 | 值 |
|------|------|
| Total instances | 59,136 |
| Unique GitHub repos | 222 |
| Unique (repo, commit) pairs | 222 |
| Avg instances per group | 266.4 |
| Has buggy_file | 100% |
| Has buggy_function | 84.4% |
| Python-only instances | 50,869 (86%) |
| Mean patch size | 1,647 chars |
| Top repo | scanny/python-pptx (2,389) |

### batch_extract.py 关键优化

**CodeQL DB 复用**：59,136 个 instance 共享 222 个 (repo, commit) 对，DB 只需创建 222 次而非 59K 次。脚本按 repo group 组织，clone 一次、建 DB 一次、所有同组 instance 共享。

其他特性：`--python-only` 过滤、断点续传（跳过已完成 instance）、skip log、`--max-instances` 限制。

### 耗时预估

| 配置 | 预估时间 |
|------|----------|
| 全量 serial | ~500h |
| 4 workers | ~125h |
| 8 workers | ~63h |
| Python-only + 8 workers | ~54h |

---
