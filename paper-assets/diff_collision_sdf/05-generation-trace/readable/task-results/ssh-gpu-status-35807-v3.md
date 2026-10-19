# ssh gpu status 35807 v3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_35807_v3_20260520T111534_result.json`
- **Structured JSON:** [`e769d169ae62cc046c37.json`](../../sessions/e7/e769d169ae62cc046c37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部存活，无异常。

| GPU | 实验 | PID | Step/30000 | Loss | VRAM | GPU Util | 状态 |
|-----|------|-----|------------|------|------|----------|------|
| 0 | baseline_spatial_bowl_s0 | 100319 | 12496 (42%) | 0.0109 | 37358/97887 MiB | 100% | 正常 |
| 1 | baseline_spatial_bowl_s1 | 94453 | 12790 (43%) | 0.0102 | 37358/97887 MiB | 100% | 正常 |
| 2 | baseline_object_pudding_s0 | 95429 | 12999 (43%) | 0.0054 | 37358/97887 MiB | 18% | 正常 |
| 3 | a1_sdf_spatial_bowl_s0 | 185994 | 8858 (30%) | 0.2873 | 13376/97887 MiB | 0% | 正常* |

**磁盘：**
- `/root/autodl-tmp`: 267G/350G (77%), 84G 可用
- `/`: 15G/30G (50%), 16G 可用

**备注：**
- GPU 3 (a1) 瞬时 util=0%、VRAM 仅 13.4G，但日志持续推进到 step 8858，进程存活。可能是采样间隙或 I/O 阶段。
- a1 从 step 6000 恢复续训，loss ~0.28 显著高于同期 baseline（~0.01）——但这是 SDF 实验，loss scale 不同，属预期。
- 3 个 baseline 进度一致（42-43%），速度 ~3.4-3.7s/it。

---
