# check m2 training progress 0515

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_m2-training-progress-0515_20260515T041456_result.json`
- **Structured JSON:** [`a219ecf602bee20cac99.json`](../../sessions/a2/a219ecf602bee20cac99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## Qwen M2 (cuda:0, PID 337267)
| 指标 | 值 |
|------|-----|
| 当前 subrun | **embedding_distance_s43** (4/9) |
| 进度 | step **1000/2810** (35.6%) |
| 最新 eval@500 | val_loss=**0.4541**, R@1=**0.5446** |
| 已完成 | random_s42 (R@1=0.5527), random_s43 (R@1=0.5554), random_s44 (R@1=**0.6009**) |
| 速度 | ~280 steps/h (~9.9h/subrun) |
| ETA 当前 subrun | ~18:30 CST 今天 |
| ETA 全部完成 | ~**May 17 21:00 CST** |

## StarCoder M2 (cuda:1, PID 519791)
| 指标 | 值 |
|------|-----|
| 当前 subrun | **random_s43** (1/8) |
| 进度 | step **1900/2810** (67.6%) |
| 最新 eval@1500 | val_loss=**0.5239**, R@1=**0.4912** |
| 已完成 | 无（首个 subrun 进行中） |
| 速度 | ~187 steps/h (~15h/subrun) |
| ETA 当前 subrun | ~17:00 CST 今天 |
| ETA 全部完成 | ~**May 20 01:00 CST** |

两个进程均正常运行，GPU 利用率 96%/100%。Qwen 比 StarCoder 快约 50%（280 vs 187 steps/h），预计提前 2 天完成全部链。StarCoder random_s43 的 R@1 随训练稳步提升（0.471→0.478→0.491），趋势正常。

---
