# verify plan 004 v5 checkpoint

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_plan-004-v5-checkpoint_20260516T000926_result.json`
- **Structured JSON:** [`af7a24588799c7174479.json`](../../sessions/af/af7a24588799c7174479.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇报如下：

---

## 验证结果

### plan-004-v5 checkpoint 训练参数
- **gradient_accumulation_steps = 1** (train_config.json 和 training_args.bin 一致)
- learning_rate = 2e-05, seed = 42, batch_size = 4, epochs = 3
- 模型：Qwen3-1.7B, LoRA r=16/alpha=32
- `final_adapter/` 目录存在，含完整 adapter 文件

### corrected eval 评估的 checkpoint
- `plan004v5_corrected.json` 中 `adapter_path = "checkpoints/plan-004-v5/final_adapter"`
- 评估结果：balanced_acc = 0.753, accuracy = 0.6885
- 使用 `split_algo = "training_load_implicit_sft_data"`, thinking_off 模式

### 所有 plan-004 变体的 ga 值

| Checkpoint | ga | lr | seed |
|---|---|---|---|
| plan-004-implicit | **8** | 2e-05 | 42 |
| plan-004-v2 | **8** | 2e-05 | 42 |
| plan-004-v3 | **8** | 2e-05 | 42 |
| plan-004-v4 | **8** | 2e-05 | 42 |
| **plan-004-v5** | **1** | 2e-05 | 42 |

### 对照组（ablation-b / seed-robustness）

| Checkpoint | ga | seed |
|---|---|---|
| ablation-b-seed123 | 8 | 123 |
| ablation-b-seed456 | 8 | 456 |
| ablation-b-seed789 | 8 | 789 |
| seed-robustness-seed43~49 (7个) | 8 | 43-49 |

### 结论

plan-004-v5 确实使用 **ga=1** 训练，与 hypothesis 一致。它是所有 plan-004 变体中唯一使用 ga=1 的版本（v1~v4 均为 ga=8）。corrected eval 确实评估了正确的 checkpoint 路径（`plan-004-v5/final_adapter`）。ablation-b 和 seed-robustness 全部使用 ga=8。

balanced_acc 从 55.7% (ga=8 主 router) 跳到 75.3% (ga=1) 的差异**不是因为评估了错误的 checkpoint**，而是 ga=1 本身带来的训练差异。effective batch size 从 32 (4×8) 降到 4 (4×1)，更频繁的梯度更新可能是性能提升的原因。

---
