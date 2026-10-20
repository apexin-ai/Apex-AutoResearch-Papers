# analysis llama fair tax recompute

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-fair-tax-recompute_20260522T062210_result.json`
- **Structured JSON:** [`7c832b129e8f418e62b6.json`](../../sessions/7c/7c832b129e8f418e62b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终结果

| Seed | fair_subset | with_evi ign_f1 | no_evi ign_f1 | fair_tax | raw_tax |
|------|------------|-----------------|---------------|----------|---------|
| s42 | 873 | 57.16 | 55.64 | **-1.53pp** | -4.39pp |
| s43 | 834 | 49.10 | 37.89 | **-11.20pp** | -15.65pp |
| s44 | 977 | 46.79 | 43.95 | **-2.83pp** | -2.82pp |
| **Mean±Std** | | | | **-5.19±4.29pp** | -7.62±5.71pp |

**与 Reviewer raw tax 对比：**
- 方向完全一致（全部为负 = evidence helps）
- fair_tax 幅度整体缩小（-5.19 vs -7.62），符合预期——去掉 format 失败的 docs 后，no-evi 在 fair subset 上表现提升（那些 format 失败的是 no-evi 的弱文档）
- s43 仍然是最极端的 seed（no-evi format_ok 只有 834/985），fair_tax 从 -15.65 缩小到 -11.20 但仍很大
- s44 几乎不变（-2.83 vs -2.82），因为 format_ok 高达 977/985，fair subset ≈ full set

JSON 输出已保存：
- `/root/autodl-tmp/eval_results/fair_tax_llama_sft_s42_matched_2048_v2.json`
- `/root/autodl-tmp/eval_results/fair_tax_llama_sft_s43_matched_2048_v2.json`
- `/root/autodl-tmp/eval_results/fair_tax_llama_sft_s44_matched_2048_v2.json`

---
