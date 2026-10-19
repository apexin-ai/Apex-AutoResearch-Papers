# research wandb seed300 seed2 curves

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wandb_seed300_seed2_curves_20260523T000744_result.json`
- **Structured JSON:** [`c5d71fd4dcd4c15133f6.json`](../../sessions/c5/c5d71fd4dcd4c15133f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。

**seed300**:
- W&B run: `ozyniycy` (`exp029-seed300-episode-level`), crashed but有 4/5 步训练数据
- seed_value=300, category=healthy
- 4 步训练数据，success 从 0.14 → 0.20，KL 稳定 ~0.0003-0.001

**seed2**:
- W&B runs: `efab7i1h` (steps 1-15) + `9xs5vfbe` (steps 16-43，续训)
- seed_value=43, category=delayed_learner
- 43 步训练数据，典型 delayed learner 曲线：前 15 步 success 低 (0.03-0.37)，step 23 开始爬升，step 28 达到 0.89 峰值，之后高方差震荡 (KL 也从 ~0.005 飙升到 0.17)

`learning_curve_data.json` 已更新，新增 `delayed_learner_seeds` 分类数组。总计 9 个 seed。

---
