# D060: Pythia-6.9B 训练准备

## 模型下载状态
- **状态**: 下载中（截至检查时 ~4.5GB/~14GB）
- **路径**: `/root/autodl-tmp/.hf_cache/pythia-6.9b-local/`
- **方式**: `huggingface-cli download` + hf_transfer, hf-mirror.com
- **PID**: 327619, 预计 ~10-15 分钟完成
- **下载完成后验证**:
  ```bash
  du -sh /root/autodl-tmp/.hf_cache/pythia-6.9b-local/
  ls /root/autodl-tmp/.hf_cache/pythia-6.9b-local/*.safetensors
  # 应有 model-00001-of-00002.safetensors + model-00002-of-00002.safetensors, 总计 ~14GB
  ```

## 硬件环境
- **GPU**: 2x NVIDIA RTX PRO 6000 Blackwell Server Edition, 98GB VRAM each
- **Compute Capability**: 12.0 (支持 bf16/fp16)
- **磁盘**: 250GB total, 95GB free (`/root/autodl-tmp/`)
- **当前占用**: GPU 0 运行 gpt2-medium 训练, GPU 1 运行 pythia-1.4b s43 训练

## 显存预估

### 问题: 标准训练 OOM
Pythia-6.9B (6.9B params) FP32 + FP16 AMP 训练的峰值显存:
| 组件 | 大小 |
|------|------|
| FP32 参数 | 28 GB |
| FP32 梯度 | 28 GB |
| FP32 Adam momentum | 28 GB |
| FP32 Adam variance | 28 GB |
| **合计 (不含 activations)** | **~112 GB** |

单 GPU 98GB, OOM.

### 解决方案: gradient_checkpointing + 8-bit Adam
| 组件 | 大小 |
|------|------|
| FP32 参数 | 28 GB |
| FP32 梯度 | 28 GB |
| 8-bit Adam momentum | 7 GB |
| 8-bit Adam variance | 7 GB |
| Activations (gradient_checkpointing) | ~2 GB |
| **合计** | **~72 GB** |

98GB GPU 有 26GB 余量, 安全.

### 推荐配置
- `--gradient_checkpointing` (已添加到脚本)
- `--optim adamw_bnb_8bit` (已添加到脚本, bitsandbytes 0.49.2 已安装)
- `--batch_size 4` (与 1.4B 实验一致)
- `--gen_batch_size 4` (生成时 KV cache ~3GB, 总 ~31GB, 安全)

### 生成阶段显存 (gen_batch_size=4)
| 组件 | 大小 |
|------|------|
| FP32 模型 | 28 GB |
| KV cache (4 batch, 768 seq, 32 layers) | ~3 GB |
| **合计** | **~31 GB** |

## 脚本兼容性
- **兼容**, 已修改 `iterative_train.py` 添加:
  - `--gradient_checkpointing` flag (line 71)
  - `--optim` arg, default="adamw_torch" (line 73)
  - 传入 `TrainingArguments` (lines 164-165)
  - 备份: `iterative_train.py.bak`
- Pythia-6.9B 使用 GPT-NeoX tokenizer, 与 410M/1.4B 相同, 无需特殊处理
- 无 model-specific 分支逻辑

### 磁盘空间注意事项
- 6.9B FP32 checkpoint: ~28GB/gen
- 10 gen 全保存 = ~308GB, 远超 95GB 可用
- **策略**: 训练过程中手动删除旧 checkpoint (保留最近 2 个 gen), 或训练后清理
- 每个实验实际占用: ~56GB (2 个 checkpoint) + synthetic_data (~2GB) + metrics (~1MB) ≈ ~58GB
- 可依次运行实验, 完成后只保留 all_metrics.json 和最后一个 checkpoint

## 4 组实验配置

### Phase 1: α=1.0, 两个 seed 并行 (各占 1 个 GPU)

**实验 1: pythia-6.9b, WikiText, α=1.0, seed=42, cuda:0**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export TRANSFORMERS_OFFLINE=1 && \
source /root/miniconda3/etc/profile.d/conda.sh && \
conda activate base && \
CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python -u iterative_train.py \
  --model_name /root/autodl-tmp/.hf_cache/pythia-6.9b-local \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 1.0 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 4 \
  --gen_batch_size 4 \
  --gradient_checkpointing \
  --optim adamw_bnb_8bit \
  --seed 42 \
  --output_dir results/generalize/pythia69b_wiki_a100_s42
