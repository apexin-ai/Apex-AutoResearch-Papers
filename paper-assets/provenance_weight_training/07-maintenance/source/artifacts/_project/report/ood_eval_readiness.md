# OOD Eval 环境就绪度检查

**检查时间**: 2026-05-19  
**服务器**: westd-41312

---

## 1. OOD Eval 数据集

| 数据集 | 状态 | 路径 | 样本数 | 大小 |
|--------|------|------|--------|------|
| OpenWebText | ✅ 就绪 | `/root/autodl-tmp/provenance_weight_training/data/eval_openwebtext.jsonl` | 5,000 | 25MB |
| Wikipedia | ✅ 就绪 | `/root/autodl-tmp/provenance_weight_training/data/eval_wikipedia.jsonl` | 5,000 | 71MB |

数据格式：JSONL，每行 `{"text": "..."}` 格式，已验证可被 `eval_perplexity.py` 读取。

## 2. FineWeb In-Distribution Eval 数据

| 数据集 | 状态 | 路径 | 样本数 | 大小 |
|--------|------|------|--------|------|
| FineWeb holdout | ✅ 就绪 | `/root/autodl-tmp/provenance_weight_training/data/human/eval_holdout.jsonl` | 67,823 | 238MB |

## 3. Eval 脚本

| 项目 | 状态 | 详情 |
|------|------|------|
| `eval_perplexity.py` | ✅ 就绪 | `/root/provenance_weight_training/eval_perplexity.py` |

参数说明：
- `--checkpoints`: checkpoint 路径列表（支持多个）
- `--data_path`: eval 数据文件路径
- `--max_docs`: 最大文档数（默认 5000）
- `--max_length`: 最大序列长度（默认 2048）
- `--output_path`: 结果输出 JSON 文件

评估方法：滑动窗口 PPL（stride = max_length/2），FP16 autocast。

## 4. Checkpoint 状态

| 实验 | 状态 | 路径 | 大小 |
|------|------|------|------|
| uniform_ood_seed123 | ✅ 完成 | `.../output/models/uniform_ood_seed123/final/` | 1.2GB |
| uniform_ood_seed456 | ✅ 完成 | `.../output/models/uniform_ood_seed456/final/` | ~1.2GB |
| adaptive_ood_seed123 | ⏳ 训练中 (step 5797/6103, ~95%) | `.../output/models/adaptive_ood_seed123/` | 无 final |
| adaptive_ood_seed456 | ⏳ 训练中 (step 5809/6103, ~95%) | `.../output/models/adaptive_ood_seed456/` | 无 final |

Uniform checkpoints 内容已验证：包含 `model.safetensors` (1.1GB)、`config.json`、`tokenizer.json`、`tokenizer_config.json`、`generation_config.json`、`training_args.bin`。

## 5. GPU 状态

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| cuda:0 | 98% | 45.6GB/97.9GB | adaptive_ood_seed123 训练 |
| cuda:1 | 100% | 45.6GB/97.9GB | adaptive_ood_seed456 训练 |
| cuda:2 | 0% | 空闲 | 可用于 eval |
| cuda:3 | 0% | 空闲 | 可用于 eval |

磁盘空间：25GB 可用（足够 eval 输出）。

## 6. 先前 w2 Eval 参考

w2_distribution_matching_eval 使用的配置：
- 模型：`adaptive_fix_seed42/final` vs `qwen06b_uniform_seed42_v2/final`
- 数据：FineWeb holdout (4.1M tokens), OpenWebText (6.8M tokens), Wikipedia (27M tokens)
- 参数：`--max_docs 5000 --max_length 2048`
- 指标：loss, perplexity, num_tokens
- 结论：negative（adaptive 在 OOD 上未显著优于 uniform）

## 7. OOD Eval 命令模板

训练完成后，在 conda base 环境下执行：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/provenance_weight_training

BASE=/root/autodl-tmp/provenance_weight_training

# --- Uniform seed123 ---
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
  --checkpoints $BASE/output/models/uniform_ood_seed123/final \
  --data_path $BASE/data/eval_openwebtext.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_uniform_seed123_openwebtext.json

CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
  --checkpoints $BASE/output/models/uniform_ood_seed123/final \
  --data_path $BASE/data/eval_wikipedia.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_uniform_seed123_wikipedia.json

CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
  --checkpoints $BASE/output/models/uniform_ood_seed123/final \
  --data_path $BASE/data/human/eval_holdout.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_uniform_seed123_fineweb.json

# --- Adaptive seed123 ---
CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py \
  --checkpoints $BASE/output/models/adaptive_ood_seed123/final \
  --data_path $BASE/data/eval_openwebtext.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_adaptive_seed123_openwebtext.json

CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py \
  --checkpoints $BASE/output/models/adaptive_ood_seed123/final \
  --data_path $BASE/data/eval_wikipedia.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_adaptive_seed123_wikipedia.json

CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py \
  --checkpoints $BASE/output/models/adaptive_ood_seed123/final \
  --data_path $BASE/data/human/eval_holdout.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_adaptive_seed123_fineweb.json

# seed456 同理，替换路径中的 seed123 → seed456
```

**优化建议**：可在 GPU 2 和 GPU 3 上并行跑 uniform 和 adaptive，利用脚本同时评估多个 checkpoint：

```bash
# 单次调用评估多个 checkpoint（同一数据集）
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
  --checkpoints \
    $BASE/output/models/uniform_ood_seed123/final \
    $BASE/output/models/uniform_ood_seed456/final \
  --data_path $BASE/data/eval_openwebtext.jsonl \
  --max_docs 5000 --max_length 2048 \
  --output_path $BASE/output/eval/ood_uniform_openwebtext.json
```

## 8. 缺失项清单

| 项目 | 状态 | 预计就绪时间 |
|------|------|-------------|
| adaptive_ood_seed123 checkpoint | ⏳ 训练中 95% | ~15-30 分钟 |
| adaptive_ood_seed456 checkpoint | ⏳ 训练中 95% | ~15-30 分钟 |

所有其他资源均已就绪。

## 9. 预估 OOD Eval 运行时间

基于 w2 eval 参考（Qwen3-0.6B, 5000 docs）：
- 每个 model × dataset 组合：~15-25 分钟（取决于 token 数）
- FineWeb holdout 文档更长，约 25 分钟
- OpenWebText 约 15 分钟
- Wikipedia 约 20 分钟

总计 12 个组合（4 models × 3 datasets）：
- **串行**：~4-5 小时
- **2 GPU 并行**（推荐）：~2-2.5 小时
- **4 GPU 并行**（训练完成后）：~1-1.5 小时

**推荐方案**：训练完成后 4 GPU 并行，GPU 0-3 各跑一个 seed×method 组合的 3 个数据集，约 1 小时完成全部评估。
