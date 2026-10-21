# eval qwen adaptive fix lm eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen_adaptive_fix_lm_eval_20260517T144741_result.json`
- **Structured JSON:** [`ebba668b2228ff37a979.json`](../../sessions/eb/ebba668b2228ff37a979.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已完成。结果（0-shot，lm-eval-harness 默认）：

| Task | Metric | Value | Stderr |
|------|--------|-------|--------|
| **arc_easy** | acc | 0.6515 | ±0.0098 |
| | acc_norm | 0.6166 | ±0.0100 |
| **hellaswag** | acc | 0.3791 | ±0.0048 |
| | acc_norm | 0.4791 | ±0.0050 |
| **piqa** | acc | 0.6882 | ±0.0108 |
| | acc_norm | 0.6888 | ±0.0108 |
| **winogrande** | acc | 0.5777 | ±0.0139 |

注意：用户指定了 few-shot（HellaSwag 10-shot, ARC-Easy 25-shot, PIQA 5-shot, WinoGrande 5-shot），但这次 eval 用的是 **0-shot**（`--num_fewshot` 未指定）。需要确认是否要用指定的 few-shot 设置重跑。现有的 qwen_base 和 qwen_adaptive 评估也是 0-shot，所以如果用于对比，0-shot 结果是一致可比的。

要我用指定的 few-shot 设置重跑吗？

---
