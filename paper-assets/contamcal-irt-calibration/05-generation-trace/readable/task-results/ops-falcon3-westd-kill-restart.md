# ops falcon3 westd kill restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-westd-kill-restart_20260522T074741_result.json`
- **Structured JSON:** [`b7d88de6610dea3e7586.json`](../../sessions/b7/b7d88de6610dea3e7586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完毕。

## 报告

### 1. 旧进程终止
4 个旧进程全部 kill 成功（PID 577758/577836/577974/578223），SIGTERM 即停，无需 SIGKILL。

### 2. Checkpoint 清理
已删除 4 个错误 checkpoint 目录和 4 个 log 文件。

### 3. 新训练状态

| Dosage | exp_id | PID | GPU | CUDA_VISIBLE_DEVICES | VRAM | lr | Steps |
|--------|--------|-----|-----|---------------------|------|-----|-------|
| d000 | sft_falcon3_7b_d000_s42_v2 | 599902 | cuda:0 | 0 | 72.6 GB | **5e-5** | 3125 |
| d005 | sft_falcon3_7b_d005_s42_v2 | 600185 | cuda:1 | 1 | 95.9 GB | **5e-5** | ~3177 |
| d025 | sft_falcon3_7b_d025_s42_v2 | 600340 | cuda:2 | 2 | 71.4 GB | **5e-5** | 3384 |
| d050 | sft_falcon3_7b_d050_s42_v2 | 600596 | cuda:3 | 3 | 34.5 GB | **5e-5** | 3642 |

LR 验证：4 个进程的 `/proc/&lt;PID>/cmdline` 均确认 `--lr 5e-5`，代码 line 219 将 `args.lr` 传入 `learning_rate=`。LoRA alpha=32 全部正确。

### 4. 异常
无。旧 registry 条目已标记 DONE(failed)，新条目由 submit_training_job 自动创建为 RUNNING。

---
