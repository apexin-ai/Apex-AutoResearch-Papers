# D063 Val Set Checkpoint Sweep 准备方案

> 生成时间: 2026-05-14 16:30 UTC

## 1. eval 脚本现状

**`eval_repo_cls.py` 已支持 `--split val`**，无需代码修改。

- Line 260: `p.add_argument("--split", choices=["val", "test"], default="test")`
- 数据加载路径: `data/swebench_full/swebench_{args.split}.jsonl`
- Output JSON 包含 `"split"` 字段用于区分

## 2. Val Set 信息

| 属性 | 值 |
|------|-----|
| 文件位置 | `data/swebench_full/swebench_val.jsonl`（westd + home 均有） |
| 样本数 | **9335** |
| Label 分布 | fail=2252, pass=7083 |
| Majority baseline | **75.88%**（pass 为多数类） |
| Test set baseline | 72.96%（对比参考） |

## 3. 已完成的 Val Sweep 结果 (home)

Home 上 CLS seed123 的 val sweep 已部分完成（前一 Worker 执行）:

| Checkpoint | Val Accuracy | Val F1_macro | Gap vs Maj (75.88%) | Test Accuracy (之前) |
|------------|-------------|-------------|---------------------|---------------------|
| ckpt-200   | 62.51%      | 55.54       | -13.37pp            | ~64.75% (test)      |
| ckpt-400   | 80.72%      | 67.03       | +4.84pp             | 75.05% (test)       |
| **ckpt-600** | 76.78%    | 66.81       | +0.90pp             | **80.73%** (test)   |
| **ckpt-800** | **81.81%** | **69.14**   | **+5.93pp**         | 74.27% (test)       |
| ckpt-1000  | ⏳ running  | —           | —                   | 73.14% (test)       |

**重要发现**: Val best (ckpt-800, 81.81%) ≠ Test best (ckpt-600, 80.73%)。Val 和 test 的最优 checkpoint 不同！这正是 D063 要解决的问题——应该在 val 上选 checkpoint。

## 4. GPU 空闲状态

### westd (4×5090) — 全部占用
| GPU | 进程 | PID | 预计释放 |
|-----|------|-----|---------|
| cuda:0 | CWM seed123 eval | 195531 | ~02:30 UTC May 15 |
| cuda:1 | CWM v12 eval | 195668 | ~02:20 UTC May 15 |
| cuda:2 | 8B CWM 训练 | 210573 | 未知（刚开始） |
| cuda:3 | 8B CLS seed123 训练 | 210657 | 未知（刚开始） |

### home (1×5090) — 占用
| GPU | 进程 | PID | 预计释放 |
|-----|------|-----|---------|
| cuda:0 | CLS seed123 val eval (ckpt-1000) | 3060047 | ~30min 内 |

## 5. 完整 Val Sweep 命令列表

### Priority 1: westd conda 模型（apple-to-apple 必须，等 GPU 0/1 释放后执行）

```bash
# === 环境准备 ===
cd /home/sonny/exec-sim-repair-verifier
mkdir -p val_eval_results
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# === CLS v5-conda (4B, seed42) — 3 checkpoints ===
# ckpt-200
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_v5_conda/checkpoint-200 \
  --split val \
  --output val_eval_results/cls_v5_conda_ckpt200.json \
  --pred_output val_eval_results/cls_v5_conda_ckpt200_predictions.jsonl \
  --batch_size 16 --device cuda:0

# ckpt-400
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_v5_conda/checkpoint-400 \
  --split val \
  --output val_eval_results/cls_v5_conda_ckpt400.json \
  --pred_output val_eval_results/cls_v5_conda_ckpt400_predictions.jsonl \
  --batch_size 16 --device cuda:0

# ckpt-600
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_v5_conda/checkpoint-600 \
  --split val \
  --output val_eval_results/cls_v5_conda_ckpt600.json \
  --pred_output val_eval_results/cls_v5_conda_ckpt600_predictions.jsonl \
  --batch_size 16 --device cuda:0

# === CLS 8B-conda (8B, seed42) — 3 checkpoints ===
# ckpt-200
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200 \
  --model_name Qwen/Qwen3-8B \
  --split val \
  --output val_eval_results/cls_8b_conda_ckpt200.json \
  --pred_output val_eval_results/cls_8b_conda_ckpt200_predictions.jsonl \
  --batch_size 8 --device cuda:0

# ckpt-400
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400 \
  --model_name Qwen/Qwen3-8B \
  --split val \
  --output val_eval_results/cls_8b_conda_ckpt400.json \
  --pred_output val_eval_results/cls_8b_conda_ckpt400_predictions.jsonl \
  --batch_size 8 --device cuda:0

# ckpt-600
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600 \
  --model_name Qwen/Qwen3-8B \
  --split val \
  --output val_eval_results/cls_8b_conda_ckpt600.json \
  --pred_output val_eval_results/cls_8b_conda_ckpt600_predictions.jsonl \
  --batch_size 8 --device cuda:0
```

