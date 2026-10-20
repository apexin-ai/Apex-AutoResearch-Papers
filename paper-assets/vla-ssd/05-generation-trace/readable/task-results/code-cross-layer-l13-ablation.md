# code cross layer L13 ablation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_layer_L13_ablation_20260518T133712_result.json`
- **Structured JSON:** [`eaae1a55b618492210ad.json`](../../sessions/ea/eaae1a55b618492210ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动并运行中：

- **脚本**: `/root/vla-ssd/scripts/action_trajectory_L13_ablation.py`
- **tmux session**: `cross_layer_L13_ablation`
- **Registry**: `cross_layer_L13_ablation` → RUNNING
- **配置**: L13 全 32 heads ablation (zero attn output), 5 tasks × 10 demos × 50 timesteps = 5000 forward passes
- **模型**: openvla-7b (base), 与 L1/L8 ablation 保持跨层可比性
- **速率**: ~6.6 pass/s, 预计 ETA ~12 分钟
- **日志**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.log`
- **结果**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.json`

注意：任务说用 finetuned 模型，但 finetuned 模型的 norm_stats 只有 `libero_goal` key（无 `bridge_orig`），会导致 `get_action_stats` 报错。为与 L1/L8 跨层对比一致，沿用了 base model + `bridge_orig`。

---
