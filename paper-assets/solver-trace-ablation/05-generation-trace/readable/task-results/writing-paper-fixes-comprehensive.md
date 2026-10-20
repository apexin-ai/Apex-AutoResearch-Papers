# writing paper fixes comprehensive

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-fixes-comprehensive_20260515T035141_result.json`
- **Structured JSON:** [`a240a078ff0966429fbb.json`](../../sessions/a2/a240a078ff0966429fbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复清单

**CRITICAL**
- C1 ✅ `experiments.tex:36` ISR* 比较方向修正为 "31.2% hacking (vs. SFT's 7.1%)"
- C2 ✅ `appendix.tex` 新增 `\subsection{Per-Seed Results at β=0.3}` (label `app:beta03`)；`experiments.tex` β=0.3 段落末尾加 `(Appendix~\ref{app:beta03})`

**WARNING**
- W1 ⏭ `introduction.tex` 引用已正确（`sec:diagnostic` / `sec:crosslogic` / `sec:taxonomy`），无需修改
- W2 ⏭ `app:per-seed` 在任何 .tex 中均不存在，无需修改
- W3 ✅ `tab:beta01-3seed` → `tab:fol-beta01-detailed`，`tab:prolog-crosslogic` → `tab:prolog-detailed`；同步更新了 4 处 `\ref{}`（experiments.tex×1，appendix.tex×3）
- W4 ⏭ `0.885` 不存在于任何 .tex 中（仅出现在 experiments.md），无需修改
- W5 ✅ `abstract.tex` β=0.3 改为 "extreme cross-seed instability (PR 66±42%), with individual seeds collapsing to as low as 18%"
- W6 ✅ `experiments.tex:153` `32% non-hacking` → `31% non-hacking`
- W7 ✅ `limitations.tex` "the 1,204 FOL-annotated examples available in FOLIO" → "FOLIO"

## 编译结果

- 4 趟编译（pdflatex → bibtex → pdflatex × 2）全部 `EXIT=0`
- `main.pdf` 14 页，正常生成
- `main.log` 无 undefined reference、无 multiply defined label
- 仅有的 warning：`'h' float specifier changed to 'ht'`（两个表格的 float placement，仍为原有非阻塞 warning）和 hyperref 的 PDF string token warning（与改动无关）

无新的 reference/label warning。

---
