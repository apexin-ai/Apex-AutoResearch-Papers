# code run benchmark 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run_benchmark_34887_20260519T170507_result.json`
- **Structured JSON:** [`f65f29e1c7da2ff68d07.json`](../../sessions/f6/f65f29e1c7da2ff68d07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Benchmark 已成功启动。**

- **PID**: 123470 (Python 进程)
- **服务器**: westd-34887, cuda:0
- **状态**: 模型加载完成，正在跑各 (batch_size, seq_len) 组合的计时
- **已完成**: batch_size=1, seq_len=512（dense/mask_multiply/sparse/predictor_only 均有结果，flashinfer 模式被跳过 — "masks not loaded or unknown mode"）
- **正在跑**: batch_size=1, seq_len=2048
- **日志**: `logs/flashinfer_benchmark.log`
- **注意**: `flashinfer_30` 和 `flashinfer_50` 被跳过了（"Skipping flashinfer_30/50 (masks not loaded or unknown mode)"），这可能是需要关注的问题。

---
