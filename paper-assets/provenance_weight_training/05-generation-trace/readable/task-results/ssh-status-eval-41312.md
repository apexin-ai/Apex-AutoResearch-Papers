# ssh status eval 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status_eval_41312_20260517T205236_result.json`
- **Structured JSON:** [`5f82d72a303b2ea542a6.json`](../../sessions/5f/5f82d72a303b2ea542a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：全部仍在运行，无实验完成。**

| 实验 | 进度 | 速率 | 预计剩余时间 |
|------|------|------|------------|
| qwen06b_uniform_seed42_v2 | 4000/6103 (65%) | 28.5 steps/min | **~74 min** |
| ess_only_seed456 | 2500/6103 (41%) | 8.1 steps/min | ~7.4 h |
| ess_only_seed123 | 2500/6103 (41%) | 8.1 steps/min | ~7.4 h |
| random_reweight_seed456 | 1000/6103 (16%) | 8.1 steps/min | ~10.5 h |

速率差异原因：qwen06b_uniform 没有 `--eval_data_path`（不做周期性 eval），其余 3 个每 500 步做一次 eval 拖慢了训练速率。

**qwen06b_uniform_seed42_v2 约 1.2 小时后完成，是最早可以跑 eval 的。** 其余 3 个今天下午才能完成。

需要我设置一个定时检查，等 qwen06b 完成后自动触发 eval 吗？还是等全部完成后统一跑？

---
