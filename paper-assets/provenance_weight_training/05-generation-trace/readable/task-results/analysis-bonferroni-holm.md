# analysis bonferroni holm

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bonferroni_holm_20260522T172820_result.json`
- **Structured JSON:** [`3705e64cc20d233f853c.json`](../../sessions/37/3705e64cc20d233f853c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Bonferroni-Holm 校正（k=9 全家族）：**
- 仅 2/9 比较通过 α=0.05：D&R full vs Adaptive (p_BH=0.0003) 和 Adaptive vs ESS-only ρ=0.6 (p_BH=0.034)
- **主要 claim（adaptive vs uniform, ρ=0.4）**：p_raw=0.019 → p_BH=0.078，**不显著**
- ρ=0.6 adaptive vs uniform：p_raw=0.009 → p_BH=0.064，刚好不显著

**按表分族校正（更合理）：**
- ρ=0.6 表（k=3）：全部通过（p_BH ≤ 0.018）
- ρ=0.4 主表（k=4）：全部不通过（最接近：adaptive vs random, p_BH=0.052）
- 若仅校正两个主 claim（k=2）：两个均通过（p_BH=0.019, 0.018）

**所有 9 个比较方向在 3 个 seed 上完全一致**，非显著是 n=3 的统计功效问题，不是效应方向问题。

**Grid b=0.6：** 未被测试。最近点 b=0.5（PPL=17.651）和 b=1.0（PPL=17.692），线性插值 ≈ 17.659。

完整报告已保存至 `artifacts/bonferroni_holm_results.md`。

---
