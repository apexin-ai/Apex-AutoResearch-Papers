# ops check cls 8b eval result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cls-8b-eval-result_20260514T012144_result.json`
- **Structured JSON:** [`5c51a55e80e192627de0.json`](../../sessions/5c/5c51a55e80e192627de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**CLS 8B eval 未退出，仍在运行中。** Cron 误判。

当前状态：

| Eval | GPU | 进度 | running_acc | 状态 |
|------|-----|------|-------------|------|
| cls_8b (D056) | 3 (21.6GB, 100%) | 5440/9784 (55.6%) | 69.8% | 运行中 |
| cls_v5 | 2 (18.4GB, 54%) | 7520/9784 (76.9%) | 52.6% | 运行中 |
| cwm_seed123 | 0 (13.0GB, 88%) | 176/9784 (1.8%) | 58.0% | 运行中 |
| cwm_v12 | 1 (13.0GB, 81%) | 176/9784 (1.8%) | 58.0% | 运行中 |

4 个 eval 全部在跑，无一退出。cls_v5 最快（77%），两个 CWM 刚开始（1.8%），cls_8b 过半（56%）。按当前速度 cls_8b 大约还需 ~30 分钟完成。

---
