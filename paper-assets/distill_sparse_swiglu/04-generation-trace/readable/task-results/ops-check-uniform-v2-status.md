# ops check uniform v2 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-uniform-v2-status_20260518T130014_result.json`
- **Structured JSON:** [`2fa61853d1b5029dec11.json`](../../sessions/2f/2fa61853d1b5029dec11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新到 RUNNING。

## 状态汇总

| 实验 | 状态 | 进度 | GPU |
|------|------|------|-----|
| **kl30_s123_uniform_v2** | RUNNING | MMLU 评估中 (task 4/5)，已完成 wikitext2 + arc + winogrande | westd-41718 cuda:0, PID 72660 |
| **kl30_s456_uniform_v2** | RUNNING | MMLU 评估中 (task 4/5)，已完成 wikitext2 + arc + winogrande | westd-41718 cuda:1, PID 72798 |

服务重启后进程存活，tmux session 完好。两个实验都在 MMLU 的 subtask 批次处理阶段，剩 MMLU 尾部 + GSM8K。预计还需 10-20 分钟完成。

---
