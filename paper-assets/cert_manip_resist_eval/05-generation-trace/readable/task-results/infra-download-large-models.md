# infra download large models

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-large-models_20260521T175959_result.json`
- **Structured JSON:** [`298f0ac765774549c79c.json`](../../sessions/29/298f0ac765774549c79c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前下载状态汇总（进程已运行 ~18.5 小时）：

| 模型 | temp 大小 | 分片进度 | 期望总大小 |
|------|----------|---------|-----------|
| Qwen2.5-72B-Instruct-AWQ | 7.0G | 8/11 shards 下载中 | ~40G |
| Qwen2.5-32B-Instruct-AWQ | 4.2G | 5/5 shards 下载中 | ~18G |
| Llama-3.1-70B-Instruct-AWQ | 6.9G | 8/9 shards 下载中 | ~37G |
| Mistral-Large-Instruct-2407-AWQ | 6.3G | 8/14 shards 下载中 | ~48G |

磁盘：39G/250G 已用（212G 剩余，足够放下全部 ~143G 模型）。

速度非常慢——18 小时总共仅下载约 24G，平均聚合速度 ~370 KB/s。按此速度剩余 ~120G 还需约 90 小时（~3.7 天）。日志显示单分片速度 460kB/s-994kB/s，4 个模型并行下载相互争抢带宽。

注意事项：
- Qwen-32B 的 `tokenizer.json` 在 temp 中仍为 0 bytes，待下载完成后验证
- 所有 4 个进程存活正常，无报错
- 没有任何分片完整下载完毕（完成后会从 temp 移到主目录）

如果想加速，可以考虑：先杀掉 3 个，只留优先级最高的 Qwen-72B 单独下载，完成后再启动下一个。要继续等还是调整策略？

---
