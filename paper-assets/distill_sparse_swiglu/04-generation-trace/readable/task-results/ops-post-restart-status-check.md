# ops post restart status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_status_check_20260520T030321_result.json`
- **Structured JSON:** [`b317ef8295d5587944a6.json`](../../sessions/b3/b317ef8295d5587944a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-41718 ===
mse30_s42_train (cuda:0): ALIVE  step 170/1000  loss=0.0043  sparsity=0.336  checkpoint: 无
cuda:1: 空闲 (0 MiB, 0%)

=== westd-34887 ===
qwen14b_teal30_global_hspiqa (cuda:0): ALIVE  45% (18305/40168 loglikelihood)  ~28min elapsed  结果: 无
qwen14b_bce30_global_hspiqa (cuda:1): ALIVE  46% (18321/40168 loglikelihood)  ~28min elapsed  结果: 无
```

三个进程全部存活，服务重启未受影响。MSE 训练约完成 17%，两个 global eval 均约 45%，预计还需 ~35 分钟完成。

---
