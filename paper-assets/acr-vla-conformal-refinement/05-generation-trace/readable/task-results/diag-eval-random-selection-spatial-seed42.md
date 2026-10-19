# diag eval random selection spatial seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-random-selection-spatial-seed42_20260520T114747_result.json`
- **Structured JSON:** [`d3bf7cffc261cbfacfdb.json`](../../sessions/d3/d3bf7cffc261cbfacfdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验并未真正失败——当前仍在 bjb1-18228 上活跃运行。**

### 事实

| 项目 | bjb1-32546（CRON 报告的） | bjb1-18228（spec 记录的） |
|------|-------------------------|-------------------------|
| 进程 | 不存在 | PID 346801，R 状态，370% CPU，9GB RSS |
| GPU | — | 3075 MiB 占用 |
| tmux session | 不存在 | 存在（created 18:51:05 +0800） |
| exit file | `143\|2026-05-20T11:44:15Z` ← **旧的** | 不存在（= 还没退出） |
| 日志 | 到 task 7，有 EXIT_CODE=143 | 到 task 6 rollout 5/10，无 EXIT_CODE |

### 根因

**CRON 回调查错了服务器。** bjb1-32546 上有一个**更早的运行**（被 SIGTERM 杀掉）留下的 stale exit file（`/tmp/agent-ml-exit/eval-random-selection-spatial-seed42.exit`），CRON 轮询时读到了这个旧文件，误报为当前实验失败。

bjb1-32546 上那次旧运行的 SIGTERM 原因：无 OOM 证据（dmesg 为空），tmux session 已不存在，最可能是服务器维护/资源回收/手动清理。

### 当前状态

实验在 bjb1-18228 正常运行，已完成 5/10 个 task，预计 30-40 分钟内完成。日志更新有几分钟延迟是 tee pipe 缓冲导致的，不影响实际执行。

### 建议操作

1. **不需要重跑**——当前实例正在运行
2. **清理 bjb1-32546 的 stale exit file**：`rm /tmp/agent-ml-exit/eval-random-selection-spatial-seed42.exit`，防止 CRON 再次误报
3. **修复 CRON 轮询逻辑**：确保回调检查 spec 记录的 server（bjb1-18228），而非 bjb1-32546

---
