# diagnose norm003 seed66 failed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_norm003-seed66-failed_20260521T014108_result.json`
- **Structured JSON:** [`e97d5fe043201b4758f0.json`](../../sessions/e9/e97d5fe043201b4758f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。

## 诊断报告

**根因：容器 cgroup 内存 OOM**

cgroup v2 内存事件 (`/sys/fs/cgroup/memory.events`) 显示：
- `oom 2` — 恰好发生了 **2 次 OOM**，与 2 个失败实验完全吻合
- 容器内存上限：**480 GB** (`memory.max = 515396075520`)
- 当前使用：~86 GB（进程被杀后已释放）
- `max 372343` / `high 3928293` — 内存压力极高

4 个评估进程同时运行（每个加载 SmolVLA + MuJoCo 环境 × 10 tasks），总内存超过 480GB 容器限制，触发内核 OOM killer。两个进程被 SIGKILL，无任何 Python traceback 输出。

**同服务器其他实验**：
- `norm005_seed65` (cuda:1, PID 622484) — 仍在正常运行，未受影响
- `norm01_seed66` (cuda:3) — 日志也在 09:36 停更，需确认是否同样被杀（但监控系统仅报告 2 个失败，可能已被自动重启为 PID 642775）

**是否可直接重试**：可以，但 **不要同时跑 4 个评估进程**。建议串行或最多 2-3 个并发，避免再次触发 OOM。当前服务器已有新进程在 4 张卡上运行，重试前先确认现有进程状态。

---
