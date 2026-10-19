# deploy bjb1 32546 k20 three seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-k20-three-seeds_20260519T150308_result.json`
- **Structured JSON:** [`f89cf32f90060a3f565a.json`](../../sessions/f8/f89cf32f90060a3f565a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:2, cuda:3, cuda:5 均被占用**，正在跑 `random_selection` K=5 评估实验：

| GPU | PID | 实验 | 显存 |
|-----|-----|------|------|
| cuda:2 | 942029 | random_selection K=5 seed44 | 3309 MiB |
| cuda:3 | 942099 | random_selection K=5 seed45 | 3309 MiB |
| cuda:5 | 939548 | random_selection K=5 seed42 | 2372 MiB |

cuda:1 完全空闲 (0%, 2 MiB)。其余 GPU (0, 4) 也有进程。

如何处理？选项：
1. **等 K=5 跑完再部署**（K=5 通常几小时）
2. **Kill 掉 random_selection 实验，立即部署 K=20**
3. **换用其他空闲 GPU**（目前只有 cuda:1 空闲，不够 3 个实验）

---
