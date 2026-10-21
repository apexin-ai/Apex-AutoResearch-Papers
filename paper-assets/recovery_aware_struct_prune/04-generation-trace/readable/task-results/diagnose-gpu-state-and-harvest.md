# diagnose gpu state and harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_state_and_harvest_20260519T152702_result.json`
- **Structured JSON:** [`04bdb0d8ffae64415368.json`](../../sessions/04/04bdb0d8ffae64415368.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

旧 PID 96018、86171、112015 已全部结束。汇总如下：

```
=== westd-29022 ===
cuda:0: 空闲 (0%, 0 MiB)
cuda:1: PID 113408 — eval_mbpp_grpo_cka_only_20 (95%, 17518 MiB) 运行 47min
cuda:2: PID 108291 — eval_mbpp_dense_unpruned (91%, 17658 MiB) 运行 1h39m
cuda:3: 空闲 (0%, 0 MiB)

旧 PID 状态：96018 (eval_humaneval_grpo_cka_only_20_1p5b_2048)、86171 (eval_humaneval_sft_standard_20_2048_v3)、112015 (sft_shortgpt_20) 均已结束。

=== westb-23072 ===
cuda:0: PID 900959 — eval_humaneval_grpo_standard_20_1p5b_2048 (94%, 4186 MiB) 运行 27min
        （原 PID 890559 eval_humaneval_sft_standard_20_1p5b_2048 已结束）
cuda:1: 空闲 (0%, 0 MiB)

=== eval_gsm8k_grpo_rasp_20_fair 结果 ===
状态: 已完成 (2026-05-19 23:20:25)
accuracy: 0.6088 ± 0.0134
correct: 803 / 1319
mode: greedy
eos_rate: 98.79%
avg_response_length: 195.7 tokens
truncated: 16 / 1319
```

---
