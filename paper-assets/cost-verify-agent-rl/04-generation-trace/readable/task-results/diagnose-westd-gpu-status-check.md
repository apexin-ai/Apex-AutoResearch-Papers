# diagnose westd gpu status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-gpu-status-check_20260519T003455_result.json`
- **Structured JSON:** [`1933201547ad29929549.json`](../../sessions/19/1933201547ad29929549.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-47453 全部 4 张 GPU 状态：全部在用**

| GPU | 利用率 | 显存 (MiB) | 温度 | PID | 进程 | 运行时间 |
|-----|--------|-----------|------|-----|------|---------|
| 0 | 100% | 96949 / 97887 | 59°C | 421310 | actor_rollout_update_actor | 1h36m |
| 1 | 100% | 97041 / 97887 | 55°C | 421311 | actor_rollout_update_actor | 1h36m |
| 2 | 99% | 36059 / 97887 | 67°C | 41416 | actor_rollout_compute_log_prob | 6h58m |
| 3 | 96% | 36059 / 97887 | 69°C | 41417 | actor_rollout_compute_log_prob | 6h58m |

**cuda:0,1 — exp029_seed2_westd_resume**
- 主进程 PID 414163 存活，运行 1h36m
- 当前处于 **training 阶段，step 26**（不是 eval）
- step 25 已完成 checkpoint 保存（`/root/autodl-tmp/checkpoints/exp029-seed2/global_step_25/`）
- train/success: 73.4%，pass@8: 100%

**cuda:2,3 — hsweep_h10_seed1**
- PID 41416, 41417，运行 6h58m
- 进程类型为 `actor_rollout_compute_log_prob`（ref model log prob 计算）
- 显存 36GB/卡，利用率 96-99%

结论：Director 说 2/4 在用不准确，**4 张卡全部满载运行**。

---
