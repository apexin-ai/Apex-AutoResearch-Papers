# paper critical auroc fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_critical-auroc-fix_20260523T195406_result.json`
- **Structured JSON:** [`6995b12d8a49a00fb9b2.json`](../../sessions/69/6995b12d8a49a00fb9b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修正报告：

### 修正结果

**Issue 1 — SciERC EM AUROC**
- `experiments_main.tex:40`: `\textbf{.749}` → `.631`（d114_auroc_investigation 确认 .749 来自 exp_012 的错误 AUROC 计算；正确 seed=42 值 .614，多 seed 均值 .631±.013）
- `experiments_main.tex:38`: SJ AUROC `.692` → `\textbf{.692}`（SJ 现为 SciERC AUROC 最高）
- appendix:1927 未修改（该排名是 LLaMA-3.2-3B 的 AUROC，EM=.776 确实是 3B 最高，与主表无关）

**Issue 2 — tab:selection caption**
- 已是修复后的版本，无需改动

**Issue 3 — MV +0.61pp → +0.6pp**
- `experiments_main.tex:90`: "MV $+0.61$\,pp on CoNLL" → "MV $+0.6$\,pp on CoNLL"
- `introduction.tex:11`: 同上

**编译**：0 undefined refs，46 页，无新 warning

**匿名仓库**：commit `b26efad`，4 files changed，已 push 到 `main`

---
