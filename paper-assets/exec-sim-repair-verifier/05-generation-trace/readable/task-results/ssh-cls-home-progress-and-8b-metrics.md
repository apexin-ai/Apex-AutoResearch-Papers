# ssh cls home progress and 8b metrics

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cls-home-progress-and-8b-metrics_20260512T190041_result.json`
- **Structured JSON:** [`f63c88cfe2c3c7637e4a.json`](../../sessions/f6/f63c88cfe2c3c7637e4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 registry 更新全部成功。下面是完整结果。

---

## Part 1: cls-home 训练进度

| 指标 | 值 |
|------|-----|
| 当前 step | **875 / 6633** (13.2%) |
| 训练速度 | ~6.4–7.2 s/step (均值 ~6.9 s/step) |
| 已运行 | ~1h44m (从 10:17 开始) |
| 剩余 step | 5758 |
| **预计剩余** | **~11.0 小时 (ETA ~23:00)** |
| GPU | RTX 5090, 99% 利用率, 19.5/32.6 GB VRAM, 76°C |
| 模型 | Qwen3-4B LoRA (0.29% trainable) |
| 数据 | train=70748, val=9335 (3.8%/20.2% truncated) |
| Checkpoints | 目录为空（尚未触发 save） |

**Loss**: 日志中没有显式 loss 打印（仅 tqdm 进度条），loss 数据需等 wandb 或 checkpoint save 后的 trainer_state.json。

---

## Part 2: 8B metrics 补全结果

### 已更新的实验

| exp_id | overall_acc | fail_f1 | pass_f1 | fail_prec | fail_recall | 数据来源 |
|--------|-------------|---------|---------|-----------|-------------|----------|
| **cls8b-eval-seed42** | 90.48 | 90.06 | 90.86 | 90.76 | 89.36 | seetacloud `eval_results/cls8b_seed42.json` |
| **cls8b-eval-seed123** | 89.37 | 89.19 | 89.54 | 87.54 | 90.9 | seetacloud `eval_results/cls8b_seed123_results.json` |
| **cls8b-seed123** | 89.4 | 89.2 | 89.5 | 87.5 | 90.9 | 已有数据，标准化 accuracy→overall_accuracy |
| **cwm8b-seed123** | 86.98 | 87.13 | 86.83 | 83.3 | 91.34 | seetacloud `eval_cwm8b_seed123.json`，补全 precision/recall |

### cwm8b-seed42

已存在于 registry，注册为 `model-size-scaling-cwm8b`（acc=87.67, fail_f1=87.77），metrics 完整，无需操作。

---

## Part 3: seed123 值不一致调查

ROADMAP 提到 CLS 8B seed123 有 3 个值：**89.52 / 89.40 / 89.37**。来源如下：

| 值 | 来源 | 说明 |
|----|------|------|
| **89.52** | home 服务器 `eval_seed123.json` | 可能是不同 checkpoint（非 best）或不同 eval 脚本版本的结果 |
| **89.40** | `cls8b-seed123` 训练 run 自带 eval | 训练时 eval，已四舍五入 |
| **89.37** | `cls8b-eval-seed123` 独立 eval (`eval_results/cls8b_seed123_results.json`) | 使用 `--save_predictions` 的正式 eval run |

**结论**：89.37 是从 `checkpoints_cls8b_seed123/best` 用独立 eval 脚本得到的权威值（cls8b-eval-seed123）。89.4 是训练时 eval 的四舍五入值。89.52 来源不明确（文件名无 "8b" 标记，可能是不同 checkpoint epoch 的 eval）。差异在 0.15pp 以内，不影响论文结论。

---
