# code gpu status and mistral launch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu_status_and_mistral_launch_20260514T020231_result.json`
- **Structured JSON:** [`53fec95917f9a768f718.json`](../../sessions/53/53fec95917f9a768f718.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### cuda:0 — Llama-3.1-8B recovery
- **PID**: 169686, tmux session: `llama_recovery`
- **利用率**: 85%, 16510MiB
- **状态**: Phase 1-2 已完成（profiling 768/768 + MCKP solver），原 Phase 3 eval 因 HF Hub 离线失败崩溃。恢复脚本 `run_llama_eval_recovery.py` 已提交，加载缓存数据集成功，正在跑 eval
- **MCKP 结果**: bit_dist={4:244, 8:4, 2:8}, memory_ratio=0.2500, distortion=0.2695

### cuda:1 — Mistral-7B-v0.3 full pipeline
- **PID**: 169768, tmux session: `mistral_pipeline`
- **利用率**: 95%, 17218MiB
- **状态**: Phase 1 profiling 进行中（768 profiles to go, ~7min）

### 采取的行动
1. **修复 `eval_ppl.py`**: 添加 arrow 文件 fallback，防止 HF Hub 不可达时 crash
2. **清理旧进程**: 终止了残留的 `mistral_full_pipeline` tmux session (PID 169384)
3. **写恢复脚本**: `run_llama_eval_recovery.py` — 跳过 profiling，加载 `llama_profiling_results.json`，re-solve MCKP，只跑 eval
4. **并行提交**: Llama recovery → cuda:0, Mistral pipeline → cuda:1
5. **Registry 已更新**: mistral_full_pipeline → RUNNING, llama_full_pipeline notes 更新

---
