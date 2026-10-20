# ops ss s42 monitor

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ss_s42_monitor_20260522T160100_result.json`
- **Structured JSON:** [`37613f69842796e9beed.json`](../../sessions/37/37613f69842796e9beed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**训练已停止，未在运行。**

- **GPU**: RTX PRO 6000 Black (98GB)，0% 利用率，0MB 显存占用，无运行进程
- **Checkpoint**: 只有 `epoch_0`（20:38 保存），含 `gate_params.pt` (3.3MB) + LoRA adapter (19.2MB)。**epoch_1 尚未出现**
- **Tensorboard**: 无任何 events 文件，无 logs 子目录
- **训练日志**: 无 `.log` 文件

结论：训练进程已经退出（可能正常完成 epoch_0 后停止，或异常中断）。需要检查 tmux session 和训练脚本的输出日志来确认原因。是否需要进一步排查或重启训练？

---
