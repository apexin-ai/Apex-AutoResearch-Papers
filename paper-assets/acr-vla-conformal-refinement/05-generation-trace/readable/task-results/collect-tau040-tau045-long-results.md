# collect tau040 tau045 long results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_tau040-tau045-long-results_20260528T024428_result.json`
- **Structured JSON:** [`37bfc08d380a4353f6cf.json`](../../sessions/37/37bfc08d380a4353f6cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。

```
smolvla-tau040-long-s42: success_rate=60.0%, trigger_rate=0.4%, conclusion=success
smolvla-tau045-long-s42: success_rate=59.5%, trigger_rate=0.3%, conclusion=success
```

符合预期——高 τ 端 trigger_rate 接近 0，CRM 几乎不介入，性能接近 VLA-only baseline (58%)，略高是正常波动。完整 Long suite τ-sweep 曲线现在有 7 个数据点：τ=0.05(44%) → 0.10(53.5%) → 0.15(61%) → 0.25(56%) → 0.35(57.5%) → 0.40(60%) → 0.45(59.5%)。

---
