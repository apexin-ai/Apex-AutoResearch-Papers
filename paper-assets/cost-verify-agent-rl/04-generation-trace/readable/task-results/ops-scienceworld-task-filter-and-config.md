# ops scienceworld task filter and config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scienceworld_task_filter_and_config_20260522T035342_result.json`
- **Structured JSON:** [`82419e18af5432f59b68.json`](../../sessions/82/82419e18af5432f59b68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verified. Summary of results:

---

### 1. 完整 30 任务 success rate
见上方表格。数据来源：`/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.json`（1796 episodes, 30.1% overall）

### 2. 筛选后 >10% 任务：21 个
排除 9 个：`boil`(0%), `chemistry-mix`(0%), `chemistry-mix-paint-tertiary-color`(0%), `freeze`(0%), `grow-fruit`(6.5%), `grow-plant`(0%), `identify-life-stages-1`(0%), `identify-life-stages-2`(0%), `power-component-renewable-vs-nonrenewable-energy`(0%)

### 3. envs.yaml 更新
新增 `ScienceWorldSG_filtered` tag，21 个任务，其余参数与 `ScienceWorldSG` 一致

### 4. v4 config 更新
- 训练（line 97）：`tags: ["ScienceWorldSG_filtered"]` — 只训练 21 个可学习任务
- 评估（line 103）：`tags: ["ScienceWorldSG"]` — 保持全量 30 任务评估
- `save_freq: 5` 已是目标值
- `val_before_train: True` 已确认

### 5. 训练/评估分开任务集：支持
`es_manager.train` 和 `es_manager.val` 是独立配置块，可以使用不同 tags。

---
