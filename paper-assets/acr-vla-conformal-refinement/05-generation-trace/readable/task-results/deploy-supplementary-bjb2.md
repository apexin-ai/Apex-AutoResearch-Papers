# deploy supplementary bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_supplementary-bjb2_20260523T032310_result.json`
- **Structured JSON:** [`7a8b1a88cf703d1e003f.json`](../../sessions/7a/7a8b1a88cf703d1e003f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 GPU 正常工作，三个新实验已加载环境和任务，开始运行。

---

## 汇总

### Object CRM eval（已完成）
| Seed | SR |
|------|------|
| 42 | 50.5% |
| 43 | 53.5% |
| 44 | 51.5% |
| **均值** | **51.8%** |

### Object VLA-only wrapper（仍在运行，GPU 3-5）
- 三个 seed 都在跑 tomato_sauce 任务（~第 6/10 个 task），预计还需几小时

### 新部署的 P3 实验
| Session | 实验 | GPU | 状态 |
|---------|------|-----|------|
| `obj_adapt` | Object Adaptive tau=0.074855 seed42 | 0 | 运行中 |
| `obj_reconvla` | Object Reconvla K=10 seed42 | 1 | 运行中 |
| `goal_crm005` | Goal CRM norm=0.05 seed42 | 2 | 运行中 |

P3-d (Goal Adaptive) 和 P3-e (Goal Reconvla) 等 VLA-only 跑完释放 GPU 3-5 后再部署。

---
