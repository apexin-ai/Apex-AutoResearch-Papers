# ssh s43 launch readiness

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_s43_launch_readiness_20260514T053516_result.json`
- **Structured JSON:** [`35ede77b6901956e5ebc.json`](../../sessions/35/35ede77b6901956e5ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已确认。结果如下：

### s42 完成后是否自动启动 s43？
**是。** 两个脚本都用嵌套 for 循环自动遍历，无需手动触发。

### 遍历顺序（两个脚本一致）
外层=strategy，内层=seed：
1. `random_s42` → `random_s43` → `random_s44`
2. `embedding_distance_s42` → `embedding_distance_s43` → `embedding_distance_s44`
3. `dataflow_aware_s42` → `dataflow_aware_s43` → `dataflow_aware_s44`

### Epochs 确认
两个脚本均为 `--num-epochs 2`（Qwen L67, StarCoder L174）。

### Checkpoint 输出路径
| 模型 | s43 路径示例 |
|------|-------------|
| Qwen | `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/` |
| StarCoder | `/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43/` |

best checkpoint 保留在 `best_by_val_loss/` 和 `best_by_recall_at_1/`（Qwen）或 `best/`（StarCoder），中间 checkpoint 自动清理。

### s43 训练命令（自动执行，无需手动）
以 Qwen random_s43 为例：
```bash
python /root/structfuse-context/training/train.py \
    --model-name /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B \
    --train-file /root/autodl-tmp/structfuse/full_m2_training_data/train_random_s43.jsonl \
    --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s43.jsonl \
    --output-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43 \
    --hard-negative-strategy random \
    --num-epochs 2 --batch-size 8 --learning-rate 2e-5 --temperature 0.07 \
    --num-negatives 7 --hard-negative-ratio 0.5 --use-lora --gradient-checkpointing \
    --max-seq-length 2048 --seed 43 --eval-steps 500 --save-steps 1000
```

### 预计 s43 单 run 时长
2 epochs × 1414 steps = 2828 steps。需要从当前 s42 日志获取 step 速度才能估算——要我查一下当前训练进度和速度吗？

---
