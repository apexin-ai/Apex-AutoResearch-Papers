# diagnose full gpu status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-gpu-status-check_20260522T040247_result.json`
- **Structured JSON:** [`974348f58ce3c185ca2f.json`](../../sessions/97/974348f58ce3c185ca2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

| 实验 | GPU | 状态 | 备注 |
|------|-----|------|------|
| dev_eval_4b_rsft_ced_s42_v2 | cuda:0 | **FAILED** | `FileNotFoundError: dev.json`（目录只有 `dev_revised.json`），需重提加 `--split dev_revised` |
| test_eval_1_7b_sft_s42_no_evi | cuda:1 | **DONE** ✓ | ign_f1=0.2093, precision=0.3899, recall=0.143 |
| test_eval_8b_sft_s42_no_evi | cuda:2 | **RUNNING** 55% | 273/500, ~31s/it, 预计还需 ~1h57m |
| test_eval_14b_sft_s42_no_evi | cuda:3 | **RUNNING** 91% | 454/500, ~38s/it, 预计还需 ~29min |

### GPU 总览

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 0 / 98GB | 0% | **空闲** |
| 1 | 0 / 98GB | 0% | **空闲** |
| 2 | 19.6 / 98GB | 87% | 8B eval |
| 3 | 32.5 / 98GB | 92% | 14B eval |

### 需要处理

**dev_eval_4b_rsft_ced_s42_v2** 需要重提。inference.py 的 `load_split` 默认查找 `dev.json`，但数据目录只有 `dev_revised.json`。需要加 `--split dev_revised` 参数。GPU 0 已空闲，可以立即重提。是否现在重提？

---
