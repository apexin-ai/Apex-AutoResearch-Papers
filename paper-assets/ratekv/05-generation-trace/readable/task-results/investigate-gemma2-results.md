# investigate gemma2 results

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_gemma2_results_20260514T154602_result.json`
- **Structured JSON:** [`121f31c40a34f77e575f.json`](../../sessions/12/121f31c40a34f77e575f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 rerun 产出的新结果文件。结论明确：

---

## Gemma-2-9B 数据质量报告

### 1. 真实 bf16 baseline PPL
**未知（需要重跑）**。当前文件里的 711.38 是 BOS bug 产生的错误值。rerun 中校准数据的 baseline PPL 从 1077 降到 9.38（~115x），按此比例 wikitext2 baseline 应在 **~6-7** 左右，与 D044 提到的 "PPL 7" 一致。

### 2. 711.38 的来源
wikitext2 bf16 baseline，由 **未修复 BOS bug 的代码** 计算。Gemma 2 要求每个 chunk 以 BOS token 开头，缺少 BOS 导致模型推理时上下文错乱，PPL 膨胀约 100 倍。

### 3. BOS fix 状态
- 修复代码 **已存在** 于 `run_gemma2_full_pipeline.py`：
  - 校准数据：L159-164，给每条序列前置 `bos_id`
  - wikitext2 评估：L244-263，检测并补 BOS，排除 BOS logit
- 但 `gemma2_full_results.json`（May 14 23:15）是修复 **之前** 产生的
- rerun（May 14 23:46）使用了修复后的代码（calibration baseline=9.38），但 **只完成了 47% 的 Phase 1 profiling 就中断了**，没有产出新的结果文件

### 4. 结论
**需要重跑。** 当前 `gemma2_full_results.json` 中的所有数值（baseline、MCKP、uniform、k ablation）全部无效——它们都基于错误的 profiling 数据（BOS bug 使校准 baseline 为 1077 而非 9.38，profiling delta 严重失真）。registry 中的 711.38 应标记为 invalid。

---
