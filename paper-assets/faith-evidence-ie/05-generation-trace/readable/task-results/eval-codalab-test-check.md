# eval codalab test check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_codalab_test_check_20260517T125948_result.json`
- **Structured JSON:** [`00c8578b615b33260aa6.json`](../../sessions/00/00c8578b615b33260aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Test predictions 已存在且格式正确。

**汇总：**

| 文件 | 路径 | 状态 |
|---|---|---|
| **plan_002_test_rsft_s43** | `/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/` | 完整 |
| **plan_002_test_rsft_s44** | `/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/` | 完整 |

**plan_002_test_rsft_s43 详情（RSFT CED s43, checkpoint-510）：**
- `predictions.json`: 8.1MB, 1000 docs, 27,119 predictions, format_ok 99.8%
- `codalab_submission.json`: 2.3MB, **25,741 triples**, 标准 DocRED 提交格式 `[{title, h_idx, t_idx, r, evidence}, ...]`
- 可直接提交 CodaLab

**plan_002_test_rsft_s44 详情（RSFT s44, checkpoint-510）：**
- `predictions.json`: 8.1MB, 1000 docs, 26,925 predictions, format_ok 99.6%
- `codalab_submission.json`: 2.3MB, 格式同上
- 可直接提交 CodaLab

文件已就绪，无需重跑 inference。两个 seed 的 `codalab_submission.json` 均可直接提交 CodaLab。

---
