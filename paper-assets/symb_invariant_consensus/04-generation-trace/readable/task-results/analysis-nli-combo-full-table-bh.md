# analysis nli combo full table bh

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-combo-full-table-bh_20260520T224413_result.json`
- **Structured JSON:** [`be19db0ea3da684cca65.json`](../../sessions/be/be19db0ea3da684cca65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据验证完成，结果已写入。

## 数据验证摘要

- **Mistral-7B**: w=1/w=3 从 `direction_r_nli_pw600/results.json` (westd-25068) 确认；w=5 原文件缺失，从 exp046 SC traces + DeBERTa predictions 重新计算得到 50.00%, +10.67pp, p=2.89e-08 ✓
- **LLaMA-3.1-8B**: 从 `exp092_llama8b_pw_nli_combo/results.json` (westd-16639) 全部确认 ✓
- **Qwen2.5-14B**: 从 `qwen14b_pw_nli_combo/results.json` (westd-16639) 全部确认 ✓
- **Qwen3-14B**: 从 `d116_qwen3_pw_deberta_large/results.json` (westd-16639) 全部确认 ✓
- **LLaMA SC=70.00%**: 从 `exp048_llama8b_pw600/exp048_results.json` (westd-16639) 确认 ✓

## 完整表格 (m=12, BH correction, α=0.05)

| Generator | n | SC% | Gap | w | Combo% | Δpp | p_raw | p_BH | Sig |
|---|---|---|---|---|---|---|---|---|---|
| Mistral-7B | 600 | 39.33 | +15.67 | 1 | 40.17 | +0.83 | .2668 | .3558 | |
| | | | | 3 | 42.83 | +3.50 | .0125 | **.0375** | * |
| | | | | 5 | 50.00 | +10.67 | <.0001 | **<.0001** | *** |
| LLaMA-3.1-8B | 600 | 70.00 | −15.00 | 1 | 72.83 | +2.83 | <.0001 | **.0005** | *** |
| | | | | 3 | 74.17 | +4.17 | .0035 | **.0142** | * |
| | | | | 5 | 71.67 | +1.67 | .4335 | .4335 | |
| Qwen2.5-14B | 600 | 73.50 | −18.50 | 1 | 74.17 | +0.67 | .3438 | .4125 | |
| | | | | 3 | 74.33 | +0.83 | .4049 | .4335 | |
| | | | | 5 | 75.33 | +1.83 | .1439 | .2190 | |
| Qwen3-14B | 600 | 85.00 | −30.00 | 1 | 85.83 | +0.83 | .1250 | .2190 | |
| | | | | 3 | 86.00 | +1.00 | .1460 | .2190 | |
| | | | | 5 | 86.83 | +1.83 | .0522 | .1254 | |

**4/12 survive BH correction** at α=0.05: Mistral w=3/w=5, LLaMA w=1/w=3.

结果已写入 `westd-25068:/root/symb_invariant_consensus/results/nli_combo_full_table_bh/results.json`。

---
