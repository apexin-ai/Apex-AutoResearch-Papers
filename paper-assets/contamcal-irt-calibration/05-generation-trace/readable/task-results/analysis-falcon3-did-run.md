# analysis falcon3 did run

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-did-run_20260522T174607_result.json`
- **Structured JSON:** [`a40f26d1d16a2527f005.json`](../../sessions/a4/a40f26d1d16a2527f005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/falcon3_did_results.md`。

**结论**：Falcon3 DiD 分析被 d000 baseline 缺失阻塞。Falcon3 只训练+eval 了 d100 一个条件，从未做 d000（clean SFT）。需要先训练 Falcon3 d000 SFT 或至少 eval pretrained base model 作为 proxy baseline，才能跑 DiD。

如果要立即产出一些结果，可以用 Option C（d100 单快照 treated vs untreated 对比），但这不是真正的 DiD。需要你决定走哪个方案。

---
