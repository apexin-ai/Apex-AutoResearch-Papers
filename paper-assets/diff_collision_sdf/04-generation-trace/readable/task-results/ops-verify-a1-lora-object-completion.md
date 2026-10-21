# ops verify a1 lora object completion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_a1_lora_object_completion_20260522T135117_result.json`
- **Structured JSON:** [`b192de049f229d63ce30.json`](../../sessions/b1/b192de049f229d63ce30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练成功完成。**

| 项目 | 结果 |
|------|------|
| 最终步数 | **30000/30000** (100%) |
| 最终 loss | 0.0184 (step 30000) |
| best_loss | **0.01326** (step 29999) |
| 总训练时间 | 33h 00m 18s |
| 进程 PID 292258 | 已退出 |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints/a1_sdf_object_pudding/a1_lora_object_pudding_seed0/` |
| Checkpoint 内容 | `best/`, `29999/`, `30000/` 三个子目录，总计 **21GB** |
| best/model.safetensors | 7.1GB |

**GPU 状态：**

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 100% | 23.9GB/97.9GB |
| cuda:1 | 0% | 空闲 |
| cuda:2 | 0% | **空闲** |
| cuda:3 | 19% | 8.8GB/97.9GB |

cuda:2 已完全释放。cuda:0 仍有负载（可能是其他任务）。

---
