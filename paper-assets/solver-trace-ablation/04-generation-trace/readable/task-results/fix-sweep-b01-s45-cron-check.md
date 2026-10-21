# fix sweep b01 s45 cron check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sweep-b01-s45-cron-check_20260516T032410_result.json`
- **Structured JSON:** [`a711603e51493430c018.json`](../../sessions/a7/a711603e51493430c018.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论：进程正常运行，Cron 误报

**进程状态**：
- PID 604564 (bash) → 604568 (timeout) → 604569 (python3, `Rl` running)
- 训练已运行 ~4 分钟，当前 step 22/500

**训练健康度**：
- Step 1-18：reward=0, loss=0, grad_norm=0（冷启动，base model 无法生成正确证明）
- **Step 20 起突破**：reward=0.52, prove_rate=0.5, isr=0.27, loss 开始有梯度
- 训练正在正常学习，无需干预

**GPU 状态**：
- GPU 0: 79547 MiB, 100% 利用率（本实验）
- GPU 1: 80355 MiB, 90% 利用率（其他实验）

**其他**：
- 无 checkpoint（正常，500 步实验未到保存点）
- 无 error/traceback
- 日志持续写入

Cron 误报原因可能是检测逻辑匹配了子进程的短暂状态变化（如 timeout 包装层）。实验无需任何操作。

---
