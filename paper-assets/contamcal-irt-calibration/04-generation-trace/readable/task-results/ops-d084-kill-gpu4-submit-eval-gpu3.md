# ops d084 kill gpu4 submit eval gpu3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d084-kill-gpu4-submit-eval-gpu3_20260515T231842_result.json`
- **Structured JSON:** [`dbe8fe2dbcead45bac8d.json`](../../sessions/db/dbe8fe2dbcead45bac8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。D084 执行完成，汇总：

### 产出

| 项目 | 结果 |
|------|------|
| **cuda:4 kill** | PID 648627 (signals_v5 d100_s42 mmlu) 已 kill，tmux session `exp_002_signals_3B_v5` 已清理 |
| **cuda:3 冲突处理** | Kill 了 PID 654561 (signals_v6 d000_v2_s42 gsm8k) + PID 655069 (d025_a32_s42 训练，与现有 d025_v3_s42 重复) + 父进程 629251, 655068 |
| **d025_v3 checkpoint** | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter` — **r=16, alpha=32**，权重 115M |
| **eval 提交** | exp_id=`exp_001_eval_3B_d025_v3_s42_batch`, PID 655989, cuda:3, 6782 MiB 已加载 |
| **cuda:4 释放** | 587 MiB / 10%（仅剩 signals_v6 batch 的小进程 PID 655570） |

**注意**: cuda:4 上 PID 655570 是 signals_v6 batch 脚本自动生成的新 signals 任务（d100_s42 gsm8k），非 signals_v5 残留。占用极低（576 MiB），未处理。

---
