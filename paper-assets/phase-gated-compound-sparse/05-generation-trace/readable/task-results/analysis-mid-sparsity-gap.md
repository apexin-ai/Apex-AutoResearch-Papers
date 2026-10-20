# analysis mid sparsity gap

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mid-sparsity-gap_20260514T064208_result.json`
- **Structured JSON:** [`901b7b498e8dedaf6714.json`](../../sessions/90/901b7b498e8dedaf6714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**两个实验缺失完全相同的 10 个问题**（同一 seed 同一数据集），原因是 quantile segmentation + min_phase_length=10 过滤：这些问题的 response 较短（平均 6.8 个 phase vs 有数据组 22.7 个），mid-sparsity segments 太短被合并掉。

关键结论：

1. **系统性偏差存在但可解释**：缺失问题偏向低难度（level 1-3）、简单科目（Algebra/Prealgebra），总 segment 数显著更少（Mann-Whitney p=0.0001）。这是短 response 的自然结果，不是 bug。

2. **Bootstrap CI 无 NaN 污染**：`bootstrap_phase_means()` 每个 phase 用自己的 N（high=49, mid=40, low=50），CI 正确。`bootstrap_gradient()` 用 n=min(N)=40 但不按 problem ID 对齐——轻微方法学瑕疵但不影响结论方向。

3. **Robustness check 通过**：40 问题完整子集 vs 全集，所有指标方向一致。mid phase 数据完全不受影响（本身就是 N=40）。gradient 方向均为 >1（low > high），结论不受缺失数据影响。

4. **一个值得注意的点**：gradient ratio 极大且 CI 很宽（因为 median(II_high) 接近 0），建议用 paired difference 而非 ratio 作为主报告指标。

报告已保存至 `artifacts/mid_sparsity_gap_analysis.md`（artifact ID: `art_20260514_99ac04`）。

---
