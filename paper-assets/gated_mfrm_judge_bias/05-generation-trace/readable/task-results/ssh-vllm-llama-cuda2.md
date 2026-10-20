# ssh vllm llama cuda2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vllm_llama_cuda2_20260522T011825_result.json`
- **Structured JSON:** [`e39594c745fe900628e0.json`](../../sessions/e3/e39594c745fe900628e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

### 产出汇总

| 项目 | 值 |
|------|------|
| PID | 122778 (APIServer) / 123152 (EngineCore) |
| 端口 | 8001 |
| 模型名 | `llama-3.3-70b-instruct` |
| GPU | cuda:2, 90104 MiB / 97887 MiB |
| tmux session | `vllm-llama` |
| KV cache | 150,128 tokens (最大并发 18.3x @ 8192 tokens) |

**API 测试**: `"Hello."` — 正常响应，延迟 ~1.7s（warmup 后）。

**注意事项**:
- 启动时需加 `VLLM_USE_FLASHINFER_SAMPLER=0`，因为 FlashInfer JIT 不识别 Blackwell GPU (sm_100)，已用 PyTorch-native sampler 替代
- vLLM 提示可用 `--quantization awq_marlin` 获得更快推理，当前用的是 `awq`

---
