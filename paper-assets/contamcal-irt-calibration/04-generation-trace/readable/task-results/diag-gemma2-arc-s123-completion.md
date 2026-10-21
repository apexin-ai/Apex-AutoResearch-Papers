# diag gemma2 arc s123 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-arc-s123-completion_20260520T180041_result.json`
- **Structured JSON:** [`3da1daf7870c46942304.json`](../../sessions/3d/3da1daf7870c46942304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Cron 列表为空（已不在本 session），registry 已更新为 DONE。

**结果汇总：**

| Dosage | Accuracy |
|--------|----------|
| d000 | 85.84% |
| d005 | 83.36% |
| d025 | 85.67% |
| d050 | 85.24% |
| d100 | 88.57% |

**Oscillation 判断：无 artifact。** 相邻 dosage 最大差异 3.33pp（d050→d100），远低于 10pp 阈值。s42 的 16pp oscillation 未在 s123 重现，说明该 artifact 是 seed-specific 而非 model-intrinsic。

注意 d005 出现 2.48pp 下降（低于 d000），d000→d100 总体 delta +2.73pp，contamination effect 方向正确但非单调。

---
