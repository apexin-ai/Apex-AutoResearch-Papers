# ops queue status and resume

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_queue_status_and_resume_20260522T235451_result.json`
- **Structured JSON:** [`3a4652f3ded175cccb70.json`](../../sessions/3a/3a4652f3ded175cccb70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. queue_runner.log 进度

| Item | 任务 | 状态 |
|------|------|------|
| **[1/8]** | SS s42 eval | **DONE** — 跳过（`results/d048_ss_s42/` 已有 `ss_s42_ar_n50.json`, `base_ar_n50.json` 等） |
| **[2/8]** | AR N=50 existing s42 checkpoints (4 sub-tasks) | **正在运行** |
| ↳ [1/4] | TG s42 AR N=50 | DONE — 结果已保存 `results/d048_ar_n50_existing/tg_s42_ar_n50.json` |
| ↳ [2/4] | UG s42 AR N=50 | **正在运行** — beta=3.0, Conv 20/50 |
| ↳ [3/4] | LO s42 AR N=50 | 未开始 |
| ↳ [4/4] | PCGrad s42 AR N=50 | 未开始 |
| **[3/8]** | SS s123 train | 未开始 |
| **[4/8]** | SS s456 train | 未开始 |
| **[5/8]** | Base s123 train | 未开始 |
| **[6/8]** | Base s456 train | 未开始 |
| **[7/8]** | TG s123 train | 未开始 |
| **[8/8]** | TG s456 train | 未开始 |

### 2. GPU 状态
- **正在使用**: PID 51492, 22336 MiB, 56% utilization
- queue_runner 正在执行 AR eval，GPU 不空闲

### 3. 可复用的旧 checkpoint
- **`checkpoints/tg_v8b_ss_s123/`** — 有 epoch_0/1/2 + gate_params.pt + lora，可用于 item [3/8] SS s123（如果 queue_runner 包含了复用逻辑）

### 4. 未启动任何新任务
GPU 正忙于 queue_runner 的 [2/8] AR N=50 eval（UG s42, beta=3.0 进行到 Conv 20/50），不需要干预。AR eval 50 convs × 3 betas × 3 remaining sub-tasks 预计还需 1-2 小时完成 item [2/8]，之后 queue_runner 会自动继续 [3/8]-[8/8]。

---
