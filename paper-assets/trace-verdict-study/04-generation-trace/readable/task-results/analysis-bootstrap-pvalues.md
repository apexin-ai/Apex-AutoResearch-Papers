# analysis bootstrap pvalues

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_pvalues_20260515T185923_result.json`
- **Structured JSON:** [`4aea15f26c22283c0c76.json`](../../sessions/4a/4aea15f26c22283c0c76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

| Comparison | Model | Acc A | Acc B | Diff (pp) | 95% CI | p-value | Sig? |
|---|---|---|---|---|---|---|---|
| loop_only vs no_trace | Qwen | 0.8563 | 0.7513 | +10.50pp | [+8.24, +12.86]pp | 0.0000 | Yes |
| full_trace vs no_trace | Qwen | 0.8176 | 0.7513 | +6.64pp | [+4.37, +8.99]pp | 0.0000 | Yes |
| label_only vs full_trace | Qwen | 0.8622 | 0.8176 | +4.45pp | [+2.35, +6.55]pp | 0.0000 | Yes |
| ae_only vs no_trace | Qwen | 0.9992 | 0.7513 | +24.79pp | [+22.35, +27.31]pp | 0.0000 | Yes |

所有 4 个 Qwen 比较的 p 值均 < 0.0001，95% CI 不跨零，统计显著。

**DeepSeek 状态**：deepseek_no_trace 和 deepseek_vota 目录下没有 predictions.jsonl（只有训练好的 adapter），无法计算比较。deepseek_exception_only 仅有 checkpoint-148 的 predictions，缺少 no_trace baseline 也无法比较。

注意：ae_only 的 accuracy 为 99.92%，异常高，建议检查该条件的数据/评估是否存在问题。

结果已保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/paired_bootstrap_results.json`。

---
