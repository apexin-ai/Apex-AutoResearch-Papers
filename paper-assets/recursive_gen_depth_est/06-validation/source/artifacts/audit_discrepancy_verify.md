# 审计争议项验证报告 (2026-05-25)

## 争议 1: Pythia seed42 baseline accuracy — 78.70% vs 78.2%

### 结论：两个值均正确，来自不同 pipeline

| 值 | 来源文件 | Pipeline 配置 |
|---|---|---|
| **78.69% ≈ 78.70%** | `bootstrap_ci_table1_v2.json` → `pythia_nucleus.rf_4class_acc.point = 0.7869` | 5-fold CV, 200 trees, bootstrap CI |
| **78.68%** | `cross_seed_transfer/summary.json` → `seed42_mean = 0.7868` | 5-fold CV (相同 pipeline，互相验证) |
| **78.2%** | `table2_caliber_a_comparison.json` → `old_table2_4class_pct = 78.2` | 旧 pipeline: 80/20 single split, 100 trees |
| **78.15%** | `classification_report.txt` → `Accuracy: 0.7815` | 首次实验 (单次 split, 100 trees, 4000 test samples) |

### 来源追溯

- Registry 中 `pythia_seed43_001.seed42_baseline = 0.782` 引用的是旧 pipeline 的 78.2%（rounded from 0.7815）
- 论文附录 B.22 引用的是 bootstrap_ci_table1_v2 中的 78.69%（rounded 78.70%），CI [78.08, 79.23] → 论文写 [78.10, 79.24]（取整）
- Δ=+0.14pp：`pythia_seed43/summary.json` 的 seed43 acc = 0.7884，delta = 0.7884 - 0.7869 = +0.0015 ≈ +0.14pp（seed43 比 seed42 高 0.14pp）

### 判定

- **论文 B.22 的 78.70% 是正确值**（当前 pipeline: 5-fold CV, 200 trees）
- **Registry 的 0.782 是过时值**（旧 pipeline），不应用于当前论文校验
- 差异不是错误，是 pipeline 升级导致（5-fold CV + 200 trees 比 single-split + 100 trees 略高 0.5pp）

---

## 争议 2: Min-K% d1-d3 Balanced Accuracy = 40.4%

### 结论：40.4% 来自 9-cell average, K=20%, methodB

### 来源文件

`/root/autodl-tmp/recursive_gen_depth_est/results/mink_prob_baseline/mink_prob_results.json`

### 数据定位

```json
"__9cell_average__": {
    "K20_methodB": {
        "4class_acc": 0.3323,
        "d1d3_bal_acc": 0.4039  // ← 40.39% ≈ 40.4%
    }
}
```

### 计算口径

- 9 cells = 3 models × 3 strategies (pythia/olmo/gpt2xl × nucleus/temp09/topk50)
- K=20%: 使用每个 token 的 bottom 20% log-prob 作为 score
- methodB: (具体 scoring 策略，区别于 methodA/C)
- d1d3_bal_acc: 仅对 d1/d2/d3 三类计算 balanced accuracy（排除 d0）

### 各 cell 的 K20_methodB d1d3_bal_acc

| Cell | d1d3_bal_acc |
|---|---|
| pythia_nucleus | 0.3423 |
| pythia_temp09 | 0.3607 |
| pythia_topk50 | 0.3445 |
| olmo_nucleus | 0.4579 |
| olmo_temp09 | 0.4195 |
| olmo_topk50 | 0.3847 |
| gpt2xl_nucleus | 0.4153 |
| gpt2xl_temp09 | 0.5110 |
| gpt2xl_topk50 | 0.3988 |
| **9-cell avg** | **0.4039** |

### 判定

- **40.4% 正确**，来自 9-cell average K20_methodB
- 注意：如果论文 Table 2 选用的是 "best K" 结果（K=30 methodB 给出 0.4075 ≈ 40.8%），需确认是否与 40.4% 矛盾
- 建议确认论文 Table 2 标注的是 K=20% 还是 "best K across all K"

---

## 争议 3: RF d2 recall (.596 vs .592 vs .5867)

### 结论：.596 是 DivEye(XGBoost) 非 RF；.592 无原始数据支撑

### 来源追溯

| 值 | 真实来源 | 方法 |
|---|---|---|
| **0.5867** | `baseline_battery_9cell/all_results.json` → `pythia_nucleus.rf.per_class_recall.d2` | **Random Forest** (100 trees, single split) |
| **0.596** | `baseline_battery_9cell/all_results.json` → `pythia_nucleus.diveye.per_class_recall.d2` | **DivEye (XGBoost)**，非 RF |
| **0.592** | 服务器上无对应原始数据 | 来源不明（可能是过时中间版本或转录错误） |

### 原始数据对照 (pythia_nucleus d2 recall)

```
RF:     0.5867
LR:     0.5027
CORAL:  0.6613
DivEye: 0.596   ← B.14 中 .596 的真实来源
```

### 判定

1. **B.14 写 "RF d2 recall = .596" 是错误的**：.596 是 DivEye(XGBoost) 的值，RF 应为 .5867
2. **B.6 写 "Pythia nucleus d2 = 59.2%" 无法溯源**：
   - 如果指 RF → 应为 58.67%
   - 如果指 DivEye → 应为 59.6%
   - 0.592 不匹配任何已有数据文件
   - seed43 run d2 recall = 0.5882，也不是 0.592
3. **统一建议**：
   - 如果论文上下文讨论 RF → 统一为 **58.67%** (0.5867)
   - 如果论文上下文讨论 DivEye/XGBoost → 统一为 **59.6%** (0.596)
   - B.14 和 B.6 必须标注清楚对应的分类器方法

---

## 附：关键数据文件索引

| 文件 | 用途 |
|---|---|
| `results/reviewer_metrics/bootstrap_ci_table1_v2.json` | Table 1 主数据（5-fold CV + bootstrap） |
| `results/reviewer_metrics/d1d3_balanced_acc.json` | d1-d3 per-class recall（标注 200 trees，实际可能是 100 trees single split） |
| `results/reviewer_metrics/table2_caliber_a_comparison.json` | 新旧 pipeline 对照表 |
| `results/baseline_battery_9cell/all_results.json` | 4 方法 × 9 cells 完整结果（RF/LR/CORAL/DivEye） |
| `results/mink_prob_baseline/mink_prob_results.json` | Min-K% baseline 全部结果 |
| `results/cross_seed_transfer/summary.json` | seed42/43 cross-seed 结果 |
| `results/pythia_seed43/summary.json` | seed43 独立实验结果 |
| `results/classification_report.txt` | 最早期 pythia_nucleus 单次 split 结果 |
