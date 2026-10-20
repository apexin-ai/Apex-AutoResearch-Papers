# ops gradient analysis and cutoff45k check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gradient_analysis_and_cutoff45k_check_20260524T112018_result.json`
- **Structured JSON:** [`a3a88f2a52253c34c014.json`](../../sessions/a3/a3a88f2a52253c34c014.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都启动正常。汇总如下：

---

### Step 1: cutoff_45k_s0_eval — DONE

| 指标 | 值 |
|------|------|
| **TSR** | **0.896 (89.6%)** |
| **CAR** | **0.764 (76.4%)** |

- 结果文件: `/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260524_184104.json`
- Registry 已更新: status=DONE, conclusion=success

### Step 2: gradient_analysis_mixed_seed — RUNNING (GPU 1)

PID 821589, 5 条件串行执行中。Vanilla_s0 已在运行 (batch 40+/200)。

| # | 条件 | Checkpoint | 状态 |
|---|------|-----------|------|
| 1 | Vanilla_s0 (seed 42) | `vanilla_retrain_s0/.../50000_chkpt` | 运行中 |
| 2 | Full_OCC_s0 (seed 42) | `full_occ_retrain_s0/.../50000_chkpt` | 排队 |
| 3 | Detach_LN_s0 (seed 42) | `detach_ln_s0/.../50000_chkpt` | 排队 |
| 4 | Detach_BN_s2 (seed 44) | `ablation_occ_detach_s2/.../50000_chkpt` | 排队 |
| 5 | Random_s2 (seed 44) | `ablation_random_occ_s2/.../50000_chkpt` | 排队 |

输出目录: `/root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/`

注意：有一个非致命 WARNING (No occ index entry for one task)，预计不影响结果。

### Step 3: vanilla_retrain_s0_eval — RUNNING (GPU 0)

PID 823300, Task 0 rollout 2/50，刚启动。预计 ~45 分钟完成。

### Checkpoint 路径全部确认存在 ✓

westd-34685 当前 GPU 分配:
- GPU 0: vanilla_retrain_s0_eval
- GPU 1: gradient_analysis_mixed_seed
- GPU 2: cutoff_25k_s1 (训练中)
- GPU 3: reverse_cutoff_s1 (训练中)

---
