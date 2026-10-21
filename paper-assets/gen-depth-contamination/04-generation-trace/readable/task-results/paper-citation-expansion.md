# paper citation expansion

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation-expansion_20260519T111739_result.json`
- **Structured JSON:** [`9ddb7a71721cf7872022.json`](../../sessions/9d/9ddb7a71721cf7872022.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## 引用前/后对比

| | 修改前 | 修改后 |
|---|---|---|
| Bib 条目 | 44 | 49 |
| 全文唯一引用 | 44 | 49 |

## 新增 5 篇引用

| 引用键 | 作者 | 标题 | 会议/期刊 | 年份 |
|---|---|---|---|---|
| `raffel2020t5` | Raffel et al. | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | JMLR | 2020 |
| `yang2024dnagpt` | Yang et al. | DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | ICLR | 2024 |
| `verma2024ghostbuster` | Verma et al. | Ghostbuster: Detecting Text Ghostwritten by Large Language Models | NAACL | 2024 |
| `hale2001surprisal` | Hale | A Probabilistic Earley Parser as a Psycholinguistic Model | NAACL | 2001 |
| `levy2008expectation` | Levy | Expectation-Based Syntactic Comprehension | Cognition | 2008 |

## Related Work 修改摘要

1. **Model collapse 段** (line 5): 加入 `bertrand2024stability`（已在 bib 但未在 RW 正文引用）
2. **Beyond binary detection 段** (line 12-13): 加入 `yang2024dnagpt` 到检测器列表；用 Ghostbuster + DivEye 替代原 DivEye 单独描述，突出特征方法对比
3. **Data selection 段** (line 20): 加入 `raffel2020t5` 作为 C4 数据集引用
4. **Ordinal classification 段** (line 24): 新增 surprisal 理论基础句，引用 `hale2001surprisal` 和 `levy2008expectation`，说明论文 surprisal 特征的信息论根源

## 额外修改
- `method.tex` line 55: C4 首次出现处加入 `\cite{raffel2020t5}`

注：任务列表中的大部分论文（Shumailov, Alemohammad, Dohmatob, Gerstgrasser, DetectGPT, Fast-DetectGPT, Binoculars, GLTR, Kirchenbauer, DSIR, D4, DoReMi, CodeSearchNet 等）修改前已全部在 bib 和正文中。Bertrand 2024 在 bib 但仅被 appendix 引用，现已补入 Related Work。

---
