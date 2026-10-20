# cpu precheck analysis pipeline

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_precheck_analysis_pipeline_20260514T214616_result.json`
- **Structured JSON:** [`34596b4f48f0fec264d6.json`](../../sessions/34/34596b4f48f0fec264d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 预检报告

### 1. s015 数据完整性 ✅

| Condition | profiling_results.json | 问题数 | median/median_ci 字段 |
|-----------|----------------------|--------|----------------------|
| ds_imp_s015 | ✓ | 500 | ✓ (median=0.006531, CI=[0.005469, 0.007701]) |
| ds_rand_s015 | ✓ | 500 | ✓ |
| qw_imp_s015 | ✓ | 500 | ✓ |
| qw_rand_s015 | ✓ | 500 | ✓ |

per_problem_ii 数据含 ii_high/ii_mid/ii_low，每 condition 500 条，配对分析就绪。

### 2. 分析脚本 ✅

`/root/autodl-tmp/pacs/analyze_c2_n500.py` 功能完备：

- **Median diff + bootstrap CI**：`bootstrap_ci_median()`，B=10000，seed=42
- **Paired d_z + bootstrap CI**：`bootstrap_ci_dz()`，D = ii_low − ii_high
- **d_z 输出**：`cohens_d_n500.json` 只存 imp 条件（within-importance），符合 D059
- **Wilcoxon signed-rank**：单侧检验 (alternative="greater")
- **缺失容错**：missing conditions 记录并跳过，不阻塞
- **n=50 对照**：自动加载旧 n=50 数据做 CI width reduction 比较
- 依赖仅 numpy + scipy，conda base 已有

**注意**：`cohens_d_n500.json` 中附带 mean_diff/std_diff 字段（用于参考），主报告以 median 为主指标，符合 D054。

### 3. s020 进度

| Condition | 完成/总数 | 进度 |
|-----------|----------|------|
| ds_imp_s020 | 374/500 | 74.8% |
| ds_rand_s020 | 422/500 | 84.4% |
| qw_imp_s020 | 419/500 | 83.8% |
| qw_rand_s020 | 395/500 | 79.0% |

（截至 05:47 UTC，每题约 30-60s，预计全部完成还需 1.5-3 小时）

### 4. 磁盘空间 ✅

`/root/autodl-tmp`: 250G 总量，已用 84G，剩余 **167G (66%)**，充足。

### 5. 结论

**分析 pipeline 就绪：Yes**

- s015 全部 4 条件数据完整，可立即跑分析（`python analyze_c2_n500.py` 会对缺失的 s020-s030 报 warning 但不中断）
- s020 正在跑，预计今天内完成
- s025/s030 的 n500 目录尚不存在——这两组实验还没启动，需要排期
- 无阻塞风险

---
