# code pythia69b config

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pythia69b_config_20260518T161616_result.json`
- **Structured JSON:** [`6fcf284782766378cb8f.json`](../../sessions/6f/6fcf284782766378cb8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. `iterative_train.py` patch（已应用到两台服务器）

4 处修改：

| 位置 | 修改 |
|------|------|
| `parse_args()` L74-75 | 新增 `--bf16` flag (`store_true`) |
| `TrainingArguments` L175-176 | `fp16=...` → `bf16=args.bf16, fp16=(not args.bf16) and torch.cuda.is_available()` |
| 模型加载（resume）L208 | 添加 `dtype=torch.bfloat16 if args.bf16 else None` |
| 模型加载（初始）L213 | 同上 |

注意：westd-19828 (transformers 4.57.6) 用 `torch_dtype`，westd-17855 (transformers 5.8.1) 用 `dtype`。

### 2. 启动脚本 `configs/launch_6.9b.sh`

已创建在 westd-17855。SEED 可通过第一个参数传入（默认 42）。

### 3. 显存估算

| 组件 | bf16 |
|------|------|
| 模型权重 | ~14 GB |
| AdamW (exp_avg + exp_avg_sq, bf16) | ~28 GB |
| 梯度 | ~14 GB |
| 激活值 (gradient_checkpointing, bs=4, seq=512) | ~5-15 GB |
| **总计** | **~61-71 GB / 98 GB** |

batch_size=4 应无 OOM 风险。`gen_batch_size` 从默认 16 降至 4（推理阶段也占显存）。

### 4. Checkpoint auto-cleanup

已内置于 `iterative_train.py`：gen >= 3 时删除 gen_{t-2} 的 checkpoint，保留 gen_0 + 最近 2 个。6.9B bf16 每个 checkpoint ~14GB，10 gen 最多同时占用 ~42GB（3 个 checkpoint）。

### 5. Dry-run 状态

模型正在从 hf-mirror.com 下载到 westd-17855（PID 7788，当前 ~520MB / ~13.5GB），预计 30 分钟后完成。BF16 支持已确认（`torch.cuda.is_bf16_supported() = True`）。

### 6. 完整启动命令（可直接用于 submit_training_job）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_ENDPOINT=https://hf-mirror.com && \
cd /root/autodl-tmp/distrib_canary_collapse && \
CUDA_VISIBLE_DEVICES=0 python iterative_train.py \
    --model_name EleutherAI/pythia-6.9b \
    --data_dir data/wikitext103_5k \
    --output_dir results/generalize/pythia69b_wiki_rtxpro_s42 \
    --num_generations 10 --steps_per_gen 5000 \
    --synthetic_ratio 1.0 --seed 42 \
    --batch_size 4 --max_length 512 --lr 5e-5 \
    --gen_batch_size 4 --gen_max_new_tokens 256 \
    --gradient_checkpointing --bf16 --optim adamw_torch
```

### 7. 额外发现

westd-17855 缺少 `HF_ENDPOINT=https://hf-mirror.com` 环境变量，已添加到 `.bashrc` 和启动脚本中。

---
