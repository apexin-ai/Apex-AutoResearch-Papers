# check server status bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-bjb1_20260517T175712_result.json`
- **Structured JSON:** [`9fd1f00a24dd79d8b73e.json`](../../sessions/9f/9fd1f00a24dd79d8b73e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546
- GPU 状态:
  - GPU 0: 3805/24564 MiB, 20% util — obs_only norm005 seed43 r2 (~45%, task 5/10)
  - GPU 1: 3343/24564 MiB, 22% util — perdof norm01 seed47 r2 (~65%, task 6/10)
  - GPU 2: 3343/24564 MiB, 21% util — obs_only norm03 seed46 (~55%, task 5-6/10)
  - GPU 3: 3343/24564 MiB, 21% util — obs_only default seed46 (~55%, task 6/10)
  - GPU 4: 2411/24564 MiB, 21% util — perdof norm01 seed46 (~78%, task 8/10)
  - GPU 5: 3805/24564 MiB, 21% util — perdof default seed46 (~55%, task 5/10)
- **K=1 ACCG eval seed42: 完成, overall_success_rate=11%** (11/100)
  - salad_dressing 20%, bbq_sauce 20%, tomato_sauce 10%, butter 10%, milk 10%, chocolate_pudding 20%, orange_juice 20%
- **K=1 ACCG eval seed43: 完成, overall_success_rate=12%** (12/100)
  - salad_dressing 20%, bbq_sauce 20%, ketchup 10%, tomato_sauce 20%, butter 10%, milk 10%, chocolate_pudding 20%, orange_juice 10%
- **K=1 ACCG eval seed44: 完成, overall_success_rate=7%** (7/100)
  - salad_dressing 10%, bbq_sauce 10%, ketchup 10%, tomato_sauce 10%, chocolate_pudding 20%, orange_juice 10%
- 其他实验: obs_only_norm005_seed43, obs_only_norm03_seed46, obs_only_default_seed46, perdof_norm01_seed46, perdof_norm01_seed47, perdof_default_seed46 (全部进行中)
- 空闲 GPU: 无

## bjb1-18228
- GPU 状态:
  - GPU 0: 4269/24564 MiB, 22% util — perdof norm02 seed45 (~30%, task 3-4/10)
  - GPU 1: 4269/24564 MiB, 22% util — obs_only norm005 seed43 r3 (~25%, task 3/10)
  - GPU 2: 3342/24564 MiB, 22% util — obs_only norm02 K=5 seed42 (~55%, task 6/10)
  - GPU 3: 5201/24564 MiB, 22% util — obs_only norm02 K=20 seed42 (~15%, task 2/10)
- **OpenVLA eval: 完成, overall_success_rate=0.0% (0/100), exit_code=0**
  - 所有 10 个 task 均 0%，avg inference 178ms/step
- 其他实验: obs_only_norm005_seed43_r3, obs_only_norm02_k5_seed42, obs_only_norm02_k20_seed42, perdof_norm02_seed45 (全部进行中)
- 空闲 GPU: 无

---
