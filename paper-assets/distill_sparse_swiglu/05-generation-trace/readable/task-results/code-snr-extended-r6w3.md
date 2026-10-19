# code snr extended r6w3

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_snr_extended_r6w3_20260518T015700_result.json`
- **Structured JSON:** [`1a01328b75c815d6cb6b.json`](../../sessions/1a/1a01328b75c815d6cb6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已成功创建并提交运行：

- **脚本**: `/root/distill_sparse_swiglu/scripts/gradient_snr_extended.py`
- **PID**: 92073（实际 python 子进程）
- **日志**: `/root/distill_sparse_swiglu/logs/snr_extended_r6w3.log`
- **GPU**: cuda:0，已开始 Phase 1 KL distillation，step 0 snapshot 已产出
- **输出**: 完成后写入 `/root/distill_sparse_swiglu/artifacts/snr_extended_results.json`

注意：`submit_training_job` 工具在当前环境不可用，已按 C002 约束用 nohup + 日志重定向启动。300 steps (batch_size=4, seq_len=2048) 预计运行约 15-20 分钟。

---
