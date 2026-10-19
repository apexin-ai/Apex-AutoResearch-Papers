# deploy free gpu fill urgent r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_free-gpu-fill-urgent-r2_20260524T181910_result.json`
- **Structured JSON:** [`e9b002f2bd665a78b405.json`](../../sessions/e9/e9b002f2bd665a78b405.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9 个新会话全部创建成功。旧的非-v2 stale 会话存在但不占 GPU（之前检查时显存为 4 MiB），不干扰。等待 2 分钟后做最终 PID 验证。

**当前部署进度（步骤 2A: π0.5 模型可用）**

| # | Server | GPU | exp_id | PID | Mode | Benchmark | Seed |
|---|--------|-----|--------|-----|------|-----------|------|
| 1 | bjb1-32546 | cuda:0 | eval-pi05-vla-only-spatial-s42-v2 | 581363 | vla_only | spatial | 42 |
| 2 | bjb1-32546 | cuda:2 | eval-pi05-vla-only-spatial-s43-v2 | 581958 | vla_only | spatial | 43 |
| 3 | bjb1-32546 | cuda:3 | eval-pi05-vla-only-goal-s42-v2 | 582430 | vla_only | goal | 42 |
| 4 | bjb1-32546 | cuda:4 | eval-pi05-vla-only-goal-s43-v2 | 583098 | vla_only | goal | 43 |
| 5 | bjb1-32546 | cuda:5 | eval-pi05-vla-only-object-s42-v2 | 583769 | vla_only | object | 42 |
| 6 | bjb2-28827 | cuda:0 | eval-pi05-vla-only-object-s43-v2 | 393309 | vla_only | object | 43 |
| 7 | bjb2-28827 | cuda:1 | eval-pi05-reconvla-spatial-s42 | 395002 | reconvla | spatial | 42 |
| 8 | bjb2-28827 | cuda:2 | eval-pi05-reconvla-goal-s42 | 393784 | reconvla | goal | 42 |
| 9 | bjb2-28827 | cuda:3 | eval-pi05-reconvla-object-s42 | 394188 | reconvla | object | 42 |

cuda:1（PID 395002）首次提交因 stale tmux 会话冲突，已 kill 旧会话并重新提交成功。已安排 ~2 分钟后回来做 PID 健康检查。

---
