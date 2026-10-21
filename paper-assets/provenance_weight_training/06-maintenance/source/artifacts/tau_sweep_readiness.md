# τ Sweep 就绪状态报告

**时间**: 2026-05-15 ~20:45 UTC

---

## 1. 当前训练进度

| 实验 | GPU | PID | 进度 | 剩余时间 | 完成顺序 |
|------|-----|-----|------|----------|----------|
| ess_only_seed42 | cuda:1 | 189240 | 96% (5856/6103) | ~9 min | 1st |
| golden_ratio_seed42 | cuda:0 | 193921 | 82% (5035/6103) | ~38 min | 2nd |
| tau_06_seed42 | cuda:3 | 195746 | 71% (4334/6103) | ~65 min | 3rd |
| nmin1_seed42 | cuda:2 | 194005 | 64% (3893/6103) | ~81 min | 4th |

所有训练正常运行，速度稳定 ~2.1-2.8s/it。

---

## 2. τ Sweep 脚本状态

**状态：就绪（通过 submit_training_job 提交，无需独立脚本）。**

scripts/ 目录下无 τ sweep 专用脚本。当前 tau_06_seed42 通过 submit_training_job 提交，后续实验同理。命令模板已从运行中进程 /proc/195746/cmdline 提取确认。

---

## 3. 各 τ 值完整训练命令

### tau_05_seed42 (τ=0.5) — cuda:1 释放后提交
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/tau_0.5_seed42 \
    --weighting_method adaptive \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --tau 0.5 \
    --bf16
```

### tau_07_seed42 (τ=0.7) — cuda:0 释放后提交
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/tau_0.7_seed42 \
    --weighting_method adaptive \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --tau 0.7 \
    --bf16
```

### tau_09_seed42 (τ=0.9) — cuda:3 释放后提交
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/tau_0.9_seed42 \
    --weighting_method adaptive \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --tau 0.9 \
    --bf16
```

### tau_095_seed42 (τ=0.95) — cuda:2 释放后提交
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/provenance_weight_training && \
WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/tau_0.95_seed42 \
    --weighting_method adaptive \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 42 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --tau 0.95 \
    --bf16
```

---

## 4. 提交顺序

| 顺序 | GPU 释放 | 新实验 | τ值 |
|------|---------|--------|-----|
| 1 | cuda:1 (ess_only_seed42) | tau_05_seed42 | 0.5 |
| 2 | cuda:0 (golden_ratio_seed42) | tau_07_seed42 | 0.7 |
| 3 | cuda:3 (tau_06_seed42) | tau_09_seed42 | 0.9 |
| 4 | cuda:2 (nmin1_seed42) | tau_095_seed42 | 0.95 |

---

## 5. 资源检查

### 磁盘空间
| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (根分区) | 30G | 14G | 17G | 46% |
| /root/autodl-tmp (数据盘) | 250G | 104G | 147G | 42% |

output/models/ 位于数据盘 (88G)。每个实验 save_total_limit=2 ≈ 3GB。4 个新实验 ≈ 12GB。**空间充足。**

### 训练数据 & 模型
- `data/scored_data.jsonl`: 930MB ✓
- `models/Qwen/Qwen3-0.6B/model.safetensors`: 1.5GB ✓

---

## 6. 关键参数确认

从运行中 tau_06_seed42 进程 cmdline 提取验证：

| 参数 | 值 | 状态 |
|------|-----|------|
| weighting_method | adaptive | ✓ |
| contamination_ratio | 0.4 | ✓ 显式传入 |
| WANDB_MODE | disabled | ✓ |
| bf16 | 启用 | ✓ |
| eval_data_path | 未传 | ✓ 禁止 inline eval |
| eval_steps | 未传 | ✓ |
| CUDA_VISIBLE_DEVICES | 由 submit_training_job 注入 | ✓ |

**结论：全部就绪，GPU 释放后可立即提交。**
