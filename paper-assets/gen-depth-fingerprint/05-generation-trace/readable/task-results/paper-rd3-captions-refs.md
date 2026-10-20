# paper rd3 captions refs

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rd3-captions-refs_20260516T050229_result.json`
- **Structured JSON:** [`0fa04e100ce4badc74f4.json`](../../sessions/0f/0fa04e100ce4badc74f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Here's the summary:

### 修改清单

**Task 1 — 表格 caption 标注 generator split:**

| 文件 | 表格 | 改动 |
|------|------|------|
| `table4.tex` | tab:cross-ref | 加 "(6-gen LOGO)" |
| `appendix_classifier.tex` | tab:alt-classifier | 加 "(6-gen split)" |
| `appendix_classifier.tex` | tab:sampling-ablation | 加 "(6-gen LOGO)" |
| `appendix_finer_depth.tex` | tab:5class-logo | 加 "(6-gen split)" |
| `appendix_qlora.tex` | tab:qlora | 加 "6-gen" |

已有标注无需修改：tab:logo-results, tab:ablation, tab:baselines, tab:human-edit, tab:lofo, tab:confusion（均已含 "6-gen" 或 "6-generator"）。

**Task 2 — Qwen3-0.6B self-referencing bias:**

`discussion.tex`: 在 "Comparison with detector ensembles" 段后、"Prompt-type dependence" 段前插入 `\paragraph{Reference model choice.}`，说明 Qwen3-0.6B 双重角色的偏差有限 (+1.3pp)，主实验默认用 Pythia-410M 避免重叠。数字与 results.tex §4.2 和 limitations.tex 一致。

**Task 3 — MR verified: all references present.** energy_ood (Liu 2020), mahalanobis_ood (Lee 2018), fineweb (Penedo 2024), dolma (Soldaini 2024), model_collapse_avoidable (Gerstgrasser 2024) 均在 references.bib 中。

**Task 4 — main.tex appendix 完整性:** 9 个 appendix \input 均存在。`appendix_dataset_stats.tex` 仅存在于 `docs/paper/`，尚未出现在 `artifacts/_project/paper/`，待另一 Worker 完成后添加 \input。

---
