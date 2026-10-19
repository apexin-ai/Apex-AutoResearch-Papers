# eval baseline object pudding gpu check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_object_pudding_gpu_check_20260521T181530_result.json`
- **Structured JSON:** [`657aaac047b353dcfe3e.json`](../../sessions/65/657aaac047b353dcfe3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### GPU VRAM 状态

| GPU | 已用 | 总计 | 空闲 |
|-----|------|------|------|
| cuda:0 | 23.3 GB | 95.6 GB | **71.6 GB** |
| cuda:1 | 23.3 GB | 95.6 GB | **71.6 GB** |
| cuda:2 | 23.3 GB | 95.6 GB | **71.6 GB** |
| cuda:3 | 23.3 GB | 95.6 GB | **71.6 GB** |

每张卡训练只占 ~23 GB，剩余 ~71 GB，远超 30 GB 阈值。**4 张卡均可同时跑 eval。**

### Baseline checkpoint

- 路径：`/root/autodl-tmp/checkpoints/baseline_object_pudding/baseline_object_pudding_seed0/best/`
- `model.safetensors`: 6.5 GB
- `optimizer.pt`: 11.7 GB
- 训练已完成（step 30000，有 best 目录）

VRAM 余量充足，可以直接在 westd-35807 任意一张卡上跑 baseline object_pudding eval，无需 scp 到其他服务器。

---
