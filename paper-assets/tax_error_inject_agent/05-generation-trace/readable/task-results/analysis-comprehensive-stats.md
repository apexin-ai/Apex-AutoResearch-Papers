# analysis comprehensive stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_comprehensive-stats_20260515T001747_result.json`
- **Structured JSON:** [`6ce6962e520947c1e8a4.json`](../../sessions/6c/6ce6962e520947c1e8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册：`artifacts/comprehensive_stats_report.md` (art_20260515_7841e2)

核心结论：

1. **所有方法对比均不显著**：TaxEI vs Vanilla p=0.503（3-seed paired permutation），recovery McNemar p≈1.0，variance F-test p>0.05
2. **方向性证据一致**：TaxEI 均值低 8.5pp、方差高 2.6×、recovery 低 2.1pp — 全部 negative 方向，但统计功效不足以确认
3. **Dose-response 线性下降**：R²=0.961，slope=−0.67pp per 1% injection，25% 注入首次达到 small effect (Cohen's h=−0.33)
4. **MDE = 27.6pp**：n=47 只能检测大于 27.6pp 的差异（80% power），观测到的 8.5pp 差异需要 ~15 seeds 才能确认
5. **Per-task 发现**：`pick_cool_then_place` 受 TaxEI 一致性影响最大（−14.3pp，两个 seed 完全一致），`pick_clean_then_place` 反而受益（+13.6pp）

Random seed=123 eval 完成后可补充更新第三个 seed 的数据。

---
