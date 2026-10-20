# code b10000 pipeline update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_b10000_pipeline_update_20260514T224823_result.json`
- **Structured JSON:** [`e3b41a9804cb114f2e32.json`](../../sessions/e3/e3b41a9804cb114f2e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕，结果汇总：

### 1. analyze_n500_unified.py 的 B 值
**已确认 B=10,000**（line 46: `B_BOOT = 10000`），无需修改。

### 2. 是否从原始数据重算 CI
**是。** `load_problems()` 从 `profiling_results.json` 读取 `per_problem_ii` 的原始逐题 II 值，`extract_diffs()` 计算 `ii_low - ii_high` 差值数组，然后 `bootstrap_median_ci()` 用 B=10,000 从头计算 bootstrap CI。**不引用预计算的 `median_ci_low/median_ci_high`。**

### 3. B=10,000 计算时间
dry-run（n=50）耗时 **2.3 秒**（wall time），完全不是问题。n=500 按线性估算约 23 秒。

### 4. Figure 1 数据源
`fig1_dose_response.py` 读取 `rebootstrap_b10000_results.json`（已存在，今天生成），该文件由 `analysis/rebootstrap_importance_b10000.py` 使用 **B=10,000** 生成。`fig5_crossmodel.py` 同样读取此文件。所有 figure CI 数据源均为 B=10,000。

### 5. profiling 脚本
`profiling/run_profiling.py` line 50: `N_BOOTSTRAP = 1000`。但分析 pipeline 不依赖其预计算 CI，所以不影响最终结果。

**结论：整个分析 pipeline 已全部使用 B=10,000 bootstrap，无需任何修改。**

---
