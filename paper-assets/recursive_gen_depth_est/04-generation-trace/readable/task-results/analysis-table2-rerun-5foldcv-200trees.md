# analysis table2 rerun 5foldcv 200trees

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table2_rerun_5foldcv_200trees_20260518T172416_result.json`
- **Structured JSON:** [`aa5148ba8e05c51bc99e.json`](../../sessions/aa/aa5148ba8e05c51bc99e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 9 cells 完成。JSON 已保存到 `results/table2_rerun_5foldcv.json`。

## Table 2 重跑结果 (RF-200, 5-Fold CV, No Scaler)

所有 cell 均 20000 样本，类别分布均衡 [5000, 5000, 5000, 5000]。

### 主表

| Cell | 4-Class Acc (%) | 95% CI | d1-d3 BalAcc (%) | 95% CI |
|------|---:|---:|---:|---:|
| pythia_nucleus | 78.70 ± 0.53 | [78.10, 79.24] | 71.83 ± 0.75 | [71.06, 72.55] |
| pythia_temp09 | 76.79 ± 0.88 | [76.21, 77.38] | 69.33 ± 1.11 | [68.61, 70.03] |
| pythia_topk50 | 68.85 ± 0.32 | [68.17, 69.44] | 58.89 ± 0.46 | [58.13, 59.61] |
| olmo_nucleus | 78.94 ± 0.54 | [78.38, 79.48] | 72.65 ± 0.74 | [71.96, 73.32] |
| olmo_temp09 | 82.27 ± 0.67 | [81.74, 82.78] | 76.60 ± 0.87 | [75.95, 77.25] |
| olmo_topk50 | 74.40 ± 0.95 | [73.81, 74.98] | 66.15 ± 1.22 | [65.48, 66.89] |
| gpt2xl_nucleus | 84.28 ± 0.52 | [83.78, 84.80] | 79.55 ± 0.58 | [78.94, 80.21] |
| gpt2xl_temp09 | 85.91 ± 0.40 | [85.48, 86.35] | 81.54 ± 0.49 | [80.99, 82.09] |
| gpt2xl_topk50 | 75.78 ± 0.88 | [75.17, 76.35] | 68.14 ± 1.11 | [67.39, 68.84] |

### Per-Class Recall (d1/d2/d3)

| Cell | d1 | d2 | d3 |
|------|---:|---:|---:|
| pythia_nucleus | 81.9% | 59.2% | 74.4% |
| pythia_temp09 | 79.9% | 56.0% | 72.1% |
| pythia_topk50 | 71.6% | 44.2% | 60.9% |
| olmo_nucleus | 82.1% | 60.6% | 75.3% |
| olmo_temp09 | 87.1% | 65.6% | 77.1% |
| olmo_topk50 | 80.9% | 50.4% | 67.2% |
| gpt2xl_nucleus | 87.4% | 72.8% | 78.5% |
| gpt2xl_temp09 | 91.1% | 73.0% | 80.5% |
| gpt2xl_topk50 | 81.3% | 54.8% | 68.4% |

### 备注

- **数据路径与任务描述不符**：实际目录结构不是 `depth_X/features.jsonl`，而是预提取的单个 `features.jsonl` 文件。`pythia_nucleus` 对应 `data/features_all.jsonl`，`olmo_nucleus` 对应 `data/olmo/features.jsonl`，部分 cell 的 features 在 `results/` 目录下。
- **特征名与任务描述不符**：实际的 19 特征是 `skewness_ppl, kurtosis_ppl, p25_ppl, p50_ppl, p75_ppl, entropy_of_surprisal, type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy, rep_2gram, rep_3gram, rep_4gram` 等，而非任务中列出的 `max_surprisal, mean_entropy, uniq_ratio` 等。脚本使用了数据中的实际特征名。
- **无异常**：无 inf/nan，9 cell 均为完美均衡分布，无数据缺失。
- **Warning**：bootstrap 中 `y_pred contains classes not in y_true` 是正常的（某些 bootstrap 样本可能缺少某个 class），不影响结果。
- **所有 cell 中 d2 recall 最低**（44%~73%），d1 最高，符合中间深度最难区分的预期。

---
