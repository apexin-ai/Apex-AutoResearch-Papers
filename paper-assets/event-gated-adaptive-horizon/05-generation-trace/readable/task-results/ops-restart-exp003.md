# ops restart exp003

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-exp003_20260513T064314_result.json`
- **Structured JSON:** [`e9e618a31fb0ffef8f34.json`](../../sessions/e9/e9e618a31fb0ffef8f34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程健康运行（1:38 elapsed, CPU 1394%, RSS 2.6GB）。DreamerV3 每个 episode 需要几分钟才会写新 metrics。

汇报如下：

---

**执行结果：**

| 项目 | 状态 |
|------|------|
| 旧 PID 18110 | 已 kill（SIGTERM 成功） |
| 新 PID | **24438**（Python 进程），tmux session: `exp_003_event_gated_v2` |
| 续训起始 step | **~48K → 当前 52000**（从 `latest.pt` checkpoint 续训成功） |
| Hotfix | 已确认：`self._step` + 硬编码 50000/150000 阈值在磁盘上 |
| Phase 2 激活 | **待确认** — step 已过 50K，但 gate metrics 尚未写入新行（上一次 gate_scale log 在 step 45000=0.0）。DreamerV3 gate metrics 写入间隔较长，需再等几分钟看下一个 training metrics dump |

Phase 2 验证需等训练跑到下一个 gate metrics log 周期（预计 step ~55000 左右）。可稍后用 `check-training-status` 或手动 `tail metrics.jsonl` 确认 gate_scale > 0。

---
