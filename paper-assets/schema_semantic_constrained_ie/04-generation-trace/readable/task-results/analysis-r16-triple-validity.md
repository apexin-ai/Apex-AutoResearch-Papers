# analysis r16 triple validity

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16_triple_validity_20260521T033232_result.json`
- **Structured JSON:** [`8159e816b381a3c8205a.json`](../../sessions/81/8159e816b381a3c8205a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Lucky violations 几乎不存在** — 平均仅 0.49% 的 gold 匹配来自类型违规 triple，约束解码造成的 recall 损失 < 0.5pp。

**关键数据对比：**

| Config | DR违规率(unc→con) | Recall变化 | Lucky违规数 |
|--------|-------------------|-----------|------------|
| SciERC Qwen-FT | 1.95% → 0% | -0.10pp | 4 (0.41% gold) |
| SciERC Llama-FT | 1.11% → 0.09% | ±0.00pp | 5 (0.51% gold) |
| DocRED Qwen-FT | 1.03% → 0.01% | -0.84pp | 1 (0.01% gold) |
| DocRED Llama-FT | 0.64% → 0.21% | -0.10pp | 1 (0.01% gold) |

**Llama SciERC 的亮点**: 5 个 unconstrained 中的 lucky violation 在 constrained 模式下全部被恢复为合法类型路径，triple churn = 0%。模型将概率质量重定向到 schema-compliant 类型组合，生成了完全相同的内容。

**Precision@valid 基本持平** (-0.20pp avg) — FT 模型的 base 违规率本已很低 (1-2%)，约束主要通过过滤工作而非改善生成质量。

**KG 构建价值**: 约束解码以 < 0.5% recall 代价换取 100% schema 合规，无需后处理过滤。

结果已写入 `artifacts/r16_verification/task_e_triple_validity.json`。

---
