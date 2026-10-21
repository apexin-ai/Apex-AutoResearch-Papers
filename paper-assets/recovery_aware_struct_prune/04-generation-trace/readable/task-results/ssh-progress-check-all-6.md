# ssh progress check all 6

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_progress_check_all_6_20260524T035446_result.json`
- **Structured JSON:** [`2c0fb10a5a82dad5f543.json`](../../sessions/2c/2c0fb10a5a82dad5f543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | Server:GPU | PID | 进度 | 速度 | ETA (UTC) | 状态 |
|------|-----------|-----|------|------|-----------|------|
| sft_standard_25_fixed_v2 | westd:0 | 166245 | **381/500** (76%) | ~85s/it | ~14:43 | 正常运行 |
| sft_rasp_alpha0p5_20_fixed | westd:1 | 184381 | **101/500** (20%) | ~83s/it | ~21:09 | 正常，已开始推理 |
| sft_rasp_alpha4p0_20_fixed | westd:2 | 185975 | **64/500** (13%) | ~75s/it | ~21:00 | 正常，已开始推理 |
| sft_standard_20_fixed_v4 | westd:3 | 182208 | **139/500** (28%) | ~74s/it | ~19:18 | 正常运行 |
| grpo_random_20_fixed | westb | 330254 | **315/500** (63%) | ~66s/it | ~15:18 | 正常运行 |
| sft_random_20_fixed_v3 | westb | 335348 | **241/500** (48%) | ~89s/it | ~18:18 | 正常运行 |

**特别关注项：**
- **westd:3 sft_standard_20_fixed_v4** — 显存 17532 MiB，无报错，已稳定跑到 139/500。本次正常。
- **westd:1 sft_rasp_alpha0p5_20_fixed** — 模型已加载，推理中 (101/500)，显存 17508 MiB 正常。
- **westd:2 sft_rasp_alpha4p0_20_fixed** — 模型已加载，推理中 (64/500)，显存 17518 MiB 正常。

注意：westb 日志实际路径在 `/root/autodl-tmp/recovery_aware_struct_prune/logs/`，不是 `~/runs/`。预计最先完成的是 **sft_standard_25_fixed_v2**（~14:43 UTC），最后完成的是 **sft_rasp_alpha0p5_20_fixed**（~21:09 UTC）。

---
