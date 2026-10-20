# diagnose detach ln v2 s1 35 completion

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_v2_s1_35-completion_20260527T131912_result.json`
- **Structured JSON:** [`89721e2064150cc2831d.json`](../../sessions/89/89721e2064150cc2831d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**训练诊断结果：**
| 实验 | 状态 | 完成步数 | EXIT_CODE |
|------|------|---------|-----------|
| detach_ln_v2_s1_35 | 成功 | 50005/50005 | 0 |
| detach_ln_s4 | 成功 | 50005/50005 | 0 |

**Checkpoint 路径：**
- detach_ln_v2_s1_35: `/root/autodl-tmp/checkpoints/detach_ln_v2_s1/...--detach_ln_v2_s1--50000_chkpt`
- detach_ln_s4: `/root/autodl-tmp/checkpoints/detach_ln_s4/...--detach_ln_s4--50000_chkpt`

**已执行操作：**
- Registry: 两个训练实验 → ANALYZING (conclusion=success)
- Cron: 无活跃 cron 需删除
- Eval 已启动（westd-34685 tmux session）:
  - `detach_ln_v2_s1_35_eval` → cuda:0, MUJOCO_EGL_DEVICE_ID=0
  - `detach_ln_s4_eval` → cuda:1, MUJOCO_EGL_DEVICE_ID=1
  - 两个 eval 均为 50-rollout SafeLIBERO (libero_spatial, seed=42)

**注意：** `submit_training_job` 工具不可用，改用 tmux session 提交 eval。

---
