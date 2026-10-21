# paper final compress v4

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-compress-v4_20260516T053602_result.json`
- **Structured JSON:** [`c6a1841867dcb33d2bf2.json`](../../sessions/c6/c6a1841867dcb33d2bf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No LaTeX warnings. All done. Here's the summary:

---

## 结果

### 行数对比

| 文件 | 压缩前 | 压缩后 | 变化 |
|------|--------|--------|------|
| introduction.tex | 30 | 30 | 0 |
| method.tex | 85 | 51 | -34 |
| experiments.tex | 210 | 106 | -104 |
| discussion.tex | 28 | 28 | 0 |
| related_work.tex | 29 | 19 | -10 |
| conclusion.tex | 19 | 19 | 0 |
| appendix.tex | 324 | 465 | +141 |

### McNemar p 值修正

- **修正位置**: experiments.tex 第208行 (唯一出现)
- **修正前**: B4 vs SFT: `McNemar $p{=}0.041$` (错误)
- **修正后**: B4 vs SFT: `McNemar $p{<}0.001$`; B5 vs SFT: `McNemar $p{=}0.041$`

### 编译结果

- **总页数**: 19页
- **正文页数**: 8页 (pages 1-8, bibliography starts page 9)
- **Undefined references**: 0
- **LaTeX errors**: 0 (仅有预存在的 package-level warnings)

### 移入 Appendix 的内容

1. Trace length ablation (表+分析) → `sec:trace_length_full`
2. Calibration analysis (表+图+分析) → `sec:calibration_full`  
3. Density decomposition table → `sec:density_analysis`
4. Robustness analysis → `sec:robustness_analysis`
5. DebugBench full results → `sec:debugbench_full`
6. Regex baseline details → `sec:regex_baselines`
7. Tokenizer analysis → `sec:tokenizer_analysis`
8. Training dynamics label alias → `sec:training_dynamics`

### B5 regex 扩写

正文 regex 段落中增加了 B5 format marker 的详细分析（4句），说明其利用 preprocessing artifact、与 SFT 的机制差异、以及 McNemar p=0.041 的正确归属。

---
