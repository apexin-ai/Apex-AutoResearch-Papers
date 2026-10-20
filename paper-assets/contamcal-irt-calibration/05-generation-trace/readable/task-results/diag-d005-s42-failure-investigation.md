# diag d005 s42 failure investigation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d005_s42_failure_investigation_20260516T015856_result.json`
- **Structured JSON:** [`39dd89c356102e27a57c.json`](../../sessions/39/39dd89c356102e27a57c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**exp_001_sft_3B_d005_s42_a32 训练已成功完成，EXIT_CODE=129 是误报。**

| 项目 | 详情 |
|------|------|
| 根因 | SIGHUP 发生在 Python 进程正常退出之后，来自 tmux shell 清理 |
| 训练进度 | 3177/3177 steps (100%), epoch=1.0 |
| 最终 loss | 1.0822, mean_token_accuracy=0.7511 |
| 训练时长 | 14913s (~4.14h) |
| Checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter` (119MB, lora_alpha=32 已确认) |

**无需重提交。** Registry 已更新为 conclusion=success，checkpoint_path 和 metrics 已补全。该 checkpoint 可直接用于下游 eval 和 signal 计算。

---
