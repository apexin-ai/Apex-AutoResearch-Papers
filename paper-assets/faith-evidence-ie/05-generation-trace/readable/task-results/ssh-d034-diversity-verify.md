# ssh d034 diversity verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d034-diversity-verify_20260515T011932_result.json`
- **Structured JSON:** [`c7b89775321248489fd9.json`](../../sessions/c7/c7b89775321248489fd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。**diversity 非常高，mean=7.11/8，与监控报告的 0.9/8 完全矛盾。**

```
== D034 Diversity 独立验证 ==
分析文档数: 200 (共 200)
每文档候选数: min=8, max=8, mode=8

Triple-set Diversity:
- mean unique sets: 7.11 / 8
- median: 8.0
- min: 1, max: 8
- 分布: [1/8: 4 docs, 2/8: 2 docs, 3/8: 4 docs, 4/8: 6 docs, 5/8: 9 docs, 6/8: 15 docs, 7/8: 37 docs, 8/8: 123 docs]

Evidence Diversity:
- mean unique sets: 5.43 / 8
- median: 6.0
- min: 1, max: 8
- 分布: [1/8: 5 docs, 2/8: 14 docs, 3/8: 23 docs, 4/8: 30 docs, 5/8: 25 docs, 6/8: 21 docs, 7/8: 43 docs, 8/8: 39 docs]

Format Parse Rate:
- 成功解析 triple 的候选比例: 90.2%

结论: diversity 合格 (mean=7.11 >= 3/8)
```

**结论**：实际 diversity 水平很高（7.11/8），与 diversity_probe 早期观察（7/8）一致。监控报告的 mean_diversity=0.9/8 是 **监控计算 bug**，不是生成质量问题。61.5% 的文档达到了 8/8 完全不同，只有 3% 的文档 diversity ≤ 2/8。

Evidence diversity 略低（5.43/8），说明模型在 triple 层面有较好多样性，但 evidence 选择更趋于一致——这是合理的，因为正确 evidence 本身选择空间有限。

---
