# infra verify 50k checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-50k-checkpoints_20260521T152543_result.json`
- **Structured JSON:** [`84758824b6ec0e0e205e.json`](../../sessions/84/84758824b6ec0e0e205e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 判定结果

### occ_s0 50K: **COMPLETE**
### occ_s2 50K: **COMPLETE**

两个 50K checkpoint 结构完全一致，采用了 **symlink 节省空间策略**：基础模型权重（safetensors）符号链接到 47500 checkpoint，可训练组件为独立文件。

---

### 文件大小对比

**可训练组件（50K 独立文件）vs 47500 参考：**

| 文件 | occ_s0 50K | occ_s0 47500 | occ_s2 50K | occ_s2 47500 |
|------|-----------|-------------|-----------|-------------|
| action_head .pt | 302,243,095 | 302,243,095 | 302,243,095 | 302,243,095 |
| occ_head .pt | 2,434,741 | 2,434,741 | 2,434,741 | 2,434,741 |
| proprio_projector .pt | 67,275,701 | 67,275,701 | 67,275,701 | 67,275,701 |
| lora_adapter/adapter_model.safetensors | 484,458,600 | 484,458,600 | 484,458,600 | 484,458,600 |

文件大小完全一致——这是预期行为，因为模型架构不变，safetensors/pt 格式的文件大小由 tensor shape 和 dtype 决定，与权重值无关。

**基础模型（50K 通过 symlink 引用 47500 的实际文件）：**

| 文件 | 47500 实际大小 |
|------|--------------|
| model-00001-of-00004.safetensors | 4,925,122,448 (~4.59GB) |
| model-00002-of-00004.safetensors | 4,947,392,496 (~4.61GB) |
| model-00003-of-00004.safetensors | 4,947,417,456 (~4.61GB) |
| model-00004-of-00004.safetensors | 262,668,432 (~250MB) |

**注意事项：** 50K checkpoint 依赖 47500 checkpoint 的 symlink 目标。如果 47500 被删除，50K 将不可用。目前 47500 完好。

### 结构说明

50K checkpoint 没有独立的 `action_head/` 或 `occ_head/` 目录，而是用 `action_head--50000_checkpoint.pt` 和 `occ_head--50000_checkpoint.pt` 等独立 .pt 文件保存，与 47500 格式一致。`lora_adapter/` 目录包含完整的 adapter（README.md + adapter_config.json + adapter_model.safetensors）。不存在文件截断或缺失的迹象。

---
