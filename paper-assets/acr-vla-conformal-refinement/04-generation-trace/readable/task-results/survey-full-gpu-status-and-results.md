# survey full gpu status and results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_survey_full-gpu-status-and-results_20260517T220756_result.json`
- **Structured JSON:** [`e72d78ee19e17af6cf17.json`](../../sessions/e7/e72d78ee19e17af6cf17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：OpenVLA v2 正在跑且 SR=68.9%（接近完成）。汇总所有结果：

---

## 服务器状态表

```
bjb2-28827: GPU0=obs_only_norm005_seed43/running/5664MiB | GPU1=obs_only_norm01_seed47/running/4736MiB | GPU2=perdof_norm02_seed47/running/3342MiB | GPU3=obs_only_norm01_seed46/running/4735MiB | GPU4=perdof_norm02_seed46/running/2411MiB | GPU5=perdof_norm02_seed43_r3/running/4735MiB
bjb1-32546: GPU0=obs_only_norm005_seed43_r2/running/2411MiB | GPU1=perdof_norm01_seed47_r2/running/1943MiB | GPU2=obs_only_norm03_seed46/running/1942MiB | GPU3=obs_only_default_seed46/running/1942MiB | GPU4=perdof_norm02_seed43_bjb1/running/5665MiB | GPU5=perdof_default_seed46/running/2411MiB
bjb1-18228: GPU0=obs_only_norm02_K5_seed42/running/3804MiB | GPU1=OpenVLA_v2_seed42/~90%done/15819MiB | GPU2=obs_only_norm02_K20_seed42/running/5200MiB | GPU3=perdof_norm02_seed45_r3/running/5664MiB
bjb2-40593: GPU0=random_selection_seed42/~40%done/3732MiB
```

**注意**: bjb2-28827 GPU0 还同时跑了 CRM K=1 训练 (tmux session `train-crm-k1-v2`)。

---

## 已完成实验结果

### OpenVLA eval (第一次, bjb1-18228) — 失败
```
eval_openvla_object_vla_only_seed42: overall SR = 0% (0/100)
  所有 10 个 task 全部 0/10
```
**OpenVLA v2 正在进行中**: 当前累计 SR = 68.9% (62 successes)，约完成 90%，预计 ~1h 内完成。

### CRM K=1 ACCG (multiscale) 系列 — 新完成
```
eval_k1_crm_multiscale_object_seed42 (bjb2-28827): overall SR = 12% (12/100)
  salad_dressing: 1/10, bbq_sauce: 2/10, tomato_sauce: 3/10, butter: 1/10, choc_pudding: 3/10, orange_juice: 2/10

eval_k1_crm_multiscale_object_seed43 (bjb1-32546): overall SR = 9% (9/100)
  salad_dressing: 1/10, bbq_sauce: 2/10, tomato_sauce: 2/10, choc_pudding: 2/10, orange_juice: 2/10

eval_k1_crm_multiscale_object_seed44 (bjb1-32546): overall SR = 10% (10/100)
  salad_dressing: 2/10, bbq_sauce: 1/10, tomato_sauce: 1/10, choc_pudding: 4/10, orange_juice: 2/10

eval_k1_crm_multiscale_object_seed43_bjb1-18228: overall SR = 9% (9/100)
  salad_dressing: 1/10, bbq_sauce: 2/10, tomato_sauce: 2/10, choc_pudding: 2/10, orange_juice: 2/10

eval_k1_crm_multiscale_object_seed44_bjb1-18228: overall SR = 10% (10/100)
  salad_dressing: 2/10, bbq_sauce: 1/10, tomato_sauce: 1/10, choc_pudding: 4/10, orange_juice: 2/10
```

### CRM K=1 ACCG 系列 (bjb1-32546)
```
eval_k1_crm_accg_object_seed42: overall SR = 11% (11/100)
  salad_dressing: 2/10, bbq_sauce: 2/10, tomato_sauce: 1/10, butter: 1/10, milk: 1/10, choc_pudding: 2/10, orange_juice: 2/10

eval_k1_crm_accg_object_seed43: overall SR = 7% (7/100)
  salad_dressing: 1/10, bbq_sauce: 1/10, ketchup: 1/10, tomato_sauce: 1/10, choc_pudding: 2/10, orange_juice: 1/10

eval_k1_crm_accg_object_seed44: overall SR = 12% (12/100)
  salad_dressing: 2/10, bbq_sauce: 2/10, ketchup: 1/10, tomato_sauce: 2/10, butter: 1/10, milk: 1/10, choc_pudding: 2/10, orange_juice: 1/10
```

### PerDoF norm=0.2 追加种子 (bjb2-28827)
```
eval_object_perdof_norm02_seed44: overall SR = 10% (10/100)
  salad_dressing: 2/10, bbq_sauce: 1/10, tomato_sauce: 1/10, choc_pudding: 3/10, orange_juice: 3/10

eval_object_perdof_norm02_seed45: overall SR = 9% (9/100, n=200)
  salad_dressing: 3/20, bbq_sauce: 2/20, tomato_sauce: 1/20, butter: 1/20, milk: 2/20, choc_pudding: 6/20, orange_juice: 3/20
```

### PerDoF norm=0.1 seed46 (bjb1-32546, 刚完成)
```
eval_object_perdof_norm01_seed46: overall SR = 10% (10/100)
  salad_dressing: 1/10, bbq_sauce: 3/10, milk: 1/10, choc_pudding: 2/10, orange_juice: 3/10
```

### Obs-only default (无 norm cap) seed45 (bjb2-28827)
```
eval_object_obs_only_default_seed45: overall SR = 12% (12/100, n=200)
  cream_cheese: 2/20, salad_dressing: 2/20, bbq_sauce: 5/20, ketchup: 1/20, tomato_sauce: 2/20, butter: 1/20, milk: 4/20, choc_pudding: 4/20, orange_juice: 3/20
```

### Scalar seed45 (bjb2-28827)
```
eval_object_scalar_seed45: overall SR = 9% (9/100, n=200)
  cream_cheese: 2/20, salad_dressing: 1/20, bbq_sauce: 3/20, ketchup: 1/20, tomato_sauce: 1/20, butter: 1/20, milk: 1/20, choc_pudding: 5/20, orange_juice: 3/20
```

---

## Random Selection 进度 (bjb2-40593)
当前在 task 4/10 (bbq_sauce)，已完成: salad_dressing 1/10, bbq_sauce 4/10。约 40% 完成。

---

## 空闲 GPU 列表
**无空闲 GPU** — 所有 17 个 GPU 全部在使用中。

---

## 关键提醒
1. **OpenVLA v2 即将完成**（68.9% SR, ~90% done）— 约 1 小时内出结果，远好于第一次的 0%
2. K=1 ACCG 系列在 seed42/43/44 上一致给出 7-12% SR，与 K=10 方法差距明显
3. bjb2-28827 GPU0 上 CRM K=1 训练 和 eval 在同一 GPU，需确认训练是否已结束

---
