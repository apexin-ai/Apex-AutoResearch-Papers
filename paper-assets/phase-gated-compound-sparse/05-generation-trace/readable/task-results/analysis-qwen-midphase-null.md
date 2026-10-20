# analysis qwen midphase null

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_midphase_null_20260515T082534_result.json`
- **Structured JSON:** [`f2d694ba275506fd69f5.json`](../../sessions/f2/f2d694ba275506fd69f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写到 `artifacts/n500_analysis/qwen_midphase_null_analysis.md`。

**根因结论**：不是 token 长度问题，而是 Qwen 的 attention sparsity 时间自相关性显著低于 DeepSeek（lag-1 r = 0.718 vs 0.894, Cohen's d = −1.68, p = 2.8e-128）。

**机制链**：
1. Qwen 的 sparsity 在 token 间快速波动 → mid-sparsity tokens 散布在 low/high 之间，不形成连续块
2. quantile 分段后，所有 226 个 mid-null 问题的最长连续 mid-run ≤ 9 tokens（100% 命中率）
3. `min_phase_length=10` 合并步骤消除了所有 mid 段
4. 若设 mpl=1（不合并），两个模型的 mid-null 率均为 0%

**token 长度是次要因素**：Cohen's d = −0.42，最佳分离阈值 554 tokens 准确率仅 60.4%，且大量 2047-token 问题仍是 mid-null。

**对论文的影响**：这是 model characteristic（Qwen 的 phase-fragmented reasoning），不影响主指标 D_imp = II_low − II_high（仅需 low+high 有效，n≈475）。

---
