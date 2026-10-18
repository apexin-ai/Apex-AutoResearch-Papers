# data figure1 candidates

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_figure1_candidates_20260521T221715_result.json`
- **Structured JSON:** [`c9c56fc77c1765cd3227.json`](../../sessions/c9/c9c56fc77c1765cd3227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。保存到 `artifacts/figure1_candidates.json`，关键发现：

**3 个候选的 original_formality 全部是 formal**（原文 formal → counterfactual 是 casual rewrite），且 gpt4o 和 llama70b/qwen32b 使用了不同的 counterfactual 文本（两轮独立 rewrite），已全部保留。

| ID | Likert | Pairwise formal wins | 亮点 |
|---|---|---|---|
| **mvp_0024** | 全部 tie (9/9, 8/8, 7/7) | 3/3 judges, consistent | 最干净的 example：Likert 完全平局却一致 pairwise 选 formal |
| **mvp_0048** | GPT-4o: casual 8 > formal 5 | 3/3 judges, consistent | GPT-4o Likert-pairwise 矛盾最突出：给 casual 更高分却选 formal |
| **mvp_0096** | 全部 tie (5/5, 6/6, 6/6) | 2/3 (GPT-4o inconsistent) | NLI 最高 (0.998)，但 GPT-4o 有 position bias |

---
