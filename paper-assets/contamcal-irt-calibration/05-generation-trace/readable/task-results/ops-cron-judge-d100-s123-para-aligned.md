# ops cron judge d100 s123 para aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cron-judge-d100-s123-para-aligned_20260515T184001_result.json`
- **Structured JSON:** [`ee43b5d6f73731a49ee2.json`](../../sessions/ee/ee43b5d6f73731a49ee2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**状态：killed（未完成）**

- 日志显示 MMLU paraphrased 已完成评估循环，但 GSM8K paraphrased 仅跑到 22% (51/228) 时进程被 kill
- 输出目录 `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/` 为空，无任何 results.json
- 日志中无 "Evaluation complete" 标记，也无 "saved" 记录 — 结果仅在全部 benchmark 完成后才写入，因此无任何可用数据
- 4 个 benchmark (mmlu, gsm8k, arc_challenge, humaneval) 的 paraphrased 评估均无产出

**Registry 已更新**：conclusion → killed

**Cron**：当前 session 无活跃 cron job（CronList 为空）。该 cron 可能在另一个 session 中创建，需在对应 session 中手动清除。

---
