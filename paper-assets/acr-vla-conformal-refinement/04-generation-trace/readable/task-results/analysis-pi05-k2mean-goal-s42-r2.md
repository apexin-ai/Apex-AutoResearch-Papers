# analysis pi05 k2mean goal s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-k2mean-goal-s42-r2_20260526T134522_result.json`
- **Structured JSON:** [`9a5f037c54fdad5a6c08.json`](../../sessions/9a/9a5f037c54fdad5a6c08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**pi05-k2mean-goal-s42-r2 → DONE (conclusion: success)**

| Metric | Value |
|---|---|
| Overall SR | 98.0% (196/200) |
| Tasks | 10 × 20 rollouts |
| Lowest task | open_the_middle_drawer_of_the_cabinet 90% |
| Perfect tasks | 8/10 at 100% |

**对比分析**:
- π0.5 VLA-only K=1 Goal SR ≈ 96% → K=2 mean = 98% (+2pp)
- 采样平均本身提供轻微但有意义的增益
- 后续 CRM K=2 在 Goal s42 上的提升若超过 98%，可归因于校正而非采样

---
