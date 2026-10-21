# ops eval task0 results and monitor

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_task0_results_and_monitor_20260525T093336_result.json`
- **Structured JSON:** [`be2d32806528bdea4d16.json`](../../sessions/be/be2d32806528bdea4d16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Task 0 结果 (30K checkpoint, 200 eps/task)

| Checkpoint | Seed | λ | TSR | CAR | frozen | fake_safe% | real_safe% | avg_ee_disp |
|------------|------|-------|------|------|--------|-----------|-----------|-------------|
| s1_l005 | 1 | 0.005 | **30.5%** (61/200) | **56.5%** (113/200) | 0.0% | 87.6% | 12.4% | 1.4653 |
| s1_l01 | 1 | 0.01 | **26.5%** (53/200) | **52.5%** (105/200) | 0.0% | 99.0% | 1.0% | 1.4864 |
| s2_l005 | 2 | 0.005 | **26.0%** (52/200) | **57.5%** (115/200) | 0.0% | 93.9% | 6.1% | 1.4938 |
| s2_l01 | 2 | 0.01 | **22.5%** (45/200) | **55.5%** (111/200) | 0.0% | 92.8% | 7.2% | 1.5217 |

### 对比 10K 参考值

| | 10K s0_l005 | 30K s1_l005 | 30K s2_l005 |
|---|---|---|---|
| TSR | ~62% | 30.5% | 26.0% |
| CAR | ~62% | 56.5% | 57.5% |

| | 10K s0_l01 | 30K s1_l01 | 30K s2_l01 |
|---|---|---|---|
| TSR | ~58% | 26.5% | 22.5% |
| CAR | ~56% | 52.5% | 55.5% |

**30K 全面劣于 10K**：TSR 骤降一半（30.5% vs 62%），CAR 略降。collision+success 占成功的绝大部分（s1_l01 只有 1 个 safe 成功），说明模型几乎只在碰撞后才能完成任务。

---

## Task 1 当前进度

| Eval | 当前 Task | Episode 进度 | 最新时间戳 |
|------|-----------|-------------|-----------|
| s1_l005 | Task 1 | **99/200** | 17:34 |
| s1_l01 | Task 1 | **96/200** | 17:35 |
| s2_l005 | Task 1 | **87/200** | 17:35 |
| s2_l01 | Task 1 | **86/200** | 17:35 |

Task 1 开始于 ~16:25-16:35，当前约 50% 进度。按当前速率（~1 ep/min），预计 ~19:15-19:40 完成 Task 1。全部 4 个 Task 完成预计还需 ~6-7 小时。

---
