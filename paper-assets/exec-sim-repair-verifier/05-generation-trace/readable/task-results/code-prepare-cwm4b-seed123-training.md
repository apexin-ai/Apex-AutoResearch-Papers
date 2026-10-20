# code prepare cwm4b seed123 training

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-cwm4b-seed123-training_20260515T233118_result.json`
- **Structured JSON:** [`5e0b2d9f5188897992cf.json`](../../sessions/5e/5e0b2d9f5188897992cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有完整的信息了。以下是发现和准备好的命令。

---

## 发现：seed123 已经训练并评估过

| | v12 (s42) | seed123 (已有) |
|---|---|---|
| 目录 | `checkpoints_repo_cwm_conda_v12` | `checkpoints_repo_cwm_seed123_conda` |
| 最终步数 | 700/6633 (中断) | 695/6633 (中断) |
| Best checkpoint | step 500, eval_loss=0.3066 | step 500, eval_loss=0.3163 |
| **Accuracy** | **58.04%** | **59.09%** |
| F1 macro | 51.67 | 43.43 |
| Unparseable | 5255 | 6574 |

两个运行配置完全相同（Qwen3-4B, LoRA r=16/alpha=32, lr=5e-5, epochs=3, batch=1, grad_accum=32），只是 seed 不同。两个都在 ~700 步时被中断（eval_loss 从 step 500 后开始上升，有过拟合迹象）。

**seed123 已有评估结果 59.09%**。但 f1_macro 和 unparseable rate 明显比 v12 差，可能需要重跑确认。

---

## 重新训练命令

如果要重新训练（全新 output_dir），以下是完整命令：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

cd /home/sonny/exec-sim-repair-verifier

CUDA_VISIBLE_DEVICES=&lt;GPU_ID> python3 train_repo_cwm.py \
  --seed 123 \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_4b_seed123/ \
  --run_name repo-cwm-4b-seed123 \
  --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
  --data_dir /home/sonny/exec-sim-repair-verifier/data/swebench_full \
  --max_seq_length 2048 \
  --batch_size 1 \
  --grad_accumulation 32 \
  --lr 5e-5 \
  --epochs 3 \
  --warmup_ratio 0.05 \
  --weight_decay 0.01 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --lora_dropout 0.05 \
  --save_steps 100 \
  --save_total_limit 5 \
  --dataloader_num_workers 4 \
  --wandb_project exec-sim-repair-verifier \
  --device cuda:0
```

将 `&lt;GPU_ID>` 替换为可用 GPU 编号（cuda:1 当前被占用，避开）。

---

## 估算

| 指标 | 值 |
|---|---|
| 总步数 | 6633 (3 epochs, 70748 train, grad_accum=32) |
| 训练速度 | ~8 s/step (单 5090) |
| Eval 次数 | ~66 次 (每 100 步) |
| Eval 耗时 | ~12 min/次 |
| **总训练时间** | **~14.7h (train) + ~13.2h (eval) ≈ 28h** |
| GPU 显存 | ~12-15 GB (4B + LoRA + gradient checkpointing) |

**注意**：v12 的 eval_loss 在 step 500 后已经上升（过拟合），实际上 best checkpoint 可能就在前 500-600 步。如果只需要 best checkpoint，~2 小时就够了。如果想确认完整 3 epoch 曲线，需要 ~28 小时。

---
