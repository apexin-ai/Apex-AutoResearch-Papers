# paper writing introduction

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260514T192854_result.json`
- **Structured JSON:** [`78e95c44fff236f2145c.json`](../../sessions/78/78e95c44fff236f2145c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入。主要改动：

1. **结构调整**：按 Hook → Gap → 现有方法不足 → STA/ISR + 诊断结果 → Meta-Goodhart → Cross-logic → Contributions → Road map 六段式重组
2. **Contributions 改为 `enumerate[nosep,leftmargin=*]`** 编号列表，每条 1-2 句
3. **`\autoref{fig:sta-overview}`** 替换 `Figure~\ref{}`
4. **`\citep{}` 替换 `\cite{}`**（ACL 格式要求括号引用）
5. **补充引用**：加入 `\citep{lightman-verify-step}`（process reward）、`\citep{folio}`（数据集）
6. **新增内容**：process reward 局限性段落、"No existing method provides..." 总结句、annotation-free/solver-agnostic 定位
7. **末尾 road map** 指向 `\S\ref{sec:related-work}`/`\S\ref{sec:method}`/`\S\ref{sec:experiments}`/`\S\ref{sec:discussion}`
8. **所有数字与 experiments.tex/method.tex 一致**：93%/87%/0.642→0.132→0.003、64.5% H7、1.06×、92.9% genuine 等

---
