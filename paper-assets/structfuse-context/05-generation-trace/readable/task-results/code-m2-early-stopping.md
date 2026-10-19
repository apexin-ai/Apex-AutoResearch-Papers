# code m2 early stopping

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m2_early_stopping_20260514T081434_result.json`
- **Structured JSON:** [`60659523260be7f0d15c.json`](../../sessions/60/60659523260be7f0d15c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**注意**：当前正在运行的 launcher 脚本（bash for 循环）已经把整个循环体读入内存，所以修改 `.sh` 文件不会影响本次执行中尚未启动的 s43/s44。如果需要让 s43 起来就带 early stopping，需要 **kill 当前脚本进程，等 random_s42 跑完后重新启动脚本**。

---

### 修改汇总

**方案**：方案 A（训练循环内判断），代码已预先存在，本次补充 `best_val_loss_step` 追踪 + 改善日志。

**修改的文件（3 个）**：

| 文件 | 修改 |
|---|---|
| `/root/structfuse-context/training/train.py` | L362: 加 `best_val_loss_step = 0`；L442: 加 `best_val_loss_step = global_step`；L463: 日志改为 `Early stopping triggered at step {step}, best val_loss={best} at step {best_step}` |
| `/root/structfuse-context/run_m2_full_qwen.sh` | L78: 加 `--early-stopping-patience 2` |
| `/root/structfuse-context/run_m2_full_starcoder.sh` | L184: 加 `--early-stopping-patience 2` |

**s43 启动时的完整命令（以 Qwen random_s43 为例）**：
```bash
python /root/structfuse-context/training/train.py \
    --model-name /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B \
    --train-file /root/autodl-tmp/structfuse/full_m2_training_data/train_random_s43.jsonl \
    --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl \
    --output-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43 \
    --hard-negative-strategy random \
    --learning-rate 2e-5 --temperature 0.07 --batch-size 8 --num-epochs 2 \
    --num-negatives 7 --hard-negative-ratio 0.5 --use-lora --gradient-checkpointing \
    --max-seq-length 2048 --seed 43 --eval-steps 500 --save-steps 1000 \
    --wandb-project structfuse --wandb-run-name m2_full_random_s43 \
    --early-stopping-patience 2
```

**dry-run 验证**：`python train.py --help` 正常显示 `--early-stopping-patience` 参数。

---
