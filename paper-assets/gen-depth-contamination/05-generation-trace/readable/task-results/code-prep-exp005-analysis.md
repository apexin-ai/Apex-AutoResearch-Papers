# code prep exp005 analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_exp005_analysis_20260513T021202_result.json`
- **Structured JSON:** [`53957554d654f689eda8.json`](../../sessions/53/53957554d654f689eda8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，产出如下：

**`scripts/run_exp005_degradation.py`** — 输入多个 `features.csv` 目录，输出：
- `degradation_analysis.json` (完整结果含 cross-model 一致性)
- `degradation_{model}.json` (每模型单独结果)

**已用 Qwen + Pythia 完整数据跑通的关键发现：**

| 指标 | 值 |
|------|-----|
| Kendall τ (first-pair AUC ranking) | **+0.54** (p=0.004) |
| Spearman ρ (first-pair AUC ranking) | **+0.72** (p=0.002) |

两个模型的特征退化排序中等一致。0v1 depth pair 的特征排名相关性显著，但更深 depth pair (1v2, 2v3...) 的排名一致性迅速下降（τ 接近 0），说明深层退化模式是模型相关的。

等 exp-002 OLMo 的 features.csv 产出后，加入 `--data_dirs` 即可做三模型对比。

---
