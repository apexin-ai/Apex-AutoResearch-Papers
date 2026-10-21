# ssh dcol cleanup and verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dcol_cleanup_and_verify_20260514T193350_result.json`
- **Structured JSON:** [`e48d34f841f6cd2eef11.json`](../../sessions/e4/e48d34f841f6cd2eef11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告如下：

---

### 1. Rename 状态

`scripts/dcol_train.py` → `dcol_train_standalone_deprecated.py` 在服务器和本地**均已完成**（之前已重命名过）。

注意：服务器 `src/dcol_train.py` 仍存在——这是**另一个版本**（feature-based MLP，非 DeBERTa），与正式的 `src/dcol_trainer.py` 不同，可能也需要清理。

### 2. `scripts/run_dcol_training.sh` 完整训练命令

```bash
python src/dcol_trainer.py \
    --data_dir "$DATA_DIR" \
    --model_path "$MODEL_PATH" \            # 默认 /root/autodl-tmp/models/deberta-v3-large
    --output_dir "$OUTPUT_DIR" \            # 默认 checkpoints/dcol/
    --log_dir "$LOG_DIR" \
    --batch_size 32 \
    --epochs 10 \
    --lr 2e-5 \
    --margin_lr 1e-3 \
    --cl_weight 0.5 \
    --max_length 512 \
    --gpu 0 \
    --seed 42
```

训练完成后自动调用 `src/dcol_eval.py` 评估。模型路径默认指向 `/root/autodl-tmp/models/deberta-v3-large`，一致。

### 3. `src/dcol_trainer.py` 架构

| 组件 | 实现 |
|------|------|
| Backbone | DeBERTa-v3-large |
| Pooling | **[CLS] token**（`last_hidden_state[:, 0, :]`） |
| Contrastive head | [CLS](1024d) concat 19-dim feature projection(64d) → 256 → **128d L2-normalized** |
| Similarity | **Cosine**（embeddings 已 L2-normalize，直接 matmul） |
| Loss | CE + multi-margin contrastive ordinal loss（learnable margins via softplus） |
| Margins | 可学习，初始化自 MVP AUC: [0.50, 0.25, 0.20]，支持 per-strategy |

### 4. Pythia topk50 进度

**仍在运行**（`.done` 文件不存在）。当前进度：Step 4 Generate depth-2，正在加载 pythia-1.4b 模型。

### 5. 待确认

`src/dcol_train.py`（MLP-based feature-only 版本）是否也需要 rename 为 deprecated？它和 `dcol_trainer.py` 是两套独立架构。

---
