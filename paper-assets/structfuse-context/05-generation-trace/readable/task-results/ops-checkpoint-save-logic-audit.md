# ops checkpoint save logic audit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_checkpoint_save_logic_audit_20260516T030841_result.json`
- **Structured JSON:** [`7240117c67c1c008694f.json`](../../sessions/72/7240117c67c1c008694f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据齐全。下面是完整分析。

---

## Checkpoint 保存逻辑

- **best_by_val_loss**: 按 `cur_val_loss < best_val_loss` 保存（`train.py:432`）
- **best_by_recall_at_1**: 按 `cur_recall_at_1 > best_recall_at_1` 保存（`train.py:450`）
- **双 checkpoint**: yes，两个条件独立判断，各存一份
- **final**: 训练循环结束后无条件保存到 `output_dir / "final"`（`train.py:477`），**不更新 best checkpoint**

## Final Eval 分析

- **触发位置**: `train.py:469`，在训练循环（包括 early stopping）结束后执行
- **模型状态**: 与 eval@1500 **完全相同**

证据链：
1. eval@1500 时 `no_improve_count` 达到 2（patience=2），触发 early stopping（`train.py:462-464`）
2. early stop 在 eval@1500 的检查逻辑 **末尾** 触发，即：先完成 best_by_recall_at_1 更新 → 再判断 patience → `break`
3. 外层 epoch 循环也 `break`（`train.py:368`）
4. Final eval 直接在 step 1500 模型状态上运行，**没有额外训练步**

日志佐证：
```
eval@1500: val_loss=0.4926, R@1=0.5606  → New best R@1=0.5606
Early stopping triggered at step 1500, best val_loss=0.4541 at step 500
[Final eval] val_loss=0.4876, R@1=0.5655
```

## Eval 确定性

- **negatives 来源**: **动态随机采样**
  - `val_ds._negatives` 从未被填充（`refresh_negatives` 仅对 `train_ds` 调用）
  - 每次 `__getitem__` 走 fallback 路径：`random.shuffle(fallback)`（`train.py:109-110`）
  - 用的是全局 `random` 模块，状态在训练过程中持续变化
- **dataloader shuffle**: no（`val_loader` 的 `shuffle=False`，`train.py:322`）
- **结论**: 同一模型两次 eval **不会**给出相同 R@1，因为每次抽的 negative 不一样

## 结论

**embed_s43 final R@1 > best R@1 的原因**：eval 非确定性（random negative sampling）。

- final eval 和 eval@1500 跑的是**同一组模型权重**（step 1500 early stop 后直接 final eval）
- R@1 差异仅 0.49pp（0.5655 vs 0.5606），在 negative 随机采样的噪声范围内
- val_loss 差异也佐证了这一点：0.4876 vs 0.4926，同一模型两次 eval 给出不同 loss

**embed_s44 对比**：final R@1=0.5470 < best R@1=0.5942，差距 4.7pp，远超噪声，因为 s44 的 early stop 发生在 step 2000，模型确实比 step 500 差了很多。

**是否影响模型选择**：**不影响**。best_by_recall_at_1 保存的就是 step 1500 的权重，和 final eval 用的权重完全一致。表面上的 "final > best" 只是 eval 噪声。

**代码层面的隐患**：
1. `val_ds` 的 negative 采样用了 `random.shuffle` 且无 seed 重置，导致每次 eval 结果不可复现 → 建议 eval 时固定 seed 或预写死 negatives
2. final eval 不更新 best checkpoint → 如果训练在非 eval step 停止（如达到 max epoch），可能漏掉更优模型。当前 early stopping 恰好在 eval step 触发所以没问题

---
