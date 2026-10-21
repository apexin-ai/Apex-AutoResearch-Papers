# ops collect all results 0521

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-all-results-0521_20260521T063822_result.json`
- **Structured JSON:** [`c6df28ee6802246ff895.json`](../../sessions/c6/c6df28ee6802246ff895.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总报告：

---

## === westd-38929 === (4× RTX PRO 6000 Blackwell 98GB)

| GPU | 状态 | PID | 实验 | 已运行 |
|-----|------|-----|------|--------|
| 0 | RUNNING | 568225 | OpenVLA L2norm k=0.5 Object seed42 | 1h36m |
| 1 | RUNNING | 568905 | OpenVLA random k=0.3 Object seed42 | 1h35m |
| 2 | RUNNING | 569611 | OpenVLA L2norm k=0.7 Object seed42 | 1h35m |
| 3 | RUNNING | 570309 | OpenVLA L2norm k=0.3 Object seed42 | 1h34m |

**空闲 GPU: 0**。4 个 eval 均在运行，预计还需 ~3 小时完成。

---

## === cqa1-33015 === (4× RTX 4090D 24GB)

| GPU | 状态 | PID | 实验 | 已运行 |
|-----|------|-----|------|--------|
| 0 | RUNNING | 118463 | X-VLA random k=0.5 Spatial seed42 | 1h16m |
| 1 | RUNNING | 223599 | X-VLA random k=0.7 Object seed43 | 47m |
| 2 | RUNNING | 379067 | X-VLA L2norm k=0.7 Object seed42 | 3m |
| 3 | RUNNING | 379143 | X-VLA random k=0.5 Object seed43 | 3m |

**空闲 GPU: 0**

**已完成的 X-VLA 结果（今日新增）：**

| 文件 | Mode | Suite | k | Seed | SR |
|------|------|-------|---|------|-----|
| xvla_prune_k0.3_libero_object.json | random | Object | 0.3 | 42 | **62.8%** |
| xvla_prune_k0.5_libero_object.json | random | Object | 0.5 | 43 | **71.0%** |
| xvla_prune_k0.7_libero_object.json | random | Object | 0.7 | 42 | **65.2%** |
| xvla_prune_k0.8_libero_object.json | random | Object | 0.8 | 42 | **89.4%** |
| xvla_prune_k0.85_libero_object.json | random | Object | 0.85 | 42 | **63.6%** |
| xvla_prune_k0.9_libero_object.json | random | Object | 0.9 | 42 | **97.8%** |
| xvla_prune_k0.85_libero_spatial.json | random | Spatial | 0.85 | 42 | **67.6%** |
| xvla_baseline_libero_goal_seed42.json | baseline | Goal | 1.0 | 42 | **98.0%** |
| xvla_baseline_libero_long_seed42.json | baseline | Long | 1.0 | 42 | **94.0%** |
| xvla_baseline_libero_spatial_seed42.json | baseline | Spatial | 1.0 | 42 | **91.6%** |

注意：X-VLA random Object 曲线非单调 — k=0.9 (97.8%) > k=0.8 (89.4%) > k=0.5 (71.0%) > k=0.7 (65.2%) > k=0.85 (63.6%) > k=0.3 (62.8%)。k=0.85 和 k=0.7 都比 k=0.5 低，方差较大。

---

## === westd-41074 === (4× RTX PRO 6000 Blackwell 98GB)

| GPU | 状态 | PID | 实验 | 已运行 |
|-----|------|-----|------|--------|
| 0 | RUNNING | 838823 | π0.5 L2norm k=0.5 Object seed42 | 53m |
| 1 | **FREE** | — | — | — |
| 2 | RUNNING | 68539 | M96 VTC train | 1d 3h |
| 3 | RUNNING | 738642 | M64 v4 VTC train | 3h55m |

**⚡ 空闲 GPU: 1 (cuda:1)**

**已完成结果：**

| 文件 | 实验 | SR |
|------|------|-----|
| pi05_baseline_libero_object.json | π0.5 baseline Object | **98.2%** |
| openvla_random_k05_seed42.json | OpenVLA random k=0.5 Object | **35.8%** |
| openvla_random_k09_seed42.json | OpenVLA random k=0.9 Object | **64.6%** |
| openvla_l2norm_k07_seed43_v2.json | OpenVLA L2norm k=0.7 Object seed43 | **49.8%** |
| pi05_vision_token_cv_random.json | π0.5 vision token CV 分析 (不是 eval) | — |

---

## === westd-27271 === (2× RTX PRO 6000 Blackwell 98GB)

| GPU | 状态 | PID | 实验 | 已运行 |
|-----|------|-----|------|--------|
| 0 | RUNNING | 188254 | M128 eval v2 (Object seed42) | 18m |
| 1 | RUNNING | 921279 | M32 VTC train (resume) | 19h51m |

**空闲 GPU: 0**

M32 VTC train 已保存 checkpoint_step40000.pt (今天 11:02)，总步数大概率 50k，预计约 80% 完成。
M128 eval v2 刚开始 18 分钟，预计需要数小时。

---

## 总结

**可立即使用的空闲 GPU：westd-41074 cuda:1（1 块 98GB RTX PRO 6000 Blackwell）**

全局 14 GPU 中 13 块在用，1 块空闲。

---
