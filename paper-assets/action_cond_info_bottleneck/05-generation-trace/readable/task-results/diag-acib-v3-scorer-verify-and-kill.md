# diag acib v3 scorer verify and kill

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_acib_v3_scorer_verify_and_kill_20260516T000340_result.json`
- **Structured JSON:** [`b2a78d2b4272b3826bb8.json`](../../sessions/b2/b2a78d2b4272b3826bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 497308 已死。GPU 0 显存 4459 MiB 可能是缓存还未释放，utilization 已经是 0%。

---

## 结果

**1. Scorer 统计（从日志 IB loss 推断）：**

| Step 区间 | β | IB loss | 状态 |
|-----------|------|---------|------|
| 100-1000 | 0.0 | 0.06→0.02 | 正常（warmup 阶段） |
| 1100-1200 | 0.001-0.002 | 0.015→**0.001** | 急剧下降 |
| 1500-2400 | 0.005-0.01 | **-0.0002~0.001** | Collapsed |

**2. Collapse 确认：是。** β ramp 启动后 IB loss 在 ~200 步内从 0.015 骤降到 ~0，之后持续为 0（含负值）。Scorer 退化为 pass-through，信息瓶颈完全失效。Task loss 无恶化进一步证实模型绕过了 bottleneck。

**3. PID 497308：已 kill（SIGTERM 成功）。**

**4. GPU 状态：** GPU 0 utilization 0%，显存 4459 MiB（缓存残留，会逐步释放）。GPU 1 被其他任务占用（21612 MiB）。

---
