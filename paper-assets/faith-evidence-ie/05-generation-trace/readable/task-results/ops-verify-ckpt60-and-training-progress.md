# ops verify ckpt60 and training progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_ckpt60_and_training_progress_20260514T222054_result.json`
- **Structured JSON:** [`ca068c7392cc8aa64927.json`](../../sessions/ca/ca068c7392cc8aa64927.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇报

### 进程状态
- **存活**，PID 90080，已运行 2h41m，GPU 0 占用 13636 MiB
- **当前 step: 86/200** (43%)，日志最后一行显示 step 86 正在处理

### Checkpoint 列表
| Checkpoint | 状态 |
|---|---|
| checkpoint-20 | ✓ 存在 |
| checkpoint-40 | ✓ 存在 |
| checkpoint-60 | ✓ 存在且完整 |
| checkpoint-80 | ✓ 存在 |

### checkpoint-60 完整性
完整，包含：
- `adapter_model.safetensors` (252MB)
- `adapter_config.json`
- `optimizer.pt` (504MB)
- `trainer_state.json` + tokenizer 文件齐全

### 训练指标（最近几步 ~step 78-80）
- reward: 0.24 → 0.28（缓慢上升）
- format_reward: ~0.22 → 0.25
- f1_reward: 极低 (~0.005-0.016)
- ced_reward: 极低 (~0.008-0.018)
- KL: 已从早期爆炸值（2.4×10⁹）降至正常范围（~0.01）
- 平均 step 时间: ~100-110s/step

### 预计完成时间
剩余 114 步 × ~105s/step ≈ 3h20m，预计 **UTC 2026-05-15 ~09:40**（北京时间 ~17:40）完成。

### 注意事项
- KL 在 step 5 和 step 30 出现过爆炸（2.4×10⁹ 和 7×10¹³），但仅告警未停止，后续已恢复正常
- f1_reward 和 ced_reward 仍然很低，模型在实际 IE 任务上的提升有限，format compliance 是主要得分来源

---
