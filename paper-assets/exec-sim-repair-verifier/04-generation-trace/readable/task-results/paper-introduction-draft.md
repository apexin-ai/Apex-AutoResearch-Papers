# paper introduction draft

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_introduction-draft_20260515T143417_result.json`
- **Structured JSON:** [`1e68b52bcc401d456d93.json`](../../sessions/1e/1e68b52bcc401d456d93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `artifacts/_project/paper/introduction.tex` 并注册。

**要点概述：**
- ~1000 words，完整 story arc：hook (verification bottleneck) → gap (CWM generation failure modes) → insight (classification reformulation) → 3 contributions
- 所有定量 claim 均来自 registry 已验证数字：function-level 1.24pp (5 seeds)、8B scaling 2.43pp (p=0.008)、repo-level 25.59pp、CWM unparseable 53.7–67.2%、TOST p=0.007、oracle 90.63%、zero-shot baselines
- 引用 key 与 related_work.tex 一致（`meta2025cwm`, `ding2025selfexecution`, `zhang2025swerm`, `snell2024scaling`, `jimenez2024swebench`）
- 引用 `Figure~\ref{fig:reformulation}` 对应 fig1
- 单 seed 结果未用 "consistently" 等措辞；多 seed 结果标注了 seed 数量和 p 值

---
