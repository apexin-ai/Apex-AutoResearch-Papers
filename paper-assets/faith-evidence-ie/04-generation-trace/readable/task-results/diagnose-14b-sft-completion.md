# diagnose 14b sft completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b_sft_completion_20260519T071832_result.json`
- **Structured JSON:** [`217e2ad75476d8d09887.json`](../../sessions/21/217e2ad75476d8d09887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan017_14b_sft 训练成功完成。**

| 指标 | 值 |
|---|---|
| global_step | 144 / 144 |
| train_loss (final) | 0.5457 |
| eval_loss | 0.6292 |
| checkpoint | `/root/autodl-tmp/sft_output_14b/checkpoint-144/` |

Loss 趋势正常，最后 5 步：0.5528 → 0.5535 → 0.5385 → 0.5240 → 0.5457

**GPU 状态：**
- cuda:0 — 29639/32607 MiB（占用中）
- **cuda:1 — 0 MiB（已释放）**
- **cuda:2 — 0 MiB（已释放）**
- cuda:3 — 5415/32607 MiB（占用中）

cuda:1 和 cuda:2 均已释放，可用于后续 eval 任务。Registry 已更新为 DONE/success。

---
