# research r3 n5 cross strategy curation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r3_n5_cross_strategy_curation_20260516T015909_result.json`
- **Structured JSON:** [`385ba45b770feb5f8c4e.json`](../../sessions/38/385ba45b770feb5f8c4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## R3-N5 分析结论

### 已有数据覆盖情况

从 9 fold 跨策略 LOO 结果量化了三种 curation 场景（keep d0+d1 / keep d0 only / keep d0+d1+d2）：

| 类别 | 折数 | d1 召回 | kept pool 精度 | d2+d3 泄露率 |
|------|------|---------|---------------|-------------|
| **反转折** (GPT-2 XL/OLMo temp09) | 2/9 | **24.3%** | **99.3%** | 0.5% |
| **正常折** | 7/9 | 77.1% | 76.6% | 36.2% |

**核心发现：失败模式是不对称的。** 反转折的 curation 是"安全但浪费"——几乎没有污染泄露（精度 99.3%），但丢弃了 76% 的可用 d1 数据。这实际上部分缓解了 R3-N5 的担忧：误用跨策略分类器做 curation 不会引入污染，只会损失数据量。

### 论文文本检查

论文已充分覆盖 R3-N5：
- **discussion.tex L8-11**: two-stage pipeline + 策略可区分性论证 ✓
- **discussion.tex L19**: curation PoC 显式声明 within-strategy caveat + 链接到 §5.3 反转 ✓
- **generalization.tex L89-91**: d1/d2 反转数据 + z-score 部分恢复 ✓
- **conclusion.tex (Limitations) L4-6**: 跨策略部署约束 + z-score 恢复数字 ✓

### 一个需要修改的地方

**conclusion.tex L6** 中 z-score 恢复数字 `(GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$)` 来自 **LR (logistic regression)** 的 scaler→zscore 结果，但论文全文主线使用 RF。RF z-score 恢复极小（0.129→0.135, 0.253→0.250）。

建议修改 conclusion.tex L6，二选一：
1. **最小改动**：加括号 `(logistic regression with per-strategy z-score features: GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$)` 
2. **更诚实**：报告 RF 数字 + LR 数字对比，说明 z-score 对 RF 无效但 LR 可部分恢复

### R3-N5 是否可以标记 ✅？

**可以**，条件是修复上述 classifier 标注。两个 action item 均已 done，论文四处（discussion ×2, generalization, limitations）充分覆盖了跨策略 curation 不可行性 + workaround。新的定量分析（asymmetric failure mode）可用于 rebuttal 补充论证。

分析结果已保存到 `/root/autodl-tmp/recursive_gen_depth_est/results/r3_n5_cross_strategy_curation/analysis.json`。

---
