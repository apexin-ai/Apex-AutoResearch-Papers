# ssh westb 25pct eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_25pct_eval_20260521T020403_result.json`
- **Structured JSON:** [`f3d2d40b3f0170a5f113.json`](../../sessions/f3/f3d2d40b3f0170a5f113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已启动并在加载模型：

| Eval | GPU | PID | 输出路径 |
|------|-----|-----|---------|
| MATH-500 on sft_standard_25 | cuda:0 | 59502 | `results/eval_math500_sft_standard_25.json` |
| HumanEval on sft_standard_25 | cuda:1 | 59663 | `results/eval_humaneval_sft_standard_25.json` |

日志：`/tmp/eval_math500_sft_standard_25.log`、`/tmp/eval_humaneval_sft_standard_25.log`

**GRPO 25% checkpoint 不在 westb 上**（在 westd-29022）。如果需要跑 GRPO 25% 的 eval，需先 `rsync` 过来（每个 checkpoint ~3-5GB，磁盘 24GB 偏紧但可行）。

---
