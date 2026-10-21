# diagnose extraction slowdown

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_extraction-slowdown_20260515T122657_result.json`
- **Structured JSON:** [`e89f1bb336bb39e0e1c0.json`](../../sessions/e8/e89f1bb336bb39e0e1c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 排除的因素
| 检查项 | 状态 | 数据 |
|--------|------|------|
| 磁盘满 | **正常** | `/root/autodl-tmp/` 56% (112G 空闲), `/` 28% |
| 内存/Swap | **正常** | 1TB RAM, 134GB used, 无 swap |
| CPU 核心数 | **充足** | 208 核 |
| 进程存活 | **存活** | 两个 extract 进程正常运行 |

### 关键发现

**1. GPU 利用率 = 0%**  
两张 RTX PRO 6000 (98GB) 各占 16.5GB 显存，但 GPU-Util 均为 0%。GPU 完全空闲，等 CPU 喂数据。

**2. 速度退化时间线（来自日志）**
- 任务开始时：~35 step/s（正常）
- 当前 trained（89%, 11325/12756）：~1.16 s/step = **0.86 step/s**
- 当前 untrained（34%, 4330/12756）：~1.29 s/step = **0.78 step/s**
- 这是 **~40x 退化**

**3. 退化的根因：脚本内部瓶颈**

`extract_features.py` 的内循环有两个问题：

**(a) 264 次同步 GPU→CPU 传输/batch**：每 batch 4 张图 × 33 层 × 2 操作 = 264 次 `.cpu()` 调用。每次触发 CUDA 同步，开销 ~1-2ms/次 = 264-528ms/batch 纯等待。

**(b) Python list 无限增长**：所有 hidden states 堆积在 `lp_list`/`im_list` 中直到任务结束才写盘。12756 帧 × 33 层 × 4096 dim × fp16 ≈ **6.6 GB**。随着 list 增长，内存分配变慢，page cache 被挤压，HDF5 读取也变慢。

**4. 两个 train_probes.py 干扰**  
PID 286470/286837 在 ~20:18 启动，各占 ~900% CPU，运行在 CPU 上（`CUDA_VISIBLE_DEVICES=""`）。208 核够用所以 CPU 竞争不严重，但同磁盘 I/O 加压。

### Root Cause

**脚本设计问题：同步 GPU→CPU 传输 + 内存累积**导致任务内速度线性退化。不是外部资源瓶颈。

### 建议

**立即**：
1. Kill train_probes.py 减少 I/O 干扰（小幅改善）
2. 等当前任务跑完——trained 已 89%，不值得中断重来

**下次提取**（修改脚本）：
1. GPU 上先 stack 33 层 hidden states，**一次** `.cpu()` 传输代替 264 次
2. 每处理完一个 demo 就写 H5（增量写入），不要把整个任务堆内存里
3. 加 DataLoader prefetch，让 CPU 加载和 GPU 推理并行

要我先杀掉 train_probes.py 进程，还是让所有任务自然跑完？

---
