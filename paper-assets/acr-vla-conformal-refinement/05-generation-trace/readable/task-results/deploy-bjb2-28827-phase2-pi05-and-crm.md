# deploy bjb2 28827 phase2 pi05 and crm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-phase2-pi05-and-crm_20260525T090556_result.json`
- **Structured JSON:** [`51a9eca03933260aabb5.json`](../../sessions/51/51a9eca03933260aabb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 GPU 全部占满，部署完成。

| GPU | 实验 | PID | 显存 | 利用率 |
|-----|------|-----|------|--------|
| cuda:0 | SmolVLA CRM Spatial s47 | 730605 | 6,287 MiB | 23% |
| cuda:1 | π0.5 Adaptive Goal s43 | 732023 | 13,947 MiB | 20% |
| cuda:2 | π0.5 Adaptive Object s42 | 732469 | 14,069 MiB | 18% |
| cuda:3 | π0.5 VLA-only Object s43 | 732906 | 14,069 MiB | 18% |
| cuda:4 | π0.5 Adaptive Object s43 | 733346 | 14,069 MiB | 19% |
| cuda:5 | π0.5 VLA-only Goal s44 | 733787 | 13,947 MiB | 22% |

SmolVLA CRM ~6.3GB，π0.5 模型 ~14GB，符合预期。6 个实验均已在 registry 注册为 RUNNING。

---
