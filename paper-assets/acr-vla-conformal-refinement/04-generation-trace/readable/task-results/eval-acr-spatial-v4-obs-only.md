# eval acr spatial v4 obs only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acr-spatial-v4-obs-only_20260514T220927_result.json`
- **Structured JSON:** [`883808f28551669ebdb4.json`](../../sessions/88/883808f28551669ebdb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **清理 cuda:0**: 杀掉了残留 vla_only baseline eval (PID 143112)，无 tmux sessions 需清理
2. **Checkpoint 路径修正**: 任务给的路径 `crm_v3_norm/obs_only/` 不存在，实际路径是 `/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt`
3. **`max_correction_norm` 注意**: evaluate.py 没有此 CLI 参数，CRM 构造函数默认值 1.42 会被使用（非任务中说的 0.1）。该值是 Python 属性不在 state_dict 中
4. **eval 已启动**: tmux session `eval-acr-spatial-v4-obs-only`，PID 199257，cuda:0 占用 4949 MiB，CRM 327K params 已加载，LIBERO spatial 10 tasks x 10 rollouts
5. **Registry 已更新**: status=RUNNING，spec 已记录

---
