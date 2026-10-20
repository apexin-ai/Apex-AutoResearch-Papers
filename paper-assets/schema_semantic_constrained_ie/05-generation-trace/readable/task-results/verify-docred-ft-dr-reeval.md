# verify docred ft dr reeval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_docred-ft-dr-reeval_20260523T114011_result.json`
- **Structured JSON:** [`53353ae7552681604892.json`](../../sessions/53/53353ae7552681604892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。最终报告：

---

## 重验结果

所有 DR 值均用 **violation_checker_docred.py (fixed_20260514_v2)** 重算，包括 unconstrained 基线，确保一致可比。

| 实验 | 论文 DR% | 重算 DR% | 偏差 | 需修正? |
|---|---|---|---|---|
| w8_qwen_docred_ft_semantic_only | 0.21 | **0.19** (31/15909) | -0.02pp | 轻微，可接受 |
| w8_llama_docred_ft_semantic_only | 0.30 | **0.48** (77/16038) | **+0.18pp** | **必须修正** |
| w8_llama_docred_ft_grammar_only | 0.51 | **0.51** (82/16199) | 0.00pp | 匹配 |

## Unconstrained 基线验证（同一 checker）

| 模型 | 基线 DR% | 重算 DR% | 一致? |
|---|---|---|---|
| Qwen | 0.76 | 0.76 (121/15870) | 是 |
| Llama | 0.49 | 0.49 (80/16171) | 是 |

## Semantic DR Reduction 修正

| 模型 | 计算方式 | 论文隐含值 | 修正值 |
|---|---|---|---|
| Qwen | (0.76−0.19)/0.76 | 72% | **75%** |
| Llama | (0.49−0.48)/0.49 | 39% | **2%** |
| **Range** | | **39--72%** | **2--75%** |

## 影响

正文 claim "39--72% DR reduction" **不成立**。Llama semantic-only 仅减少 3 个 DR violation（80→77），reduction 仅 2%，远非 39%。这意味着 semantic constraint 对 FT Llama+DocRED 几乎无效。

论文中 0.30% 可能是用旧版 checker（未修正 entity type normalization）计算的结果。当前修正版 checker 多检出约 29 个 DR violation。

## 已完成

- 3 个实验的 DR_pct 已回填至 registry（含 ET/RV/CF 全量 violation 数据）
- 需要修正论文中 Llama semantic-only DR 值和 "39--72%" claim

---
