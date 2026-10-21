# analysis e5 mistral rerun correct layers

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e5_mistral_rerun_correct_layers_20260518T205334_result.json`
- **Structured JSON:** [`4bbfbea873435b1134b1.json`](../../sessions/4b/4bbfbea873435b1134b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**Sanity check 通过**: QwQ-32B (unchanged) 结果与 v1 完全一致 (delta 全为 0)。

**修正后 HS 均提升**（3个 CHANGED 模型全部改善）：

| Model | v1 BA | v2 BA | v1 Prec | v2 Prec | v1 FPR | v2 FPR |
|-------|-------|-------|---------|---------|--------|--------|
| R1-8B | 0.7555 | **0.7568** | 0.5323 | **0.6298** | 0.2114 | **0.1251** |
| OT-7B | 0.6385 | **0.6821** | 0.3724 | **0.4460** | 0.1645 | **0.1379** |
| R1-32B | 0.7236 | **0.7419** | 0.5525 | **0.5882** | 0.3203 | **0.2730** |

**Permutation tests (E5 vs HS)**：修正 layer 后 HS 优势更大，显著性提升：
- **R1-8B**: BA p=0.0041, Prec p=0.0013, FPR p=0.0214 (v1: 0.0399, 0.033, 0.2093)
- **OT-7B**: Prec p=0.0089, FPR p=0.0066 (v1: 0.3635, 0.1808)
- **R1-32B**: BA p=0.0910 (v1: 0.2581)
- **QwQ-32B**: 不变

R1-8B 变化最大（Precision +0.097, FPR -0.086），主要来自 W 从 15 改为 3 + layer 修正的联合效应。E5 和 MiniLM 在 R1-8B 上也因 W 变化有所改变，其他模型 E5/MiniLM 不变（符合预期）。

---
