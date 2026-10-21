# ops cleanup stale and monitor s47

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_stale_and_monitor_s47_20260528T223130_result.json`
- **Structured JSON:** [`cf85e44e9ce4c1d94bd6.json`](../../sessions/cf/cf85e44e9ce4c1d94bd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

w27 result JSON not found on any other server. Here's the full report:

---

## 1. s47 on cqa1-33015

**4 experiments running** across all 4 GPUs:

| Tmux Session | GPU | Python PID | Mode | Keep Ratio |
|---|---|---|---|---|
| `eval_pi05_l2norm_k07_long_seed47_w41` | 0 | **541097** | l2norm | 0.7 |
| `eval_pi05_attn_k07_long_seed47_cqa1` | 1 | **543413** | attention | 0.7 |
| `eval_pi05_attn_k075_long_seed47_cqa1` | 2 | **543553** | attention | 0.75 |
| `eval_pi05_l2norm_k05_long_seed47_cqa1` | 3 | **543727** | l2norm | 0.5 |

All started ~06:23-06:32 server time, all actively running (600%+ CPU each).

---

## 2. Stale s46 实验状态

All 4 were already auto-transitioned to DONE by on_complete hooks. I've set `checkpoint_path = "N/A (eval only)"` on all 4.

| Experiment | Server | SR | Status |
|---|---|---|---|
| `eval_pi05_random_k05_long_seed46_strict_w41` | w41 | **50.2%** | DONE(success) ✓ |
| `eval_pi05_random_k095_long_seed46_strict_w41` | w41 | **60.8%** | DONE(success) ✓ |
| `eval_pi05_attn_k095_long_seed46_strict_w38` | w38 | **75.2%** | DONE(success) ✓ |
| `eval_pi05_l2norm_k095_long_seed46_strict_w27` | w27 | **unknown** | DONE(success), but metrics missing |

**w27 问题**: westd-27271 连接失败 (`Unable to connect to port 27271`)，hook 触发时也无法读取 SR，result JSON 仅存于 w27 本地。可能需要去 AutoDL 控制台查新端口，或者等实例恢复后补录 metrics。

---
