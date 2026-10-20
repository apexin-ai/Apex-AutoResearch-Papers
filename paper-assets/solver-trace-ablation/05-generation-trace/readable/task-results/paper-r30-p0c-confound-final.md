# paper r30 p0c confound final

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r30-p0c-confound-final_20260522T155849_result.json`
- **Structured JSON:** [`2d57a71b5278d888d7b4.json`](../../sessions/2d/2d57a71b5278d888d7b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compile clean: 0 undefined refs, 0 multiply-defined labels, 24 pages.

---

**修改汇总**:

### 任务 1: experiments.tex (paper/ + docs/paper/)

**L44** — `$3.2\times$ → $214\times$ raw`:
- Before: `the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$`
- After: `the apparent $214\times$ raw ISR advantage collapses to $1.06\times$`

**L79-85** — Premise-count confound paragraph 全量替换:
- Before: 用 `$3.2\times$` 和 "independent of premise count" 的两层框架（5行）
- After: Director 确认的精确措辞——Scalar Goodhart（`$214\times$ → $1.06\times$`, McNemar `p=0.317`, `n=100`）+ Compositional Goodhart（"robust in modal premise-count range 4–6", `19.7%` vs `0%` TS, complexity dependence is mechanistic）（7行）

### 任务 2: appendix.tex (paper/ + docs/paper/)

**L128** — McNemar 详情更新:
- Before: `$n{=}16$ paired samples; the near-unity ratio indicates...negligible`
- After: `McNemar's test: $\chi^2{=}1.0$, $p{=}0.317$, $n{=}100$ problem-level matched pairs...not statistically significant`

**L130+** — 新增 `tab:premise-bin-modes` 表格（6行数据，3 premise bins × 2 conditions）

### 编译
0 undefined, 0 multiply, 24 pages, 无 citation warnings。

---
