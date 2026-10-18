# code config restore hgrn2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_config_restore_hgrn2_20260518T142334_result.json`
- **Structured JSON:** [`d85161942764a5a392d5.json`](../../sessions/d8/d85161942764a5a392d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 被恢复的 config.json（5 个）

| 模型 | 状态 |
|---|---|
| 1.3B-100B-GatedDeltaNet-hybrid-12-1 | ✓ 已恢复 |
| 1.3B-100B-GatedDeltaNet-hybrid-24-1 | ✓ 已恢复 |
| 1.3B-100B-GatedDeltaNet-hybrid-3-1 | ✓ 已恢复 |
| 1.3B-100B-GatedDeltaNet-hybrid-6-1 | ✓ 已恢复 |
| 1.3B-100B-GatedDeltaNet-pure | ✓ 已恢复 |

验证通过：grep 无 `allow_neg_eigval` 残留。

### 2. HGRN2 weight tying 检查结果

**HGRN2 存在与 GDN 完全相同的 `_tied_weights_keys` 问题。** 所有 5 个 HGRN2 模型都有 `tie_word_embeddings: True`，且 fla 库的 `modeling_hgrn2.py:270` 定义了 `_tied_weights_keys = ["lm_head.weight"]`（list 类型），新版 transformers 期望 dict，导致 `AttributeError: 'list' object has no attribute 'keys'`。评测时需要同样的运行时修复（手动 tie weights）。

### 3. 所有 1.3B 模型目录清单

| 模型目录 | model_type | tie_word_embeddings |
|---|---|---|
| 1.3B-100B-GatedDeltaNet-hybrid-12-1 | gated_deltanet | False |
| 1.3B-100B-GatedDeltaNet-hybrid-24-1 | gated_deltanet | False |
| 1.3B-100B-GatedDeltaNet-hybrid-3-1 | gated_deltanet | False |
| 1.3B-100B-GatedDeltaNet-hybrid-6-1 | gated_deltanet | False |
| 1.3B-100B-GatedDeltaNet-pure | gated_deltanet | False |
| 1.3B-100B-HGRN2-hybrid-12-1 | hgrn2 | True |
| 1.3B-100B-HGRN2-hybrid-24-1 | hgrn2 | True |
| 1.3B-100B-HGRN2-hybrid-3-1 | hgrn2 | True |
| 1.3B-100B-HGRN2-hybrid-6-1 | hgrn2 | True |
| 1.3B-100B-HGRN2-pure | hgrn2 | True |
| 1.3B-100B-RetNet-hybrid-12-1 | retnet | True |
| 1.3B-100B-RetNet-hybrid-24-1 | retnet | True |
| 1.3B-100B-RetNet-pure | retnet | True |
| retnet_ms_cache | (无 config) | - |
| transformer_1.3B_baseline | transformer | True |

340M 模型目录为空。

### 4. 评测完成情况

**已完成（5 个）：**
- GatedDeltaNet-hybrid-24-1（完整 benchmarks）
- GatedDeltaNet-hybrid-3-1（完整 benchmarks）
- GatedDeltaNet-hybrid-6-1（完整 benchmarks）
- GatedDeltaNet-pure（仅 lambada_openai）
- RetNet-pure（完整 benchmarks）

**未评测（10 个）：**
- GatedDeltaNet-hybrid-12-1
- 全部 5 个 HGRN2 模型
- RetNet-hybrid-12-1, RetNet-hybrid-24-1
- transformer_1.3B_baseline

---
