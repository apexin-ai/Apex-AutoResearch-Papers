# pre check analysis readiness

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pre-check_analysis-readiness_20260515T041452_result.json`
- **Structured JSON:** [`f306009044daf1c9a90a.json`](../../sessions/f3/f306009044daf1c9a90a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## n=500 分析环境预验证报告

### 1. 脚本存在性：**PASS**
`analyze_n500_unified.py` 存在，结构完整。仅依赖 stdlib + numpy + scipy.stats（不需要 pandas）。

### 2. 依赖检查：**PASS（条件性）**
| 包 | conda base (`/root/miniconda3/bin/python3`) | 系统 python |
|---|---|---|
| numpy | 2.2.6 ✓ | ✗ ModuleNotFoundError |
| scipy | 1.17.1 ✓ | ✗ ModuleNotFoundError |

**必须用 conda 环境运行**（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），裸 `python3` 会失败。

### 3. n=500 数据完整性：**12/16 完成，4 个 s030 在跑**

| 条件 | s015 | s020 | s025 | s030 |
|------|------|------|------|------|
| ds_imp | ✓ | ✓ | ✓ | 运行中 111/500 |
| ds_rand | ✓ | ✓ | ✓ | 运行中 157/500 |
| qw_imp | ✓ | ✓ | ✓ | 运行中 335/500 |
| qw_rand | ✓ | ✓ | ✓ | 运行中 328/500 |

### 4. s030 进度与 ETA（基于 12:15 快照）

| 任务 | 进度 | 启动时间 | 预计完成 |
|------|------|---------|---------|
| qw_imp_s030 | 335/500 (67%) | 09:53 | ~13:00 |
| qw_rand_s030 | 328/500 (66%) | 10:01 | ~13:00 |
| ds_rand_s030 | 157/500 (31%) | 10:54 | ~15:10 |
| ds_imp_s030 | 111/500 (22%) | 11:19 | ~15:30 |

**最晚完成时间：~15:30 今天。**

### 5. 磁盘空间：**PASS**
`/root/autodl-tmp` 250G 中用了 84G，剩余 167G（66%），充足。

### 6. 活跃进程：**4 个 profiling 任务正常运行**
通过 tmux（c2_n500_gpu0/gpu1）和 screen（c2_qw_gpu2/gpu3）管理，均 100% CPU 正常跑。

### 7. 输出目录：**PASS**
`analysis_output/` 已存在，已有之前 dryrun 产出（`n500_unified_dryrun.json/csv`），写权限正常。

---

### 结论

**分析脚本可以顺利执行。** 唯一注意点：运行时必须激活 conda 环境。预计 **15:30** 后所有 s030 数据就绪，届时可立即执行：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/pacs
python analyze_n500_unified.py --csv
```

---
