# analyze exp029 seed6 v3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp029_seed6_v3_20260521T130011_result.json`
- **Structured JSON:** [`10aa6e3cbd8453bb96bd.json`](../../sessions/10/10aa6e3cbd8453bb96bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**exp029_seed6_v3: SUCCESS**

核心结果：
- Val success: 9.4% → 21.9% → 28.1% → 28.1% (step 0/5/10/15)，单调上升后 step 10-15 持平
- Train reward 从 0.70 持续升到 8.91，无 collapse
- Response length 从 14910 缩短到 3329，agent 学会更高效行动
- KL 全程 < 0.008，训练稳定
- Checkpoint: `/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15/actor/`

与其他 seed 对比：Seed 6 (28.1%) 是三个已完成 seed 中 val 最低的（Seed 1: ~43%, Seed 3: ~40.6%），差距 12-15pp。但 hypothesis 成立——无 collapse、有 consistent learning。

建议下一步：对 global_step_15 跑 OOD eval，等 Seed 4/5 完成后汇总 5 seeds 方差。

---
