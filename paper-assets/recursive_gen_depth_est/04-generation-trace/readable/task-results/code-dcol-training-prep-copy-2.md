# code dcol training prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcol_training_prep_20260514T160308_result.json`
- **Structured JSON:** [`e93b02eacd0803f62a24.json`](../../sessions/e9/e93b02eacd0803f62a24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件总结：

**产出 (1199 行代码)**

| 文件 | 行数 | 功能 |
|------|------|------|
| `src/dcol_dataset.py` | 239 | 多 model/strategy 数据加载、19维特征 log1p 预处理、stratified split、ContrastiveBatchSampler（每 batch 各深度等量采样） |
| `src/dcol_trainer.py` | 526 | DCOLModel (DeBERTa + BatchNorm feature projector + ordinal contrastive head)、累积和 margin 矩阵构建、strategy-aware learnable margins、multi-margin contrastive ordinal loss + CE loss、AdamW 三组 LR (backbone 2e-5 / head 2e-4 / margins 1e-3)、cosine warmup、early stopping |
| `src/dcol_eval.py` | 293 | pairwise AUC、per-model/per-strategy 分组评估、confusion matrix 可视化、RF baseline 对比 |
| `scripts/run_dcol_training.sh` | 141 | 端到端 pipeline（环境检测 → 模型下载 → 训练 → 评估），支持 `--dry_run` 和全部超参数覆写 |

**调试过程中修复的 3 个问题**

1. **fp16 overflow** — 特征值极端（var_ppl ~ 1e11）导致 autocast fp16 溢出 → 加 `log1p` 变换 + `BatchNorm1d`
2. **GradScaler 不兼容** — 移除 GradScaler，改用 autocast forward + fp32 loss 计算
3. **AdamW NaN** — 默认 `eps=1e-8` 在 DeBERTa multi-group optimizer 下产生 NaN → 改为 `eps=1e-6`

**Dry-run 验证通过**：200 样本 × 1 epoch，loss 数值稳定 (1.65)，margins 正常学习。DeBERTa-v3-large 未缓存，正式训练时需下载（脚本已内置自动下载逻辑）。

---
