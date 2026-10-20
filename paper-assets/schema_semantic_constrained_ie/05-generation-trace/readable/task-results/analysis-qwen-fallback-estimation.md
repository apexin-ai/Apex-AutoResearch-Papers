# analysis qwen fallback estimation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_fallback_estimation_20260514T181647_result.json`
- **Structured JSON:** [`a896759a97d72e92e3ac.json`](../../sessions/a8/a896759a97d72e92e3ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Model | Dataset | Fallback Triples | Total Triples | Rate | Avg/doc | Source |
|-------|---------|-----------------|---------------|------|---------|--------|
| Llama | SciERC | — | — | — | ~10.7 | 日志 (token-level) |
| Llama | DocRED | — | — | — | ~57 | 日志 (token-level) |
| **Qwen** | **SciERC** | **16** | **1,729** | **0.9%** | **0.03** | post-hoc (triple-level) |
| **Qwen** | **DocRED** | **1,770** | **17,341** | **10.2%** | **1.77** | post-hoc (triple-level) |

关键发现：

1. **Qwen DocRED fallback 率 10.2%**（1,770 triples），高频 fallback 关系包括：parent taxon (77.8%)、unemployment rate (83.3%)、territory claimed by (45%)、product or material produced (30.8%)
2. **Qwen SciERC 几乎无 fallback**（仅 16 triples, 0.9%），集中在 Evaluate-for 和 Feature-of
3. **DocRED vs SciERC 差异与 Llama 一致**：DocRED 的 96 种关系类型 + 6 种实体类型组合空间更大，更容易触发 fallback

注意单位差异：Llama 日志是 **token-level** fallback 事件计数（每次 semantic∩grammar=∅ 都记一次），Qwen post-hoc 是 **triple-level** DR violation 计数（fallback 下界）。两者不能直接数值对比，但趋势方向一致（DocRED >> SciERC）。

脚本和结果已保存在服务器 `/root/schema_semantic_constrained_ie/outputs/fallback_estimation_results.json`。

---
