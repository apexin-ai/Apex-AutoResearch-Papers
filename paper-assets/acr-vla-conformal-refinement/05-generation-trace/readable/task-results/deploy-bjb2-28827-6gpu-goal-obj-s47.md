# deploy bjb2 28827 6gpu goal obj s47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-6gpu-goal-obj-s47_20260524T094131_result.json`
- **Structured JSON:** [`4c144c2fd2b592dd59a4.json`](../../sessions/4c/4c144c2fd2b592dd59a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 registry 条目已创建并设为 RUNNING。

## 汇报

**bjb2-28827 服务器状态：** 无 OpenVLA 进程（已被之前某次操作 kill 或替换），6 个 GPU 已全部部署目标 SmolVLA eval 实验。

| GPU | exp_id | PID | 状态 |
|-----|--------|-----|------|
| 0 | `eval-supp-goal-adapt-tau025-s47` | 205107 | 已加载模型+CRM，运行中 |
| 1 | `eval-supp-goal-crm-norm005-s47` | 199883 | rollout 5/20 进行中 |
| 2 | `eval-supp-goal-k2mean-s47` | 205380 | 已加载模型，运行中 |
| 3 | `eval-supp-goal-reconvla-s47` | 200418 | rollout 5/20 进行中 |
| 4 | `eval-supp-obj-reconvla-s47` | 200690 | rollout 5/20 进行中 |
| 5 | `eval-supp-long-k2mean-s47-r2` | 205647 | 已加载模型，运行中 |

**注意事项：**
- Registry 中有几个旧条目（spatial s45/s46、OpenVLA v3）仍标记为 RUNNING 但对应进程已不存在于 bjb2-28827，可能需要后续清理
- 任务中的 mode 名与代码实际参数的对应：`adaptive` = `adaptive_conformal_crm`，`k2_mean` = `vla_only --baseline_mode mean`

---
