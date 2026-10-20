# ops e2 cka extended results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_e2_cka_extended_results_20260518T153548_result.json`
- **Structured JSON:** [`b7e17d98920cdf2395aa.json`](../../sessions/b7/b7e17d98920cdf2395aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态
**仍在运行** — step 112/300，尚未完成。

关键细节：

**速度**：tqdm 显示 72.67s/it 是误导的（resume 导致 EMA 偏移）。实际每步 ~115s（`step_time: 114.1`），因为每步包含 generation（4 completions × max 512 tokens）。188 步剩余 ≈ **~6 小时**，预计 ~05:30 May 19 完成。

**W&B 无数据**：服务器网络不通（`[Errno 101] Network is unreachable`），metrics 只在本地，无法 sync。

**唯一 log point — step 110**：

| Metric | Value |
|--------|-------|
| reward | 0.3206 |
| frac_reward_zero_std | 0.175 (17.5%) |
| loss | 0.0246 |
| kl | 0.001129 |
| entropy | 0.09788 |
| completions/clipped_ratio | 0.4 |

## 与 Standard Extended 初步对比

| | CKA-only (step 110) | Standard (step 110 区间) |
|--|--|--|
| reward | 0.3206 | ~0.10 (已在下降) |
| frac_zero_std | 17.5% | 高得多 |

CKA-only 在 step 110 的 reward (0.3206) 虽略低于 step 100 peak (0.354)，但仍在健康区间，远高于 Standard extended 同期。需要等到 step 150+ 才能判断趋势。

**Checkpoint**：尚无（save_steps=50，首个 checkpoint 在 step 150）。

## 建议
等 ~6 小时后再查。不更新 registry/不删 cron。

---
