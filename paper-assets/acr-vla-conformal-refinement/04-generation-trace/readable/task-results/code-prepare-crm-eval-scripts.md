# code prepare crm eval scripts

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-crm-eval-scripts_20260522T184705_result.json`
- **Structured JSON:** [`d68958c094c734b0e771.json`](../../sessions/d6/d68958c094c734b0e771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署脚本已写入，memory.md 已更新。

**总结：**

| 项目 | 确认结果 |
|------|---------|
| CRM checkpoint | `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` (1.3MB, epoch15, bjb2-28827) |
| CRM 架构 | obs_only (unc_dim=0, obs_dim=960) — 文件大小验证匹配 |
| 正确 eval mode | **`crm_obs_only`**，不是 `acr_vla`（后者期望 unc_dim=40 会 crash） |
| Precompute cache | eval 不需要（只训练用），bjb1-32546 不需要传 cache |
| 需要 scp | 仅 `crm_best.pt` (1.3MB) → bjb1-32546 |
| GPU 可用 | bjb2-28827 cuda:1-5 (5), bjb1-32546 cuda:0,1,2,4,5 (5), 共 10 张，用 9 + 1 spare |
| 部署方式 | 9 GPU 各跑 ACR→VLA chained pair，共 18 evals，预计 2-4h wall time |

脚本路径: `artifacts/deploy_smolvla_crm_eval.sh`，用法:
- `bash deploy_smolvla_crm_eval.sh prereq` — 查看 checkpoint 拷贝指令
- `bash deploy_smolvla_crm_eval.sh all` — 一键部署全部 18 evals
- `bash deploy_smolvla_crm_eval.sh status` — 检查 tmux 状态
- `bash deploy_smolvla_crm_eval.sh harvest` — 收割结果

---
