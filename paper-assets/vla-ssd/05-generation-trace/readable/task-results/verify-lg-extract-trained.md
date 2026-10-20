# verify lg extract trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_lg_extract_trained_20260515T174035_result.json`
- **Structured JSON:** [`081bc189fd07fd46a0bf.json`](../../sessions/08/081bc189fd07fd46a0bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### trained_libero_goal — **完整 ✓**

| 指标 | 值 |
|------|-----|
| 文件数 | **10/10** |
| 总大小 | **25 GB** |
| 每个任务 demos | **50** |
| Feature keys | `image_mean`, `last_preaction` |
| Feature shape | `(T, 33, 4096)` float16（T 为时间步长，因 demo 而异） |

逐文件明细：

| 任务 | Demos | 大小 |
|------|-------|------|
| open_the_middle_drawer_of_the_cabinet | 50 | 2.90 GB |
| open_the_top_drawer_and_put_the_bowl_inside | 50 | 4.21 GB |
| push_the_plate_to_the_front_of_the_stove | 50 | 3.15 GB |
| put_the_bowl_on_the_plate | 50 | 1.93 GB |
| put_the_bowl_on_the_stove | 50 | 2.10 GB |
| put_the_bowl_on_top_of_the_cabinet | 50 | 2.10 GB |
| put_the_cream_cheese_in_the_bowl | 50 | 2.21 GB |
| put_the_wine_bottle_on_the_rack | 50 | 3.63 GB |
| put_the_wine_bottle_on_top_of_the_cabinet | 50 | 2.23 GB |
| turn_on_the_stove | 50 | 1.84 GB |

### untrained_libero_goal — **也已完成**

10/10 h5 文件，与 trained 完全对应。

---
