# code mvp gmfrm update

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_gmfrm_update_20260521T163849_result.json`
- **Structured JSON:** [`b71d2b5e8b39a6053707.json`](../../sessions/b7/b71d2b5e8b39a6053707.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四个文件语法检查全部通过。变更总结：

1. **`models.py`** — `fit_sequential` 从两次 MCMC 合并为一次，theta/b/d 从同一次 run 提取，diagnostics 也直接用该次结果
2. **`evaluate.py`** — `run_significance_test` 从 paired t-test 改为 Wilcoxon signed-rank test（支持 `alternative` 参数）；新增 `evaluate_pass_fail` 函数实现三项 pass/fail 判定（收敛、rho=0.3/0.6 改善、rho=0 无退化），返回 PASS / CONDITIONAL PASS / FAIL
3. **`run_mvp.py`** — 完整重写，20 seeds，中心化 theta_true，带格式化输出表（含 p-value 列）和 verdict 打印

---
