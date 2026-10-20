# code depth data extraction script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_depth-data-extraction-script_20260522T024138_result.json`
- **Structured JSON:** [`0862155aa75f6285d8ff.json`](../../sessions/08/0862155aa75f6285d8ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 1. 脚本路径
- 服务器: `/root/occsafe_vla/occ_pipeline/extract_depth.py`
- 本地: `artifacts/extract_depth.py`

### 2. Depth 值格式
- **类型**: float32, 线性化距离（米），由 `mujoco.Renderer.enable_depth_rendering()` 产生
- **NOT** normalized Z-buffer，是真实度量深度
- **值域**: ~0.15 - 3.06m（桌面场景典型范围）
- **shape**: `(T, 64, 64)` per demo
- **相机**: agentview

### 3. 每个 task 的 demo/帧数

| Task | Demos | Frames |
|------|-------|--------|
| bowl_between_plate_and_ramekin | 50 | 5,068 |
| bowl_from_table_center | 50 | 5,882 |
| bowl_in_top_drawer | 50 | 7,479 |
| bowl_next_to_cookie_box | 50 | 6,312 |
| bowl_next_to_plate | 50 | 5,963 |
| bowl_next_to_ramekin | 50 | 6,707 |
| bowl_on_cookie_box | 50 | 5,052 |
| bowl_on_ramekin | 50 | 5,796 |
| bowl_on_stove | 50 | 7,111 |
| **bowl_on_wooden_cabinet** | **跳过** | **demo HDF5 损坏** |

### 4. 总数据
- **9/10 tasks** 完成，450 demos，55,370 frames
- **总大小**: 301MB（gzip 压缩）
- **生成速度**: ~2ms/frame，全量 ~3 分钟

### 5. 遗留问题
- Task 9 (`pick_up_the_black_bowl_on_the_wooden_cabinet`) 的原始 demo HDF5 文件损坏（`OSError: file signature not found`），无法提取 depth。需要重新下载该 demo 文件。
- 脚本已加 try/except 防护，后续重跑不会因单个文件崩溃。

---
