# analysis test eval 14b rsft s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_14b_rsft_s43_20260523T165514_result.json`
- **Structured JSON:** [`613a024470a5b606c57f.json`](../../sessions/61/613a024470a5b606c57f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**s43 Test Results:**
| | Ign-F1 | Precision | Recall |
|---|---|---|---|
| with-evi | 0.3767 | 0.4252 | 0.3382 |
| no-evi | 0.3775 | 0.4138 | 0.3470 |
| **Evidence tax** | **+0.08pp** | | |

**14B 2-Seed Reproducibility:**
- with-evi: 0.3808 ± 0.0058 (s42=0.3849, s43=0.3767)
- no-evi: 0.3851 ± 0.0107 (s42=0.3926, s43=0.3775)
- evidence tax: **+0.42 ± 0.49pp** (n=2)，置信区间跨零，方向不确定

**Full-Scale Evidence Tax:**
| Scale | Tax (pp) | Direction |
|---|---|---|
| 4B | +1.65±0.29 | positive (evidence hurts) |
| 8B | -0.91±0.74 | negative (evidence helps) |
| **14B** | **+0.42±0.49** | **ambiguous** |
| LLaMA-8B | -1.46±0.40 | negative (evidence helps) |

s43 整体 ign_f1 低于 s42（with-evi 低 0.82pp，no-evi 低 1.51pp），seed 方差偏大。CodaLab 提交文件已生成。

---
