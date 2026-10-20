# exp sft 1 7b s44 dev eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sft_1_7b_s44_dev_eval_20260525T040242_result.json`
- **Structured JSON:** [`378081994a888f2dad00.json`](../../sessions/37/378081994a888f2dad00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已有结果！** `plan019_1_7b_sft_s44_eval` 已存在完整数据，无需重跑。

## 结果对比

| Model | ign_f1 | evi_f1_joint | 备注 |
|-------|--------|-------------|------|
| **SFT s42 1.7B** | 0.4786 | 0.3958 | `qwen3_1_7b_sft_eval` |
| **SFT s44 1.7B** | 0.4321 | 0.3482 | `plan019_1_7b_sft_s44_eval` |
| RSFT s42 1.7B (d102) | 0.5122 | 0.4275 | |
| RSFT s44 1.7B (d158) | 0.4730 | 0.3897 | |

## 结论

SFT s44 本身就比 SFT s42 弱 **4.65pp**（0.4321 vs 0.4786）。

RSFT 相对 SFT 的提升：
- RSFT s42 over SFT s42: **+3.36pp** (0.5122 - 0.4786)
- RSFT s44 over SFT s44: **+4.09pp** (0.4730 - 0.4321)

RSFT s44 的绝对值低不是 RSFT pipeline 的问题——是 SFT s44 base 本身弱。RSFT 的相对提升其实 s44 (+4.09pp) > s42 (+3.36pp)。

注：plan019 eval 用的 inference seed=42（非 44），但对 greedy 生成影响可忽略。field_compliance 较低（52% vs 68%）也印证 SFT s44 自身质量差异。

---
