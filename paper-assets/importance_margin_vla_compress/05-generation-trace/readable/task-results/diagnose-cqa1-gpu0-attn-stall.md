# diagnose cqa1 gpu0 attn stall

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_gpu0_attn_stall_20260525T150358_result.json`
- **Structured JSON:** [`ce1e4cd4232d05a955e4.json`](../../sessions/ce/ce1e4cd4232d05a955e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 GPU 状态清晰了。

## cqa1-33015 全部 GPU 状态汇报

| GPU | Util | VRAM | PID | 实验 | 运行时间 | 状态 |
|-----|------|------|-----|------|---------|------|
| **0** | 63% | 10.8/24.6 GB | 401165 | `attention k=0.9 seed42 libero_10` | 1h55m | **正常** — T4 ep20/50, 累计 SR=67.5% |
| **1** | 23% | 10.1/24.6 GB | 431242 | `random k=0.925 seed42 libero_10` | 1h08m | **正常** — T2 ep10/50, 累计 SR=44.0% |
| **2** | 19% | 10.5/24.6 GB | 374171 | `l2norm k=0.7 seed43 libero_10` | 2h35m | **正常** — T6 ep40/50, 累计 SR=73.3% |
| **3** | 15% | 10.0/24.6 GB | 313394 | `random k=0.3 seed43 libero_10` | 4h00m | **正常** — T8 ep20/50, 累计 SR=30.2% |

**结论：GPU 0 没有 stall。** 当前 util=63%，日志持续输出（最新 23:00），进度正常推进。Reviewer 观测到 0% util 可能是瞬时波动（episode 间隙、环境 reset 阶段 GPU 空闲）。

全部 4 个 GPU 均在正常运行评估实验，无需干预。

tmux sessions：
- `eval_pi05_l2norm_k07_long_seed43_v3` — GPU 2
- `eval_pi05_random_k03_long_seed43_v4` — GPU 3
- `eval_pi05_random_k095_object_seed42_v2` — 旧 session（May 24），可能已结束

---
