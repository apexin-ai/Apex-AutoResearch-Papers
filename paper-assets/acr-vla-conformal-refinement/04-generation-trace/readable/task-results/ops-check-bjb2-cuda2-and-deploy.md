# ops check bjb2 cuda2 and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb2-cuda2-and-deploy_20260515T183742_result.json`
- **Structured JSON:** [`d32462d7e0603d89bc45.json`](../../sessions/d3/d32462d7e0603d89bc45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:2 不空闲，无法提交新实验。**

cuda:2 上运行着 `eval-mag-perdof-norm0p3-object`（PID 117278，已运行约 1 小时，占用 5645 MiB），是通过 `submit_training_job` 提交的 perdof norm=0.3 实验。

### 全部 GPU 状态

| GPU | PID | 实验 | 状态 |
|-----|-----|------|------|
| cuda:0 | 105947 | eval-mag-perdof-norm003 (`--max_correction_norm 0.03`) | 正常 |
| cuda:1 | 109655 | eval-mag-perdof-norm005 (`--max_correction_norm 0.05`) | 正常 |
| cuda:2 | 117278 | **eval-mag-perdof-norm0p3** (`--max_correction_norm 0.3`, output `eval_object_perdof_norm0p3.json`) | 通过 submit_training_job 提交 |
| cuda:3 | 118886 | eval-mag-perdof-norm03 (`--max_correction_norm 0.3`, output `eval_object_perdof_norm03.json`) | 手动提交 |
| cuda:4 | 101616 | eval-mag-obsonly-norm005 (`--max_correction_norm 0.05`) | 正常 |
| cuda:5 | 103034 | eval-mag-obsonly-norm03 (`--max_correction_norm 0.3`) | 正常 |

**注意：cuda:2 和 cuda:3 跑的是同一个实验（perdof, norm=0.3），只是输出文件名不同（`norm0p3` vs `norm03`）。** 这是重复提交。需要决定是否 kill 其中一个来腾出 GPU 给 `eval-acr-object-obs-only-default`。

---
