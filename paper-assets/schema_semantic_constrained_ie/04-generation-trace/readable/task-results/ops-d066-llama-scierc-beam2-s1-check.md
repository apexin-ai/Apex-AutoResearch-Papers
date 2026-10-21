# ops d066 llama scierc beam2 s1 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_scierc_beam2_s1_check_20260520T150551_result.json`
- **Structured JSON:** [`0252e3c951e1f274948e.json`](../../sessions/02/0252e3c951e1f274948e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**beam4 s1 eval (完成，已 DONE)**

| Metric | P | R | F1 |
|--------|------|------|------|
| Entity | 65.96 | 70.29 | **68.06** |
| Relation | 42.10 | 51.13 | **46.18** |

Schema 合规：ET=100%, RV=100%, DR=0%, CF=0%。0 parse failures。

**beam2 s1 — 原始运行失败**，缺少 `--constraints_path`。已被重新启动（PID 769697, GPU1），带正确参数 `--constraints_path ontology_constraints.json`，正在运行中。已注册新 cron 监控。

**beam8 s1 暂无法启动**——两个 GPU 都在跑：
- GPU0: beam8 unc (PID 769000)
- GPU1: beam2 s1 重跑 (PID 769697)

beam2 完成后 GPU1 释放，再启动 beam8 s1。

---
