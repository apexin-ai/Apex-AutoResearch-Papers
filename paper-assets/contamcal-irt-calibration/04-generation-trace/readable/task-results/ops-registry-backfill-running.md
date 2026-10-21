# ops registry backfill running

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-backfill-running_20260515T182447_result.json`
- **Structured JSON:** [`319966528962f38be781.json`](../../sessions/31/319966528962f38be781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个实验均已存在于 registry 中，且状态都是 RUNNING：

| 实验 | Registry 状态 | PID | 存活 | 运行时间 |
|------|-------------|-----|------|---------|
| exp_001_sft_d025_3B_v3 | RUNNING | 589763 | ✓ (R) | 2h12m |
| exp_001_sft_3B_d100_s42_a32_v2 | RUNNING | 593740 | ✓ (S) | 1h54m |
| exp_001_sft_3B_d100_s123_a32_v2 | RUNNING | 594489 | ✓ (S) | 1h51m |
| exp_001_sft_3B_d000_v3 | RUNNING | 597174 | ✓ (S) | 1h33m |
| exp_001_eval_3B_d005_s123_aligned | RUNNING | 580693 | ✓ (S) | 3h19m |
| exp_004_sim_sweep_v7 | RUNNING | — (tmux) | — | — |

Registry 当前共 172 条实验，不是 39 条。6 个目标实验全部已有条目且状态为 RUNNING，无需补录，全部跳过。

---
