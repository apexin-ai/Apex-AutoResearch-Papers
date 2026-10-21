# code exp006 analysis script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006-analysis-script_20260514T083951_result.json`
- **Structured JSON:** [`dc0d38869b83e6403c50.json`](../../sessions/dc/dc0d38869b83e6403c50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`scripts/analyze_exp006.py` 已创建。与已有的两个分析脚本相比，新增：

- **Cohen's d** effect size
- **Bonferroni 校正**（12 次比较，校正后 α≈0.0042）
- **Contingency 判断**：自动判定 VERSION_A（graduated 显著优于 binary）或 VERSION_B（无显著差异），输出判据
- **LaTeX 表格**包含 `vs binary-ours (p)` 列
- **Wilcoxon signed-rank** 作为非参数补充

数据结构匹配实际实验：graduated 按 α 扫描（0.1–0.9），自动选最优 α 后与其他策略对比。

用法：`python analyze_exp006.py --results_dir /root/autodl-tmp/gen-depth-contamination/outputs/exp006 --output_dir artifacts/exp006`

---
