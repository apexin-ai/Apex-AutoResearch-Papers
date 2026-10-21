# deploy bjb2 40593 gpu0

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-40593-gpu0_20260524T064404_result.json`
- **Structured JSON:** [`86e7a615016c78e9006c.json`](../../sessions/86/86e7a615016c78e9006c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重复条目已修复。

**结果汇总：**

| 任务 | 状态 |
|------|------|
| 收割 `eval-supp-crm-norm005-obj-s45` | 已完成 (SR=76.5%)，无需操作 |
| 修复重复条目 `eval-supp-obj-crm-norm005-s45` | PREPARING → DONE 已修复 |
| 部署 Spatial CRM s46 | **已跑完** (SR=81%)，无需部署 |
| GPU 0 | 被 `eval-supp-spatial-crm-norm005-s47` 占用（刚启动，预计需 1-2 小时） |

**无新实验可部署** — Spatial CRM s46 已有结果，s47 正在跑，GPU 0 没有空闲窗口。

---
