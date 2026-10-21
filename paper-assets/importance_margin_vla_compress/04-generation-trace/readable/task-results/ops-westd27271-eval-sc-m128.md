# ops westd27271 eval sc m128

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-eval-sc-m128_20260521T030106_result.json`
- **Structured JSON:** [`5077280f20113d622c5b.json`](../../sessions/50/5077280f20113d622c5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。汇报：

**Checkpoint**: `checkpoints/openvla_sc_m128_seed42/checkpoint.pt`（完整训练，20GB，6 keys: step/model_state_dict/optimizer_state_dict/scheduler_state_dict/config/info）

**PID**: 176320（实际 python 进程），父 bash PID 176314

**GPU 占用**: cuda:0 已占用 36288 MiB / 97887 MiB

**日志摘要**:
- 模型加载成功，`OpenVLASmartCompressWrapper loaded: M=128, compressor params=403308544`
- 有 missing/unexpected keys 警告（LoRA 格式 vs 标准格式的 key 名差异，属正常行为）
- Suite: libero_object, 10 tasks, 50 episodes, max 280 steps
- Task 0 已开始推理（`pick up the alphabet soup and place it in the basket`），首个 action 已成功输出

**注意**: cuda:1 上有 M32 训练在跑（PID 921279），两个互不干扰。

---
