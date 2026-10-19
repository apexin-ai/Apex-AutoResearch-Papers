# ssh check cuda0 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_cuda0_status_20260516T052230_result.json`
- **Structured JSON:** [`8ff5e52338c60ddaf18c.json`](../../sessions/8f/8ff5e52338c60ddaf18c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 状态 | 显存占用 | GPU利用率 | 进程 |
|-----|------|----------|-----------|------|
| cuda:0 | **空闲** | 0 / 97887 MiB | 100%* | 无 |
| cuda:1 | 占用 | 90947 / 97887 MiB | 100% | PID 205598 - bce_isocompute_v3_s42 训练 |

**cuda:0**：无 GPU 进程，显存 0 MiB 占用，空闲可用。GPU 利用率显示 100% 但无进程挂载，可能是 nvidia-smi 采样延迟，实际空闲。

**cuda:1**：bce_isocompute_v3_s42 正常运行中（PID 205597/205598），占用 ~91GB 显存。

**PID 194814**：已死。ROADMAP 中记录的 TEAL 30% eval 进程已结束。

---
