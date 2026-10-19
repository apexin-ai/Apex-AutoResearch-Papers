# eval resubmit 30pct v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_resubmit_30pct_v2_20260516T015649_result.json`
- **Structured JSON:** [`4cb08de54459ea348a5e.json`](../../sessions/4c/4cb08de54459ea348a5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已通过上次失败点。状态：

- **PID**: 191335
- **GPU**: cuda:0
- **tmux session**: lm_eval_kl_30pct_s42
- **日志**: `~/runs/distill_sparse_swiglu/lm_eval_kl_30pct_s42.log`

模型加载成功，WikiText-2 calibration data 加载成功（32 sequences），正在计算 TEAL global masks (sparsity=0.3)。上次失败根因是缺少 `source /etc/network_turbo`，本次已修复，同时配置了 `HF_HOME=/root/autodl-tmp/.hf_cache` 指向缓存目录。

---
