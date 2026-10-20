# ops sync paper and citations

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_paper_and_citations_20260515T234454_result.json`
- **Structured JSON:** [`f1e25872f730048e5870.json`](../../sessions/f1/f1e25872f730048e5870.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报清单

### 同步的文件
所有 docs/paper/sections/ 的 .tex 文件已与 artifacts 版一致（前一个 Worker 已完成内容同步和 section header 剥离）。本次修复了全部 44 个引用键格式问题：

| 文件 | 字节数 | 引用键修复数 |
|------|--------|-------------|
| introduction.tex | 5,768 | 7 |
| method.tex | 9,163 | 8 |
| experiments.tex | 2,604 | 5 |
| related_work.tex | 5,259 | 21 |
| results.tex | 4,404 | 2 |
| limitations.tex | 1,576 | 1 |
| conclusion.tex | 1,324 | 0 |

### 引用修复
1. **introduction.tex:2** — `20--60\% of crawled data~\citep{cheng2025contamination}` — 已存在（来自 artifacts 同步）
2. **related_work.tex:5** — `\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora` — 已存在

所有引用键从 artifact 格式（`cheng_2025_contamination_survey`）统一为 bib 格式（`cheng2025contamination`）。bib 中已有 `cheng2025contamination` 条目（references.bib:118），无需添加。

### experiments.tex Evaluation 段落内容
第 16 行：`We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text`  — "held-out FineWeb" 和 "human-authored" 均存在。

### 编译结果
**成功**。7 页，269KB PDF。  
- 修复了 `\bibliographystyle` 重复（acl.sty 已提供，main.tex 中的重复已移除）  
- 3 个 undefined ref warnings（`app:proofs`, `fig:dual_constraint`, `app:grid`）— 指向尚未创建的 appendix/figure，非致命

### 空文件
- `abstract.tex` (0 bytes)
- `appendix.tex` (0 bytes)
- `discussion.tex` (0 bytes)

---
