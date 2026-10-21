# fix bootstrap voting conf p1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap_voting_conf_p1_20260514T214500_result.json`
- **Structured JSON:** [`7a6586b6167e91683317.json`](../../sessions/7a/7a6586b6167e91683317.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修复总结：

**修改的文件：**
1. **`run_bootstrap_loo.py`（服务器）** — `compute_vc()` 函数（第 101-109 行）：删除 `if v > n/2` majority 过滤，改为 `np.mean([v / n for v in counter.values()])`，与主 pipeline `compute_voting_confidence()` 定义对齐。增加 `n == 0` 边界检查。
2. **`bootstrap_ci_summary.json`（本地）** — `_metadata.notes` 中增加 `voting_conf_bootstrap_caveat` 说明。

**影响范围：**
- `run_llama_conll_bootstrap.py` 从 `run_bootstrap_loo` import `compute_all_signals`，自动继承修复。
- `analyze_exp016_ensemble.py` / `exp_016_v2_ensemble.py` 中的 `if v > n/2` 是 ensemble 选择逻辑（非 voting_conf 信号计算），不受影响，无需修改。
- 已有 bootstrap 结果未重跑，JSON 中数据不变，论文表格已排除 voting_conf。

---
