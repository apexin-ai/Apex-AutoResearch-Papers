# check gpu reality 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_reality_41312_20260518T144420_result.json`
- **Structured JSON:** [`b3f137d0a0d46a905abb.json`](../../sessions/b3/b3f137d0a0d46a905abb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整报告（westd-30476）

### Step 1: nvidia-smi
```
4× NVIDIA RTX PRO 6000 Black (每卡 97887MiB)

GPU 0: 0MiB / 0%  — 空闲
GPU 1: 0MiB / 0%  — 空闲
GPU 2: 41757MiB / 99% — PID 36443 (python) — 活跃
GPU 3: 0MiB / 0%  — 空闲
```

### Step 2: pretrain_weighted 进程
**GPU 2 上运行的是 `detect_remove_q07_seed42` 任务，不是 1.7B 训练：**
```
python training/pretrain_weighted.py \
  --data_path data/scored_data_filtered_q07.jsonl \
  --output_dir /root/autodl-tmp/output/models/detect_remove_q07_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method uniform \
  --contamination_ratio 0.4 \
  --num_train_tokens 200000000 \
  --seed 42 --bf16
```
已运行约 153 分钟，CPU 100%。

### Step 3: N-gram 训练状态
```
ngram_adaptive output NOT FOUND
ngram_uniform output NOT FOUND
ngram_adaptive log NOT FOUND
ngram_uniform log NOT FOUND
```
**N-gram 训练从未启动过。**

### Step 4: 1.7B 训练进度
```
uniform_1_7b log NOT FOUND
adaptive_1_7b log NOT FOUND
```
**1.7B 训练从未启动过。**

### Step 5: tmux sessions
```
detect_remove_q07_seed42_r2: 1 windows (created Mon May 18 20:11:58 2026)
```
只有一个 tmux session，对应 detect_remove_q07 任务。

### Step 6: N-gram 训练数据
```
ngram qscore data NOT FOUND
```
**N-gram 评分数据文件不存在。**

---

### 总结

| 项目 | 状态 |
|------|------|
| GPU 使用 | 仅 GPU 2 被占用（detect_remove_q07_seed42_r2） |
| 1.7B 训练 | **从未启动**（无日志、无输出） |
| N-gram 训练 | **从未启动**（无日志、无输出、无数据文件） |
| 当前唯一任务 | detect_remove_q07_seed42 (0.6B, uniform, GPU 2, 运行中) |
| 空闲 GPU | GPU 0, 1, 3（共 3 张卡空闲） |

---
