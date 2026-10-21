# investigate pi05 object s43 conflict

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_pi05-object-s43-conflict_20260524T192714_result.json`
- **Structured JSON:** [`f7779a61c937e918a48c.json`](../../sessions/f7/f7779a61c937e918a48c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册。

**最终结论：不更新 registry 的 metrics。** r4=98.5% 是 `n_action_steps=10` 范式下的有效结果，v2=86.5% 是 CUDA OOM 崩溃废结果。论文使用时注意评估范式一致性——如果 baseline 表用 closed-loop，则引用 r3=81.5%；如果用 chunked 范式，则用 r4=98.5%。

---
