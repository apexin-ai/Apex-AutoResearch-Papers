# ssh gpu status 45947 v3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_45947_v3_20260520T111539_result.json`
- **Structured JSON:** [`a883d9f87f83cae0801a.json`](../../sessions/a8/a883d9f87f83cae0801a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | PID | Step/30000 | Loss | Speed | VRAM | 状态 |
|-----|------|-----|-----------|------|-------|------|------|
| cuda:0 | a3_gradient_spatial_bowl_s0 | 71494 | 2924/30000 (9.7%) | 0.2606 | ~3.06 s/it | 16.9/97.9 GB | 运行中 (util 0%*) |
| cuda:1 | a3_gradient_object_pudding_s0 | 73165 | 5247/30000 (17.5%) | 0.0994 | ~4.20 s/it | 23.9/97.9 GB | 运行中 (util 100%) |

磁盘: 49G/250G (20%)

*GPU0 utilization 0% 是 nvidia-smi 采样瞬时值，进程在跑（step 在推进，已运行 ~3h09m），正常。

两个进程都远超预期 step（bowl 2924 > 1400+，pudding 5247 > 3800+），训练正常推进中。pudding 的 loss 已降到 ~0.09 区间，bowl 仍在 ~0.26 区间。

---
