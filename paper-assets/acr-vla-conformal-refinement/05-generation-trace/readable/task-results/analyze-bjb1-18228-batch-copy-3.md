# analyze bjb1 18228 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bjb1-18228-batch_20260520T103655_result.json`
- **Structured JSON:** [`de6b927ba4726d0c929a.json`](../../sessions/de/de6b927ba4726d0c929a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验在 registry 中均已是 **DONE** 状态，metrics 已填充：

| 实验 | Registry Status | SR (registry) | SR (log) | 一致？ |
|------|----------------|---------------|----------|--------|
| eval-crm-object-k20-seed42 | DONE | 20 (raw %) | 20.0% (20/100) | ✓ |
| eval-adaptive-k-spatial-p75-seed42 | DONE | 0.31 | 31.0% (31/100) | ✓ |
| eval-vla-only-long-seed49-r2 | DONE | 0.16 | 16.0% (16/100) | ✓ |

所有三个实验已被处理完毕，log 数据与 registry metrics 一致。无需更新。

唯一处于 ANALYZING 状态的实验是 **eval-obs-only-object-norm005-seed44**（在 bjb1-32546 上，不是 bjb1-18228）。需要处理这个吗？

### 结果汇总

1. **eval-crm-object-k20-seed42** — SR=20.0%, K=20 vs K=10 baseline (16.8±1.8%) → +3.2pp，略超 K=10 error bar 上界，改善有限
2. **eval-adaptive-k-spatial-p75-seed42** — SR=31.0%, avg_K=5.0, fast_path=62.2% → 低于 Spatial CRM K=10 (34.4±1.5%)，差 3.4pp
3. **eval-vla-only-long-seed49-r2** — SR=16.0% → 与 registry 原有值 (0.16) 一致，re-run 确认数据可靠

---
