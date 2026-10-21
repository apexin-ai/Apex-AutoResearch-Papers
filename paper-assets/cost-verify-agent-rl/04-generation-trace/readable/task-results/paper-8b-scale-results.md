# paper 8b scale results

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_8b-scale-results_20260520T131942_result.json`
- **Structured JSON:** [`35ae09e0997283cb4fa5.json`](../../sessions/35/35ae09e0997283cb4fa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已在两个文件中添加 `\subsection{Cross-Scale Verification}` (`\label{sec:cross_scale}`)：

- `docs/paper/experiments.tex` — 添加在 §5.7 Results 之后
- `artifacts/_project/paper/experiments.tex` — 添加在 §5.5 Additional Baselines 之后

内容结构：
- 开头段：动机（scale invariance 测试）
- 4 个 `\paragraph{}`：Setup / Information loss / Cell A collapse / Cell C episode-level
- `Table 5`（`tab:8b_results`）：4 行汇总 SFT baseline / SFT h=2 / Cell A / Cell C
- 结尾段：scale-invariant 结论

所有数字附 `% exp_id:` 注释，无 em-dash，无 -ing 短语结尾，booktabs 表格格式。

---
