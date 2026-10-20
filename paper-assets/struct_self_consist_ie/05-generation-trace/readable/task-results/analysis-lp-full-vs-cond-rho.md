# analysis lp full vs cond rho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lp_full_vs_cond_rho_20260515T160119_result.json`
- **Structured JSON:** [`ca7939aecbbb8de46682.json`](../../sessions/ca/ca7939aecbbb8de46682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LP Rho 对比

### T=0.7 (exp_lp_scierc_t07) — Qwen SciERC NER, N=8

| 信号 | full rho | cond rho | full n | cond n |
|------|----------|----------|--------|--------|
| **LP (logprob)** | **0.2494** | **0.1852** | 529 | 477 |
| SoftJaccard | 0.3645 | 0.3625 | 529 | 477 |
| Fleiss Kappa | 0.2890 | 0.2549 | 529 | 477 |

### T=1.0 (exp_012_rerun_1024) — Qwen SciERC Joint, N=8

**NER:**

| 信号 | full rho | cond rho | full n | cond n |
|------|----------|----------|--------|--------|
| **LP (logprob)** | **0.2052** | **0.1538** | 529 | 477 |
| SoftJaccard | 0.3599 | 0.3113 | 529 | 477 |
| Fleiss Kappa | 0.2665 | 0.1761 | 529 | 477 |

**RE:**

| 信号 | full rho | cond rho | full n | cond n |
|------|----------|----------|--------|--------|
| **LP (logprob)** | **0.2662** | **0.0112** (p=0.86, n.s.) | 397 | 238 |
| SoftJaccard | 0.2503 | 0.2457 | 397 | 238 |
| Fleiss Kappa | 0.2752 | 0.1139 (p=0.08, n.s.) | 397 | 238 |

### LP full vs cond 差异汇总

| 实验 | subtask | LP full rho | LP cond rho | Δ |
|------|---------|-------------|-------------|---|
| T=0.7 | NER | 0.249 | 0.185 | -0.064 |
| T=1.0 | NER | 0.205 | 0.154 | -0.051 |
| T=1.0 | RE | 0.266 | 0.011 | -0.255 |

### 数据来源
- T=0.7: `exp_lp_scierc_t07/report.json` → `logprob_baseline.full.rho` / `logprob_baseline.conditional.rho`
- T=1.0: `exp_012_rerun_1024/report.json` → `ner_logprob_baseline.full.rho` / `ner_logprob_baseline.conditional.rho`（RE 同理前缀 `re_`）
- `analysis_round8/` 中的 `seed456_lp_range.json` 和 `exp017_t07_lp_range.json` 是 LP range 分布统计（tied fraction 等），不含 rho 对比。`exp017_t07_lp_range.json` 有一组 LLaMA CoNLL 的信号 rho（LP full rho=0.295），但那是不同模型/数据集。

---
