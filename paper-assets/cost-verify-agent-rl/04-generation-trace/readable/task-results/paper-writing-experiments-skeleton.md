# paper writing experiments skeleton

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_skeleton_20260517T092338_result.json`
- **Structured JSON:** [`1f493e276a870ff65468.json`](../../sessions/1f/1f493e276a870ff65468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`experiments.tex` 已写入。结构概览：

- **§5.1 Experimental Setup** (~600 words): ALFWorld 环境、Qwen3-1.7B 基座、GRPO 训练配置（所有超参数）、32-episode 评估协议。全部为确定数据，无 placeholder。
- **§5.2 Window-Size Ablation** (~400 words): $h \in \{2,5,10,20,\text{full}\}$ 设计、理论预测（双机制分离）、post-hoc full-context evaluation 设计。含 `plan_002` 多 seed 状态 placeholder。
- **§5.3 Results** (~800 words): 叙事骨架完整，已填入确定数字（exp029 28.125%、exp028c 两阶段崩溃、exp013f dense reward）。待填 placeholder：`tab1_main_results`、`fig6_training_curves`、`tab2_h_sweep`、`fig5_h_sweep_curve`。
- **§5.4 Sign Misattribution Verification** (~400 words): 方法论完整（per-window advantage logging、三个统计量）、理论预测值已写入。待填 `tab3_mechanism_verification`。
- **§5.5 Additional Baselines** (~200 words): GAE 两配置设计说明、selective verification placeholder。

共 6 个 `\placeholder{}` 标记，对应待完成的多 seed 实验和 per-window logging 数据。已通过 dash/ing-phrase 检查，无 AI 风格违规。

---
