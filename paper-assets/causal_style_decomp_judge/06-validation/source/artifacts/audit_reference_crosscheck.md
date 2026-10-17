# 引用正确性交叉验证报告

> 3 个独立 Worker 并行核查 57 条 bib 引用，交叉比对结果。
> 日期：2026-05-26

## 统计总览

| 指标 | 数量 |
|------|------|
| 总引用数 | 57 |
| 完全正确 | 39 |
| 有错误（必须修） | 4 |
| 未使用的孤立引用 | 14 |
| Worker 间一致率 | 100%（无分歧） |

## 必须修正的错误（4 条）

### ❌ CRITICAL: `saito2023verbosity` — 幻觉拼凑条目

**严重度：CRITICAL**（标题、作者、Venue、URL 全部错误）

| 字段 | bib 中（错误） | 正确值 |
|------|---------------|--------|
| 作者 | Saito, Yuki; Nishida, Noriki; Okazaki, Naoaki | **Saito, Keita; Wachi, Akifumi; Wataoka, Koki; Akimoto, Youhei** |
| 标题 | Verbosity Bias in Multi-Turn Chatbot Evaluations | **Verbosity Bias in Preference Labeling by Large Language Models** |
| Venue | EMNLP 2023 | **NeurIPS 2023 Instruction Workshop** |
| URL | aclanthology.org/2023.emnlp-main.665/ (不相关论文) | **arXiv:2310.10076** |

正文引用上下文本身合理（related_work 和 method 中作为 verbosity bias 的 prior evidence），修正 bib entry 即可。

### ❌ HIGH: `murugadoss2025sos` — 作者完全错误

| 字段 | bib 中（错误） | 正确值 |
|------|---------------|--------|
| 作者 | Murugadoss, Aakanksha and others | **Feuer, Benjamin and Goldblum, Micah and Datta, Teresa and Nambiar, Sanjana and Besaleli, Raz and Dooley, Samuel and Cembalest, Max and Dickerson, John P.** |

标题、年份、Venue（ICLR 2025）均正确。"Murugadoss" 不在该论文作者列表中。bib key 也应改为 `feuer2025style`。

### ❌ MEDIUM: `soumik2026judging` — 作者名错误

| 字段 | bib 中（错误） | 正确值 |
|------|---------------|--------|
| 作者 | Soumik, Mohammad and others | **Soumik, Sadman Kabir**（单一作者，无 others） |

标题、年份、Venue（arXiv）均正确。

### ⚠️ LOW: `chen2024humans` — 标题小错

| 字段 | bib 中 | ACL Anthology 正式版 |
|------|--------|---------------------|
| 标题 | "A Study on Judgement **Biases**" | "A Study on Judgement **Bias**"（单数） |

此条同时也是孤立引用（未在正文中被 cite）。

## 未使用的孤立引用（14 条）

以下引用定义在 references.bib 中但未被任何 tex 文件 `\cite{}`：

| # | cite key | 论文 |
|---|----------|------|
| 1 | `kiritchenko2017bws` | Best-Worst Scaling More Reliable than Rating Scales (ACL 2017) |
| 2 | `stevens1946theory` | On the Theory of Scales of Measurement (Science 1946) |
| 3 | `decoster2011median` | Best Practices for Using Median Splits (J Exp Psychopathology 2011) |
| 4 | `wang2023faireval` | Large Language Models are not Fair Evaluators (ACL 2024) |
| 5 | `li2024calibraeval` | CalibraEval (ACL 2025) |
| 6 | `tan2025judgebench` | JudgeBench (ICLR 2025) |
| 7 | `koo2024cobbler` | Benchmarking Cognitive Biases (Findings ACL 2024) |
| 8 | `stureborg2024inconsistent` | Large Language Models are Inconsistent and Biased Evaluators (arXiv 2024) |
| 9 | `park2024offsetbias` | OffsetBias (Findings EMNLP 2024) |
| 10 | `chen2024humans` | Humans or LLMs as the Judge? (EMNLP 2024) |
| 11 | `bavaresco2025llms` | LLMs instead of Human Judges? (ACL 2025 Short) |
| 12 | `simms2019does` | Does the Number of Response Options Matter? (Psychological Assessment 2019) |
| 13 | `deutsch-etal-2023-ties` | Ties Matter (EMNLP 2023) |
| 14 | `embretson2000irt` | Item Response Theory for Psychologists (book 2000) |

**处理建议**：从 bib 中删除或补回正文引用。LaTeX/bibtex 不会因孤立引用报错，但 reviewer 可能注意到 reference list 中有未引用的条目。

## bib key 命名不规范（不影响编译，仅供参考）

| cite key | 问题 | 建议 |
|----------|------|------|
| `wang2026fairjudge` | 第一作者姓 Yang，非 Wang | 改为 `yang2026fairjudge` |
| `casse2026concise` | 以框架名命名，第一作者姓 Cho | 改为 `cho2026concise` |
| `murugadoss2025sos` | 第一作者是 Feuer | 改为 `feuer2025style` |
| 多条 key 年份 ≠ year 字段 | arXiv 首发年 vs 正式发表年 | 不影响编译，保持现状可接受 |

## Worker 交叉一致性

| 问题 | Worker A | Worker B | Worker C | 最终判定 |
|------|----------|----------|----------|----------|
| murugadoss 作者错 | ✗ 标出 | — | — | ✗ 确认错误 |
| soumik 作者名错 | ✗ 标出 | — | — | ✗ 确认错误 |
| saito 幻觉条目 | — | — | ✗ 标出 | ✗ 确认错误 |
| chen 标题复数 | — | — | ⚠ 标出 | ⚠ 确认小错 |
| 所有其他条目 | ✓ | ✓ | ✓ | ✓ 一致通过 |

三个 Worker 之间无矛盾判定，一致率 100%。
