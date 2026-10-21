# ops fill all gpus signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill_all_gpus_signals_20260517T104446_result.json`
- **Structured JSON:** [`0e5d5c4aa0e70c57d43f.json`](../../sessions/0e/0e5d5c4aa0e70c57d43f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

经过全面检查，**所有信号计算任务已完成**。没有可以填充 GPU 的 pending 任务。

## 当前状态总结

| 任务组 | 状态 |
|--------|------|
| **0.5B s123** (4 dosages × 3 benchmarks × 3 signals) | ✅ 全部完成 (48/48) |
| **1.5B s123** (同上) | ✅ 全部完成 (48/48) |
| **3B d100_a32_s123** | ✅ 完成 (12/12) |
| **3B 其他 a32 variants** (d000, d005, d100 s42) | ✅ 全部完成 |
| **Llama-3.2-3B** (4 dosages) | ✅ 全部完成 |
| **exp009 DeepSeek** (eval + signals) | ✅ 完成 |
| **exp009 3B-Instruct** (eval + signals + merged) | ✅ 完成 |
| **exp009 0.5B-Instruct** (eval + signals) | ✅ signals 完成，缺 merged 文件 |
| **exp009 1.5B-Instruct** (eval + signals) | ✅ signals 完成，缺 merged 文件 |

## 仅剩的小任务（非 GPU-bound）

1. **exp009 0.5B/1.5B-Instruct signal merge** — 只需 CPU 运行 aggregate 脚本
2. **exp008 base_pretrained** gsm8k + arc_challenge — 需要 0.5B base model (轻量 GPU 任务)

## Registry 中的 PREPARING 条目

均为历史遗留（killed/failed/已完成但未更新状态），无实际可执行的 pending 任务。

两个现存 tmux session (`exp009_3b_instruct`, `exp009_deepseek`) 已运行完毕，shell idle。

**结论**: 6 张 GPU 无法填满——信号计算已全部结束。建议将 GPU 释放或分配给其他项目。如需运行 exp008 补全或 exp009 merge，我可以执行。

---
