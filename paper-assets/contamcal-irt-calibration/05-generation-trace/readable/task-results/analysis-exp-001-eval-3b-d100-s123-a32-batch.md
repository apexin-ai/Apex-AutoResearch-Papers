# analysis exp 001 eval 3B d100 s123 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_d100_s123_a32_batch_20260516T031221_result.json`
- **Structured JSON:** [`b7094ee64d16c01fff50.json`](../../sessions/b7/b7094ee64d16c01fff50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部指标已提取。日志 EXIT_CODE=0，无 error/traceback。

```
=== ALIGNED ===
mmlu: 0.6330 (8889/14042)
gsm8k: 0.7074 (933/1319)
arc_challenge: 0.8251 (967/1172)
humaneval: 0.1159 (19/164)

=== PARA_ALIGNED ===
mmlu: 0.6598 (4352/6596)
gsm8k: 0.5746 (131/228)
arc_challenge: 0.8049 (561/697)
humaneval: 0.0000 (0/26)

=== STATUS ===
aligned: complete (4/4 benchmarks, .done sentinel present)
para_aligned: complete (4/4 benchmarks, .done sentinel present)
overall: success (EXIT_CODE=0, no errors)
```

注意：para_aligned humaneval 只有 26 个 QC-passed 的 paraphrase 样本（原始 164 个），且 pass@1=0，样本量过小导致指标不可靠。

---
