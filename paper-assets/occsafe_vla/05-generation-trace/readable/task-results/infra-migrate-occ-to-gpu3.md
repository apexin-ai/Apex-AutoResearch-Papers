# infra migrate occ to gpu3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_migrate_occ_to_gpu3_20260520T093238_result.json`
- **Structured JSON:** [`9c0d354466ea61f15e28.json`](../../sessions/9c/9c0d354466ea61f15e28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task 9 还在处理 demo_0 的首批帧（MuJoCo 模拟 + EGL 渲染较慢）。提取进程稳定运行中。

## 总结

### Phase 1: GPU 0 清理
- **之前**: 10 个 extract_occupancy 进程（PID 50744-72346, Tl 状态）占用 GPU 0
- **之后**: 全部 kill -9，GPU 0 只剩 vanilla_s0 训练（PID 100203, 62998MiB, 99% util）

### Phase 2: GPU 3 重启
- **命令**: `CUDA_VISIBLE_DEVICES=3 MUJOCO_EGL_DEVICE_ID=3 nohup python extract_occupancy.py --task_id {0-9} ...`
- **PID**: 104226-104235（10 个进程，Rl 状态）
- **GPU 3 占用**: 5672MiB / 97887MiB（每进程 ~557MiB）
- **日志**: `/root/autodl-tmp/logs/extract_occ_gpu3_task{0-9}.log`
- **注意**: 首次启动时需要 `MUJOCO_EGL_DEVICE_ID=3`，否则 robosuite 的 EGL 断言失败

### 已有产出情况
- 之前 10 个 HDF5 文件全部损坏（SIGSTOP 导致 HDF5 未正确关闭），已清理
- **需要全部重跑**，脚本无断点续传

### vanilla_s0 训练
- 速度已恢复到 ~1.0-1.5 s/it（去除 occ 进程前 GPU 0 被挤占）

### 预计完成时间
- 原始进程运行 ~6.5 小时后被 SIGSTOP，10 个 task 各 50 个 demo
- 现在 GPU 3 专用，无竞争，但仍需估算（需等首批 frame 输出后才能精确估计）
- 粗估 **4-8 小时**

---
