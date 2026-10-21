# code arxiv bootstrap ci 3models

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arxiv_bootstrap_ci_3models_20260523T030224_result.json`
- **Structured JSON:** [`91b41522c269efa6de7c.json`](../../sessions/91/91b41522c269efa6de7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `artifacts/arxiv_2v3_bootstrap_ci.json`. Here's the summary:

## arXiv 2v3 Bootstrap CI Results (Crossscorer Features)

| Model | 2v3 AUC (OOF) | 95% CI | Boot Std | CI lower > θ=0.60 | Perm p |
|-------|---------------|--------|----------|-------------------|--------|
| **LLaMA-8B** | 0.6202 | [0.6047, 0.6352] | 0.0077 | **PASS** | 0.001 |
| **Mistral-7B** | 0.6075 | [0.5939, 0.6223] | 0.0072 | **FAIL** | 0.001 |
| **Qwen-7B** | 0.5986 | [0.5829, 0.6145] | 0.0078 | **FAIL** | 0.001 |

### K* (CI-based)
- LLaMA-8B: **K*=3** (2v3 CI lower 0.6047 > 0.60)
- Mistral-7B: **K*=2** (2v3 CI lower 0.5939 < 0.60)
- Qwen-7B: **K*=2** (2v3 CI lower 0.5829 < 0.60)

### Cross-check (0v1, 1v2 pairs — all PASS)
| Model | 0v1 AUC | 1v2 AUC |
|-------|---------|---------|
| LLaMA-8B | 0.9627 | 0.8427 |
| Mistral-7B | 0.9798 | 0.8138 |
| Qwen-7B | 0.9573 | 0.8163 |

### 关键发现

**"arXiv K\*=3 across 3 families" claim 无法在 95% CI 下成立** — 只有 LLaMA-8B 的 2v3 CI lower bound (0.6047) 超过 θ=0.60。Mistral-7B 和 Qwen-7B 在 crossscorer 设定下 2v3 的 CI lower bound 分别为 0.5939 和 0.5829。

**注意**：这些结果基于 `data/exp_arXiv_*_crossscorer/features.csv` 中的现有特征。Pipeline 的 `--skip_generation` 模式检测到 features.csv 已存在后跳过了特征重新提取。域表中的自评 AUC（LLaMA 0.622, Mistral 0.628, Qwen 0.626）高于 crossscorer AUC，如果需要基于自评特征的 bootstrap CI，需要对 `data/exp_arXiv_*`（非 crossscorer）目录运行。

---
