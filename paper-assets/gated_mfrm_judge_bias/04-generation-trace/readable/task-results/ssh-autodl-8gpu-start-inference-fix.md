# ssh autodl 8gpu start inference fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_8gpu_start_inference_fix_20260522T110023_result.json`
- **Structured JSON:** [`7085fe90d950e12c06bf.json`](../../sessions/70/7085fe90d950e12c06bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

**Inference (running on autodl-8gpu, 4x RTX PRO 6000 Blackwell, 96GB each):**

| Model | GPU | Progress | Speed |
|-------|-----|----------|-------|
| Qwen3-8B | GPU 0 | ~15% (75/500) | ~450 tok/s output |
| gemma-2-9b-it | GPU 1 | 36% (181/500) | ~478 tok/s output |

**Downloads (ModelScope, ~700KB/s via AutoDL proxy):**

| Model | Status |
|-------|--------|
| Llama-3.1-8B-Instruct | 4/4 safetensors in temp dir, nearly done |
| Qwen2.5-7B-Instruct | 12MB/~15GB, early stage |
| Mistral-7B-Instruct-v0.3 | Not started yet (queued after Qwen2.5) |

**Key fix applied:** vLLM 0.21.0 + FlashInfer 0.6.8 fails on Blackwell SM 12.0 (`check_cuda_arch()` can't detect the arch). Fixed by setting `VLLM_USE_FLASHINFER_SAMPLER=0`. This env var is now in the orchestrator script (`run_remaining.sh`), which watches for Llama/Qwen2.5/Mistral downloads and auto-launches them on GPUs 2-3.

**What's running:**
- `orchestrator2` tmux session — waits for remaining downloads, launches inference automatically
- 2 ModelScope download processes still active (PIDs 98593, 102451)
- Both inference processes healthy and generating

Gemma should finish in ~5min, Qwen3-8B in ~20min. Llama download should complete within the hour. Qwen2.5 and Mistral will take several more hours at current speeds.

---
