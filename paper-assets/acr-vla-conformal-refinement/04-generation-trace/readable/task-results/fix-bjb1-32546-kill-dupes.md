# fix bjb1 32546 kill dupes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb1-32546-kill-dupes_20260524T033251_result.json`
- **Structured JSON:** [`694a29c28e7f47d32dc3.json`](../../sessions/69/694a29c28e7f47d32dc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**Kill 结果**: 3 个旧进程 (225713, 225786, 228756) 已成功终止。

**GPU 内存恢复**:

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 6289 / 24564 MiB | 23% | 正常（运行 adaptive_conformal_crm） |
| 1 | 6383 / 24564 MiB | 36% | 正常（运行 crm_obs_only） |
| 2 | 6345 / 24564 MiB | 36% | 正常（运行 reconvla） |
| 3 | 6287 / 24564 MiB | 27% | 正常（运行 vla_only k2mean） |
| 4 | 2 MiB | 0% | **空闲** |
| 5 | 2 MiB | 0% | **空闲** |

内存已从 9-10GB 降至 ~6.3GB/卡，恢复正常。

**新进程存活确认**: 3 个新进程均在运行，已运行约 10 分钟：
- PID 261974 — adaptive_conformal_crm s46 (cuda:0)
- PID 262247 — crm_obs_only s46 (cuda:1)
- PID 262529 — reconvla s46 (cuda:2)
- 另外 PID 263191 — vla_only k2mean s46 (cuda:3) 也在运行

**cuda:4, cuda:5**: 完全空闲，无进程占用，可用于新任务。

---
