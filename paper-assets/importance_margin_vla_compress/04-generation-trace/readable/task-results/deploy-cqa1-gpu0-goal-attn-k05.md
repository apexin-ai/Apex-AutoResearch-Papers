# deploy cqa1 gpu0 goal attn k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu0_goal_attn_k05_20260526T235227_result.json`
- **Structured JSON:** [`de45d737030aed25a7e4.json`](../../sessions/de/de45d737030aed25a7e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常启动，模型正在加载中。

**部署完成：**
- **PID**: 834185
- **服务器**: cqa1-33015 GPU 0
- **exp_id**: `eval_openvla_attn_k05_goal_seed42_v2`
- **状态**: 正常启动，模型加载中（`Loading OpenVLA from: /root/autodl-tmp/openvla-libero-goal`）
- **命令**: `eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_goal --num_episodes 50 --seed 42`

注：初始提交用了错误脚本（`eval_openvla_pruning_libero.py`），已 kill 后用正确脚本 `eval_openvla_l2norm_libero.py` 重新提交。GPU 1 的 Object Attn k=0.95 (PID 832015) 未受影响。

---
