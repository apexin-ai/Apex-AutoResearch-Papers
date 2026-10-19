# deploy fill idle gpus and collect

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill-idle-gpus-and-collect_20260517T210101_result.json`
- **Structured JSON:** [`64af6c4f7cab77c25a48.json`](../../sessions/64/64af6c4f7cab77c25a48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## Multi-scale K=1 CRM (crm_k1_accg) 结果

```
seed=42 (bjb2-28827): overall SR = 12/100 (12%)
  alphabet_soup:      0/10
  cream_cheese:       0/10
  salad_dressing:     1/10
  bbq_sauce:          2/10
  ketchup:            0/10
  tomato_sauce:       3/10
  butter:             1/10
  milk:               0/10
  chocolate_pudding:  3/10
  orange_juice:       2/10

seed=43 (bjb1-32546): overall SR = 9/100 (9%)
  alphabet_soup:      0/10
  cream_cheese:       0/10
  salad_dressing:     1/10
  bbq_sauce:          2/10
  ketchup:            0/10
  tomato_sauce:       2/10
  butter:             0/10
  milk:               0/10
  chocolate_pudding:  2/10
  orange_juice:       2/10

seed=44 (bjb1-32546): overall SR = 10/100 (10%) [已在 registry]
  alphabet_soup:      0/10
  cream_cheese:       0/10
  salad_dressing:     2/10
  bbq_sauce:          1/10
  ketchup:            0/10
  tomato_sauce:       1/10
  butter:             0/10
  milk:               0/10
  chocolate_pudding:  4/10
  orange_juice:       2/10
```

**3-seed 平均: 10.3%** (12% / 9% / 10%)

---

## OpenVLA eval 状态 (bjb1-18228)

`eval-openvla-object-vla-only-seed42-v2` 在 cuda:1 运行中，进度 **5/10 tasks (50%)**，已加载模型并开始评估。flash-attn 同时在编译中。

---

## 新部署实验

| exp_id | server | GPU | 状态 |
|--------|--------|-----|------|
| eval-perdof-object-norm02-seed45-r3 | bjb1-18228 | cuda:3 | RUNNING (PID 749540) |
| eval-obs-only-object-norm005-seed43 | bjb2-28827 | cuda:0 | RUNNING (PID 476529) |

---

## 各服务器 GPU 占用

- **bjb1-18228**: cuda:0/1/2 占用 (OpenVLA + flash-attn 编译), cuda:3 刚部署 perdof seed45
- **bjb2-28827**: cuda:0 刚部署 obs_only norm005 seed43, cuda:1-5 被 perdof/obs_only magnitude sweep 占满
- **bjb1-32546**: 6 GPU 全部被 magnitude sweep 和 default norm 实验占用，无空闲

---
