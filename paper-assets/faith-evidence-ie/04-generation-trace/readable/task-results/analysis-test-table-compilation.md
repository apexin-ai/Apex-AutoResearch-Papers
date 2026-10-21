# analysis test table compilation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test-table-compilation_20260522T014235_result.json`
- **Structured JSON:** [`f29c6f7a35d812d33e92.json`](../../sessions/f2/f29c6f7a35d812d33e92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。表格写入 `artifacts/test_table_compilation.md` 并注册为 `art_20260522_2b6be9`。

汇总：
- **Table 1** 覆盖 5 个 scale，4B/8B/14B/LLaMA 数据完整，1.7B SFT 仍在跑（⏳）
- **Table 2** 三个 spot-check（1.7B/8B/14B）的 no-evidence test eval 全部 RUNNING，待完成后填入 test tax 并与 dev tax 对比一致性
- 8B RSFT 截断率异常低（1.8% vs SFT 82%），14B RSFT 略低于 SFT（−0.37pp）——均在表内备注

---
