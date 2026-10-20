# analysis prepare violation analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prepare_violation_analysis_20260513T200611_result.json`
- **Structured JSON:** [`704cfbd6e2323feaa69d.json`](../../sessions/70/704cfbd6e2323feaa69d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本通过 dry-run 验证。结果总结：

---

## Part 1: 实验进度

| 实验 | 已处理 | 状态 | GPU 占用 |
|------|--------|------|----------|
| SciERC schema-informed | 551/551 | **完成** | cuda:0 空闲 |
| DocRED minimal | 457/998 | 运行中 (~40min 剩余) | cuda:1: 83%, 18.5GB |

## Part 2: SciERC 对比结果 (minimal vs schema_informed)

**核心指标 — Domain/Range violation rate 下降 62.4%：15.37% → 5.78%**

| 指标 | minimal | schema_informed | 变化 |
|------|---------|-----------------|------|
| D/R violation rate | 15.37% | 5.78% | **-62.4%** |
| Relation vocab violation | 1.39% | 0.30% | -78.4% |
| Entity type violation | 0.40% | 0.00% | -100% |
| Total violation rate | 7.17% | 2.53% | -64.7% |

Per-relation 改进最大：Feature-of (-22.3pp), Part-of (-22.5pp), Compare (-14.8pp)。唯一退步的是 Evaluate-for (+5.8pp)。

McNemar 检验四类 violation 全部统计显著 (p<0.01)。

## 产出

1. `compare_prompts.py` 已部署到服务器，支持 SciERC/DocRED 两个数据集，包含聚合对比和 McNemar 检验
2. `outputs/violation_report_schema.json` — schema_informed violation report
3. `outputs/comparison_minimal_vs_schema_informed.json` — 完整对比 JSON

---
