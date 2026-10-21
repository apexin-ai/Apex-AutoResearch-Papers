# diagnose mvp2 grpo flatnli r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp2_grpo_flatnli_r3_20260514T151222_result.json`
- **Structured JSON:** [`bf6f6fe9ad4659f73217.json`](../../sessions/bf/bf6f6fe9ad4659f73217.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：**误报，进程正常运行**

PID 53292 在 cuda:3 上正常训练，当前 step 94/756（12%），GPU 占用 13GB。

**误报原因**：监控系统依赖 sentinel 文件和 W&B heartbeat 判活，但该实验可能未成功连接 W&B（AutoDL 网络），也未写入 sentinel 文件，被误判为 dead。

**训练健康度**：正常，非 mode collapse。reward 在 0.33-0.74 波动，f1 从 step 84 起开始出现，grad_norm 健康。唯一需关注的是 clipped_ratio 偏高（0.41-0.73）。

| 字段 | 值 |
|------|-----|
| error_type | false_alarm |
| can_auto_fix | N/A（无需修复） |
| action | 标记为 running，修复监控检测逻辑 |

---
