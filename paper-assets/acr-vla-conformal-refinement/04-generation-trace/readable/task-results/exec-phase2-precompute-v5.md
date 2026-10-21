# exec phase2 precompute v5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_phase2-precompute-v5_20260514T075529_result.json`
- **Structured JSON:** [`694de898be12ad8b405f.json`](../../sessions/69/694de898be12ad8b405f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个 shard 已成功启动，模型加载完毕，正在处理数据。

| Shard | exp_id | PID | GPU | 状态 |
|-------|--------|-----|-----|------|
| 0 | `precompute-v5-shard0` | 180251 | cuda:0 | 已加载 spatial，4056 samples |
| 1 | `precompute-v5-shard1` | 180400 | cuda:1 | 已加载 spatial，4056 samples |
| 2 | `precompute-v5-shard2` | 180480 | cuda:3 | 已加载 spatial，加载中 |

日志路径: `~/runs/acr-vla-conformal-refinement/precompute-v5-shard{0,1,2}.log`
缓存输出: `/root/autodl-tmp/crm_cache_v5/`
GPU 2 (reconvla eval) 未受影响。

---
