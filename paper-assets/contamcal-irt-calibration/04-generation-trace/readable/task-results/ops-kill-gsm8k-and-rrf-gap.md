# ops kill gsm8k and rrf gap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_gsm8k_and_rrf_gap_20260516T153700_result.json`
- **Structured JSON:** [`3e1c36b8e6dc25c42b26.json`](../../sessions/3e/3e1c36b8e6dc25c42b26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成：

### 1. cuda:5 Kill ✅
PID 806081 已终止。cuda:5 仅剩 PID 804791（Llama d100 SFT，20576 MiB）。

### 2. cuda:1 Llama eval v3 ✅ 已在运行
**PID 807025** — `python evaluate.py --model-path .../Llama-3.2-3B_d000_s42/merged --benchmarks gsm8k arc_challenge humaneval --mc-format aligned --output-dir .../eval_results/Llama-3.2-3B_d000_s42_aligned/ --batch-size 4`

占用 6838 MiB，无需重新提交。

### 3. RRF gap fill ✅ 无需操作
两个 model 的 merged 文件全部已存在：

| Model | mmlu | gsm8k | arc_challenge |
|-------|------|-------|---------------|
| Qwen2.5-3B_d100_a32_s42 | EXISTS | EXISTS | EXISTS |
| Qwen2.5-3B_d000_s123_a32 | EXISTS | EXISTS | EXISTS |

之前的审计信息已过时，gap 已被填补。

---
