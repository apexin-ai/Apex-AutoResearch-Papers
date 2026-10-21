# ssh check gpu availability

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu-availability_20260517T064049_result.json`
- **Structured JSON:** [`ab290f75e9e530a9e557.json`](../../sessions/ab/ab290f75e9e530a9e557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 空闲状态汇总

| 服务器 | GPU | 型号 | Util | Mem Used | 状态 |
|--------|-----|------|------|----------|------|
| **bjb1-18228** | 0 | RTX 4090 | 21% | 2410 MiB | 忙 |
| | 1 | RTX 4090 | 20% | 2411 MiB | 忙 |
| | **2** | RTX 4090 | 0% | 1 MiB | **空闲** |
| | **3** | RTX 4090 | 0% | 1 MiB | **空闲** |
| **bjb1-32546** | 0 | RTX 4090 | 20% | 2876 MiB | 忙 |
| | 1 | RTX 4090 | 20% | 1907 MiB | 忙 |
| | 2 | RTX 4090 | 17% | 2411 MiB | 忙 |
| | 3 | RTX 4090 | 21% | 2840 MiB | 忙 |
| | **4** | RTX 4090 | 0% | 2 MiB | **空闲** |
| | 5 | RTX 4090 | 21% | 2876 MiB | 忙 |
| **bjb2-28827** | 0 | RTX 4090 | 17% | 2875 MiB | 忙 |
| | 1 | RTX 4090 | 17% | 2875 MiB | 忙 |
| | **2** | RTX 4090 | 0% | 1 MiB | **空闲** |
| | 3 | RTX 4090 | 19% | 2875 MiB | 忙 |
| | 4 | RTX 4090 | 18% | 1942 MiB | 忙 |
| | 5 | RTX 4090 | 19% | 4268 MiB | 忙 |

## 空闲卡汇总

| 服务器 | 空闲 GPU | 数量 |
|--------|----------|------|
| bjb1-18228 | GPU 2, 3 | 2 张 |
| bjb1-32546 | GPU 4 | 1 张 |
| bjb2-28827 | GPU 2 | 1 张 |

**总计 4 张空闲 RTX 4090。**

## Tmux Sessions

| 服务器 | Sessions | 备注 |
|--------|----------|------|
| bjb1-18228 | 0 | 无活跃 session（GPU 0/1 可能是后台进程） |
| bjb1-32546 | 5 | eval-argmin-object-seed46/47, eval-dc-r2, eval-obs-only-object-norm02-seed47, eval-perdof-object-norm03-seed45-r2 |
| bjb2-28827 | 2 | eval-obs-only-object-norm03-seed45-r2, eval-perdof-object-norm02-seed44 |

bjb1-18228 的 GPU 0/1 虽在用但无 tmux session，可能是非 tmux 方式启动的进程。bjb1-32546 和 bjb2-28827 的忙碌 GPU 与 tmux 中的 eval 任务对应。

---
