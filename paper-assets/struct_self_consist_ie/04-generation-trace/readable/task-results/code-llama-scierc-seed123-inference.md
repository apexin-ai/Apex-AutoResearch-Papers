# code llama scierc seed123 inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_scierc_seed123_inference_20260518T190455_result.json`
- **Structured JSON:** [`9bdc4e3a4dde9aca4fbc.json`](../../sessions/9b/9bdc4e3a4dde9aca4fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。分析报告：

## LLaMA-3.1-8B SciERC seed=123 — 结果

推理数据已存在于 `output/exp_018_llama_scierc_seed123/samples.jsonl`（551 instances, N=8, T=1.0, logprobs），跳过重跑。

### 5-Signal (full split, n=529)

| Signal | ρ | AUROC |
|--------|------|-------|
| voting_conf | **0.4193** | 0.7159 |
| SJ | 0.3552 | 0.7092 |
| FK | 0.2897 | 0.6678 |
| EM | 0.2844 | **0.7468** |
| logprob | 0.1970 | 0.5839 |

- Greedy F1: 0.6454
- Oracle F1: 0.7657
- Headroom: **12.04pp**

### DGS

| Metric | Value |
|--------|-------|
| Degeneracy | 141/529 (26.7%) |
| DGS F1 | 0.6416 |
| DGS - Greedy | **-0.38pp** (CI: [-1.62, +0.78]) |
| NonDegen LP - Greedy | -0.51pp (CI: [-2.26, +1.19]) |

DGS 未能改善 greedy baseline，LP selection 在非退化实例上略微负向。与 LLaMA seed=42/456 结果一致。

输出路径: `output/exp_007_llama_scierc_seed123/`（symlink + 分析报告）
Registry: `exp_007_llama_scierc_seed123` (DONE, negative)

---
