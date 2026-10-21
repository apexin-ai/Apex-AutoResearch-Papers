# diagnose all running experiments

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_all_running_experiments_20260521T231807_result.json`
- **Structured JSON:** [`25da69a7b9553ad310e4.json`](../../sessions/25/25da69a7b9553ad310e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验都在正常运行，GPU 全部在用。Director 的 "idle 16h+" 判断有误。

## 汇总报告

| 实验ID | 实际状态 | 进度 | GPU | 预计剩余 |
|--------|---------|------|-----|---------|
| test_eval_14b_sft_s42 | **RUNNING** ✓ | 419/500 (84%) | cuda:1, 32.5GB, 91% | ~1h |
| test_eval_1_7b_sft_s42 | **RUNNING** ✓ | 70/500 (14%) | cuda:0, 6.1GB, 52% | ~3.2h |
| retrain_4b_rsft_ced_s42_v2 | **RUNNING** ✓ | 53/510 (10%) | cuda:2, 94.5GB, 99% | ~38min |
| test_eval_14b_sft_s42_no_evi | **RUNNING** ✓ | 5/500 (1%) | cuda:3, 32.5GB, 91% | ~6.7h |

**结论：全部 4 个实验进程存活且活跃推进，GPU 利用率正常。Registry 状态准确，无需更新。**

最先完成的是 retrain_4b_rsft_ced_s42_v2（~38min），其次是 test_eval_14b_sft_s42（~1h）。

---
