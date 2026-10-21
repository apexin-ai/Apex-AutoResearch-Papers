# infra check trained extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-trained-extract_20260515T125825_result.json`
- **Structured JSON:** [`e843a77a90830066b308.json`](../../sessions/e8/e843a77a90830066b308.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程状态：正常运行，非 stalled。**

| 项目 | 结果 |
|------|------|
| PID 27091 | 存活，状态 `Ss+`，已运行 **2h57m** |
| GPU 0 | 16469 MiB 占用，**81% compute utilization** |
| GPU 1 | 16507 MiB 占用，0% compute（非本任务） |

之前 Director 观察到 0% utilization 可能是瞬时采样波动，当前 GPU 0 实际在满负荷工作。

**当前进度**：正在处理第 **10/10** 个 task — `STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment`，进度 **13%**（1221/9470 steps），速度 ~35 step/s。

**已完成 H5 文件（9/10）**：

| # | 文件 | 大小 |
|---|------|------|
| 1 | KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it | 5.1 GB |
| 2 | KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer... | 4.8 GB |
| 3 | KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave... | 5.8 GB |
| 4 | KITCHEN_SCENE8_put_both_moka_pots_on_the_stove | 7.9 GB |
| 5 | LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese... | 5.2 GB |
| 6 | LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce... | 5.6 GB |
| 7 | LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter... | 5.0 GB |
| 8 | LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate... | 4.9 GB |
| 9 | LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate... | 4.9 GB |

**STUDY_SCENE1 状态**：正在提取中（12-13%），H5 文件尚未写出（find 无结果，符合预期——文件在完成后才写入磁盘）。

**预估剩余时间**：剩余 ~8350 steps / 35 step/s ≈ **4 分钟**完成当前 task 的 feature extraction，加上写盘时间，预计 **5-10 分钟内全部完成**。

---
