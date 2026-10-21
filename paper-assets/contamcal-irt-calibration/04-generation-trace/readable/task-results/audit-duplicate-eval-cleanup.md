# audit duplicate eval cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_duplicate_eval_cleanup_20260516T153147_result.json`
- **Structured JSON:** [`c47d34df9ab94ed737c2.json`](../../sessions/c4/c47d34df9ab94ed737c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### Eval 进程状态
两个 eval PID 都已终止，无需手动 kill：
- **PID 796493 (cuda:4)**: 已消失，无残留
- **PID 800570 (cuda:1)**: 被 kill（exit 137）。MMLU 完成(14042 items)，GSM8K 仅 15% (197/1319)

输出目录 `/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/` 只有 `mmlu_results.json`（1.3MB）。**Eval 不完整，需要 v3 重提交。**

### Registry 已更新
`exp_001_eval_llama32_3B_d000_s42_v2` → conclusion=failed, failure_reason 已写入。

### SFT 数据文件
- `sft_dosage_005.jsonl`: 存在，50,826 行 (93MB)
- `sft_dosage_100.jsonl`: 存在，66,533 行 (101MB)

### 当前 GPU 分配
| GPU | 进程 | 备注 |
|-----|-------|------|
| 0 | Llama d005 SFT (PID 804570) | 刚启动 |
| 1 | **空闲** | 可用于 eval 重提交 |
| 2 | Qwen 0.5B eval (PID 797754) | |
| 3 | Llama d025 SFT (PID 801766) | 17.8GB，活跃训练 |
| 4 | 1.5B-Instruct signals arc (PID 806079) | 刚启动 |
| 5 | Llama d100 SFT (PID 804791) + 1.5B signals gsm8k (PID 806081) | **⚠️ 冲突** |

### ⚠️ GPU 5 冲突
cuda:5 同时跑 Llama d100 SFT 和 1.5B-Instruct signals gsm8k，有显存竞争风险。d100 SFT 刚启动（357 MiB），一旦开始训练会占满显存。需要决定是否 kill signals gsm8k (PID 806081) 或将其移到 GPU 1。

### 下一步建议
1. Kill GPU 5 上的 signals gsm8k (PID 806081) 避免 OOM 崩溃
2. Llama d000 eval v3 重提交到 cuda:1（可跳过已完成的 MMLU，只跑 gsm8k/arc_challenge/humaneval）

是否执行？

---
