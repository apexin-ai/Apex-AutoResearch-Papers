# ops verify gpu health all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpu-health-all-servers_20260515T193140_result.json`
- **Structured JSON:** [`27f3ee092088efa48fa6.json`](../../sessions/27/27f3ee092088efa48fa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心摘要：

**全部 17 GPU 健康，每 GPU 恰好一个实验在跑，无 OOM。**

| 服务器 | GPU 数 | 活跃实验 | 进度范围 |
|--------|--------|---------|---------|
| bjb2-40593 | 1/1 | crm_obs_only spatial norm=0.03 | 7/10 |
| bjb1-18228 | 4/4 | perdof/obs_only/reconvla object (seed42/43) | 0-5/10 |
| bjb1-32546 | 6/6 | obs_only/scalar/vla_mean object (seed42/43) | 0-2/10 |
| bjb2-28827 | 6/6 | perdof/obs_only object (多 norm 值) | 0-1/10 |

**bjb2-28827:cuda:2 无冲突** — PID 138858 已退出，只有 PID 140759 独占该 GPU。

bjb1-18228 上 eval-mag-obsonly-norm03-b2 此前被 kill (exit 143)，当前无影响。

---
