# deploy bjb1 32546 gpu0 gpu2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-gpu0-gpu2_20260524T082906_result.json`
- **Structured JSON:** [`70db2751fee6cd1a4964.json`](../../sessions/70/70db2751fee6cd1a4964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 GPU 全部在工作。部署完成。

## 部署汇总 — bjb1-32546

**变更说明：** 原任务要求的 Spatial Adaptive s46 和 CRM norm005 Spatial s46 已有成功结果（SR=80%、81%），无需重跑。改为部署 **Object s47**（此前 0 覆盖）。

| GPU | 实验 | Registry ID | Tmux Session |
|-----|------|------------|--------------|
| 0 | Object VLA-only s47 | `eval-supp-obj-vla-only-s47` | `obj-vla-s47` |
| 1 | Object K2mean s47 | `eval-supp-obj-k2mean-s47` | `obj-k2mean-s47` |
| 2 | Object CRM norm005 s47 | `eval-supp-obj-crm-norm005-s47` | `obj-crm-s47` |
| 3 | Object Adaptive s47 | `eval-supp-obj-adapt-tau025-s47` | `obj-adapt-s47` |
| 4 | Long Reconvla s47 (已有) | `eval-supp-long-reconvla-s47` | `long-reconvla-s47` |
| 5 | Long CRM s47 (已有) | `eval-supp-long-crm-norm005-s47` | `long-crm-s47` |

**仍缺失：** Object Reconvla s47（第5个方法，等 GPU 释放后可补）。

**另外注意：** `eval-supp-long-crm-norm005-s46` 在 registry 中仍标记 RUNNING，但已有完整 metrics（SR=0.54, 108/200），应标记为 DONE。

---
