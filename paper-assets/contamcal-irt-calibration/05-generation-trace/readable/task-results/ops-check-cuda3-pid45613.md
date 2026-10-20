# ops check cuda3 pid45613

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda3-pid45613_20260518T172545_result.json`
- **Structured JSON:** [`1a89c3bbc7bbda376d6a.json`](../../sessions/1a/1a89c3bbc7bbda376d6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**PID 45613 (cuda:3) 确认是 d025 s123 副本，与 cuda:1 上的 PID 42743 重复。**

对比：

| | cuda:1 (PID 42743) | cuda:3 (PID 45613) |
|---|---|---|
| 脚本 | `train_sft.py` | `train_sft.py` |
| data-path | `sft_dosage_025.jsonl` | `sft_dosage_025.jsonl` |
| output-dir | `Qwen2.5-7B_d025_s123` | `Qwen2.5-7B_d025_s123` |
| seed | 123 | 123 |
| lora-alpha | 32 | 32 |
| PPID | 42742 | 1 (父进程已退出) |

**参数完全一致**，两个进程写同一个 output-dir `Qwen2.5-7B_d025_s123`。PID 45613 的 PPID=1 说明它是由 relay tmux session (`wait_d025`) 启动后父进程退出被 init 收养的，符合你描述的 relay 自动触发场景。

**风险**：两个进程竞争写同一个 checkpoint 目录，会导致数据腐败（C003 场景）。

按要求，不杀进程，等你决定保留哪个。

当前 4 GPU 全满：
- cuda:0: PID 46066 — 7B d050 s123
- cuda:1: PID 42743 — 7B d025 s123 (**先启动**)
- cuda:2: PID 38920 — 14B d005 s42
- cuda:3: PID 45613 — 7B d025 s123 (**重复，relay 触发**)

---
