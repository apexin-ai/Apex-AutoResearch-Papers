# ssh check all servers status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_servers_status_20260523T173555_result.json`
- **Structured JSON:** [`ae1c1167a50693f357d6.json`](../../sessions/ae/ae1c1167a50693f357d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32935
**GPU 状态:**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 87% | 12,867 / 97,887 MiB |
| 1 | 98% | 17,541 / 97,887 MiB |
| 2 | 92% | 19,251 / 97,887 MiB |
| 3 | 98% | 19,251 / 97,887 MiB |

**进程存活:**
| PID | 实验 | 状态 | 运行时间 | 进度 |
|-----|------|------|----------|------|
| 142477 | eval_math500_grpo_standard_20_fixed | RUNNING | 2h32m | 183/500 (37%) |
| 142638 | eval_math500_sft_standard_20_fixed | RUNNING | 2h32m | 170/500 (34%) |
| 145167 | eval_math500_grpo_rasp_alpha1p0_20_fixed | RUNNING | 1h51m | 177/500 (35%) |
| 147914 | eval_math500_sft_rasp_alpha1p0_20_fixed | RUNNING | 1h06m | 223/500 (45%) |

**已完成 eval 结果:** 无，全部仍在运行中

**空闲 GPU:** 无

---

## westb-23072
**GPU 状态:**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 100% | 55,539 / 97,887 MiB |
| 1 | 99% | 17,039 / 97,887 MiB |

**进程存活:**
| PID | 实验 | 状态 | 运行时间 | 进度 |
|-----|------|------|----------|------|
| 309964 | grpo_random_20_retrain_v2 | RUNNING | 1h19m | 39/100 steps (39%), ~114s/step |
| 306963 | eval_math500_sft_cka_only_20_fixed_v2 | RUNNING | 1h51m | 232/500 (46%) |

**已完成 eval 结果:** 无，仍在运行中

**grpo_random_20_retrain_v2 进度:** 39/100 steps，预计还需约 ~2h

**空闲 GPU:** 无

---

**预计完成时间估算：**
- sft_rasp_alpha1p0_20_fixed (45%) 最快，约 1-1.5h 后完成
- sft_cka_only_20_fixed_v2 (46%) 类似，约 1.5h
- grpo 两个 eval (~35-37%) 约 3-4h（GRPO 模型生成更长，每题耗时更高）
- grpo_random_20_retrain_v2 训练约 2h 后完成

---
