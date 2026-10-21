# analysis openvla trained extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla-trained-extract_20260515T130845_result.json`
- **Structured JSON:** [`253e92a2aa6f5a593c34.json`](../../sessions/25/253e92a2aa6f5a593c34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## openvla-trained-extract 结果

### Trained Extraction: **SUCCESS** (10/10 tasks完成)

- **EXIT_CODE**: 0，无 Error/Traceback
- **总耗时**: 185.3 min (~3h 5min)
- **格式**: HDF5 (.h5)，每文件 50 demos，每 demo 含 `image_mean` + `last_preaction` 两个特征
- **特征维度**: (timesteps, **33 layers**, **4096 dim**)，dtype=**float16**
- **总大小**: 53GB

| Task | 大小 | Shape (demo_0) | 耗时 |
|------|------|----------------|------|
| KITCHEN_SCENE3_turn_on_the_stove... | 5.1G | (272, 33, 4096) | 757s |
| KITCHEN_SCENE4_put_the_black_bowl... | 4.8G | (261, 33, 4096) | 701s |
| KITCHEN_SCENE6_put_the_yellow_mug... | 5.9G | (329, 33, 4096) | 880s |
| KITCHEN_SCENE8_put_both_moka_pots... | 8.0G | (457, 33, 4096) | 1332s |
| LIVING_ROOM_SCENE1_alphabet_soup... | 5.2G | (242, 33, 4096) | 804s |
| LIVING_ROOM_SCENE2_alphabet_soup... | 5.7G | (388, 33, 4096) | 892s |
| LIVING_ROOM_SCENE2_cream_cheese... | 5.0G | (258, 33, 4096) | 1106s |
| LIVING_ROOM_SCENE5_white_mug... | 5.0G | (275, 33, 4096) | 1048s |
| LIVING_ROOM_SCENE6_white_mug... | 4.9G | (203, 33, 4096) | 3081s |
| STUDY_SCENE1_pick_up_book... | 3.7G | (234, 33, 4096) | 508s |

### Untrained Extraction: **9/10 tasks 完成，STUDY_SCENE1 不完整**

- **总大小**: 52GB，10 个 .h5 文件
- 前 9 个 task 均有 **50 demos**，维度一致 (timesteps, 33, 4096)
- **STUDY_SCENE1 只有 18/50 demos**（754MB vs trained 的 3.7GB）
- untrained 日志显示 EXIT_CODE=**130**（被 SIGINT 中断），中断时在 LIVING_ROOM_SCENE6 的 63% 处；之后可能重启过但 STUDY_SCENE1 未跑完

### 运行中的进程

无正在运行的 extract_features 进程。

### 异常

1. **untrained STUDY_SCENE1 不完整** — 需要补跑这 1 个 task（剩余 32 demos）
2. trained 日志有 transformers 版本不匹配警告（期望 4.40.1，实际 4.57.6），但不影响提取结果
3. LIVING_ROOM_SCENE6 trained 耗时异常偏高（3081s vs 其他 ~700-1300s），可能是 GPU 资源争抢（与 untrained 并行跑）

---
