# paper pre dream reference audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_pre-dream-reference-audit_20260519T050926_result.json`
- **Structured JSON:** [`9326b8a60684aaf03d33.json`](../../sessions/93/9326b8a60684aaf03d33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 引用审计报告

### 1. Bib 条目完整性

**总条目数：44**

**字段完整性：全部通过。** 每条均含 title, author, year, booktitle/journal。

**年份：全部合理**（2001–2026，无 2027+）。

**重复条目：无。**

**Title case / `{}` 保护：**
- 所有需要保护的缩写词（AI, LLM, GPT, MAD, GLTR, LightGBM, FineWeb, DoReMi, D4, CodeSearchNet, DivEye, CoDeC, SemEval, DetectGPT, Fast-DetectGPT, Min-K）均已用 `{}` 保护。无遗漏。

**Minor issues（不影响编译但值得留意）：**
| 条目 | 问题 |
|---|---|
| `spennemann2025quantifying` | title 含 "Delving into:" — 违反项目写作规则（正文禁用冒号式破折号/AI风格），但这是原论文标题，bib 中保留原样无问题 |
| `alain2017understanding` | booktitle = "ICLR Workshop"，缺具体 workshop 名称（minor） |
| 多条 | booktitle 格式不完全统一："Proceedings of ICML" vs "Proceedings of the 40th International Conference on Machine Learning" vs "Advances in Neural Information Processing Systems"。功能正确但风格不一致 |

### 2. 引用覆盖

**正文引用 key 数：44（去重后）**
**Bib 中存在但未引用：0 条**
**正文引用但 bib 中不存在：0 条** ← 无严重问题

**引用密度：44 条。** EMNLP 典型范围 30–60，处于正常区间。

**引用分布（按文件）：**
| 文件 | 引用次数（含重复） |
|---|---|
| related_work.tex | ~30 |
| introduction.tex | ~12 |
| experiments_c1.tex | ~4 |
| experiments_c3.tex | ~4 |
| appendix_extended.tex | ~3 |
| method.tex | 1 |
| main.tex | 0 |
| discussion.tex | 0 |

### 3. 核心论文引用检查

| 要求 key | 实际 bib key | Bib 中 | 正文引用 | 引用位置 |
|---|---|---|---|---|
| shumailov2024 | `shumailov2024collapse` | ✓ | ✓ | introduction, related_work, experiments_c3 |
| alemohammad2024 | `alemohammad2024selfconsuming` | ✓ | ✓ | introduction, related_work |
| dohmatob2024 | `dohmatob2024model` | ✓ | ✓ | introduction, related_work, experiments_c3 |
| gerstgrasser2024model | `gerstgrasser2024model` | ✓ | ✓ | related_work, appendix_extended |
| bertrand2024stability | `bertrand2024stability` | ✓ | ✓ | appendix_extended |
| drayson2025 | `drayson2025` | ✓ | ✓ | introduction, related_work, experiments_c3 |
| husain2019codesearchnet | `husain2019codesearchnet` | ✓ | ✓ | experiments_c1, appendix_extended |

**全部 7 篇核心论文均在 bib 中且被正文引用。**

### 结论

Bib 文件状态良好，无严重问题。44 条引用全部双向对应，7 篇核心论文全覆盖，引用密度达标。唯一可改进点是 booktitle 格式统一化（cosmetic）。

---
