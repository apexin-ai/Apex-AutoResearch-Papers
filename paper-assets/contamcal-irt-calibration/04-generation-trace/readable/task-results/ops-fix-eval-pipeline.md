# ops fix eval pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-eval-pipeline_20260518T115047_result.json`
- **Structured JSON:** [`d5bed7c636b2b02abeeb.json`](../../sessions/d5/d5bed7c636b2b02abeeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总：

**数据集预缓存** — 全部成功
| 数据集 | Split | 数量 |
|--------|-------|------|
| GSM8K | test/train | 1,319 / 7,473 |
| MMLU | test/val | 14,042 / 1,531 |
| ARC-Challenge | test/val | 1,172 / 299 |

**GSM8K Eval** — 运行中
- PID 25326, GPU 1, 17.7GB VRAM, ~7.8s/item
- 预计完成时间：约 2.8 小时（1319 items × 7.8s）

**14B 模型下载** — 仍有 1 个 incomplete 文件，已下载 7 个 safetensors shard。

---
