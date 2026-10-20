# analysis code wiki bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_code_wiki_bootstrap_ci_20260524T095055_result.json`
- **Structured JSON:** [`079b116f6db66624b0d2.json`](../../sessions/07/079b116f6db66624b0d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 20 pairs complete. JSON artifact saved locally. Here's the full summary:

## Bootstrap CI + Permutation Test Results (10K resamples, Bonferroni-corrected)

### Mistral-7B Code — K\*=2
| Pair | AUC | 95% CI | Bonf CI (α=0.01) | bonf_p | >θ |
|------|-----|--------|-------------------|--------|----|
| 0v1 | 0.9189 | [0.9142, 0.9237] | [0.9127, 0.9251] | 0.0005 | YES |
| **1v2** | **0.6150** | **[0.6054, 0.6250]** | **[0.6024, 0.6281]** | **0.0005** | **YES** |
| 2v3 | 0.5292 | [0.5191, 0.5393] | [0.5155, 0.5426] | 0.0005 | NO |
| 3v4 | 0.5286 | [0.5183, 0.5387] | [0.5152, 0.5418] | 0.0005 | NO |
| 4v5 | 0.5099 | [0.4994, 0.5207] | [0.4961, 0.5235] | 0.1870 | NO |

### Qwen-7B Code — K\*=2
| Pair | AUC | 95% CI | Bonf CI (α=0.01) | bonf_p | >θ |
|------|-----|--------|-------------------|--------|----|
| 0v1 | 0.9050 | [0.9000, 0.9102] | [0.8985, 0.9118] | 0.0005 | YES |
| 1v2 | 0.7273 | [0.7184, 0.7362] | [0.7153, 0.7389] | 0.0005 | YES |
| 2v3 | 0.5367 | [0.5267, 0.5464] | [0.5237, 0.5496] | 0.0005 | NO |
| 3v4 | 0.5088 | [0.4984, 0.5190] | [0.4950, 0.5223] | 0.2950 | NO |
| 4v5 | 0.5137 | [0.5034, 0.5240] | [0.5002, 0.5274] | 0.0415 | NO |

### Mistral-7B Wiki — K\*=1
| Pair | AUC | 95% CI | Bonf CI (α=0.01) | bonf_p | >θ |
|------|-----|--------|-------------------|--------|----|
| 0v1 | 0.9614 | [0.9581, 0.9644] | [0.9571, 0.9654] | 0.0005 | YES |
| 1v2 | 0.5576 | [0.5470, 0.5681] | [0.5434, 0.5716] | 0.0005 | NO |
| 2v3 | 0.5193 | [0.5083, 0.5301] | [0.5046, 0.5337] | 0.0020 | NO |
| 3v4 | 0.5172 | [0.5062, 0.5280] | [0.5029, 0.5317] | 0.0100 | NO |
| 4v5 | 0.5011 | [0.4903, 0.5120] | [0.4866, 0.5155] | 1.0000 | NO |

### LLaMA-8B Wiki — K\*=1
| Pair | AUC | 95% CI | Bonf CI (α=0.01) | bonf_p | >θ |
|------|-----|--------|-------------------|--------|----|
| 0v1 | 0.9321 | [0.9273, 0.9366] | [0.9260, 0.9380] | 0.0005 | YES |
| 1v2 | 0.5919 | [0.5822, 0.6019] | [0.5788, 0.6049] | 0.0005 | NO |
| 2v3 | 0.5379 | [0.5275, 0.5484] | [0.5240, 0.5514] | 0.0005 | NO |
| 3v4 | 0.5105 | [0.4999, 0.5213] | [0.4962, 0.5244] | 0.2310 | NO |
| 4v5 | 0.5051 | [0.4944, 0.5161] | [0.4908, 0.5193] | 1.0000 | NO |

---

### 关键判定

**Mistral-7B Code 1v2 — Bonferroni CI 下界 0.6024 > θ=0.60。** 即使经过最严格的多重比较校正，CI 仍不跨越阈值，K\*=2 成立。这是最关键的 borderline case，现在可以确认。

### K\* 汇总

| Config | K\* | 判定依据 |
|--------|-----|---------|
| Mistral-7B Code | 2 | 1v2 Bonf CI [0.6024, 0.6281] 整体在 θ 之上 |
| Qwen-7B Code | 2 | 1v2 AUC=0.7273，远超 θ |
| Mistral-7B Wiki | 1 | 1v2 AUC=0.5576，Bonf CI 上界 0.5716 < θ |
| LLaMA-8B Wiki | 1 | 1v2 AUC=0.5919，Bonf CI 上界 0.6049 跨 θ 但点估计 < θ |

JSON artifact 已保存至 `artifacts/code_wiki_bootstrap_ci.json`（本地+远程）。

---
