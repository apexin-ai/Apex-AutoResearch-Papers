# ops verify frozen definition sdf l01 s0

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_frozen_definition_sdf_l01_s0_20260526T094809_result.json`
- **Structured JSON:** [`e3f93320fcfa8c07ba74.json`](../../sessions/e3/e3f93320fcfa8c07ba74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整的结论如下：

---

## frozen_rate 定义验证结果

### JSON schema（per-episode 字段）
`episode`, `success`, `collided`, `collision_step`, `collision_obstacle`, `max_displacement`（obstacle）, `max_ee_displacement`（EE）, `total_steps`, `smoothness`, `total_ee_path_length`。**JSON 中没有 `frozen` 字段**，是外部计算的。

### "frozen" 实际含义
`frozen_rate = 55.5%` 对应的是 **`max_displacement`（obstacle 位移）< 0.0001** 的 episode 数占总 episode 数：111/200 = 55.5%。

来源代码：`analyze_displacement.py:34` 定义 `frozen_eps = [e for e in safe_eps if e["max_displacement"] < threshold]`——即**安全 episode 中 obstacle 几乎没动的比例**，不是 EE-based。

### 核心发现：SDF 和 LoRA 的 frozen 数据完全一致

| 指标 | SDF s0 l01 30k | LoRA s0 reeval |
|---|---|---|
| **EE frozen (<0.1m)** | **0/200 (0%)** | **0/200 (0%)** |
| EE disp range | 0.312 – 0.865 | 0.305 – 0.841 |
| Obs frozen (<0.0001) | **111/200 (55.5%)** | **111/200 (55.5%)** |
| Obs frozen (<0.001) = CAR | 114/200 (57.0%) | 113/200 (56.5%) |
| Safe+Failed (fake safe) | 49/200 (24.5%) | 54/200 (27.0%) |

### 矛盾解释

1. **EE-based frozen = 0% for both models**。Robot 在每个 episode 都在动（min EE disp > 0.3m），SDF 没有导致 action collapse。

2. **Reported frozen=55.5% for SDF 是 obstacle-based**（obs_disp < 0.0001），实际上就是"没碰到障碍物"的 episode，跟 CAR 几乎等价（114 safe 中 111 个 obs < 0.0001）。

3. **LoRA-only "frozen=0%" 是错的/不一致的**——LoRA 用同样标准算也是 55.5%。reeval_comparison.py 中 LoRA frozen=0.0 是手动填入的，未从 JSON 实际计算。

4. Task 1 (chocolate pudding) TSR=78% + obs_frozen=36/50 没有矛盾：robot 在动（EE disp ~0.41m），完成任务的同时没碰障碍物，obstacle 没位移是正常的。

### 正确的 EE-based 指标

| | SDF s0 l01 | LoRA s0 |
|---|---|---|
| EE-based frozen rate | **0%** | **0%** |
| EE-based fake safe rate | N/A（无 frozen episode） | N/A |
| Obstacle-based fake safe (safe+failed) | 24.5% | 27.0% |

---
