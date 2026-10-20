# cpu paper metrics table prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_paper_metrics_table_prep_20260516T052206_result.json`
- **Structured JSON:** [`32eee38865bbfe29f5b9.json`](../../sessions/32/32eee38865bbfe29f5b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**服务器产出**: `/root/autodl-tmp/eval_results/paper_table_data.json` — 22 个方法条目，含完整 metrics + 协议元数据

**收集到的完整数据 (13 个方法)**:

| 方法 | Rel-F1 | Evi-F1 | EDCR |
|------|--------|--------|------|
| SFT baseline | 0.4106 | 0.8013 | 0.7039 |
| SFT no-evidence | 0.4893 | — | — |
| RSFT-CED (2-seed mean) | 0.4557 | 0.8118 | 0.6546 |
| RSFT-flatNLI (2-seed mean) | 0.4583 | 0.8143 | 0.6490 |
| RSFT top-k=3 | 0.4454 | 0.8088 | 0.6635 |
| CED-reranker (N=8) | 0.4864 | — | — |
| DPO-CED | 0.4034 | 0.8088 | 0.7139 |
| GRPO bf16 (ckpt100) | 0.4549 | 0.8086 | 0.6318 |
| GRPO QLoRA | 0.2167 | 0.5746 | 0.8539 |

**4 个 reeval 仍在跑**: rsft_ced_s42, rsft_ced_s44, rsft_flat_nli_s42, rsft_flat_nli_s43_r2。完成后 CED 和 flatNLI 的 seed mean 会从 2-seed 变 4-seed。

---
