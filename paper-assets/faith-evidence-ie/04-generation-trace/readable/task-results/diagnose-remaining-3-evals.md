# diagnose remaining 3 evals

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_remaining-3-evals_20260522T013439_result.json`
- **Structured JSON:** [`407f8ef4c8fb96623004.json`](../../sessions/40/407f8ef4c8fb96623004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Conversion works. Output is a flat list with `title`, `h_idx`, `t_idx`, `r`, `evidence` — correct CodaLab format, 8049 triples.

---

## 实验状态

| Status | Experiment | Progress | GPU | ETA |
|--------|-----------|----------|-----|-----|
| RUNNING | test_eval_1_7b_sft_s42 | 410/500 (82%) | GPU 0, 6GB | ~40 min |
| RUNNING | test_eval_1_7b_sft_s42_no_evi | 180/500 (36%) | GPU 1, 6GB | ~2h22m |
| RUNNING | test_eval_14b_sft_s42_no_evi | 218/500 (44%) | GPU 3, 32GB | ~3.5h |

额外发现：GPU 2 上跑着 `test_eval_4b_rsft_s42_v2` (PID 151222, 9.5GB, 18min)。

## Registry 更新
- 三个实验均未完成，无结果可写入

## CodaLab 脚本
- 状态: 已创建 `/root/autodl-tmp/freige/scripts/convert_codalab.py`
- 验证: 对 `test_eval_8b_rsft_s42/codalab_submission.json` 转换成功，输出 8049 triples，格式正确（list of `{title, h_idx, t_idx, r, evidence}`）

---
