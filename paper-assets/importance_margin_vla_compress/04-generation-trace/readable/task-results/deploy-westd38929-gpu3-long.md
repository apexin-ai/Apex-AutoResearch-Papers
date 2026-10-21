# deploy westd38929 gpu3 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu3_long_20260526T091855_result.json`
- **Structured JSON:** [`2f7e56ddadb90f7abd50.json`](../../sessions/2f/2f7e56ddadb90f7abd50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU3 残留进程报告**：

- **PID**: 288325
- **命令**: `python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.85 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object`
- **显存占用**: 15961 MiB
- **描述**: 这是一个 OpenVLA attention_prune k=0.85 libero_object 的评估实验

GPU3 正在跑 attention_prune 实验，无法直接部署新实验。请确认：
1. 这个实验是否已完成/可以终止？需要我杀掉它再部署新实验吗？
2. 还是等它跑完再部署？

---
