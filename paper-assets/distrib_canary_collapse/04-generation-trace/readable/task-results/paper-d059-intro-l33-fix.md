# paper d059 intro L33 fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d059_intro_L33_fix_20260518T041708_result.json`
- **Structured JSON:** [`ff016cb9682640b8da40.json`](../../sessions/ff/ff016cb9682640b8da40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 errors，26 页 PDF 输出正常。

---

## 产出汇总

### 1. L33 修改前后对比

**修改前** (introduction.tex:33):
```
...the full consensus pipeline confirms directional asymmetry with cross-correlation
|r|>0.99, 24/24 forward-direction pairs significant, and 0/24 in the reverse direction.
```

**修改后**:
```
...the full consensus pipeline confirms directional asymmetry with cross-correlation
|r|>0.99; token entropy maintains complete unidirectional precedence (0/12 reverse
across 4 seeds and 3 diversity metrics), while ECE shows marginal reverse significance
($p\approx 0.03$) consistent with a canary quality hierarchy (\S\ref{sec:discussion}).
```

### 2. 0/16→0/12 修改位置

| 文件 | 行号 | 上下文 |
|------|------|--------|
| abstract.tex | 5 | "0/16 reverse pairs significant across 4 seeds" → 0/12 |
| conclusion.tex | 16 | "token entropy: 0/16 reverse pairs across 4 seeds" → 0/12 |
| experiments.tex | 147 | "token entropy reverse 0/16 across four seeds" → 0/12 |

全文 grep 确认 0/16 无残留。

### 3. 0/24 和 24/24 残留检查

所有剩余出现均属正确语境，无需修改:
- **FPR null control** (0/24, 3 seeds × 8 pairs): abstract:3, conclusion:9, experiments:234-235, introduction:32, method:128
- **α=0.75 regime** (19/24 forward, 0/24 reverse, 3 seeds × 8 pairs): abstract:5, conclusion:15, introduction:34,48, limitations:39, experiments:205
- **差分前后** (24/24→24/24): experiments:66,79, method:23
- **regime shift** (24/24→0/8): conclusion:5, introduction:41
- **regime onset** (0/24 at α≤0.25): introduction:26, method:29

### 4. 编译结果

`pdflatex` 编译通过，0 errors，输出 main.pdf (26 pages, 491 KB)。

---
