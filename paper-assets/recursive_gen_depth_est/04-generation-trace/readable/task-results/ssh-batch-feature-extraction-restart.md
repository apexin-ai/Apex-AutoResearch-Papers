# ssh batch feature extraction restart

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_batch_feature_extraction_restart_20260515T035255_result.json`
- **Structured JSON:** [`1f1a90a0ff8fd705f312.json`](../../sessions/1f/1f1a90a0ff8fd705f312.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**batch_feature_extraction_5cells 已全部完成，无需重启。**

| Cell | 行数 | 状态 |
|------|------|------|
| gpt2xl_topk50 | 20,000 | 完成 |
| gpt2xl_temp09 | 20,000 | 完成 |
| olmo_topk50 | 20,000 | 完成 |
| olmo_temp09 | 20,000 | 完成 |
| pythia_topk50 | 20,000 | 完成 |

- 总计 100,000 行，每个 cell 20,000 samples × 19 features
- 输出路径：`results/{cell}/features.jsonl`
- Registry 已更新为 DONE/success
- cuda:0 当前空闲，可用于下游分类任务

---
