# analysis ddr temperature stability

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ddr_temperature_stability_20260519T120117_result.json`
- **Structured JSON:** [`e52efc7b55ae80c691a8.json`](../../sessions/e5/e52efc7b55ae80c691a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个交付物已完成。汇总：

## 分区稳定性结果

**稳定锚点（跨温度不变）：**
- `entropy_mean`：12/12 条件下始终 drifting
- `entropy_min`、`entropy_max`：分别 10/12 和 9/12 条件下 near-stationary

**基本稳定（偶尔偏移）：**
- `ttr`：10/12 drifting，仅 t=0.9 时 Pythia-2.8B 和 Qwen3-0.6B 降至 intermediate
- `hapax_ratio`：9/12 drifting，同样在 t=0.9 高温下压缩

**温度敏感特征：**
- `entropy_std`：t=0.5 时全部 drifting，t=0.7 时 borderline（3/4 generator 仍 >0.5），t=0.9 时 3/4 降至 intermediate
- `tail_decay`：在 near-stationary 和 intermediate 之间摇摆（7/12 vs 5/12），受 generator 影响大于温度

**核心发现：** 严格的 3/1/3 分区在任何单个 (generator, temperature) 组合中都不精确成立——实际模式更接近 4/0-1/2-3。但特征的相对排序（lexical diversity 特征漂移最快，entropy 极值最稳定）在所有温度下保持一致。Effect size 随温度单调压缩：mean drifting |d| 从 t=0.5 的 1.03 降至 t=0.9 的 0.58。

**文件：**
- CSV: `artifacts/_project/tables/ddr_temperature_stability.csv`（84 行，4 gen × 3 temp × 7 features）
- LaTeX: `artifacts/_project/tables/ddr_temperature_stability_latex.tex`

---
