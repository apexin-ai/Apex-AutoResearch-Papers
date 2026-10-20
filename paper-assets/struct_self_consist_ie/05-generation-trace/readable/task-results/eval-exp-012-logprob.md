# eval exp 012 logprob

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp_012_logprob_20260514T105409_result.json`
- **Structured JSON:** [`b4e658b1a308969114d0.json`](../../sessions/b4/b4e658b1a308969114d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-012 完成。结果汇总：

## exp-012 Logprob Baseline 对比结果

### NER (Full Set, n=529)
| Signal | ρ_spearman | p-value | τ_kendall | AUROC |
|---|---|---|---|---|
| **soft_jaccard** | **+0.3565** | 2.66e-17 | **+0.2658** | **0.6892** |
| fleiss_kappa | +0.2651 | 5.86e-10 | +0.2027 | 0.6292 |
| mean_logprob | +0.1396 | 1.29e-03 | +0.1006 | 0.5907 |
| greedy_logprob | +0.1615 | 1.92e-04 | +0.1184 | 0.5941 |

**NER → SJ 碾压 logprob (ρ delta = +0.217)**

### RE (Full Set, n=397)
| Signal | ρ_spearman | p-value | τ_kendall | AUROC |
|---|---|---|---|---|
| soft_jaccard | +0.2112 | 2.21e-05 | +0.1619 | 0.5916 |
| **fleiss_kappa** | **+0.2528** | 3.32e-07 | **+0.1967** | **0.6262** |
| mean_logprob | +0.2467 | 6.47e-07 | +0.1808 | 0.6186 |
| greedy_logprob | +0.2307 | 3.40e-06 | +0.1696 | 0.6131 |

### RE (Conditional Set, n=296, 过滤101个全零实例)
| Signal | ρ_spearman | τ_kendall | AUROC |
|---|---|---|---|
| **soft_jaccard** | **+0.3683** | **+0.2699** | **0.6839** |
| fleiss_kappa | +0.3168 | +0.2398 | 0.6469 |
| mean_logprob | +0.1457 | +0.1039 | 0.5487 |
| greedy_logprob | +0.1566 | +0.1119 | 0.5499 |

**RE Conditional → SJ 碾压 logprob (ρ delta = +0.223)**

### 结论

- **NER**: SJ 在所有指标上大幅领先 logprob — 强贡献成立
- **RE Full Set**: logprob 略优于 SJ（ρ 0.247 vs 0.211, delta=0.036），但 FK 以 0.253 胜出，且 AUROC FK 也最高（0.626）
- **RE Conditional Set**（排除模型完全无法处理的实例后）: SJ 反超 logprob 两倍以上（0.368 vs 0.146）

RE full set 中 logprob 的微弱优势来自 101 个全零实例（模型完全不会抽关系的 instance）——logprob 能区分"模型完全困惑"的情况，但对于模型有能力处理的实例，结构一致性信号远优于 logprob。

**Paper direction: SJ 作为 confidence signal 的独特价值成立。** Logprob 不是竞争对手，而是互补信号——尤其在 RE 上可以考虑 ensemble（SJ + logprob）作为后续工作。

---
