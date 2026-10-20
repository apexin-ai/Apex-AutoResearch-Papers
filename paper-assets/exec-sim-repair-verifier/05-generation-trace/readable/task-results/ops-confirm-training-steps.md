# ops confirm training steps

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_confirm-training-steps_20260516T115651_result.json`
- **Structured JSON:** [`1f937f6dc9640fc8d14c.json`](../../sessions/1f/1f937f6dc9640fc8d14c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture obtained. Here's the precise report:

---

## 训练状态汇报（2026-05-16 实时数据）

### 重要发现：原 Qwen3 训练全部已死，当前运行的是新的 DeepSeek 训练

原来 5/14 启动的 Qwen3-4B/8B 训练三个全部在 2026-05-14 ~08:58 停止（train.log 最后修改时间），当前 cuda:0 和 cuda:1 上运行的是**今天（5/16）新启动的 DeepSeek-Coder-6.7B 训练**。

---

### 1. cls-repo (cuda:0, PID 470263)

| 项目 | 值 |
|------|-----|
| **当前 step** | **1754/6633** |
| **total steps** | 6633 |
| **模型** | deepseek-coder-6.7b-instruct（非 Qwen3） |
| **run_name** | deepseek-cls-repo-seq8192 |
| **启动时间** | 2026-05-16 15:29:33 |
| **已运行** | ~5h24m |
| **速度** | ~11.8s/it |
| **output_dir** | /root/autodl-tmp/checkpoints_deepseek_cls_repo/ |
| **重启** | 第一次 OOM 失败（GPU 0 被旧进程占满），随后成功启动 |

命令：
```
CUDA_VISIBLE_DEVICES=0 python3 train_unified.py \
  --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --data_dir data/ --task cls \
  --output_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo/ \
  --run_name deepseek-cls-repo-level --epochs 3 --no_wandb
```

---

### 2. cwm-repo (cuda:1, PID 479953)

| 项目 | 值 |
|------|-----|
| **当前 step** | **1643/13266** |
| **total steps** | **13266**（确认，非 6633） |
| **模型** | deepseek-coder-6.7b-instruct |
| **run_name** | deepseek-cwm-repo-s42 |
| **启动时间** | 2026-05-16 16:04:49（tmux创建），训练开始 16:15:35 |
| **已运行** | ~3h44m |
| **速度** | ~8.0s/it |
| **output_dir** | /root/autodl-tmp/checkpoints_deepseek_cwm_repo/ |

**total steps = 13266 的原因**：`batch_size=2, grad_accumulation=8` → effective batch 16 → 70748/16 ≈ 4422 steps/epoch × 3 epochs = 13266

命令：
```
python3 train_unified.py \
  --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --train_file swebench_full/swebench_train.jsonl --val_file swebench_full/swebench_val.jsonl \
  --task cwm --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 \
  --epochs 3 --batch_size 2 --grad_accumulation 8 --lr 2e-4 \
  --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/
```

---

### 3. cuda:2 orphan (PID 499350) — 已死亡

| 项目 | 值 |
|------|-----|
| **状态** | **进程已不存在，GPU 空闲（0% util, 0 MiB）** |
| **死亡时间** | 2026-05-14 08:58:39（log 最后修改） |
| **死亡时 step** | ~662/6633 |
| **模型** | Qwen3-8B（/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/） |
| **任务** | CLS |
| **数据** | train=70748, val=9335 |
| **params** | trainable: 15,335,424 / total: 8,206,070,784 (0.19%) |
| **output_dir** | /root/autodl-tmp/checkpoints_repo_cls_8b_conda/ |
| **已保存 ckpt** | checkpoint-200, checkpoint-400, checkpoint-600 |

---

### 关于之前报告的矛盾

- **"step 1632/6633" vs "step 643/6633"**：两个都过时了。之前的 Qwen3-4B cls 训练停在了 step 643/6633（5/14 死亡）。当前实际跑的是 DeepSeek-6.7B，在 step 1754/6633。
- **cwm total steps 13266 vs 6633**：Qwen3-4B 旧 run 是 6633（grad_accum=16），DeepSeek 新 run 是 13266（grad_accum=8）。当前运行的确实是 13266。

---
