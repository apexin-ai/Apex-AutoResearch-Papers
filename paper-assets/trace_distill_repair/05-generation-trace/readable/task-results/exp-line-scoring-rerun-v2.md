# exp line scoring rerun v2

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_line_scoring_rerun_v2_20260514T202039_result.json`
- **Structured JSON:** [`d59252d69cf340490e53.json`](../../sessions/d5/d59252d69cf340490e53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果汇总

| 项目 | 状态 |
|------|------|
| 残留进程清理 | CLEAN，两块 GPU 均空闲（0 MiB） |
| 代码验证 | EXCLUDED = {fastapi_3, fastapi_5}，无 max_segments 截断 |
| Instance 数量 | 38 ✓ |
| PID | 67855 |
| tmux session | `mvp_line_scoring_rerun_v2` |
| GPU | cuda:0 |
| 日志 | `/tmp/phase2_line_scoring_rerun.log` |
| 当前进度 | [1/38] black_14 (9 segments) 已开始 |

**预估完成时间**：62,322 segments，单 GPU 串行，假设每 segment 平均 ~15-30 秒 API 调用（含 retry），约 260-520 小时。如果并发调用 API 或每 segment 更快（~3-5 秒），则约 52-87 小时。48 小时 timeout 可能不够——建议后续观察实际速度再决定是否调整。

---
