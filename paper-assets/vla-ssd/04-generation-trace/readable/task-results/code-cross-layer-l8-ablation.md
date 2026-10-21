# code cross layer L8 ablation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_layer_L8_ablation_20260518T133705_result.json`
- **Structured JSON:** [`951753cf6ed22e268c9a.json`](../../sessions/95/951753cf6ed22e268c9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并正在运行：

- **脚本**: `/root/vla-ssd/scripts/action_trajectory_L8_ablation.py`
- **PID**: 53738
- **exp_id**: `cross_layer_L8_ablation` (RUNNING)
- **配置**: L8 全层 ablation (32 heads), 5 tasks × 10 demos × 50 timesteps
- **ablation 方式**: monkey-patch `LlamaAttention.forward`, 正常计算 attention + KV cache，但将 `attn_output` 置零后再过 `o_proj`，使该层 attention 贡献为零
- **输出**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.json`
- **日志**: `/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log`

---
