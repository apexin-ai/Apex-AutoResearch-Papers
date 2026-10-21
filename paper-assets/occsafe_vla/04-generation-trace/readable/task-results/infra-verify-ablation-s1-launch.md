# infra verify ablation s1 launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_ablation_s1_launch_20260521T042326_result.json`
- **Structured JSON:** [`1a1049fc246dbb43da3d.json`](../../sessions/1a/1a1049fc246dbb43da3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全部 4 卡状态

| GPU | Util | Memory |
|-----|------|--------|
| 0 | 0%* | 62203 / 97887 MiB |
| 1 | 0%* | 62209 / 97887 MiB |
| 2 | 0%* | 62779 / 97887 MiB |
| 3 | 0%* | 62203 / 97887 MiB |

*util 0% 是瞬时采样，4 卡均已分配 ~62GB 显存，log 显示训练在正常推进。

## ablation_occ_detach_s1
- **PID**: wrapper 485753, python worker 可见于 cmdline
- **CUDA**: CUDA_VISIBLE_DEVICES=2 ✓
- **参数验证**: OK — `--occ_detach true --seed 43 --num_images_in_input 2 --use_proprio True`
- **进度**: step 26/50005
- **速度**: 稳态 ~1.08 it/s（最后两步偶发慢至 4-6 s/it，可能是 checkpoint/数据加载抖动）

## ablation_random_occ_s1
- **PID**: wrapper 485903, python worker 486047
- **CUDA**: CUDA_VISIBLE_DEVICES=3 ✓
- **参数验证**: OK — `--random_occ True --occ_detach false --seed 43 --num_images_in_input 2 --use_proprio True`
- **进度**: step 24/50005
- **速度**: 稳态 ~1.07-1.08 it/s（同样末尾有短暂抖动）

两个 s1 实验均正常启动，参数正确，训练速度符合预期。

---
