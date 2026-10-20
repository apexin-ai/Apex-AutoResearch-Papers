# analysis v4 random fixed inject50 s1 r2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject50-s1-r2_20260516T000223_result.json`
- **Structured JSON:** [`13925506fd3cd3281443.json`](../../sessions/13/13925506fd3cd3281443.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被删除或未在当前 session 中创建）。

**结果：v4-random-fixed-inject50-s1-r2 失败**

- **原因**：CUDA OOM，step 5/1635 崩溃。bs=4 ga=2 仍然 OOM（30.63 GiB 已用，需再分配 4.25 GiB）
- **可能原因**：GPU 被其他进程占用（31.36 GiB 总量中 27.41 GiB 已被使用，而模型+LoRA 不应占这么多），或 `CUDA_VISIBLE_DEVICES` 未正确设置导致跑到了已被占用的 GPU 0 上
- **Registry**：已更新 → DONE, conclusion=failed
- **Cron**：当前 session 无此 cron，无需删除

如需 retry，建议先检查 cuda:1 是否被其他实验占用，并确认 `CUDA_VISIBLE_DEVICES=1` 是否在启动命令中正确传入。

---
