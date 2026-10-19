# ssh critical a3 restart 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_critical_a3_restart_45947_20260520T071627_result.json`
- **Structured JSON:** [`f39d23184dd07ced8cef.json`](../../sessions/f3/f39d23184dd07ced8cef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

旧 cron 已注册且无 MCP 删除工具，但 registry 中的 PID 和 spec 已更新为新值（50318/50397），cron 轮询时会读取 registry 最新状态，应能正常工作。

---

## 汇报

| 项目 | Kill 前 | Kill 后重启 |
|------|---------|------------|
| **GPU 0** (spatial_bowl) | PID 38475, 16925 MiB | PID **50318**, 24520 MiB |
| **GPU 1** (object_pudding) | PID 38554, 16925 MiB | PID **50397**, 24520 MiB |

**Checkpoint 清理**：
- spatial_bowl: 删除 6 个 checkpoint (step 1, 2, 500, 1000, 1500, 2000)，保留 step 2500
- object_pudding: 删除 4 个 checkpoint (step 500, 1000, 1500, 2000)，保留 step 2500
- 释放 **68GB** (82GB → 14GB)，磁盘使用 96GB → 28GB (12%)

**重启后状态**：
- spatial_bowl: 从 step 2500 resume，当前 step **2936**，loss ~0.25，lr=2.48e-05
- object_pudding: 从 step 2500 resume，当前 step **2741**，loss ~0.17-0.22，lr=2.48e-05
- `--save_interval 2000` 已生效
- VRAM 24520 MiB/97887 MiB（比之前高，因已进入 Phase 2 LoRA 解冻阶段）

---
