# check server status bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-bjb2_20260517T175656_result.json`
- **Structured JSON:** [`a8651e7e03c0271da1b0.json`](../../sessions/a8/a8651e7e03c0271da1b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827
- **GPU 状态**:
  - GPU 0: 1/24564 MiB, 0% — 空闲
  - GPU 1: 1/24564 MiB, 0% — 空闲
  - GPU 2: 4269/24564 MiB, 17% — eval perdof seed47 运行中
  - GPU 3: 1/24564 MiB, 0% — 空闲
  - GPU 4: 3804/24564 MiB, 18% — eval perdof seed46 运行中
  - GPU 5: 1/24564 MiB, 0% — 空闲
- **multi-stage 训练**: **已崩溃** (PID 436926 已死)。Precompute 已完成 (72507/72507 samples, 5043.9s)，加载了 65223 cached samples，模型初始化完成 (MultiScaleCRM 327,522 params)，但在 `wandb.init()` 时报错退出：`No API key configured. Use wandb login to log in.`
- **正在运行的 eval**:
  - PID 389051 (GPU 4): `crm_perdof object seed46 norm0.2` — 进行中，当前在 ketchup task rollout 5/10
  - PID 404983 (GPU 2): `crm_perdof object seed47 norm0.2` — 进行中，当前在 bbq_sauce task rollout 5/10
- **空闲 GPU**: 0, 1, 3, 5

## bjb2-40593
- **GPU 状态**:
  - GPU 0: 4663/24564 MiB, 11% — random selection eval 运行中
- **random selection**: PID 395256 运行中 (已运行 ~5h50m)，完成了 2/10 tasks:
  - alphabet_soup: 0% (0/10)
  - cream_cheese: 10% (1/10)
  - 当前估计还需约 ~23 小时完成剩余 8 tasks
- **空闲 GPU**: 无其他 GPU（此服务器仅 1 张卡）

**需要处理**: bjb2-28827 的 multi-stage 训练需要先配置 wandb API key 再重启。

---
