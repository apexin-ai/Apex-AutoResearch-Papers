# analysis tail384 metrics extraction

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tail384_metrics_extraction_20260518T134126_result.json`
- **Structured JSON:** [`4579f721665211fb70fd.json`](../../sessions/45/4579f721665211fb70fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都完成了。汇总结果：

---

## Eval 结果：full_trace_tail_384 (n=1190, majority baseline=71.5%)

| 指标 | DeepSeek-6.7B | Qwen2.5-Coder-7B |
|---|---|---|
| **Accuracy** | **80.7%** [78.6%, 82.9%] | **79.8%** [77.6%, 82.1%] |
| **Lift over majority** | +9.2pp [+7.0, +11.5] | +8.3pp [+5.1, +11.6] |
| Pass P / R / F1 | 0.83 / 0.92 / 0.87 | 0.89 / 0.82 / 0.85 |
| Fail P / R / F1 | 0.73 / 0.51 / 0.60 | 0.62 / 0.75 / 0.68 |

**关键观察**：
- DeepSeek 和 Qwen 在 tail-384 条件下 accuracy 接近（80.7% vs 79.8%），差异不显著
- 两者有不同的 precision/recall trade-off：DeepSeek 倾向 predict pass（pass recall 高 0.92，fail recall 低 0.51），Qwen 更平衡（fail recall 0.75 明显更高）
- 结果文件已保存：
  - `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail384_seed42/final/eval_results.json`
  - `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail384_seed42/final/eval_results.json`
  - 两个 `predictions.jsonl` 也已保存

---
