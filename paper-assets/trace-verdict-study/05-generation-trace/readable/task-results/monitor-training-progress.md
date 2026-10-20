# monitor training progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_20260515T051024_result.json`
- **Structured JSON:** [`0f263e243c01299d0a72.json`](../../sessions/0f/0f263e243c01299d0a72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_training_progress.md`。

| 实验 | 进度 | Loss | 速度 | 预计完成 (UTC) |
|------|------|------|------|----------------|
| vota_no_ae_seed42 | 208/444 (47%) | 0.0603 ↓ | 13.5 s/it | ~14:04 |
| full_trace_label_only_seed42 | 70/444 (16%) | 待输出 | 18.4 s/it | ~15:06 |

两张 RTX PRO 6000 Blackwell 均 100% 利用率，温度正常，无 OOM/loss spike。实验 2 因 gradient_checkpointing + full trace 输入更长，显存占用 92%（90 GB），单步慢约 36%。

---
