# ops urgent gpu check and recover

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_gpu_check_and_recover_20260517T080047_result.json`
- **Structured JSON:** [`e1ac1388b88f2ed1ecb6.json`](../../sessions/e1/e1ac1388b88f2ed1ecb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘 100% 满了。** 这是 GRPO 和 8B 训练崩溃的原因。两个 eval 还在跑，但写结果时可能也会失败。

## nvidia-smi 摘要
| GPU | 显存 | Util | 进程 |
|-----|------|------|------|
| cuda:0 | 11383/32607 MiB | 51% | PID 414837 (rsft_s44_dev_eval_preds) |
| cuda:1 | 5469/32607 MiB | 39% | PID 420018 (plan006_1_7b_rsft_eval) |
| cuda:2 | 0/32607 MiB | 0% | **空闲** |
| cuda:3 | 0/32607 MiB | 0% | **空闲** |

## 实验状态

### lead2_rsft_grpo_ced_r2
- **状态: 崩溃** (EXIT_CODE=1, 2026-05-17T07:07:17Z)
- **原因: `No space left on device`** — step 30/50 (60%) 保存 checkpoint 时磁盘满
- Checkpoints: checkpoint-10, checkpoint-20, checkpoint-30
- 最后 metrics (step 30):
  - reward: 1.023, ced_reward: 0.540, format_reward: 0.483
  - f1_reward: 0.0 (始终为 0)
  - loss: 0.248, kl: 0.000145
- reward 曲线: step 5→30, reward 从 0.96 → 1.02, ced_reward 从 0.51 → 0.54（缓慢上升）

### plan_006_qwen3_8b_rsft_train
- **状态: 崩溃** (EXIT_CODE=1, 2026-05-17T06:56:59Z)
- **原因: `RuntimeError: unexpected pos` (磁盘满导致 optimizer 保存失败)**
- 进度: step 1000/3393 (29%), epoch 0.88
- Checkpoints: checkpoint-750, 800, 850, 900, 950, 1000
- 最后 metrics:
  - loss: ~0.47, mean_token_accuracy: 0.872
  - lr: 1.49e-05

### plan_006_qwen3_1_7b_rsft_eval
- **状态: 运行中** (PID 420018, cuda:1)
- 进度: 183/247 batches (74%), 已运行 ~1h50m
- 预计剩余 ~48 min
- 输出目录尚为空

### rsft_s44_dev_eval_preds
- **状态: 运行中** (PID 414837, cuda:0)
- 进度: 239/247 batches (97%), 已运行 ~3h
- 预计剩余 ~4-5 min
- 输出目录尚为空

## 空闲 GPU
**cuda:2, cuda:3** 完全空闲

## 关键问题
**`/root/autodl-tmp` 磁盘 250G 已 100% 占满 (剩余 1.2M)**。两个正在运行的 eval 写结果时极大概率会失败。需要立即清理磁盘空间。

---
