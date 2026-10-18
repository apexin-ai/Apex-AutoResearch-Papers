# gpu gemma2 hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma2_hires_bf16_2bitonly_20260514T220044_result.json`
- **Structured JSON:** [`368c74c415aec2a51e2a.json`](../../sessions/36/368c74c415aec2a51e2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Profiling 已正常启动：

- **模型**: Gemma-2-9B bf16, 18.5GB GPU mem on cuda:0
- **Calibration**: 64 seqs x 2048 tokens (BOS-prepended, D044 修复生效)
- **Baseline PPL**: 7.3200
- **进度**: [1/336] L0H0 @2bit: delta=0.004034
- **预估时间**: ~1.3min/head × 336 heads ≈ **7.3h**（比预期的 1.9h 慢，因为 64seq×2048tok 数据量大，batch_size=2 需要 32 次 forward pass）
- **tmux session**: `gemma2_hires_bf16_2bitonly`
- **日志**: `/root/ratekv/logs/gemma2_hires_bf16_2bitonly.log`
- **Registry**: `gemma2_hires_bf16_2bitonly` → RUNNING

---
