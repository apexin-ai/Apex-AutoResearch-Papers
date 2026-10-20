# paper writing experiments

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260515T091611_result.json`
- **Structured JSON:** [`f6985f8be5faaa4d2094.json`](../../sessions/f6/f6985f8be5faaa4d2094.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All key numbers verified present: 25.59pp gap, 83.63/58.04 accuracy, 42.88% parseable-only, 53.7/67.2% unparseable, 72.96% majority, shrout1979icc citation, D088 protocol, dataset sizes (70K/9,335/9,784), error mode breakdown (76.9%/22.9%), cross-size gaps (25.48/26.51pp), 42--43% parseable range, absolute counts (5,255/6,574).

完成。experiments.tex 已完全重写：
- §3.1: 新增 repo-level dataset 段落（70K/9,335/9,784）、ICC 引用（shrout1979icc）、D088 val-selected checkpoint protocol
- §3.2–§3.5: 保持不变，§3.3 末尾加了 §3.6 前向引用
- §3.6: 两层 C1 结构完全重写——7 列新 Table 4（含 Size 列），same-size 4B-4B 25.59pp 为主，cross-size 8B CLS vs 4B CWM 为辅，CWM 8B placeholder，单 seed 限制显式披露
- §3.7: 重写为 6 段（a–f），新增 (b) CWM error mode breakdown（v12 repo-level 数据：unparseable 分类、parseable-only 42.88%、per-repo variation）

---
