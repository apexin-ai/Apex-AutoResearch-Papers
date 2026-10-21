# code exp014 v1 independent

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp014_v1_independent_20260525T160109_result.json`
- **Structured JSON:** [`dfc424ebffb5a7563cfb.json`](../../sessions/df/dfc424ebffb5a7563cfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交（tmux session: `exp_014_independent_metrics`, GPU: cuda:1）。

执行流程：
1. 下载 GPT-2 Large（~3GB，网络加速已开启）
2. 计算 5K docs 的 6 个独立指标（PPL/MTLD/HDD/3gram-rep/4gram-rep/Zipf）
3. 运行分析脚本：correlation + stratified + statistical tests + length-controlled + MAUVE + plots

预计总时长约 20-40 分钟（5K docs 比较小，GPT-2 PPL 约 10 分钟，MAUVE 约 5 分钟，下载时间取决于网络）。

输出文件：
- `results/exp014_v2/cc_quality_independent.csv`
- `results/exp014_v2/independent_analysis_results.json`
- `results/exp014_v2/independent_violin.pdf`
- `results/exp014_v2/depth_distribution.pdf`
- `results/exp014_v2/mauve_by_bin.pdf`

---
