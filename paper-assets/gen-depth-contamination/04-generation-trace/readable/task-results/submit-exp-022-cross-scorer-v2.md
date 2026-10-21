# submit exp 022 cross scorer v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_022_cross_scorer_v2_20260516T150528_result.json`
- **Structured JSON:** [`c8597084166653a5c529.json`](../../sessions/c8/c8597084166653a5c529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验运行正常。状态汇总：

**cuda:3 已占用** — 第一个组合 `qwen_base × qwen_base` feature extraction 已到 75%（depth 0），~8 it/s。

**12 个组合的进度**：
- 第 1 批（已缓存模型，6 个组合）：qwen_base/pythia 做 scorer × 3 generators — 正在进行
- 第 2 批（待下载模型，6 个组合）：qwen_instruct/olmo 做 scorer × 3 generators — 等模型下载

**模型下载**：
- Qwen2.5-1.5B-Instruct：3% of 2.88GB，~6MB/s
- OLMo-1B-hf：26% of 4.38GB，~6MB/s

**注意**：原计划 4 generators 但 OLMo-1B 没有 depth chain 数据，实际可跑 3 generators × 4 scorers = 12 个组合。

**tmux session**: `exp022`
**日志**: `logs/exp022.log`

第一批约 60 分钟跑完。下载完成后重跑脚本处理第二批（脚本自动跳过已完成的组合）。需要我持续监控还是你稍后自己看？

---
