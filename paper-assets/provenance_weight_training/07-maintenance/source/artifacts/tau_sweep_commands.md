# τ Sweep 后续实验提交命令

## Dry-Run 验证结果

| 检查项 | 状态 |
|--------|------|
| `--tau` 参数 | ✅ pretrain_weighted.py 支持，控制 target effective human proportion |
| 数据路径 `data/scored_data.jsonl` | ✅ 存在 |
| 模型路径 `models/Qwen/Qwen3-0.6B` | ✅ 存在 |
| 脚本 `training/run_tau_0.{5,7,9,95}_seed42.sh` | ✅ 全部存在，格式与 tau_0.6 一致 |
| 输出目录 `output/models/tau_0.{5,7,9,95}_seed42` | ✅ 尚未创建（干净起点） |

## 脚本内容确认

所有脚本仅在 `--tau` 和 `--output_dir` 上与 tau_0.6 不同，其余参数完全一致：
- `--weighting_method adaptive`
- `--model_name models/Qwen/Qwen3-0.6B`
- `--num_train_tokens 200000000`
- `--batch_size 4 --gradient_accumulation_steps 4 --max_length 2048`
- `--learning_rate 5e-5 --seed 42`
- `--contamination_ratio 0.4 --bf16`

## 当前 GPU 占用（2026-05-15 约 20:45 UTC）

| GPU | 当前实验 | CUDA_VISIBLE_DEVICES | Step / ~6104 | 进度 | 预计剩余 |
|-----|---------|---------------------|-------------|------|---------|
| 0 | golden_ratio_seed42 | 0 | 5032 | 82% | ~39 min |
| 1 | ess_only_seed42 | 1 | 5852 | 96% | ~9 min |
| 2 | nmin1_seed42 | 2 | 3889 | 64% | ~105 min |
| 3 | tau_0.6_seed42 | 3 | 4332 | 71% | ~65 min |

GPU 释放顺序：GPU1 → GPU0 → GPU3 → GPU2

## 提交命令

按 GPU 释放顺序安排：

### 1. tau_05_seed42 (τ=0.5) → GPU 1（最先空闲）

```bash
tmux new-session -d -s tau_05_seed42 \
  "CUDA_VISIBLE_DEVICES=1 bash /root/provenance_weight_training/training/run_tau_0.5_seed42.sh"
```

### 2. tau_07_seed42 (τ=0.7) → GPU 0

```bash
tmux new-session -d -s tau_07_seed42 \
  "CUDA_VISIBLE_DEVICES=0 bash /root/provenance_weight_training/training/run_tau_0.7_seed42.sh"
```

### 3. tau_095_seed42 (τ=0.95) → GPU 3

```bash
tmux new-session -d -s tau_095_seed42 \
  "CUDA_VISIBLE_DEVICES=3 bash /root/provenance_weight_training/training/run_tau_0.95_seed42.sh"
```

### 4. tau_09_seed42 (τ=0.9) → GPU 2（最后空闲）

```bash
tmux new-session -d -s tau_09_seed42 \
  "CUDA_VISIBLE_DEVICES=2 bash /root/provenance_weight_training/training/run_tau_0.9_seed42.sh"
```

## 预计 GPU 小时数

- 单个实验：**~3.7 GPU-hours**（基于 tau_0.6 实际运行速率 ~0.037 min/step × 6104 steps）
- 4 个实验共计：**~14.8 GPU-hours**
- Wall-clock 时间：最后一个 GPU 释放 (~105 min) + 实验时长 (~3.7h) ≈ **5.5 小时**

## 批量提交（等全部 GPU 空闲后一次提交）

```bash
# 确认所有 GPU 空闲
nvidia-smi --query-compute-apps=pid --format=csv,noheader | wc -l
# 应返回 0

# 批量启动
tmux new-session -d -s tau_05_seed42 "CUDA_VISIBLE_DEVICES=0 bash /root/provenance_weight_training/training/run_tau_0.5_seed42.sh"
tmux new-session -d -s tau_07_seed42 "CUDA_VISIBLE_DEVICES=1 bash /root/provenance_weight_training/training/run_tau_0.7_seed42.sh"
tmux new-session -d -s tau_09_seed42 "CUDA_VISIBLE_DEVICES=2 bash /root/provenance_weight_training/training/run_tau_0.9_seed42.sh"
tmux new-session -d -s tau_095_seed42 "CUDA_VISIBLE_DEVICES=3 bash /root/provenance_weight_training/training/run_tau_0.95_seed42.sh"
```
