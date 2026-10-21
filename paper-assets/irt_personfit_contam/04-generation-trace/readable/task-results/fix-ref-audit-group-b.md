# fix ref audit group b

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ref-audit-group-b_20260526T114339_result.json`
- **Structured JSON:** [`1a490cc97eaccb6eea9d.json`](../../sessions/1a/1a490cc97eaccb6eea9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 git repo，已完成文件编辑但未 commit。

### 修改汇总

**文件 1: `paper/sections/background.tex`**
- 第 15 行：`Min-K\%++` → `Min-K\% Prob`（修正方法名归因）

**文件 2: `paper/references.bib`**
- 删除 `levine1988` 条目（原第 108–117 行，无 .tex 引用）
- `golchin2024quiz`：year `2024` → `2025`，补 `volume = {13}`, `pages = {809--830}`
- `oren2024`：title `Black-Box` → `Black Box`（匹配官方标题）
- `han2026quantifying`：booktitle 改为 `Findings of the Association for Computational Linguistics: EACL 2026`（统一格式）
- `martinezplumed2019`：补 `volume = {271}`, `pages = {18--42}`

---
