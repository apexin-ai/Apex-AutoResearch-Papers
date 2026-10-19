# ops check m1 reextract v2 status

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-m1-reextract-v2-status_20260515T164919_result.json`
- **Structured JSON:** [`807265b3ca020c94226f.json`](../../sessions/80/807265b3ca020c94226f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## m1_reextract_v2 状态

**仍在运行**，未完成。

| 指标 | 值 |
|------|------|
| all.jsonl | 44,173 行（未变，需 combine） |
| JSON 文件总数 | 43,749 |
| repos 完成 | 80/82 |
| 剩余实例 | 416 |

**未完成 repos:**
- **getmoto/moto**: 180/536 (33.6%) — call_graph.ql 每个实例超时 ~5min
- **Project-MONAI/MONAI**: 464/524 (88.5%) — 接近完成

**提取速率**: ~28 files/hour → **新 ETA: 2026-05-16 15:00 CST**（比原 ETA 晚，主因 moto 的 CodeQL 超时拖慢速度）

---
