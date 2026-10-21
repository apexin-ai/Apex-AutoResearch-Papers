# analysis cpu parallel tasks

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cpu_parallel_tasks_20260518T092937_result.json`
- **Structured JSON:** [`23fbd4b6faef821cc68b.json`](../../sessions/23/23fbd4b6faef821cc68b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总结果

### 任务 1: Within-Instance ρ(LP, F1) 三数据集对比表

| Dataset | Model | n_instances (gold-filtered) | n_valid_rho | Median ρ(LP,F1) | Mean ρ(LP,F1) | % Positive ρ | % LP-best=F1-best |
|---------|-------|-----------------------------|-------------|-----------------|---------------|--------------|-------------------|
| SciERC | Qwen | 529 | 435 | **0.2624** | 0.1791 | 64.14% | 58.41% |
| Few-NERD | Qwen | 32,565 | 28,055 | **0.6667** | 0.5096 | 84.43% | 71.24% |
| CoNLL | Qwen | 2,756 | 1,124 | **0.5055** | 0.3457 | 77.85% | 89.01% |
| CoNLL | LLaMA | 2,756 | 298 | **0.5117** | 0.2172 | 65.10% | 96.01% |

注：n_valid_rho < n_instances 因为排除了 constant-LP 和 constant-F1 的 instances（LLaMA CoNLL 仅 298/2756 有变异，说明高 degeneracy）。

---

### 任务 2: DALS 跨模型验证 (τ=0.05)

| Dataset | Greedy F1 | LP-Sel F1 | DALS F1 | DALS Gain | Degen Rate | 95% CI |
|---------|-----------|-----------|---------|-----------|------------|--------|
| **CoNLL Qwen N=8** | 90.88 | — | 90.01 | **-0.87pp** | 40.4% | [-1.26, -0.50] |
| **CoNLL LLaMA N=8** | 92.42 | — | 92.39 | **-0.04pp** | 86.8% | [-0.16, +0.05] |
| **SciERC Qwen N=8** | 64.41 | — | 65.55 | **+1.14pp** | 60.3% | [+0.31, +2.02] |
| SciERC LLaMA seed123 | 64.79 | — | 64.73 | -0.06pp | 59.2% | [-1.06, +0.92] |
| SciERC LLaMA seed456 | 64.83 | — | 65.07 | +0.24pp | 55.8% | [-0.63, +1.10] |
| SciERC LLaMA seed42_r1024 | 64.86 | — | 64.76 | -0.10pp | 55.4% | [-0.91, +0.76] |
| SciERC LLaMA seed456_r1024 | 64.84 | — | 65.22 | +0.38pp | 57.1% | [-0.36, +1.18] |

关键发现：
- LLaMA CoNLL 的 degeneracy rate 极高 (86.8%)，导致 DALS 几乎退化为 greedy
- LLaMA SciERC 的 DALS gain 在不同 seed 间不稳定（-0.10 到 +0.38pp），CI 都跨零
- 只有 Qwen SciERC 有统计显著的正 gain

---

### 任务 3: LLaMA CoNLL N=16 3-seed 数据

6 个 N=16 目录全部有 `samples.jsonl`（3453 instances, N=16）：

| 目录 | has analysis | greedy_f1 | logprob ρ (full) | SJ ρ (full) | best_of_n logprob |
|------|-------------|-----------|-----------------|-------------|-------------------|
| `exp_017_llama_conll_n16` (default seed) | all_signals_report | 0.9243 | 0.3058 | 0.4642 | 0.9250 |
| `exp_017_llama_conll_n16_s123` | all_signals_report | 0.9242 | 0.3161 | 0.4698 | 0.9253 |
| `exp_017_llama_conll_n16_s456` | all_signals_report | 0.9243 | 0.3078 | 0.4552 | 0.9243 |
| `exp_017_llama_conll_n16_r1024` | report only | — | — | — | — |
| `exp_017_llama_conll_n16_s123_r1024` | report only | — | — | — | — |
| `exp_017_llama_conll_n16_s456_r1024` | report only | — | — | — | — |

3 个 non-r1024 seed 都有完整的 `all_signals_report.json`，N=8→N=16 delta 显示：SC signals (SJ/FK/EM) 的 ρ/AUROC 稳定提升约 +0.02~0.04，但 logprob 几乎不变（delta ~ 0）。

r1024 variants 只有 `report.json`，没有 `all_signals_report.json`（没跑过 full signal analysis）。

所有结果已保存到 `output/within_instance_rho_table.json`、`output/dals_cross_model.json`、`output/llama_conll_n16_check.json`。

---
