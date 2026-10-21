# ssh vota checkpoint version check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vota_checkpoint_version_check_20260515T145337_result.json`
- **Structured JSON:** [`8f439b726121380416bd.json`](../../sessions/8f/8f439b726121380416bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MD5 一致说明 final/ 和 checkpoint-444 是同一个文件。现在完整的情况已经清楚了。

## 报告

### vota/final 对应哪次训练

**第四次训练运行**（started 09:46, finished ~12:07），run_name = `vota_seed42_v5`，seed=42，3 epochs。

时间线：
| 时间 | 事件 |
|------|------|
| 02:01 | Run 1 开始训练 |
| 04:18 | Run 1 完成，保存 checkpoints + final/ |
| **05:36** | **evaluate.py 对 Run 1 adapter 评估 → 99.16%** (写入 eval_results.json) |
| 06:12, 06:21 | Run 2, Run 3（中间尝试） |
| 09:46 | Run 4 开始训练 |
| **12:07** | **Run 4 完成，覆盖了所有 checkpoint 和 final/ 的 adapter 文件** |
| 20:34 | calibration.py 对 Run 4 adapter 评估 → **99.41%** |

### 99.41% vs 99.16% 差异原因

**不同 checkpoint，不是不同评估方法。**

- `eval_results.json`（99.16% = 1180/1190）是 Run 1 的 adapter 的结果，但那个 adapter 已经在 12:07 被 Run 4 覆盖了。eval_results.json 没有被重新生成，所以是**过期数据**。
- `calibration_metrics.json`（99.41% = 1183/1190）是 Run 4 当前 adapter 的结果。两个脚本的预测方法完全一致（greedy generation, max_new_tokens=1）。
- ROADMAP 记录的 "99.2%" 就是 99.16% 四舍五入到一位小数。

### 论文应该用哪个数字

**99.41%**（1183/1190）——这是当前 final/ adapter 的真实 accuracy。

建议重新运行 evaluate.py 更新 eval_results.json 使其与当前 adapter 一致，避免后续混淆。

---
