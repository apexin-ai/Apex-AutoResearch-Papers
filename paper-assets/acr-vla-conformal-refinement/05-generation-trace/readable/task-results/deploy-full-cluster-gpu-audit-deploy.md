# deploy full cluster gpu audit deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_full-cluster-gpu-audit-deploy_20260523T090232_result.json`
- **Structured JSON:** [`826a647d6c4c753e1312.json`](../../sessions/82/826a647d6c4c753e1312.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 审计结果

### bjb1-32546（6 GPU，有 CRM checkpoint）
| GPU | 显存 | 实验 |
|-----|------|------|
| 0 | 5173/24564 MiB | adaptive_conformal_crm object s43 |
| 1 | 4707/24564 MiB | crm_obs_only goal s43 norm=0.05 |
| 2 | 4613/24564 MiB | adaptive_conformal_crm goal s43 |
| 3 | 544/24564 MiB | train_crm unified 4suite r6（CRM 训练） |
| 4 | 5267/24564 MiB | crm_obs_only object s43 norm=0.05 |
| **5** | **4→加载中** | **🆕 adapt-tau025-goal-s44（刚部署）** |

### bjb2-28827（6 GPU，有 CRM checkpoint）
| GPU | 显存 | 实验 |
|-----|------|------|
| 0 | 2847/24564 MiB | adaptive_conformal_crm object s42 |
| 1 | 2845/24564 MiB | k2mean object s42 |
| 2 | 5692/24564 MiB | reconvla object s43 |
| 3 | 2409/24564 MiB | reconvla goal s42 |
| 4 | 2505/24564 MiB | k2mean spatial s42 |
| 5 | 2347/24564 MiB | vla_only goal s42 wrapper（不重复部署） |

### bjb2-40593（1 GPU，无 CRM checkpoint）
| GPU | 显存 | 实验 |
|-----|------|------|
| 0 | 5324/24564 MiB | k2mean goal s42 r2 |

### bjb1-18228（4 GPU，无 CRM checkpoint）
| GPU | 显存 | 实验 |
|-----|------|------|
| 0-3 | ~9884/24564 MiB | precompute-pi05 object（不 kill） |

### cqa1-32758（6 GPU，无 CRM checkpoint）
| GPU | 显存 | 实验 |
|-----|------|------|
| 0 | 4356/24564 MiB | k2mean spatial s43 |
| 1 | 4912/24564 MiB | reconvla spatial s43 |
| 2 | 4967/24564 MiB | k2mean object s43 |
| 3 | 4912/24564 MiB | reconvla spatial s44 |
| 4 | 4419/24564 MiB | k2mean goal s43 |
| 5 | 4901/24564 MiB | reconvla goal s43 |

## 新部署
| 实验 | 服务器 | GPU | exp_id | 状态 |
|------|--------|-----|--------|------|
| Goal Adaptive tau=0.25 s44 | bjb1-32546 | 5 | eval-supp-adapt-tau025-goal-s44 | RUNNING（模型加载中） |

## 最终状态
**总 GPU：23/23 在用**（含新部署 1 个）。集群已满载，无更多空卡可部署。

剩余未部署的优先级任务（等卡释放后部署）：
- P1: Goal CRM norm=0.05 s44、Goal Reconvla s44
- P2: Object Adaptive tau=0.25 s44、Object CRM norm=0.05 s44、Object Reconvla s44、Object K=2 mean s44
- P3: Spatial K=2 mean s44

---
