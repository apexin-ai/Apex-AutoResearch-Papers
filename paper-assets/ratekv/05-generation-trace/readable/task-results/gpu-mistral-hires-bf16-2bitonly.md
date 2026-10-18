# gpu mistral hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_mistral_hires_bf16_2bitonly_20260514T204003_result.json`
- **Structured JSON:** [`396dcfa92554ed098110.json`](../../sessions/39/396dcfa92554ed098110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

~24-26% across all shards at 7.4 min. Total ~3.3GB/13.5GB. Consistent ~7.5MB/s aggregate. ETA about 22 min. The download is proceeding normally — let me give a status summary now and you can check back later.

**Status summary:**

- **Script**: `run_mistral_hires_bf16_2bitonly.py` created on server and locally
- **Model**: Mistral-7B-v0.3 downloading from ModelScope (PID=259321), 3.3GB/13.5GB at ~7.5MB/s, ETA ~22 min
- **Architecture confirmed**: 32L × 8KV heads = 256 total, GQA 4:1, head_dim=128
- **Registry**: `mistral_hires_bf16_2bitonly` registered as RUNNING
- **GPU**: cuda:1 reserved (both GPUs currently idle)

**Next steps** (once download completes):
- Model path will be at `/root/autodl-tmp/models/mistral-7b-v0.3/LLM-Research/Mistral-7B-v0___3`
- Launch profiling: `cd /root/ratekv && python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/mistral-7b-v0.3/LLM-Research/Mistral-7B-v0___3 --gpu cuda:1`
- 256 heads × ~30s/head ≈ 2h profiling time
- Log: `/root/ratekv/logs/mistral_hires_bf16_2bitonly.log`

Download still in progress — want me to wait and launch the profiling automatically when it finishes?

---
