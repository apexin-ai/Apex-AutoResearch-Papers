# eval cuda3 downstream followup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cuda3_downstream_followup_20260520T045053_result.json`
- **Structured JSON:** [`cd42e2f399ebb3c836be.json`](../../sessions/cd/cd42e2f399ebb3c836be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已成功完成，结果 JSON 存在且 registry 已包含正确的 downstream metrics。

## 汇总

| Benchmark | detect_remove_q03_seed42_r2 | detect_remove_q04_seed42 |
|---|---|---|
| arc_easy (acc_norm) | **0.6301** | 0.6107 |
| arc_challenge (acc_norm) | 0.3549 | **0.3567** |
| hellaswag (acc_norm) | **0.4851** | 0.4819 |
| piqa (acc_norm) | 0.6872 | **0.6931** |
| winogrande (acc) | **0.5675** | 0.5659 |

- **状态**: 两个 eval 均已完成（q03 完成于 12:46，q04 完成于 12:48，今天）
- **Registry**: 两个 exp_id 的 downstream metrics 已全部写入，数值与 JSON 完全一致
- **GPU 3**: 当前空闲（0% 利用率，0 MiB 显存）

上一个 Worker 报告"空结果"可能是在 eval 尚未完成时就检查了。无需额外操作。

---
