# exp attention gradient analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_attention_gradient_analysis_20260522T035342_result.json`
- **Structured JSON:** [`61a32439a40d4d63d4f1.json`](../../sessions/61/61a32439a40d4d63d4f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交。

- **exp_id**: `attention_gradient_analysis`
- **PID**: 742526
- **GPU**: cuda:1
- **Log**: `~/runs/trace-verdict-study/attention_gradient_analysis.log`
- **tmux session**: `attention_gradient_analysis`
- **输出目录**: `/root/trace-verdict-study/artifacts/attention_gradient_analysis/`

脚本说明：
- 数据中无 Python 异常（Traceback/Error），trace 是变量状态日志，故 token 分类适配为 4 类：**source_code** / **test_code** / **execution_trace** / **framing**
- Part A: 200 个 fail 样本的 last-layer attention（verdict→all tokens），按 section 聚合
- Part B: input embedding gradient L2 norm w.r.t. verdict CE loss，按 section 聚合 + 归一化
- Part C: 3 张图（attention heatmap × 2, gradient bar chart, dilution comparison）+ results.json
- gradient dilution ratio = trace token 占比 / trace gradient 占比，越大说明稀释越严重

---
