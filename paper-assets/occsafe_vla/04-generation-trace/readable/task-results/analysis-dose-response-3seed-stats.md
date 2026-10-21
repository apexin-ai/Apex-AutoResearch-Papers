# analysis dose response 3seed stats

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose_response_3seed_stats_20260525T093236_result.json`
- **Structured JSON:** [`821244424c7bed935ffb.json`](../../sessions/82/821244424c7bed935ffb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。输出：

- **统计汇总表**：7 个条件 vs Vanilla baseline，含 mean±SD/SE、paired t-test (n≥3)、Cohen's d、显著性标记
- **dose_response_curve_data_car.csv**：matplotlib 可直接消费的曲线数据
- **dose_response_3seed_final.pdf/png**：学术风格图表，filled circles、Vanilla SE band、Reverse cutoff diamond marker、n= 标注（n<3 红色高亮）

当前结果：Detach+BN 显著低于 Vanilla (p=0.031, d=-3.21)；4 个条件仍有 seeds 在训练中。

---
