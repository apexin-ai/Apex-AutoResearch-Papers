# gpu exp 069 mistral logiqa200

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-069-mistral-logiqa200_20260519T114529_result.json`
- **Structured JSON:** [`b6ae54dae38ad1e43692.json`](../../sessions/b6/b6ae54dae38ad1e43692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-069 部署完成，全量实验正在运行。

**部署摘要：**
- **vLLM**: tmux `exp069_vllm`, Mistral-7B-Instruct-v0.3, cuda:1, port 8001
- **实验**: tmux `exp-069-mistral-logiqa200`, 200 条 LogiQA, K=12, T=0.7, seed=42
- **Dry-run 结果**: 5 条通过，SICA=40% SC=20% (Δ=+20pp)，无 OOM/crash
- **输出**: `results/exp069_mistral_logiqa200/exp069_results.json`
- **预估运行时间**: ~80 分钟 (基于 dry-run 5 条 ~2 分钟推算)
- **注**: 清理了已完成的 exp066_vllm (Qwen2.5-14B, GPU 1 idle) 和 exp033/034/035 的 finished sessions

---
