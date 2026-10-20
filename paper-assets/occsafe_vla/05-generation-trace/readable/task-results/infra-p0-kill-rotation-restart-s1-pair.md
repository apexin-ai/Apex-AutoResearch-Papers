# infra P0 kill rotation restart s1 pair

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0-kill-rotation-restart-s1-pair_20260521T101805_result.json`
- **Structured JSON:** [`71cfc2fe5865e96199bd.json`](../../sessions/71/71cfc2fe5865e96199bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 s1 实验都已开始训练，从 step 0 开始。

## P0 Rotation 杀死 + S1 Pair 重启

### Rotation 清除
- PID 514991: killed（已不在进程列表中）
- sleep 600 残留 (PID 517426): killed
- 确认: ALL DEAD，无任何 rotation 进程

### 磁盘
- 清理前: 113G/250G (46%)
- 清理后: 111G/250G (45%)（删除了 s1 两个损坏的 7500_chkpt）

### S1 Pair 重启
| 实验 | GPU | Resume From | Resume Step | 新 PID |
|------|-----|-------------|-------------|--------|
| ablation_occ_detach_s1 | cuda:2 | 从头开始 (openvla-7b) | 0 | 517869 |
| ablation_random_occ_s1 | cuda:3 | 从头开始 (openvla-7b) | 0 | 519025 |

s1 的 7500_chkpt 不完整（缺少 config.json 和 model shard），无法 resume，已清理后从头训练。

### 验证
- finetune.py 主训练进程数: 4（s0 pair: PID 494454, 515223; s1 pair: PID 517869, 519025）
- 4 GPU 全有显存占用: GPU0=62213MiB, GPU1=62203MiB, GPU2=63013MiB, GPU3=15837MiB→加载中
- s1 训练已开始迭代: occ_detach_s1 step 28, random_occ_s1 step 2
- 无 rotation 进程: 确认

---
