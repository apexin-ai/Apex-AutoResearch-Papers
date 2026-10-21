# analysis random selection spatial writeup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-selection-spatial-writeup_20260521T035553_result.json`
- **Structured JSON:** [`8a4bd1b674ec7be9470e.json`](../../sessions/8a/8a4bd1b674ec7be9470e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。更新摘要：

**paper_framing.md 更新了 4 处：**
1. **Headline Metrics - Component decomposition**: 添加 "Cross-benchmark: Spatial random K=10 = 29.3% (n=3) ≈ VLA-only Spatial 29.3%"
2. **Headline Metrics - Spatial**: 添加 Random Selection Spatial K=10 数据，标注 "correction is sole driver on Spatial too"
3. **C1 section**: 新增 "Spatial cross-benchmark validation" bullet，含完整 exp_ids、数据、结论（+5.8pp Object, +5.2pp Spatial consistent）
4. **Hard Evidence - Component Decomposition**: 新增 "Spatial Random Selection K=10" 子节，含完整分解（Random-VLA=0.0pp, CRM-Random=+5.2pp）和双 benchmark 一致性结论

**memory.md 更新：** Random Selection Baseline 段落扩展为双 benchmark 汇总表，含所有 exp_ids 和结论。

所有数字均追溯至 registry：Spatial seed42-r2=34%, seed43=26%, seed44=28% → mean 29.3% ≈ VLA-only 29.3%。

---
