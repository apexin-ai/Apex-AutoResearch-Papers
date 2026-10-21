# ssh fix qwen download deploy vllm

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_qwen_download_deploy_vllm_20260522T023333_result.json`
- **Structured JSON:** [`939ba013e48c17c0ec8f.json`](../../sessions/93/939ba013e48c17c0ec8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**下载修复**：缺失的 `model-00001-of-00011.safetensors` (3.7GB) 通过 ModelScope CDN 下载完成，11/11 分片齐全。

**vLLM 部署**：
- 端口 8002，cuda:3，`served-model-name: qwen2.5-72b-instruct`
- PID 161427，模型 38.76 GiB，KV cache 137,680 tokens
- API 验证通过：`curl localhost:8002/v1/models` 返回 `qwen2.5-72b-instruct`

**遇到的问题**：FlashInfer JIT 不识别 Blackwell sm120 架构（误报 "requires sm75 or higher"），通过 `VLLM_USE_FLASHINFER_SAMPLER=0` 绕过。

---
