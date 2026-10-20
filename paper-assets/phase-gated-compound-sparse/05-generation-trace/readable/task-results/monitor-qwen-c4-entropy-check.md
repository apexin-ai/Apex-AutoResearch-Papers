# monitor qwen c4 entropy check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_qwen_c4_entropy_check_20260514T085649_result.json`
- **Structured JSON:** [`20cf2146c87ea03d862f.json`](../../sessions/20/20cf2146c87ea03d862f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验状态汇总：

| 项目 | 状态 |
|------|------|
| **进程** | Running, PID **100543** |
| **tmux** | `qwen_c4_entropy` session 存活 |
| **进度** | **22/30** 完成，正在处理 Problem 23/30 (`intermediate_algebra/121.json`) |
| **JSON 已保存** | 20 个 problem 的结果（JSON 滞后于日志，写入可能有延迟） |
| **GPU** | GPU 1, 22567 MiB / 97887 MiB |
| **输出路径** | `/root/autodl-tmp/pacs/results/c4_attention_entropy_qwen/c4_entropy_results.json` |
| **日志** | `~/runs/phase-gated-compound-sparse/qwen_c4_entropy.log` |

从日志看，Problem 20-22 每个约 10-40s，Problem 22（2048 tokens）花了约 4min。按当前速度，剩余 7-8 个 problem 预计 **10-30 分钟**内完成。

需要我注册 cron 监控吗？

---
