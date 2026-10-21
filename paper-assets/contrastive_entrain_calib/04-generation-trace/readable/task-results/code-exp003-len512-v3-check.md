# code exp003 len512 v3 check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003-len512-v3-check_20260525T073550_result.json`
- **Structured JSON:** [`ba42ebb70ef0fa8bc8b0.json`](../../sessions/ba/ba42ebb70ef0fa8bc8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## 报告：exp-003-len512-v3

| 项目 | 结果 |
|------|------|
| **状态** | **被 kill**（PID 553700 已不存在，日志无 error/traceback） |
| **进度** | 3830/8000 步（48%），运行 ~49.7 小时 |
| **最后 checkpoint** | checkpoint-3500（2026-05-25 07:49） |
| **日志中断时间** | 2026-05-25 12:10:04 |

**Checkpoint 列表：** 500, 1000, 1500, 2000, 2500, 3000, 3500

**关键 Metrics（最近 window）：**
- `reward_mean`: 0.47~0.64，均值约 0.54，**与 step 100 时的 0.52 基本持平，无上升趋势**
- `kl`: 0.014（从初始 0.0005 涨上来，说明 policy 已偏移）
- `clipped_ratio`: 0.95-0.98（绝大多数生成撞 512 上限）
- `entropy`: 0.30-0.33（较低）
- `loss`: ~0.001（接近零）

**结论：killed**

进程在 step 3830 处被外部 kill（可能是之前 SSH 断连期间服务器重启或手动终止）。之前 registry 记录的 "SSH check failed" 实际上是监控连不上服务器，而非训练本身报错。

从 metrics 看，即使训练未被中断，效果也不乐观——3800 步后 reward 无明显提升，clipped_ratio 极高说明模型几乎总是生成到最大长度。假设"加长 max_completion_length 能缓解 reward 失败"**暂时不成立**。

---
