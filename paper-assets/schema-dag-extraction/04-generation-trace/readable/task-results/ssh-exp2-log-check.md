# ssh exp2 log check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp2-log-check_20260515T022358_result.json`
- **Structured JSON:** [`aba837c07870c680b5f9.json`](../../sessions/ab/aba837c07870c680b5f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已无残留任务，无需删除。

---

**exp002_confusability_controlled — 成功完成**

- **判定**：成功。54/54 batches 全部完成，日志无 error/traceback，进程正常退出。
- **总耗时**：11732.5s (~3.3h)
- **结果文件**：
  - `artifacts/eval_exp2.json` (49KB) — 54 batches 评估指标
  - `artifacts/predictions_exp2.json` (39MB) — 全部预测输出
  - `artifacts/batch_config_exp2.json` (19KB) — batch 配置
- **日志最后关键行**：
  - 各 batch 汇总指标正常输出（exact_F1 范围 0.00~0.04，relaxed_F1 范围 0.05~0.21）
  - `Results saved to: ../artifacts`
- **Registry**：status → `ANALYZING`，log_path 已更新
- **Cron**：本 session 无活跃 cron，已确认清空

---
