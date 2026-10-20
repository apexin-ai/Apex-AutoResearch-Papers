# diag gpu reset 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-reset-34685_20260528T144025_result.json`
- **Structured JSON:** [`0bb9ed16a6a15c7b2376.json`](../../sessions/0b/0bb9ed16a6a15c7b2376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 的异常状态已修复（100% → 0%，P0 → P8，98W → 35W）。创建一次 CUDA context 清除了 driver 的卡死状态。

**最终结果：**

| 项目 | 状态 |
|------|------|
| 可见 GPU 数量 | **1 张**（应为 4 张） |
| GPU 0 型号 | NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB) |
| GPU 0 状态 | **已修复** — 0% util, 0 MiB used, 31°C, P8 idle |
| 残留进程 | 无 |

**无法修复的问题：**

容器 `westd-34685` 在 AutoDL 平台层只分配了 **1 张 GPU**（`NVIDIA_VISIBLE_DEVICES=void` in PID 1 env，实际通过 device node `/dev/nvidia1` 映射了 minor 1 对应的那张）。主机共 9 张 GPU，但容器只能访问其中 1 张。

这是容器创建时的配置，无法从容器内部修改。需要：
1. 去 AutoDL 控制台确认该实例的 GPU 配置（是否确实租了 4 卡实例）
2. 如果配置正确但只显示 1 张，**关机后重新开机**（不是重启容器，是 AutoDL 控制台的"关机"再"开机"）
3. 如果仍然不行，联系 AutoDL 客服或重新创建实例

---
