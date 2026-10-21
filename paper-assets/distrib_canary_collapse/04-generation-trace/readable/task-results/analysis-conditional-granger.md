# analysis conditional granger

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conditional_granger_20260518T095827_result.json`
- **Structured JSON:** [`9e232b2d366ba5cb2c63.json`](../../sessions/9e/9e232b2d366ba5cb2c63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D061 完成。

**核心结论：token_entropy 和 ECE 提供冗余信息，不是独立信息。**

结果摘要：
- 所有 6 个 marginal Granger 测试都高度显著（p < 0.002）
- 所有 6 个 conditional Granger 测试都不显著（p > 0.08）
- 控制 ECE 后，entropy 对 diversity 无独立预测力（0/3）
- 控制 entropy 后，ECE 对 diversity 无独立预测力（0/3）

**解读**：两个 canary 高度共线性，追踪的是同一个底层校准退化过程。对实际早期预警而言，监测任一即可；同时监测增加鲁棒性但不提供新信息。

**Limitation**: T=11 下条件模型 df_resid=5，统计力极低。冗余结论可能部分反映 power 不足。

产出：
- 脚本：`/root/autodl-tmp/distrib_canary_collapse/analyze_conditional_granger.py`
- 报告：`artifacts/d061_conditional_granger_analysis.md`（已注册 manifest）

---
