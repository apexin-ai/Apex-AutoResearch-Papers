# ops pythia69b v3 collect results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pythia69b_v3_collect_results_20260521T133257_result.json`
- **Structured JSON:** [`869d3c606dff646946d1.json`](../../sessions/86/869d3c606dff646946d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整报告。

---

## Pythia-6.9B C4 Depth Chain v3 实验结果

### 1. 空文本情况

| 文件 | 总行数 | 空文本数 (`"text": ""`) |
|------|--------|------------------------|
| depth_0.jsonl | 5000 | 0 |
| depth_1.jsonl | 5000 | 0 |
| depth_2.jsonl | 5000 | 68 |
| depth_3.jsonl | 5000 | 33 |
| depth_4.jsonl | 5000 | 22 |
| depth_5.jsonl | 5000 | 21 |
| **合计** | **30000** | **144** |

注：JSONL 原始文件中仍存在 144 条空文本（0.48%），集中在 depth 2-5。features.csv 行数 = 30001（含 header），即 30000 数据行 = 6×5000，未剔除空文本行。

### 2. Pairwise AUC（5-fold CV，mean ± std）

| Pair | AUC | Folds | > θ=0.60? |
|------|-----|-------|-----------|
| 0 vs 1 | **0.9941** ± 0.0015 | [0.9968, 0.9940, 0.9938, 0.9938, 0.9921] | Yes |
| 1 vs 2 | **0.8542** ± 0.0031 | [0.8565, 0.8512, 0.8588, 0.8506, 0.8538] | Yes |
| 2 vs 3 | **0.5373** ± 0.0079 | [0.5266, 0.5400, 0.5427, 0.5475, 0.5297] | No |
| 3 vs 4 | **0.5339** ± 0.0046 | [0.5287, 0.5294, 0.5330, 0.5402, 0.5381] | No |
| 4 vs 5 | **0.5211** ± 0.0069 | [0.5206, 0.5189, 0.5153, 0.5345, 0.5164] | No |

### 3. Pairwise JSD

| Pair | JSD |
|------|-----|
| 0 vs 1 | 0.53459 |
| 1 vs 2 | 0.06438 |
| 2 vs 3 | 0.00502 |
| 3 vs 4 | 0.00338 |
| 4 vs 5 | 0.00287 |

### 4. K* 计算

θ = 0.60 时：
- 0v1: 0.9941 > 0.60 → discriminable
- 1v2: 0.8542 > 0.60 → discriminable
- 2v3: 0.5373 < 0.60 → **不可区分**

**K\* = 2**（depth 0→1→2 可区分，depth 2→3 开始饱和）

### 5. Ordinal Classification（6-class, 5-fold CV）

- MAE = 1.0019
- Accuracy = 43.75%

### 6. Top-10 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | surp_d1_mean | 9427.2 |
| 2 | surp_d1_skew | 9366.6 |
| 3 | surp_d2_mean | 9177.2 |
| 4 | freq_kurtosis | 8451.0 |
| 5 | surp_std | 8215.8 |
| 6 | surp_mean | 7998.0 |
| 7 | freq_entropy | 7990.6 |
| 8 | ttr | 6839.6 |
| 9 | surp_d1_std | 6748.8 |
| 10 | surp_d2_std | 6547.2 |

### 7. features.csv

- 路径：`/root/autodl-tmp/gen-depth-contamination/data/exp_pythia69b_c4/features.csv`
- 行数：30001（header + 30000 数据行）
- 列：doc_id, depth, surp_mean, surp_std, surp_skew, surp_kurt, surp_d1_mean, surp_d1_std, surp_d1_skew, surp_d2_mean, surp_d2_std, ttr, hapax_ratio, self_bleu, freq_kurtosis, freq_entropy, low_freq_ratio（16 features）

### 8. 关键观察

AUC 从 0v1 的 0.994 骤降到 2v3 的 0.537（接近随机），JSD 同步从 0.535 降到 0.005。Pythia-6.9B 的信号饱和点（K\*=2）与此前较小模型的实验结果一致：前两代生成文本差异显著，第三代起基本不可区分。surprisal 梯度特征（d1_mean, d1_skew, d2_mean）主导分类。

---
