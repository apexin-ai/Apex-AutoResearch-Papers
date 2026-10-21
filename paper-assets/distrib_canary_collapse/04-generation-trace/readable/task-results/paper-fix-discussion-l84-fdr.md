# paper fix discussion L84 fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_discussion_L84_fdr_20260518T014147_result.json`
- **Structured JSON:** [`ef0a0d3828bb47c8241b.json`](../../sessions/ef/ef0a0d3828bb47c8241b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 errors，输出 26 页 PDF。

修改完成。`discussion.tex` 的 canary quality hierarchy 段落已修正：
- 原文错误地将所有条件统称为 "non-significant after FDR correction"
- 新文本区分了 Baseline/OPT（$p\approx 0.03$, FDR 后不显著）和 C4（3/4 pairs $p<0.005$, BH-significant）
- 补充了 "coupling strength varies with training domain" 的解释，衔接后续 calibration-diversity feedback 机制段

---
