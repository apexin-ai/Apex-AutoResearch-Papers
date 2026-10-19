# fix checkpoint path and deploy prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_checkpoint-path-and-deploy-prep_20260523T010352_result.json`
- **Structured JSON:** [`f6afe447dcc48406957c.json`](../../sessions/f6/f6afe447dcc48406957c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 产出汇总

### 1. evaluate.py 路径修复
- **bjb1-32546**: 第533行 `crm_v3_norm/obs_only/crm_best.pt` → `crm_smolvla_3suite_v1/crm_best.pt`，语法验证通过
- **bjb2-40593**: 第536行同样修复完成（注：bjb2-28827 主机名已失效，改为直接在 bjb2-40593 上 sed 修复）

### 2. 本地部署脚本更新
- **deploy_3dir_spatial_seed42.md**: nohup → tmux + PIPESTATUS 防护，服务器引用更新为 bjb2-40593
- **deploy_adaptive_k_eval.sh**: CRM_CKPT 从 `crm_v3_norm/obs_only/crm_best.pt` → `crm_smolvla_3suite_v1/crm_best.pt`

### 3. GPU 状态

**bjb1-32546** — 正在跑 CRM eval（全部已用新 checkpoint）：
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 34% | 3132 MiB | CRM spatial seed42 |
| 1 | 34% | 3132 MiB | CRM spatial seed43 |
| 2 | 34% | 3132 MiB | CRM spatial seed44 |
| 3 | 10% | 542 MiB | pi05 eval session (待机/排队) |
| 4 | 33% | 3351 MiB | CRM goal seed42 |
| 5 | 30% | 2900 MiB | CRM goal seed43 |

**bjb2-40593** — 全部空闲：GPU 0 利用率 0%，无 evaluate.py 进程。

---
