# ops verify 22k eval and check s1

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_22k_eval_and_check_s1_20260527T021619_result.json`
- **Structured JSON:** [`80f0741ea3077210f268.json`](../../sessions/80/80f0741ea3077210f268.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/verify_22k_eval_report.md`。

核心结论：
- **22K eval 数据完全验证通过**，所有 Reviewer 报告值匹配：CAR=60.5%, TSR=45.5%, frozen=0%, 200 episodes 全部有效
- **s1 22K checkpoint 存在**，已进一步推进到 24000 步
- **cuda:0 空闲**，可用于后续 eval
- **s0 当前在 step 24000**，距 30K 目标还差约 6000 步，仍在 cuda:1-3 上训练

---
