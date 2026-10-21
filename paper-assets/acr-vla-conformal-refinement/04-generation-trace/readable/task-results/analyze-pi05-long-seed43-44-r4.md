# analyze pi05 long seed43 44 r4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-long-seed43-44-r4_20260522T164138_result.json`
- **Structured JSON:** [`0138d884199d86ccfd7b.json`](../../sessions/01/0138d884199d86ccfd7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**π0.5 VLA-only LIBERO-Long Baseline**

| Seed | Overall SR |
|------|-----------|
| 42 | 94.0% |
| 43 | **95.5%** (191/200) |
| 44 | **95.5%** (191/200) |
| **3-seed 均值** | **94.83%** |

两个实验均正常完成（EXIT_CODE=0），结果与 seed42 高度一致。唯一困难 task 是 KITCHEN_SCENE8 (moka pots on stove)，seed43=80%、seed44=70%，其余 9 个 task 均 ≥90%。Baseline 非常 robust。

两个实验 registry 已更新为 DONE/success，摘要已写入 memory.md。

---
