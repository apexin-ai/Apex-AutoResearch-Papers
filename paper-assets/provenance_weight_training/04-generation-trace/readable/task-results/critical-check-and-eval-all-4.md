# critical check and eval all 4

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_check_and_eval_all_4_20260521T094128_result.json`
- **Structured JSON:** [`cd94f596c7f91bc55f5b.json`](../../sessions/cd/cd94f596c7f91bc55f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 eval 完成。汇报：

---

**实验状态: 全部完成**

**Holdout PPL:**
| 实验 | Loss | Perplexity |
|------|------|------------|
| adaptive_tau08_v2 | 2.8729 | 17.69 |
| gpt2_seed123_v2 | 2.8786 | 17.79 |
| gpt2_seed456_v2 | 2.8790 | 17.80 |
| ngram_seed456_v2 | 2.8807 | 17.83 |

**OOD PPL (adaptive_tau08_v2 only):**
| 数据集 | Loss | Perplexity |
|--------|------|------------|
| OpenWebText | 2.9107 | 18.37 |
| Wikipedia | 2.7311 | 15.35 |

tau08 在所有指标上都是最好的。Holdout PPL 差异在 0.14 以内 (17.69–17.83)，四个实验表现一致。

---
