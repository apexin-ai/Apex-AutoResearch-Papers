# analyze collect results and latex

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_collect-results-and-latex_20260518T211717_result.json`
- **Structured JSON:** [`9c08f85b8e2d80050b2a.json`](../../sessions/9c/9c08f85b8e2d80050b2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 实验状态

| 实验 | 状态 | 进程 |
|------|------|------|
| exp_code_qwen1b5 | **Crashed → Fixed → Completed** | PID 84256 已退出，手动重跑 analysis 成功 |
| exp_qwen_retrain_chain | **Running** (bootstrap CI 2/4) | PID 86205 活跃 |
| exp_code_llama8b | **Running** (depth 1, 27%) | PID 96335 活跃 |

### exp_code_qwen1b5 (Code domain, Qwen2.5-1.5B) — Completed

| Pair | AUC | 95% CI | JSD |
|------|-----|--------|-----|
| 0 vs 1 | 0.9388 | [0.929, 0.949] | 0.0814 |
| 1 vs 2 | 0.7382 | [0.709, 0.767] | 0.0443 |
| 2 vs 3 | 0.5300 | [0.514, 0.546] | 0.0038 |
| 3 vs 4 | 0.5022 | [0.486, 0.518] | 0.0033 |
| 4 vs 5 | 0.5219 | [0.510, 0.534] | 0.0030 |

**K\*=2** (θ=0.60). Ordinal 6-class accuracy=0.359, MAE=1.204. Top features: freq_entropy, surp_d2_mean, surp_d1_mean.

Bug fix: `run_pipeline.py:462` — `int(doc_id)` failed on string IDs (`code_py_0`). Patched with try/except fallback to string array.

### exp_qwen_retrain_chain (Qwen2.5-1.5B retrain-chain) — Running

| Pair | AUC | 95% CI | JSD |
|------|-----|--------|-----|
| 0 vs 1 | 0.9838 | [0.980, 0.988] | 0.2263 |
| 1 vs 2 | 0.8969 | [0.890, 0.904] | 0.1046 |
| 2 vs 3 | 0.8100 | [0.799, 0.821] | 0.0752 |
| 3 vs 4 | 0.7624 | [0.744, 0.781] | 0.0654 |

**K\*≥4** (θ=0.60, all pairs > 0.60). Bootstrap CI 正在运行，已完成 2/4 pairs (~30min/pair)，预计再 ~60min 完成。

### exp_code_llama8b — Running

- 当前: depth 1 generation, 375/1375 batches (27%)
- 已有: depth_0.jsonl (5500 samples)
- GPU 2: 94% utilization, 15981 MiB
- 每 batch ~5.5s → depth 1 剩余 ~1h40m, 总共 5 个 depth + analysis 预计还需 ~10h

### GPU 利用率

| GPU | Utilization | Memory |
|-----|-------------|--------|
| 0 | 0% | 3403 MiB (retrain_chain bootstrap, CPU-bound) |
| 1 | 0% | 0 MiB |
| 2 | 94% | 15981 MiB (llama8b generation) |
| 3 | 0% | 0 MiB |

### LaTeX tables

- `artifacts/exp_code_qwen1b5/paper/code_domain_results.tex`
- `artifacts/exp_qwen_retrain_chain/paper/qwen_retrain_results.tex`

CI 列使用 5-fold CV std (mean ± 1.96σ)。exp_qwen_retrain_chain 的 bootstrap CI 完成后可更新。

---
