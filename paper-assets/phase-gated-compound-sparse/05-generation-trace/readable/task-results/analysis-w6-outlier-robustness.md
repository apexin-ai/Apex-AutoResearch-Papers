# analysis w6 outlier robustness

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w6_outlier_robustness_20260515T131441_result.json`
- **Structured JSON:** [`684e7c1d6e767e3a5cee.json`](../../sessions/68/684e7c1d6e767e3a5cee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W6 分析完成。核心发现：

**Median-based 指标完全不受 winsorization 影响** — D_median、G_ratio、Wilcoxon p 在原始/5%/10% winsorization 下数值完全一致。这是因为 winsorize 只替换尾部极值，不影响分布中心。

**Mean-based 指标被严重扭曲** — random masking 条件下 mean/median ratio 最高达 97,640:1（远超审稿人提到的 43:1），由 1-2 个 catastrophic perplexity explosion 驱动。5% winsorize 后 MMR 全部降至 ≤13×。

**三个核心 claims 全部 ROBUST**：
- compound > individual (所有 importance 条件 p < 10⁻¹⁴，winsorize 后不变)
- importance > random (8/8 sparsity 配对比较，median 不变)
- dose-response 单调性 (median-based 全部保持)

交付物：
- 服务器：`analysis_output/w6_outlier_robustness.json`
- 本地报告：`artifacts/w6_outlier_robustness/report.md`

---
