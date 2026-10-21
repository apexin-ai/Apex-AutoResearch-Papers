# eval grid b0 3 ppl and cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b0_3_ppl_and_cleanup_20260517T170830_result.json`
- **Structured JSON:** [`3e6c3afe9d0c282f63b5.json`](../../sessions/3e/3e6c3afe9d0c282f63b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。汇总结果：

```
grid_b0_3_seed456 PPL = 17.64, loss = 2.8701, tokens = 4077068

westd-41312 GPU:
cuda:0: uniform_seed42 retrain 运行中 (75014MiB, 83%)
cuda:1: ess_only_seed456 运行中 (75014MiB, 91%)
cuda:2: ess_only_seed123 运行中 (75014MiB, 100%)
cuda:3: 空闲 (eval 已完成)

westd-30476 GPU:
cuda:0: 空闲 (0MiB, 0%) — eval 进程 32393/32718 已自行结束，无需 kill
cuda:1: 训练中 PID 22478 (81678MiB, 60%)
cuda:2: 训练中 PID 22917 (46496MiB, 99%)
cuda:3: 训练中 PID 22108 rho02_adaptive_tau09_seed42 (46496MiB, 99%)
```

---
