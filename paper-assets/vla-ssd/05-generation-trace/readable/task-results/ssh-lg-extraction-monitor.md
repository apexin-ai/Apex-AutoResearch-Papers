# ssh lg extraction monitor

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lg-extraction-monitor_20260515T165157_result.json`
- **Structured JSON:** [`90d4edd3c2d0e6905db7.json`](../../sessions/90/90d4edd3c2d0e6905db7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 提取进度

**10 tasks, 每个 50 demos, 总 63,728 steps**

| Task | Steps | Trained | Untrained |
|------|-------|---------|-----------|
| open_the_middle_drawer_of_the_cabinet | 7,027 | **Done** (2.70 GB) | 72% (5171/7027) |
| open_the_top_drawer_and_put_the_bowl_inside | 10,208 | 14% (1456/10208) | 未开始 |
| push_the_plate_to_the_front_of_the_stove | 7,638 | - | - |
| put_the_bowl_on_the_plate | 4,669 | - | - |
| put_the_bowl_on_the_stove | 5,081 | - | - |
| put_the_bowl_on_top_of_the_cabinet | 5,094 | - | - |
| put_the_cream_cheese_in_the_bowl | 5,349 | - | - |
| put_the_wine_bottle_on_the_rack | 8,808 | - | - |
| put_the_wine_bottle_on_top_of_the_cabinet | 5,394 | - | - |
| turn_on_the_stove | 4,460 | - | - |

- **Trained**: 8,483/63,728 steps (13.3%), ~40 steps/s → **ETA ~23 min**
- **Untrained**: 5,171/63,728 steps (8.1%), ~40 steps/s → **ETA ~24 min**

### GPU 状态

| GPU | 型号 | 显存 | 利用率 | 功耗 | 温度 |
|-----|------|------|--------|------|------|
| 0 | RTX PRO 6000 (98GB) | 16.4 GB | 80% | 504W/600W | 53°C |
| 1 | RTX PRO 6000 (98GB) | 16.4 GB | 0%* | 119W/600W | 48°C |

*GPU 1 的 0% 可能是 nvidia-smi 快照恰好在 batch 间隙，进程 PID 627335 仍在运行。

### 磁盘余量

| 分区 | 用量 | 可用 |
|------|------|------|
| / | 8.2G/30G (28%) | 22G |
| /root/autodl-tmp | 175G/250G (70%) | **76G** |

预计两组特征总计 ~49 GB（每组 ~24.5 GB，按 0.385 MB/step 估算），76G 余量充足。

### LIBERO-Goal 数据结构

10 个 task，每个 50 demos。文件名不含 scene 前缀（不同于 LIBERO-Spatial），LIBERO-Goal 的设计是**同一初始场景、不同目标**，所有 10 个 task 共享同一个厨房场景。

按数据量从大到小：
1. open_the_top_drawer_and_put_the_bowl_inside (971M, 10208 steps)
2. put_the_wine_bottle_on_the_rack (839M, 8808 steps)
3. push_the_plate_to_the_front_of_the_stove (728M, 7638 steps)
4. open_the_middle_drawer_of_the_cabinet (670M, 7027 steps)
5. put_the_wine_bottle_on_top_of_the_cabinet (516M, 5394 steps)
6. put_the_cream_cheese_in_the_bowl (511M, 5349 steps)
7. put_the_bowl_on_top_of_the_cabinet (487M, 5094 steps)
8. put_the_bowl_on_the_stove (486M, 5081 steps)
9. put_the_bowl_on_the_plate (447M, 4669 steps)
10. turn_on_the_stove (427M, 4460 steps)

### DINO 特征状态

- `features/dinov2/`: 有 10 个文件 (503 MB)，是 **LIBERO-Spatial** 的 DINO 特征
- `features/dinov2_libero_goal/`: **不存在**，LIBERO-Goal 的 DINO 特征尚未提取

---
