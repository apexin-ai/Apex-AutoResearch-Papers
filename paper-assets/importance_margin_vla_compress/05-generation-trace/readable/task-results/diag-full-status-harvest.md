# diag full status harvest

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full-status-harvest_20260523T175203_result.json`
- **Structured JSON:** [`4dd4ef8089aabb125939.json`](../../sessions/4d/4dd4ef8089aabb125939.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个实验已标 DONE。完整状态表：

## 服务器状态总览

| Server | GPU | Experiment | Status | SR |
|--------|-----|-----------|--------|-----|
| **westd-38929** | 0-3: 0%, idle | E5 attn_last k=0.5 Goal v2 | **DONE** | **98.2%** |
| | | E5 attn_mean k=0.5 Goal v2 | **DONE** | **97.4%** |
| | | E5 attn_rollout k=0.5 Goal v2 | **DONE** | **96.8%** |
| | | E5 random k=0.5 Goal v2 | **DONE** | **67.2%** |
| **westd-27271** | 0: 68%, 16GB | OpenVLA Goal baseline v3 | Running | Task 10/10 (~soon) |
| | 1: 78%, 16GB | OpenVLA Long baseline | Running | Task 3/10 (ep 40/50) |
| **westd-41074** | 0: 39% | π0.5 l2norm k=0.925 Goal v2 | Running | T8/10, ~94.5% avg |
| | 1: 31% | π0.5 l2norm k=0.85 Spatial v2 | Running | T6-7/10 |
| | 2: 11% | π0.5 random k=0.925 Goal v2 | Running | T5-6/10 |
| | 3: ~0% | π0.5 random k=0.85 Spatial v2 | Running | T4-5/10 |
| **cqa1-33015** | 0-2: idle | π0.5 l2norm k=0.95 Goal v2 | **DONE** | **89.4%** |
| | | π0.5 l2norm k=0.90 Goal v2 | **DONE** | **90.6%** |
| | | π0.5 l2norm k=0.70 Goal v2 | **DONE** | **73.6%** |
| | 3: 11% | π0.5 l2norm k=0.30 Goal v2 | Running | T9/10 (ep 20/50) |

## Registry harvest 完成

| Experiment | conclusion | SR |
|-----------|-----------|-----|
| eval_e5_xvla_attn_last_goal_k05_v2 | success | 98.2% |
| eval_e5_xvla_attn_mean_goal_k05_v2 | success | 97.4% |
| eval_e5_xvla_attn_rollout_goal_k05_v2 | success | 96.8% |
| eval_e5_xvla_random_goal_k05_v2 | negative | 67.2% |
| eval_pi05_random_k095_goal_seed42_v2 | success | 83.8% |
| eval_pi05_random_k09_goal_seed42_v2 | negative | 62.2% |
| eval_pi05_random_k07_goal_seed42_v2 | negative | 78.2% |
| eval_pi05_random_k03_goal_seed42_v2 | negative | 50.6% |

## 关键发现

**E5 Goal k=0.5 v2 — 论文叙事核心数据**：attention-based pruning 在 50% 极端剪枝下 Goal 套件依然保持 96.8-98.2% SR，而 random 只有 67.2%。**Importance margin = +29-31pp**，比 Object/Spatial 套件的 margin 更大，强化了论文叙事。

**westd-38929 已空闲**，可部署新实验。westd-41074 和 cqa1-33015 的实验预计 1-2 小时内全部完成。westd-27271 的 OpenVLA Goal baseline 即将完成（Task 10/10），Long 还需数小时。

---
