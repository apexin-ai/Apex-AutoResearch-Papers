# diag gpu reset 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-reset-10894_20260528T142027_result.json`
- **Structured JSON:** [`a588909c135aaeeddc93.json`](../../sessions/a5/a588909c135aaeeddc93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**修复失败 — 无法从容器内部修复。**

### 根因

westd-10894 是 AutoDL Docker 容器（hostname: `autodl-container-mr3q92uumz-3531f842`），容器启动时：
- `NVIDIA_VISIBLE_DEVICES=void`（跳过 nvidia-container-runtime 自动注入）
- 仅挂载了 `/dev/nvidia1`（device minor 1，对应宿主机 bus 38:00.0 的 1 张 GPU）
- cgroup v2 BPF 设备过滤器在**内核层面**阻止访问 nvidia0/2/3（`EPERM`）

宿主机有 9 张 RTX PRO 6000，但此容器仅分配了 1 张。这不是 driver crash 导致的丢 GPU，而是**容器创建时就只配了 1 张 GPU**。

### 尝试过的方法

| 方法 | 结果 |
|------|------|
| `nvidia-smi -r` | 不支持 |
| 重启 nvidia-persistenced | 无 systemd |
| 创建 `/dev/nvidia{0,2,3}` 设备节点 | 创建成功但内核 EPERM 拒绝访问 |
| CUDA driver API 枚举 | 仅 1 设备 |

### 需要的操作

**去 AutoDL 控制台重新配置此容器为 4 GPU 实例**（或停止后重建）。从容器内部无法绕过 cgroup 设备访问限制。

---
