# deploy westd 27271 e5 fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-27271-e5-fill_20260523T123550_result.json`
- **Structured JSON:** [`2984ed77d5f6ac4a3f17.json`](../../sessions/29/2984ed77d5f6ac4a3f17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，汇报如下：

**新部署:**
- **GPU 0**: E5 attn_rollout Long k=0.5, PID=991950 — 正常运行中（Ep 4/50, ~7s/ep）
- **GPU 1**: E5 attn_rollout Object k=0.7, PID=992022 — 正常运行中（Ep 7/50, ~4s/ep）

**OpenVLA 下载进度:**
- `openvla-7b-finetuned-libero-goal`: 缺 model-00001-of-00004.safetensors（~4.7GB），已有 3/4 文件（9.5GB）
- `openvla-7b-finetuned-libero-10`: 缺 model-00003-of-00004.safetensors（~4.7GB），已有 3/4 文件（9.5GB）

两个 OpenVLA 模型各差一个 shard 未下载，没有活跃下载进程。

---
