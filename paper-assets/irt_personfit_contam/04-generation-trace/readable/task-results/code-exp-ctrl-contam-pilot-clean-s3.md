# code exp ctrl contam pilot clean s3

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-ctrl-contam-pilot-clean-s3_20260520T185936_result.json`
- **Structured JSON:** [`42e70b2dd71aa25b4d40.json`](../../sessions/42/42e70b2dd71aa25b4d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，每 3 分钟自动检查进度。当前状态：

- **已完成**: train.py SEED_MAP 已添加 `clean_s3: 456`，`data/clean_s3/train.jsonl` 已生成（5000 条 Alpaca）
- **进行中**: clean_s3 训练（模型已加载，开始训练中，预计 ~17 分钟）
- **待执行**: eval → Cohen's d 重算

训练完成后 cron 会触发，届时自动继续 eval 步骤。

---
