# code ablation 50demos main

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_50demos_main_20260517T182747_result.json`
- **Structured JSON:** [`db2e2de0f09baf4200fd.json`](../../sessions/db/db2e2de0f09baf4200fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动，模型正在加载。

**总结：**
- 脚本 `/root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py` 已修改：
  - `demos_per_task` 默认值 5→50
  - 输出路径改为 `action_probe_50demos.json`
  - 添加 `bootstrap_paired_ci` 函数（10,000 resamples，paired by task，95% CI + two-sided p-value）
  - conditions 保持原来的 3 个（baseline/ablate_all24/ablate_all32），layers 保持 [1,8,13]
- 已在 cuda:0 上提交运行，tmux session: `l1_head_ablation_50demos`
- 日志：`~/runs/vla-ssd/l1_head_ablation_50demos.log`
- 预计运行 2-3 小时

---
