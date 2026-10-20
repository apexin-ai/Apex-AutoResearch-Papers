# analysis e5 hp audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e5-hp-audit_20260515T143111_result.json`
- **Structured JSON:** [`dec5e0432a58629a5148.json`](../../sessions/de/dec5e0432a58629a5148.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the audit result.

## E5 超参数审计结论

### HP 来源链

| 模型 | 代码 | lr | 来源 |
|------|------|-----|------|
| 30-feat GB | `run_e5_e8_server.py:284` | 0.05 | 硬编码 canonical HP |
| 11-feat GB | `run_e5_e8_server.py:296` | **0.05** | 同上，硬编码 |
| 30-feat GB | `bootstrap_ci_crossagent.py` (server) | 0.05 | 来自 `feature_overlap_ablation.py` grid search |
| 11-feat GB | `bootstrap_ci_crossagent.py` (server) | **0.01** | 来自 `no_all_lf` 设定的 grid search 结果 |

### 关键问题

**存在两个版本的 E5，使用不同 HP：**

1. **`run_e5_e8_server.py`** — 两个模型都用 `lr=0.05`，无 grid search
2. **`bootstrap_ci_crossagent.py`** — 30-feat 用 `lr=0.05`，11-feat 用 `lr=0.01`（标注为 "matching original ablation"）

**`e5_e6_e8_results.json` 第 25 行写的是：**
> `"hp_note": "full_30 lr=0.05, lf_overlap_11 lr=0.01 (matching original ablation)"`

### 11-feat 的 `lr=0.01` 是怎么来的？

`feature_overlap_ablation.py:317-325` 有 per-setting grid search（`lr in [0.01, 0.05, 0.1, 0.2]`）。对 **`no_all_lf`** 设定（保留 19 个 non-overlapping 特征），grid search 选中了 `lr=0.01`。

**但 `no_all_lf`（19 特征）和 `lf_overlap_11`（11 特征）是互补的不同特征集。** Bootstrap worker 把 19-feat 的最优 HP 错误地套用到了 11-feat 模型。

### 是否各自 CV-tuned？

**否。**

- `feature_overlap_ablation.py` 的 grid search 是 simple train-val split（不是 k-fold CV），且只 tune `lr`（`n_estimators=200`、`max_depth=5` 固定）
- 它没有 "lf_overlap_11" 这个设定——只有 `full_30`、`no_cmd_rep`、`no_file_diff`、`no_outcome_bp`、`no_all_lf`
- 11-feat 模型从未被独立 tuned，其 `lr=0.01` 来自不同特征集（19-feat residual）的 tuning 结果
- `run_e5_e8_server.py` 直接硬编码 `lr=0.05` 给两个模型，完全没有 tuning

### 影响评估

两个版本报告的 F1 相同（0.977 vs 0.9674），说明 lr=0.01 vs 0.05 对 11-feat 模型影响不大。但这仍然是一个方法论瑕疵。

### 修复建议

**方案 A（最简单，推荐）：** 统一使用 `lr=0.05`（`run_e5_e8_server.py` 的做法），两个模型共享 canonical HP。这是公平对比，ablation 比较的是特征集差异而非 HP 差异。更新 `hp_note` 即可。

**方案 B（最严谨）：** 对 11-feat 和 30-feat 分别做 grid search（`lr in [0.01, 0.05, 0.1, 0.2]`），在 train-val split 上各自选最优 HP，然后重跑 bootstrap。

---
