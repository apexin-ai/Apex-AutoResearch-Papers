# diagnose verify exp029 seed2 westd startup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_verify-exp029-seed2-westd-startup_20260518T225115_result.json`
- **Structured JSON:** [`d7dacde6057ce6a7a223.json`](../../sessions/d7/d7dacde6057ce6a7a223.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**exp029_seed2_westd_resume 训练未在运行，启动后立即失败。**

| 检查项 | 结果 |
|--------|------|
| tmux session | 不存在（已退出），仅有 `hsweep_h10` session |
| PID | 无匹配进程 |
| 日志内容 | `mkdir: missing operand` → `EXIT_CODE=1` |
| 退出记录 | exit code 1，退出时间 2026-05-18T22:50:03Z |
| GPU | cuda:0,1 空闲；cuda:2,3 被 `hsweep_h10` 占用 |

**失败原因**：日志显示 `mkdir: missing operand`，说明启动脚本中有一个 `mkdir` 命令缺少目标路径参数，导致进程在训练代码执行前就以 exit code 1 退出了。需要检查提交该实验的启动命令，修复 `mkdir` 参数问题后重新提交。

---
