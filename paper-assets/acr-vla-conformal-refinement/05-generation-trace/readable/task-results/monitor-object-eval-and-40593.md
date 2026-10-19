# monitor object eval and 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_object-eval-and-40593_20260515T051427_result.json`
- **Structured JSON:** [`49a1ba49fbb2440a10e4.json`](../../sessions/49/49a1ba49fbb2440a10e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: bjb1-32546 — Object Eval 进度

所有 6 个进程存活。GPU 0-5 均在使用 (21-23%, ~5.2GB each)。

| GPU | exp_id | mode | 运行时间 | 完成 tasks | 当前 task | 当前 rollout | 已完成 task SR |
|-----|--------|------|----------|-----------|-----------|-------------|---------------|
| cuda:0 | eval-reconvla-object | reconvla K=10 | 2h37m | 1/10 | #2 cream_cheese | 5/10 (0/5) | T1: 0% |
| cuda:1 | eval-acr-object-v4-perdof | crm_perdof norm=0.1 | 2h35m | 1/10 | #2 cream_cheese | 5/10 (0/5) | T1: 0% |
| cuda:2 | eval-acr-object-v4-obs-only | crm_obs_only norm=0.1 | 2h21m | 1/10 | #2 cream_cheese | 5/10 (**1/5**) | T1: 0% |
| cuda:3 | eval-acr-object-v4-scalar | crm_scalar norm=0.1 | 2h21m | 1/10 | #2 cream_cheese | 5/10 (0/5) | T1: 0% |
| cuda:4 | eval-vla-only-object-k1 | vla_only K=1 | 3m | 0/10 | 加载模型中 | — | — |
| cuda:5 | eval-vla-mean-object | vla_only mean K=10 | 2h14m | 1/10 | #2 cream_cheese | 5/10 (0/5) | T1: 0% |

**进度估算**: K=10 实验约 1.7h/task，10 tasks 共需 ~17h，剩余 ~14-15h。K=1 实验刚启动，预计 ~2h 完成。

**参考基线**: 已完成的 vla_only K=1 single 结果 (`eval_object_vla_only.json`): **overall SR = 12%** (12/100)。

目前 task 1 (alphabet_soup) 所有方法 SR 均为 0%——这和已完成基线一致（基线该 task 也是 0%）。obs_only 在 task 2 部分 rollout 中有 1/5 成功，是目前唯一看到 success 的 CRM 变体。

---

### Part 2: bjb2-40593 状态

- **v4-default-r3 已被 kill**，无训练进程
- **有活跃 eval 进程**: reconvla object eval (n_rollouts=**20**, K=10), PID 211962，已运行 3.5h
  - 进度: task 1 alphabet_soup, rollout 10/20, 0/20 success
  - 这是 20 rollouts 版本，比 bjb1 的 10 rollouts 慢一倍
- **GPU**: 1 GPU, 12% 利用率, 5592/24564 MiB — 被该 eval 占用，非空闲

---
