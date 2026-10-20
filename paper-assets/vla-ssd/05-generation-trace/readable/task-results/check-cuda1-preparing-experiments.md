# check cuda1 preparing experiments

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda1_preparing_experiments_20260523T153732_result.json`
- **Structured JSON:** [`326efd92e2a6988ad256.json`](../../sessions/32/326efd92e2a6988ad256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### PREPARING 实验状态

| 实验 | 状态 | 说明 |
|------|------|------|
| tracvla_spatial_full_v2 / tracvla_spatial_trained | ✅ 已完成 | trained + untrained 各4个JSON齐全 |
| behavioral_smoketest_diag | ❌ 已取消 | — |
| libero_finetuned_probe | ✅ 已完成 | `libero_finetuned_probe_profile.json` 含32层完整结果 |
| fulllayer_action_probe | ❌ 已废弃 | notes 标注 superseded |

**Registry 中所有 PREPARING 实验要么已完成要么已取消，没有可直接启动的。**

### 发现的数据缺口

`nora_spatial/untrained/` **缺少 `counterfactual_combined.json`**（仅3个文件，其他所有目录均为4个）：
- ✅ action_r2_probing.json
- ✅ cross_instruction_classification.json
- ✅ l1_attention_profile.json
- ❌ counterfactual_combined.json ← **缺失**

已有 `nora_goal_untrained_counterfactual_only.py`（针对 goal），可改写为 spatial 版本立即跑。脚本默认 `DEVICE = "cuda:0"`，改为 `cuda:1` 即可。

### 建议

cuda:1 最快能启动的工作：**补跑 nora_spatial untrained counterfactual**。需要将 `nora_goal_untrained_counterfactual_only.py` 复制一份，改 DATA 路径为 `libero_spatial`、RESULTS_DIR 为 `nora_spatial/untrained`、DEVICE 为 `cuda:1`，以及更新 TASKS/INSTRUCTIONS 列表。GPU 当前空闲，可立即执行。

---
