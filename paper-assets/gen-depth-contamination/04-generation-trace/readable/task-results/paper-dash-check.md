# paper dash check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_dash-check_20260519T035417_result.json`
- **Structured JSON:** [`6e7cc1d22feb92d0aa13.json`](../../sessions/6e/6e7cc1d22feb92d0aa13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dash 修正结果

| 文件 | 行 | 原文 | 修正 | 说明 |
|---|---|---|---|---|
| `main.tex:1` | `% EMNLP 2026 Main — ARR May 2026` | `% EMNLP 2026 Main - ARR May 2026` | 注释行 em-dash，已修正 |

**解释性 en-dash（ – ）**：全文未发现。

**数字范围 en-dash（1.4B--8B 等）**：均为 LaTeX `--` 写法，属于例外，保留。

---

## `-ing` 分词短语（需改写清单）

以下均为句末/句中的尾随 -ing 分词短语，是典型 AI 写作痕迹：

### introduction.tex
| 行 | 原文片段 |
|---|---|
| 8 | `...treats all machine-generated text identically, **discarding** the generational depth dimension.` |
| 21 | `...information degrades monotonically across generations, **motivating** a finite discrimination boundary $\Kstar$.` |

### discussion.tex
| 行 | 原文片段 |
|---|---|
| 35 | `...Wikipedia yields $\Kempirical{=}1$..., **producing** a consistent ordering that correlates with structural complexity` |
| 37 | `...(CI upper $= 0.603$), **paralleling** its narrower surprisal dynamic range on code generation` |
| 38 | `...has $\Kempirical{=}3$ on arXiv, **reinforcing** the domain-governed interpretation` |

### main.tex
| 行 | 原文片段 |
|---|---|
| 77 | `...CI lower marginally below $\theta$ ($0.5979$), **indicating** the boundary weakens at longer generation lengths.` |

### appendix_extended.tex
| 行 | 原文片段 |
|---|---|
| 69 | `...fine-tuned model, **creating** inter-generation dependencies that standard bootstrap resampling cannot preserve without **inflating** AUC estimates.` |
| 115 | `...same step-function AUC decay pattern as low-truncation models, **confirming** that EOS truncation does not drive the boundary.` |
| 147 | `...above the base model (0.6018), **indicating** that synthetic data at these proportions is net-beneficial` |
| 150 | `...**confirming** that depth assignments beyond $\Kempirical$ inject noise regardless of contamination severity.` |
| 295 | `...near-complete information loss at the first step, **making** the exponential fit unreliable` |
| 298 | `...supply persistent depth-distinguishing signal, **explaining** the elevated $\Kempirical{=}3$.` |
| 313 | `...**indicating** that domain lexical diversity can rescue even web-text one-wash generators` |
| 315 | `...**indicating** that scale in the 1B--14B range does not shift the discrimination boundary.` |
| 319 | `...**confirming** that arXiv's $\Kempirical{=}3$ at the same sample size reflects genuine domain signal` |
| 329 | `...**indicating** that deeper generations produce proportionally more formatting tokens.` |
| 381 | `...**confirming** that our results are well above the minimum required for reliable boundary estimation.` |
| 420 | `...**indicating** that no single feature group is individually critical` |
| 511 | `...**making** the discrepancy attributable to mode rather than threshold instability.` |
| 517 | `...**invalidating** the gap-based threshold derivation.` |
| 613 | `...**indicating** that the scorer model already finds Mistral's output highly predictable.` |

**总计 21 处**，高频词：`indicating`(8)、`confirming`(4)、`making`(2)、其余各 1 次。正文（introduction + discussion + main）有 6 处，appendix 有 15 处。正文部分建议优先改写。

---
