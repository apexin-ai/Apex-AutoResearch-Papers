# transfer crm checkpoints to new servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_transfer_crm-checkpoints-to-new-servers_20260515T024547_result.json`
- **Structured JSON:** [`1fa5d7897eab969b9d9f.json`](../../sessions/1f/1fa5d7897eab969b9d9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint Transfer Results

| File | Source MD5 (bjb1-18228) | bjb1-32546 MD5 | bjb2-28827 MD5 | Match |
|------|------------------------|----------------|----------------|-------|
| obs_only/crm_best.pt | cecc5e5f636dcfebfe20e79a7deb1cf3 | cecc5e5f636dcfebfe20e79a7deb1cf3 | cecc5e5f636dcfebfe20e79a7deb1cf3 | ✓ |
| scalar_unc/crm_best.pt | 17ae4594d7b503cc0fe8ca89ab71c057 | 17ae4594d7b503cc0fe8ca89ab71c057 | 17ae4594d7b503cc0fe8ca89ab71c057 | ✓ |
| perdof/crm_best.pt | ed7f309f8fb3c39c549c430b1d529fc3 | ed7f309f8fb3c39c549c430b1d529fc3 | ed7f309f8fb3c39c549c430b1d529fc3 | ✓ |

perdof checkpoint 两台目标服务器上已存在且 MD5 与源一致，无需额外操作。

---
