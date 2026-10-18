# ops westd redeploy and check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_redeploy_and_check_20260526T093017_result.json`
- **Structured JSON:** [`717f59db1e2b539a5326.json`](../../sessions/71/717f59db1e2b539a5326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## Part 1: westd-41074 GPU 2 — Attn k=0.7 Object 重跑 ✅

- 旧实验 `eval_openvla_attn_k07_object_seed42` → 标记 DONE/failed（崩溃于 Task 6/10）
- 新实验 `eval_openvla_attn_k07_object_seed42_v2` → **RUNNING**
  - tmux session: `eval_openvla_attn_k07_object_seed42_v2`
  - PID: 542010 (python)
  - GPU 2: 15479 MiB loaded, attention pruning 256→179 tokens
  - 日志: `~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_object_seed42_v2.log`

## Part 2: westd-41074 GPU 1 + GPU 3 — 在跑（仅监控）

| GPU | 实验 | tmux | 当前进度 | 中间结果 |
|-----|------|------|----------|----------|
| GPU 1 | L2norm k=0.85 Object | eval_k085_obj | Task 4/10, Ep 20/50 | T2=40%, T3=60% |
| GPU 3 | L2norm k=0.95 Object | eval_k095_obj | Task 4/10, Ep 20/50 | T2=52%, T3=82% |

两个实验运行正常，速度 ~1.7-1.8 eps/min。

## Part 3: westd-27271 GPU 0 ✅

- 发现 `eval_openvla_l2norm_k09_goal_seed43_v3` **已完成**，SR=75.2% (376/500)，已更新 registry 为 DONE/success
- GPU 0 空闲，部署新实验 `eval_openvla_l2norm_k085_goal_seed42` → **RUNNING**
  - tmux session: `eval_openvla_l2norm_k085_goal_seed42`
  - PID: 207593 (python)
  - GPU 0: 15131 MiB loaded, L2 pruning 256→217 tokens
  - 日志: `~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k085_goal_seed42.log`
- westd-27271 GPU 1: Attn k=0.9 Goal seed43 仍在跑（PID 112477）

---
