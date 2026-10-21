# deploy cqa1 free gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-free-gpus_20260526T164122_result.json`
- **Structured JSON:** [`a8819dc92bd98018262a.json`](../../sessions/a8/a8819dc92bd98018262a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张空闲卡部署完毕，全部进入 RUNNING 状态。

| GPU | PID | exp_id | 模式 | seed | 显存 |
|-----|-----|--------|------|------|------|
| cuda:0 | 488507 | smolvla-adapt-tau015-object-s42-cqa1 | adaptive_conformal_crm K=2 τ=0.15 | 42 | 5896 MiB |
| cuda:1 | 489504 | smolvla-adapt-tau015-object-s43-cqa1 | adaptive_conformal_crm K=2 τ=0.15 | 43 | 5896 MiB |
| cuda:2 | 491094 | smolvla-adapt-tau015-object-s44-cqa1 | adaptive_conformal_crm K=2 τ=0.15 | 44 | 5896 MiB |
| cuda:3 | 492008 | smolvla-crm-norm005-k10-object-s44-cqa1 | crm_obs_only K=10 ε=0.05 (D149) | 44 | 5970 MiB |

cuda:4/5（10.7/10.1 GiB）保持原有 pi05-adaptive-long s43/s44 运行不受影响。

要点：
- 优先级 1 跳过：`eval_object_adaptive_pi05_seed44.json` 已存在且数据完整（SR=0.88, 200 rollouts），无 registry 条目但日志文件有效
- checkpoint 路径修正：`crm_smolvla_3suite_unified` → `crm_smolvla_3suite_v1`（v1 存在，unified 不存在；evaluate.py line 541 默认也是 v1）
- 部署优先级 2 时同步加 s43/s44 完整 3 seed sweep，填满 4 张卡
- 所有 4 个进程 SmolVLA + CRM v1 加载成功，已进入 rollout 阶段

---
