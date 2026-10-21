# train mlp adapter control

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_mlp_adapter_control_20260519T060656_result.json`
- **Structured JSON:** [`f1317d9d3d9de19bd587.json`](../../sessions/f1/f1317d9d3d9de19bd587.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

**完成总结：**
- Killed M=16 seed44 进程，释放 cuda:0
- 实现 `MLPCompressor`：3层 MLP (960→3840→960) + average pooling (128→32 tokens)，参数量 **22,138,560 (22.14M)**，匹配 VisionTokenCompressor M=32
- 修改 `SmartCompressWrapper` 支持 `compressor.type: mlp` 配置切换
- 创建 `configs/mlp_adapter_control.yaml`
- Dry-run 验证通过，正式训练已在 tmux session `mlp_adapter_control` 中运行，step=100 loss=0.584，~3.5 sps
- Registry 已更新为 RUNNING (`train_mlp_adapter_control`)

---
