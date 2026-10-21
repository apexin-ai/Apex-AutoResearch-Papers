# analysis w2 regex baseline verification

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w2_regex_baseline_verification_20260521T061442_result.json`
- **Structured JSON:** [`72c230e040e7aba966a7.json`](../../sessions/72/72c230e040e7aba966a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/w2_regex_baseline_analysis.md`。

核心发现：

| 指标 | 值 |
|------|-----|
| **Best regex (B_marker)** | **99.33%** (1182/1190) |
| **SFT (3 seeds 一致)** | **99.83%** (1188/1190) |
| **Delta** | **+0.50% = 6 样本** |

**Reviewer 的推演有误**：`[ERROR]→fail, else→pass` 只有 93.45%（漏掉 70 个 `[No trace available]` fail 样本）。最优 regex 是 `[No exception data in trace]→pass, else→fail`，达到 99.33%，而非 Reviewer 声称的 99.83%。

**SFT 的 6 样本优势全部来自 caught exceptions**：HumanEval/95 的 `check_dict_case` 函数用 try/except 捕获 ValueError，trace 有 `[ERROR]` 但程序正常通过。SFT 学会了区分 caught vs uncaught exception，regex 做不到。

**唯一共同失败**：2 个 GeneratorExit 样本（Python generator 清理时的 benign exception），SFT 和 regex 都判错。

**Rebuttal 可用的 4 个论点**已列在报告 Section 5。

---
