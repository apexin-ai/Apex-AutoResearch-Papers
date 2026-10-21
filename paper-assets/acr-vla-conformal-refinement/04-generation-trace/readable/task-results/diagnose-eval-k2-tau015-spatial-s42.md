# diagnose eval k2 tau015 spatial s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-k2-tau015-spatial-s42_20260525T004449_result.json`
- **Structured JSON:** [`df02b51527060de2967a.json`](../../sessions/df/df02b51527060de2967a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断已写入 memory.md。

**总结：** `eval-k2-tau015-spatial-s42` 超时纯粹因为 timeout=7200s (2h) 不够。spatial benchmark 10 tasks × 20 rollouts = 200 rollouts，每 rollout ~80s，需 ~4.5h。实验跑了 45% (90/200 rollouts) 就被 kill。已完成的 4 个 task 成绩很好 (90%-95%)，无任何错误或资源问题。重试建议 timeout=18000s (5h)，等当前 tau=0.10 跑完后再启动。

---
