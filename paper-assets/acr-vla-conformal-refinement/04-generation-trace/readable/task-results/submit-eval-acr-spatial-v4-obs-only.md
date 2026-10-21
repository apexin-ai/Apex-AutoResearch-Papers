# submit eval acr spatial v4 obs only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-acr-spatial-v4-obs-only_20260514T221706_result.json`
- **Structured JSON:** [`b38cfefff941a5463709.json`](../../sessions/b3/b38cfefff941a5463709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已在运行，registry 已更新为 RUNNING。

**总结：**

- `eval-acr-spatial-v4-obs-only-r2` 已经在 bjb1-18228 cuda:0 上运行（PID 268361，tmux: `eval-acr-spatial-v4-obs-only-r2`）
- 完整命令：`python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1`
- **input_mode 处理**：evaluate.py 原生支持 `--mode crm_obs_only`，设置 `unc_dim=0` 且 `uf_input=None`，CRM 只接收 obs features，不需要额外的 `--input_mode` 参数
- **perdof eval 确认**：`eval-acr-spatial-v4-small` 用 `--mode acr_vla`（= `crm_perdof`），默认 `unc_dim=40`，不需要显式 `--input_mode perdof`
- CRM 已加载确认：327,198 params，max_correction_norm=0.1，10 tasks loaded
- 预计运行 ~9 小时，日志：`/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only-r2.log`

---
