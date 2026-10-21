# analysis golden ratio ess only

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_golden_ratio_ess_only_20260515T132426_result.json`
- **Structured JSON:** [`64c76289544cd827669b.json`](../../sessions/64/64c76289544cd827669b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 实验结果汇总

### 1. golden_ratio_seed42

| 指标 | 值 |
|------|-----|
| **状态** | 正常完成 (EXIT_CODE=0) |
| **train_loss** | 8.4580 |
| **train_runtime** | 13441.5s (~3h43m) |
| **total_steps** | 6103 |
| **train_steps/s** | 0.454 |
| **epoch** | 0.26 |
| **weighting_method** | golden_ratio |
| **b 值** | 全部为 0.0（golden_ratio 方法不使用 b 参数） |
| **eval_ppl_holdout** | **未记录**（训练脚本未执行 holdout 评估） |
| **Checkpoint** | `/root/provenance_weight_training/output/models/golden_ratio_seed42/final/` (model.safetensors 1.11GB) |

其他 checkpoint: `checkpoint-6000`, `checkpoint-6103`

---

### 2. ess_only_seed42

| 指标 | 值 |
|------|-----|
| **状态** | 正常完成 (EXIT_CODE=0) |
| **train_loss** | 10.2113 |
| **train_runtime** | 12977.7s (~3h36m) |
| **total_steps** | 6103 |
| **train_steps/s** | 0.470 |
| **epoch** | 0.26 |
| **weighting_method** | ess_only |
| **eval_ppl_holdout** | **未记录**（训练脚本未执行 holdout 评估） |
| **Checkpoint** | `/root/provenance_weight_training/output/models/ess_only_seed42/final/` (model.safetensors 1.11GB) |

其他 checkpoint: `checkpoint-6000`, `checkpoint-6103`

#### ess_only b 值分布统计 (n=24412)

| 统计量 | 值 |
|--------|-----|
| mean | 3.5061 |
| median | 1.5820 |
| stdev | 4.6920 |
| min | 0.1953 |
| max | 20.0000 |
| p25 | 0.8203 |
| p75 | 3.7695 |

| 区间 | 占比 |
|------|------|
| b == 0 | 0.00% |
| 0 < b ≤ 1 | 32.66% |
| 1 < b ≤ 5 | 48.14% |
| b > 5 | 19.20% |

---

### 与 Baseline 对比

| 实验 | train_loss | PPL (holdout) | b_mean | b_median |
|------|-----------|---------------|--------|----------|
| uniform_seed42 | — | **17.69** | — | — |
| adaptive_fix_seed42 | — | **17.65** | 1.399 | 0.871 |
| **golden_ratio_seed42** | 8.458 | ❌ 未评估 | 0.0 (不使用) | 0.0 |
| **ess_only_seed42** | 10.211 | ❌ 未评估 | 3.506 | 1.582 |

### 关键发现

1. **两个实验都没有运行 holdout 评估**，无法直接对比 PPL。需要单独运行 eval 脚本。

2. **golden_ratio 的 b 始终为 0**——该方法通过 golden ratio 直接计算权重，不搜索 b 参数。ESS 在 3.79–4.0 之间（batch_size=4 时接近均匀）。

3. **ess_only 的 b 分布明显偏高**（mean=3.51, median=1.58），相比 adaptive_fix（mean=1.40, median=0.87）更激进。19.2% 的样本 b>5，符合预期的 max-intervention behavior。b 最高达 20.0。

4. **ess_only 的 train_loss (10.21) 显著高于 golden_ratio (8.46)**——ess_only 因为更激进的加权导致 weighted loss 更大，这是预期行为。

5. **需要下一步**：对两个 checkpoint 运行 holdout eval 以获取 PPL，才能完成与 uniform/adaptive_fix 的公平对比。

---
