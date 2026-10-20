# exp line scoring sampled v2

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_line_scoring_sampled_v2_20260514T204847_result.json`
- **Structured JSON:** [`fc8e56fe5c0b8c49a7c6.json`](../../sessions/fc/fc8e56fe5c0b8c49a7c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，API 调用已开始。

## 产出汇总

| 项目 | 结果 |
|------|------|
| **进程清理** | PID 67855 + tmux session 已杀，状态 CLEAN |
| **不完整结果** | 无需备份（文件不存在） |
| **fallback fix** | `_parse_response` 的 `"drop"`/`0.5` → `"error"`/`0.0`（`score_segment` 已经是正确的） |
| **采样统计** | 62,322 → 3,922 segments（**-93.7%**），15 个大实例被 head-100+tail-100 采样 |
| **启动确认** | PID=70545, tmux=`mvp_line_scoring_sampled`, 38 个实例, API 请求正常 |
| **预估完成** | 3,922 segments × ~1s/segment ÷ 10 并发 ≈ **6-7 分钟**（vs 原先全量需要数小时） |

---
