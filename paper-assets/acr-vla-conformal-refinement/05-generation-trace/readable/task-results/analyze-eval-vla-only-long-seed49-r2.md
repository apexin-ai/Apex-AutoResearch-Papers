# analyze eval vla only long seed49 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-vla-only-long-seed49-r2_20260520T103241_result.json`
- **Structured JSON:** [`d91f28ed884962ec89d7.json`](../../sessions/d9/d91f28ed884962ec89d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## eval-vla-only-long-seed49-r2 结果

**Overall SR: 16.0% (16/100)** — 与原 seed49 (SR=0.16) 完全一致。

### Per-task 明细

| Task | SR |
|------|-----|
| KITCHEN_SCENE3 (stove + moka pot) | 90% |
| LIVING_ROOM_SCENE5 (mugs + plates) | 30% |
| LIVING_ROOM_SCENE6 (mug + pudding) | 20% |
| STUDY_SCENE1 (book + caddy) | 10% |
| KITCHEN_SCENE6 (mug + microwave) | 10% |
| LIVING_ROOM_SCENE2 x2, KITCHEN_SCENE4, LIVING_ROOM_SCENE1, KITCHEN_SCENE8 | 0% |

### 分析

- **与原 seed49 对比**：re-run SR=0.16，与被移除的原始数据 SR=0.16 完全一致，确认原始结果是可复现的。
- **范围合理性**：16% 落在 Long VLA-only 预期范围 (~10-20%) 内。
- **对 Long OOD 数据池的影响**：这个 clean re-run 可以替换被移除的原始 seed49 数据重新纳入分析。由于 SR 数值完全相同（0.16），对 D081 中 CRM vs VLA marginal (+2.3pp, t p=0.049, MW-U p=0.061) 的结论不会产生变化。

### Conclusion: **success**

Clean re-run 确认原始结果可复现，数据溯源问题已解决。Registry 已更新 (status=DONE, conclusion=success, metrics.sr=0.16)。

---
