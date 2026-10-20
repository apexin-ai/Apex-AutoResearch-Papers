# paper d111 tex modifications

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d111_tex_modifications_20260521T073709_result.json`
- **Structured JSON:** [`9e7aead9da7fb71b0465.json`](../../sessions/9e/9e7aead9da7fb71b0465.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

主文+Limitations+Ethics = 8 页（Limitations 和 Ethics 不计入8页限制），references 从第9页开始，appendix 从第11-12页开始。主文 ≤8 页，符合限制。

---

## 修改汇报

| 项 | 文件 | 行号 | 改动 |
|---|---|---|---|
| **MF-1** C3 降级 | `introduction.tex` | ~31 (item 3) | "Approximate quantitative decomposition" → "Preliminary analysis...on the Qwen-2.5-Coder-7B model (with 1.5B corroboration)" |
| **MF-1** Table caption | `experiments.tex` | 129 | 加 "Results are from Qwen-2.5-Coder-7B only; cross-model validation is left for future work." |
| **MF-1** Caveats 段 | `discussion.tex` | ~40 | 已有 "verified only on the Qwen family (two scales)"，与 C3 降级一致，无需改 |
| **MF-2** C4 降格 | `introduction.tex` | ~33 (item 4) | "Two-tier diagnostic hierarchy" → "Consistent two-tier pattern across four models: We observe that..." |
| **MF-2** Tier 段 | `discussion.tex` | 33 | 标题改为 "Observed tier pattern and future directions."，措辞改为 observational，"suggests—but does not establish—a potential fallback design" |
| **SF-1** Novelty | `introduction.tex` | ~10 | 加 "The core question driving our study is counter-intuitive: *why do richer execution traces hurt model performance?*" |
| **SF-1** Abstract | `main.tex` | 23 | 已与 intro 一致（density framing），无额外改动需要 |
| **SF-2** 应用降级 | `discussion.tex` | 33 | 合并进 "Observed tier pattern and future directions"，标注为 speculative/future work |
| **SF-3** Info density 定义 | `experiments.tex` | 123 | 加 operational definition paragraph |
| **SF-7** Abstract 数字 | `main.tex` | 23 | `${\sim}$80\%` → `76--82\%` |
| **SF-7** Intro 数字 | `introduction.tex` | 13 | `${\sim}$80\%` → `76--82\%` |
| **SF-9** 补引用 bib | `references.bib` | 446, 456 | 加 Paul et al. 2021 (Data Diet) + Sorscher et al. 2022 (data pruning) |
| **SF-9** 补引用 text | `related_work.tex` | 28 | Training Efficiency 段加 `\citep{paul2021datadiet,sorscher2022beyond}` |
| **数值** nomarker | `discussion.tex` | 21 | `96.55\%` → `97.65\%$\pm$0.93pp...3-seed mean` |
| **数值** GPU | `main.tex` | 58 | "two RTX PRO 6000 Blackwell GPUs" → "two high-end GPUs" |
| Press et al. ALiBi | — | — | 跳过（本文不涉及位置编码） |

**PDF 状态：**
- MD5: `3b5c9a07455149c597b108958e9123fb`
- 总页数: 21（主文8页 + references ~3页 + appendix ~10页）
- Warnings: **0**
- Undefined citations: **0**
- 8 页限制: **通过**（Limitations/Ethics 不计入）

---
