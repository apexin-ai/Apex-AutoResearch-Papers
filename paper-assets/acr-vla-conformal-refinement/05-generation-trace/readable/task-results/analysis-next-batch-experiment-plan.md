# analysis next batch experiment plan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_next-batch-experiment-plan_20260517T113300_result.json`
- **Structured JSON:** [`c3ec3bc9b13dd08c9fe9.json`](../../sessions/c3/c3ec3bc9b13dd08c9fe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计划已写入并注册。核心结论：

**最薄弱点**: norm=0.03 和 norm=0.05（obs_only 和 perdof 各仅 1 seed，无法画 error bar）。这是 Figure 2 左端点，对 "低 magnitude 时两者表现相近" 的 claim 至关重要。

**推荐 Tier 1（8 个实验，全部必做）**:
- obs_only norm=0.03 seed43/44
- obs_only norm=0.05 seed43/44
- perdof norm=0.03 seed43/44
- perdof norm=0.05 seed43/44

**部署分配**: bjb1-18228 (4 GPU) 跑 obs_only，bjb1-32546 (4 GPU) 跑 perdof。完成后 Figure 2 所有点均有 >=3 seeds 可绘制 mean +/- stderr。

详细命令见 `artifacts/next_batch_plan_20260517.md`。

---
