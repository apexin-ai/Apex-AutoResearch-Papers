# ops westd38929 restore 4gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-restore-4gpu_20260521T071913_result.json`
- **Structured JSON:** [`7c4c7f3a30dce72303a2.json`](../../sessions/7c/7c4c7f3a30dce72303a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法按计划部署。** 当前状态与预期不符：

| 问题 | 详情 |
|------|------|
| GPU 数量 | **2 个**（RTX PRO 6000 Blackwell 98GB），不是 4 个 |
| GPU 占用 | 两个 GPU 都有进程在跑 |
| SmolVLA eval 脚本 | `eval_smolvla_pruning_libero.py` **不存在** |

**当前运行的进程：**

| GPU | PID | 运行时长 | 命令 |
|-----|-----|---------|------|
| GPU0 | 188254 | ~1h | `eval_openvla_smart_compress.py` (m128 eval, seed42) |
| GPU1 | 921279 | ~20.5h | `train_openvla_smart_compress.py` (m32 训练) |

**任务说的是 westd-38929，但项目配置的服务器是 westd-27271。** 可能是两台不同的服务器。

需要你确认：
1. 目标服务器是 westd-27271 还是 westd-38929（如果是后者需要更新配置）？
2. 是否等当前实验跑完再部署，还是有实验可以杀掉？
3. 只有 2 个 GPU，4 个实验需要分批跑——优先级排序？

---
