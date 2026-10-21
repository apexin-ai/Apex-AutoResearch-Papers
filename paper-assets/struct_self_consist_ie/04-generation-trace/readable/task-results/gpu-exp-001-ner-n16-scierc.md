# gpu exp 001 ner n16 scierc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_001_ner_n16_scierc_20260514T114538_result.json`
- **Structured JSON:** [`5a9ce949a6a86543ea87.json`](../../sessions/5a/5a9ce949a6a86543ea87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `exp_001_ner_n16_scierc` 全部完成。

## 结果汇总

**配置:** ft_002_v2 merged model, SciERC test, N=16, T=0.7, seed=42, 200 instances, logprobs=yes

### 5 类 Confidence Signal 排名

**NER (n=193):**

| Signal | ρ_spearman | τ_kendall | AUROC |
|---|---|---|---|
| voting_confidence | **+0.401** | +0.301 | 0.675 |
| soft_jaccard | +0.384 | +0.287 | 0.671 |
| exact_match_rate | +0.362 | +0.267 | 0.666 |
| logprob | +0.314 | +0.227 | 0.639 |
| fleiss_kappa | +0.306 | +0.229 | 0.670 |

**RE (n=155):**

| Signal | ρ_spearman | τ_kendall | AUROC |
|---|---|---|---|
| voting_confidence | **+0.448** | +0.336 | **0.730** |
| soft_jaccard | +0.333 | +0.256 | 0.684 |
| logprob | +0.310 | +0.227 | 0.658 |
| fleiss_kappa | +0.286 | +0.232 | 0.680 |
| exact_match_rate | +0.225 | +0.171 | 0.611 |

### N-scaling (N=8 → N=16)

- **RE:** 全部信号显著提升 Δρ = +0.07 ~ +0.10（N=16 明显更好）
- **NER:** 基本持平（N=8 已饱和）

### 结论
- **voting_confidence** 是最强信号（NER/RE 均排第一）
- 所有结构化 consistency 信号优于 logprob baseline
- RE 任务从增大 N 中获益更多，NER 更早饱和
- Verdict = MARGINAL（RE ρ_sj=0.333 < 0.40 阈值，但 voting_confidence 已达 0.448）

---
