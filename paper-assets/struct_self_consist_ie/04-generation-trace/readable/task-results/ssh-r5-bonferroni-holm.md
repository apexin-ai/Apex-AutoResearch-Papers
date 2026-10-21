# ssh r5 bonferroni holm

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_r5-bonferroni-holm_20260520T101440_result.json`
- **Structured JSON:** [`8b7b439824b1c28e9450.json`](../../sessions/8b/8b7b439824b1c28e9450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

57 个 entity construction paired bootstrap tests，Holm-Bonferroni 校正后：

**17 → 8 survive (α=0.05)**

### Survived correction (corrected p=0.0057)
| Config | Method | ΔF1 | raw p |
|--------|--------|-----|-------|
| n16_scierc | adaptive_uniform | +4.05pp | 0.0000 |
| n16_fewnerd | uniform_cv | +1.32pp | 0.0000 |
| n16_fewnerd | lp_selection | +1.88pp | 0.0000 |
| n16_fewnerd | lp_weighted_cv | +1.42pp | 0.0000 |
| n16_fewnerd | adaptive_uniform | +5.55pp | 0.0000 |
| n8_fewnerd | lp_selection | +1.36pp | 0.0000 |
| n8_fewnerd | lp_weighted_confirm | +0.88pp | 0.0000 |
| n8_fewnerd | lp_weighted_cv | +0.88pp | 0.0000 |

### Lost significance (9 tests)
- **n16_conll adaptive_uniform** (raw p=0.0012 → corr p=0.0588) — borderline miss
- **n16_scierc uniform_cv / lp_weighted_cv** (raw p≈0.018 → corr p=0.79)
- **n8_scierc** 的 confirm/cv 构造方法
- **n16_scierc RE uniform_cv** (raw p=0.049 → corr p=1.0)

### 主线 claim 评估
- **FewNERD 上的构造方法优势** — 全部 survive，主线 claim 最稳固
- **SciERC adaptive_uniform** — survive
- **CoNLL adaptive_uniform** — borderline miss (corr p=0.0588)，需谨慎表述
- **SciERC 上的 cv/lp_weighted_cv 构造** — 不 survive，论文中应弱化或标注为 exploratory
- **RE 构造** — 没有任何 test survive

---
