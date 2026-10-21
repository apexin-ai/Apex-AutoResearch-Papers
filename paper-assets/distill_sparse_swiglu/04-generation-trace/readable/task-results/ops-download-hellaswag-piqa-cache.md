# ops download hellaswag piqa cache

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-hellaswag-piqa-cache_20260518T232040_result.json`
- **Structured JSON:** [`d3b39205b6035322d9b5.json`](../../sessions/d3/d3b39205b6035322d9b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**
- **hellaswag** (`Rowan/hellaswag`): 下载成功，63MB，缓存在 `/root/autodl-tmp/.hf_cache/datasets/Rowan___hellaswag/`
  - train: 39905, test: 10003, validation: 10042
- **piqa** (`baber/piqa`): 下载成功，5.2MB，缓存在 `/root/autodl-tmp/.hf_cache/datasets/baber___piqa/`
  - train: 16113, validation: 1838, test: 3084

注意：直连 huggingface.co 不通（Network unreachable），通过 `HF_ENDPOINT=https://hf-mirror.com` 镜像下载。lm_eval 的 piqa task 配置使用的是 `baber/piqa`（非 `ybisk/piqa`），已正确缓存。离线模式下 lm_eval 运行时应可直接命中缓存。

---
