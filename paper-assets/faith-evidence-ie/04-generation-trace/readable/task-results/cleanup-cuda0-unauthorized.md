# cleanup cuda0 unauthorized

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_cuda0_unauthorized_20260521T184430_result.json`
- **Structured JSON:** [`2a8ef3653fc24d2cab66.json`](../../sessions/2a/2a8ef3653fc24d2cab66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，汇报：

**进程状态：**
| PID | 进程 | 状态 |
|-----|------|------|
| 126054 | test_eval_4b_sft_s42 | ✅ 保留，正常运行 (16/500, ~3%) |
| 126534/126539 | freige.training.r... (未知训练) | ❌ 已 kill |
| 126855/126860 | retrain_4b_rsft_ced_s42 (未授权) | ❌ 已 kill |

**cuda:0 显存：** 9,409 MiB / 97,887 MiB — 仅剩 test_eval_4b_sft_s42，OOM 风险已消除。

**test_eval_4b_sft_s42：** 正常推理中，已完成 16/500 样本。

---
