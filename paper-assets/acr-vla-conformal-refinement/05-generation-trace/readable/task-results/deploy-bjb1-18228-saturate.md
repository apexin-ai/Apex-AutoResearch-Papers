# deploy bjb1 18228 saturate

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-saturate_20260526T155921_result.json`
- **Structured JSON:** [`b16b0f92e6296346b03a.json`](../../sessions/b1/b16b0f92e6296346b03a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部在跑，bjb1-18228 满载。

## 部署汇报

| GPU | exp_id | mode | 参数 | PID | tmux | log |
|-----|--------|------|------|-----|------|-----|
| 0 | E_smolvla_adaptive_tau035_spatial_s42 | adaptive_conformal_crm | τ=0.35, K=2, norm=0.2, spatial s42 | 422173 | adapt_tau035_s42 | eval_spatial_adaptive_tau035_k2_s42.log |
| 1 | E_smolvla_adaptive_tau015_spatial_s42 | adaptive_conformal_crm | τ=0.15, K=2, norm=0.2, spatial s42 | 422441 | adapt_tau015_s42 | eval_spatial_adaptive_tau015_k2_s42.log |
| 2 | E_smolvla_adaptive_tau045_spatial_s42 | adaptive_conformal_crm | τ=0.45, K=2, norm=0.2, spatial s42 | 422713 | adapt_tau045_s42 | eval_spatial_adaptive_tau045_k2_s42.log |
| 3 | E_smolvla_crm_norm005_spatial_s42_d149 | crm_obs_only | K=10, norm=0.05, spatial s42 | 429223 | smolvla_crm_norm005_spatial_s42 | eval_spatial_crm_norm005_s42_d149.log |

**GPU 显存**: 6211/6211/6211/3205 MiB（全部 4×4090 在跑）  
**模型**: smolvla + CRM checkpoint `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`  
**预计完成**: ~1.7h/实验  
**注意事项**: 
- 优先级 3（K2mean s42 goal）已有结果 (`eval_goal_k2mean_pi05_seed42.json`)，跳过
- GPU 3 首次提交因任务模板缺 `--crm_checkpoint` 参数失败，已修复重启；已沉淀到 memory (`evaluate_crm_checkpoint_arg.md`)
- 4 个实验已在 registry 标记 RUNNING

---
