# ssh check duplicates and nrollouts bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-duplicates-and-nrollouts-bjb2-28827_20260517T103200_result.json`
- **Structured JSON:** [`6f2612efb473da76dd52.json`](../../sessions/6f/6f2612efb473da76dd52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

K 默认值是 10，所以 bjb2 PID 365893 虽然没显式写 --K，实际等效于 K=10。

```
=== 重复实验对比 ===

--- seed 47 ---
bjb2-28827 PID 363223:
  python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
    --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json

bjb1-18228 PID 588037:
  python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
    --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json

差异项：完全一致（连 output_file 都相同）

--- seed 46 ---
bjb2-28827 PID 365893:
  python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 46 \
    --max_correction_norm 0.1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
    --n_rollouts 10 --output_file results/eval_crm_obs_only_object_norm01_seed46.json

bjb1-18228 PID 587763:
  python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
    --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json

差异项：
  - output_file 不同（bjb2: results/..., bjb1: logs/...）
  - bjb2 未显式指定 --K，但默认值=10，与 bjb1 的 --K 10 等效
  - 其余参数（mode, benchmark, seed, n_rollouts, crm_checkpoint, max_correction_norm）完全一致

结论：是，两组都是重复实验。seed47 完全一致；seed46 实质等效（仅 output_file 路径不同）。

=== n_rollouts 确认 ===

PID 224623 (scalar seed45):       无 --n_rollouts 参数 → 使用默认值 20
PID 222824 (perdof norm02 seed45): 无 --n_rollouts 参数 → 使用默认值 20
PID 242264 (obs_only default seed45): 无 --n_rollouts 参数 → 使用默认值 20
  （此进程也无 --max_correction_norm，使用代码默认值）

代码默认值：--n_rollouts default=20（src/evaluate.py 第 61 行）

三个实验确认都在跑 n_rollouts=20。
```

---
