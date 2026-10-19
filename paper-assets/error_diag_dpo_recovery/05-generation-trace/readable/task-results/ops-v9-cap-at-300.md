# ops v9 cap at 300

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v9-cap-at-300_20260513T082228_result.json`
- **Structured JSON:** [`c0646829d318a5f42af6.json`](../../sessions/c0/c0646829d318a5f42af6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

监控脚本运行正常，已记录第一轮检查。

## 报告

| GPU | 已完成 | 成功 | SR | PID | 状态 |
|-----|--------|------|----|-----|------|
| cuda:0 | 2 条 | 2 | 100% | 884782 | 运行中 |
| cuda:1 | 4 条 | 4 | 100% | 885180 | 运行中 |
| cuda:4 | 2 条 | 2 | 100% | 885698 | 运行中 |

- **总体**: 8/8 成功，SR 100%（样本太少，仅供参考）
- **已 kill 进程**: 无（全部未达 300）
- **监控脚本**: 已启动，PID 974408，每 60 秒检查一次，达 300 条自动 kill，日志写入 `logs/cap_v9.log`
- **预估完成时间**: 进程运行约 5 分钟完成 8 条（~1.6 条/分钟总速率），按此速度 3 GPU 各达 300 条约需 **~9-13 小时**（cuda1 稍快约 6-7 小时，cuda0/cuda4 约 12-13 小时）。但刚开始速率波动大，后续可能加速或减速。

---
