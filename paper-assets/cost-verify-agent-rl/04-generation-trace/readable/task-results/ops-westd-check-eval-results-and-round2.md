# ops westd check eval results and round2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_check_eval_results_and_round2_20260522T095925_result.json`
- **Structured JSON:** [`349b651b2193dcccb2c8.json`](../../sessions/34/349b651b2193dcccb2c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认正常运行。4 个 tmux session 活跃，4 个 `train.py` 进程在运行。

## 汇总

### Round 1 OOD Eval 结果（134 episodes）

| GPU | Checkpoint | OOD Success | action_is_valid | response_length | 状态 |
|---|---|---|---|---|---|
| 0 | SFT baseline | **5.97%** | 67.5% | 7718 | **完成** |
| 1 | seed8_step5 | **13.4%** | 58.2% | 6051 | **完成** |
| 2 | seed2048_step5 | **8.21%** | 59.4% | 6453 | **完成** |
| 3 | intervention_c_step5 | — | — | — | **运行中** |

### Round 2 启动状态

| GPU | Checkpoint | Config | tmux | 进程状态 |
|---|---|---|---|---|
| 0 | intervention_c_step7 | `_alfworld_intervention_c_step7_ood_eval` (新建) | ragen_eval_gpu0 | 加载中 (8149 MiB) |
| 1 | high_kl_step5 | `_alfworld_seed7_high_kl_step5_ood_eval` | ragen_eval_gpu1 | 启动中 |
| 2 | high_kl_step7 | `_alfworld_seed7_high_kl_step7_ood_eval` | ragen_eval_gpu2 | 启动中 |
| 3 | intervention_c_step5 (Round 1) | 继续运行 | ragen_eval_gpu3 | 活跃 (90467 MiB) |

### 当前 GPU 状态
- GPU 0: 8149 MiB（模型加载中）
- GPU 1: 3 MiB（初始化中）
- GPU 2: 3 MiB（初始化中）
- GPU 3: 90467 MiB（Round 1 eval 持续运行）

---
