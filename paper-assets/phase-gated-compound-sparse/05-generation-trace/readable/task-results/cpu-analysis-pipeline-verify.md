# cpu analysis pipeline verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_analysis-pipeline-verify_20260515T005302_result.json`
- **Structured JSON:** [`1ff15cd6c1c44d4a70d6.json`](../../sessions/1f/1ff15cd6c1c44d4a70d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。报告如下：

---

## 分析 Pipeline 就绪状态报告

### 1. 脚本状态

| 项目 | 状态 |
|------|------|
| `analyze_n500_unified.py` | ✅ 存在（676行） |
| Bootstrap B=10,000 | ✅ `B_BOOT = 10000`，从 `per_problem_ii` 原始数据重算 |
| Median（非 mean）| ✅ D054 合规 |
| d_z within-importance only | ✅ D059 合规，imp-vs-rand 仅 Wilcoxon + median_diff |
| 依赖 numpy/scipy | ✅ numpy=2.2.6, scipy=1.17.1 |
| `analyze_c2_n500.py` 重命名 | ❌ **未重命名**，仍以原名存在 |

### 2. 已完成数据完整性

8 个已完成条件全部 **n=500** 验证通过：

| 文件 | 大小 | n |
|------|------|---|
| ds_imp_s015 | 22.2MB | 500 |
| ds_rand_s015 | 22.2MB | 500 |
| ds_imp_s020 | 22.2MB | 500 |
| ds_rand_s020 | 22.2MB | 500 |
| qw_imp_s015 | 18.7MB | 500 |
| qw_rand_s015 | 18.7MB | 500 |
| qw_imp_s020 | 18.7MB | 500 |
| qw_rand_s020 | 18.7MB | 500 |

### 3. 当前实验进度（s025 阶段）

| 任务 | 进度 | 完成率 |
|------|------|--------|
| DeepSeek imp s025 (GPU0) | 235/500 | 47% |
| DeepSeek rand s025 (GPU1) | 287/500 | 57% |
| Qwen imp s025 (GPU2) | 367/500 | 73% |
| Qwen rand s025 (GPU3) | 341/500 | 68% |

s025 之后每个 GPU 还需跑 **s030（500 problems）**。s030 目录尚未创建。运行脚本 (`run_c2_n500_gpu{0,1}.sh`, `run_c2_qw_n500_gpu{2,3}.sh`) 按 s015→s020→s025→s030 顺序串行执行。

### 4. Dry-run 结果

`--dry-run` 模式成功完成（4.3秒），产出 JSON + CSV。注意：dry-run 按设计使用非 n500 旧数据（`n500 = not args.dry_run`），不是 n500 数据的真实测试。但分析逻辑一致，且脚本对缺失数据优雅降级（返回 `"error": "missing data"`）。

输出文件：
- `analysis_output/n500_unified_dryrun.json` ✅
- `analysis_output/n500_unified_dryrun.csv` ✅

### 5. 需要修复的问题

1. **`analyze_c2_n500.py` 未重命名**：仍以原名存在，需执行 `mv analyze_c2_n500.py analyze_c2_n500_DEPRECATED.py`
2. **预计完成时间**：4 个 GPU 的 s025 平均完成 61%，s025 完成后还需跑完整 s030。按当前速度估计还需 **10-15 小时**才能全部完成，可能明天才能运行正式分析。

---
