# ops check a3 v11 status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_a3_v11_status_20260522T135742_result.json`
- **Structured JSON:** [`5b51186f74771515733c.json`](../../sessions/5b/5b51186f74771515733c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## A3 Eval v11 — 中间状态

**进程状态: RUNNING** — PID 564007, 已运行 50min, 当前在 Task 3 ep 30/50

**GPU 3**: 8127 MiB / 97887 MiB, 正常

### 已完成任务结果

| Task | TSR | CAR | Displacement | refined_count |
|------|-----|-----|-------------|---------------|
| 0 | **0.0%** (0/50) | 84.0% (42/50) | 0.0149m | **0** |
| 1 | **0.0%** (0/50) | **48.0%** (24/50) | 0.0388m | **0** |
| 2 | **0.0%** (0/50) | 82.0% (41/50) | 0.0079m | **0** |

### MVP Gate 评估：**全线不达标**

| 指标 | 目标 | 实际 | 状态 |
|------|------|------|------|
| CAR ≥94% | ≥94% | 48~84% | **FAIL** (Task 1 甚至低于 baseline 83%) |
| TSR drop <10% | >0% | **0.0%** | **CATASTROPHIC** — 150 episodes 无一成功 |
| refined_count >0 | >0 | **全部 0** | **FAIL** — SDF gradient refinement 完全未激活 |
| displacement ≈0.027m | ~0.027m | 0.008~0.039m | 波动大 |

### 关键问题

1. **TSR=0%**: 所有 episode 都跑满 300 步超时，机器人从未完成任何任务
2. **refined_count=0**: A3 的核心机制（SDF gradient refinement）完全没有触发。sdf_min 值都 >0.5，说明 SDF 场认为所有点都远离碰撞面——SDF 计算或 refinement 阈值可能配置错误
3. **Triton autotuning OOM**: 日志中有多个 triton kernel OutOfMemoryError，虽然 fallback 到了其他 config，但可能影响推理质量

进程还在跑（Task 3 剩余 ~20 episodes + 后续 tasks），但从前 3 个 task 的结果看，v11 距离 MVP gate 差距很大。是否需要现在就排查 refinement 未激活的根因？

---
