# ops status snapshot 0516c

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-snapshot-0516c_20260515T181527_result.json`
- **Structured JSON:** [`f29dfad6039ddbe8c660.json`](../../sessions/f2/f29dfad6039ddbe8c660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## 状态快照 — 2026-05-16 02:30 UTC

### Watchers

| PID | 状态 | 运行时长 | 脚本 |
|-----|------|---------|------|
| 966920 | **ALIVE** | 1d 2h 42m | `watch_and_chain_qwen_s42.sh` |
| 20226 | **ALIVE** | 2h 16m | `watch_and_chain_starcoder_s42.sh` |

### Qwen cuda:0 (`m2_full_qwen_continued`)

| subrun | 状态 | best val_loss | best R@1 | early stop | final R@1 |
|--------|------|--------------|----------|-----------|-----------|
| random_s43 | DONE | 0.4476 | 0.5554 | step 1500 | 0.5501 |
| random_s44 | DONE | 0.4252 | **0.6009** | step 1500 | 0.5542 |
| embed_dist_s43 | DONE | 0.4541 | 0.5606 | step 1500 | 0.5655 |
| embed_dist_s44 | DONE | 0.4341 | 0.5942 | step 2000 | 0.5470 |
| **dataflow_s43** | **RUNNING** | 0.4617 | 0.5495 | — | — |
| dataflow_s44 | PENDING | — | — | — | — |
| bm25_s42 | PENDING | — | — | — | — |

- PID 18427, step ~550/2810 (epoch 1/2), VRAM 50992 MiB, ~230 steps/h
- eval@500: val_loss=0.4617, R@1=0.5495, R@5=0.9728
- **ETA dataflow_s43**: ~May 16 12:00 CST | **ETA 全链完成**: ~May 17 14:00-18:00 CST

### StarCoder cuda:1 (`m2_full_starcoder_resumed`)

| subrun | 状态 | best val_loss | best R@1 | early stop | final R@1 |
|--------|------|--------------|----------|-----------|-----------|
| random_s42 | DONE | 0.6134 | 0.4604 | — (3 epoch) | — |
| random_s43 | DONE | 0.5239 | 0.4912 | step 2500 | 0.4859 |
| random_s44 | DONE | 0.5913 | 0.4897 | step 1500 | 0.4897 |
| **embed_dist_s42** | **RUNNING** | — | — | — | — |
| embed_dist_s43 | PENDING | — | — | — | — |
| embed_dist_s44 | PENDING | — | — | — | — |
| dataflow_s42–s44 | PENDING | — | — | — | — |

- PID 38016, step ~200/4242 (epoch 1/3, 3 epochs), VRAM 54478 MiB, ~200 steps/h
- **ETA embed_dist_s42**: ~May 17 00:00 CST | **ETA 全链完成**: ~May 19-20 CST

### m1_reextract_v2

- MONAI 和 moto 均有大量已生产的 JSON 文件（从 `-newer` 查询可见持续输出）
- codeql DB 已建成：`Project-MONAI__MONAI_codeql_db`, `getmoto__moto_codeql_db`
- 上次检查：80/82 repos done，剩余 MONAI (~91.8%) 和 moto (~35.8%，call_graph 100% timeout)
- **ETA**: ~May 16 10:00-12:00 CST（可能已完成或接近完成）

### 磁盘

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root | 30G | 11G | 20G | 34% |
| /root/autodl-tmp | 250G | 171G | 80G | 69% |

---
