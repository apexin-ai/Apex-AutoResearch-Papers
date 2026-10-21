# analysis exp 016 signal ensemble

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_016_signal_ensemble_20260514T120704_result.json`
- **Structured JSON:** [`793763b17cfc8593ec6b.json`](../../sessions/79/793763b17cfc8593ec6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-016 完成。核心结果：

## Part 1: 信号相关性
- SJ vs logprob 相关性中等（NER Pearson=0.57, RE=0.42），**有互补空间**
- SJ vs exact_match 高度相关（NER 0.79, RE 0.86），冗余较大
- logprob vs voting_confidence 低相关（NER 0.16, RE 0.48），互补性最强

## Part 2: 线性组合
- **NER**: SJ+voting_conf 最佳（α=0.3, ρ=0.489），优于两个单信号（SJ 0.357, VC 0.430）
- **RE**: voting_conf+logprob 最佳（α=0.6, ρ=0.429），略优于单 VC（0.427）
- SJ+logprob 在 RE 也有增益（ρ=0.287 vs SJ 0.211, logprob 0.247）

## Part 3: Logistic Ensemble
| | Ensemble | Best Single | Δ |
|---|---|---|---|
| NER AUROC | **0.735** | 0.700 (VC) | +0.035 |
| RE AUROC | **0.719** | 0.721 (VC) | -0.002 |

- 系数最大：voting_confidence（NER 0.86, RE 1.03），其次 exact_match（NER 0.65）
- fleiss_kappa 系数为负（被其他信号包含的冗余信息）

## Part 4: Best-of-N Selection F1
| Method | NER | RE |
|---|---|---|
| greedy | 0.609 | 0.374 |
| random | 0.580 | 0.338 |
| SJ-best | 0.604 | 0.368 |
| voting-conf-best | 0.596 | 0.338 |
| **logprob-best** | **0.609** | **0.397** |
| ensemble-best | 0.604 | 0.367 |
| oracle | 0.769 | 0.561 |

RE 中 logprob-best（0.397）是唯一超过 greedy 的方法。Oracle gap 依然很大（NER +0.16, RE +0.19），暗示当前信号远未充分利用采样多样性。

---
