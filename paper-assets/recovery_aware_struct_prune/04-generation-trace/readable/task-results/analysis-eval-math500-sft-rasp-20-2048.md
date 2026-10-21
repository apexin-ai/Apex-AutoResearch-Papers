# analysis eval math500 sft rasp 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_sft_rasp_20_2048_20260519T013720_result.json`
- **Structured JSON:** [`d3c1c1e6279020b7f485.json`](../../sessions/d3/d3c1c1e6279020b7f485.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `eval_math500_sft_rasp_20_2048` 结果：

| 指标 | 值 |
|---|---|
| **MATH-500 Accuracy** | **22.6%** |
| Correct / Total | 113 / 500 |
| Stderr | ±1.87% |
| Avg response length | 930.58 tokens |
| Median response length | 274.0 tokens |
| Natural EOS | 314 (62.8%) |
| Truncated (hit 2048) | 186 (37.2%) |

模型路径: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd`

日志文件不存在，数据全部来自 JSON。无 W&B run ID。

注意：37.2% 的样本被截断到 2048 tokens，且截断样本的 pred 几乎全为 null（未能产出答案），这是拉低 accuracy 的重要因素。

---
