# ops random s42 anomaly investigation

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_random_s42_anomaly_investigation_20260516T055642_result.json`
- **Structured JSON:** [`6d338bd2f156977c7708.json`](../../sessions/6d/6d338bd2f156977c7708.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整排查报告。

---

## 排查结果

### 1. Checkpoint MD5 对比

| Seed | best_by_val_loss | best_by_recall_at_1 | 相同？ |
|------|-----------------|---------------------|--------|
| s42 | `e082584c...` | `e082584c...` | **是** — 同一 step 1000 保存 |
| s43 | `701d1f7f...` | `b1a6714...` | **否** — step 500 vs step 1500 |
| s44 | `00554c5a...` | `00554c5a...` | **是** — 同一 step 500 保存 |

s42 两个 checkpoint 是同一文件，因此 pool=50 R@1 完全相同是预期行为。

### 2. 训练 Regime 差异（已确认）

| | s42 | s43 | s44 |
|---|-----|-----|-----|
| num_epochs | **3** | 2 | 2 |
| early_stopping_patience | **0 (禁用)** | 2 | 2 |
| 实际训练步数 | **4242 (3 full epochs)** | 1500 (early stop) | 1500 (early stop) |
| Best val_loss step | 1000 | 500 | 500 |
| Best R@1 step | 1000 | 1500 | 500 |
| warmup 步数 (ratio=0.1) | **424** | 283 | 283 |

### 3. s42 Val Loss 趋势 — 明确过拟合

| Step | val_loss | recall@1 | 备注 |
|------|----------|----------|------|
| 500 | 0.4869 | 0.5332 | 首次 eval，new best |
| **1000** | **0.4651** | **0.5527** | **best checkpoint 保存点** |
| 1500 | 0.5365 ↑ | 0.5228 ↓ | 开始恶化 |
| 2000 | 0.5162 | 0.5228 | |
| 2500 | 0.5264 | 0.5268 | |
| 3000 | 0.5406 | 0.5356 | |
| 3500 | 0.5601 | 0.5336 | |
| 4000 | 0.5510 | 0.5346 | |
| Final | 0.5456 | 0.5503 | |

step 1000 之后 val_loss 持续上升，连续 6 次 "not improved"。训练跑完了 3 个完整 epoch（18 小时），但最后 14 小时完全是浪费。

### 4. Best Metrics 对比

| | s42 | s43 | s44 |
|--|-----|-----|-----|
| Best val_loss | 0.4651 | 0.4476 | **0.4252** |
| Best val R@1 | 0.5527 | 0.5554 | **0.6009** |
| **Pool=50 R@1** | **0.2730** | **0.3138** | **0.3181** |

注意：val set 在不同 seed 间不同，所以 val 指标跨 seed 不直接可比。但 pool=50 是同一测试集上的结果。

### 5. Embed_s42 状态

`run_m2_s42_supplement.sh` 覆盖 `embedding_distance_s42` + `dataflow_aware_s42`，使用 D050 统一 regime：**`NUM_EPOCHS=2, early_stopping_patience=2`**。不会重蹈 s42 的覆辙。

### 6. 结论：anomaly 原因

**主因：LR schedule 差异导致最优 checkpoint 质量更差。**

3-epoch schedule（total_steps=4242）vs 2-epoch schedule（total_steps=2828）导致：
- warmup 更长（424 vs 283 步），模型在前 500 步有效训练更少
- step 500 时 s42 的 val_loss（0.4869）已经比 s43（0.4476）/ s44（0.4252）差
- 虽然 s42 在 step 1000 追回一些（0.4651），但仍未达到 s43/s44 step 500 的水平
- 即使保存了 best checkpoint，该 checkpoint 本身的质量就低于 s43/s44 的 best

**次因：不同 seed 的数据分割方差。** 但 s43/s44 间仅差 0.4pp，而 s42 差 4pp+，不太可能仅由随机性解释。

**建议：用 2 epoch + patience=2 的统一 regime 重新训练 random_s42**，消除 regime 差异这一混淆因素，得到可比结果。当前 s42 结果不应纳入 cross-seed 统计。

---
