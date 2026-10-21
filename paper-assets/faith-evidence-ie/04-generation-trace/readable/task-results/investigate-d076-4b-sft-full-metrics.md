# investigate d076 4b sft full metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_d076_4b_sft_full_metrics_20260518T135459_result.json`
- **Structured JSON:** [`dba3c0b00685eec2366e.json`](../../sessions/db/dba3c0b00685eec2366e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Config 确认：两个 eval 均为 base+adapter, bs=4, quantize=false, seed=42。no-evidence 的 `metrics.json` 和 `metrics_v2.json` 数值一致（v2 仅多了 recomputed Ign-F1 备注），ign_f1 ≠ f1，非 buggy 版本。

```
4B SFT with-evidence (D076):
  ign_f1: 39.74%
  f1: 40.49%
  evi_f1 (cond): 79.86%
  evi_f1_joint: 31.47%
  EDCR: 0.6982
  format_compliance_rate: 0.998
  field_compliance_rate: 0.707
  n_truncated: 288

4B SFT no-evidence (D076):
  ign_f1: 47.21%
  f1: 48.76%
```

---
