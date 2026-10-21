# deploy bjb2 28827 pi05 table2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-pi05-table2_20260526T055140_result.json`
- **Structured JSON:** [`8ea986afb9b12a736857.json`](../../sessions/8e/8ea986afb9b12a736857.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**汇总：**
- bjb2-28827 上 6 个 π0.5 Spatial 实验**已在运行**（约 6 分钟前由先前 session 启动）
- GPU 0-2: `crm_obs_only` K=2, seed 42/43/44
- GPU 3-5: `adaptive_conformal_crm` K=2 τ=0.25 ε=0.2, seed 42/43/44
- 依赖齐全：CRM checkpoint (2.4MB) ✓, π0.5 模型 ✓, evaluate.py ✓
- 日志正常：task 1 rollout 5/20，5/5 success
- Registry 已全部注册为 RUNNING

无需额外部署操作。之前的 SmolVLA 实验（registry 中 6 个 RUNNING on bjb2-28827）实际进程已被替换，需要后续更新那些 registry 条目状态。

---
