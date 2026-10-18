# analysis fewrel 80rel error taxonomy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewrel_80rel_error_taxonomy_20260515T150702_result.json`
- **Structured JSON:** [`be7ffda494785ace7df3.json`](../../sessions/be/be7ffda494785ace7df3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰。

## FewRel 80-rel Error Taxonomy

| Bin | BCS_mean | Batches | Samples | Correct% | WrongType% | IntraSub% | Missed% |
|-----|----------|---------|---------|----------|------------|-----------|---------|
| zero | 0.0000 | 80 | 960 | 85.73% | 0.00% | 0.00% | 14.27% |
| low | 0.5652 | 6 | 528 | 85.42% | 4.17% | 4.17% | 10.42% |
| medium | 0.7293 | 37 | 5568 | 75.70% | 13.00% | 13.00% | 11.30% |
| high | 0.8602 | 19 | 5952 | 66.67% | 20.28% | 20.28% | 13.05% |
| very_high | 0.9706 | 12 | 7968 | 52.03% | 32.25% | 32.25% | 15.71% |

## Spearman Correlations (n=154 batches)

| Metric | ρ | p |
|--------|------|------|
| **IntraSub rate vs BCS** | **0.9539** | <1e-6 |
| WrongType rate vs BCS | 0.9539 | <1e-6 |
| Accuracy vs BCS | -0.5821 | <1e-6 |

## Cross-task 对比 (NER exp-007 vs FewRel RE)

| | NER (Few-NERD) | RE (FewRel 80-rel) |
|---|---|---|
| IntraSub vs BCS ρ | **1.0** | **0.9539** |
| 机制一致性 | IntraSub 随 BCS 单调增 | IntraSub 随 BCS 单调增 |

关键发现：

1. **IntraSub = WrongType**：在每个 bin 中 intra_sub_rate == wrong_type_rate，说明 RE 任务中 **100% 的类型混淆都是 batch 内混淆**（模型不会预测 schema 之外的 relation），这与 NER 结论一致。
2. **Missed rate 相对平坦**（10-16%），BCS 主要驱动类型混淆而非检测失败。
3. **IntraSub 机制从 NER 成功迁移到 RE**：ρ=0.9539 vs NER 的 ρ=1.0，跨任务验证成立。

输出已保存到 `artifacts/fewrel_80rel_error_taxonomy.json`。

---
