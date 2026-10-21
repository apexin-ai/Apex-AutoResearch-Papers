# paper r30 p0 confound text

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r30-p0-confound-text_20260522T155330_result.json`
- **Structured JSON:** [`56a4d4f37c6e0afcc1fd.json`](../../sessions/56/56a4d4f37c6e0afcc1fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，0 undefined refs，0 citation warnings，0 multiply-defined labels，23 页。

---

### 修改汇总

**Task 1: experiments.tex §4.2 Premise-count confound 段**
- 文件: `paper/experiments.tex:82` + `docs/paper/experiments.tex:82`
- Before: `The asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.`
- After: 替换为两层框架——scalar level（premise-count artifact, $3.2\times \to 1.06\times$, 引用新 label `app:premise-count`）+ compositional level（CE-to-TS mode shift, OR_CMH=2.46, TS 分类不依赖 premise count）。末句明确"compositional shift 才是 Goodhart effect 的主要证据"。

**Task 2: appendix.tex premise-count confound 段**
- 文件: `paper/appendix.tex:120-128` + `docs/paper/appendix.tex:120-128`
- 新增 `\label{app:premise-count}` 于段首
- 末尾新增 2 句：(1) $1.06\times$ 基于 n=16 paired samples，near-unity 表明 scalar ISR 优势可忽略；(2) mode composition 分析（CE vs TS）不受 premise-count confound 影响，因为 TS 分类依赖 tautological proof structure

**Task 3: method.tex §3.2 — 无需修改**
- `method.tex:46` 已有 "its diagnostic value is realized through the downstream mode breakdown (\S\ref{sec:taxonomy}), not the scalar alone"
- `method.tex:54` 已区分 aggregate vs per-sample ISR
- `method.tex:82` 已有 "the mode breakdown, not the ISR scalar, licenses interpretation"

**两个目录均已同步修改。**

---
