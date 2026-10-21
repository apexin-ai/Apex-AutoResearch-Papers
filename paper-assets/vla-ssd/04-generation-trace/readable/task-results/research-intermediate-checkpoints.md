# research intermediate checkpoints

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_intermediate_checkpoints_20260520T150440_result.json`
- **Structured JSON:** [`7e715f3667947c72768c.json`](../../sessions/7e/7e715f3667947c72768c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Checkpoint 清单

| 目录 | 类型 | 大小 | Intermediate checkpoints |
|------|------|------|--------------------------|
| `openvla-7b/` | pretrained base (HF 下载) | 15G | 无 — 仅 final weights |
| `openvla-7b-llama2base/` | 自制 Llama2 base 变体 | 15G | 无 — 仅 final weights |
| `openvla-7b-finetuned-libero-goal/` | 官方 LoRA fine-tuned (HF 下载) | 14G | 无 — 仅 final weights |
| `openvla-phi3v/` | 仅 README + LICENSE，无模型文件 | ~0 | 无 |
| `tracevla-phi3v/` | TracVLA-Phi3V (HF 下载) | 7.8G | 无 — 仅 final weights (2 个 .bin 文件) |
| `dinov2-large/` | DINOv2 vision encoder | — | N/A |

### 关键结论

**没有任何 intermediate checkpoints。** 所有模型目录都只包含 final checkpoint（完整训练结束后的单一快照）。

- 没有 `checkpoint-XXXX/`、`step-XXXX/`、`epoch-X/` 子目录
- 没有 `trainer_state.json`（HuggingFace Trainer 保存中间 checkpoint 时会生成）
- 训练脚本中没有 `save_steps`、`save_strategy`、`save_total_limit` 配置
- `openvla-7b-finetuned-libero-goal` 的 README 显示训练了 60K gradient steps（8×A100），但官方只发布了 final checkpoint
- HF cache 中也没有其他 openvla 版本

### 对 routing emergence dynamics 分析的影响

**不可行。** 分析 L1 instruction-dominant heads 在训练过程中何时出现，需要至少 5-10 个均匀分布的中间 checkpoint。当前只有训练前（pretrained）和训练后（fine-tuned）两个点，只能做 before/after 对比，无法追踪 emergence trajectory。

要获取 intermediate checkpoints，需要自行 fine-tune 并配置 `save_steps`（例如每 5K steps 保存一次，60K steps 训练可产生 12 个中间点）。

---
