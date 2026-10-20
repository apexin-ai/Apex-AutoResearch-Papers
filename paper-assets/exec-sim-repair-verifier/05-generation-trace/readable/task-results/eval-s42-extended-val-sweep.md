# eval s42 extended val sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s42-extended-val-sweep_20260515T141312_result.json`
- **Structured JSON:** [`fa929ac0caea8d00f0e4.json`](../../sessions/fa/fa929ac0caea8d00f0e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动并注册。汇总：

**s42-extended-val-sweep 已在运行**
- **tmux session**: `s42-val-sweep`
- **GPU**: cuda:0 (RTX 5090, 当前 9101 MiB 已加载模型)
- **数据集**: swebench_val, 9335 instances
- **当前进度**: checkpoint-1800 正在评估中（模型已加载）
- **日志**: `/root/autodl-tmp/eval_results/s42_val_sweep.log`
- **汇总输出**: `/root/autodl-tmp/eval_results/s42_extended_val_sweep_summary.json`

18 个 checkpoint 顺序执行，每个预估 1-2h，不存在的 checkpoint 自动跳过。查进度可用 `tail -50 /root/autodl-tmp/eval_results/s42_val_sweep.log`。

---
