# ops m2 embed verify fix check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m2-embed-verify-fix-check_20260513T050843_result.json`
- **Structured JSON:** [`c3c00ecbba9d355229f8.json`](../../sessions/c3/c3c00ecbba9d355229f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

| 检查项 | 状态 | 详情 |
|--------|------|------|
| epochs = 2 | ❌ | wrapper 写的 `--num-epochs 3`，train.py 默认也是 3 |
| eval 每 500 步 | ✅ | `--eval-steps 500` 已设置 |
| early stopping (patience=3) | ❌ | **完全没有实现。** train.py 无 `--early-stop` / `--patience` 参数，训练循环只有 best_val_loss 保存逻辑，无 patience 计数器，不会提前终止 |
| recall@k fallback 修复 | ✅ | 第244行 `logits.topk(min(k, logits.size(1)), dim=1)` — 已修复，不再错误回退到 argmax |

### 缺失项详情

**1. epochs=3 而非 2** — `run_m2_embed_verify.sh` 第38行：
```bash
--num-epochs 3 \
```

**2. 无 early stopping** — train.py 第406-425行的 eval 分支仅保存 best checkpoint，无任何 patience / no_improve 计数逻辑：
```python
cur_val_loss = metrics["val_loss"]
if cur_val_loss < best_val_loss:
    # ... saves best checkpoint ...
    best_val_loss = cur_val_loss
# 没有 else 分支，没有计数器，没有 break
```

### 训练进度

刚刚启动，第一个 strategy（random）Epoch 1 刚开始加载，尚未完成任何 training step 的日志输出。现在停掉的代价最小。

---
