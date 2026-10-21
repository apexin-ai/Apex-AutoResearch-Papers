# writing generalization

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_generalization_20260515T155339_result.json`
- **Structured JSON:** [`06616454adabbf9989e4.json`](../../sessions/06/06616454adabbf9989e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `section_generalization.tex`，已注册 artifact。

**报告：**

| Subsection | 内容 | 关键数据 |
|---|---|---|
| 5.1 Baseline Comparison | RF/CORAL/DivEye 统计不可区分，叙事重心在 feature set 而非 classifier；DeepSeek zero-shot 40.0% 作 external anchor | tab_baselines 含 7 methods |
| 5.2 Cross-Model Transfer | mean 66.4%，per-class recall 表完整呈现 d0 膨胀 + d2 bottleneck (26.8–52.6%)，3-class 55.4% | tab_cross_model 含 per-class recall |
| 5.3 Cross-Strategy Transfer | mean 59.1%，temp09 d1v2 反转 (0.13/0.25)，z-score falsification (LR d1v2 0.50→0.24/0.19)，RF scale-invariant | tab_cross_strategy 含 z-score LR 行 |
| 5.4 Negative Result | DeBERTa 58.3%/RoBERTa 59.5% << RF 78.2%，feature overlap ρ=−0.484，DCOL v6 64.5% + 过拟合 | architecture-independent conclusion |

**交叉引用**：`\ref{sec:gen:crossstrategy}` 与 Discussion §6 已有引用对齐；`\ref{sec:generalization}` 与 Method §3 对齐。占位表/图 label (`tab_baselines`, `tab_cross_model`, `tab_cross_strategy`, `fig_confusion_matrix`) 均已嵌入。约 980 words 正文（不含表格）。

---
