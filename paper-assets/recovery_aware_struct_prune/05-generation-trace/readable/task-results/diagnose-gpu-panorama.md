# diagnose gpu panorama

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_panorama_20260519T171832_result.json`
- **Structured JSON:** [`3ac8ee7f0dc28b7ff6e0.json`](../../sessions/3a/3ac8ee7f0dc28b7ff6e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-29022 ===
cuda:0: 空闲  0%  0/97887 MiB
cuda:1: 空闲  0%  0/97887 MiB
cuda:2: PID 120188 — eval_mbpp (grpo_standard_20)  93%  16767/97887 MiB  运行 57min
cuda:3: 空闲  0%  0/97887 MiB

=== westb-23072 ===
cuda:0: PID 909411 — eval_humaneval (sft_rasp_20_1p5b)  96%  4237/97887 MiB  运行 16min
cuda:1: PID 903941 — eval_gsm8k (grpo_cka_only_20_seed123)  89%  29653/97887 MiB  运行 1h51m
```

**汇总**: 6 GPU 中 3 张在跑评测，3 张空闲（westd-29022 的 cuda:0/1/3）。

---
