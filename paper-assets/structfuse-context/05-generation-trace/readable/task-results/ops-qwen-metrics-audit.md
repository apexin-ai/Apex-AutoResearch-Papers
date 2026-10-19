# ops qwen metrics audit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen_metrics_audit_20260516T025804_result.json`
- **Structured JSON:** [`0d39328e58c55dfd5c59.json`](../../sessions/0d/0d39328e58c55dfd5c59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部日志已读完。以下是完整结果。

---

## 核查结论

### 差异根因

**不是 pool_size 差异。** 所有 in-training eval 使用相同的 pool = 8（1 pos + 7 neg），`R@10=1.0` 处处为 1 即可确认。

差异来源：**ROADMAP 记的是 best_by_recall_at_1 checkpoint 对应的 eval step 值，SSH 读到的是 `[Final eval]`（early-stop 后的 final model 值）。** 两者是不同 checkpoint 的 R@1。

### 完整指标表（in-training eval, pool=8）

所有数据来源：`/root/runs/m2_full_qwen/&lt;subrun>.log`

#### random_s42

| eval step | val_loss | R@1 | R@5 | 备注 |
|-----------|----------|------|------|------|
| 500 | 0.4869 | 0.5332 | 0.9540 | |
| 1000 | **0.4651** | **0.5527** | 0.9594 | best val_loss + best R@1 |
| 1500 | 0.5365 | 0.5228 | 0.9550 | |
| 2000 | 0.5162 | 0.5228 | 0.9544 | |
| 2500 | 0.5264 | 0.5268 | 0.9564 | |
| 3000 | 0.5406 | 0.5356 | 0.9493 | |
| 3500 | 0.5601 | 0.5336 | 0.9493 | |
| 4000 | 0.5510 | 0.5346 | 0.9440 | |
| Final | 0.5456 | 0.5503 | 0.9463 | 跑完全部 3 epochs |

#### random_s43

| eval step | val_loss | R@1 | R@5 | 备注 |
|-----------|----------|------|------|------|
| 500 | **0.4476** | 0.5357 | 0.9699 | best val_loss |
| 1000 | 0.4638 | 0.5285 | 0.9672 | |
| 1500 | 0.5477 | **0.5554** | 0.9545 | best R@1 |
| Final | 0.5434 | 0.5501 | 0.9584 | early stop @1500 |

#### random_s44

| eval step | val_loss | R@1 | R@5 | 备注 |
|-----------|----------|------|------|------|
| 500 | **0.4252** | **0.6009** | 0.9583 | best val_loss + best R@1 |
| 1000 | 0.4695 | 0.5638 | 0.9524 | |
| 1500 | 0.4918 | 0.5592 | 0.9504 | |
| Final | 0.4943 | 0.5542 | 0.9514 | early stop @1500 |

**ROADMAP=0.6009 是 eval@500 值，SSH=0.5542 是 Final eval 值。** 差 4.67pp 是同一模型不同 training step 的退化，不是评估方法差异。

#### embedding_distance_s43

| eval step | val_loss | R@1 | R@5 | 备注 |
|-----------|----------|------|------|------|
| 500 | **0.4541** | 0.5446 | 0.9666 | best val_loss |
| 1000 | 0.4709 | 0.5390 | 0.9656 | |
| 1500 | 0.4926 | **0.5606** | 0.9630 | best R@1 |
| Final | 0.4876 | 0.5655 | 0.9663 | early stop @1500 |

#### embedding_distance_s44

| eval step | val_loss | R@1 | R@5 | 备注 |
|-----------|----------|------|------|------|
| 500 | 0.4403 | **0.5942** | 0.9563 | best R@1 |
| 1000 | **0.4341** | 0.5813 | 0.9643 | best val_loss |
| 1500 | 0.5256 | 0.5473 | 0.9421 | |
| 2000 | 0.5182 | 0.5390 | 0.9468 | |
| Final | 0.5123 | 0.5470 | 0.9481 | early stop @2000 |

**ROADMAP=0.5942 是 eval@500 值，SSH=0.5470 是 Final eval 值。** 同样是不同 step 的差异。

#### dataflow_aware_s43

| eval step | val_loss | R@1 | R@5 | 备注 |
|-----------|----------|------|------|------|
| 500 | **0.4617** | 0.5495 | 0.9728 | best val_loss |
| 1000 | 0.4984 | 0.5174 | 0.9581 | |
| 1500 | 0.5186 | **0.5541** | 0.9564 | best R@1 |
| Final | 0.5137 | 0.5564 | 0.9590 | early stop @1500 |

#### dataflow_aware_s44

**仍在训练**（刚启动 epoch 1，尚无 eval 输出）。

### ROADMAP 对照

| subrun | ROADMAP R@1 | 来源 | Final eval R@1 | 差值 |
|--------|-------------|------|----------------|------|
| random_s42 | 0.5527 | eval@1000 (best R@1) | 0.5503 | -0.24pp |
| random_s43 | 0.5554 | eval@1500 (best R@1) | 0.5501 | -0.53pp |
| random_s44 | 0.6009 | eval@500 (best R@1) | 0.5542 | **-4.67pp** |
| embed_s43 | 0.5606 | eval@1500 (best R@1) | 0.5655 | +0.49pp |
| embed_s44 | 0.5942 | eval@500 (best R@1) | 0.5470 | **-4.72pp** |
| dataflow_s43 | — | 0.5541 (best R@1) | 0.5564 | +0.23pp |

### 关于 pool_size

- **in-training eval (上表所有值)**: pool = 8（1 pos + 7 neg）
- **eval_p2b.py**: pool = 25（全部 neg_candidates），尚未对 m2_full_qwen 跑过
- **eval_p2b_pooled.py / run_eval_p50.sh**: pool = 50，尚未对 m2_full_qwen 跑过
- **`/root/autodl-tmp/structfuse/eval_results_p50/`**: 不存在

**目前没有 pool=20 或 pool=50 的 eval 结果。** 所有现有 R@1 数字都来自 pool=8 的 in-training eval。

---
