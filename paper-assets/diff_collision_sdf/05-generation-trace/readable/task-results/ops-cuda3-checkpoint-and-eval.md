# ops cuda3 checkpoint and eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda3_checkpoint_and_eval_20260525T140252_result.json`
- **Structured JSON:** [`8db84a1694c34242ffcf.json`](../../sessions/8d/8db84a1694c34242ffcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇总**

- **优先级 C**：seed0_l005 和 seed0_l01 均只有 `30000/`，无中间 checkpoint。启动 s0_l01 30k 重跑。
- **PID**: 349448
- **GPU 占用**：
  | GPU | 显存占用 | 利用率 |
  |-----|---------|--------|
  | 0 | 27045 MiB | 100% (spatial_bowl 训练) |
  | 1 | 8365 MiB | 0% (eval v3) |
  | 2 | 9014 MiB | 15% (eval v3) |
  | 3 | 3835 MiB | 4% (模型加载中) |

- **日志确认**：模型加载正常，LoRA 注入完成（PaliGemma rank=16, Expert rank=32），checkpoint 和 norm stats 加载成功。cuda:3 显存 3.8GB 表明模型刚加载，后续推理时会继续上升。

---
