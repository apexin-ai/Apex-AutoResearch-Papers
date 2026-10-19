# ops save displacement analysis summary

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_save_displacement_analysis_summary_20260525T172259_result.json`
- **Structured JSON:** [`31b09e37c2488206cbd3.json`](../../sessions/31/31b09e37c2488206cbd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成：`/root/autodl-tmp/eval_results/displacement_analysis_30k_summary.txt`（52 行）。

关键结果：所有 4 个 30K checkpoint 的 Filtered CAR 均为 **0.0%**，Frozen 比例 **100%**——所有"safe"的 episode 都是 frozen（max_displacement < 0.001m）。即使把阈值降到 0.0005m，除 s2_l01_30k 有 1 个 episode 外，其余全部 frozen。Sensitivity analysis 在 0.0005~0.01 范围内结果几乎无变化。

---
