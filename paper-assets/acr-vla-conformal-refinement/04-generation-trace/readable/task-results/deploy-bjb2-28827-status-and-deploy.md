# deploy bjb2 28827 status and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-status-and-deploy_20260528T063821_result.json`
- **Structured JSON:** [`382a086911b6a3bdc180.json`](../../sessions/38/382a086911b6a3bdc180.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 状态汇总

**6 张卡全部占用，无空闲 GPU。**

| GPU | 显存 | tmux session | 实验内容 | 进度 |
|-----|------|-------------|---------|------|
| cuda:0 | 2507 MiB | eval-k2-tau045-spatial-s42-bjb2 | adaptive_conformal_crm, τ=0.45, spatial, s42 | **7/10 tasks** |
| cuda:1 | 2507 MiB | eval-supp-adapt-tau025-spatial-s46 | adaptive_conformal_crm, τ=0.25, spatial, s46 | **7/10 tasks** |
| cuda:2 | 4662 MiB | eval-supp-long-vla-only-s42 | vla_only, long, s42 | **3/10 tasks** |
| cuda:3 | 4662 MiB | eval-supp-long-vla-only-s44 | vla_only, long, s44 | **3/10 tasks** |
| cuda:4 | 1977 MiB | smolvla-tau025-spatial-s42 | adaptive_conformal_crm, τ=0.25, spatial, s42 | **8/10 tasks** |
| cuda:5 | 1967 MiB | smolvla-tau020-spatial-s42 | adaptive_conformal_crm, τ=0.20, spatial, s42 | **8/10 tasks** |

**P1 候选已在跑 2/3：**
- `smolvla-tau045-spatial-s42` → cuda:0 ✅
- `eval-supp-adapt-tau025-spatial-s46` → cuda:1 ✅
- `eval-supp-long-adapt-tau025-s47-r2` → 未部署 ❌

**评估脚本和参数格式确认：**
- 脚本：`src/evaluate.py`
- benchmark 参数值：`spatial` / `long`（不是 `libero_*`）
- CRM checkpoint 存在：`/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`（1.3MB）
- **注意**：当前运行的实验全部用 `--max_correction_norm 0.2`，不是任务模板中的 `0.05`

**预计释放时间（实验已跑约 2h）：**
- cuda:4, cuda:5 最快释放（~30 min，spatial 80% 完成）
- cuda:0, cuda:1 次之（~45-60 min，spatial 70% 完成）
- cuda:2, cuda:3 最慢（~3h+，long 30% 完成）

**部署计划**：等 cuda:4/5 释放后优先部署 P1 剩余的 `eval-supp-long-adapt-tau025-s47-r2` + P2 中的高优候选。需要确认：`--max_correction_norm` 用 0.2 还是 0.05？

---
