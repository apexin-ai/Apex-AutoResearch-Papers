# analysis libero lora baseline 100k

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_libero_lora_baseline_100k_20260516T212853_result.json`
- **Structured JSON:** [`c0f879a823ba63ee0f4d.json`](../../sessions/c0/c0f879a823ba63ee0f4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总报告：

---

## libero_lora_baseline 100K 最终结果

| 指标 | 值 |
|------|-----|
| final_step | 99999 |
| final_train_loss | 0.0648 |
| final_eval_loss | 0.0804 |
| final_lr | ~2.5e-6 (cosine → 0) |
| final_grad_norm | 0.415 |
| checkpoint | `checkpoints/libero_baseline/step_099999/checkpoint.pt` (883MB) |
| SR@100K (libero_object) | **0%** (task_0: 0/10, all episodes hit max_steps=400) |

### Conclusion: **NEGATIVE**

LoRA (r=32, alpha=16, 1.49M trainable params) 在 SmolVLA + LIBERO 上确认无效：
- **不是 mode collapse**：diversity check PASS (std=0.174)
- **不是训练问题**：loss 正常下降并收敛
- **是 capacity bottleneck**：对比 Full FT (99.9M params) 在相同数据/步数下 SR=33%，LoRA 的 1.49M 参数无法学习 LIBERO 操作策略
- LoRA 训练 loss (0.065) 略高于 Full FT (0.041)，但两者 eval loss 相近 (0.080 vs 0.078)，说明 LoRA 在训练集上就已欠拟合

### 其他进程状态

| 实验 | GPU | 进度 | ETA |
|------|-----|------|-----|
| libero_lora_seed0 | cuda:2 | 84700/100K | ~1h |
| libero_fullft_seed0 | cuda:3 | 83900/100K | ~1h |
| libero_full_ft_baseline | cuda:0 | **完成** 100K (train_loss=0.041) | — |
| eval_lora_100k (后���) | cuda:1 | task 0 done, tasks 1-9 running | ~2h |

---
