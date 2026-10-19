# analyze eval stepwise s0 l1 26k

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_stepwise_s0_l1_26k_20260527T050312_result.json`
- **Structured JSON:** [`9c4c77027cae62849adf.json`](../../sessions/9c/9c4c77027cae62849adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 已清除。

**结果汇总：**

- **eval_stepwise_s0_l1_26k** → **failed**
- **原因**：26K checkpoint 的 `model.safetensors` 使用了 AdaLN 架构（`layernorm.dense.weight/bias`, `time_mlp_in/out`），但 eval 以 `--model_type lora_baseline` 加载，期望标准 LayerNorm keys（`layernorm.weight`, `action_time_mlp_in/out`）。模型加载阶段直接崩溃，无任何 eval 结果。
- **根因**：24K→26K 之间训练代码发生了架构变更（可能 git pull 了新代码），导致 26K checkpoint 的权重格式与 24K 不兼容。

**需要决定下一步：**
1. 如果要重跑 26K eval，需要用匹配 AdaLN 架构的 model_type 或更新 eval 脚本来适配新格式
2. 或者确认 26K checkpoint 是否为有效 checkpoint（训练代码变更后保存的权重可能本身就有问题）

---
