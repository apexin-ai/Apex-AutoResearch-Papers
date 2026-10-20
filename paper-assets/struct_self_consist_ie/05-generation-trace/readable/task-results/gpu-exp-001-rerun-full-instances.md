# gpu exp 001 rerun full instances

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_001_rerun_full_instances_20260514T121024_result.json`
- **Structured JSON:** [`ba0a8405ceaca46c3bb6.json`](../../sessions/ba/ba0a8405ceaca46c3bb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## exp_001 全量 551 实例结果

**推理参数**: N=16, T=1.0, seed=42, Qwen3-8B, SciERC 全量 551 句

### NER（n=529 有效）
| Signal | ρ_full | τ_full | AUROC | ρ_cond | τ_cond | AUROC_c |
|---|---|---|---|---|---|---|
| **voting_confidence** | **+0.399** | +0.297 | **0.704** | +0.340 | +0.248 | 0.683 |
| soft_jaccard | +0.398 | +0.294 | 0.697 | +0.349 | +0.253 | 0.677 |
| **exact_match_rate** | +0.339 | +0.247 | 0.677 | **+0.414** | **+0.306** | **0.692** |
| fleiss_kappa | +0.288 | +0.216 | 0.632 | +0.191 | +0.140 | 0.601 |
| logprob | +0.237 | +0.171 | 0.622 | +0.164 | +0.118 | 0.597 |

### RE（n=397 有效）
| Signal | ρ_full | τ_full | AUROC | ρ_cond | τ_cond | AUROC_c |
|---|---|---|---|---|---|---|
| **voting_confidence** | **+0.380** | **+0.289** | **0.699** | +0.350 | +0.255 | 0.693 |
| logprob | +0.293 | +0.214 | 0.655 | +0.025 | +0.017 | 0.562 |
| fleiss_kappa | +0.281 | +0.222 | 0.651 | +0.119 | +0.097 | 0.566 |
| soft_jaccard | +0.277 | +0.210 | 0.637 | +0.318 | +0.232 | 0.675 |
| **exact_match_rate** | +0.148 | +0.115 | 0.556 | **+0.475** | **+0.358** | **0.742** |

### 关键发现
1. **voting_confidence** 在 full 设定下两个子任务都是最佳信号
2. **exact_match_rate** 在 conditional 设定下两个子任务都大幅领先（RE cond ρ=0.475, AUROC=0.742）
3. 所有结构性信号在 conditional 设定下都超越 logprob baseline
4. RE 整体 verdict=FAIL（SJ ρ=0.277 < 0.40 阈值），主要因为 T=1.0 带来更多噪声

### 与 200 实例 (T=0.7) 对比
- NER SJ ρ: 0.398 vs 0.384 (+0.014)，基本稳定
- RE SJ ρ: 0.277 vs 0.333 (-0.057)，T=1.0 下显著退化
- NER greedy F1: 0.659 vs 0.658，几乎一致
- 200 实例 verdict 为 MARGINAL，551 实例为 FAIL

---
