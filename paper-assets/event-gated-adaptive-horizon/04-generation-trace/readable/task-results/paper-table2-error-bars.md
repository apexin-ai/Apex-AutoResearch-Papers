# paper table2 error bars

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table2-error-bars_20260529T003406_result.json`
- **Structured JSON:** [`71b2a012f220248e13ea.json`](../../sessions/71/71b2a012f220248e13ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 overfull 警告，表格完整。

## 产出汇总

### 1. 每组 exp_ids + eval_return 值

| Group | Seeds | Experiments & eval values |
|---|---|---|
| **Untreated** | 10 | W: 008d/009e s1=131.1, 009b s2=267.9, 008d_s3=268, 008d_s4=63.6, 059 s5=95.8, 068 s1r=39.1; C: 010b_s0=0.83, 010b s1=51.7, 078 s0=119.5, 097 s3=61.7 |
| **Reward-only SGS** | 2 | 016e=31.7, 044=538.6 |
| **Full-pathway SGS** | 3 | 018v2=448.3, 018 s2=40.8, 021=221.5 |
| **Obs-decoder SGS** | 6 | 025 s1=726.4, s2=89.6, s3=590.2, s4=241.5; 026 s0=38.8, s1=38.3 |
| **RAVE** | 2 | 028 c2.0=29, 028 c1.5=76.2 |
| **TCN σ=0.1** | 1 | 029c=188.6 |
| **TCN σ=0.2** | 6 | 027_σ02=171.4, 029a=180.3, 029b=44.7, 029d=104.5, 030a(C)=31.9, 031(P)=11.6 |
| **TCN σ=0.5** | 3 | 027 s0=166.4, 027 s1=94.6, 030b(C)=143.6 |
| **TCN σ=1.0** | 1 | 030c(C)=72.8 |
| **Wide single** | 2 | 033=407.9, 037(C)=146.1 |
| **Narrow dual** | 2 | 035=697.8, 039=592.7 |
| **Wide dual** | 4 | 032=739.7, 032b=516, 041=544, 034(C)=97.5 |
| **Frozen** | 7 | 042=612, 067=281.5, 047=144.2, 057=123.9, 084=334.1, 046(C)=150.5, 058(C)=80.5 |
| **Removed** | 6 | 008f=139.5, 008f s1=468.8, 008f s4=289.3, 009c s3=311.9, 024b(C) s0=96.5, s1=77.3 |

### 2. Mean±std (%BL)

| Group | Eval (%BL) |
|---|---|
| Untreated | 15±10% |
| Reward-only SGS | 31±39% |
| Full-pathway SGS | 34±26% |
| Obs-decoder SGS | 33±31% |
| RAVE | 6±4% |
| TCN σ=0.1 | 21% (n=1) |
| TCN σ=0.2 | 14±7% |
| TCN σ=0.5 | 20±11% |
| TCN σ=1.0 | 16% (n=1) |
| Wide single | 39±8% |
| Narrow dual | 70±8% |
| Wide dual | 55±24% |
| Frozen | 31±18% |
| Removed | 29±13% |

### 3. 表格 diff

添加了第 6 列 `Eval (%BL)`，更新了 `tabular` 为 `{llcccc}`，caption 中增加了 Eval 列说明。

### 4. 编译结果

pdflatex 成功，42 页输出，0 个 overfull hbox 警告。表格在单栏内正常显示。

---
