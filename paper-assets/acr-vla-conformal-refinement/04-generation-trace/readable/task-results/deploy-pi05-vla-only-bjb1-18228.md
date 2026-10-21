# deploy pi05 vla only bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-vla-only-bjb1-18228_20260525T042825_result.json`
- **Structured JSON:** [`aa4519d8d307c75261f7.json`](../../sessions/aa/aa4519d8d307c75261f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**已提交**:
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-pi05-vla-only-spatial-s42-paired | cuda:1 | 446358 | RUNNING |
| eval-pi05-vla-only-goal-s42-paired | cuda:2 | 446717 | RUNNING |

**命令**: `CUDA_VISIBLE_DEVICES={1,2} python -u src/evaluate.py --model pi05 --mode vla_only --benchmark {spatial,goal} --seed 42 --n_rollouts 20 --output_file logs/eval_{spatial,goal}_vla_only_pi05_seed42_paired.json`

**验证**: 两进程已启动并进入 PI05 模型加载阶段（日志显示 "Loading PI05 from ..."），cuda:1/cuda:2 显存从 0 → 3 MiB，CUDA context 已初始化，等模型加载完会涨到 ~8-12GB。cuda:0 (CRM) 和 cuda:3 (precompute) 未触碰。

**注意**: 加了 `--output_file ..._paired.json` 后缀，避免覆盖此前 `eval_spatial_vla_only_pi05_seed42.json` 旧结果。

---
