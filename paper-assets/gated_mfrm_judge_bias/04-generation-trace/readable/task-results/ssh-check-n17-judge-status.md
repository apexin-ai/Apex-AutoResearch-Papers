# ssh check n17 judge status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_n17_judge_status_20260523T213855_result.json`
- **Structured JSON:** [`e6a1887e796ca312b1f0.json`](../../sessions/e6/e6a1887e796ca312b1f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/n17_judge_status.md`。

**结论**: 评测正在进行中，总体完成约 50%。

关键状态：
- **8/9 个 judge 活跃运行**，结果文件持续写入中（最后更新 ~2分钟前）
- 3 个 vLLM 服务器（llama/qwen/mistral）均正常
- **最快 sonnet 65.7%，最慢 deepseek 39.8%**
- llama-3.3-70b-shard2 已停止 16 小时，需确认

**需要关注的问题**：
1. Mistral 早期因 4096 token 上下文限制跳过了大量 items（vLLM 已重启修复，但跳过的 items 需要重跑）
2. llama-shard2 停了，不确定是废弃还是需要继续
3. 预计全部完成需 24-36 小时

---
