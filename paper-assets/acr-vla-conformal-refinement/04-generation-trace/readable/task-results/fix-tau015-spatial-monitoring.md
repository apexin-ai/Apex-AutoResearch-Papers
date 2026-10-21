# fix tau015 spatial monitoring

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tau015-spatial-monitoring_20260527T235348_result.json`
- **Structured JSON:** [`2bf8899800732ea9ab50.json`](../../sessions/2b/2bf8899800732ea9ab50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。汇总：

**实验 `smolvla-tau015-spatial-s42-fix`**
- **PID**: 20271
- **GPU**: cuda:4 (CUDA_VISIBLE_DEVICES=4), 占用 5136 MiB
- **tmux**: 在 tmux 中运行（server PID 660857, pane %25），无法通过 read-only 命令确定 session name，但进程在 pts/4 上
- **log_path**: `~/runs/acr-vla-conformal-refinement/smolvla-tau015-spatial-s42-fix.log`
- **命令**: `python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --benchmark spatial --K 2 --seed 42 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --max_correction_norm 0.2 --conformal_threshold 0.15 --output_file logs/eval_spatial_adaptive_conformal_crm_smolvla_k2_norm0.2_tau0.15_seed42.json`
- **进度**: 正在评估中，task 1 完成 20/20 (100%)，task 2 完成 18/20 (90%)，task 3 进行中 5/20

另注：旧的 `smolvla-tau015-spatial-s42` (PID 13505) 也在 PREPARING 状态，且其 command 有 bug（`--benchmark long` 而非 `--benchmark spatial`），应该是被 `-fix` 版替代了。

---
