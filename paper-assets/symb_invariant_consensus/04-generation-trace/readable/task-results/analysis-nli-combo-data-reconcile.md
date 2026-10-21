# analysis nli combo data reconcile

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-combo-data-reconcile_20260522T145105_result.json`
- **Structured JSON:** [`f4581c67df9713e2b607.json`](../../sessions/f4/f4581c67df9713e2b607.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整的证据链已找到。根因是 **tiebreaking bug**。

---

## 排查结果

### 1. +6.67pp 来自哪个实验

来自 `nli_combo_recomputed.json`（tiebreaking 修正后的版本）：
- **配置**: DeBERTa-large-MNLI × Mistral-7B × ProofWriter-600, w=3, n=600
- **SC baseline**: 39.33% (236/600)
- **combo w=3**: 46.00% (276/600), **+6.67pp**, McNemar p=1.13e-05
- **tiebreaking**: 字母序（alphabetical），与 SC baseline 一致

### 2. exp-090 是什么实验

`exp-090-r-nli-proofwriter`，**同一实验的原始版本**（未修正 tiebreaking）：
- 完全相同的模型、数据集、配置
- **combo w=3**: 42.83% (257/600), **+3.50pp**, McNemar p=0.0125
- **tiebreaking**: `Counter.most_common(1)[0][0]`——插入序（insertion-order），与 SC baseline 不一致

### 3. 数据不一致的根因

**Tiebreaking bug**。详见 `nli_tiebreaking_audit.json`：

| 项目 | exp-090 (buggy) | recomputed (corrected) |
|------|-----------------|----------------------|
| tiebreaking | `Counter.most_common()` 插入序 | `sorted(tied)[0]` 字母序 |
| combo w3 correct | 257/600 | 276/600 |
| delta | +3.50pp | +6.67pp |
| McNemar p | 0.0125 | 1.13e-05 |
| 受影响题数 | — | 30题 |

combo 脚本用 `votes.most_common(1)[0][0]` 做 tie resolution，而 SC baseline 用字母序。两套 tiebreaking 标准导致 combo 在 30 个平票问题上选了不同答案。DRC cascade pilot 独立使用字母序也得到 46.0%，交叉验证了修正值。

### 4. 论文应引用哪组数据

**+6.67pp (recomputed)**。理由：
- 字母序 tiebreaking 与 SC baseline convention 一致（同一 comparand 同一标准）
- DRC cascade pilot 独立确认 46.0%
- BH 校正后 p=6.78e-05，仍 <0.001
- tiebreaking audit 明确建议更新到修正值

**需要做的**：将 exp-090 registry 的 metrics 更新为修正后数值，避免未来再次产生混淆。exp-091/092/093 也需要同步 recompute（audit 标记为 `NEEDS_RECOMPUTATION`）。

---
