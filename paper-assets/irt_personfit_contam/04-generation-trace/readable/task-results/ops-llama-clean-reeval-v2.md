# ops llama clean reeval v2

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama-clean-reeval-v2_20260523T131357_result.json`
- **Structured JSON:** [`8859ced3ab64e965118a.json`](../../sessions/88/8859ced3ab64e965118a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估正在进行，速度约 500 items/4-5min。估算：

- 每个 condition (~14042 items): ~2 小时
- 10 个 conditions: ~20 小时
- 预计完成时间：约明天下午

目前状态：
- **GPU 2** 独占运行，无冲突
- **clean (s1)**: 1000/14042 进行中
- 剩余 clean_s2 ~ clean_s10 排队

批量任务在后台 nohup 运行 (PID 138419)，不会因 SSH 断开而中断。结果会自动保存到 `/root/autodl-tmp/ctrl_contam_llama/results/` 下覆盖旧文件。

需要我定期检查进度还是等全部完成后再报告？

---
