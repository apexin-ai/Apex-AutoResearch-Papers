# diag westb status harvest 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westb_status_harvest_20260522_20260522T020941_result.json`
- **Structured JSON:** [`fe1f6aee450955b30fb9.json`](../../sessions/fe/fe1f6aee450955b30fb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== GPU 状态 ==
GPU 0: 17053/97887 MiB (17%), utilization 97%
GPU 1: 19195/97887 MiB (20%), utilization 99%

== eval_math500_sft_cka_only_20_v7 (GPU 0, PID 133850) ==
状态: RUNNING
进度: 203/500 (41%)
启动时间: 2026-05-22 08:38
已运行: ~1.5h
预计剩余: ~2-3h
Interim accuracy: 日志中无中间 accuracy 输出（仅 tqdm 进度条）

== eval_math500_sft_standard_25 (GPU 1, PID 104592) ==
状态: RUNNING
进度: 483/500 (97%)
启动时间: 2026-05-21 23:20
已运行: ~10.8h
预计剩余: ~25min
Interim accuracy: 日志中无中间 accuracy 输出
注: v1 结果 (13.0%) 已存在于 /root/autodl-tmp/.../results/eval_math500_sft_standard_25.json，当前为 v2 重跑

== 可用 checkpoint（/root/autodl-tmp/recovery_aware_struct_prune/）==
sft_cka_only_20, sft_standard_25/checkpoint-1870, sft_cka_only_20_1p5b,
sft_rasp_20_1p5b, sft_standard_20_1p5b, sft_rasp_rlvr_20,
sft_qwen_math_cka_only_20_final, sft_standard_20_qwen_math_final,
grpo_cka_only_20, grpo_standard_25_westb, grpo_cka_only_20_seed123,
pruned_* (6 variants), grpo_*_1p5b (3 variants)

== 可用结果文件 ==
/root/recovery_aware_struct_prune/results/: 30+ JSON（含 eval_checkpoint-100_greedy.json 等）
/root/autodl-tmp/.../results/: 60+ JSON（含 gsm8k, humaneval, mbpp, math500, inference_benchmark 等）
```

standard_25 还差 17 个样本，~25 分钟内完成。cka_only_20_v7 预计还需 2-3 小时。两个结果 JSON 都尚未生成，无法收割。

---
