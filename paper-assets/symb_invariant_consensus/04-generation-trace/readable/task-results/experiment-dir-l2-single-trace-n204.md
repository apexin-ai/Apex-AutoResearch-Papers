# experiment dir l2 single trace n204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-l2-single-trace-n204_20260520T181931_result.json`
- **Structured JSON:** [`8fb884f52717703ce1f0.json`](../../sessions/8f/8fb884f52717703ce1f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。全部 3 个模型均使用完整 N=204 数据。结果摘要：

| 模型 | N | K | Single-trace mean ± std | SC@12 | Agg gain |
|---|---|---|---|---|---|
| Mistral-7B | 204 | 12 | 46.41% ± 2.80% | 54.41% | +8.01 pp |
| Qwen3-14B non-thinking | 204 | 12 | 79.37% ± 1.99% | 83.82% | +4.45 pp |
| Qwen3-14B thinking | 204 | 12 | 85.42% ± 1.08% | 86.27% | +0.86 pp |

关键变化（vs Dir-L 旧结果）：Qwen3-thinking 从 166→204 题后，single-trace mean 从 83.28% 升至 **85.42%**（新增 38 题准确率更高），SC@12 = 86.27% 与 Dir-I3 一致，aggregation gain 从 0.45pp 升至 0.86pp。

Mistral 和 Qwen3-nonthinking 数字不变（之前已是 204 题）。结果已写入 `/root/symb_invariant_consensus/results/dir_l2_single_trace_n204/results.json`。

---
