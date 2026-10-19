# deploy magnitude sweep bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_magnitude-sweep-bjb2-28827_20260515T031505_result.json`
- **Structured JSON:** [`989c824987a702afca10.json`](../../sessions/98/989c824987a702afca10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 GPU 全部在使用中，实验正在加载。

### 部署结果

| exp_id | PID | GPU | mode | norm | 状态 |
|--------|-----|-----|------|------|------|
| eval-mag-perdof-norm003 | 13185 | cuda:0 | acr_vla | 0.03 | 运行中 |
| eval-mag-perdof-norm005 | 13456 | cuda:1 | acr_vla | 0.05 | 运行中 |
| eval-mag-perdof-norm02 | 13728 | cuda:2 | acr_vla | 0.2 | 运行中 |
| eval-mag-perdof-norm03 | 14260 | cuda:3 | acr_vla | 0.3 | 运行中 |
| eval-mag-obsonly-norm005 | 14854 | cuda:4 | crm_obs_only | 0.05 | 运行中 |
| eval-mag-obsonly-norm02 | 15190 | cuda:5 | crm_obs_only | 0.2 | 运行中 |

6/6 实验全部提交成功。注意 GPU 0-2 之前已有进程占用（各 ~6.2GB），新实验共享了这些 GPU，当前显存用量 11-12GB，4090 有 24GB 应该够用。

---
