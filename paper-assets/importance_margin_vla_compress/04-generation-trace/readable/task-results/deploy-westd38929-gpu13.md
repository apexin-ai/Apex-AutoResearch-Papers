# deploy westd38929 gpu13

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu13_20260526T044035_result.json`
- **Structured JSON:** [`a2ba6b05be9490f6060a.json`](../../sessions/a2/a2ba6b05be9490f6060a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载进行中（1/16 files）。等待完成后重新提交 GPU3 实验。

现在汇报当前状态：

**GPU1 — `eval_openvla_random_k085_object_seed42`**
- PID: 269122, 显存: 15961 MiB, GPU利用率: 72%
- 已正常运行

**GPU3 — `eval_openvla_random_k05_long_seed42`**
- 启动失败：`/root/autodl-tmp/openvla-7b-finetuned-libero-10` 在 westd-38929 上不存在
- 正在从 HuggingFace 下载模型（15GB, 16 files），PID 270186
- 下载完成后需要重新提交

等下载完成后我重新提交 GPU3 实验。要我继续轮询下载进度吗？

---
