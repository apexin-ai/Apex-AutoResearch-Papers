# deploy bjb1 32546 fill 4gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-fill-4gpu_20260520T172918_result.json`
- **Structured JSON:** [`8b2f582a0df769848737.json`](../../sessions/8b/8b2f582a0df769848737.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**审计结果：**
- cuda:0/1/3/4 确认空闲，cuda:2/5 在跑 K sweep seed44
- 1 个未 harvest 的 JSON（eval-perdof-object-norm02-seed49, success_rate=0.12）已更新到 DONE

**部署状态（全部 RUNNING，日志初始化正常）：**

| GPU | exp_id | mode | benchmark | seed |
|-----|--------|------|-----------|------|
| cuda:0 | eval-obs-only-spatial-norm02-seed50 | crm_obs_only K=10 ε=0.2 | spatial | 50 |
| cuda:1 | eval-perdof-object-norm02-seed50 | crm_perdof K=10 ε=0.2 | object | 50 |
| cuda:3 | eval-vla-only-object-seed49 | vla_only K=1 | object | 49 |
| cuda:4 | eval-obs-only-object-norm02-seed51 | crm_obs_only K=10 ε=0.2 | object | 51 |

bjb1-32546 全部 6 张 GPU 现已满载。

---
