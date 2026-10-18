# m103 check cqa1 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_m103_check_cqa1_status_20260525T011910_result.json`
- **Structured JSON:** [`63bf0793cb5ace51b561.json`](../../sessions/63/63bf0793cb5ace51b561.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| # | 实验 | 状态 | GPU | 进度/结果 |
|---|------|------|-----|-----------|
| 1 | eval_pi05_l2norm_k085_object_seed43_postfix | **运行中** | GPU 0 (54%) | Task 5/10 完成，累计 249/250=99.6%，已跑 44.5min |
| 2 | eval_pi05_random_k085_goal_seed43_postfix | **已完成** ✓ | — | **SR=53.4%** (267/500)，结果文件 May 23 已生成 |
| 3 | eval_pi05_random_k085_spatial_seed43_postfix | **运行中** | GPU 1 (40%) | Task 9/10 进行中，累计 272/450=60.4%，141min |
| 4 | eval_pi05_random_k085_long_seed43_v2 (=postfix) | **运行中** | GPU 2 (0%*) | Task 3/10，累计 70/150=46.7%，73min |
| 5 | eval_pi05_l2norm_k085_spatial_seed43_postfix | **已完成** ✓ | — | **SR=88.2%** (441/500)，今天 08:39 结束 |

**GPU 空闲：1 块**（GPU 3 完全空闲，24GB 可用）

*GPU 2 显示 0% utilization 但占用 9.8GB 显存，可能处于 episode 间隙。

**Registry 已更新**：实验 #2 和 #5 → status=DONE + metrics。

---
