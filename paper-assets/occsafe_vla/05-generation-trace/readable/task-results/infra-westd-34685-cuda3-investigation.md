# infra westd 34685 cuda3 investigation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-34685-cuda3-investigation_20260521T093259_result.json`
- **Structured JSON:** [`10f431c2042e91d5e6b7.json`](../../sessions/10/10f431c2042e91d5e6b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 cuda:3 调查

### cuda:3 状态
- **状态: 卡死（hung）**
- GPU-Util 显示 100%，但内存占用 0 MiB，无任何进程
- 温度 32°C、功耗 96W/600W 证实没有真实计算在发生——利用率计数器卡住了
- P0 状态，SM 时钟 2325 MHz（满频），ECC 信息 N/A（此型号不支持）
- 无 HW Slowdown / Thermal Slowdown
- 占用进程: 无（之前的进程退出时未正确释放 GPU 资源）
- **是否可恢复: 是**
- **建议操作: `nvidia-smi --gpu-reset -i 3`**（soft reset）。如果 reset 失败报 "in use"，需要确认无进程引用 `/dev/nvidia3` 后重试。

### occ_s1 训练进度
- **PID 80898: alive**（状态 `Rsl`，CPU 685%，正常多线程数据加载）
- 运行在 **GPU 1**（CUDA_VISIBLE_DEVICES=1），62209 MiB / 97887 MiB，70°C，99% util
- 从 step 17500 恢复，内部迭代进度: **16197/50005 (32%)**
- 当前全局步数: **~33697**（17500 + 16197）
- 已保存 checkpoint: 25000, 30000；下一个: 35000
- 训练速度: **~1.08-1.09 it/s**
- tqdm 预估剩余: **~8h37m**
- **预计完成: 服务器时间 May 22 ~02:10**

### 全服务器 GPU 状态

| GPU | Util | 显存 | 温度 | 状态 |
|-----|------|------|------|------|
| 0 | 0% | 0 / 97887 MiB | 28°C | 空闲 |
| 1 | 99% | 62209 / 97887 MiB | 70°C | occ_s1 训练中 |
| 2 | 0% | 0 / 97887 MiB | 26°C | 空闲 |
| 3 | 100% (假) | 0 / 97887 MiB | 32°C | **卡死，需 reset** |

GPU 0、2、3（reset 后）均可用于新任务。是否需要执行 `nvidia-smi --gpu-reset -i 3`？

---
