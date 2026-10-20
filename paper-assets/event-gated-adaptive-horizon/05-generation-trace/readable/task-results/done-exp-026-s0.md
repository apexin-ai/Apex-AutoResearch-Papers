# done exp 026 s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_done_exp_026_s0_20260520T013129_result.json`
- **Structured JSON:** [`e19b78584c67bc7fa437.json`](../../sessions/e1/e19b78584c67bc7fa437.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## exp_026_obs_sgs_cheetah_s0 最终结果

**状态**: DONE (negative) — 训练正常完成至 105K steps，CIVO collapse 确认。

### ve_ratio trajectory

| Step | value_mean | eval_return | ve_ratio |
|------|-----------|-------------|----------|
| 5K | 0.00 | 8.26 | 0.0001 |
| 15K | 1.56 | 64.05 | 0.0244 |
| 25K | 11.68 | 124.23 | 0.094 |
| 35K | 28.53 | 161.22 | 0.177 |
| 45K | 48.25 | 155.77 | 0.310 |
| 55K | 57.94 | 58.30 | 0.994 |
| **65K** | **51.10** | **5.97** | **8.561** |
| 75K | 51.91 | 42.59 | 1.219 |
| 85K | 53.29 | 54.96 | 0.970 |
| 95K | 51.14 | 34.42 | 1.486 |
| 105K | 51.16 | 38.76 | 1.320 |

**Peak ve_ratio**: 8.5607 @ 65K (full CIVO collapse, NVE=21.85×)
**Final**: ve_ratio=1.32, eval_return=38.8 (partial recovery but performance permanently degraded vs baseline ~160)

### Registry 更新 + cron 删除均已完成。

---
