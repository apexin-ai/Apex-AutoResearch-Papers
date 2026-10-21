# ops gpu collision check seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-collision-check-seed44_20260516T013717_result.json`
- **Structured JSON:** [`6199372295d2a7ca85db.json`](../../sessions/61/6199372295d2a7ca85db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 冲突确认

**cuda:2 和 cuda:3 上 r2 和 r3 同时在跑，存在 GPU 冲突。**

### nvidia-smi 进程详情

| GPU | PID | 显存 | 来源 | 模式 |
|-----|-----|------|------|------|
| cuda:2 | 428411 | 5645MiB | **r2** (428406 子进程) | crm_obs_only |
| cuda:2 | 431194 | 5645MiB | **r3** (431189 子进程) | crm_obs_only |
| cuda:3 | 428122 | 5609MiB | **r2** (428117 子进程) | reconvla |
| cuda:3 | 430990 | 5609MiB | **r3** (430985 子进程) | reconvla |

### 状态

- **4 个 wrapper PID 全部存活**，r2 启动于 09:32，r3 启动于 09:34
- cuda:2 占用 11324MiB/24564MiB，利用率 99%
- cuda:3 占用 11252MiB/24564MiB，利用率 98%
- 每个进程约 5.6GB，两个进程合计没有 OOM（24GB 卡装得下两个），但 GPU 计算资源在互相抢占
- 两组实验写同一个输出文件（`logs/eval_object_reconvla_seed44.json` 和 `logs/eval_object_obs_only_norm02_seed44.json`），**结果会互相覆盖**

### 结论

r2 没死，r3 也在跑 → **两组实验在 cuda:2 和 cuda:3 上完全重叠**。需要 kill 掉其中一组（建议 kill r2，因为 r3 更新），否则两组结果都不可信。

---
