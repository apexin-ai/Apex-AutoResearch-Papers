# ssh gpu check post restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_check_post_restart_20260523T034149_result.json`
- **Structured JSON:** [`75907dccea75a0053b40.json`](../../sessions/75/75907dccea75a0053b40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有进程正常运行，无异常。汇总如下：

## westd-32935

| GPU | 显存占用 | 利用率 | PID | 任务 | 状态 |
|-----|---------|--------|-----|------|------|
| cuda:0 | 16747 MiB | 93% | 100223 | GRPO α=3.0 eval_math500 | ✓ 运行中 |
| cuda:1 | 19855 MiB | 99% | 89536 | GRPO α=4.0 eval_math500 | ✓ 运行中 |
| cuda:2 | 16049 MiB | 97% | 83161 | GRPO Random eval_math500 | ✓ 运行中 |
| cuda:3 | 17541 MiB | 98% | 86243 | GRPO α=1.0 eval_math500 | ✓ 运行中 |

## westb-23072

| GPU | 显存占用 | 利用率 | PID | 任务 | 状态 |
|-----|---------|--------|-----|------|------|
| cuda:0 | 19277 MiB | 92% | 250766 | Qwen-Math SFT CKA-only eval_math500 | ✓ 运行中 |
| cuda:1 | 17551 MiB | 98% | 262771 | GRPO α=0.5 eval_math500 | ✓ 运行中 |

全部 6 个 eval 进程在服务重启后均存活，GPU 利用率 92-99%，无异常。

---
