# research track e 14b prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-e-14b-prep_20260522T042022_result.json`
- **Structured JSON:** [`706eda784fedf6ccb946.json`](../../sessions/70/706eda784fedf6ccb946.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 已运行 20 分钟仍在生成阶段（1.4B × 5000 samples × 256 tokens，共享 GPU）。已有足够信息出报告。

---

## Track E 产出

### 1. 1.4B 模型验证 ✅
- **状态**: 17855 可用
- **参数量**: 1.41B
- **训练精度**: fp32（脚本默认 `torch.float32`，`fp16=False`）
- **词表**: 50277

### 2. 脚本兼容性 ✅
- 模型加载成功（`HF_HUB_CACHE=/root/autodl-tmp/.hf_cache`，**不能用 `HF_HOME`**）
- batch_size=4 **不 OOM**（生成阶段 GPU 占用 ~11GB，训练阶段预估 ~25-30GB，98GB GPU 无压力）
- 服务器版脚本比本地版多：`--bf16`, `--optim`, `--start_gen`, `--gradient_checkpointing`, intervention args
- Checkpoint 自动清理：保留 gen_0 + 最近 2 个 checkpoint

### 3. 性能估算（基于 dry-run 和 410M 基线）

| 阶段 | 410M | 1.4B（估算） |
|------|------|-------------|
| 生成 5000 样本 | ~11 min | ~25-30 min（dry-run 20+ min 仍在跑，共享 GPU） |
| 训练 5000 步 | ~12 min | ~35-40 min |
| 指标计算 | ~1.5 min | ~3-5 min |
| **每 gen 总计** | **~24 min** | **~65-75 min** |

| 实验 | 预估时长 |
|------|---------|
| T=10（10 gen + baseline） | **12-14 小时** |
| T=15（15 gen + baseline） | **17-20 小时** |
| **6 格总计（串行）** | **~90-100 GPU-hours** |

### 4. 2.8B 下载状态
- **模型权重**: ✅ 完整（5.3GB safetensors）
- **Config**: ✅
- **Tokenizer**: ❌ 不完整（vocab=2，缺 tokenizer.json/tokenizer_config.json）
- 需重新下载 tokenizer 文件

### 5. 服务器资源
- **GPU**: 6x RTX PRO 6000 Blackwell, 98GB
- **磁盘**: 104GB 可用 / 350GB 总
- **当前负载**: 6 个 410M 实验占满 6 GPU
  - ~1h 空出 2 GPU (t10_a075_s43, t25_a060_s42)
  - ~2h 空出 4 GPU
  - ~3.5h 空出 5 GPU
  - t20_a075_s43 还需 ~8h
- **磁盘**: 每个 1.4B 实验峰值 ~20-25GB（自动清理后），6 格串行没问题

### 6. 六格实验命令模板

```bash
# 环境变量前缀（所有实验共用）
ENV_PREFIX="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HUB_CACHE=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && cd /root/autodl-tmp/distrib_canary_collapse"

# ===== T=10 =====
# Cell 1: T=10, α=0.45, s42
CUDA_VISIBLE_DEVICES=X python -u iterative_train.py \
  --model_name EleutherAI/pythia-1.4b-deduped \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.45 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --output_dir results/phase_diagram/t10_a045_s42_fp32_14b \
  --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 \
  --gen_max_new_tokens 256 --gen_batch_size 8 \
  --top_p 0.95 --optim adamw_torch

# Cell 2: T=10, α=0.50, s42
# → 同上，--synthetic_ratio 0.50, --output_dir .../t10_a050_s42_fp32_14b

# Cell 3: T=10, α=0.60, s42
# → 同上，--synthetic_ratio 0.60, --output_dir .../t10_a060_s42_fp32_14b

# ===== T=15 =====
# Cell 4: T=15, α=0.45, s42
# → --num_generations 15, --output_dir .../t15_a045_s42_fp32_14b

# Cell 5: T=15, α=0.50, s42
# → --num_generations 15, --synthetic_ratio 0.50, --output_dir .../t15_a050_s42_fp32_14b

# Cell 6: T=15, α=0.60, s42
# → --num_generations 15, --synthetic_ratio 0.60, --output_dir .../t15_a060_s42_fp32_14b
```

### 7. 注意事项
- **Dry-run 仍在运行**（PID 607226，已 20+ min），完成后需清理 `results/dryrun_14b_test/`
- 提交实验前用 `CUDA_VISIBLE_DEVICES=X` 绑定到空闲 GPU，避免多实验争抢同一 GPU
- 2.8B tokenizer 不完整，需联网补下载后才能用于实验
- C007 约束：提交前 `df -h` 确认空间充足

---
