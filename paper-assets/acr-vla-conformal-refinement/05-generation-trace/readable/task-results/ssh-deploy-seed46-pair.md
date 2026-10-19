# ssh deploy seed46 pair

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-seed46-pair_20260516T155735_result.json`
- **Structured JSON:** [`f213a8b269eb9b0d9e49.json`](../../sessions/f2/f213a8b269eb9b0d9e49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器都没有空闲 GPU：

| 服务器 | GPU 显存占用 |
|--------|-------------|
| bjb1-32546 | 1906-3343 MiB（6/6 占用） |
| bjb2-28827 | 3768-5664 MiB（6/6 占用） |

所有 12 个白名单 GPU 均在使用中，无法部署 seed46 配对实验。需要等现有实验完成释放 GPU 后再部署。

---
