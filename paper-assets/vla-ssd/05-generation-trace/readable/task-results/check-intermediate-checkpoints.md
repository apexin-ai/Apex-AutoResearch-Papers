# check intermediate checkpoints

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_intermediate_checkpoints_20260523T234750_result.json`
- **Structured JSON:** [`fb866800f235c89202da.json`](../../sessions/fb/fb866800f235c89202da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**服务器上所有模型均只有最终 checkpoint，没有任何中间 checkpoint。**

| 模型 | 路径 | 大小 | 中间 checkpoint |
|------|------|------|----------------|
| **TracVLA** | `tracevla-phi3v/` | 7.8G | 无 — 仅最终权重（2 个 .bin） |
| **NORA-goal** | `nora-libero-goal/` | 7.1G | 无 — 仅最终权重（2 个 .safetensors） |
| **NORA-spatial** | `nora-libero-spatial/` | 7.1G | 无 — 同上 |
| **OpenVLA-goal** | `openvla-7b-finetuned-libero-goal/` | 14G | 无 — 仅最终权重（4 个 .safetensors） |
| **OpenVLA-object** | `openvla-7b-finetuned-libero-object/` | 15G | 无 — 同上 |
| **OpenVLA-spatial** | `openvla-7b-finetuned-libero-spatial/` | 15G | 无 — 同上 |
| **OpenVLA-OFT** | `openvla-7b-oft-finetuned-libero-10/` | 15G | 无 — 有 `action_head--150000_checkpoint.pt` 和 `proprio_projector--150000_checkpoint.pt`，但这是 OFT 的 head 权重，不是 backbone 中间 checkpoint |

补充确认：
- 全盘搜索 `checkpoint-*`、`epoch_*`、`step_*`、`global_step*` 命名目录：**零结果**
- 无 `trainer_state.json`、`training_args.bin`、`optimizer.pt` 等训练中间产物
- 这些 checkpoint 全部从 HuggingFace Hub 下载的预训练/微调最终权重，不是本地训练产出

**无法在现有 checkpoint 上做 training dynamics 分析。** 需要重新训练并配置 `save_steps` 保存中间 checkpoint。

---
