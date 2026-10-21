# analysis eval gsm8k sft standard 20 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_gsm8k_sft_standard_20_1p5b_20260519T031959_result.json`
- **Structured JSON:** [`1aa950b1b899766317fb.json`](../../sessions/1a/1aa950b1b899766317fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果 JSON（核心字段）

```json
{
  "model_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b",
  "mode": "greedy",
  "accuracy": 0.22896133434420016,
  "stderr": 0.01156902486841511,
  "n_correct": 302,
  "n_total": 1319,
  "eos_stats": {
    "natural_eos": 1193,
    "truncated": 126,
    "eos_rate": 0.9044730856709629,
    "avg_response_length": 516.69,
    "max_response_length": 4096,
    "min_response_length": 32
  },
  "temperature": 0.0,
  "do_sample": false,
  "examples": [ ... 20 examples ... ]
}
```

## 关键指标

| 指标 | 值 |
|---|---|
| **Accuracy** | **22.90%** (302/1319) |
| Stderr | ±1.16% |
| EOS rate | 90.45% (126 truncated) |
| Avg response length | 516.7 tokens |

## Log 尾部

- 模型加载时检测到 Non-uniform MLP：`intermediate_size range [3738, 8960]`
- 评估耗时约 4h15m（1319 samples，greedy decoding）
- 最终输出：`GSM8K Accuracy: 0.2290 ± 0.0116 (302/1319)`
- 退出码 0，正常完成

---
