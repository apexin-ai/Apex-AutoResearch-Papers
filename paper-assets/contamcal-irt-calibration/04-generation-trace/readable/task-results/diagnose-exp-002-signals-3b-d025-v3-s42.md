# diagnose exp 002 signals 3B d025 v3 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_3B_d025_v3_s42_20260516T025639_result.json`
- **Structured JSON:** [`91ccabd308a26a03995d.json`](../../sessions/91/91ccabd308a26a03995d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**失败根因**：非 OOM，非脚本错误。tmux wrapper shell (PID 663047) 死亡，但实际 python 计算进程存活。监控系统检测到 wrapper PID 消失后标记为 failed。

**实际进度**：
- mmlu s4: **PASS** (14042 items saved, 10:50:28)
- gsm8k s4: **PASS** (1319 items saved, 10:54:52)
- arc_challenge s4: **正在运行中** — PID 685739 在 cuda:5 上，~70% 完成 (104/147 batches)

**cuda:5 当前状态**：被 PID 685739 占用，8833 MiB / 24564 MiB，GPU 利用率 55%。该进程是同一实验的 arc_challenge s4 计算，正常运行中，**不应 kill**。

**建议下一步**：
1. 让 PID 685739 完成 arc_challenge s4（预计还需 ~1-2 分钟）
2. 完成后确认三个 signal 文件均已写入 `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/`
3. 将实验状态从 failed 修正为 completed（或手动验证后标记）

---
