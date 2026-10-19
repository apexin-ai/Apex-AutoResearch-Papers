# check training status loop9

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-status-loop9_20260515T010840_result.json`
- **Structured JSON:** [`f4b92114cae9f2f9d56c.json`](../../sessions/f4/f4b92114cae9f2f9d56c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 全部进程正常，无异常

### m2_full_qwen_continued (cuda:0) ✅ ALIVE
| 指标 | 值 |
|------|-----|
| 当前 subrun | embedding_distance_s43 (3/9) |
| 进度 | step 150/2810 (~5%)，刚开始 |
| 已完成 | random_s42 (R@1=0.5527), random_s43 (R@1=0.5554), **random_s44 (R@1=0.6009)** |
| 剩余 | 6 subruns |
| ETA | ~50-55h |

注意：random_s44 R@1=0.6009 是目前 Qwen 最高，best step 在 500（极早期就达峰，后续过拟合）。

### m2_full_starcoder_resumed (cuda:1) ✅ ALIVE
| 指标 | 值 |
|------|-----|
| 当前 subrun | random_s43 (1/8) |
| 进度 | step 1300/2810 (~46%) |
| eval@1000 | R@1=0.4780, val_loss=0.5430 (early_stop 1/2) |
| 剩余 | 7 subruns |
| ETA | ~55-65h |

eval@1500 预计 ~1h 后到达，val_loss 大概率再次不改善 → 触发 early stopping。

### m1_reextract_v2 (CPU) ✅ ALIVE
| 指标 | 值 |
|------|-----|
| 进度 | 24,321/28,276 instances (86.0%) |
| 错误 | 0 |
| 活跃 repos | sqlfluff, conan-io, pydicom, Project-MONAI |
| all.jsonl | 44,173 行（尚未合并新产出） |
| 磁盘 | 78G 可用 |
| ETA | ~May 15 15:00-17:00 CST |

### BM25 watchers
两个 BM25 watcher 均在后台等待：Qwen 链结束后自动启动 BM25 Qwen (cuda:0)，StarCoder 链结束后自动启动 BM25 StarCoder (cuda:1)。

---
