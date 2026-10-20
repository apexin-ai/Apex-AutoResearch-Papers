# ssh westd olmo gpu01 poll launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-gpu01-poll-launch_20260519T115848_result.json`
- **Structured JSON:** [`9222f0476e07b77ac486.json`](../../sessions/92/9222f0476e07b77ac486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Monitor script running in tmux `olmo2_monitor`。

- 日志：`/root/autodl-tmp/exp001/phase2_logs/olmo2_monitor.log`
- 每 120 秒检查一次 GPU 0/1，空闲即自动启动 OLMo-2 eval（GPU0: d000+d005, GPU1: d025+d050）
- 最长轮询 60 分钟，超时退出
- 查看进度：`tmux attach -t olmo2_monitor` 或 `cat /root/autodl-tmp/exp001/phase2_logs/olmo2_monitor.log`

---
