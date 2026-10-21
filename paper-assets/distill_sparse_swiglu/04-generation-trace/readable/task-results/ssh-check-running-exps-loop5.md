# ssh check running exps loop5

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_running_exps_loop5_20260516T020015_result.json`
- **Structured JSON:** [`0a88030d6bf4d780828e.json`](../../sessions/0a/0a88030d6bf4d780828e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/process_check_loop5.md`。

**汇总**:

| 实验 | 状态 | GPU |
|------|------|-----|
| lm_eval_teal_50pct (PID 190830) | ALIVE, 56% loglikelihood 进度，预计 30-60min 完成 | cuda:1, 92% util, 20GB |
| lm_eval_kl_s42 | DONE, **negative** — mmlu 0.26 (≈随机), gsm8k 0.01 | — |
| lm_eval_kl_30pct (PID 191340) | ALIVE, 运行 2h32m，0% GPU util（需关注） | cuda:0, 16GB |

kl_s42 50% sparsity 全面崩溃，winogrande 勉强 0.62，其余接近随机。GPU 0 上额外发现 kl_30pct 评估在跑但 GPU 利用率为 0，可能卡住或处于 CPU 阶段。

---
