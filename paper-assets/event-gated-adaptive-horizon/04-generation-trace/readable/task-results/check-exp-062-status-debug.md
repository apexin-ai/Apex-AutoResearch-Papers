# check exp 062 status debug

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_062_status_debug_20260525T034402_result.json`
- **Structured JSON:** [`96672421c28d6dad9bc5.json`](../../sessions/96/96672421c28d6dad9bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_062_cartpole_control 排查结果

**状态：已完成 (DONE)** — 3 seeds 全部跑满 112K steps，进程正常退出 (EXIT_CODE=0)。reconcile 未捕获是因为 tmux session 已自然结束。

**结果（符合预期 — negative）：**

| Seed | eval_return | ve_ratio_peak | civo_detected |
|------|-------------|---------------|---------------|
| s0 | 230.4 | 0.069 | False |
| s1 | 255.3 | 0.079 | False |
| s2 | 248.8 | 0.065 | False |
| **mean** | **244.8** | **0.071** | **None** |

**结论：** dt_embed_dim=0 在 Cartpole Swingup 上未触发 CIVO（ve_ratio_peak 均 < 0.08，远低于 1.5x 阈值）。与 exp_061（有 dt_emb）形成因果对比，确认 dt embedding 是 CIVO 触发的必要条件。

Registry 已更新为 status=DONE, conclusion=negative。

---
