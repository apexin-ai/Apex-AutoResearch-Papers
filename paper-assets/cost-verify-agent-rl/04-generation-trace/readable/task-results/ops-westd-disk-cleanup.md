# ops westd disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-cleanup_20260517T182218_result.json`
- **Structured JSON:** [`e9e6397e75f93ed6d4a7.json`](../../sessions/e9/e9e6397e75f93ed6d4a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总：

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 240G (96%) | 96G (39%) |
| 可用 | 11G | 155G |
| **释放** | — | **144G** |

两个实验进程状态正常：
- **PID 40267** (gae_baseline_seed1) — 运行中，`python train.py --config-name _alfworld_reinforce_pp_baseline`
- **PID 85798** (gsweep_g050_h5_seed1) — 运行中，`python train.py --config-name _alfworld_gamma_sweep_g050_h5`

---
