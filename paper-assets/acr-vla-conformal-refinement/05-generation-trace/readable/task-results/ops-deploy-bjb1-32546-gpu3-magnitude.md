# ops deploy bjb1 32546 gpu3 magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb1-32546-gpu3-magnitude_20260518T212737_result.json`
- **Structured JSON:** [`712e451a8ce604ff5347.json`](../../sessions/71/712e451a8ce604ff5347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**GPU 3 (bjb1-32546) 状态：**
- VRAM: 10862 MiB / 24564 MiB (~13.7 GB 空闲)
- 实验 `eval-perdof-norm003-seed48-t16` 已启动，模型加载完毕，10 个 task 已加载
- 同一 GPU 上还有一个 `norm01_seed48` 实验 (PID 698215)

注意：原始命令的 tmux 工作目录缺失，导致相对路径 `logs/` 指向 `/root/logs/`（不存在）。已修复为 `-c /root/acr-vla-conformal-refinement`，日志正确写入 `/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003_seed48.log`。

---
