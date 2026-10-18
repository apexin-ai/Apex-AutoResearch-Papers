# research per example data audit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_per_example_data_audit_20260519T125609_result.json`
- **Structured JSON:** [`9a6c302d22f88fddc736.json`](../../sessions/9a/9a6c302d22f88fddc736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册 (`art_20260519_e33ecb`)。

核心发现：

**1.3B**：13/16 个模型有全 benchmark per-example 数据（嵌入在 127M JSON 中）。缺口是 GDN-h3/h6/h24 三个模型——仅有 lambada_openai 的 JSONL logsamples，其余 5 个 benchmark 无 per-example 数据。

**340M**：GDN 全系列 + Transformer baseline（6 个模型）有完整 per-example 数据。RetNet 和 HGRN2 全部 10 个模型仅有 aggregate results，需要补跑 `--log_samples`。

**Analysis CSV**：已有两份 lambada per-example CSV（5161 examples），分别覆盖 GDN pure/h12 vs HGRN2 pure/h3 和 GDN pure/h31 vs HGRN2 pure/h31 的对比。

---
