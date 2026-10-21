# ssh westd35807 alive check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd35807_alive_check_20260520T030426_result.json`
- **Structured JSON:** [`778eedb4b3cc491c5993.json`](../../sessions/77/778eedb4b3cc491c5993.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活。

| GPU | 任务 | PID | 运行时间 | Step | Loss | VRAM | GPU Util |
|-----|------|-----|----------|------|------|------|----------|
| 0 | baseline_spatial_bowl_seed0 | 95429 | 4h41m | **4390**/30000 (15%) | 0.024 | 37.4/97.9 GB | 99% |
| 1 | baseline_spatial_bowl_seed1 | 94453 | 4h41m | **4645**/30000 (15%) | 0.020 | 37.4/97.9 GB | 0%* |
| 2 | baseline_object_pudding_seed0 | 100319 | 4h29m | **2685**/30000 (9%) | 0.243 | 37.4/97.9 GB | 100% |
| 3 | **A1** sdf_spatial_bowl_s0 | 123362 | 2h38m | **2686**/30000 (9%) | 0.243 | **13.4**/97.9 GB | 0%* |

\* GPU util 0% 是 nvidia-smi 瞬时采样，PID 存活且 CPU 占用 65-128%，训练正常推进。

**A1 (cuda:3) 尚未进入 Phase 2** — step 2686 < 5000，VRAM 13.4GB < 35GB。按当前速度（~3.5s/step），预计还需 ~2.3h 到 step 5000。

---
