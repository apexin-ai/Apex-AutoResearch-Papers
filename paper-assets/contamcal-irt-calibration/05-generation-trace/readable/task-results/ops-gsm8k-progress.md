# ops gsm8k progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-progress_20260523T073234_result.json`
- **Structured JSON:** [`be2420a4a72d519928e1.json`](../../sessions/be/be2420a4a72d519928e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**volume_control eval 正在跑 GSM8K**：554/660 (84%)，~7s/it，预计还需 ~12 分钟完成。MMLU 和 ARC-Challenge 已完成（结果文件已生成）。

**d000 eval 尚未开始**：结果目录不存在。从进程命令看，当前脚本只在跑 volume_control，d000 应在其后执行。

**进程状态**：
- tmux session `eval_falcon3` 活跃
- PID 778253 运行中（CPU 101%），从 14:09 开始，已跑 ~84 分钟

GSM8K 完成还需约 12 分钟，之后 d000 的 3 个 benchmark 估计再需 ~90 分钟。建议稍后再查。

---
