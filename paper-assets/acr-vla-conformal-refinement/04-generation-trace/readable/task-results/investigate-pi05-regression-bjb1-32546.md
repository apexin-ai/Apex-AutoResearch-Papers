# investigate pi05 regression bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_pi05-regression-bjb1-32546_20260528T063015_result.json`
- **Structured JSON:** [`78d8289fa51e45eca093.json`](../../sessions/78/78d8289fa51e45eca093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 tmux sessions 对应 6 块 GPU，全部占用：

| GPU | 显存占用 | 可能对应的 session |
|-----|---------|-------------------|
| cuda:0 | 10353/24564 MiB | Pi05 session |
| cuda:1 | 10353/24564 MiB | Pi05 session |
| cuda:2 | 10835/24564 MiB | Pi05 session |
| cuda:3 | 2439/24564 MiB | SmolVLA session |
| cuda:4 | 3080/24564 MiB | SmolVLA session |
| cuda:5 | 3080/24564 MiB | SmolVLA session |

**结论：bjb1-32546 上 3 个 Pi05 实验均正常运行（obs_dim=2048，SR 远高于 0%），不受 regression 影响，不应 kill。6 块 GPU 全部占满，没有空闲 GPU 可以部署新实验。**

如果仍需部署 3 个 SmolVLA 候选实验（smolvla-tau045-spatial-s42、eval-supp-long-vla-only-s44、eval-supp-long-vla-only-s42），需要另选服务器或等当前实验完成。需要我查看其他可用服务器吗？

---
