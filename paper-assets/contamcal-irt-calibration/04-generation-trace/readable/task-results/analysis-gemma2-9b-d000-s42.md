# analysis gemma2 9b d000 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2_9b_d000_s42_20260518T205347_result.json`
- **Structured JSON:** [`9015897fa15bbd407e1d.json`](../../sessions/90/9015897fa15bbd407e1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型权重加载完成（464/464）。训练即将开始。

---

## Part 1: Gemma-2-9B d000 s42 分析结果

| Metric | Value |
|---|---|
| **status** | SUCCESS |
| **final_loss** | 1.159 |
| **avg_train_loss** | 1.257 |
| **total_steps** | 3125 |
| **epoch** | 1.0 |
| **final_token_accuracy** | 0.7284 |
| **avg_token_accuracy** | 0.7196 |
| **runtime** | ~2h 37min (9453s) |
| **adapter_size** | 206.2 MB |
| **lora_r / lora_alpha** | 16 / 32 ✓ |
| **total_flos** | 9.85e+17 |
| **errors/warnings** | 无（`torch_dtype` deprecated warning 无害） |

**Conclusion**: loss 正常收敛（5.65 → 1.16），token accuracy 从 0.30 升至 0.73，checkpoint 完整。Gemma-2-9B 训练兼容性确认。

## Part 2: Gemma-2-9B d005 提交状态

| Field | Value |
|---|---|
| **exp_id** | exp_001_sft_gemma2_9b_d005_s42 |
| **PID** | 62861 |
| **GPU** | cuda:1 (CUDA_VISIBLE_DEVICES=1 显式设置) |
| **tmux session** | gemma2_d005 |
| **server** | westd-29999 |
| **data** | sft_dosage_005.jsonl (50826 行) |
| **log** | /root/autodl-tmp/exp001/logs/gemma2_d005_s42.log |
| **status** | 模型权重加载完成，即将开始训练 |

## 注意事项
- **无独立 log 文件**：d000 训练没有产生 `/root/autodl-tmp/exp001/logs/gemma2_d000_s42.log`（logs 目录不存在），metrics 从 `checkpoint-3125/trainer_state.json` 提取。已为 d005 创建 logs 目录并通过 tee 输出日志。
- **W&B**：`list_wandb_runs` 工具报错（参数签名不匹配），未能检查 W&B run。如需 W&B 数据需排查工具问题。
- d005 预计运行 ~2.5h（与 d000 类似），基于 50826 samples / batch=16 ≈ 3177 steps。

---
