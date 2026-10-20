# check embedding and llm judge status

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_embedding-and-llm-judge-status_20260514T131900_result.json`
- **Structured JSON:** [`a67783077a51ec1faefb.json`](../../sessions/a6/a67783077a51ec1faefb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Encoder Ablation Embedding — 两个都完成了

| Encoder | Windows | 维度 | 文件大小 |
|---------|---------|------|----------|
| e5-large | 54,809 | [10, 1024] | 2.07 GB |
| bge-m3 | 54,809 | [10, 1024] | 1.05 GB |
| gte-large | 10 (pilot) | [10, 1024] | 0.4 MB |

进程均已退出，embedding 数量与日志一致（54,809 windows from 5,000 trajectories）。

### Baseline LLM-Judge — 运行中，76.8%

- **1,400 / 1,824** 已完成，pid=27419 存活
- macro_f1 = **0.6659**，0 parse failures
- 已花费 ~$8.93，预计总花费 ~$11.6
- 剩余 424 条，预计 1-2 小时完成

报告已写入 `artifacts/report_embedding_llmjudge_status.md`。

---
