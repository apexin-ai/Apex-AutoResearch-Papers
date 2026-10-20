# ssh data prep resume

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_data-prep-resume_20260515T180618_result.json`
- **Structured JSON:** [`cb0d1e0a2723f5110244.json`](../../sessions/cb/cb0d1e0a2723f5110244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 数据状态报告

| 文件 | 行数 | 大小 | Token 数 | 状态 |
|------|------|------|----------|------|
| `probe_set.jsonl` | 5,000 | 5.8 MB | 1,280,000 (每条 256) | ✓ |
| `val_set.jsonl` | 14,881 | 44 MB | 10,002,013 (10.0M) | ✓ |
| `real_pool.jsonl` | 579,255 | 1.7 GB | 400,000,299 (400.0M) | ✓ |

- 格式：每行一个 JSON，含 `text` 字段（probe_set 额外有 `token_count`）
- 数据来源互不交集：probe+val 来自 `014_00000.parquet`，real_pool 来自 `000_00000.parquet`
- Token 计数使用 Pythia tokenizer 实际编码验证，与生成脚本一致

**数据完整就绪，可进入下一步实验。**

---
