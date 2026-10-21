# cron register obj s47 r2 retry

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cron_register-obj-s47-r2-retry_20260524T134341_result.json`
- **Structured JSON:** [`62785edf600385f5043e.json`](../../sessions/62/62785edf600385f5043e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

k2mean 不在 registry 中。该实验没有结果文件且无运行进程——属于未完成状态。

## 汇报

| 实验 | exp_id | 状态 | 结果 |
|------|--------|------|------|
| vla-only | eval-supp-obj-vla-only-s47-r2 | **DONE** | success_rate = 0.755 |
| crm | eval-supp-obj-crm-norm005-s47-r2 | **DONE** | success_rate = 0.825 |
| adapt | eval-supp-obj-adapt-tau025-s47-r2 | **DONE** | success_rate = 0.77 (trigger_rate=4.03%) |
| k2mean | eval-supp-obj-k2mean-s47-r2 | **未完成** | 日志只有初始化，无结果 JSON，进程已死 |

**不需要注册 cron**——3 个实验已完成并更新为 DONE，k2mean 需要重新启动。

k2mean 的问题：其 `output_file` 设为 `logs/eval_object_vla_only_seed47.json`（与 vla-only 相同），可能是启动参数未指定独立输出路径。重跑时需要修正输出文件名或确认脚本内部有 baseline_mode 区分逻辑。

---
