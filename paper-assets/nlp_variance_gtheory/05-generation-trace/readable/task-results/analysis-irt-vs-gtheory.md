# analysis irt vs gtheory

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt_vs_gtheory_20260521T042145_result.json`
- **Structured JSON:** [`c62e18285381f83fbcce.json`](../../sessions/c6/c62e18285381f83fbcce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/analysis/irt_vs_gtheory.json`。

IRT vs G-theory comparison:

| Method | Min Items | Accounts for |
|---|---|---|
| IRT (random) | 116 | item difficulty only |
| IRT (optimal) | 47 | item difficulty (best items) |
| G-theory (all random) | 510 | item + all facet interactions |
| G-theory (practical) | 414 | item + prompt/seed/ordering |

Ratio: G-theory needs **3.6–4.4×** more items than IRT.

At IRT-recommended 116 items, G-theory G = **0.477**（远低于 0.80 阈值）。

Key insight: IRT 只建模 item difficulty，将 prompt/seed/ordering 视为固定或忽略。G-theory 显式捕获了 IRT 遗漏的 ~37% 方差（prompt×item 4.58%、seed×item 4.73%、ordering×item 0.59%、residual 21.59%），因此需要显著更多 items 才能达到同等可靠性。|IRT difficulty| 与 G-theory item variance 的 Spearman ρ = 0.44，说明两种框架对 item 特征的刻画方向一致但量化差异大。

---
