# analyze repo level cls 8b s42 resume

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_repo-level-cls-8b-s42-resume_20260515T184049_result.json`
- **Structured JSON:** [`87f610910bd3ca71bcb8.json`](../../sessions/87/87f610910bd3ca71bcb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## CLS 8B s42 Resume 训练结果

### 状态: **SUCCESS**
- EXIT_CODE=0
- 最终 step: **6633/6633**, epoch: **3.0**
- 训练耗时: 74425s (~20h 40m)
- 最终 train_loss: **0.4284**

### eval_loss 完整趋势（每 200 步）

| Step | Epoch | eval_loss | 备注 |
|------|-------|-----------|------|
| 200 | 0.09 | **0.0796** | **BEST** |
| 400 | 0.18 | 0.0927 | |
| 600 | 0.27 | 0.0937 | resume 起点 |
| 800 | 0.36 | 0.1717 | |
| 1000 | 0.45 | 0.1820 | |
| 1200 | 0.54 | 0.2046 | |
| 1400 | 0.63 | 0.3226 | |
| 1600 | 0.72 | 0.2758 | |
| 1800 | 0.81 | 0.2764 | |
| 2000 | 0.90 | 0.3210 | |
| 2200 | 1.00 | 0.3063 | epoch 1 结束 |
| 2400 | 1.09 | 0.3444 | |
| 2600 | 1.18 | 0.2576 | |
| 2800 | 1.27 | 0.2744 | |
| 3000 | 1.36 | 0.2975 | |
| 3200 | 1.45 | 0.2981 | |
| 3400 | 1.54 | 0.4132 | |
| 3600 | 1.63 | 0.2612 | |
| 3800 | 1.72 | 0.3429 | |
| 4000 | 1.81 | 0.3694 | |
| 4200 | 1.90 | 0.2516 | epoch 2 局部低点 |
| 4400 | 2.00 | 0.2811 | epoch 2 结束 |
| 4600 | 2.09 | 0.3713 | |
| 4800 | 2.18 | 0.3919 | |
| 5000 | 2.26 | 0.4417 | |
| 5200 | 2.35 | 0.4021 | |
| 5400 | 2.44 | 0.4070 | |
| 5600 | 2.53 | 0.4002 | |
| 5800 | 2.62 | **0.5263** | 最差点 |
| 6000 | 2.71 | 0.4230 | |
| 6200 | 2.80 | 0.4385 | |
| 6400 | 2.89 | 0.4769 | |
| 6600 | 2.99 | 0.4768 | |

### Checkpoint 列表
32 个目录，共 **5.4G**：
- `checkpoint-800` ~ `checkpoint-6600`（每 200 步，共 30 个）
- `checkpoint-6633`（最终）
- `best/`

checkpoint-6600 和 checkpoint-6633 均含 `adapter_model.safetensors`（~58MB），完整性 OK。

### best/ 目录
- 含 adapter_model.safetensors + tokenizer 文件，完整
- 路径: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/best/`

### 异常/警告

**严重过拟合。** eval_loss 从 step 200 的 0.0796 单调上升到最终的 0.4768（增长 ~6x）。整个 3 epoch 的训练没有任何一个 eval 点接近早期的 best。

**best_model_checkpoint 指向旧目录。** trainer_state.json 记录的 best_model_checkpoint 是 `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200`（原训练目录，不是 resume 目录）。best_metric=0.0796 对应 step 200，在 resume 起点（step 600）之前。需确认 `best/` 目录里保存的是否真的是 step 200 的权重——如果原目录的 checkpoint-200 已被清理，`load_best_model_at_end` 可能加载失败而 fallback 到最终模型。

---
