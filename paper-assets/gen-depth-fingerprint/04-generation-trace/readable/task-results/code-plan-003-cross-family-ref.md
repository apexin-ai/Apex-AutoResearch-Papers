# code plan 003 cross family ref

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-003-cross-family-ref_20260515T000733_result.json`
- **Structured JSON:** [`a898c242f318c18a3eae.json`](../../sessions/a8/a898c242f318c18a3eae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan-003 全部完成，已补注册实验和产出物。

**总结：**

| 项目 | 状态 |
|------|------|
| `extract_features_crossref.py` | 已存在，支持 `--reference-model` / `--device` 参数 |
| `features_ref_olmo.csv` (OLMo-2-1B ref) | 23032 行，5 生成器 |
| `features_ref_qwen.csv` (Qwen3-0.6B ref) | 23032 行，5 生成器 |
| `cross_ref_analysis.py` + `cross_ref_results.json` | 完整分析（Spearman ρ + entropy drift + LOGO 3-class） |
| 实验注册 | `plan-003-olmo2ref` / `plan-003-qwen06bref` → DONE/success |

**核心发现：** entropy_mean drift 在 3 个参考模型（Pythia-410M / OLMo-2-1B / Qwen3-0.6B）下均为负漂移，所有 5 个生成器方向一致。LOGO macro-F1 ≈ 0.82。假设成立——dual dynamics 是生成链内在属性，非参考模型 artifact。

---
