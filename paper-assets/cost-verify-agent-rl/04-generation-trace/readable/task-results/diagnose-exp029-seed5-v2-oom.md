# diagnose exp029 seed5 v2 oom

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_seed5_v2_oom_20260521T120913_result.json`
- **Structured JSON:** [`070c7d7990da74da254e.json`](../../sessions/07/070c7d7990da74da254e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集足够信息。诊断结果：

## exp029_seed5_v2 OOM 诊断报告

**OOM 位置**：Step 12/15（73%→80%），`update_actor` 阶段的 `loss.backward()`（策略梯度反向传播），`dp_actor.py:469`。

**Process 196655 身份**：seed5_v2 自己的 Ray worker（`ray::WorkerDict.actor_rollout_generate_sequences`），隶属 Ray session `session_2026-05-21_19-57-18`（raylet pid=190494）。不是 seed6 泄漏。seed5 主进程崩溃退出后，该 rollout worker 和 raylet 未被清理，仍占用 GPU 1 共 17.5 GiB。

**GPU 0/1 当前状态**：
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 0 MiB | 已释放（seed5 主进程退出），但 util 100% 为残留读数 |
| 1 | 17,561 MiB | 被孤儿 Ray worker 196655 占用 |
| 2,3 | 96 GiB each | seed6_v3 正常运行中 |

**能否直接重试**：不能。需先杀掉 orphan Ray 进程（pid 196655 + raylet 190494 + head 189089）释放 GPU 1，然后才能重启 seed5。

**建议操作**：
```bash
kill -9 196655 190494 189089   # 清理孤儿 Ray 进程树
```
清理后 GPU 0/1 即可复用。

---
