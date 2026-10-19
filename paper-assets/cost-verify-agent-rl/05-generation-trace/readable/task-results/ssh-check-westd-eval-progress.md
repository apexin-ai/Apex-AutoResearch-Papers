# ssh check westd eval progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_eval_progress_20260523T011126_result.json`
- **Structured JSON:** [`e5a75b8cfcfc36111f12.json`](../../sessions/e5/e5a75b8cfcfc36111f12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | PID | 状态 | 进度/结果 |
|------|-----|------|-----------|
| seed100 step10 OOD eval | 320618 | **失败** (EXIT_CODE=1) | vLLM 启动失败：cuda:0 仅 5.26/94.97 GiB 空闲，需要 80.73 GiB |
| seed7 high_kl step5 eval v3 | 310594 | **完成** (EXIT_CODE=129) | 134 episodes 评估完成，结果见下 |
| seed7 high_kl step7 eval v3 | 303608 | **失败** (EXIT_CODE=1) | vLLM 启动失败：cuda:0 仅 79.36/94.97 GiB 空闲，需要 80.73 GiB（差 1.37 GiB） |

**step5 OOD 评估结果（seed7 high_kl, 134 episodes）：**

| 指标 | 值 |
|------|-----|
| pass@1 / success | **9.70%** |
| action_is_valid | 65.18% |
| action_is_effective | 99.99% |
| num_actions (avg) | 45.92 |
| best@2 | 1.83 |
| best@4 | 3.51 |
| best@8 | 5.80 |
| best@16 | 8.33 |
| best@32 | 9.71 |
| best@64 | 10.0 |

**失败原因分析：** step10 和 step7 都报 `cuda:0` 内存不足——说明它们没有正确绑定到指定 GPU（cuda:0 和 cuda:3），vLLM 默认尝试使用 cuda:0。需要通过 `CUDA_VISIBLE_DEVICES` 确保 GPU 隔离后重跑。

---
