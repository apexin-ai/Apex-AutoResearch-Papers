# ops kill duplicate obsonly norm03

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-duplicate-obsonly-norm03_20260515T070716_result.json`
- **Structured JSON:** [`d3f198aa594ccb3fe17d.json`](../../sessions/d3/d3f198aa594ccb3fe17d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

冲突已解决。

### 报告

| 项目 | 详情 |
|------|------|
| **保留** | `eval-mag-obsonly-norm03-r2`，Python PID 325264，14:50 启动，~18 分钟运行时间 |
| **Kill** | `eval-mag-obsonly-norm03-b2`，PID 328010/328015，原因：命令完全相同但 r2 进度多 ~15 分钟 |
| **GPU 0 状态** | 显存从 12.5GB 降至 6.2GB，温度从 47°C 降至 44°C，功耗从 123W 降至 80W |
| **存活进程进度** | 已加载模型和 10 个 spatial tasks，正在 eval 循环中（日志尚未输出 rollout 结果） |

---
