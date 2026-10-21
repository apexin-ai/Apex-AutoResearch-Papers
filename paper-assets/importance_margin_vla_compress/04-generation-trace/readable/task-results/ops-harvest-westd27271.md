# ops harvest westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-westd27271_20260524T080029_result.json`
- **Structured JSON:** [`6281999e48496e1c8438.json`](../../sessions/62/6281999e48496e1c8438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行中，尚未完成。

## 实验状态报告

| 字段 | eval_openvla_attn_k05_object_seed42_v2 (GPU 0) | eval_openvla_attn_k05_goal_seed42 (GPU 1) |
|------|------|------|
| **Status** | **running** | **running** |
| **PID** | 676491 | 675522 |
| **Started** | ~14:49 | ~14:47 |
| **Progress** | Task 3/10, Ep 10/50 | Task 4/10, 刚开始 |
| **已完成 tasks** | Task 1: 0/50 (0%), Task 2: 0/50 (0%) | Task 1: 7/50 (14%), Task 2: 28/50 (56%), Task 3: 35/50 (70%) |
| **Speed** | ~1.5 eps/min | ~1.7-2.0 eps/min |
| **结果文件** | 尚未生成 | 尚未生成 |
| **日志** | `logs/eval_openvla_attn_k05_object_seed42_v2.log` | `logs/eval_openvla_attn_k05_goal_seed42.log` |

**预估剩余时间**：
- Object: 完成了 ~110/500 episodes，剩 ~390 eps ÷ 1.5 eps/min ≈ **4.3 小时**
- Goal: 完成了 ~150/500 episodes，剩 ~350 eps ÷ 1.8 eps/min ≈ **3.2 小时**

注意：Object 实验前 2 个 task 成功率为 0%，attention pruning k=0.5 在 object suite 上可能表现很差。Goal 前 3 个 task 平均成功率 46.7%，表现合理。

---
