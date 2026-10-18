# ops cuda1 mistral results and next

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1_mistral_results_and_next_20260515T175212_result.json`
- **Structured JSON:** [`ebe7f88c9bd8f93f2291.json`](../../sessions/eb/ebe7f88c9bd8f93f2291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: Mistral Compounding Sweep — 完成 ✓

Registry 已更新 (conclusion=success + metrics)。

| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
|---|-----|-------|-------|-------|--------|-----|
| 0 | **7.1308** | 0 | 256 | 0 | 0 | 0.2500 |
| 2 | 7.1471 | 2 | 254 | 0 | 0 | 0.2490 |
| 4 | 7.1640 | 4 | 252 | 0 | 0 | 0.2480 |
| 8 | 7.2001 | 8 | 247 | 0 | 1 | 0.2490 |
| 16 | 7.3100 | 16 | 238 | 0 | 2 | 0.2480 |
| 32 | 7.4877 | 32 | 219 | 0 | 5 | 0.2490 |
| 64 | 7.5932 | 41 | 209 | 0 | 6 | 0.2476 |
| 128 | 7.5932 | 41 | 209 | 0 | 6 | 0.2476 |
| 256 | 7.5932 | 41 | 209 | 0 | 6 | 0.2476 |

**结论**：PPL 随 k 单调递增，k=0（全 4-bit）最优。budget=0.25 下 MCKP solver 在 k≥64 饱和（实际只分配 41 个 2-bit head + 6 个 16-bit head）。对 Mistral 而言，compounding（强制更多 2-bit）在此 budget 无收益。

### Part 2: cuda:1 下一个任务

- **cuda:0**：忙 (96%, 36894 MiB) — Yi/Mistral eval 在跑，不碰
- **cuda:1**：空闲 (0%, 3 MiB)
- **Phi-3 下载**：未完成（只有 config/tokenizer，无 safetensors 权重）
- **CodeLlama-7B 下载**：已启动 (PID 357563)，ModelScope `AI-ModelScope/CodeLlama-7b-hf` → `/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf/`，下载速度 ~2-3 MB/s，预计 30-60 分钟完成
- **监控**：`tail -5 /root/ratekv/logs/codellama_download.log`

**下一步**：CodeLlama 下载完成后，读 config.json 确认架构参数，基于 `run_llama_hires_bf16_2bitonly.py` 模板创建 profiling 脚本，CUDA_VISIBLE_DEVICES=1 提交到 cuda:1。

---
