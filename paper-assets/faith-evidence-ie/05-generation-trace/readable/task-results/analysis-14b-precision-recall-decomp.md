# analysis 14b precision recall decomp

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b_precision_recall_decomp_20260525T010222_result.json`
- **Structured JSON:** [`1bdc0a5e801a6057b3a7.json`](../../sessions/1b/1bdc0a5e801a6057b3a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EDCR bins 全显示 1.0 是脚本 bug —— 只有 TP 预测才有匹配的 gold evidence 来计算 EDCR，所以那个分层实际上只包含 TP。evidence count 分层的 precision 分析是有效的。

完整结果如下：

## 14B RSFT s42 — Test-Set P/R Decomposition

**Overall**: P=0.4951, R=0.3188, F1=0.3878 (TP=5562, Pred=11235, Gold=17448)

### Top-5 高 F1 关系 (gold≥10)
| Relation | P | R | F1 | TP | Gold |
|---|---|---|---|---|---|
| date of birth | 0.553 | **0.920** | 0.690 | 184 | 200 |
| original network | **0.909** | 0.556 | 0.690 | 20 | 36 |
| director | **0.884** | 0.528 | 0.661 | 38 | 72 |
| date of death | 0.533 | **0.853** | 0.656 | 145 | 170 |
| performer | 0.745 | 0.580 | 0.652 | 164 | 283 |

### 最保守 (P >> R)
| Relation | P | R | Gap | Gold |
|---|---|---|---|---|
| notable work | 0.750 | 0.050 | **+0.700** | 598 |
| spouse | 0.889 | 0.300 | +0.589 | 80 |
| P131 (admin entity) | 0.748 | 0.164 | +0.585 | **4048** |
| composer | 0.824 | 0.246 | +0.578 | 57 |

### 最激进 (R >> P)
| Relation | P | R | Gap | Gold |
|---|---|---|---|---|
| date of birth | 0.553 | 0.920 | **-0.367** | 200 |
| date of death | 0.533 | 0.853 | -0.320 | 170 |
| place of death | 0.376 | 0.683 | -0.307 | 60 |
| member of sports team | 0.469 | 0.762 | -0.293 | 80 |
| inception | 0.292 | 0.572 | -0.280 | 180 |

### Cross-Sentence vs Within-Sentence
| Category | TP | Gold | Recall |
|---|---|---|---|
| Cross-sentence (evi≥2) | 1427 | 3848 | **0.371** |
| Within-sentence (evi=1) | 1812 | 3699 | **0.490** |
| No evidence annotation | 2323 | 9901 | 0.235 |

跨句 recall 比句内低 12pp（0.371 vs 0.490）。

### Precision by Evidence Count
| Predicted evi sents | Correct | Total | Precision |
|---|---|---|---|
| 1 sent | 2774 | 4669 | **0.594** |
| 2 sents | 2389 | 5316 | **0.449** |
| 3 sents | 263 | 896 | **0.294** |
| 4+ sents | 81 | 228 | 0.355 |

证据句越多，precision 越低。单句证据预测 P=0.594 是 3 句证据的 2 倍。

### 关键问题
1. **P131 (located in admin entity)** 是最大瓶颈：gold=4048 但 recall=0.164，贡献了大量漏检（3385 FN）
2. **notable work (P800)**: gold=598, recall=0.050，几乎没检出
3. **4 个关系 zero-recall** (gold≥10): territory claimed by, position held, influenced by, replaces
4. **0 个幻觉关系**：所有预测的关系类型都存在于 gold 中
5. **Macro-avg**: P=0.419, R=0.294, F1=0.318（比 micro 低因为长尾关系表现差）

---
