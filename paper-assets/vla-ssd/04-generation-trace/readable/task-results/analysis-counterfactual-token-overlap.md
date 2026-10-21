# analysis counterfactual token overlap

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_counterfactual_token_overlap_20260519T011529_result.json`
- **Structured JSON:** [`40b96ae9a3615d115b9c.json`](../../sessions/40/40b96ae9a3615d115b9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

## Token Overlap 分析结果

| Perturbation | Jaccard | Token Novelty (1-J) | Cohen's d |
|---|---|---|---|
| empty | 0.000 | 1.000 | 0.968 |
| wrong | 0.174 | 0.827 | 0.844 |
| paraphrased | 0.533 | 0.467 | 0.697 |
| shuffled | 1.000 | 0.000 | 0.625 |

**Spearman r = 1.0** (perfect rank-order match), **Pearson r = 0.957**

**结论：审稿人的质疑成立。** Token novelty 完美预测了 Cohen's d 的排序。paraphrased (d=0.697) > shuffled (d=0.625) 是因为 paraphrased 引入了约 47% 的新 token（替换了 "middle"→"center", "of"→"on", 新增 "pull" 等），而 shuffled 保留了 100% 的原始 token（Jaccard=1.0）。

两层机制：
1. **Token identity change**：新 token 越多，action shift 越大（解释 paraphrased > shuffled）
2. **Word order sensitivity**：即使 token 完全相同（shuffled），打乱顺序仍产生 d=0.625 的 action shift

结果 JSON 写入 `/root/autodl-tmp/vla-ssd/results/counterfactual_token_overlap.json`，registry 已更新为 DONE/success。

---
