# analysis exp 018 llama scierc seed42 r1024

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_018_llama_scierc_seed42_r1024_20260515T061759_result.json`
- **Structured JSON:** [`24dd615e1c682e91d766.json`](../../sessions/24/24dd615e1c682e91d766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。下面汇总跨 seed 对比。

## 分析结果

### exp_018_llama_scierc_seed42_r1024 — **DONE / success**

551 实例，N=8，T=1.0，LLaMA-3.1-8B-SciERC-merged，joint (NER+RE)

### NER 5-signal（full split, n=529）

| Signal | ρ | τ | AUROC |
|---|---|---|---|
| **voting_conf** | **+0.405** | 0.304 | 0.697 |
| SJ | +0.310 | 0.229 | 0.668 |
| EM | +0.259 | 0.197 | **0.717** |
| FK | +0.235 | 0.176 | 0.607 |
| logprob | +0.150 | 0.109 | 0.532 |

NER SJ ρ(0.310) > logprob ρ(0.150) → **structural signals 胜出**

### RE 5-signal（full split, n=397）

| Signal | ρ | τ | AUROC |
|---|---|---|---|
| **voting_conf** | **+0.384** | 0.297 | 0.734 |
| logprob | +0.316 | 0.233 | 0.631 |
| FK | +0.303 | 0.234 | 0.691 |
| SJ | +0.275 | 0.210 | **0.724** |
| EM | +0.168 | 0.128 | **0.770** |

RE SJ ρ(0.275) < logprob ρ(0.316)，但 SJ AUROC(0.724) > logprob AUROC(0.631)

### 跨 3-seed 对比（NER SJ full ρ）

| Seed | SJ ρ | logprob ρ | SJ - logprob |
|---|---|---|---|
| 42 (r1024) | 0.310 | 0.150 | **+0.159** |
| 123 | 0.355 | 0.197 | **+0.158** |
| 456 (r1024) | 0.310 | 0.139 | **+0.171** |
| **Mean** | **0.325** | **0.162** | **+0.163** |
| CV | 8.1% | 18.9% | — |

**3 个 seed 全部 NER SJ > logprob，优势稳定 (CV 8.1%)，均值差距 +0.163 pp。**

---
