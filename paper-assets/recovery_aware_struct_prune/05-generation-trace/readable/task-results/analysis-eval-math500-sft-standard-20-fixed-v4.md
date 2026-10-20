# analysis eval math500 sft standard 20 fixed v4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_sft_standard_20_fixed_v4_20260524T091308_result.json`
- **Structured JSON:** [`2fbecd969592d36da8cc.json`](../../sessions/2f/2fbecd969592d36da8cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**总结**：

- **SFT Standard 20% → MATH-500 accuracy = 25.6%** (128/500, ±1.95%)
- 日志无异常，EXIT_CODE=0，运行 7h15m（7.35 GPU-hours）
- 46.6% 截断率较高（233/500 达到 2048 token 上限），说明剪枝后模型推理链偏长且不收敛，这本身就是 standard SFT 恢复能力有限的一个信号
- Registry 状态：DONE (success)

---
