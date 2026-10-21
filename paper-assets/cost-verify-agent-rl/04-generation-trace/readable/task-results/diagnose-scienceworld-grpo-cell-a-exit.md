# diagnose scienceworld grpo cell a exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld-grpo-cell-a-exit_20260520T135058_result.json`
- **Structured JSON:** [`effad21ef1d366de4737.json`](../../sessions/ef/effad21ef1d366de4737.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**Cell A 正常完成训练**，非异常退出。

| 项目 | 详情 |
|------|------|
| 状态 | **success** — 15/15 steps 全部完成 |
| Checkpoints | `global_step_5`, `global_step_10`, `global_step_15` 均保存于 `/root/autodl-tmp/checkpoints/scienceworld-cell-a/` |
| 关键 val 指标 | `val-core/unknown/reward/mean@303 = 0.1`, `val-env/ScienceWorldSG/non-zero/final_score = 1.0` |
| Traceback | 仅 W&B teardown atexit race condition，无害 |
| 时间线 | 20:44 启动 → 21:05 step5 ckpt → 21:27 step10 ckpt → 21:46 step15 ckpt + val + 退出 |

**GPU 当前状态**：Cell C 仍在运行（PIDs 774557/774558，已运行 ~1h07m，各占 ~45GB 显存）。Cell A 退出后 GPU 0,1 已被 Cell C 独占使用。

---
