# prep analysis pipeline verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_analysis_pipeline_verify_20260515T025618_result.json`
- **Structured JSON:** [`1f181e66e50c290783cc.json`](../../sessions/1f/1f181e66e50c290783cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 可运行性：✅ 通过
- dry-run (`--dry-run --csv --latex`) 端到端成功，JSON/CSV/LaTeX 全部正常输出
- 依赖就绪：scipy 1.17.1, numpy 2.2.6（脚本只用这两个）

### 输入数据路径匹配

脚本期望 16 个目录：`profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json`

| 条件 | 目录存在 | 数据文件 |
|------|---------|---------|
| Qwen imp s015-s030 | ✅ 全部 | ❌ 空（实验在跑） |
| Qwen rand s015-s030 | ✅ 全部 | ❌ 空 |
| DeepSeek imp s015-s025 | ✅ | ❌ 空 |
| **DeepSeek imp s030** | **❌ 目录不存在** | — |
| DeepSeek rand s015-s030 | ✅ 全部 | ❌ 空 |

**问题：`profiling_output_n500_bf16_ds_imp_s030` 目录缺失。** 脚本会将 ds_imp_s030 报为 "missing data"，导致 DeepSeek 的 s025_vs_s030、s015_vs_s030 d_z 对比缺失。脚本不会崩溃（graceful error handling），但 DeepSeek 分析不完整。

### 统计方法合规性：✅ 符合 D054/D059

| 规范要求 | 脚本实现 | 状态 |
|---------|---------|------|
| 主指标 median（非 mean） | `np.median(diffs)` + `bootstrap_median_ci(B=10000)` | ✅ |
| Wilcoxon signed-rank | `scipy.stats.wilcoxon` 全部 paired 检验 | ✅ |
| d_z 仅 within-importance | `within_dz_importance` 用 d_z；rand/imp-vs-rand 仅报 median_diff | ✅ |
| `np.mean` 使用 | 仅在 `paired_cohens_dz`（line 101），d_z 定义本身就是 mean/SD | ✅ 合规 |
| Bonferroni | 全局收集所有 p 值统一校正 | ✅ |

### 输出

- JSON → `analysis_output/n500_unified.json`
- CSV → `analysis_output/n500_unified.csv`（`--csv`）
- LaTeX → stdout（`--latex`）

### 待解决

**唯一问题：确认 DeepSeek n=500 importance s030 实验是否已启动。** 缺少该目录意味着要么实验未启动，要么输出目录名不同。其余 15/16 条件的目录已就绪，等实验写入 `profiling_results.json` 即可运行全量分析。

---
