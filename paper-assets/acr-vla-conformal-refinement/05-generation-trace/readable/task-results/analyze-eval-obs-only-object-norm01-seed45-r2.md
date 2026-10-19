# analyze eval obs only object norm01 seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm01-seed45-r2_20260519T050023_result.json`
- **Structured JSON:** [`7abec1a7b76914ee37b2.json`](../../sessions/7a/7abec1a7b76914ee37b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

**seed45-r2 SR = 17% (17/100)**，实验正常完成，registry 已更新为 DONE(success)。

### 与其他 seed 对比

| Seed | SR |
|------|-----|
| seed42 | 19% |
| seed44 | 16% |
| **seed45-r2** | **17%** |
| seed46-r3 | 18% |
| seed48 | 18% |

**5-seed 均值: 17.6%** (原含 seed45-original 14% 时为 17.0%)

标准化后 seed45 从 14% 升至 17%，落入其他 seed 的正常范围 (16%~19%)。原始偏低大概率是 n_rollouts=20 的采样噪声。ε=0.1 配置的整体统计结论不变。

---
