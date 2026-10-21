# paper regex baseline writeup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_regex_baseline_writeup_20260516T034437_result.json`
- **Structured JSON:** [`808267c99d39bbc2cf75.json`](../../sessions/80/808267c99d39bbc2cf75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改完成：

1. **experiments.tex**: ablation 表底部加了 `Regex (best) 93.61%` 行 + caption 注释；§4.2 末尾加了 2 行正文（6.22pp gap、8 boundary samples、caught vs uncaught）
2. **discussion.tex**: 在 Limitations 前加了 2 句——format-marker 99.33% 是格式伪像，SFT 6/8 boundary samples 证明学到 caught/uncaught 语义
3. **appendix.tex**: 新增 `\section{Regex Baseline Analysis}` 含完整 7 行基线表 + B4/B5 的详细分析

---
