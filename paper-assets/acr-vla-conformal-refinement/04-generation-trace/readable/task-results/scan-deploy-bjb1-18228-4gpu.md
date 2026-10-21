# scan deploy bjb1 18228 4gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan-deploy_bjb1-18228-4gpu_20260523T124520_result.json`
- **Structured JSON:** [`db101ef41b27fa5a8774.json`](../../sessions/db/db101ef41b27fa5a8774.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pi0.5 precompute 仍在全速运行，4 张卡全被占用，无法部署实验。**

各卡状态：

| GPU | 任务 | 进度 | 预计剩余 |
|-----|------|------|---------|
| cuda:0 | object precompute | 30800/72507 (42%) | ~22h |
| cuda:1 | spatial precompute | 29500/60250 (49%) | ~17h |
| cuda:2 | goal precompute | 29500/61728 (48%) | ~18h |
| cuda:3 | long precompute | 30700/136090 (23%) | ~56h |

Director 20 分钟前观察到的 42-49% 利用率就是这些 precompute 进程的正常 GPU 利用率（Pi0.5 推理 ~25% GPU util），并非空闲。4 张卡每张都占用 ~9.8GB 显存。

按规则不能 kill precompute。Long suite s43 实验部署需要等 precompute 完成。spatial 和 goal 预计最早 ~明天中午完成，long 最慢需到后天。

---
