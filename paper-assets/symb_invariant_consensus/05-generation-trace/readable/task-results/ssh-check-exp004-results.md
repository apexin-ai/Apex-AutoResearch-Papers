# ssh check exp004 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp004-results_20260517T174319_result.json`
- **Structured JSON:** [`4de55e226828a3edaa06.json`](../../sessions/4d/4de55e226828a3edaa06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-004 Qwen-7B 实验结果

**状态**: 已完成（tmux session 仍在，结果文件已生成）

| Metric | Value |
|---|---|
| **n** | 56 (summary) / 57 (results array) |
| **k** | 12 |
| **SICA accuracy** | 69.64% (39/56) |
| **SC accuracy** | 69.64% (39/56) |
| **delta_pp** | 0.00% |
| **multi_candidate_rate (C0)** | **42.11%** (24/57) |
| **extraction_rate** | 93.75% |
| **answer_extraction_rate** | 100% |
| **contradiction_rate** | 2.69% |
| **discordant SICA wins** | 2 |
| **discordant SC wins** | 2 |
| **mcnemar_p** | 1.0000 (无显著差异) |
| **wall_time** | 1751.7s (~29 min) |
| **truncated_traces** | 0 |

### Per-domain breakdown

| Domain | SICA | SC | n |
|---|---|---|---|
| **ProofWriter (D5)** | 60.00% | 63.33% | 30 |
| **FOLIO** | 80.77% | 76.92% | 26 |

### 关键发现

**C0 = 42.11%** — Qwen-7B 在 42% 的问题上产生了多候选答案，说明 within-family scaling 有实质性分歧空间。但 SICA 和 SC 在整体准确率上完全持平（69.64% vs 69.64%），discordant pairs 仅 4 对且对半分（2:2），McNemar p=1.0。

FOLIO 上 SICA 略优于 SC（80.77% vs 76.92%），ProofWriter D5 上 SC 略优（63.33% vs 60.00%），但样本量太小无统计显著性。

---
