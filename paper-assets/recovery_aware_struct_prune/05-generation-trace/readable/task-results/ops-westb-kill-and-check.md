# ops westb kill and check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_kill_and_check_20260517T124415_result.json`
- **Structured JSON:** [`c03e1636651e54a1f650.json`](../../sessions/c0/c03e1636651e54a1f650.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### westb-23072

**1. Kill 712124 / 712819**：两个进程已不存在（`No such process`），在 kill 之前就已经退出了。

**2. Random SFT (PID 710113)**：PID 710113 **不在进程列表中**，已退出。

当前 westb-23072 上活跃的 eval 进程：

| PID | GPU | 任务 | 输出文件 | CPU% |
|-----|-----|------|---------|------|
| 710618 | cuda:0 | eval_gsm8k cka_only_20 (n200) | `eval_cka_only_20_n200.json` | 112% |
| 715803 | cuda:0 | eval_gsm8k cka_only_20 (n200) | `eval_postprune_cka_only_20.json` | 133% |
| 680597 | cuda:1 | eval_unstructured_20 (n1319) | `eval_unstructured_20_n1319.json` | (tmux) |

**3. cka_only eval 结果文件**：`eval_cka_only_20_n200.json` **不存在**。PID 710618 仍在运行该 eval，文件尚未生成。

---

### westd-11672

用户询问的 PID 23702 和 23780 **不在** nvidia-smi 进程列表中。当前 GPU 上的实际进程：

| GPU | PID | 显存 | GPU利用率 |
|-----|-----|------|----------|
| 0 | 23707 | 17,658 MiB / 97,887 MiB | 91% |
| 1 | 14556 | 30,078 MiB / 97,887 MiB | 99% |
| 2 | 23785 | 12,780 MiB / 97,887 MiB | 88% |
| 3 | 11896 | 31,518 MiB / 97,887 MiB | 99% |

PID 与用户提供的略有出入（23702→23707, 23780→23785），可能是进程重启过。4 张 GPU 均满载运行中。

---
