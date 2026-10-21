# experiment cwm rank32 resubmit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_cwm-rank32-resubmit_20260515T124842_result.json`
- **Structured JSON:** [`35510164d850f0ffdc15.json`](../../sessions/35/35510164d850f0ffdc15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**`cwm-rank32-ablation` (PID 368823) 未被 killed，正在 GPU 0 上正常训练。**

| 项目 | 状态 |
|------|------|
| PID 368823 | 活跃，`/proc/368823/cmdline` 确认是 `train_cwm_baseline.py --lora_rank 32` |
| GPU 0 | 18238MiB / 32607MiB, 59% util |
| 进度 | step 324/1434 (22%), ~3.3s/it |
| 预计完成 | ~60min (服务器时间 ~21:50) |
| 配置 | bs=2, ga=16, rank=32, seed=42 — 与 baseline 一致（仅 rank 不同） |

**`cwm-4b-rank32-ablation` (PID 369497) 是重复提交**，在第一个进程还占 GPU 0 时启动，因显存争夺仅跑到 step 38 就死了（速度 6.5s/it 约 2x 正常值）。

**不需要重新提交任务。** Registry hypothesis 字段已更新标注 PID 368823 仍在运行。

唯一的小问题：运行中的命令未串联 eval。训练完成后需要手动或由 cron 触发 eval。

---
