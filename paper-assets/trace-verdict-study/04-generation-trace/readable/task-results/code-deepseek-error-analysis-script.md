# code deepseek error analysis script

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deepseek_error_analysis_script_20260515T153137_result.json`
- **Structured JSON:** [`a6650698a4fecf4e7fde.json`](../../sessions/a6/a6650698a4fecf4e7fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建在 `/root/trace-verdict-study/eval/error_analysis.py`，参数解析正常。

用法：
- 首次运行（生成 predictions）：`python eval/error_analysis.py --gpu 0`
- 已有 predictions：`python eval/error_analysis.py --skip_eval`

分析维度：cross-tabulation → label 分布 → error direction → input/trace token 长度 → trace feature 分布（has_error/has_assert/has_loop/truncated/no_trace）→ error type 统计 → raw_pred 分析（含 illegal token 检测）→ problem-level 聚合。结果同时输出 stdout 和 JSON 到 `deepseek_vota/final/error_analysis.json`。

---
