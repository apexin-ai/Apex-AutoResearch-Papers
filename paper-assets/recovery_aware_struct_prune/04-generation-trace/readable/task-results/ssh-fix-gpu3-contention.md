# ssh fix gpu3 contention

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_gpu3_contention_20260523T223849_result.json`
- **Structured JSON:** [`457a9ff505559cb534fe.json`](../../sessions/45/457a9ff505559cb534fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况有变：

**GPU 3 当前状态**: 只有 PID 168451 (GRPO cka_only)，PID 170326 (SFT RASP) 已经不在了 — 进程已死，可能因 GPU 竞争 OOM。

**GPU 1 状态**: 只剩 PID 168524 (grpo_rasp_alpha2p0)，符合预期（170179 已被 kill）。

**四卡概览**:
| GPU | PID | 显存 | 利用率 |
|-----|-----|------|--------|
| 0 | 166245 | 16824MiB | 96% |
| 1 | 168524 | 16732MiB | 97% |
| 2 | 171964 | 16732MiB | 91% |
| 3 | 168451 | 16846MiB | 98% |

PID 170326 (SFT RASP) 已死，GPU 3 上的竞争已自行消除。现在 kill 168451 会让 GPU 3 完全空闲，而 GRPO 已跑了 ~50min 的进度也会丢失。

还要 kill 168451 吗？还是让它跑完？

---
