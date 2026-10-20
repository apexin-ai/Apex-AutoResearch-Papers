# eval exp 026 resume

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-026-resume_20260518T140401_result.json`
- **Structured JSON:** [`98c9d7e832462b5ee0e0.json`](../../sessions/98/98c9d7e832462b5ee0e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-026 状态报告

**进程状态**: 正常运行中，无需干预

| 项目 | 详情 |
|---|---|
| 评估脚本 PID | 27245 |
| vLLM PID | 23182 (cuda:0, 88GB) |
| 进度 | **154/204** (75.5%), 正在处理 #155 |
| ETA | ~37 分钟 (剩余 50 题, ~44s/题) |
| 启动时间 | 20:11 (via nohup) |

**当前准确率** (154 题):
- SICA: **112/154 = 72.7%**
- SC: **112/154 = 72.7%**

**清理操作**: 无。所有进程都是 exp-026 相关的，没有残留需要清理。

**结果路径**: `/root/symb_invariant_consensus/results/folio_204_14b/`
- `folio_204_results.json` (223KB, 持续更新)
- `intermediates/` (154 个文件)
- `folio_204_14b.log` (497KB)

实验已在 `--resume` 模式下运行，预计约 37 分钟后完成全部 204 题。由于是 nohup 启动而非 tmux/submit_training_job，没有 cron 监控，但进程稳定运行中，无需重启。

---
