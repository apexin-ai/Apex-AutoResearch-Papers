# check bjb1 32546 object status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-32546-object-status_20260515T044311_result.json`
- **Structured JSON:** [`0df5faa7a5cba98130ba.json`](../../sessions/0d/0df5faa7a5cba98130ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 remaining processes alive. Here's the full status:

## bjb1-32546 Object Eval Status (2026-05-15 ~12:40)

| GPU | exp_id | mode | tasks_done | current_task | SR so far | pid | alive |
|-----|--------|------|------------|--------------|-----------|-----|-------|
| cuda:0 | eval-reconvla-object | reconvla (K=10) | 1/10 | task 2 | 0% (0/10) | 9659 | YES |
| cuda:1 | eval-acr-object-v4-perdof | crm_perdof (K=10) | 1/10 | task 2 | 0% (0/10) | 11116 | YES |
| cuda:2 | eval-acr-object-v4-obs-only | crm_obs_only (K=10) | 1/10 | task 2 | 0% (0/10) | 13806 | YES |
| cuda:3 | eval-acr-object-v4-scalar | crm_scalar (K=10) | 1/10 | task 2 | 0% (0/10) | 14003 | YES |
| cuda:4 | eval-vla-only-object | vla_only (K=1) | **10/10** | — | **12% (12/100)** | — | **DONE** |
| cuda:5 | eval-vla-mean-object | vla_only mean (K=10) | 1/10 | task 2 | 0% (0/10) | 18808 | YES |

## eval-vla-only-object 诊断

- **不是 crash，是正常完成。** 进程跑完了全部 10 tasks × 10 rollouts 后正常退出。
- Overall SR: **12.0% (12/100)**
- Per-task breakdown:

| task | SR |
|------|----|
| alphabet_soup | 0% |
| cream_cheese | 10% |
| salad_dressing | 20% |
| bbq_sauce | 20% |
| ketchup | 0% |
| tomato_sauce | 10% |
| butter | 0% |
| milk | 10% |
| chocolate_pudding | 20% |
| orange_juice | 30% |

- JSON 结果已保存: `logs/eval_object_vla_only.json`
- **无需重启** — GPU 4 空闲可复用

其余 5 个实验均在 task 1/10 (alphabet_soup 完成, 全部 0%)，正在跑 task 2。K=10 比 K=1 慢约 10 倍，预计还需较长时间。

---
