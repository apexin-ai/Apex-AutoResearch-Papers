# cpu rrf 3B s42 aggregation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_rrf_3B_s42_aggregation_20260516T125426_result.json`
- **Structured JSON:** [`0eed0b02ed8a36e1bab4.json`](../../sessions/0e/0eed0b02ed8a36e1bab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**3B s42 signals 完整性：全齐 ✓**

| Dose | mmlu | gsm8k | arc_challenge | Signals |
|------|------|-------|---------------|---------|
| d000_a32_s42 | ✓ | ✓ | ✓ | s1+s2+s4 |
| d005_a32_s42 | ✓ | ✓ | ✓ | s1+s2+s4 |
| d025_v3_s42 | ✓ | ✓ | ✓ | s1+s2+s4 |
| d100_a32_s42 | ✓ | ✓ | ✓ | s1+s2+s4 |

**RRF 聚合：已完成，无需重新启动。**

- `rrf_3B_s42/exposure_scores.json` — 今天 18:52 生成，4 doses × 3 benchmarks = 12 条目
- `rrf_all_scales/exposure_scores.json` — 今天 19:56 更新，已整合 3B s42 到全尺寸 pooled 数据中（0.5B/1.5B/3B 共 23 个 respondent）

RRF 产出已就绪，可直接供 exp-006 pooled IRT fitting 使用。

---
