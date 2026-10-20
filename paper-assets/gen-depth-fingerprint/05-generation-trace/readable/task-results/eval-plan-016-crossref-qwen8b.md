# eval plan 016 crossref qwen8b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-016-crossref-qwen8b_20260516T083031_result.json`
- **Structured JSON:** [`3af9576597dd617ba082.json`](../../sessions/3a/3af9576597dd617ba082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

### Table 4: Cross-Ref LOGO macro-F1（6-gen × 3 ref）

| Generator | Pythia-410M | OLMo-2-1B | Qwen3-0.6B |
|-----------|------------|-----------|------------|
| olmo-2-1b | 0.7657 | 0.7775 | 0.7773 |
| pythia-1b | 0.8515 | 0.8432 | 0.8468 |
| pythia-2.8b | 0.8019 | 0.7967 | 0.7997 |
| qwen3-0.6b | 0.8240 | 0.8354 | 0.8446 |
| qwen3-1.7b | 0.8063 | 0.8195 | 0.8556 |
| **qwen3-8b** | **0.6854** | **0.6962** | **0.7568** |
| **Avg** | **0.7891** | **0.7948** | **0.8135** |
| 95% CI | [0.747, 0.824] | [0.757, 0.828] | [0.785, 0.842] |

### 一致性验证
- 所有 3 个 reference model 下，6/6 generators 的 entropy drift 方向一致（均为负），确认 depth signal 与 reference model 无关。

### 产出文件
- `data/features_qwen8b_ref_olmo.csv` — qwen3-8b × OLMo ref features (4497 rows)
- `data/features_qwen8b_ref_qwen.csv` — qwen3-8b × Qwen ref features (4497 rows)
- `data/features_ref_olmo.csv` — 已更新为 6 generators (27529 rows)
- `data/features_ref_qwen.csv` — 已更新为 6 generators (27529 rows)
- `data/cross_ref_results.json` — 完整分析结果
- `results/table4_cross_ref_logo.json` — Table 4 数字

---
