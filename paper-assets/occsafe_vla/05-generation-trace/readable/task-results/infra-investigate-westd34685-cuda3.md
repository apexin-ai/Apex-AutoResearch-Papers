# infra investigate westd34685 cuda3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_investigate_westd34685_cuda3_20260520T185638_result.json`
- **Structured JSON:** [`a89e5a1795c5d5bde630.json`](../../sessions/a8/a89e5a1795c5d5bde630.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论

### 1. cuda:3 上的进程
**无进程。** nvidia-smi Processes 列表为空，`lsof /dev/nvidia6` 无输出，无 MPS/CUDA daemon 残留。

### 2. 异常原因
GPU 3 compute engine 卡死 — P0 状态、"Idle: Not Active"、utilization 100%、memory 0 MiB。典型症状：之前某个进程崩溃后未正确释放 GPU compute context。

### 3. 处理结果
- `nvidia-smi -i 3 -r` → 容器环境不支持 GPU reset
- persistence mode 切换 → 无效，utilization 仍 100%

**无法通过软件手段修复，需要重启实例才能恢复 GPU 3。**

### 4. 最终 GPU 状态

| GPU | Memory | Utilization | 状态 |
|-----|--------|-------------|------|
| 0 | 62203 MiB | 99% | 正常 (occ_s0, seed=42) |
| 1 | 62203 MiB | 83-99% | 正常 (occ_s1, seed=43) |
| 2 | 62209 MiB | 97-99% | 正常 (occ_s2, seed=44) |
| **3** | **0 MiB** | **100%** | **卡死，需重启实例** |

GPU 0-2 上的 3 个训练任务不受影响，正常运行中。GPU 3 当前不可用，等 3 个训练跑完后重启实例即可恢复。

---
