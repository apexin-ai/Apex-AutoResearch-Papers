# fix lr verifier numbers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_lr_verifier_numbers_20260516T160217_result.json`
- **Structured JSON:** [`6ccc4f8abab52e160f14.json`](../../sessions/6c/6ccc4f8abab52e160f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数值已经是修正后的了。在 `experiments.tex:153` 可以看到 `F1${=}0.641$` 和 `experiments.tex:154` 有 `AUROC (0.652)`——这正是 exp-027 的修正值。

**结论：旧数值（0.697 和 0.648）已经不存在于 `docs/paper/sections/` 的任何 tex 文件中。当前文件已使用 exp-027 的修正值：**
- AUROC = 0.652（experiments.tex:154）
- F1 = 0.641（experiments.tex:153）

无需修改。此任务已由之前的编辑完成。

---
