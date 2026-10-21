# ssh verify dcol readiness

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_dcol_readiness_20260514T200618_result.json`
- **Structured JSON:** [`1ea0844793d41faa81b7.json`](../../sessions/1e/1ea0844793d41faa81b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查通过。

## DCOL 训练就绪状态：**DCOL READY**

| 检查项 | 状态 |
|--------|------|
| 代码文件 | `src/dcol_trainer.py` + `src/dcol_dataset.py` + `src/dcol_feature_mlp.py` + `src/dcol_eval.py` + `scripts/run_dcol_training.sh` |
| 语法检查 | SYNTAX_OK (3 个核心文件) |
| 模型 | DeBERTa-v3-large 已缓存在 `/root/autodl-tmp/models/deberta-v3-large` (868MB safetensors) |
| 依赖 | torch=2.10.0+cu128, transformers=5.8.1, cuda=True, 2 GPUs |
| 训练数据 | `data/depth_{0..3}.jsonl` 全部就绪 + `data/features_all.jsonl` (13.7MB 19维特征) |
| 多模型数据 | gpt2xl、olmo、pythia_temp09、pythia_topk50 子目录存在 |
| Loss | Contrastive Ordinal Loss with learnable margins (N-pair, 非 uniform 初始化 from MVP AUC) |
| 输出 | 4 类深度分类，19 维统计特征 + [CLS] embedding |

### 架构确认
- **dcol_trainer.py**: DeBERTa-v3-large backbone + OrdinalContrastiveHead (19-dim feature projector → 128-dim contrastive embedding) + LearnableOrdinalMargins + 4-class classifier。三组学习率 (backbone/head/margins)。
- **dcol_feature_mlp.py**: 纯 MLP 版本（无 DeBERTa），19→128→64→32 contrastive space + 4-class head。独立 baseline。

### 启动命令

```bash
# DeBERTa DCOL (主实验，cuda:0)
CUDA_VISIBLE_DEVICES=0 bash scripts/run_dcol_training.sh

# 或直接 python:
CUDA_VISIBLE_DEVICES=0 python src/dcol_trainer.py \
  --data_dir data/ \
  --model_path /root/autodl-tmp/models/deberta-v3-large \
  --features_path data/features_all.jsonl \
  --output_dir checkpoints/dcol/ \
  --batch_size 32 --epochs 10 --lr 2e-5 --margin_lr 1e-3 --cl_weight 0.5
```

---
