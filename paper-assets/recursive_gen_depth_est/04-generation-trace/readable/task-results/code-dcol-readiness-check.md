# code dcol readiness check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcol_readiness_check_20260514T193655_result.json`
- **Structured JSON:** [`893359ecd4f37462d18c.json`](../../sessions/89/893359ecd4f37462d18c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全通过。

## 汇报

### 代码完成度：100%

| 文件 | 行数 | 状态 |
|------|------|------|
| `src/dcol_trainer.py` | 526 | ✅ 完整：模型定义 + loss + 训练循环 + argparse + dry_run |
| `src/dcol_dataset.py` | ~200 | ✅ 完整：数据加载 + DCOLDataset + ContrastiveBatchSampler |
| `src/dcol_eval.py` | ~200 | ✅ 完整：pairwise AUC + confusion matrix + per-model/strategy |
| `scripts/run_dcol_training.sh` | ~100 | ✅ 完整：环境设置 + 参数传递 + 训练后自动 eval |

### 核心组件
- **模型**: `DCOLModel` = DeBERTa-v3-large backbone + `OrdinalContrastiveHead`（CLS + 19-dim features → L2-normalized 128-d embedding）+ linear classifier
- **Loss**: `contrastive_ordinal_loss` — 完整 N-pair formulation，`L = CE + λ·CL`，CL 用 margin matrix 实现 attractive + repulsive
- **Learnable margins**: `LearnableOrdinalMargins` — K-1 个 softplus 参数，cumsum 构建 effective margin matrix，支持 per-strategy margins（3 个策略：default/temp09/topk50）
- **初始化**: 从 MVP RF AUC 反推，softplus(raw) ≈ [0.50, 0.25, 0.20]

### Dry-run 结果
- `python src/dcol_trainer.py --dry_run --model_path /root/autodl-tmp/models/deberta-v3-large --features_path data/features_all.jsonl --gpu 1` ✅
- 数据加载正常：118,519 条（7 个模型×策略组合，depth 0-3）
- 模型加载正常：434M 参数，全部可训练
- 前向传播 + 反向传播正常，margins 在训练中有梯度更新
- 1 epoch × 200 samples 耗时 ~6s

### 数据与模型
- `/root/autodl-tmp/models/deberta-v3-large/` ✅
- `data/depth_{0..3}.jsonl` ✅（45k/28.5k/25k/20k）
- `data/features_all.jsonl` ✅

### 启动命令
```bash
cd /root/autodl-tmp/recursive_gen_depth_est
bash scripts/run_dcol_training.sh --gpu <0或1>
```

### 无 bug，无缺失组件。GPU 释放后可直接启动训练。

---
