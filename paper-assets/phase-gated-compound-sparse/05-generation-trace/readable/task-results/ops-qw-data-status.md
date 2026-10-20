# ops qw data status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qw_data_status_20260515T170833_result.json`
- **Structured JSON:** [`44e8ba79bd7ac8667e6c.json`](../../sessions/44/44e8ba79bd7ac8667e6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## QW GSM8K Profiling 状态

### QW importance — **已完成** (50/50)
- 输出文件: `profiling_results.json` (3.2MB), `generations.json` (156KB)
- **ii_low 全部为 0.0 或 null**：200 个 ii_low 条目中，100 个 = `0.0`，100 个 = `null`（n_segments_low=1 时无法计算）。非零值 = 0。**全零模式确认。**
- Verdict: **PASS** — high_sparsity vs low_sparsity CI 在 sparsity=0.2 不重叠
- 聚合 II：
  - low_sparsity: 全 4 个 sparsity level 均 mean=0.0, CI=[0,0]
  - high_sparsity @ 0.2: mean=+432.64 (显著)
  - mid_sparsity @ 0.2: mean=+323.33

### QW random — **进行中** (45/50)
- 输出目录为空（结果在完成后才写入）
- 日志显示正在处理 problem 45/50（gsm8k_test/1206），每题约 3-4 min
- **预计还需 ~15-20 min 完成**

### GPU 状态
| GPU | Utilization | Memory |
|-----|------------|--------|
| 0-2 | 0% | 3 MiB |
| 3 | 94% | 59931 MiB |

GPU 3 上运行 3 个进程：QW random profiling (PID 245314)、mpl_sensitivity (PID 221265)、另一个 profiling run (PID 251888)。GPU 0-2 空闲。

---
