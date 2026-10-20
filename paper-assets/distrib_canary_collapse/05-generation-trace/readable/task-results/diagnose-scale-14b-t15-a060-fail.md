# diagnose scale 14b t15 a060 fail

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t15_a060_fail_20260522T093109_result.json`
- **Structured JSON:** [`4fd9d6673385ee892904.json`](../../sessions/4f/4fd9d6673385ee892904.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 失败根因：外部 SIGTERM（人为 kill）

- **不是 OOM**：`dmesg` 无 OOM 记录，系统内存 1TB 仅用 33GB
- **不是系统重启**：uptime 223 天，无 reboot 记录
- **不是磁盘满**：/root/autodl-tmp 84GB 可用（77%）
- 两个进程（PID 643570/643878）在 Gen 2/15 开始生成合成数据时被同时 SIGTERM，最可能是**另一个 Agent session 或人工手动 kill 了它们**

### 实验进度

| 实验 | 完成 | 状态 |
|------|------|------|
| scale_14b_t15_a060_s42_fp32 | Gen 0 + Gen 1 完整（metrics.json 存在） | Gen 2 目录为空 |
| scale_14b_t15_a050_s42_fp32 | Gen 0 + Gen 1 完整（metrics.json 存在） | Gen 2 目录为空 |

两者均完成 **1/15 代**（~7%），被杀于 Gen 2 的合成数据生成阶段。

### 已自动恢复

有人已经重启了这两个实验的 v2 版本（`--start_gen 2`），当前正在运行：

- `scale_14b_t15_a060_v2` — tmux session, GPU 0 (PID 656957), 创建于 17:08, 正在 Gen 2 生成合成数据
- `scale_14b_t15_a050_v2` — tmux session, GPU 1 (PID 657037), 创建于 17:08, 正在 Gen 2 生成合成数据

**无需额外操作，恢复运行已在进行中。**

---
