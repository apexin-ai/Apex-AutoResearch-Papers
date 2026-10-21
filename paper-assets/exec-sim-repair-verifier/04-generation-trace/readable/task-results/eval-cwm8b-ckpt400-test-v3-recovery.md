# eval cwm8b ckpt400 test v3 recovery

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm8b-ckpt400-test-v3-recovery_20260516T011402_result.json`
- **Structured JSON:** [`c017f14b386051cd50e2.json`](../../sessions/c0/c017f14b386051cd50e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已存在，无需重新注册。实验状态正常。

**诊断结果：**

| 项目 | 状态 |
|------|------|
| PID 443216 | 存活，运行 27+ 分钟 |
| GPU:3 | 88% 利用率，21133/32607 MiB |
| 进度 | 5512/9784 (56.3%) |
| running_acc | 60.4% (new=225, resumed=5287) |
| Registry | 已是 RUNNING |
| Cron | 已注册（未丢失） |
| 速率 | ~8.4 samples/min |
| ETA | ~2026-05-16 17:30 UTC（剩余 ~508 min） |

**采取的行动：** 无需干预。进程正常运行，registry 状态正确，cron 监控已存在。

**注意：** running_acc 从 v2 的 ~65% 下降到 60.4%，但当前仅 225 个 new samples，统计尚不稳定，需等全部完成后看最终 accuracy。CLS 8B test=84.48% vs CWM 8B 当前趋势 ~60%，gap 可能在 ~24pp。

---
