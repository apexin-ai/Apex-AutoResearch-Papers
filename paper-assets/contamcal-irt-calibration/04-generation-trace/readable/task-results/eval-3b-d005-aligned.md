# eval 3B d005 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_3B_d005_aligned_20260514T131326_result.json`
- **Structured JSON:** [`7c71a882dd75abc45d14.json`](../../sessions/7c/7c71a882dd75abc45d14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：未提交新任务（C001 约束）。** cuda:4 上已有完全相同的 3B d005 aligned eval 在运行（PID 373931，启动于 21:09:39），参数一致：

- adapter: `Qwen2.5-3B_d005_s42/lora_adapter` (114MB, 验证通过)
- output: `Qwen2.5-3B_d005_s42_aligned/`
- benchmarks: mmlu gsm8k arc_challenge humaneval, mc-format aligned

已补建 registry 记录 `exp_001_eval_3B_d005_aligned` → RUNNING，parent 指向 `exp_001_sft_d005_3B`。

---
