# monitor bjb1 32546 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-32546-status_20260515T044914_result.json`
- **Structured JSON:** [`a8c8b92b8b010ef8a919.json`](../../sessions/a8/a8c8b92b8b010ef8a919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 Object Eval Status

| Experiment | Mode | GPU | PID | Tasks Done | Total | Task 1 SR | Status |
|---|---|---|---|---|---|---|---|
| eval-reconvla-object | reconvla, K=10 | cuda:0 | 9659 | 1/10 | 10 | 0% | **running** — task 2 rollout 5/10 |
| eval-acr-object-v4-perdof | crm_perdof, norm=0.1 | cuda:1 | 11116 | 1/10 | 10 | 0% | **running** — task 2 rollout 5/10 |
| eval-acr-object-v4-obs-only | crm_obs_only, norm=0.1 | cuda:2 | 13806 | 1/10 | 10 | 0% | **running** — starting task 2 |
| eval-acr-object-v4-scalar | crm_scalar, norm=0.1 | cuda:3 | 14012 | 1/10 | 10 | 0% | **running** — starting task 2 |
| eval-vla-only-object | vla_only, K=1 | cuda:4 | — | **10/10** | 10 | 0% | **done** — SR=12.0% |
| eval-vla-mean-object | vla_only mean, K=10 | cuda:5 | 18814 | 1/10 | 10 | 0% | **running** — starting task 2 |

### eval-vla-only-object 完整结果 (SR = 12.0%)

| Task | Success | Rate |
|---|---|---|
| alphabet_soup | 0/10 | 0% |
| cream_cheese | 1/10 | 10% |
| salad_dressing | 2/10 | 20% |
| bbq_sauce | 2/10 | 20% |
| ketchup | 0/10 | 0% |
| tomato_sauce | 1/10 | 10% |
| butter | 0/10 | 0% |
| milk | 1/10 | 10% |
| chocolate_pudding | 2/10 | 20% |
| orange_juice | 3/10 | 30% |

### 备注

- 所有 5 个运行中的实验都刚完成第 1 个 task（alphabet_soup，全部 0%），正在进入 task 2（cream_cheese）
- obs_only 和 scalar 的日志在 `/root/runs/acr-vla-conformal-refinement/` 而非 `logs/` 目录，且未指定 `--output_file`，完成后不会自动生成 JSON
- scalar 实际 PID=14012（非 14003），vla_mean 实际 PID=18814（非 18808）
- 按当前进度估算，每个实验还需完成 9 个 task × 10 rollouts，预计数小时后完成

---
