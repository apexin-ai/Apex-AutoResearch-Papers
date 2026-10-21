# analyze eval math500 sft standard 20 2048 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_math500_sft_standard_20_2048_v2_20260519T085554_result.json`
- **Structured JSON:** [`c398e24c9221b9601f65.json`](../../sessions/c3/c398e24c9221b9601f65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已提取。

**final_accuracy: 25.8% (129/500)**

| 指标 | 值 |
|---|---|
| Accuracy | 25.8% (129/500) |
| Stderr | ±1.96% |
| Checkpoint | `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20` |
| Natural EOS | 53.4% (267/500) |
| Truncated | 46.6% (233/500) |
| Avg response length | 1145.7 tokens |
| Median response length | 1501.5 tokens |

**异常/错误**: 无。日志中有 HuggingFace Hub 网络不可达警告，但成功使用了本地缓存，500 题全部评测完成。

**W&B run**: 日志中未记录 W&B 信息。

**对比上下文**: ROADMAP 中中间进度显示 20.8% (104/500)，最终结果为 25.8% (129/500)。在所有 20% 剪枝方法中，SFT Standard (25.8%) 低于 CKA-only SFT (29.0%) 和 GRPO Standard (26.4%)，但高于 SFT RASP (22.6%) 和 GRPO RASP (24.0%)。

---
