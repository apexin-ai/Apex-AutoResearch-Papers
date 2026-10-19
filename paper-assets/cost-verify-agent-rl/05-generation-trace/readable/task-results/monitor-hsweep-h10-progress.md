# monitor hsweep h10 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_hsweep_h10_progress_20260524T065505_result.json`
- **Structured JSON:** [`e6a6096b84089300da30.json`](../../sessions/e6/e6a6096b84089300da30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：hsweep_h10_seed2 已挂死

**状态：异常 — 进程存活但训练已停滞**

| 项目 | 状态 |
|------|------|
| PID 95503 | 存活（6h47m），CPU 0.4% |
| GPU 0 | 利用率 0%，显存 55GB/98GB 占用 |
| 当前 step | **0/5**（未开始任何训练 step） |
| 日志最后更新 | 02:36:27（约6.5小时前） |

**关键发现：**

1. Step 0 validation 完成后，进度条刚打印 `Training Progress: 0%|  | 0/5`
2. 随即 Ray 子进程（PID 42504）收到 **SIGTERM**，导致 worker 被杀
3. 主进程 95503 仍存活但无任何新输出，已挂死 6.5 小时
4. 日志文件自 02:36:27 后未写入任何内容

**Step 0 初始 eval 指标（基线，32 episodes）：**
- success: **12.5%**
- pass@1: 12.5%
- reward mean@1455: 0.378
- action_is_valid: 76.1%
- action_is_effective: 97.2%

**结论：** 进程需要 kill 后重启。训练从未实际开始（0/5 steps），只完成了初始 validation。SIGTERM 的来源需要排查（可能是其他进程冲突或 OOM killer）。

---
