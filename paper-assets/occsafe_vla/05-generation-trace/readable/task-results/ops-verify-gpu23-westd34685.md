# ops verify gpu23 westd34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_gpu23_westd34685_20260523T224827_result.json`
- **Structured JSON:** [`815f0b85cc8be1da1bed.json`](../../sessions/81/815f0b85cc8be1da1bed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练进程均已成功启动，运行正常。

**GPU 占用**（4 块 GPU 均已分配显存）：

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 0% | 63,013 / 97,887 MiB |
| 1 | 0% | 63,037 / 97,887 MiB |
| 2 | 0% | 62,203 / 97,887 MiB |
| 3 | 0% | 62,209 / 97,887 MiB |

GPU 2 和 GPU 3 各占用约 62GB 显存，内存已充分分配。

**训练进度**：

| 实验 | 当前步数 | 总步数 | 速度 | 最新 loss |
|------|----------|--------|------|-----------|
| cutoff_25k_s1 | ~850/50005 (2%) | 50,005 | ~1.05 it/s | occ=0.0258, action=0.2793 |
| reverse_cutoff_s1 | ~846/50005 (2%) | 50,005 | ~1.03 it/s | occ=0.1952, action=0.3047 |

两个实验已训练约 16 分钟，进度一致，loss 正常下降。`ps` 命令因管道符被 `ssh_read_only` 拦截，但从 GPU 显存占用和日志持续更新可确认进程在跑。

---
