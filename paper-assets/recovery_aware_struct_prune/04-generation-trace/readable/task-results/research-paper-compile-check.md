# research paper compile check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_compile_check_20260521T153325_result.json`
- **Structured JSON:** [`fa1f64d34c6c45680934.json`](../../sessions/fa/fa1f64d34c6c45680934.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture.

---

## 编译状态：PASS

- 0 errors, 0 undefined references（full bibtex cycle 后全部 resolve）
- BibTeX warnings: 2 个空 journal 字段（`davari2023cka`, `selfhealing2025`）—— 可能是 arXiv 预印本，不影响编译
- 若干 overfull/underfull hbox 警告（排版微调，非阻塞）

## 页数：14 页总计，主文本 = 8 页（刚好踩线）

| 区域 | 页码 |
|---|---|
| 主文本（Abstract → Conclusion） | 1–8 |
| Limitations + Ethics | 8（尾部）–9 开头 |
| References | 9–10 |
| Appendix | 10–14 |

主文本恰好 8 页，**符合 EMNLP 2026 限制**，但没有余量。任何新增内容都会超页。

## TODO/FIXME/TBD 标记

**活跃源文件中：无。** 所有 TBD/TODO 标记仅存在于不参与编译的文件中：

| 文件 | 标记 | 状态 |
|---|---|---|
| `tables/table2_recovery.tex:11` | "TBD" | 旧表，未被任何 `\input` 引用 |
| `backup/experiments.tex:38,46` | `[TBD]` | backup 目录，不编译 |
| `backup/introduction.tex:35` | `% TODO` | backup 目录，不编译 |

## MATH-500 表格结构

文件：`tables/tab_math500.tex`，通过 `appendix.tex:103` 的 `\input{tables/tab_math500}` 引入（Appendix §MATH-500 Out-of-Distribution Evaluation, label `sec:appendix_math500`）。

结构：3 列表格 `{Method, Recovery, MATH-500 (%)}` ，**数据已完整填入**：

| Method | Recovery | MATH-500 (%) |
|---|---|---|
| Dense | -- | 53.0 |
| CKA-only | SFT | 29.0 |
| CKA-only | GRPO | 29.2 |
| Standard | SFT | 25.8 |
| Standard | GRPO | 26.4 |
| RASP | SFT | 22.6 |
| RASP | GRPO | 24.0 |

表格下方有脚注说明 Dense 模型在 2048 tokens 下的截断效应。**无需 Paper Agent patch——数据已齐全。**

---
