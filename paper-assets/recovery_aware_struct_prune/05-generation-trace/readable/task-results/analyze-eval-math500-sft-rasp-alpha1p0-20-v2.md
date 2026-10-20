# analyze eval math500 sft rasp alpha1p0 20 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_math500_sft_rasp_alpha1p0_20_v2_20260522T225931_result.json`
- **Structured JSON:** [`3bb76b9001f7e5c86352.json`](../../sessions/3b/3bb76b9001f7e5c86352.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_math500_sft_rasp_alpha1p0_20_v2 结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **21.2%** (106/500) |
| Stderr | ±1.83% |
| Natural EOS | 314 (62.8%) |
| Truncated | 186 (37.2%) |
| Avg response length | 930.58 tokens |

**模型**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd`（Non-uniform MLP, intermediate_size 范围 [8128, 18944]）

**运行状态**: 正常完成，EXIT_CODE=0，耗时约 1h36m。

**值得注意**: 37.2% 的回复被截断（达到 2048 token 上限），说明模型在较难题目上倾向于生成冗长但不收敛的推理链。截断样本的答案提取质量可能受影响。

---
