# fix d076 table ign f1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d076-table-ign-f1_20260522T225429_result.json`
- **Structured JSON:** [`c87c1829da4f322b00cb.json`](../../sessions/c8/c87c1829da4f322b00cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the result:

## D076 表 ign_f1 修正对照表

| Config | 当前值 (f1) | 正确值 (ign_f1) | 差值 | 来源文件 |
|--------|-----------|---------------|------|---------|
| SFT baseline | 0.4049 | **0.3974** | -0.75pp | sft_baseline_d076_reeval/metrics.json |
| CED RSFT s42 | 0.4517 | **0.4423** | -0.94pp | rsft_ced_s42_reeval/metrics.json |
| CED RSFT s44 | 0.4621 | **0.4511** | -1.10pp | rsft_ced_s44_reeval/metrics.json |
| CED RSFT mean | 0.4569 | **0.4467** | -1.02pp | 计算值 |
| flat-NLI RSFT s42 | 0.4535 | **0.4448** | -0.87pp | rsft_flat_nli_s42_reeval/metrics.json |
| flat-NLI RSFT s43_r2 | 0.4586 | **0.4503** | -0.83pp | rsft_flat_nli_s43_reeval_r2/metrics.json |
| flat-NLI RSFT mean | 0.4561 | **0.4475** | -0.86pp | 计算值 |
| LLaMA-8B SFT | 0.5514 | **0.5384** | -1.30pp | llama_3_1_8b_sft_eval/metrics.json |
| LLaMA-8B no-evidence | 0.5624 | **0.5452** | -1.72pp | llama_3_1_8b_no_evidence_eval/metrics.json |
| Qwen3-1.7B SFT | 0.4945 | **0.4786** | -1.59pp | qwen3_1_7b_sft_eval/metrics.json |
| Qwen3-1.7B RSFT k=1 s42 | 0.5290 | **0.5122** | -1.68pp | d102_1_7b_k1_s42/metrics.json |
| Qwen3-8B SFT | 0.5262 | **0.5051** | -2.11pp | qwen3_8b_sft_eval/metrics.json |
| Qwen3-8B RSFT k=1 s42 | 0.5376 | 0.5376 | ign_f1=f1 ✓ 已正确 | d102_8b_k1_s42/metrics.json |
| Qwen3-8B RSFT k=1 s43 | 0.5471 | 0.5471 | ign_f1=f1 ✓ 已正确 | d102_8b_k1_s43/metrics.json |
| Qwen3-8B RSFT k=1 s44 | 0.5451 | 0.5451 | ign_f1=f1 ✓ 已正确 | rsft_8b_k1_s44_eval/metrics.json |
| Qwen3-8B RSFT k=1 mean | 0.5433 | 0.5433 | ✓ 已正确 | 计算值 |
| LLaMA-8B RSFT k=1 s42 | 0.5714 | 0.5714 | ign_f1=f1 ✓ 已正确 | d102_llama_k1_s42/metrics.json |
| LLaMA-8B RSFT k=1 s43 | 0.5662 | 0.5662 | ign_f1=f1 ✓ 已正确 | d102_llama_k1_s43/metrics.json |
| LLaMA-8B RSFT k=1 s44 | 0.5587 | 0.5587 | ign_f1=f1 ✓ 已正确 | rsft_llama_k1_s44_eval/metrics.json |
| LLaMA-8B RSFT k=1 mean | 0.5654 | 0.5654 | ✓ 已正确 | 计算值 |

**注意：** 表中当前值≠ign_f1 的行，实际 f1 与 ign_f1 对应关系已交叉验证（f1 match 表值）。

**修正说明：**
- Qwen3-8B RSFT k=1 (3 seeds) 和 LLaMA-8B RSFT k=1 (3 seeds) 的表值**已经是 ign_f1**（表值≠f1，match ign_f1）
- 其余 12 行当前使用 f1，需替换为 ign_f1。差值范围 -0.75pp 到 -2.11pp
- 替换后，Qwen3-1.7B RSFT k=1 s42 的 gain 从 +3.5pp 变为 +3.4pp（0.5122-0.4786）
- CED RSFT mean 从 0.4569 降至 0.4467（over SFT baseline gain: +4.93pp → +4.93pp，不变因 baseline 也下降）

---
