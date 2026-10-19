# ops p0 fix c1 s123 and verify evals

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-fix-c1-s123-and-verify-evals_20260518T171731_result.json`
- **Structured JSON:** [`69de2f8f87a6ce55e731.json`](../../sessions/69/69de2f8f87a6ce55e731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### Task 1: 50% KL s123 checkpoint

**存在，在 westd-34887 上：**
```
/root/distill_sparse_swiglu/checkpoints/kl_50pct_s123/predictor_kl_normalized.pt
```
- 大小：151,966,687 bytes
- 时间：May 17 18:56

westd-41718 上没有 `kl_50pct_s123`，但有 `mvp_kl_norm_v2_s123`（不同实验）。如果 C1 ablation 需要在 41718 上跑，需要先把 checkpoint scp 过去。

### Task 2: 3 个 eval 全部在跑

| Eval | Server | tmux session | PID | GPU 占用 | 状态 |
|------|--------|-------------|-----|---------|------|
| bce_30pct_s42_eval | westd-41718 | ✅ 存在 (01:12:43) | 89401 | 44840 MiB (cuda:0) | ✅ 运行中 |
| kl_sparsity35_s42_eval_teal | westd-34887 | ✅ 存在 (01:12:47) | 39468 | 44840 MiB (cuda:0) | ✅ 运行中 |
| kl_sparsity45_s42_eval_teal | westd-34887 | ✅ 存在 (01:12:49) | 39548 | 44840 MiB (cuda:1) | ✅ 运行中 |

三个 eval 日志都显示 progress bar 正在推进，无需重新提交。

### 下一步

C1 ablation s123 需要的 50% KL checkpoint 在 westd-34887 上已就绪。需要确认 C1 ablation 在哪台机器上跑，如果在 41718 需要先传输 checkpoint。

---
