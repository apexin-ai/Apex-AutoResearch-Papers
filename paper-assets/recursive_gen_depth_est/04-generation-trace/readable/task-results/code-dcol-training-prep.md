# code dcol training prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcol_training_prep_20260514T165507_result.json`
- **Structured JSON:** [`638967ed68b7c0230871.json`](../../sessions/63/638967ed68b7c0230871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已写入 `artifacts/dcol_code/`：

| 文件 | 行数 | 功能 |
|------|------|------|
| `dcol_model.py` | 29 | DeBERTa-v3-large + MLP projection → 128-dim L2-normalized embedding |
| `dcol_loss.py` | 65 | N-pair contrastive ordinal loss，可学习 margin 矩阵 M[i][j] = \|i-j\| × base_margin |
| `dcol_dataset.py` | 58 | 读取 depth_X.jsonl，DepthCollator 做 tokenize + pad |
| `train_dcol.py` | 206 | 训练主循环：AdamW（encoder/head 分组 LR）、cosine warmup、FP16、kNN eval、W&B logging、checkpoint |
| `eval_dcol.py` | 138 | 加载 checkpoint → embedding 提取 → kNN accuracy + confusion matrix + pairwise AUC + t-SNE 可视化 |

关键设计点：
- **分组学习率**：projection head + margin 参数用 10× encoder LR
- **Margin 矩阵**可学习且初始化为序数距离，保证 depth 差大的 pair margin 更大
- **FP16 混合精度**通过 `torch.amp.autocast` + `GradScaler` 实现
- **评估**用 kNN 而非 linear probe，直接反映 embedding 空间质量

---
