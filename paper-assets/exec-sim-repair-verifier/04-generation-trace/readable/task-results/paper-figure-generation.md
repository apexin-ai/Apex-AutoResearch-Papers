# paper figure generation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-generation_20260515T182118_result.json`
- **Structured JSON:** [`fb1a1c2b37391eb1dbff.json`](../../sessions/fb/fb1a1c2b37391eb1dbff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 张图表全部生成完毕，位于 `artifacts/` 目录：

| 文件 | PDF | PNG |
|------|-----|-----|
| Fig 1: Task Reformulation | 35K | 218K |
| Fig 2: Gap Amplification | 22K | 73K |
| Fig 3: Oracle Stratified | 25K | 139K |

视觉检查结果：
- **Fig 1** — 三行流程图，CLS/CWM/TRAJ 分色标注，CWM 下方标注 3 failure modes，TRAJ 标注 no per-test signal
- **Fig 2** — Broken axis 柱状图，下半 0–5pp 放 Function 级别，上半 20–28pp 放 Repo-level 25.59pp，带 error bars 和 "single seed" 标注
- **Fig 3** — 分组柱状图 + 右 Y 轴 Instance share 折线，T=2 处标注 "55.3% of total advantage"，T=1 两个 bar 接近 0

---
