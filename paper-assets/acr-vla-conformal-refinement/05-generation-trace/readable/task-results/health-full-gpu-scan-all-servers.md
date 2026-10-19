# health full gpu scan all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_health_full-gpu-scan-all-servers_20260524T093345_result.json`
- **Structured JSON:** [`0e294015f3e4f3f1af66.json`](../../sessions/0e/0e294015f3e4f3f1af66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器 GPU 状态全景

---

### bjb1-32546
GPU 数量：6（24GB x6）
| GPU | 显存占用 | 进程/实验 | 状态 |
|-----|---------|----------|------|
| 0 | 3297 MiB | obj-vla-s47 | 运行中 — bbq_sauce 100% (20/20) |
| 1 | 3775 MiB | obj-k2mean-s47 | 运行中 — ketchup 10/20 (8/10) |
| 2 | 3871 MiB | obj-crm-s47 | 运行中 — ketchup 5/20 (5/5) |
| 3 | 3777 MiB | obj-adapt-s47 | 运行中 — ketchup 5/20 (5/5) |
| 4 | 3083 MiB | long-crm-s47 | 运行中 — LIVING_ROOM_SCENE6 5/20 (1/5) |
| 5 | 3121 MiB | long-reconvla-s47 | 运行中 — LIVING_ROOM_SCENE6 5/20 (3/5) |

tmux sessions: 6 个 eval 全部活跃

---

### bjb1-18228
GPU 数量：4（24GB x4）
| GPU | 显存占用 | 进程/实验 | 状态 |
|-----|---------|----------|------|
| 0 | 9884 MiB | **precompute-pi05-object** | 运行中 — 71500 samples 已完成 |
| 1 | 6282 MiB | goal-vla-s47 eval | 运行中 — open_middle_drawer 10/20 (7/10) |
| 2 | 5508 MiB | long-vla-s47 eval | 运行中 — 刚加载环境 |
| 3 | 9883 MiB | **precompute-pi05-long** | 运行中 — 69000 samples 已完成 |

tmux sessions: goal-vla-s47, long-vla-s47
特殊发现: GPU 1+2 不再是 SmolVLA eval，已换为 seed47 系列 eval（goal-vla, long-vla）

**Precompute 输出文件状态：**
| Suite | 状态 | 详情 |
|-------|------|------|
| spatial | **已完成** | 60250 samples，merged files 已生成 (expert_actions.pt, k_samples.pt, obs_features.pt) |
| goal | **已完成** | 61728 samples，merged files 已生成 |
| object | 运行中 | 71500 samples done，最新 chunk `partial_s0_71000_71500.pt` (17:24) |
| long | 运行中 | 69000 samples done，最新 chunk `partial_s0_68500_69000.pt` (17:25) |

---

### bjb2-28827
GPU 数量：6（24GB x6）
| GPU | 显存占用 | 进程/实验 | 状态 |
|-----|---------|----------|------|
| 0 | 1 MiB | — | **空闲** |
| 1 | 19320 MiB | OpenVLA object eval (seed42, vla_only) | 运行中（无 tmux） |
| 2 | 1 MiB | — | **空闲** |
| 3 | 1 MiB | — | **空闲** |
| 4 | 1 MiB | — | **空闲** |
| 5 | 1 MiB | — | **空闲** |

tmux sessions: 无
特殊发现: GPU 1 跑着 `openvla_eval.py --benchmark object --seed 42`，无 tmux 管理，5 GPU 空闲

---

### bjb2-40593
GPU 数量：1（24GB x1）
| GPU | 显存占用 | 进程/实验 | 状态 |
|-----|---------|----------|------|
| 0 | 2301 MiB | eval-spatial-crm-s47 | 运行中 — pick_up_black_bowl 10/20 (7/10) |

tmux sessions: eval-spatial-crm-s47

---

### cqa1-32758
GPU 数量：6（24GB x6）
| GPU | 显存占用 | 进程/实验 | 状态 |
|-----|---------|----------|------|
| 0 | 2763 MiB | spatial-vla-s47 | 运行中 — black_bowl_on_stove 75% (15/20) |
| 1 | 2237 MiB | spatial-reconvla-s47 | 运行中 — black_bowl_on_stove 90% (18/20) |
| 2 | 2265 MiB | spatial-k2mean-s47 | 运行中 — black_bowl_on_stove 80% (16/20) |
| 3 | 2237 MiB | spatial-adapt-s47 | 运行中 — black_bowl_next_to_plate 5/20 (2/5) |
| 4 | 4565 MiB | long-adapt-s47 | 运行中 — LIVING_ROOM_SCENE5 10/20 (4/10) |
| 5 | 4565 MiB | long-vla-s47 | 运行中 — LIVING_ROOM_SCENE5 15/20 (7/15) |

tmux sessions: 6 个 eval 全部活跃

---

## 汇总

**总空闲 GPU：5**（全在 bjb2-28827 的 GPU 0/2/3/4/5）

**π0.5 precompute 完成状态：**
| Suite | 状态 | 进度 |
|-------|------|------|
| spatial | 已完成 | 60250 samples，已 merge |
| goal | 已完成 | 61728 samples，已 merge |
| object | 运行中 | 71500/? samples（持续生成中，~15min/chunk） |
| long | 运行中 | 69000/? samples（持续生成中，~15min/chunk） |

**正在跑的实验清单（全部 seed 47 eval）：**
| 实验 | 服务器 | GPU |
|------|--------|-----|
| obj-vla-s47 | bjb1-32546 | 0 |
| obj-k2mean-s47 | bjb1-32546 | 1 |
| obj-crm-s47 | bjb1-32546 | 2 |
| obj-adapt-s47 | bjb1-32546 | 3 |
| long-crm-s47 | bjb1-32546 | 4 |
| long-reconvla-s47 | bjb1-32546 | 5 |
| goal-vla-s47 | bjb1-18228 | 1 |
| long-vla-s47 | bjb1-18228 | 2 |
| precompute-object | bjb1-18228 | 0 |
| precompute-long | bjb1-18228 | 3 |
| openvla-object-s42 | bjb2-28827 | 1（无 tmux） |
| eval-spatial-crm-s47 | bjb2-40593 | 0 |
| spatial-vla-s47 | cqa1-32758 | 0 |
| spatial-reconvla-s47 | cqa1-32758 | 1 |
| spatial-k2mean-s47 | cqa1-32758 | 2 |
| spatial-adapt-s47 | cqa1-32758 | 3 |
| long-adapt-s47 | cqa1-32758 | 4 |
| long-vla-s47 | cqa1-32758 | 5 |

---
