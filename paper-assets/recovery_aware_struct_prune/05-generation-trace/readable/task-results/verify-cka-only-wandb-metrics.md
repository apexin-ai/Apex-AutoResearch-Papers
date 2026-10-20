# verify cka only wandb metrics

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cka_only_wandb_metrics_20260518T022117_result.json`
- **Structured JSON:** [`c6f765f83551ed645b07.json`](../../sessions/c6/c6f765f83551ed645b07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已提取。结果如下：

| Step | reward | frac_zero_std | entropy | grad_norm | kl |
|------|--------|---------------|---------|-----------|------|
| 10 | 0.2531 | 0.1750 | 0.0830 | 1.8906 | 0.00121 |
| 20 | 0.2181 | 0.2000 | 0.0749 | 1.2500 | 0.00123 |
| 30 | 0.2500 | 0.2000 | 0.0968 | 1.1016 | 0.00167 |
| 40 | 0.2344 | 0.3500 | 0.0940 | 0.9844 | 0.00150 |
| 50 | **0.3544** | 0.1500 | 0.0938 | 1.9766 | 0.00157 |
| 60 | 0.2994 | 0.2000 | 0.0934 | 3.7500 | 0.00158 |
| 70 | 0.3075 | 0.1250 | 0.0862 | 1.1641 | 0.00156 |
| 80 | **0.3419** | 0.2500 | 0.0851 | 2.6719 | 0.00170 |
| 90 | 0.2419 | 0.3000 | 0.0772 | 1.2188 | 0.00151 |
| 100 | 0.3444 | 0.2000 | 0.0875 | 1.4141 | 0.00161 |

**关键发现：**

- **Peak reward: 0.3544 at step 50** (不是 step 80)
- **Step 50 reward: 0.3544** — Reviewer 说 0.264 是错的。0.354 就来自这里。
- **Step 80 reward: 0.3419** — Reviewer 说 0.342 是正确的。
- **Step 100: reward=0.3444, frac_zero_std=0.200, grad_norm=1.4141**
- **0.354 出现在哪？** 出现在 **step 50**（精确值 0.354375）

**结论：** Director 之前报的 0.354 是真实的，就是 step 50 的 reward。Reviewer 说 step 50=0.264 是错误的（可能看的是另一个 run 或另一个 metric）。真实 peak 在 step 50 而非 step 80。

---
