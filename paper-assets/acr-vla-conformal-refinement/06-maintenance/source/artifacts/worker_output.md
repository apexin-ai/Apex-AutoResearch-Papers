# 实验状态检查 (2026-05-21)

## 关键发现
1. 14 个 registry-RUNNING 实验中 **13 个已完成**，1 个已死（OpenVLA timeout + 重跑 ImportError）
2. **bjb1-32546 发现 π0.5 batch 正在运行**（6 个实验，未在 registry 中）— 但模型加载异常，前几个 task SR=0%
3. **bjb1-18228 发现额外 3 个 crm_obs_only 实验正在运行**（seed 55/76/77，未在 registry 中）
4. bjb2-28827 所有 GPU 已空闲（reconcile 一致）

## 已完成（需更新 registry）

| exp_id | SR | 来源 | server |
|--------|-----|------|--------|
| eval-argmin-object-seed48 | 15.0% (15/100) | logs/eval_argmin_object_seed48.json | bjb1-32546 |
| eval-obs-only-object-norm02-seed49 | 14.0% (14/100) | logs/eval_obs_only_object_norm02_seed49.json | bjb1-32546 |
| eval-random-selection-spatial-seed44 | 28.0% (28/100) | logs/eval_random_selection_spatial_seed44.json | bjb1-18228 |
| eval-random-selection-spatial-seed42 | 34.0% (34/100) | logs/eval_random_selection_spatial_seed42.json | bjb1-18228 |
| eval-perdof-object-norm02-seed45-r3 | 12.0% (12/100) | logs/eval_object_perdof_norm02_seed45_r3.json | bjb1-18228 |
| eval-adaptive-k-spatial-p90-seed42 | 31.0% (31/100) | logs/eval_adaptive_k_spatial_p90_seed42.json | bjb2-28827 |
| eval-adaptive-k-spatial-p25-seed44 | 32.0% (32/100) | logs/eval_adaptive_k_spatial_p25_seed44.json | bjb2-28827 |
| eval-adaptive-k-spatial-p75-seed44 | 33.0% (33/100) | logs/eval_adaptive_k_spatial_p75_seed44.json | bjb2-28827 |
| eval-obs-only-spatial-norm02-seed46-r2 | 33.0% (33/100) | logs/eval_spatial_obs_only_norm02_seed46_r2.json | bjb2-28827 |
| eval-vla-only-goal-seed44-r2 | 73.0% (73/100) | logs/eval_goal_vla_only_seed44_r2.json | bjb2-28827 |
| eval-argmin-object-k5-seed44-r2 | 11.0% (11/100) | logs/eval_object_argmin_k5_seed44_r2.json | bjb2-28827 |
| eval-perdof-object-norm02-seed48 | 7.0% (7/100) | logs/eval_object_perdof_norm02_seed48.json | bjb2-28827 |
| eval-obs-only-object-norm005-seed43 | 13.0% (13/100) | logs/eval_object_obs_only_norm005_seed43.json | bjb2-28827 |

注：bjb2-28827 上 adaptive-k 三个实验 EXIT_CODE=129（SIGHUP，可能终端断开）但 results 已落盘，可正常 harvest。

### Adaptive-K 额外统计（bjb2-28827）
- p90-seed42: fast_path=80.6%, avg_k=3.5, mean_l2=0.0907
- p25-seed44: fast_path=28.8%, avg_k=7.7, mean_l2=0.0896
- p75-seed44: fast_path=61.8%, avg_k=5.1, mean_l2=0.0920

## 仍在运行（非 registry 内，需人工确认是否合法）

| exp_id | 进度 | server | elapsed |
|--------|------|--------|---------|
| eval-pi05-vla-only-object-seed42 (PID 943185) | task 4/10 (bbq_sauce 5/20)，前 3 task SR=0/60 | bjb1-32546 | 1h32m |
| eval-pi05-vla-only-object-seed43 (PID 943552) | (未细查) | bjb1-32546 | 1h32m |
| eval-pi05-vla-only-object-seed44 (PID 943904) | (未细查) | bjb1-32546 | 1h31m |
| eval-pi05-vla-only-spatial-seed42 (PID 944269) | (未细查) | bjb1-32546 | 1h31m |
| eval-pi05-vla-only-spatial-seed43 (PID 945464) | (未细查) | bjb1-32546 | 1h29m |
| eval-pi05-vla-only-spatial-seed44 (PID 946617) | task 3/10 完成，前 3 task SR=0/60 | bjb1-32546 | 1h29m |
| eval-object-obs-only-norm02-seed55 (PID 735451) | crm_obs_only norm02 | bjb1-18228 | 8m44s |
| eval-object-obs-only-norm003-seed76 (PID 736646) | crm_obs_only norm003 | bjb1-18228 | 8m13s |
| eval-object-obs-only-norm003-seed77 (PID 738108) | crm_obs_only norm003 | bjb1-18228 | 7m42s |

## 已死（需重跑）

| exp_id | 原因 | server |
|--------|------|--------|
| eval-openvla-object-baseline-seed42 | EXIT_CODE=124 (timeout) at episode 400/600；r2 重跑因 `AutoModelForVision2Seq` ImportError 失败 | bjb2-28827 |

OpenVLA 重跑前必须修 transformers 版本：`/root/miniconda3/lib/python3.12/site-packages/transformers/` 当前 import `AutoModelForVision2Seq` 失败。

## π0.5 发现

**位置**：bjb1-32546，`/root/acr-vla-conformal-refinement/logs/eval-pi05-vla-only-{object,spatial}-seed{42,43,44}.log`

**部署详情**：今天约 16:25 启动，6 个进程同时跑（PID 943185, 943552, 943904, 944269, 945464, 946617，分别用 cuda:0-5），命令：
```
python -u src/evaluate.py --model pi05 --mode vla_only \
    --benchmark {object|spatial} --n_rollouts 20 --seed {42|43|44} \
    --K 10 --output_file logs/eval_pi05_vla_only_{bench}_seed{N}.json
```

**严重问题**：模型加载告警
```
[pi05] Fixed 437 vision tower keys
[pi05] Vision tower missing_keys (376): [
  'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight',
  'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias',
  'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight',
  'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight',
  'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.k_proj.weight', ...]
```
376 个 key missing（含 multi_modal_projector 和整个 language_model 的核心层），且：
- object-seed42 前 3 task 全 0/20（alphabet_soup, cream_cheese, salad_dressing）
- spatial-seed44 前 3 task 全 0/20（black_bowl 三种位置）

π0.5 checkpoint 加载逻辑有 bug，跑下去也是 0% SR。

**还没有 JSON 落盘**：`find /root/acr-vla-conformal-refinement/logs -name "eval_pi05*.json"` 空结果。

## 操作建议（优先级）

1. **立即 harvest**：13 个已完成实验的 JSON → registry update（reconcile 这些为 SUCCEEDED）
2. **π0.5 紧急 kill**：6 个进程跑废，先 kill 释放 GPU，查 checkpoint 加载（multi_modal_projector + language_model 权重映射），修好再重启
3. **OpenVLA baseline 重跑**：先修 transformers 依赖（升级或装兼容版本），再重启 seed42
4. **bjb1-18228 上 3 个额外 crm_obs_only 实验**（seed55/76/77）需人确认是否合法启动
