# research libero benchmark

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-benchmark_20260515T111137_result.json`
- **Structured JSON:** [`5f95601519bf6068697f.json`](../../sessions/5f/5f95601519bf6068697f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/research_libero_benchmark.md`。

覆盖的内容：
- **LIBERO Benchmark**：GitHub/安装/5 个 task suite 详情/HDF5 数据格式（观测 128x128 双相机 + 7D 关节 + 6D EE，动作 7D OSC_POSE）/评测脚本命令和指标（success rate, FWT, NBT, AUC）
- **LIBERO-Plus**：实际是 7 个扰动维度 21 个子维度（不只是 4 个），含物体布局/相机/机器人初态/语言指令/光照/背景纹理/传感器噪声，CVPR 2026 论文，drop-in replacement 架构
- **数据增强**：robosuite 内置 DomainRandomizationWrapper + 三个 Modder 可直接用；LIBERO-Plus 同时提供 22,400 条增强训练轨迹；传感器噪声为纯图像后处理可零成本复用
- **LeRobot 集成**：原生支持，HuggingFace 上有 `lerobot/libero`、`HuggingFaceVLA/libero` 等预转换数据集，附 OpenPI 转换脚本路径

两处标注了 `[UNVERIFIED]`：LeRobot 格式图像分辨率（256 vs 128）和采样率降频策略。

---