```

**实验 2: pythia-6.9b, WikiText, α=1.0, seed=43, cuda:1**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export TRANSFORMERS_OFFLINE=1 && \
source /root/miniconda3/etc/profile.d/conda.sh && \
conda activate base && \
CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 python -u iterative_train.py \
  --model_name /root/autodl-tmp/.hf_cache/pythia-6.9b-local \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 1.0 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 4 \
  --gen_batch_size 4 \
  --gradient_checkpointing \
  --optim adamw_bnb_8bit \
  --seed 43 \
  --output_dir results/generalize/pythia69b_wiki_a100_s43
```

### Phase 2: 完成 Phase 1 后

**实验 3: pythia-6.9b, WikiText, α=0.75, seed=42, cuda:0**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export TRANSFORMERS_OFFLINE=1 && \
source /root/miniconda3/etc/profile.d/conda.sh && \
conda activate base && \
CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python -u iterative_train.py \
  --model_name /root/autodl-tmp/.hf_cache/pythia-6.9b-local \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.75 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 4 \
  --gen_batch_size 4 \
  --gradient_checkpointing \
  --optim adamw_bnb_8bit \
  --seed 42 \
  --output_dir results/generalize/pythia69b_wiki_a075_s42
```

**实验 4: pythia-6.9b, C4, α=1.0, seed=42, cuda:1**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export TRANSFORMERS_OFFLINE=1 && \
source /root/miniconda3/etc/profile.d/conda.sh && \
conda activate base && \
CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 python -u iterative_train.py \
  --model_name /root/autodl-tmp/.hf_cache/pythia-6.9b-local \
  --data_dir data/c4_5k \
  --synthetic_ratio 1.0 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 4 \
  --gen_batch_size 4 \
  --gradient_checkpointing \
  --optim adamw_bnb_8bit \
  --seed 42 \
  --output_dir results/generalize/pythia69b_c4_a100_s42
```

**数据目录确认**: `data/wikitext103_5k/` ✓, `data/c4_5k/` ✓

## 训练时间预估

### 参考基准: Pythia-1.4B
- 配置: batch_size=4, steps_per_gen=5000, max_length=512, fp16
- 每 gen (含 generation + training + metrics): ~36 min
- 训练速度: ~2.3 it/s (推算)
- 10 gen 总时间: ~6h

### Pythia-6.9B 预估
- 模型参数: ~5x of 1.4B
- gradient_checkpointing 开销: ~30% (重计算前向激活)
- 8-bit optimizer 开销: 可忽略
- 预估每 step 速度: ~5 * 1.3 = 6.5x slower than 1.4B → ~0.35 it/s
- 每 gen 训练: 5000 / 0.35 / 60 ≈ 238 min
- 每 gen generation (gen_batch_size=4): ~20-30 min (6.9B 生成较慢)
- 每 gen metrics: ~5-10 min
- **每 gen 总计: ~4.5-5h**
- **10 gen 总计: ~45-50h per experiment**
- **Phase 1 (2 experiments parallel): ~45-50h**
- **Phase 2 (2 experiments parallel): ~45-50h**

### 注意
- 以上基于参数量线性推算 + gradient_checkpointing 开销, 实际可能因 Blackwell GPU 优化而更快
- 建议先跑 1 个 gen 测量实际速度后再调整预估
- 如果 batch_size=4 OOM, 降到 batch_size=2 + gradient_accumulation_steps=2 (脚本暂不支持此参数, 需额外添加)

## 前置条件
1. ✅ Tokenizer 下载完成
2. ⏳ 模型权重下载中 (PID 327619)
3. ✅ 脚本已修改 (gradient_checkpointing + optim)
4. ⏳ 等待当前 GPU 训练完成 (gpt2m on GPU 0, pythia-1.4b s43 on GPU 1)
5. ⚠️ 磁盘空间需管理: 训练过程中定期清理旧 checkpoint
