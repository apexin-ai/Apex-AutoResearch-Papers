# ssh v72 seed1 completion check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v72-seed1-completion-check_20260517T132650_result.json`
- **Structured JSON:** [`ddfe0169a85c0ccb33c0.json`](../../sessions/dd/ddfe0169a85c0ccb33c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在正常运行。

---

## 产出汇总

### 训练完成确认
| Seed | Steps | 时间 | Checkpoint |
|------|-------|------|------------|
| seed1 | 20000/20000 | 3.0h | ✅ `/root/autodl-tmp/acib_v7.2_connector_scorer/checkpoint-20000/` (955 MB) |
| seed2 | 20000/20000 | 3.1h | ✅ `/root/autodl-tmp/acib_v7.2_connector_scorer_seed2/checkpoint-20000/` (955 MB) |

### Probe A 结果 (step 20000)

**Seed1 — Probe A (fixed image, swap instruction):**

| Pair | cos | l2 | bit_identical |
|------|-----|----|---------------|
| bbq_sauce vs bowl_cookie | 0.877 | 3.74 | False |
| bbq_sauce vs bowl_cabinet | 0.791 | 4.06 | False |
| bowl_cookie vs bowl_cabinet | 0.944 | 2.15 | False |

→ **Scorer is language-condition-dependent** (cos ∈ [0.791, 0.944])

**Seed1 — Probe B (natural cross-task):**

| Pair | cos | l2 |
|------|-----|----|
| bbq_sauce vs bowl_cookie | 0.670 | 3.22 |
| bbq_sauce vs bowl_cabinet | 0.624 | 3.28 |
| bowl_cookie vs bowl_cabinet | 0.755 | 2.82 |

→ **Task-dependent importance maps** (cos ∈ [0.624, 0.755])

**Seed2 — Probe A:**

| Pair | cos | l2 | bit_identical |
|------|-----|----|---------------|
| bbq_sauce vs bowl_cookie | 0.689 | 5.80 | False |
| bbq_sauce vs bowl_cabinet | 0.593 | 6.12 | False |
| bowl_cookie vs bowl_cabinet | 0.923 | 1.24 | False |

→ **Language-condition-dependent** (cos ∈ [0.593, 0.923])

**Seed2 — Probe B:**

| Pair | cos | l2 |
|------|-----|----|
| bbq_sauce vs bowl_cookie | 0.830 | 4.53 |
| bbq_sauce vs bowl_cabinet | 0.790 | 5.05 |
| bowl_cookie vs bowl_cabinet | 0.769 | 2.83 |

→ **Task-dependent importance maps** (cos ∈ [0.769, 0.830])

### Heatmap 文件
- `/root/autodl-tmp/v72_probe/seed1_step20000/probe_A_fixed_image_swap_instruction.png`
- `/root/autodl-tmp/v72_probe/seed1_step20000/probe_B_cross_task_heatmaps.png`
- `/root/autodl-tmp/v72_probe/seed2_step20000/probe_A_fixed_image_swap_instruction.png`
- `/root/autodl-tmp/v72_probe/seed2_step20000/probe_B_cross_task_heatmaps.png`

### Eval 启动确认
| GPU | α | PID | Memory | Status |
|-----|---|-----|--------|--------|
| 0 | 0.0 | 40598 | 6560 MiB | Running (rollouts in progress) |
| 1 | 1.0 | 44022 | 3816 MiB | Running (building envs, starting rollouts) |

---
