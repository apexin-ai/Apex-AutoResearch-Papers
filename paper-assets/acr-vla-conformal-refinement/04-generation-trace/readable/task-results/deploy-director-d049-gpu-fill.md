# deploy director d049 gpu fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_director-d049-gpu-fill_20260517T132950_result.json`
- **Structured JSON:** [`ad12e4146107077c6dc1.json`](../../sessions/ad/ad12e4146107077c6dc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

**成功部署 4 个实验：**
- **Exp 4** (obs_only ε=0.05 seed43) → bjb1-18228 cuda:0, PID 631667
- **Exp 5** (perdof ε=0.2 seed45) → bjb1-18228 cuda:1, PID 631687
- **Exp 2** (K=5 obs_only seed42) → bjb1-18228 cuda:2, PID 633662（另一 worker 部署）
- **Exp 3** (K=20 obs_only seed42) → bjb1-18228 cuda:3, PID 636638（首次失败，已重新提交）

**无需部署：**
- **Exp 1** (random selection seed42): 已在 bjb2-40593 cuda:0 运行中 (PID 395256, ~1.5h)
- **Exp 6** (obs_only ε=0.03 seed43): Registry 显示已 DONE

**偏差：** Exp 2、3 原计划部署到 bjb2-28827 cuda:1/2，但该 GPU 被 perdof seed45 (29h!) 和 seed47 (~2h) 占用，改部署到 bjb1-18228。bjb1-18228 现有 4 个 LIBERO 进程（达上限）。

**需关注：** bjb2-28827 cuda:1 的 perdof seed45 已跑 29 小时，可能 stuck。

---
