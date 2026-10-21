# check home lora checkpoints

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-lora-checkpoints_20260518T001150_result.json`
- **Structured JSON:** [`b94894ef8999a1db3399.json`](../../sessions/b9/b94894ef8999a1db3399.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。汇总如下：

---

## home-1x5090 LoRA Checkpoints 汇总

所有 3 个 checkpoint 配置完全相同，来自同一次训练 run（CWM/CAUSAL_LM，3 epoch，max_steps=1434）。

| # | 路径 | 大小 | 完整性 |
|---|------|------|--------|
| 1 | `checkpoints/best/` | 61M | ✅ `adapter_model.safetensors` 有，**无** `trainer_state.json`（仅推理用导出） |
| 2 | `checkpoints/checkpoint-956/` | 151M | ✅ 完整（含 optimizer/scheduler/trainer_state） |
| 3 | `checkpoints/checkpoint-1434/` | 151M | ✅ 完整（含 optimizer/scheduler/trainer_state） |

### 共同配置

| 项目 | 值 |
|------|-----|
| Base model | `Qwen/Qwen3-4B` |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| Dropout | 0.05 |
| Target modules | `q_proj, k_proj, v_proj, o_proj` |
| Task type | `CAUSAL_LM` |
| PEFT version | 0.19.1 |

### 训练详情（from trainer_state）

- 任务类型：**CWM (Causal LM)**，从目录结构和 task_type 推断
- 训练 3 epochs，总 1434 steps，batch_size=2
- `best/` 对应 step 956（epoch 2），best eval_loss = **0.0797**
- `checkpoint-1434` 是最终 step（epoch 3 结束）

### 可用于 eval 的 checkpoint

| Checkpoint | 可直接 eval | 说明 |
|------------|-------------|------|
| `best/` | ✅ | 最佳验证 loss，推荐首选 |
| `checkpoint-956/` | ✅ | 等同 best 的 step，但含 optimizer 等额外文件 |
| `checkpoint-1434/` | ✅ | 训练结束（epoch 3），loss 可能略高于 best |

三个都可以跑 eval（都有 `adapter_model.safetensors` + `adapter_config.json`）。推荐用 `best/` 或 `checkpoint-1434`（前者验证最优，后者训练最充分）。

---
