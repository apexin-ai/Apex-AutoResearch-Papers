# paper experiments results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments_results_20260517T232143_result.json`
- **Structured JSON:** [`714e5142d2f40ad2c521.json`](../../sessions/71/714e5142d2f40ad2c521.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The two remaining em-dashes (lines 31 and 68) are in the existing Setup sections, not in the new Results content. The new Results and Ablation sections (lines 70-154) are clean.

修改完成。改动概要：

**4 个文件已更新：**

- **experiments.tex** (lines 70-154): 替换所有 `[TBD]` 段落，写入 4 个完整结果段落 + α ablation 分析
  - **Reward-accuracy decoupling**: Unpruned 81.27%→81.27% (1072/1319 identical), Δ≤0 for all configs, bidirectional (step-10 eval 61.87% confirms collapse ≠ accuracy loss)
  - **Collapse dynamics**: RASP step 10 permanent (frac_zero_std=0.95, grad=0.007), Standard step 60 transient, Unpruned none; 6x acceleration = zero-cost diagnostic
  - **Redundancy-stability tradeoff**: SFT +2.2pp for RASP (p=0.25) vs GRPO 6x faster collapse; ties to RL Squeezes, SFT Expands
  - **α ablation**: post-prune monotonic (17.5%→40%), post-SFT non-monotonic (α=0: 64%, α=1: 57%, α=4: 62%); post-prune ≠ recovery quality
- **table2_recovery.tex**: 新 6 列表 (SFT/GRPO/Δ/Reward/Collapse)，含 Unpruned baseline，N=1319
- **table1_postprune.tex**: 移除 GRASPrune 和 25% TBD 行
- **table3_alpha.tex**: 填入实际数据，α=0.5 和 α=2.0 post-SFT 待补 (`--`)

**注意**: Table 3 有 2 个 post-SFT 值缺失 (α=0.5, α=2.0)，提交前需补齐。

---
