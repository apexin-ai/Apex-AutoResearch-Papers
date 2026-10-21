# Repo-Level 8B Training Plan

## 1. westd-48478 环境状况

**SSH 认证失败。** 使用 account=root 连接 westd-48478 时，detect_image 和 ssh_execute 均返回 "Authentication failed"。无法探测该服务器环境。

**需要 Director 介入：** 确认 westd-48478 的 SSH 配置/密钥是否正确，或提供替代服务器。

## 2. 4B Repo-Level 脚本分析

两个脚本均已支持 `--model_name` 参数，切换到 8B 只需改 CLI 参数。

### train_repo_verifier.py (CLS) 默认配置
| 参数 | 4B 默认值 |
|------|-----------|
| model_name | `/root/.cache/huggingface/hub/Qwen/Qwen3-4B` |
| output_dir | `/root/autodl-tmp/checkpoints_repo_cls/` |
| batch_size | 2 |
| grad_accumulation | 16 |
| max_seq_length | 2048 |
| lr | 2e-4 |
| epochs | 3 |
| lora_rank | 16 |
| lora_alpha | 32 |
| lora_dropout | 0.05 |
| target_modules | q_proj, k_proj, v_proj, o_proj |
| device | cuda:2 |

### train_repo_cwm.py (CWM) 默认配置
与 CLS 相同，仅 output_dir=`/root/autodl-tmp/checkpoints_repo_cwm/`，device=`cuda:3`。

### 数据规模
- train: 70,748 samples
- val: 9,335 samples
- test: 9,784 samples

## 3. 8B 训练命令

### CLS (Verifier)
```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
python train_repo_verifier.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --output_dir /root/autodl-tmp/checkpoints_repo_cls8b/ \
  --run_name repo-cls-qwen3-8b-lora \
  --batch_size 1 \
  --grad_accumulation 32 \
  --lr 1e-4 \
  --device cuda:0
```

### CWM (Code World Model)
```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
python train_repo_cwm.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm8b/ \
  --run_name repo-cwm-qwen3-8b-lora \
  --batch_size 1 \
  --grad_accumulation 32 \
  --lr 1e-4 \
  --device cuda:1
```

### 4B → 8B 调整说明
| 参数 | 4B | 8B | 原因 |
|------|-----|-----|------|
| batch_size | 2 | 1 | 8B 显存约 2× 4B |
| grad_accumulation | 16 | 32 | 维持 effective batch_size=32 |
| lr | 2e-4 | 1e-4 | 8B 通常需要更低 lr |
| LoRA (r/alpha/dropout) | 16/32/0.05 | 16/32/0.05 | 不变（函数级 8B 验证过） |
| PYTORCH_CUDA_ALLOC_CONF | 无 | expandable_segments:True | 防 OOM 碎片 |

## 4. 显存/性能预估

### 显存 (RTX 5090 32GB)
- Qwen3-8B bf16 权重: ~16GB
- LoRA adapter: ~60MB
- Gradient checkpointing 激活显存: ~4-8GB (seq_len=2048, batch=1)
- 优化器状态 (AdamW, LoRA only): ~240MB
- **总计约 21-25GB，32GB 应该够用**

### 训练时间预估
- 函数级 8B 在 4×5090 上单卡训练约 2-3 小时/epoch
- Repo-level 数据量（70K samples）与函数级相当
- 预计 3 epochs ≈ 6-9 小时/任务

### 可并行性
CLS 和 CWM 可在不同 GPU 上并行训练（如上命令分别用 cuda:0 和 cuda:1）。

## 5. 前置条件

1. **[BLOCKER] 修复 westd-48478 SSH 认证** — 当前无法连接
2. **同步代码到 westd-48478** — `train_repo_verifier.py`, `train_repo_cwm.py`, 数据目录
3. **确认 Qwen3-8B 模型在 westd-48478 上的路径** — 可能需要下载（~16GB），或从 seetacloud 的 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` 传输
4. **确认依赖包** — torch, transformers, peft, datasets, wandb, flash-attn

## 6. 风险点

| 风险 | 影响 | 缓解方案 |
|------|------|----------|
| westd-48478 SSH 认证失败 | 无法执行任何操作 | 需 Director 检查 SSH 配置 |
| 8B batch_size=1 仍 OOM | 无法训练 | 降 max_seq_length 到 1536 或用 QLoRA (4bit) |
| Qwen3-8B 未缓存在 westd-48478 | 需要额外下载时间 | 提前下载或从 seetacloud rsync |
| 数据目录不在 westd-48478 | 训练无法启动 | 需要 rsync 数据 |

## 7. 已有函数级 8B Checkpoints（seetacloud，仅供参考）

| 目录 | Adapter 大小 | 日期 |
|------|-------------|------|
| checkpoints_cls8b/best/ | 61MB | 2026-05-12 |
| checkpoints_cls8b_seed123/best/ | 61MB | 2026-05-12 |
| checkpoints_cwm8b/best/ | 61MB | 2026-05-12 |
| checkpoints_cwm8b_seed123/best/ | 61MB | 2026-05-12 |
| checkpoints_cwm8b_seed456/best/ | 61MB | 2026-05-12 |

这些是**函数级** 8B checkpoints，repo-level 需从 base model 重新训练。LoRA 配置相同（r=16, alpha=32, q/k/v/o_proj）。
