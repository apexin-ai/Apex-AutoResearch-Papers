# ssh prepare 14b eval commands

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-14b-eval-commands_20260522T220151_result.json`
- **Structured JSON:** [`a3f7d49fdd72e6579c6e.json`](../../sessions/a3/a3f7d49fdd72e6579c6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information. Here's the summary:

---

## 确认结果

### 当前状态
| 项目 | GPU | PID | 状态 |
|------|-----|-----|------|
| CLS 14B v2 | GPU 0 (57%, 16.9GB) | 215642 | 训练中，checkpoint 尚未保存 |
| CWM 14B | GPU 2 (82%, 14.4GB) | 211098 | 训练中，已有 checkpoint-478 (epoch 1) |
| GPU 1 | 0%, 空闲 | — | 可用于 eval |
| GPU 3 | 0%, 空闲 | — | 可用于 eval |

### 关键路径确认
- Base model: `/dev/shm/Qwen3-14B` — **存在**
- CLS test data: `data/test.jsonl` — **1890 samples**
- CWM test data: `data/cwm_test.jsonl` — **1890 samples**
- CWM checkpoint dir: `/root/autodl-tmp/checkpoints_cwm14b_func_s42/` — 目前有 `checkpoint-478`，总步数 1434
- CLS checkpoint dir: `/root/autodl-tmp/checkpoints_cls14b_func_s42_v2/` — **空**，等待保存

### 训练参数差异
| | CWM 14B | CLS 14B v2 |
|---|---|---|
| max_seq_length | 2048 | **4096** |
| 其他参数 | 一致 | 一致 |

### Eval 脚本
- **CLS**: `eval_verifier.py` — 支持 `--quantize_4bit`，输出 accuracy/F1/confusion matrix
- **CWM**: `eval_cwm_baseline.py` — **不支持 `--quantize_4bit`**，需要 bf16 加载 (~28GB)，32GB GPU 可行但 batch_size 需设为 1

### 注意事项
1. CWM eval 脚本无 4-bit 量化支持，14B bf16 约占 28GB，在 32GB 5090 上 batch_size 只能用 1
2. 训练完成后需先检查 `trainer_state.json` 中的 `best_model_checkpoint` 确定最佳 checkpoint

---

## 完整 Eval 命令

### 步骤 0: 训练完成后查找最佳 checkpoint
```bash
# CWM — 找最佳 checkpoint
python3 -c "import json; s=json.load(open('/root/autodl-tmp/checkpoints_cwm14b_func_s42/$(ls /root/autodl-tmp/checkpoints_cwm14b_func_s42/ | sort -V | tail -1)/trainer_state.json')); print(s['best_model_checkpoint'])"

# CLS — 找最佳 checkpoint
python3 -c "import json; s=json.load(open('/root/autodl-tmp/checkpoints_cls14b_func_s42_v2/$(ls /root/autodl-tmp/checkpoints_cls14b_func_s42_v2/ | sort -V | tail -1)/trainer_state.json')); print(s['best_model_checkpoint'])"
```

### CWM 14B eval (GPU 1):
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=1 python3 eval_cwm_baseline.py \
  --data_dir data/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints_cwm14b_func_s42/{BEST_CKPT} \
  --model_name /dev/shm/Qwen3-14B \
  --output /root/autodl-tmp/eval_results/cwm14b_func_s42/eval_cwm_results.json \
  --batch_size 1 \
  --max_seq_length 2048 \
  --max_new_tokens 64 \
  --save_predictions' > /tmp/eval_cwm14b.log 2>&1 &
```

### CLS 14B eval (GPU 3):
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 python3 eval_verifier.py \
  --data_dir data/ \
  --checkpoint_dir /root/autodl-tmp/checkpoints_cls14b_func_s42_v2/{BEST_CKPT} \
  --model_name /dev/shm/Qwen3-14B \
  --output /root/autodl-tmp/eval_results/cls14b_func_s42_v2/eval_results.json \
  --batch_size 4 \
  --max_seq_length 4096 \
  --quantize_4bit \
  --save_predictions' > /tmp/eval_cls14b_v2.log 2>&1 &
```

**`{BEST_CKPT}`** 替换为步骤 0 查到的实际 checkpoint 名（如 `checkpoint-478`）。运行前需要先 `mkdir -p /root/autodl-tmp/eval_results/cwm14b_func_s42/ /root/autodl-tmp/eval_results/cls14b_func_s42_v2/`。

CWM eval 因 batch_size=1 会较慢（约 1890 次推理 × ~64 新 token/次），预计 30-60 分钟。CLS eval 用 4-bit 量化，batch_size=4，预计 15-30 分钟。

---
