# analysis batch results update 20260517

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_batch-results-update-20260517_20260517T070805_result.json`
- **Structured JSON:** [`bbeb78192815a7b694e7.json`](../../sessions/bb/bbeb78192815a7b694e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。主要变更：

1. **Fisher test section** 升级为 5-seed: obs_only 85/500=17.0%, 预估 6-seed pooled p≈0.037（有望显著）
2. **新增 Direct Correction Ablation section**: direct_correction=14% ≈ argmin=12%, 远低于 obs_only=22%。最干净的 ablation 证明 CRM 价值在 selection 不在 correction
3. **新增 VLA-mean multi-seed**: 4-seed mean=12.5%, 确认 mean aggregation ≈ argmin, 无增益
4. **Magnitude curve 补充 multi-seed**: norm=0.2 obs_only 5-seed mean=17.0% [15,22]; norm=0.3 perdof 2-seed 4% 零方差（deterministic collapse）
5. **Object Baseline 补充** VLA-mean 数据

关键结论: seed46/47 argmin 结果是决定性的。如果符合预期 (~13%), 6-seed Fisher p≈0.037 将使 Narrative A (statistical significance) 重新可行。

---
