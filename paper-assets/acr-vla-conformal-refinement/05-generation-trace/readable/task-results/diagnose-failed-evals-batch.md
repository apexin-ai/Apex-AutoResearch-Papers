# diagnose failed evals batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_failed-evals-batch_20260521T011303_result.json`
- **Structured JSON:** [`1d7cde4a62f093145d3f.json`](../../sessions/1d/1d7cde4a62f093145d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。三个独立问题：

1. **bjb2-28827 SIGHUP 批量故障** — 短命名批次（seed60-64）未用 nohup 保护，SSH 断连后被 SIGHUP 杀死。已被 seed71-75 替代。当前运行的实验均安全。

2. **bjb1-32546 `python` 不在 PATH** — norm003-seed62/63 因 `nohup: failed to run command 'python'` 而启动失败。已注册 r2 重试。

3. **seed57/seed58 是监控误报**（最重要发现）— 日志确认两个实验均已正常完成（19.0% 和 16.0%），但因 evaluate.py 无 W&B + 未用 tmux_wrapper.sh 导致无 sentinel，监控持续报 miss。需纠正注册表状态并补 sentinel 机制。

报告已写入 artifacts 并注册。

---
