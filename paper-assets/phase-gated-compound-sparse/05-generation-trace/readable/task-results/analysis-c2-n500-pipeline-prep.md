# analysis c2 n500 pipeline prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2_n500_pipeline_prep_20260514T183855_result.json`
- **Structured JSON:** [`bcdc2e6cff86eaee5bde.json`](../../sessions/bc/bcdc2e6cff86eaee5bde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已保存到 memory.md。以下是完整汇总：

---

## C2 n=500 Pipeline 状态

### 实验进度

**DeepSeek (tmux, GPU 0+1)**
| Condition | 状态 | 进度 |
|-----------|------|------|
| ds_imp_s015 | **完成** | 500/500 ✅ |
| ds_rand_s015 | **完成** | 500/500 ✅ |
| ds_imp_s020 | 运行中 | 刚启动 (02:31 UTC) |
| ds_rand_s020 | 运行中 | 刚启动 (02:05 UTC) |
| ds_{imp,rand}_s025 | 排队 | chained in shell script |
| ds_{imp,rand}_s030 | 排队 | chained in shell script |

**Qwen (screen, GPU 2+3)**
| Condition | 状态 | 进度 |
|-----------|------|------|
| qw_imp_s015 | 运行中 | **455/500** (~03:08 完成) |
| qw_rand_s015 | 运行中 | **438/500** (~03:19 完成) |
| qw_{imp,rand}_s020-s030 | 排队 | 6 conditions |

**ETA**: DeepSeek ~17:30 UTC, Qwen ~19:10 UTC

### 分析 Pipeline：就绪，无需修改

- `analyze_c2_n500.py` (512行) 已通过 n=50 dryrun 验证
- 统计方法全部符合要求：paired d_z (B=10000), **median** 为主指标, Wilcoxon, 预注册决策逻辑
- 依赖就绪：scipy 1.17.1 + numpy 2.2.6 (conda base)
- 输出格式与 `cohens_d_bf16.json` 一致
- 脚本支持缺失条件的优雅降级（打印 MISSING 继续执行）

### 数据完整性：无污染

- ds_imp_s015: 500 unique indices, 无重复 ✅
- ds_rand_s015: 500 unique indices, idx [0,499] ✅
- Qwen 目录：空（死进程 PID 132389/132392 未留下残余数据）✅
- `profiling_results.json` 在条件完成时原子写入

### 唯一注意事项

s025/s030 的 `profiling_output_n500_bf16_*` 目录尚不存在，会在对应条件开始时由 `run_profiling` 自动创建。启动脚本用 `set -e`，若中间条件失败会阻断后续条件。

---
