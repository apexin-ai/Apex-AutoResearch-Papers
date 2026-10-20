# code v2 rescore batch1

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2_rescore_batch1_20260515T225424_result.json`
- **Structured JSON:** [`6d81ef851c9ed42b2f76.json`](../../sessions/6d/6d81ef851c9ed42b2f76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Rescore 结果（v2 增强 matcher）

所有 14 项 unit test 通过。7 个目标文件全部已 rescore（修改时间更新为 `May 16 06:54`）。

| 文件 | Section | Old Acc | New Acc | Changed |
|------|---------|---------|---------|---------|
| accuracy_eval_ds_s015.json | dense | 0.52 | 0.52 | 0 |
| accuracy_eval_ds_s015.json | sparse | 0.36 | 0.36 | 0 |
| accuracy_eval_ds_s030.json | sparse | 0.10 | 0.10 | 0 |
| accuracy_eval_ds_dense_n50.json | top-level | 0.52 | 0.52 | 0 |
| accuracy_eval_qw_s015.json | dense | 0.32 | 0.32 | 0 |
| accuracy_eval_qw_s015.json | sparse | 0.34 | 0.34 | 0 |
| accuracy_eval_qw_s030.json | sparse | 0.14 | 0.14 | 0 |
| accuracy_eval_qw_s020.json | importance_s020 | 0.26 | 0.26 | 0 |
| accuracy_eval_qw_s025.json | importance_s025 | 0.32 | 0.32 | 0 |

**结论：v2 matcher 的增强规则（radical 简化、度数符号、分数小数互转）在 batch1 数据上未改变任何评分。** 所有 9 个 section 的 accuracy 保持不变，changed 均为 0。原始 matcher 已经正确处理了这些 case。备份已保存在 `analysis_output_pre_v2_backup/`。

---
