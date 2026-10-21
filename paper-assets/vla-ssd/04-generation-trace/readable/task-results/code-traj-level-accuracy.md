# code traj level accuracy

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_traj-level-accuracy_20260515T170104_result.json`
- **Structured JSON:** [`972ce7b03a077a7815f2.json`](../../sessions/97/972ce7b03a077a7815f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本语法验证通过。

修改汇总：

**`train_probes.py`** (6处):
1. `train_goal_classification_probe()` 返回值增加 `val_preds`
2. `run_goal_classification()` 的 `flatten()` 增加 `return_traj_ids` 参数，val set 额外返回每个样本的 trajectory index
3. 训练后对 val predictions 按 trajectory 分组，`np.bincount` 取多数投票，计算 `traj_accuracy`
4. 打印增加 `traj_acc` 字段
5. CSV summary 字段增加 `traj_accuracy`
6. JSON summary 增加 `best_traj_accuracy`（所有层最大值）和 `traj_accuracy_by_layer`

**`analyze_goal_probes.py`** (3处):
1. 新增 `get_traj_acc()` helper
2. Per-layer 表格每个模型增加 `_traj` 列
3. Best summary 和 Gate judgment 增加 traj_accuracy 展示

---
