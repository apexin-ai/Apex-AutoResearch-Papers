# eval boolq hellaswag probe

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_boolq-hellaswag-probe_20260520T113034_result.json`
- **Structured JSON:** [`b1574f92ed75f9e10167.json`](../../sessions/b1/b1574f92ed75f9e10167.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 稳步进行中（6/30 done, 每对约 5min）。预计还需约 ~60 分钟。让任务继续跑，接下来改为大间隔检查。

**当前状态汇报：**
- **数据可用性**：需重跑（BoolQ/HellaSwag 无 per-sample logs）
- **eval 已提交**：`exp-boolq-hellaswag-eval` 在 westb-48145 上运行中
- **进度**：6/30 tasks done（GDN 全部 5 个配置中 3 个完成），按 ~5min/model-pair 速率
- **预估完成时间**：~20:50 UTC（从 19:32 开始，总计约 78 分钟）
- **分析脚本**：已写好 `artifacts/analyze_per_example.py`，eval 完成后即可执行

需要我继续轮询等待 eval 完成后自动执行分析，还是等 eval 结束后再通知？

---
