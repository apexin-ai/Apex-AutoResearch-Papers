# ops verify analysis readiness

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-analysis-readiness_20260514T235050_result.json`
- **Structured JSON:** [`1bae717892678d21a4c4.json`](../../sessions/1b/1bae717892678d21a4c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### 脚本就绪状态：**YES**

所有关键点均通过检查：

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 数据路径 | ✅ | `profiling_output_n500_bf16_{ds,qw}_{imp,rand}_{s015..s030}` — 与实际目录匹配 |
| median (非 mean) | ✅ | `np.median()` + `bootstrap_median_ci()`, D054 约束已标注 |
| Bootstrap B=10,000 | ✅ | `B_BOOT = 10000` |
| d_z within-importance only | ✅ | imp pairs 报 d_z + bootstrap CI; rand pairs 和 imp-vs-rand 只报 Wilcoxon + median_diff, 不算 d_z (D059) |
| 缺失数据容错 | ✅ | 缺失目录/文件优雅跳过，报 "missing data" |
| Dry-run 实测 | ✅ | 对已完成的 s015+s020 正常执行，2.6 秒无报错 |

### 当前数据完成状态

已完成（有 `profiling_results.json`）：ds/qw × imp/rand × s015/s020 = **8/16 条件**

未完成：s025（目录已创建但空）、s030（目录不存在）

### 运行命令

实验全部完成后，直接执行：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/pacs
python analyze_n500_unified.py --csv --latex 2>&1 | tee analysis_output/n500_unified.log
```

### 预计运行时间

实测 2 conditions = 2.6s（含 1 组 d_z bootstrap）。16 conditions + 8 组 d_z bootstrap + 4 组 permutation monotonicity (N=5000) 估计 **60-90 秒**。

---
