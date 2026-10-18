# diag westd 27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-27271_20260527T012800_result.json`
- **Structured JSON:** [`032939a4566c621e6118.json`](../../sessions/03/032939a4566c621e6118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-27271 全面诊断报告

### 当前 GPU 状态

| GPU | 显存占用 | 利用率 | PID | 实验 | 状态 |
|-----|---------|--------|-----|------|------|
| 0 | 15964/97887 MiB | 78% | 609731 | L2Norm k=0.95 Goal s42 | **running** (Task 3/10) |
| 1 | 1/97887 MiB | 0% | — | — | **idle** |

### 上次已知实验对比

- **PID 499267** (OV Attn k=0.75 Goal s42) → **已完成并被替换**。结果已保存，SR = **67.4%**
- **PID 397225** (OV Attn k=0.5 Long s42) → **已完成并被替换**。结果已保存，SR = **14.6%** (libero_10)

### 最近完成的 OpenVLA 实验汇总

#### libero_goal (500 episodes)

| Method | k_ratio | Seed | SR | 完成时间 | 日志 |
|--------|---------|------|----|---------|------|
| **baseline** | — | 42 | **74.8%** | May 24 | `eval_openvla_baseline_goal_seed42_v3.log` |
| l2norm | 0.90 | 42 | 74.8% | May 25 | `eval_openvla_l2norm_k09_goal_seed42.log` |
| l2norm | 0.90 | 43 | 75.2% | May 26 | `eval_openvla_l2norm_k09_goal_seed43_v3.log` |
| l2norm | 0.85 | 42 | 75.4% | May 26 | `eval_openvla_l2norm_k085_goal_seed42.log` |
| l2norm | 0.75 | 42 | 70.2% | May 27 | `eval_openvla_l2norm_k075_goal_seed42_v2.log` |
| l2norm | 0.70 | 42 | 68.4% | May 27 | `eval_openvla_l2norm_k07_goal_seed42.log` |
| l2norm | 0.50 | 42 | 43.4% | May 24 | `eval_openvla_l2norm_k05_goal_seed42_v3.log` |
| attention | 0.90 | 42 | 73.2% | May 25 | JSON: `openvla_attention_prune_k09_goal_seed42.json` |
| attention | 0.90 | 43 | 73.2% | May 26 | JSON: `openvla_attention_prune_k09_goal_seed43.json` |
| attention | 0.75 | 42 | 67.4% | May 27 | JSON: `openvla_attention_prune_k075_goal_seed42.json` |
| attention | 0.50 | 42 | 44.2% | May 24 | JSON: `openvla_attention_prune_k05_goal_seed42.json` |
| random | 0.90 | 43 | 80.4% | May 26 | `eval_openvla_random_k09_goal_seed43.log` |
| random | 0.70 | 42 | 68.4% | May 26 | `eval_openvla_random_k07_goal_seed42_v4.log` |
| random | 0.50 | 42 | 52.2% | May 26 | JSON: `openvla_random_k05_goal_seed42.json` |
| **l2norm** | **0.95** | **42** | **进行中** | — | `eval_openvla_l2norm_k095_goal_seed42.log` |

#### libero_10 (long, 500 episodes)

| Method | k_ratio | Seed | SR | 完成时间 |
|--------|---------|------|----|---------|
| baseline | — | 42 | 52.8% | May 24 |
| attention | 0.50 | 42 | 14.6% | May 27 |

#### libero_spatial (500 episodes)

| Method | k_ratio | Seed | SR | 完成时间 |
|--------|---------|------|----|---------|
| l2norm | 0.90 | 42 | 75.0% | May 25 |

#### libero_object (500 episodes)

| Method | k_ratio | Seed | SR | 完成时间 |
|--------|---------|------|----|---------|
| baseline | — | 42 | 74.0% | May 25 |
| l2norm | 0.50 | 42 | 39.2% | May 25 |
| random | 0.70 | 43 | 51.2% | May 25 |

### 失败/中断的实验

| 实验 | 问题 | 详情 |
|------|------|------|
| `eval_openvla_l2norm_k075_goal_seed42` | exit 127 | `python: command not found`（conda 未激活），已由 v2 成功重跑 |
| `eval_openvla_random_k05_goal_seed42` (May 26 23:59 log) | 中断 | 日志停在 Task 4/10，无 sentinel。但更早的完整结果 (SR=52.2%) 已存在 |

### 关键发现

1. **GPU 1 完全空闲**，可立即调度新实验
2. 当前 GPU 0 的 L2Norm k=0.95 Goal s42 已完成 Task 1-2 (SR 58%/88%)，正在跑 Task 3，预计还需 ~2.5 小时完成
3. L2Norm 在 goal suite 上 k=0.85-0.90 表现最好 (74.8%-75.4%)，接近 baseline (74.8%)，剪枝 10-15% token 几乎无损

---
