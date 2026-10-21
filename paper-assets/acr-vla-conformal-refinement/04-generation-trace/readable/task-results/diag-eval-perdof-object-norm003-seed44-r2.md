# diag eval perdof object norm003 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-perdof-object-norm003-seed44-r2_20260518T191703_result.json`
- **Structured JSON:** [`5b071a889a0440a28e76.json`](../../sessions/5b/5b071a889a0440a28e76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```
失败原因：进程被调度系统 SIGTERM 杀掉（EXIT_CODE=143），非脚本/环境/CUDA错误。r2 运行 ~5h42m 后，在完成 4/10 个任务时被终止。同一服务器上多个 eval 实验在 03:13 被批量杀掉，03:14 新实验 tmux session 立即创建。
根因分类：调度抢占（agent-ml 调度系统为新实验腾 GPU slot）
建议修复：
  1. 在 bjb1-32546（当前有空闲 slot）上重新提交，避免 bjb1-18228 的 GPU 争抢
  2. 或拆分为更小任务（如每次只跑 5 个 task），减少被抢占的风险
  3. 如必须在 bjb1-18228 上跑，需确保 GPU slot 不会被新调度覆盖
可否立即重试：是，推荐在 bjb1-32546 上重试，命令：
  cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=<空闲GPU> /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json
```

---
