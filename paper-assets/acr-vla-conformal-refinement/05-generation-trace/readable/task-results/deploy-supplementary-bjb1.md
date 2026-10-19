# deploy supplementary bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_supplementary-bjb1_20260523T032249_result.json`
- **Structured JSON:** [`d4fcbf43b39c5338b516.json`](../../sessions/d4/d4fcbf43b39c5338b516.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个实验全部启动成功，参数正确：

| tmux session | GPU | 实验 | Python PID |
|---|---|---|---|
| `crm_norm02` | cuda:0 | CRM norm=0.2 always-on, spatial | **625804** |
| `adapt_tau015` | cuda:1 | Adaptive tau=0.15, spatial | **626005** |
| `adapt_tau025` | cuda:2 | Adaptive tau=0.25, spatial | **626274** |
| `adapt_tau035` | cuda:4 | Adaptive tau=0.35, spatial | **626543** |
| `obj_crm005` | cuda:5 | CRM norm=0.05, object | **626812** |

已 kill 旧 `dirA_norm03` session。GPU 3 的 CRM 4-suite training（PID 548658）未动。

---
