# code mistral hires pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_hires_pipeline_20260514T023143_result.json`
- **Structured JSON:** [`bd9a2f4e3cd94cd954f1.json`](../../sessions/bd/bd9a2f4e3cd94cd954f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral hires pipeline 已启动并注册。

**状态总结：**
- **PID**: 173653 (python), cuda:1 (物理 GPU-84da)
- **Phase 1 进行中**: L0H0 已完成 (1/256), ETA ~168 min (~2.8h)
- **Baseline calibration PPL**: 5.8674
- **配置**: 64 seqs × 2048 tokens, budget=0.25, max_2bit=18, bf16, eager attention
- **修复**: 适配了新版 transformers 的 Mistral attention API（`position_embeddings` 参数替代 `rotary_emb` 属性）
- **监控**: `tail /tmp/mistral_hires_launch.log`（主日志有缓冲延迟）
- **Llama (cuda:0, PID 171900)**: 未受影响

---
