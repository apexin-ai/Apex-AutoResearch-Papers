# analysis eval results compilation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-results-compilation_20260514T125616_result.json`
- **Structured JSON:** [`c9b3049492ef1ddc6a30.json`](../../sessions/c9/c9b3049492ef1ddc6a30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/report_eval_compilation.md` 并注册为 `art_20260514_69dbcf`。

核心数据：

- **Aligned 已完成**：4/24 cells (16.7%) — 0.5B d000 (original+para), 1.5B d000, 1.5B d100
- **运行中**：9 cells，完成后达 54.2%
- **主要缺口**：d025 全线缺失（4 点曲线关键中间点），3B paraphrase 全部未开始
- **唯一可算 delta**：0.5B d000 baseline (MMLU −4.5pp, GSM8K +8.9pp, ARC −1.0pp)，反映 paraphrase 难度差异 noise floor
- **1.5B d000→d100**：MMLU +0.80pp, GSM8K −0.46pp, ARC −0.34pp — 100% 污染下 MC benchmark 变化极小，HumanEval +17.7pp 显著但 appendix-only

---
