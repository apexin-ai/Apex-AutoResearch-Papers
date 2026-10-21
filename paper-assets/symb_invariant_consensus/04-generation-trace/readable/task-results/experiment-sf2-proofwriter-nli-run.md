# experiment sf2 proofwriter nli run

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_sf2-proofwriter-nli-run_20260520T135632_result.json`
- **Structured JSON:** [`33888b66ed441f8b3c4d.json`](../../sessions/33/33888b66ed441f8b3c4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

---

## SF-2 DeBERTa NLI on ProofWriter-D5 (600Q) — 完整结果

### DeBERTa Standalone (NLI-only)
- **Accuracy: 55.00%** (330/600)
- Inference time: 597.3s

### Baselines
| Method | Accuracy |
|--------|----------|
| SC (Mistral-7B) | 39.33% (236/600) |
| SICA | 36.50% (219/600) |

### NLI Per-Label Accuracy
| Label | N | Correct | Accuracy | Precision | Recall | F1 |
|-------|---|---------|----------|-----------|--------|-----|
| True | 200 | 128 | 64.0% | 0.696 | 0.640 | 0.667 |
| False | 200 | 195 | **97.5%** | 0.479 | 0.975 | 0.643 |
| Unknown | 200 | 7 | **3.5%** | 0.778 | 0.035 | 0.067 |

DeBERTa 预测分布严重偏向 False（407/600），几乎不预测 Unknown（仅 9/600）。

### Complementarity (NLI vs SC)
| | Count |
|--|-------|
| NLI correct & SC wrong | **274** |
| SC correct & NLI wrong | 180 |
| Both correct | 56 |
| Both wrong | 90 |

### Combo (DeBERTa + SC votes) vs SC Baseline
| Weight | Accuracy | Δ vs SC | McNemar b | McNemar c | p-value | Sig |
|--------|----------|---------|-----------|-----------|---------|-----|
| w=1 | 40.17% | +0.83pp | 4 | 9 | 0.2668 | |
| w=3 | 42.83% | +3.50pp | 22 | 43 | 0.0125 | * |
| w=5 | 50.00% | **+10.67pp** | 35 | 99 | <0.0001 | *** |

### Combo vs SICA Baseline
| Weight | Accuracy | Δ vs SICA | McNemar p |
|--------|----------|-----------|-----------|
| w=1 | 40.17% | +3.67pp | 0.0021 ** |
| w=3 | 42.83% | +6.33pp | 0.000051 *** |

### DeBERTa vs SICA Agreement
- Agreement: 8.7% (52/600) — 当两者一致时 accuracy 80.8%
- Disagree: DeBERTa correct=288, SICA correct=177

---

**关键发现**: DeBERTa NLI 单独 (55%) 大幅超过 SC baseline (39.3%)。Combo w=5 显著提升 +10.67pp（p<0.0001）。互补性强：NLI 独对 274 例 vs SC 独对 180 例。但 DeBERTa 对 Unknown 类别几乎完全失效（3.5%），False 预测偏重。

---
