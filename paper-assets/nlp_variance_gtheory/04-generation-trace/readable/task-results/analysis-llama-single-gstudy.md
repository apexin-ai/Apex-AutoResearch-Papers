# analysis llama single gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_single_gstudy_20260521T034025_result.json`
- **Structured JSON:** [`59d65e77094014b784e1.json`](../../sessions/59/59d65e77094014b784e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已获得。

---

**Llama single-model G-study (239,200 records, 1196 conditions × 200 items):**

### binary_correct:
| Component | % |
|---|---|
| item_id | 61.08% |
| residual | 21.59% |
| seed:item_id | 4.72% |
| prompt_template:item_id | 4.58% |
| precision:item_id | 4.16% |
| temperature:item_id | 1.83% |
| precision | 1.19% |

**G coefficient: 0.6108** (MVP: 0.357)

### text_exact_match:
| Component | % |
|---|---|
| temperature | 79.72% |
| residual | 8.85% |
| precision:temperature | 4.15% |
| precision | 2.81% |
| temperature:item_id | 0.85% |
| item_id | 0.66% |

**G coefficient: 0.0066** (MVP: 0.975)

### D-study (binary_correct):
| n_items | G |
|---|---|
| 25 | 0.164 |
| 50 | 0.282 |
| 100 | 0.440 |
| 200 | 0.611 |
| 300 | 0.702 |
| 500 | 0.797 |

G>0.8 需要 ~510 items。

### vs MVP 对比:

**binary_correct — 稳定，方向一致，数值提升：**
- item_id 从 58.4% → 61.1%（略升，4x items 采样更完整）
- G 从 0.357 → 0.611（大幅提升，符合预期——200 items 比 50 items 降低了相对误差）
- residual 从 17.6% → 21.6%（略升，更多 items 暴露了更多高阶交互未建模的变异）
- 新发现的关键交互：seed:item_id=4.7%, prompt_template:item_id=4.6%, precision:item_id=4.2% — 这些 facet×item 交互在 50 items 时信号不足，200 items 后清晰浮现

**text_exact_match — 结构剧变：**
- MVP 的 G=0.975 降至 0.0066，因为 text_exact_match 在 200 items 下几乎完全被 temperature 主效应 (79.7%) 主导
- item_id 仅占 0.66%，说明 text 层面的变异主要来自 temperature 的全局效应（高 temp → 文本不稳定），跨 item 无差异化

---
