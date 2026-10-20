# research n samples confound

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_n_samples_confound_20260515T200139_result.json`
- **Structured JSON:** [`c9ab8129f7fcf6ddbccf.json`](../../sessions/c9/c9ab8129f7fcf6ddbccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. Qwen3-8B n=8 CoNLL：**存在**

- **路径**: `output/exp002_conll2003/samples.jsonl`
- **模型**: `qwen3-8b-conll2003-merged`
- **配置**: n_samples=8, T=1.0, 3453 instances
- **greedy F1**: 0.9074
- **已有分析**: `n8_5signal_results.json`（SJ rho=0.4357, EM rho=0.4507）

### 2. Qwen3-8B n=8 SciERC：**存在**

- **路径**: `output/mvp_pilot_001/samples.jsonl`
- **模型**: `qwen3-8b-scierc-merged`
- **配置**: n_samples=8, T=1.0, 551 instances
- **greedy F1**: 0.6110

### 3. N-scaling 对比分析也已完成

`output/bootstrap_ci_nscaling/results.json` 包含 Qwen_CoNLL 和 Qwen_SciERC 的 n=8 vs n=16 bootstrap CI 对比：

| 数据集 | 信号 | rho_n8 | rho_n16 | Δρ | 95% CI |
|--------|------|--------|---------|------|--------|
| CoNLL | SJ | 0.4389 | 0.4496 | 0.011 | [-0.014, 0.035] |
| CoNLL | EM | 0.4523 | 0.4612 | 0.009 | [-0.015, 0.032] |
| SciERC | SJ | 0.3624 | 0.4280 | 0.066 | [0.004, 0.128] |
| SciERC | EM | 0.3339 | 0.3409 | 0.007 | [-0.049, 0.065] |

CoNLL 上 n=8→16 几乎无差异（CI 跨零）；SciERC 上 SJ 有微弱提升但绝对值仍小。**数据齐全，可直接用于控制组对比。**

---
