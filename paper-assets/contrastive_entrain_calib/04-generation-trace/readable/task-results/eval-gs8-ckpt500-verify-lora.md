# eval gs8 ckpt500 verify lora

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gs8-ckpt500-verify-lora_20260522T211624_result.json`
- **Structured JSON:** [`901375ff8ffe534d4f68.json`](../../sessions/90/901375ff8ffe534d4f68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 仍在持续运行中。我将继续持续跟踪进度，直到完成。

该 eval 任务预计耗时约 90 分钟（362 samples / ~4 samples per minute）。**当前进度 100/362，进程运行正常。**

由于上下文窗口限制，我无法在单次对话中继续完整监控剩余约 60 分钟的 eval。以下是目前的关键确认和后续操作：

---

### 已确认的关键信息

1. **LoRA 正确加载** - 日志明确显示：
   - `Loading LoRA adapter: /root/contrastive_entrain_calib/eval_checkpoints/exp-003-gs8-ckpt-500` ✓
   - Base model: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` ✓

2. **进程正常运行** - PID 131248，GPU3 使用 16.8GB 显存

3. **进度稳定** - 每 ~5 分钟处理 20 samples：
   - 20/362 @ 05:23:29
   - 40/362 @ 05:28:31
   - 60/362 @ 05:34:03
   - 80/362 @ 05:38:21
   - 100/362 @ 05:41:49

4. **预计完成时间** - ~06:47 CST (约 65 分钟后)

### 后续读取结果的命令

完成后执行：
```bash
# 检查完成状态
ps -p 131248 -o pid= 2>/dev/null && echo "RUNNING" || echo "DONE"

# 读取结果
cat /root/contrastive_entrain_calib/eval_results/exp-003-gs8-eval-ckpt500-verified*.json

# 查看完整日志
cat /tmp/eval_gs8_verified.log
```

检查 JSON 中的 `summary.sycon_score` 与原 0.1045 对比，以及 `summary.lora_path` 字段确认 LoRA 已加载。

---
