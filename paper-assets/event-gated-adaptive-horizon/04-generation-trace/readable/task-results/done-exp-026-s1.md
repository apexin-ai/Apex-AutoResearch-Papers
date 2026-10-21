# done exp 026 s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_done_exp_026_s1_20260520T013627_result.json`
- **Structured JSON:** [`204146ccc5fbaecb74a1.json`](../../sessions/20/204146ccc5fbaecb74a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**exp_026_obs_sgs_cheetah_s1** — DONE / negative

- **Final**: 105K steps, eval_return=38.26, value_mean=37.84, ve_ratio=0.989
- **Peak collapse**: ve_ratio=**11.81 @ 75K**（s0 峰值 8.56 @ 65K，s1 更严重）
- **Collapse window**: 45K–95K，eval_return 从 271.9 (35K) 崩至 3.65 (75K)
- 105K 时 ve_ratio 回落至 ~1.0，但 eval_return (38.3) 仍低于 35K 峰值 86%

s0/s1 一致确认：Cheetah 上 obs-decoder SGS 加剧而非抑制 CIVO。Cron 已删除，registry 已更新。

---
