# ssh redeploy bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_redeploy-bjb2-28827_20260519T214903_result.json`
- **Structured JSON:** [`feac8a6f6bbd3901847d.json`](../../sessions/fe/feac8a6f6bbd3901847d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 CRM 实验全部启动成功：

| Session | GPU | PID | Benchmark | Seed | 状态 |
|---|---|---|---|---|---|
| eval-crm-goal-seed44-r2 | cuda:0 | 24694 | goal | 44 | 已加载 10 tasks |
| eval-crm-goal-seed45-r2 | cuda:2 | 24959 | goal | 45 | 已加载 10 tasks |
| eval-crm-long-seed47 | cuda:3 | 25274 | long | 47 | 加载中 |

所有实验使用 `--mode crm_obs_only --K 10 --max_correction_norm 0.2 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --n_rollouts 10`。

注意：PID 21588 (eval-vla-only-spatial-seed49) 已不存在，可能之前已结束。cuda:5 上的 openvla baseline (PID 900134) 仍在运行。

---
