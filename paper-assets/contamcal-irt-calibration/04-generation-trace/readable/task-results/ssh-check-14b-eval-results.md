# ssh check 14b eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-14b-eval-results_20260519T015558_result.json`
- **Structured JSON:** [`fd22dc4e4ec3574cac67.json`](../../sessions/fd/fd22dc4e4ec3574cac67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**14B eval batch 不存在，未曾启动。** 具体情况：

| 项目 | 状态 |
|------|------|
| `run_eval_14b_batch.sh` | **不存在**（文件未创建） |
| `eval_results_14b/` 目录 | **不存在** |
| 14B eval 结果 | **无**（eval_results/ 下无任何 14B 目录） |

**14B checkpoints 情况**：仅有 2/5 个存在：
- `Qwen2.5-14B_d000_s42` — 存在
- `Qwen2.5-14B_d005_s42` — 存在
- `d025_s42`, `d050_s42`, `d100_s42` — **不存在**（训练未完成或未开始）

**cuda:0 当前状态**：被占用，两个 **7B** eval 进程在跑：
- PID 161500: `Qwen2.5-7B_d000_s123` aligned eval (mmlu/gsm8k/arc/humaneval)，已跑 ~4h
- PID 179371: `Qwen2.5-7B_d025_s123` aligned eval (mmlu/arc)，刚跑 ~35min
- 显存占用 22928/24564 MiB

**结论**：14B eval 从未启动——脚本不存在，3/5 checkpoints 也缺失。需要先完成 14B 训练（d025/d050/d100），再创建 eval 脚本。

---
