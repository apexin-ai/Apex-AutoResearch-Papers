# ssh gpu status check all 20260522T2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_all_20260522T2_20260522T202438_result.json`
- **Structured JSON:** [`7edd3236beb30d4a1bbc.json`](../../sessions/7e/7edd3236beb30d4a1bbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== WESTD-32935 ===
GPU 0: PID=66827, 16990 MiB, experiment=eval_math500_sft_rasp_alpha3p0_20, progress=308/500 (62%)
GPU 1: PID=75284, 16758 MiB, experiment=eval_math500_sft_cka_only_20 (新启动 04:06), progress=22/500 (4%)
GPU 2: PID=58276, 19218 MiB, experiment=eval_math500_sft_rasp_alpha0p5_20, progress=371/500 (74%)
GPU 3: PID=58435, 17518 MiB, experiment=eval_math500_sft_rasp_alpha4p0_20, progress=425/500 (85%)

所有 4 GPU 利用率 98%，全部满载。

=== WESTB-23072 ===
GPU 0: IDLE (0 MiB, PID 234500 已不存在)
GPU 1: PID=220343, 16538 MiB, experiment=eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2, progress=224/500 (45%)

注意：GPU 0 显示 100% utilization 但 0 MiB 且无计算进程，为驱动残留报告，实际空闲。

=== α=1.0 RESULT ===
NOT FOUND — 文件 eval_math500_sft_rasp_alpha1p0_20.json 不存在（eval 在 304/500 时被 kill，结果文件未写入）
```

**补充：** westd-32935 GPU 1 上的 CKA-only eval 已由迁移 worker 成功启动（PID 75284, 04:06 开始），正在跑 sft_cka_only_20 的 MATH-500 评测。α=1.0 需要重跑，当前没有空闲 GPU——最快释放的是 GPU 3（α=4.0, 425/500, 预计 ~1-2h 完成）。

---
