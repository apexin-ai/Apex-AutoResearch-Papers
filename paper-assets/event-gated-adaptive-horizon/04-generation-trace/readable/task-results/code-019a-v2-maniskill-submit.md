# code 019a v2 maniskill submit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_019a_v2-maniskill-submit_20260516T201059_result.json`
- **Structured JSON:** [`190405fb559943a29e1c.json`](../../sessions/19/190405fb559943a29e1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 项目 | 状态 |
|------|------|
| ManiSkill3 环境 | mani_skill 3.0.1，import 正常 |
| 集成代码 | `envs/maniskill.py` + `resolve_physical_device()` 就绪 |
| 配置 | 使用 `maniskill_state` config (state-based, 无 CNN) |
| 实验提交 | **成功** |
| PID | 614975 |
| log_path | `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline.log` |
| 初始 eval | eval_return=1.1, eval_length=200 (step 2500) |
| registry | `exp_019a_v2_pickcube_baseline` → RUNNING |

训练已正常进入 training loop，`cuda:1` + `MUJOCO_EGL_DEVICE_ID=1` 配合 `resolve_physical_device` 正确工作。

---
