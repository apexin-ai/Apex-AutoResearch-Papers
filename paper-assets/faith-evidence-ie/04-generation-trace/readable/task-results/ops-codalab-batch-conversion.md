# ops codalab batch conversion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_codalab-batch-conversion_20260522T051453_result.json`
- **Structured JSON:** [`78f0aeb1930d5afde942.json`](../../sessions/78/78f0aeb1930d5afde942.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12 个文件全部转换成功，汇总：

| 实验 | Triples |
|------|---------|
| test_eval_14b_sft_s42 | 14,423 |
| test_eval_14b_rsft_s42 | 11,235 |
| test_eval_14b_sft_s42_no_evi | 15,563 |
| test_eval_8b_sft_s42 | 8,678 |
| test_eval_8b_rsft_s42 | 8,049 |
| test_eval_4b_sft_s42 | 10,609 |
| test_eval_4b_rsft_s42_v2 | 9,630 |
| test_eval_1_7b_sft_s42 | 8,020 |
| test_eval_1_7b_rsft_s42 | 7,793 |
| test_eval_1_7b_sft_s42_no_evi | 6,144 |
| test_eval_llama_sft_s42 | 9,502 |
| test_eval_llama_rsft_s42 | 9,641 |

- 输出格式已验证：`list[{title, h_idx, t_idx, r, evidence}]`
- 原地文件：各 `eval_results/test_eval_*/codalab_submission_codalab.json`
- 统一目录：`/root/autodl-tmp/codalab_submissions/{exp_id}.json`
- 失败：无

注意用户列表中的 `test_eval_4b_rsft_s42`（无 v2）不存在 `codalab_submission.json`，另外发现 3 个额外的 no_evi 目录（`4b_sft_s42_no_evi`、`8b_sft_s42_no_evi`、`llama_sft_s42_no_evi`）存在但没有 `codalab_submission.json`，未转换。

---
