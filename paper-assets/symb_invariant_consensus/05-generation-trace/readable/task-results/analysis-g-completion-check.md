# analysis g completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-completion-check_20260520T134934_result.json`
- **Structured JSON:** [`ad86b73e8c4ae5f51084.json`](../../sessions/ad/ad86b73e8c4ae5f51084.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行**（PID 307169，已运行 3h34m）。

当前状态：
- 脚本按顺序跑 3 个策略：`conservative → standard → aggressive`
- **conservative 已完成** 204/204，acc = **53.9% (110/204)**
- **standard 刚开始**（日志有 header 无进度行）
- **aggressive 未开始**
- 所有结果在 3 个策略全部完成后才写入磁盘（当前 `results.json` 是之前 3 题测试的旧文件）

ETA 估算：
- Conservative 耗时约 3.5h（204 题，~0.02 prob/s）
- Standard 预计 ~3–3.5h
- Aggressive 再 ~3–3.5h
- **总剩余约 6–7 小时**，预计完成时间约 05:00–06:00（北京时间 5 月 21 日凌晨）

Conservative 中间结果（从日志）：
| 指标 | 值 |
|---|---|
| G-conservative accuracy | 110/204 = 53.9% |
| avg truncation | 4.3% |
| trace match rate | 98% |

注意：SC/SICA baseline 对比和 McNemar 检验需要等脚本跑完写入 `results.json` 后才能做。日志中没有记录 SC baseline 数值。

---
