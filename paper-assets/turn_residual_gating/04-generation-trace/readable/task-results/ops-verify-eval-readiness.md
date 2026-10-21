# ops verify eval readiness

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_eval_readiness_20260519T125453_result.json`
- **Structured JSON:** [`e0c91e1dae453ce452fb.json`](../../sessions/e0/e0c91e1dae453ce452fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 四路 Eval 准备状态汇报

### 1. Eval 脚本 (`run_4way_eval.sh`)
实际是 **8 条** eval（4 条件 × 2 GAR 变体 ours/dongre），参数正确。LoRA-only checkpoint 路径：
```
LO_CKPT=/root/turn_residual_gating/runs/phase2_lora_only_s42
```
脚本安全检查要求 **`$LO_CKPT/lora/`** 目录存在。

### 2. Checkpoint 完整性

| 条件 | lora adapter | gate_params.pt | 状态 |
|------|-------------|----------------|------|
| TG v7 | ✅ | ✅ | 就绪 |
| UG | ✅ | ✅ | 就绪 |
| Base | N/A | N/A | 无需 checkpoint |
| **LoRA-only** | ⚠️ | N/A | **未就绪** |

**LoRA-only 问题**：当前只有 `epoch_0/lora/` 和 `epoch_1/lora/`，**没有顶层 `lora/` 目录**。eval 脚本的 `[ -d "$LO_CKPT/lora" ]` 检查会失败。训练正在跑 epoch 2，需确认训练结束后是否会生成顶层 `lora/`。

### 3. Eval 数据
`ultrachat_eval_sample.json` — 446KB, 2737 行，✅ 存在。

### 4. PPL 功能
`compute_conversation_ppl` 出现 2 次，✅ 已包含。

### 5. 启动前需要做的事

唯一阻塞项：**LoRA-only 训练完成后，确认顶层 `runs/phase2_lora_only_s42/lora/` 是否自动生成。** 如果训练脚本只保存 `epoch_N/lora/`，则需要二选一：
- 创建 symlink：`ln -s epoch_2/lora runs/phase2_lora_only_s42/lora`（指向最终 epoch）
- 或修改 eval 脚本中 `LO_CKPT` 指向具体 epoch 目录（如 `phase2_lora_only_s42/epoch_2`）

其余全部就绪，无其他阻塞。

---
