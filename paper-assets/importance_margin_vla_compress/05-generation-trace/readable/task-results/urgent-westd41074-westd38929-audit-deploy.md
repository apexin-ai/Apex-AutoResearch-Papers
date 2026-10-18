# urgent westd41074 westd38929 audit deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd41074-westd38929-audit-deploy_20260524T031920_result.json`
- **Structured JSON:** [`b5b02110e04a6c19584a.json`](../../sessions/b5/b5b02110e04a6c19584a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41074

| GPU | 状态 | 实验 | 进度 |
|-----|------|------|------|
| 0 | **新部署** PID 542222 | pi05_l2norm_k05_spatial_seed43_v2 | 刚启动 |
| 1 | RUNNING PID 515300 | pi05_random_k03_long_seed43_v2 | Task 0/10, SR=32% |
| 2 | RUNNING PID 363842 | pi05_l2norm_k05_long_seed43 | Task 5/10, 累计56.4% |
| 3 | RUNNING PID 450962 | pi05_random_k085_object_seed42_postfix | Task 4/10, 累计3.0% |

**收割结果：**
- pi05_random_k095_goal_seed43: **SR=83.4%** (417/500) ✓ registry 已更新
- pi05_random_k085_goal_seed43: **SR=52.2%** (261/500) ✓ registry 已更新

**Orphan tmux sessions（无活跃 python）：** diag_read_goal_results, eval_random_k09_s42, smolvla_spatial, xvla_long, eval_pi05_random_k085_goal_seed43
**其他：** PID 584493 http.server:18765 (serving pi05_libero_finetuned)

---

## westd-38929

| GPU | 状态 | 实验 | 进度 |
|-----|------|------|------|
| 0 | **IDLE** | xvla_l2norm_k05_goal_seed42_v2 刚完成 | SR=59.0% ✓ |
| 1 | RUNNING PID 951181 | xvla_l2norm_k05_spatial_seed42_v2 | Task 8/10 |
| 2 | RUNNING PID 16456 | xvla_l2norm_k03_goal_seed42_v3 | 早期，全 FAIL |
| 3 | RUNNING PID 16599 | xvla_l2norm_k07_goal_seed42_v2 | ep 35/50，全 FAIL |

**收割结果：**
- xvla_l2norm_k05_goal_seed42_v2: **SR=59.0%** (295/500) ✓ registry 已更新
- xvla_l2norm_k05_goal_seed43: **SR=60.2%** (301/500) — 之前已完成
- xvla_random_k05_spatial_seed43: **SR=72.6%** (363/500) — 之前已完成

**Orphan tmux sessions：** eval_xvla_l2norm_k05_goal_seed43, eval_xvla_random_k05_spatial_seed43, eval_xvla_l2norm_k05_goal_seed42_v2

---

**注意：** westd-38929 GPU 0 当前空闲，可部署新实验。westd-41074 的 k095_goal_seed43 之前因网络不可达崩溃过，但重跑后成功出结果。

---
