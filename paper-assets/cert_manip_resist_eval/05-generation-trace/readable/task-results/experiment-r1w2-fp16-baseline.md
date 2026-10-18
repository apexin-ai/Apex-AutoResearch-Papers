# experiment r1w2 fp16 baseline

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1w2-fp16-baseline_20260524T163008_result.json`
- **Structured JSON:** [`127184a9d27aaff39218.json`](../../sessions/12/127184a9d27aaff39218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Files are growing — 10MB -> 20MB for two shards, 180MB -> 200MB for the largest. Download speed is ~10MB/s aggregate. Each shard is ~2.5GB, so total ~8GB will take about 13 minutes. The download is progressing fine.

This is a long-running job (6 models, each requiring model download + inference). The entire run will likely take 2-3 hours including downloads and evaluations. The job is running in tmux and will checkpoint after each model.

Status summary:
- **Job**: `r1w2-fp16-baseline` running in tmux on seetacloud-rtx6000
- **Current**: Downloading Qwen2.5-14B-Instruct-AWQ weights (~200MB/8GB done)
- **Pipeline**: 6 models total, with checkpoint/resume. First 3 get both AWQ+FP16, last 3 AWQ-only
- **Output**: `/root/cert_manip_resist_eval/artifacts/results/plan001/fp16_baseline.json`

I'll check back on progress periodically. Would you like me to monitor it now, or shall I check later?

---
