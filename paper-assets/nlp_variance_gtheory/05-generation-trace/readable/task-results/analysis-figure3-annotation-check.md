# analysis figure3 annotation check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_figure3_annotation_check_20260522T114144_result.json`
- **Structured JSON:** [`6782feeb92d15dcf9d52.json`](../../sessions/67/6782feeb92d15dcf9d52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据读取完毕。以下是逐项核查结果。

---

## 1. Figure 3 标注核查

Figure 3 caption（`docs/paper/experiments.tex:121`）：

| 标注内容 | 数据源 (intermediate_dstudy_table.json) | 结论 |
|---|---|---|
| "10.0× fewer items" | 552 / 55 = 10.04× | **正确** |
| "G ≥ 0.80 at 55 items" | Full multi-facet `n_for_g80` = 55 | **正确** |
| "552 items" (single-condition) | Single-condition `n_for_g80` = 552 | **正确** |
| "Shaded band: 95% bootstrap CIs" | 描述性标注 | **正确** |

Table 4（`experiments.tex:98-108`）中的数值也与 JSON 完全一致：Multi-facet G200=.936（JSON: 0.936121），Single-cond G200=.592（JSON: 0.591748）。

**Figure 3 标注全部正确，无需修改。**

---

## 2. "nearly double" 核查

出现在三处：
- `abstract.tex:1` — "free-form benchmarks showing nearly double the efficiency gain"
- `introduction.tex:12` — "~21× versus ~12× for MC, indicating ... nearly double the reliability penalty"
- `conclusion.tex:4` — "nearly double the gain (~21× vs. ~12× for MC)"

数据核实（`dstudy_bootstrap_ci.json`）：
- MC mean ratio: **12.0×** [11.6, 12.5]
- FF mean ratio: **21.5×** [20.4, 22.8]
- FF / MC = 21.5 / 12.0 = **1.79×**

"~21×" 和 "~12×" 的约数与数据一致。但 "nearly double" 对应的实际倍数是 1.79×，CI 范围约 [1.63×, 1.97×]。**点估计 1.79× 偏离 2× 约 10%**，CI 下界 1.63× 距 "double" 更远。

**判定：偏高但可辩护。** 如果审稿人严格，可能被质疑。两种处理方案：

- **保留**：改为 "roughly 1.8× the efficiency gain" 或 "approaching double"
- **微调（推荐）**：将 "nearly double" 改为更精确的表述如 "approximately 1.8 times"，同时保留 "~21× vs. ~12×" 的具体数字

---

## 3. 额外发现：3×3 设计数值错误

`experiments.tex:116`:
> "3 prompts × 3 seeds ($G_{200} = 0.766$, $n_{G \geq 0.80} \approx 140$)"

数据核实：

| 设计 | JSON 中的 G200 | JSON 中的 n(G≥0.80) |
|---|---|---|
| 2 prompts × 2 seeds ("Easy upgrade") | **0.766** | 245 |
| 3 prompts × 3 seeds ("Moderate") | **0.818** | 178 |

**G200=0.766 来自 2×2 设计，被错误地标注为 3×3。n≈140 也与两个设计都不匹配。**

正确表述应该是以下之一：
- "**3 prompts × 3 seeds** ($G_{200} = 0.818$, $n_{G \geq 0.80} = 178$)" — 如果想保留 3×3 设计
- "**2 prompts × 2 seeds** ($G_{200} = 0.766$, $n_{G \geq 0.80} = 245$)" — 如果想保留 G200 数值

注意：该句声称这是 "cheapest design exceeding $G = 0.80$"。2×2 的 G200=0.766 未达 0.80，而 3×3 的 G200=0.818 超过 0.80，所以描述匹配 3×3，应修正数值为 **G200=0.818, n=178**。

---

## 总结

| 项目 | 状态 | 需修改？ |
|---|---|---|
| Figure 3 caption 数值 | 全部正确 | 否 |
| Table 4 数值 | 全部正确 | 否 |
| "~21× vs ~12×" | 与数据一致 | 否 |
| "nearly double" (3处) | 实际 1.79×，偏高 | 建议微调为 "approximately 1.8×" |
| 3×3 设计内联数值 (line 116) | **G200 和 n 均错误** | **必须修正** |

---
