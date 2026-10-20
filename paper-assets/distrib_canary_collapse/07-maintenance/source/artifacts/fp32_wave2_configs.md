# fp32 Wave 2 实验配置

## 参考基准

从 westd-17855 `results/alpha_sweep/a050_s42_fp32/config.json` 提取：

```json
{
  "model_name": "EleutherAI/pythia-410m",
  "data_dir": "data/wikitext103_5k",
  "num_generations": 10,
  "steps_per_gen": 5000,
  "batch_size": 4,
  "max_length": 512,
  "lr": 5e-05,
  "gen_max_new_tokens": 256,
  "gen_batch_size": 16,
  "top_p": 0.95,
  "accumulate": false,
  "gradient_checkpointing": false,
  "bf16": false,
  "optim": "adamw_torch"
}
```

> **注意**: 脚本没有 `--torch_dtype` 参数。fp32 通过**不传 `--bf16`** 实现（默认即 fp32）。

---

## 目标服务器

**westd-17855**（推荐）
- 6× NVIDIA RTX PRO 6000 Blackwell (98 GB)
- 磁盘: 223 GB 可用
- 数据: `data/wikitext103_5k` 已就位
- 代码: `/root/autodl-tmp/distrib_canary_collapse/`

---

## 前置条件（阻塞）

### padding_side 修复必须先同步

westd-17855 的 `iterative_train.py` **没有** padding_side 修复。日志中大量出现：
```
[transformers] A decoder-only architecture is being used, but right-padding was detected!
```

westd-19828 版本已修复（行 100-127，生成时临时切换 `padding_side='left'`）。

**同步命令**：
```bash
# 在 westd-17855 上执行
scp westd-19828:/root/autodl-tmp/distrib_canary_collapse/iterative_train.py \
    /root/autodl-tmp/distrib_canary_collapse/iterative_train.py
```

或手动在 westd-17855 的 `generate_synthetic_data()` 函数开头加入：
```python
original_padding_side = tokenizer.padding_side
tokenizer.padding_side = 'left'
# ... 生成逻辑 ...
# 结束时恢复:
tokenizer.padding_side = original_padding_side
```

---

## 4 个实验的完整命令

### 工作目录

```bash
cd /root/autodl-tmp/distrib_canary_collapse
mkdir -p /root/runs/distrib_canary_collapse
```

### 实验 1: alpha_sweep_a025_s42_fp32

```bash
tmux new-session -d -s alpha_sweep_a025_s42_fp32 \
  "CUDA_VISIBLE_DEVICES=2 python iterative_train.py \
    --model_name EleutherAI/pythia-410m \
    --data_dir data/wikitext103_5k \
    --synthetic_ratio 0.25 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/alpha_sweep/a025_s42_fp32 \
    --seed 42 \
    --batch_size 4 \
    --max_length 512 \
    --lr 5e-5 \
    --gen_max_new_tokens 256 \
    --gen_batch_size 16 \
    --top_p 0.95 \
    --optim adamw_torch \
    2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_fp32.log"
```

**输出目录**: `results/alpha_sweep/a025_s42_fp32`

### 实验 2: alpha_sweep_a025_s43_fp32

```bash
tmux new-session -d -s alpha_sweep_a025_s43_fp32 \
  "CUDA_VISIBLE_DEVICES=3 python iterative_train.py \
    --model_name EleutherAI/pythia-410m \
    --data_dir data/wikitext103_5k \
    --synthetic_ratio 0.25 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/alpha_sweep/a025_s43_fp32 \
    --seed 43 \
    --batch_size 4 \
    --max_length 512 \
    --lr 5e-5 \
    --gen_max_new_tokens 256 \
    --gen_batch_size 16 \
    --top_p 0.95 \
    --optim adamw_torch \
    2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a025_s43_fp32.log"
```

**输出目录**: `results/alpha_sweep/a025_s43_fp32`

### 实验 3: alpha_sweep_a025_s44_fp32

```bash
tmux new-session -d -s alpha_sweep_a025_s44_fp32 \
  "CUDA_VISIBLE_DEVICES=4 python iterative_train.py \
    --model_name EleutherAI/pythia-410m \
    --data_dir data/wikitext103_5k \
    --synthetic_ratio 0.25 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/alpha_sweep/a025_s44_fp32 \
    --seed 44 \
    --batch_size 4 \
    --max_length 512 \
    --lr 5e-5 \
    --gen_max_new_tokens 256 \
    --gen_batch_size 16 \
    --top_p 0.95 \
    --optim adamw_torch \
    2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a025_s44_fp32.log"
```

**输出目录**: `results/alpha_sweep/a025_s44_fp32`

### 实验 4: alpha_sweep_a075_s42_fp32

```bash
tmux new-session -d -s alpha_sweep_a075_s42_fp32 \
  "CUDA_VISIBLE_DEVICES=5 python iterative_train.py \
    --model_name EleutherAI/pythia-410m \
    --data_dir data/wikitext103_5k \
    --synthetic_ratio 0.75 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/alpha_sweep/a075_s42_fp32 \
    --seed 42 \
    --batch_size 4 \
    --max_length 512 \
    --lr 5e-5 \
    --gen_max_new_tokens 256 \
    --gen_batch_size 16 \
    --top_p 0.95 \
    --optim adamw_torch \
    2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log"
```

**输出目录**: `results/alpha_sweep/a075_s42_fp32`

---

## GPU 分配

当前 westd-17855 GPU 状态（2026-05-19 ~14:00 CST）：

| GPU | 已用内存 | 用途 |
|-----|---------|------|
| 0 | 71 GB | scale_69b / qwen35 实验 |
| 1 | 35 GB | 其他实验 |
| 2 | 14 GB | a050_s42_fp32 (或 a010) |
| 3 | 14 GB | a050_s43_fp32 |
| 4 | 14 GB | a050_s44_fp32 |
| 5 | 14 GB | a010_s42_fp32 |

**Wave 2 启动策略**: 等 GPU 2-5 上的当前实验完成后，逐卡替换启动。预计 a050 fp32 3 个实验还需 ~2 小时完成，a010_fp32 还需 ~2.5 小时。

如需提前启动，可检查 GPU 0/1 的实验是否即将结束，或将 Pythia-410m 实验 2 个共享一张 GPU（fp32 单实验 ~14 GB，98 GB GPU 可容纳多个）。

---

## 预估资源

| 指标 | 值 |
|------|-----|
| 单实验 GPU 内存 | ~14 GB |
| 单实验磁盘占用 | ~1.6 GB |
| 4 实验总磁盘 | ~6.4 GB |
| 单实验耗时 | ~3 小时（10 gens × ~17 min/gen + gen_0 baseline） |
| 训练速度 | ~7.68 it/s (fp32, Pythia-410m, batch_size=4) |
| 总 GPU hours | ~12 GPU-hours（4 实验并行则 wall time ~3h） |

---

## 注意事项

1. **padding_side 修复（阻塞）**: 必须在启动前完成同步，否则生成数据质量受 right-padding 影响，实验结果与 westd-19828 上其他实验不可比
2. **GPU 调度**: 命令中的 `CUDA_VISIBLE_DEVICES` 需根据启动时实际空闲 GPU 调整
3. **不传 `--bf16`**: 脚本默认即 fp32，无需额外 dtype 参数
4. **不传 `--accumulate`**: 保持与 a050_fp32 一致的非累积模式
5. **输出目录命名**: 使用 `_fp32` 后缀与 pre-D080（fp16）实验区分
6. **C004 约束**: 启动前确认目标 GPU 无正在运行的实验进程
