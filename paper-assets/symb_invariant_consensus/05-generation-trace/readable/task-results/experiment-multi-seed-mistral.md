# experiment multi seed mistral

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_multi-seed-mistral_20260522T032530_result.json`
- **Structured JSON:** [`6bce2ad2df92bda257a8.json`](../../sessions/6b/6bce2ad2df92bda257a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中。Seed 42 已处理 1/600，ETA ~272 分钟。4 个 seed 总共约 18-20 小时。

当前状态：
- vLLM Mistral-7B 在 cuda:2 port 8003 运行中
- 4-seed 序列实验已启动（PID 510987）：seed 42 → 123 → 456 → 789
- 每题 ~27s，600 题/seed，预计 seed 42 完成约 4.5 小时后
- 输出：`results/multi_seed/mistral_pw_seed{42,123,456,789}/results.json`
- 日志：`/tmp/multiseed_mistral_pw_all.log`

监控命令：
```bash
# 查进度
tail -5 /tmp/multiseed_mistral_pw_all.log
# 查当前 seed 的 checkpoint
ls -la results/multi_seed/mistral_pw_seed*/results.json
# 确认进程存活
ps -p 510987 -o pid=
```

cuda:0 和 cuda:3 的 FOLIO 2×2 实验未受影响。

---
