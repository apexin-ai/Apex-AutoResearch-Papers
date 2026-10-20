# analysis entity order fair comparison

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entity-order-fair-comparison_20260522T181050_result.json`
- **Structured JSON:** [`058042ba223ace22d811.json`](../../sessions/05/058042ba223ace22d811.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果比预期更强：

**Entity ordering 不仅没有显著影响，而且对输出完全零影响。** 551 个样本的 raw_output 和 parsed_output 在 original 和 shuffled 之间逐字节一致。之前的 -3.38pp R-F1 差异 100% 来自 checker 版本不一致（旧版给 original 算出 47.15，新版给 shuffled 算出 43.77）。

这意味着 shuffling `ontology_constraints.json` 中的 entity/relation type 顺序根本没有改变 constrained decoding 的 token 生成——grammar 在每个类型位置接受的 token 集合与 schema 中的枚举顺序无关，greedy 解码在相同 prompt 下产生完全确定性的输出。

Conclusion 已从 `negative` 改为 `success`（order-invariant confirmed），R19-W3 reviewer concern 可安全回应。

---
