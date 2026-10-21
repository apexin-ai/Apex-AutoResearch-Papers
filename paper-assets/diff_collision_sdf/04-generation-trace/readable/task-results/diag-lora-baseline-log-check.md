# diag lora baseline log check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_lora_baseline_log_check_20260525T174904_result.json`
- **Structured JSON:** [`4ff58a24bfd4de586cf8.json`](../../sessions/4f/4ff58a24bfd4de586cf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

两个 LoRA baseline 实验**并未失败**——resume2 进程正在运行中：

| 实验 | PID | GPU | 状态 | 从 step | 启动时间 (UTC) | ETA |
|------|-----|-----|------|---------|---------------|-----|
| s0 | 3622 | cuda:0 | 运行中 | 24000 | 05-26 01:48 | ~09:30 |
| s1 | 3712 | cuda:1 | 运行中 | 24000 | 05-26 01:48 | ~09:30 |

**关键发现**：
- 之前的 resume（从 step 16000）确实因 tmux 服务器崩溃中断，s0 停在 25695，s1 停在 25705
- 但 resume2 已在 01:48 UTC 自动重新提交，从 step 24000 成功恢复
- Checkpoint 加载正常，Phase 2 LoRA 解冻正常
- 日志文件只有 ~13KB 因为 tqdm 进度条用 `\r`，周期性 step 日志尚未触发新条目
- 剩余 6000 steps × ~4.6s/step ≈ 7.7h

Registry 已更新为 RUNNING 状态，notes 记录了完整的 resume 历史。

---
