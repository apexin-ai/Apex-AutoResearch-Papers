# diagnose exp029 seed300 step5 ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_seed300_step5_ood_eval_20260522T183123_result.json`
- **Structured JSON:** [`f69ff8b0301da01bedb3.json`](../../sessions/f6/f69ff8b0301da01bedb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，已写入 `artifacts/diag_exp029_seed300_step5_ood_eval.md`。

**根因**：不是 OOM/checkpoint/代码 bug。OOD eval 的 134 个任务实际已跑完，但在 `_validate()` 返回结果前，`wandb.log()` 尝试将 `wandb.Table` 序列化到 `/tmp/tmpjqaf9lrywandb-media/` 时失败——该目录已被清理（`wandb-core` 进程已变僵尸）。异常未捕获，导致整个 `_validate()` 崩溃，指标未返回、未上报 W&B。

**残留进程**：`ray::TaskRunner`（PID 433097, 60% CPU）和 `wandb-core`（PID 433602, zombie）仍在服务器上。

**修复**：(1) kill 残留进程 (2) 在 `ragen/utils.py:log_generations_to_wandb` 加 try-except 防止 wandb 日志失败拖垮 eval (3) 可选设 `WANDB_DATA_DIR` 到数据盘避免 /tmp 清理问题 (4) 重跑。

---
