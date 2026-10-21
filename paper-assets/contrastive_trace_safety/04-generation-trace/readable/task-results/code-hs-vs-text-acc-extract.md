# code hs vs text acc extract

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hs_vs_text_acc_extract_20260516T235541_result.json`
- **Structured JSON:** [`09afefb4e16ce5fa6606.json`](../../sessions/09/09afefb4e16ce5fa6606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Model | HS bal_acc | Text bal_acc | Δ acc | HS precision | Text precision | Δ prec |
|-------|-----------|-------------|-------|-------------|---------------|--------|
| r1-8b | 81.3% | 72.9% | **+8.4pp** | 69.7% | 47.2% | **+22.5pp** |
| R1-32B | 70.2% | 67.3% | **+2.9pp** | 55.1% | 50.2% | **+4.9pp** |
| QwQ-32B | 71.4% | 61.7% | **+9.6pp** | 51.4% | 46.0% | **+5.4pp** |

**3/3 models HS acc > text acc, 3/3 models HS precision > text precision。** 效果量从 r1-8b 最大到 R1-32B 最小。报告已写入 `artifacts/report_hs_vs_text_acc.md`，原始数据在 `artifacts/hs_vs_text_acc_prec.json`。

---
