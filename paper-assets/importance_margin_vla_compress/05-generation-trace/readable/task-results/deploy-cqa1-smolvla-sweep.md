# deploy cqa1 smolvla sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-smolvla-sweep_20260521T191518_result.json`
- **Structured JSON:** [`716906bf135161d0a4c9.json`](../../sessions/71/716906bf135161d0a4c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

**第一批 4 个实验（已启动，4 GPU 并行）：**

| 实验 | GPU | tmux 会话 | 状态 |
|------|-----|-----------|------|
| random_k030_object_seed42 | 0 | random_k030 | 运行中，加载完成 |
| random_k070_object_seed42 | 1 | random_k070 | 运行中，已产出首个 episode (FAIL) |
| l2norm_k030_object_seed42 | 2 | l2norm_k030 | 运行中，加载完成 |
| l2norm_k070_object_seed42 | 3 | l2norm_k070 | 运行中，加载完成 |

**修复问题：** 首次启动因缺少 `HF_HOME=/root/autodl-tmp/.hf_cache` 导致找不到 SmolVLM2 基础模型缓存，已加上并重启成功。

**第二批 2 个实验（random_k090, random_k050）：** 等第一批空出 GPU 后自动部署，已设 cron 每小时 :37 监控。

**预计时长：** 每个实验 ~4-5 小时，第一批预计 ~07:30 完成。

---
