# analysis paper status and debugbench summary

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_status_and_debugbench_summary_20260516T040953_result.json`
- **Structured JSON:** [`3cd98b08bf35740eb0e3.json`](../../sessions/3c/3cd98b08bf35740eb0e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

## 任务 1：论文状态

| 文件 | 行数 | 最后修改 |
|------|------|----------|
| main.tex | 39 | 03:46 (框架文件) |
| introduction.tex | 30 | 07:44 |
| method.tex | 85 | 07:48 |
| experiments.tex | 189 | 10:29 |
| discussion.tex | 86 | 10:50 |
| related_work.tex | 29 | 07:55 |
| conclusion.tex | 19 | 07:56 |
| appendix.tex | 224 | 09:32 |
| references.bib | 213 | 08:00 |
| **main.pdf** | — | **12:11 (已编译)** |

论文位于 `/root/trace-verdict-study/docs/paper/`（不是 `/paper/`），ACL review 格式，标题 *"Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction"*。Abstract 完整，所有 section 有内容，PDF 已编译（322KB）。Introduction 和 related_work 较短（各~30行），experiments 和 appendix 最充实。Discussion 今天最近修改（10:50）。

## 任务 2：DebugBench 跨任务分析

已写入 `artifacts/debugbench_cross_task_analysis.md` 并注册（`art_20260516_bbd3c1`）。

核心数字全部通过 registry 交叉验证（修正 no_trace 为 75.13%，用户原文 75.10% 有微小偏差）。分析包含：
- 跨任务对比表（3 conditions × 2 benchmarks）
- 4 个关键发现（baseline 极高、exception 100%、marginal contribution 任务依赖、universal signal）
- Regex baseline 6 策略汇总（B5 最高 99.33%，McNemar p=0.041）
- 4 个 Discussion 角度及可直接用于论文的英文句子

---
