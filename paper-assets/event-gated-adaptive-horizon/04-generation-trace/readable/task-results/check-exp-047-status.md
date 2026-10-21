# check exp 047 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_047_status_20260522T183414_result.json`
- **Structured JSON:** [`5518a1fd6a232a1466d4.json`](../../sessions/55/5518a1fd6a232a1466d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_047_frozen_dt_emb_walker_s1 状态汇报：**

| 项目 | 状态 |
|------|------|
| PID 282452 | **存活**，已运行 7h31m42s |
| 当前 step | **216000 / 210000** — 已超过目标步数，仍在运行 |
| GPU | cuda:0, 3025 MiB |
| 最新 checkpoint | `checkpoint_175000.pt`（有 25k/75k/125k/175k，缺 200k） |
| train_return (step 216k) | 最近 4 episode: 154.8, 40.5, 185.2, 146.5 |
| gate_dt | 固定 dt=2（dt_emb_freeze=True，gate_dt_2_frac=1.0，符合预期） |
| FPS | ~8.2 |

注意：步数已超过 `--steps 210000`，进程仍在跑，可能是在完成最后的 eval 或 checkpoint 保存。缺少 checkpoint_200000.pt（checkpoint_every=25000 应该在 200k 存一次）。

---
