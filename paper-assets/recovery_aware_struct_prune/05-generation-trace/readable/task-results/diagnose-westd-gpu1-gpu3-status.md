# diagnose westd gpu1 gpu3 status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_gpu1_gpu3_status_20260522T113444_result.json`
- **Structured JSON:** [`8c016a6066a911499a59.json`](../../sessions/8c/8c016a6066a911499a59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd:1 MATH-500 SFT Random ===
PID 5241: alive (运行 7h29m, CPU 101%)
结果文件: 不存在
状态判断: 运行中, 373/500 (75%), 预计还需 ~2.5h

=== westd:3 pipeline_depth_first_20 ===
PID 40073: alive (运行中, eval_gsm8k_grpo_depth_first_20)
PID 36161: alive (父进程)
GRPO eval 结果: 不存在
SFT eval 结果: 不存在
状态判断: Phase 4 (Eval GRPO) 运行中, Phase 5 (Eval SFT) 待执行

=== GPU 总览 ===
GPU 0: 54341/97887 MiB, 89% — grpo_rasp_alpha3p0_20_v2 训练 (PID 42008)
GPU 1: 17651/97887 MiB, 98% — eval_math500_sft_random_20_v3 (PID 5241, 75%)
GPU 2: 16261/97887 MiB, 93% — (可能是 pipeline Phase 4 的实际 GPU 分配)
GPU 3: 28832/97887 MiB, 95% — eval_gsm8k_grpo_random_20_seed123 (PID 41541, tmux) + pipeline eval 共占
```

注意: GPU 3 上同时跑了 pipeline 的 Phase 4 eval 和 tmux 里的 eval_gsm8k_grpo_random_20_seed123，两个 eval 共享 GPU 3 可能导致速度下降。

---
