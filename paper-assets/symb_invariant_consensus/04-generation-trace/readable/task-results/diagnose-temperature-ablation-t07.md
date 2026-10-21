# diagnose temperature ablation t07

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_temperature-ablation-t07_20260517T190813_result.json`
- **Structured JSON:** [`b8afec3c58668643b33d.json`](../../sessions/b8/b8afec3c58668643b33d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**temperature-ablation-t07** → **DONE (negative)**

| 指标 | 值 |
|------|------|
| SC accuracy | 75.00% |
| SICA accuracy | 71.67% |
| Δ (SICA-SC) | -3.33pp |
| C0 | 40.0% |
| Discordant | 0 SICA wins, 2 SC wins |

C0 修正后四温度点呈单调递增：T=0.3(30%) → T=0.5(38.3%) → T=0.7(40.0%) → T=1.0(43.3%)，消除了旧数据混淆。结论不变：diversity 随温度增加，但 delta 始终≈0。

cron 已删除。

---
