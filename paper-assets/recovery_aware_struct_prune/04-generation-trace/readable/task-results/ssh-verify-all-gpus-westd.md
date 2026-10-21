# ssh verify all gpus westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_all_gpus_westd_20260523T222345_result.json`
- **Structured JSON:** [`859580e96a24f794bf7c.json`](../../sessions/85/859580e96a24f794bf7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已清理完毕。当前各 GPU 状态：

| GPU | PID | 进程 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 166245 | `eval_math500` — sft_standard_25_fixed_v2 | 16824 MiB | 98% |
| 1 | 168524 | `eval_math500` — grpo_rasp_alpha2p0_20_fixed | 16732 MiB | 98% |
| 2 | 171964 | `eval_math500` — sft_rasp_alpha2p0_20_fixed | 16732 MiB | 98% |
| 3 | 168451 | `eval_math500` — grpo_cka_only_25_fixed | 16846 MiB | 98% |

GPU 3 的入侵进程 `sft_rasp_alpha0p5_20` (PID 170326) 已 kill，显存从 33594 MiB 降回 16855 MiB。4 张卡现在每张都只有一个进程，运行正常。

---
