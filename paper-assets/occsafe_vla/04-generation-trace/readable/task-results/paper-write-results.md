# paper write results

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_write-results_20260522T183913_result.json`
- **Structured JSON:** [`17b99b47766479631e70.json`](../../sessions/17/17b99b47766479631e70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `docs/paper/results.tex`。结构：

- **§4.1 Main Results** — Table 2（6条件×TSR/CAR/Seeds），叙事覆盖 gradient flow 排序、label content 次要性、TSR 稳定性
- **§4.2 Mechanism Analysis** — 2×2 factorial 表（Table 3），gradient flow 主效应 +3.9pp，label content 主效应 -0.9pp，Detach 前向干扰解释，引用 §5 假说
- **§4.3 Per-Task Analysis** — Table 4（10 tasks × Vanilla TSR/CAR + 4条件 CAR），ceiling effect 分析，T5/T3/T6 spotlight；非 Vanilla 列为红色 placeholder
- **§4.4 Temporal Dynamics** — Cutoff 框架，三种结果预测（匹配/中间/超越 Full OCC），全部红色 placeholder
- **§4.5 Depth vs BEV** — Depth 框架，三种结果预测，全部红色 placeholder

交叉引用指向 method.tex（`eq:occ_decay`, `sec:depth_head`, `tab:ablation_design`）和 discussion.tex（`sec:why_gradient`）。所有 pending 数据用 `\textcolor{red}{}` 标记。

---
