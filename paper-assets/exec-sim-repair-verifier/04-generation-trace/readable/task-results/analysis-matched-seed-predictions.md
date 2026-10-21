# analysis matched seed predictions

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matched-seed-predictions_20260512T160154_result.json`
- **Structured JSON:** [`d8110f54dc11a2a60e8d.json`](../../sessions/d8/d8110f54dc11a2a60e8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 结果报告

### 1. Checkpoint 路径
| Model | Seed | Checkpoint Path | Date |
|-------|------|----------------|------|
| CLS | 42 | `checkpoints_seed42/best/` | May 11 17:54 |
| CWM | 42 | `checkpoints_cwm/best/` | May 11 15:25 |

（`checkpoints/best/` 是另一个 CLS 运行，metrics 不同于 seed42，不是同一个。）

### 2. 已有 Aggregate Metrics
**eval_seed42.json (CLS seed42)** — 已存在：
- Accuracy: 87.83%，fail_f1: 87.59，pass_f1: 88.06

**eval_cwm_results.json (CWM default)** — 已存在：
- Accuracy: 87.51%，fail_f1: 87.71，pass_f1: 87.31
- Exact match rate: 84.02%

### 3. Per-instance Output：**脚本不支持**

两个脚本都**只输出 aggregate metrics**，不保存 per-instance predictions。

**`eval_verifier.py` 输出格式**：`{test_set_size, class_balance, majority_baseline_accuracy, overall_accuracy, per_class{fail/pass: P/R/F1}, confusion_matrix, unparseable_predictions}`

**`eval_cwm_baseline.py` 输出格式**：同上 + `cwm_metrics{exact_match_rate, by_error_type, generation_length}`

**缺失的内容**：
- `y_true` 和 `y_pred` 数组在内存中生成但未写入文件
- CWM 的 `gen_texts`（生成的执行输出文本）未保存
- 没有 `--save_predictions` 或类似参数
- 没有 sample ID 或可追踪的 per-instance 信息

**要获取 per-instance predictions，需要给两个脚本添加功能**——将 `y_true`、`y_pred`（以及 CWM 的 `gen_texts`）写入单独的 JSON 文件。按任务要求，不修改代码，在此报告格式限制。

---
