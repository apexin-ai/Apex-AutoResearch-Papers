# code random s42 retrain verify

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random_s42_retrain_verify_20260516T114407_result.json`
- **Structured JSON:** [`ab970060ba529ededb08.json`](../../sessions/ab/ab970060ba529ededb08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完毕。汇总如下：

## 配置确认清单

| 配置项 | 要求 | 实际 | 状态 |
|--------|------|------|------|
| seed | 42 | 42 | ✅ |
| strategy | random | `--hard-negative-strategy "random"` | ✅ |
| epochs | 2 | `--num-epochs 2` | ✅ |
| early_stopping_patience | 2 | `--early-stopping-patience 2` | ✅ |
| batch_size | 8 | `--batch-size 8` | ✅ |
| lr | 2e-5 | `--learning-rate 2e-5` | ✅ |
| num_negatives | 7 | `--num-negatives 7` | ✅ |
| max_seq_length | 2048 | `--max-seq-length 2048` | ✅ |
| temperature | 0.07 | `--temperature 0.07` | ✅ |
| LoRA r | 16 | `--lora-r 16` | ✅ |
| gradient_checkpointing | True | `--gradient-checkpointing` | ✅ |
| 输出目录 | `.../random_s42_retrain/` | ✅ | ✅ |
| conda 激活 | 需要 | `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` | ✅ |

## 训练数据

| 文件 | 行数 |
|------|------|
| train_random_s42.jsonl | 11,308 |
| val_random_s42.jsonl | 2,980 |

## 模型路径

`/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B` — ✅ 存在

## 训练时间估算

- Total steps per epoch: 11,308 ÷ 8 = 1,413 steps
- 2 epochs = **2,826 steps**（不含 early stopping 提前终止）
- 参考同系列 Qwen 训练速率，单 GPU 预估 **4–6 小时**

## 启动命令

```bash
nohup bash /root/structfuse/scripts/run_random_s42_retrain.sh &lt;GPU_ID> > /dev/null 2>&1 &
```

## 结论

脚本配置全部正确，无需修复。训练数据和模型路径均存在。可在 GPU 释放后立即启动。

---
