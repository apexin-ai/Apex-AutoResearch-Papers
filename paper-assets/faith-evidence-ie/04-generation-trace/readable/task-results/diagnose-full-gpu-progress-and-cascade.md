# diagnose full gpu progress and cascade

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-gpu-progress-and-cascade_20260522T073135_result.json`
- **Structured JSON:** [`99d5e6d740198dc554a7.json`](../../sessions/99/99d5e6d740198dc554a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## 完成的实验

**test_eval_4b_sft_s42_no_evi** → DONE
| 指标 | 值 |
|------|-----|
| ign_f1 | 0.2219 |
| precision | 0.2753 |
| recall | 0.1859 |
| 配对 with-evi ign_f1 | 0.2232 |
| **test fair_tax** | **-0.13pp** (evidence 略有帮助) |

与 dev fair_tax +0.25±0.47pp 一致，test 上也确认 4B SFT evidence tax 中性。Registry 已更新为 DONE/success。

## 仍在运行

| 实验 | GPU | 进度 | 预计完成 |
|------|-----|------|---------|
| dev_eval_4b_rsft_ced_s42_v2 | cuda:0 | 553/985 (56%) | ~3h后 |
| test_eval_llama_sft_s42_no_evi | cuda:3 | 运行中 2h54m | 待定 |

## 未提交的后续任务

dev_eval_4b_rsft_ced_s42_v2 尚未完成（metrics.json 不存在），cuda:1 和 cuda:2 空闲。等 dev eval 完成后根据 ign_f1 决定是否提交 test eval。

---
