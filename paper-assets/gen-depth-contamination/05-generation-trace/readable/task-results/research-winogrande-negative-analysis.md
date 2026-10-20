# research winogrande negative analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_winogrande_negative_analysis_20260521T035728_result.json`
- **Structured JSON:** [`373097029037bd8ef33e.json`](../../sessions/37/373097029037bd8ef33e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：-0.79pp 是 noise，不是 systematic pattern。**

关键证据：

| 检验 | 结果 |
|---|---|
| Paired t-test | t=−2.63, df=2, **p=0.12**（不显著） |
| Gap vs eval stderr | 0.79pp < 1.35pp（不到一个标准误） |
| 逐 seed 稳定性 | 幅度变化 4× (0.31pp ~ 1.34pp) |
| 相对 base model | 所有策略 WinoGrande ±0.5pp 以内，fine-tuning 本身对这个 benchmark 几乎无影响 |
| 跨 benchmark | binary 在 GSM8K (+1.90pp)、TruthfulQA (+1.52pp) 上有一致优势，排除系统性退化 |

报告已保存至 `artifacts/exp_expanded_downstream_eval/report/winogrande_negative_analysis.md`。论文中如实报告即可，不需要为一个不显著的结果构造解释机制。

---
