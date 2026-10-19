# ops progress check all running

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-all-running_20260515T051719_result.json`
- **Structured JSON:** [`7bd4c3c60b4f6cb22f6b.json`](../../sessions/7b/7bd4c3c60b4f6cb22f6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

## GPU 状态

| Server | GPU 0 | GPU 1 | GPU 2 | GPU 3 | GPU 4 | GPU 5 |
|--------|-------|-------|-------|-------|-------|-------|
| bjb1-32546 | 22%, 5165M | 23%, 5201M | 22%, 5201M | 23%, 5201M | 23%, 5629M | 21%, 5165M |
| bjb2-28827 | 19%, 5183M | 22%, 5183M | 18%, 5183M | 19%, 5183M | 19%, 5183M | 19%, 5182M |

全部 12 GPU 在用，负载正常。

---

## Server 1: bjb1-32546 — Object Eval（6 个实验）

| exp_id | gpu | tasks_done | per_task_results | process_alive | elapsed | ETA |
|--------|-----|------------|------------------|---------------|---------|-----|
| eval-reconvla-object | 0 | 1/10 | T1: **0%** | 是 (PID 9659) | 2h41m | ~24h |
| eval-acr-object-v4-perdof | 1 | 1/10 | T1: **0%** | 是 (PID 11116) | 2h39m | ~24h |
| eval-acr-object-v4-obs-only | 2 | 1/10 | T1: **0%** | 是 (PID 13806) | 2h25m | ~22h |
| eval-acr-object-v4-scalar | 3 | 1/10 | T1: **0%** | 是 (PID 14003) | 2h25m | ~22h |
| eval-vla-only-object-k1 | 4 | **0/10** | 进行中(T1 r5/10, 0/5) | 是 (PID 39397) | **7m** | 刚启动 |
| eval-vla-mean-object | 5 | 1/10 | T1: **0%** | 是 (PID 18808) | 2h18m | ~21h |

所有 object eval 都在 task 1 (alphabet_soup) 得到 **0%**，当前正在跑 task 2 (cream_cheese)。`eval-vla-only-object-k1` 刚启动 7 分钟。

日志路径修正：reconvla → `/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log`，perdof → `/root/acr-vla-conformal-refinement/logs/eval_object_perdof.log`

---

## Server 2: bjb2-28827 — Magnitude Sweep（6 个实验）

**注意：这些实验实际跑的是 spatial benchmark，不是 object。**

| exp_id | gpu | norm | mode | tasks_done | T1 (bowl_between) | T2 (bowl_next_to) | avg | process_alive | elapsed | ETA |
|--------|-----|------|------|------------|-------|-------|-----|---------------|---------|-----|
| eval-mag-perdof-norm003 | 0 | 0.03 | acr_vla | 2/10 | 60% | 100% | **80%** | 是 | 2h02m | ~8h |
| eval-mag-perdof-norm005 | 1 | 0.05 | acr_vla | 2/10 | 50% | 100% | **75%** | 是 | 2h02m | ~8h |
| eval-mag-perdof-norm02 | 2 | 0.2 | acr_vla | 2/10 | 60% | 90% | **75%** | 是 | 2h02m | ~8h |
| eval-mag-perdof-norm03 | 3 | 0.3 | acr_vla | 2/10 | 70% | 50% | **60%** | 是 | 2h02m | ~8h |
| eval-mag-obsonly-norm005 | 4 | 0.05 | crm_obs_only | 2/10 | 80% | 90% | **85%** | 是 | 2h02m | ~8h |
| eval-mag-obsonly-norm02 | 5 | 0.2 | crm_obs_only | 2/10 | 90% | 100% | **95%** | 是 | 2h02m | ~8h |

---

## Magnitude Sweep 早期趋势（前 2 tasks, spatial）

| 方法 | norm=0.03 | norm=0.05 | norm=0.2 | norm=0.3 |
|------|-----------|-----------|----------|----------|
| **perdof (acr_vla)** | 80% | 75% | 75% | 60% |
| **obs_only (crm_obs_only)** | — | 85% | **95%** | — |

**关键发现：**
- **obs_only norm=0.2 当前 95% 均值，远超 argmin baseline 42.9%**（但仅 2/10 tasks，spatial benchmark，后续 tasks 可能更难）
- perdof 在小 norm (0.03) 时表现最好 (80%)，norm 增大到 0.3 反而下降到 60%，task 2 只有 50%
- obs_only 整体优于 perdof，且 norm=0.2 > norm=0.05
- **norm=0.3 对 perdof 有害** — task 2 (bowl_next_to) 从其他 norm 的 90-100% 骤降到 50%

⚠️ 只有 2/10 tasks 完成，且 spatial 前两个 task 通常较简单，完整结论需等全部跑完（~8h 后）。

---
