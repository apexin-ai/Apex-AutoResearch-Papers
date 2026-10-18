# ops healthcheck westd38929 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_healthcheck-westd38929-v2_20260524T093531_result.json`
- **Structured JSON:** [`dd889e25214400a9e783.json`](../../sessions/dd/dd889e25214400a9e783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 GPU 状态报告

### GPU 0 — IDLE (空闲)
- **实验**: eval_pi05_random_k09_goal_seed42_postfix
- **Status**: ✅ **COMPLETED**
- **SR = 61.8%** (309/500)
- 结果文件: `eval_results/pi05_random_k0.90_libero_goal_seed42.json`
- Per-task: T0=76%, T1=32%, T2=38%, T3=38%, T4=90%, T5=88%, T6=80%, T7=88%, T8=74%, T9=14%

### GPU 1 — IDLE (空闲)
- **实验**: eval_pi05_random_k085_goal_seed42_postfix
- **Status**: ✅ **COMPLETED**
- **SR = 52.8%** (264/500)
- 结果文件: `eval_results/pi05_random_k0.85_libero_goal_seed42.json`
- Per-task: T0=68%, T1=4%, T2=20%, T3=30%, T4=66%, T5=80%, T6=86%, T7=90%, T8=78%, T9=6%

### GPU 2 — IDLE (空闲)
- **实验**: eval_pi05_random_k07_goal_seed42_postfix
- **Status**: ✅ **COMPLETED**
- **SR = 75.6%** (378/500)
- 结果文件: `eval_results/pi05_random_k0.70_libero_goal_seed42.json`
- Per-task: T0=90%, T1=48%, T2=82%, T3=74%, T4=96%, T5=72%, T6=62%, T7=100%, T8=82%, T9=50%

### GPU 3 — PID 16832, 4838MiB, 1% GPU util
- **实验**: eval_xvla_l2norm_k03_goal_seed42_v5
- **Status**: 🔄 **RUNNING** — Task 6 进行中 (ep 9/50, 暂全 FAIL)
- **已完成 6/10 tasks**: T0=42%, T1=92%, T2=20%, T3=24%, T4=98%, T5=0%
- **Interim SR**: 138/300 = **46.0%**
- 注意: T5 和 T6 连续全 FAIL（800 step timeout），最终 SR 可能会较低
- 对比旧 domain_id=1 的结果 (SR=0.2%)，domain_id=3 大幅改善

### 关键发现

**π0.5 Random Goal 呈非单调趋势**:
| keep_ratio | SR |
|---|---|
| 0.90 | 61.8% |
| 0.85 | 52.8% |
| 0.70 | **75.6%** |

k=0.7 反而最高，比 k=0.9 高 14 个点。

**GPU 0-2 已空闲**，可部署新实验。GPU 3 的 v5 预计还需 ~50 分钟完成（Task 6-9 剩余约 200 episodes）。

---
