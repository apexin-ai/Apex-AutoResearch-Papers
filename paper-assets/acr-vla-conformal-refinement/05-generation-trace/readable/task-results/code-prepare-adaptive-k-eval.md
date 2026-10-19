# code prepare adaptive k eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-adaptive-k-eval_20260523T004914_result.json`
- **Structured JSON:** [`d444dfba8db5f05740d3.json`](../../sessions/d4/d444dfba8db5f05740d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**任务 1-2 确认结果**:
- `adaptive_conformal_crm` mode 完整实现，`select_action_conformal_crm()` 在 lines 447-508
- `conformal_threshold` 默认 0.074855 (P50)，函数 hardcode K=2，与 `--K` 参数无关
- CRM 用 obs_only (unc_dim=0)，max_correction_norm 自动设为 0.2

**注意**: 用户指定的 checkpoint 路径 `crm_smolvla_3suite_v1/crm_best.pt` 在两台服务器上均不存在。代码默认使用 `crm_v3_norm/obs_only/crm_best.pt`，该文件在两台服务器上都存在。

**产出**:
- `artifacts/deploy_adaptive_k_eval.sh` — 部署脚本，接受 GPU 列表参数，为 3 suite × 3 seed 创建 tmux session
- `artifacts/adaptive_k_eval_prep.md` — 完整参数列表、threshold 策略、命令模板、checkpoint 可用性

---
