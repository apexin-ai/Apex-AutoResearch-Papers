# paper citation check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation-check_20260514T132110_result.json`
- **Structured JSON:** [`d783731d7c87182fcbf9.json`](../../sessions/d7/d783731d7c87182fcbf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 引用完整性报告

### Critical: 缺失引用（tex 中引用但 bib 中无条目）

**无。** 全部 23 个引用 key 在 `references.bib` 中均有对应条目。

### Info: 未使用引用（bib 中有但 tex 中未引用）

7 条：
| Key | Title |
|-----|-------|
| `compression-ordering-2025` | A Systematic Study of Compression Ordering for LLMs |
| `h2o-neurips2023` | H₂O: Heavy-Hitter Oracle for Efficient Generative Inference |
| `mustafar-neurips2025` | Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning |
| `obcache-2025` | OBCache: Optimal Brain KV Cache Pruning |
| `pagedeviction-eacl2026` | PagedEviction: Structured Block-wise KV Cache Pruning |
| `pyramidkv-2024` | PyramidKV: Dynamic KV Cache Compression |
| `raas-acl2025` | RaaS: Reasoning-Aware Attention Sparsity |

注：`h2o-neurips2023` 和 `pyramidkv-2024` 在 `discussion.tex` 正文中以文字形式提及（"H₂O, SnapKV, PyramidKV"），但未用 `\cite{}` 引用。可考虑补上 `\cite`。

### Warning: 格式不完整的 bib 条目

**无。** 全部 30 条 bib 条目均包含 title、author、year 三个必需字段。

---
