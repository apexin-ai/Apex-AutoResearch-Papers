# ssh urgent status westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_westd_20260523T183555_result.json`
- **Structured JSON:** [`c3679142e1523f45eb32.json`](../../sessions/c3/c3679142e1523f45eb32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32935 状态

**GPU:**
| GPU | 显存占用 | 总显存 | 利用率 | 状态 |
|-----|---------|--------|--------|------|
| cuda:0 | 0 MiB | 97887 MiB | 0% | **空闲** |
| cuda:1 | 17541 MiB | 97887 MiB | 98% | 占用 |
| cuda:2 | 19251 MiB | 97887 MiB | 98% | 占用 |
| cuda:3 | 19251 MiB | 97887 MiB | 97% | 占用 |

**空闲 GPU:** cuda:0

**运行中 (3 个 eval):**
| PID | GPU | 运行时长 | 实验 | 进度 |
|-----|-----|---------|------|------|
| 142477 | cuda:2 | 3h32m | eval_math500_grpo_standard_20_fixed | 252/500 (50%) |
| 142638 | cuda:3 | 3h31m | eval_math500_sft_standard_20_fixed | 241/500 (48%) |
| 145167 | cuda:1 | 2h50m | eval_math500_grpo_rasp_alpha1p0_20_fixed | 280/500 (56%) |

**已完成 eval:**
- **eval_math500_sft_rasp_alpha1p0_20_fixed**: accuracy=**21.6%**, correct=108/500, EXIT_CODE=0

**PID 147914 (eval_math500_sft_rasp_alpha1p0_20_fixed):** 已结束，正常退出

**sft_standard_25 checkpoint:** 存在，`/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors`，10.8GB

**预计剩余时间:** 3 个运行中的 eval 按当前速度还需约 2.5-3.5 小时完成。

---
