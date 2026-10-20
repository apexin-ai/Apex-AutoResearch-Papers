# analyze exp fewnerd n16 s42 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_fewnerd_n16_s42_v2_20260521T151706_result.json`
- **Structured JSON:** [`27a0081a0152d4f3abc2.json`](../../sessions/27/27a0081a0152d4f3abc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **正常完成**。

**关键结果**：
- greedy_f1 = 0.7885，oracle_f1 = 0.9059，headroom = 0.1173
- 37648 instances 全部处理完毕，report.json + samples.jsonl (1.2GB) 均已生成
- soft_jaccard conditional rho (0.2126) > logprob conditional rho (0.1755)，结构化信号优于 logprob baseline
- verdict = FAIL（单 subtask MVP 阈值未达标，需 NER/RE/EAE 中至少一个通过）

报告已写入 `artifacts/exp_fewnerd_n16_s42_v2_analysis.md`。

---
