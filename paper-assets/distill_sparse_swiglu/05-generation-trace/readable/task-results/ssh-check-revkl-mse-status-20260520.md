# ssh check revkl mse status 20260520

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_revkl_mse_status_20260520_20260520T205750_result.json`
- **Structured JSON:** [`6c6bf7b0714dc7b39e13.json`](../../sessions/6c/6c6bf7b0714dc7b39e13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-41718: RevKL 30% uniform ===
Status: RUNNING (both on HellaSwag, competing for GPU 0)
PID 279686 (nohup): alive, 1h11m elapsed
PID 280143 (tmux):  alive, 1h08m elapsed

Partial results:
  PPL: 9.3081  (both processes agree)

Progress:
  Completed tasks: wikitext2, arc_challenge, winogrande+mmlu, gsm8k
  Current task: hellaswag (loglikelihood)
    PID 279686: 3673/40168 = 9.1%, ~8.65 it/s, ETA ~70 min
    PID 280143:  489/40168 = 1.2%, ~8.25 it/s, ETA ~80 min
  Remaining: piqa

⚠️ 两个进程抢同一个 GPU 0，互相拖慢。速度只有正常的一半（~8 it/s vs 正常 ~18 it/s）。
建议 kill 其中一个，预计 HellaSwag + PIQA 还需 ~40-50 min（单进程）。

=== westd-34887: MSE 50% s123 eval retry ===
Status: RUNNING
PID 240870: alive, 4m elapsed

Partial results:
  PPL: 15789.6426  ⚠️⚠️⚠️

Progress:
  Completed tasks: wikitext2, arc_challenge
  Current task: winogrande + mmlu (just started)
  Remaining: gsm8k, hellaswag, piqa

⚠️ PPL=15789 基本等于随机输出，checkpoint 有严重问题。
日志显示 layers 17-19, 22, 26-28 的 sparsity 严重偏离 target（0.255~0.381 vs target 0.500）。
下游指标大概率也会崩。是否要提前 kill 节省时间？
```

---
