# monitor progress check may15

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_may15_20260514T211439_result.json`
- **Structured JSON:** [`689f2c4e339c76249cb1.json`](../../sessions/68/689f2c4e339c76249cb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## 实验状态汇总 (2026-05-15 05:15 CST)

### 1. m2_full_qwen_continued ✅ 正常运行
| 项目 | 值 |
|------|-----|
| PID | 337267 (uptime 09:50:41) |
| GPU | cuda:0, 100% util, 51.5/97.9GB, 68°C |
| 当前子任务 | random_s44 (第 3/7 个) |
| 进度 | step 850/1408, epoch 1/2 |
| eval@500 | **R@1=0.6009**, val_loss=0.4252 |
| 已完成 | random_s42 (R@1=0.5527), random_s43 (R@1=0.5554) |
| 剩余 | 5 个子任务 (emb_dist×2, dataflow×2, bm25) |
| 预计完成 | ~40-45h 后 |

random_s44 的 R@1=0.6009 是目前 Qwen 所有 runs 中最高的。

### 2. m2_full_starcoder_resumed ✅ 正常运行
| 项目 | 值 |
|------|-----|
| PID | 519791 (uptime 03:11:44) |
| GPU | cuda:1, 100% util, 53.9/97.9GB, 72°C |
| 当前子任务 | random_s43 (第 1/9 个) |
| 进度 | step 550/1405, epoch 1/2 |
| eval@500 | R@1=0.4708, val_loss=0.5279 |
| 剩余 | 8 个子任务 |
| 预计完成 | ~65-70h 后 |

StarCoder R@1 明显低于 Qwen (0.47 vs 0.60)，符合预期（Qwen2.5-Coder 编码能力更强）。

### 3. m1_reextract_v2 ✅ 正常运行
| 项目 | 值 |
|------|-----|
| Workers | 4 CPU |
| 运行时间 | ~25h (启动 May 14 03:59) |
| 总量 | 28,276 instances / 82 repo groups |
| 产出 | 40,225 JSON files |
| 活跃 repos | sqlfluff 250/1272, bleach 350/455, conan 450/972, MONAI 150/524 |
| 进度 | ~82% (上次检查 80.8%, 仅剩 4 个大 repo) |
| 预计完成 | ~15:00 CST May 15 |
| 磁盘 | 98GB 可用，充足 |

无异常，三个实验均健康运行。

---
