# P0 实验诊断报告

**时间**: 2026-05-21 21:05 UTC
**服务器**: westd-41312

## 1. GPU 占用情况

**结论: 4 张 GPU 全部在跑 P0 实验，不存在空闲 GPU。**

| GPU | PID | 实验名 | Method | 数据 | 总步数 | 当前步 | 进度 |
|-----|-----|--------|--------|------|--------|--------|------|
| 0 | 601614 | detect_remove_q05_seed42 | uniform | scored_data_filtered_q05.jsonl (217774条) | 6103 | 2769 | 45% |
| 1 | 605276 | dr_epoch_matched_indep_lr_seed42 | uniform | scored_data_filtered_q05.jsonl (217774条) | 2533 | 1974 | 78% |
| 2 | 606296 | uniform_epoch_matched_indep_lr_seed42 | uniform | scored_data.jsonl (371499条) | 2533 | 1467 | 58% |
| 3 | 603555 | random_reweight_baseline_seed42 | adaptive | scored_data_random_shuffle.jsonl (371499条) | 6103 | 2064 | 34% |

所有 GPU 显存占用 45634MiB/97887MiB，利用率 69-100%。

## 2. LR Scheduler 诊断

**结论: 无 cosine 问题。所有实验均使用 linear schedule。**

- 脚本 `pretrain_weighted.py` 第328行: `--lr_scheduler_type` 默认值为 `"linear"`
- 4 个运行中的实验均未指定 `--lr_scheduler_type` → 均使用默认 linear
- uniform_epoch_matched 和 dr_epoch_matched 的 config.json 中明确记录 `"lr_scheduler_type": "linear"`
- warmup_ratio 默认 0.05

## 3. 训练脚本能力

### 支持的 weighting_method
`uniform`, `grid`, `adaptive`, `golden_ratio`, `ess_only`, `random`

### Detect-Remove 实现方式
**不是**独立的 weighting_method。通过预过滤数据实现:
- 用 `scored_data_filtered_q05.jsonl` (q_score ≤ 0.5 的样本，217774条)
- 然后用 `--weighting_method uniform` 训练
- 已有过滤数据: q03 / q05 / q07 / q08 四个阈值
- **GPU 0 正在跑的 detect_remove_q05_seed42 就是这个方案**

### Random Reweight 实现方式
GPU 3 上的 random_reweight_baseline_seed42 采用的方案:
- 数据: `scored_data_random_shuffle.jsonl` (shuffle 后的 q_score)
- 方法: `--weighting_method adaptive` (对打乱的分数应用 adaptive 算法)
- 目的: 证明 adaptive 的增益来自 score 信号而非加权本身

注: 脚本也有 `--weighting_method random` (从 U(0,2) 随机采权重)，但当前实验未采用此方式。

## 4. 各实验启动命令（记录）

### GPU 0: detect_remove_q05_seed42
```bash
python -u training/pretrain_weighted.py \
  --data_path data/scored_data_filtered_q05.jsonl \
  --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method uniform \
  --contamination_ratio 0.4 \
  --num_train_tokens 200000000 \
  --batch_size 4 --gradient_accumulation_steps 4 \
  --learning_rate 5e-5 --max_length 2048 \
  --seed 42 --save_steps 500 --logging_steps 10 \
  --bf16 --save_total_limit 3
```

### GPU 1: dr_epoch_matched_indep_lr_seed42
```bash
python -u training/pretrain_weighted.py \
  --data_path data/scored_data_filtered_q05.jsonl \
  --output_dir /root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_indep_lr_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method uniform \
  --contamination_ratio 0.4 \
  --max_steps 2533 \
  --batch_size 4 --gradient_accumulation_steps 4 \
  --learning_rate 5e-5 --max_length 2048 \
  --seed 42 --save_steps 500 --logging_steps 10 \
  --bf16 --save_total_limit 3
```

### GPU 2: uniform_epoch_matched_indep_lr_seed42
```bash
python -u training/pretrain_weighted.py \
  --data_path data/scored_data.jsonl \
  --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_epoch_matched_indep_lr_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method uniform \
  --contamination_ratio 0.4 \
  --max_steps 2533 \
  --batch_size 4 --gradient_accumulation_steps 4 \
  --learning_rate 5e-5 --max_length 2048 \
  --seed 42 --save_steps 500 --logging_steps 10 \
  --bf16 --save_total_limit 3
```

### GPU 3: random_reweight_baseline_seed42
```bash
python -u training/pretrain_weighted.py \
  --data_path data/scored_data_random_shuffle.jsonl \
  --output_dir /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_baseline_seed42 \
  --model_name models/Qwen/Qwen3-0.6B \
  --weighting_method adaptive \
  --contamination_ratio 0.4 --tau 0.8 \
  --num_train_tokens 200000000 \
  --batch_size 4 --gradient_accumulation_steps 4 \
  --learning_rate 5e-5 --max_length 2048 \
  --seed 42 --save_steps 500 --logging_steps 10 \
  --bf16 --save_total_limit 3
```

## 5. 预估完成时间

基于 checkpoint 保存间隔推算 (~500 steps / 17-19 min):

| 实验 | 剩余步数 | 预估剩余时间 | 预计完成时间 (UTC) |
|------|----------|-------------|-------------------|
| dr_epoch_matched (GPU 1) | ~559 | ~20 min | May 21 ~21:25 |
| uniform_epoch_matched (GPU 2) | ~1066 | ~38 min | May 21 ~21:43 |
| detect_remove_q05 (GPU 0) | ~3334 | ~2 hrs | May 21 ~23:05 |
| random_reweight (GPU 3) | ~4039 | ~2.5 hrs | May 21 ~23:35 |

## 6. 需要 Agent 决策的事项

1. **无需 kill 任何实验** — 所有 4 个 P0 实验已在正确运行，lr_scheduler 均为 linear
2. **无需提交新实验** — 4 张 GPU 已满载
3. **dr_epoch_matched 和 uniform_epoch_matched 约 20-40 分钟后完成**，届时 GPU 1 和 GPU 2 释放，可提交新实验
4. detect_remove_q05 的 config.json 未记录 lr_scheduler_type 字段（较早版本的 config 保存逻辑），但启动命令无 --lr_scheduler_type 参数，默认为 linear，无误
