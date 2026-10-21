# fix ft ablation data correction

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ft_ablation_data_correction_20260516T171555_result.json`
- **Structured JSON:** [`3debce170e8c2df15083.json`](../../sessions/3d/3debce170e8c2df15083.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files now match the reviewer's correct data and are consistent with each other. Registry verification confirmed all values match.

---

## 修正清单

### 文件 1: `ft_ablation_analysis.md` — 15 个字段修正

| 行 | 字段 | 错误值 | 正确值 |
|---|---|---|---|
| Qwen Grammar Only | RV% | 0.27 | 0 |
| Qwen Grammar Only | CF% | 0.12 | 0.11 |
| Qwen Grammar Only | E_F1 | 82.15 | 82.19 |
| Qwen Grammar Only | R_F1 | 40.86 | 40.85 |
| Qwen Grammar Only | Parse Fail% | 7.11 | 7.01 |
| Qwen Semantic Only | RV% | 0.27 | 0.23 |
| Qwen Semantic Only | CF% | 0.12 | 0.27 |
| Qwen Semantic Only | R_F1 | 40.86 | 40.89 |
| Qwen Semantic Only | Parse Fail% | 7.11 | 7.52 |
| Llama Unconstrained | DR% | 0.51 | 0.49 |
| Llama Unconstrained | CF% | 0.16 | — |
| Llama Unconstrained | E_F1 | 84.04 | 83.93 |
| Llama Unconstrained | R_F1 | 43.77 | 43.72 |
| Llama Grammar Only | RV% | 0.15 | 0 |
| Llama Grammar Only | CF% | 0.16 | 0.12 |

### 文件 2: `table4_ft_ablation.md` — 7 个字段修正

| 行 | 字段 | 错误值 | 正确值 |
|---|---|---|---|
| Llama semantic_only | E_F1 | — | 84.02 |
| Llama semantic_only | R_F1 | — | 43.90 |
| Llama semantic_only | ET% | — | 0.00 |
| Llama semantic_only | RV% | — | 0.15 |
| Llama semantic_only | DR% | — | 0.30 |
| Llama semantic_only | CF% | — | 0.16 |
| Llama semantic_only | Parse Fail% | RUNNING | 2.40 |

错误模式：ft_ablation_analysis.md 中 grammar_only 和 semantic_only 行直接复制了 unconstrained 的 RV/CF/E_F1/R_F1/parse_fail 值；unconstrained 行则复制了 grammar_only 的 DR/CF/E_F1/R_F1 值。table4 的 DocRED 数据原本就是正确的（除了 Llama semantic_only 当时还在 RUNNING）。

SciERC 部分两文件均与 registry 一致，无需修正。

---
