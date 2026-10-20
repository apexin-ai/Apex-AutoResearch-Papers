# Generalization 实验准备报告

## 1. 环境状态

| 资源 | 状态 | 详情 |
|------|------|------|
| C4 数据集 | **已就绪** | `data/c4_5k/` — train:4500, eval:500, prompts:500 |
| GPT-2-medium | **已缓存** | 355M params, vocab 50257, cache: `/root/autodl-tmp/.hf_cache/models--gpt2-medium/` |
| iterative_train.py | **兼容** | 已支持 `--model_name` 和 `--data_dir` 参数，无需修改 |

## 2. 脚本兼容性

`iterative_train.py` 完全参数化：
- `--model_name`: 默认 `EleutherAI/pythia-410m`，可传 `gpt2-medium`
- `--data_dir`: 默认 `data/wikitext103`，可传 `data/c4_5k`
- `--dataset`: 仅用于日志标识
- `--synthetic_ratio`: 即 α 参数
- `tokenizer.pad_token = tokenizer.eos_token` 已处理 GPT-2 无 pad_token 的情况
- `metrics.py` 完全模型无关

**不需要创建新脚本。**

## 3. 数据量差异警告

| 数据集 | train 样本数 | train 大小 | 每代覆盖率 (steps=5000, bs=4) |
|--------|-------------|-----------|---------------------------|
| wikitext103_5k | ~1,801,350 (全 WikiText-103 train) | 3.3GB | ~1.1% |
| c4_5k | 4,500 | 11MB | ~444% (每样本被看 4.4 次) |

C4 train 集远小于 WikiText。每代训练会多次遍历 C4，可能导致更严重的过拟合效应（与 collapse 信号混淆）。如需公平对比，可考虑增大 C4 至 ~20k 样本（匹配每代 20k 次访问），或减少 `steps_per_gen`。

## 4. 训练命令

环境前缀（所有命令共用）：
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export HF_ENDPOINT=https://hf-mirror.com && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

### 实验 A: C4 + Pythia-410M（控制变量：只换数据集）

**A1: α=0.25**
```bash
CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python -u iterative_train.py \
    --model_name EleutherAI/pythia-410m \
    --data_dir data/c4_5k \
    --dataset c4-en \
    --synthetic_ratio 0.25 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/generalization/c4_pythia_a025_s42 \
    --seed 42
```

**A2: α=1.0**
```bash
CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python -u iterative_train.py \
    --model_name EleutherAI/pythia-410m \
    --data_dir data/c4_5k \
    --dataset c4-en \
    --synthetic_ratio 1.0 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/generalization/c4_pythia_a100_s42 \
    --seed 42
```

### 实验 B: WikiText + GPT-2-medium（控制变量：只换模型）

**B1: α=0.25**
```bash
CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python -u iterative_train.py \
    --model_name gpt2-medium \
    --data_dir data/wikitext103_5k \
    --dataset wikitext-103-v1 \
    --synthetic_ratio 0.25 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/generalization/wiki_gpt2m_a025_s42 \
    --seed 42
```

**B2: α=1.0**
```bash
CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python -u iterative_train.py \
    --model_name gpt2-medium \
    --data_dir data/wikitext103_5k \
    --dataset wikitext-103-v1 \
    --synthetic_ratio 1.0 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --output_dir results/generalization/wiki_gpt2m_a100_s42 \
    --seed 42
```

## 5. 时间估算

基于 a000_s42 (Pythia-410M, WikiText, 10gen×5000steps) 的实际运行时间：**~4.5 小时**

| 实验 | 模型 | 预估时间 | 说明 |
|------|------|---------|------|
| A1: C4+Pythia α=0.25 | Pythia-410M (410M) | ~4.5h | 同模型，数据更小可能略快 |
| A2: C4+Pythia α=1.0 | Pythia-410M (410M) | ~4h | α=1.0 无 mix，generation 更快 |
| B1: Wiki+GPT2m α=0.25 | GPT-2-medium (355M) | ~4h | 模型更小，训练速度略快 |
| B2: Wiki+GPT2m α=1.0 | GPT-2-medium (355M) | ~3.5h | 模型更小 + α=1.0 |

**串行总计：~16h（4 个实验），或 ~8h（Director 选 2 个实验）**

## 6. 推荐执行顺序

Director 要求跑 2 组实验（α=0.25 + α=1.0 × 1 seed），串行在 cuda:0。

**推荐先跑 B 组（WikiText + GPT-2-medium）**：
1. B1 (α=0.25) → B2 (α=1.0)：先跑 GPT-2 因为与现有 Pythia baseline 直接可比（同数据），且模型更小更快
2. 如有时间再跑 A 组

**替代顺序**（如果 Director 优先验证数据集影响）：
1. A1 (α=0.25) → A2 (α=1.0)：先跑 C4+Pythia 因为保持模型不变，单独看数据集影响

## 7. 注意事项

- GPT-2-medium tokenizer 无 pad_token，脚本已处理（`pad_token = eos_token`）
- 训练时 `report_to="none"`，不需要 wandb
- 清理临时文件：`rm /tmp/c4_shard0.json.gz /tmp/c4_prep.log /tmp/gpt2_dl.log`
- C4 数据来源：allenai/c4 en split 第一个 json.gz 分片，过滤 ≥50 词