### Priority 2: home CLS v5 (home 环境，seed123 完成后接着跑)

```bash
# === CLS v5 (4B, seed42, home) — 5 checkpoints ===
cd /home/sonny/exec-sim-repair-verifier

# ckpt-600
python eval_repo_cls.py \
  --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-600 \
  --split val \
  --output val_eval_results/cls_v5_home_ckpt600.json \
  --pred_output val_eval_results/cls_v5_home_ckpt600_predictions.jsonl \
  --batch_size 8 --device cuda:0

# ckpt-4000
python eval_repo_cls.py \
  --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4000 \
  --split val \
  --output val_eval_results/cls_v5_home_ckpt4000.json \
  --pred_output val_eval_results/cls_v5_home_ckpt4000_predictions.jsonl \
  --batch_size 8 --device cuda:0

# ckpt-4200
python eval_repo_cls.py \
  --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4200 \
  --split val \
  --output val_eval_results/cls_v5_home_ckpt4200.json \
  --pred_output val_eval_results/cls_v5_home_ckpt4200_predictions.jsonl \
  --batch_size 8 --device cuda:0

# ckpt-4400
python eval_repo_cls.py \
  --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4400 \
  --split val \
  --output val_eval_results/cls_v5_home_ckpt4400.json \
  --pred_output val_eval_results/cls_v5_home_ckpt4400_predictions.jsonl \
  --batch_size 8 --device cuda:0

# ckpt-4600
python eval_repo_cls.py \
  --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4600 \
  --split val \
  --output val_eval_results/cls_v5_home_ckpt4600.json \
  --pred_output val_eval_results/cls_v5_home_ckpt4600_predictions.jsonl \
  --batch_size 8 --device cuda:0
```

### Priority 3 (bonus): westd 8B seed123 conda（训练仍在进行，checkpoint 已有）

```bash
# === CLS 8B seed123-conda (8B, seed123) — 3 checkpoints ===
python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200 \
  --model_name Qwen/Qwen3-8B \
  --split val \
  --output val_eval_results/cls_8b_seed123_conda_ckpt200.json \
  --pred_output val_eval_results/cls_8b_seed123_conda_ckpt200_predictions.jsonl \
  --batch_size 8 --device cuda:0

python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-400 \
  --model_name Qwen/Qwen3-8B \
  --split val \
  --output val_eval_results/cls_8b_seed123_conda_ckpt400.json \
  --pred_output val_eval_results/cls_8b_seed123_conda_ckpt400_predictions.jsonl \
  --batch_size 8 --device cuda:0

python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-600 \
  --model_name Qwen/Qwen3-8B \
  --split val \
  --output val_eval_results/cls_8b_seed123_conda_ckpt600.json \
  --pred_output val_eval_results/cls_8b_seed123_conda_ckpt600_predictions.jsonl \
  --batch_size 8 --device cuda:0
```

## 6. 执行策略

| 时间 | 服务器 | GPU | 动作 |
|------|--------|-----|------|
| 现在 | home | cuda:0 | seed123 ckpt-1000 val eval 运行中（~30min 内完成） |
| seed123 完成后 | home | cuda:0 | 接着跑 CLS v5 (home) 5 个 ckpt val eval（~2.5h） |
| ~02:30 UTC May 15 | westd | cuda:0 | CWM eval 完成，启动 P1 v5-conda val sweep（~1.5h for 3 ckpts） |
| v5-conda 后 | westd | cuda:0 | 启动 P1 8b-conda val sweep（~2h for 3 ckpts, 8B 更慢） |
| 8b-conda 后 | westd | cuda:0 | P3 8b-seed123-conda val sweep（可选） |

**每个 CLS 4B ckpt val eval 约 25-30 分钟，8B 约 40-50 分钟（9335 samples）。**

## 7. 注意事项

1. **Val set majority baseline (75.88%) ≠ Test set (72.96%)**：val 上 pass 比例更高，绝对数字会偏高
2. **Val 和 test 最优 checkpoint 可能不同**：seed123 已验证——val best=ckpt-800, test best=ckpt-600
3. **不要在同一 GPU 上同时跑 eval 和训练**：GPU 2/3 正在 8B 训练，不可用
4. **Output 文件命名统一放 val_eval_results/**：与 home 已有结果保持一致
5. **westd 上需要先 `mkdir -p val_eval_results`**：目录不存在
