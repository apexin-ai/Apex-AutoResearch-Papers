# viz tau bstar table1

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_tau_bstar_table1_20260515T234545_result.json`
- **Structured JSON:** [`385d5d22d85bf77b6914.json`](../../sessions/38/385d5d22d85bf77b6914.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图和 LaTeX 表都已生成。

**输出文件：**
- `artifacts/figures/tau_sweep.pdf` / `.png` — τ sweep 双 Y 轴图
- `artifacts/figures/bstar_distribution.pdf` / `.png` — b* 分布 4 段柱状图
- `output/figures/table1_main_results.tex` — Table 1 booktabs LaTeX

**图 1 (τ sweep)：** 左轴 PPL（蓝），右轴 Mean b*（红），绿色 safe range [0.5, 0.8]，灰色虚线 Uniform baseline，箭头标注 best τ=0.8。

**图 2 (b* 分布)：** 4 段柱状图 [0,0.5)/[0.5,1)/[1,2)/[2,20]，浅→深蓝色渐变，百分比标注，红色虚线 median=0.87，橙色点划线 mean=1.40。

**Table 1：** booktabs 风格，5 methods × 3 seeds，Adaptive (n_min=3) 的 Mean±Std 和 Δ 加粗，脚注标注 † 含义。

---
