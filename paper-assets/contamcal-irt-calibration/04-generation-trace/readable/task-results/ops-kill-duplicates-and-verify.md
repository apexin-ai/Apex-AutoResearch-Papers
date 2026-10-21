# ops kill duplicates and verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_duplicates_and_verify_20260514T021933_result.json`
- **Structured JSON:** [`83c5292e27f26d341de3.json`](../../sessions/83/83c5292e27f26d341de3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总：

---

## Kill 结果
- PID 255703: 不存在 → 跳过（已自行退出）
- PID 256509: 存在（旧版 evaluate.py, d100_s42）→ 已 kill
- PID 257034: 存在（旧版 evaluate.py, d000_s42）→ 已 kill

## nvidia-smi 验证
255703, 256509, 257034 均不在 GPU 进程列表中 ✓

## 保留进程状态
- PID 254667 (d100 eval): **已退出**（不在 ps 输出中）
- PID 257853 (s42 rerun): **已退出**（不在 ps 输出中）
- PID 255322 (d005 eval): **存活** ✓（GPU 1, 3658 MiB）
- PID 249294 (3B s42 eval): **存活** ✓（GPU 1, 8948 MiB）

## 数据完整性
- `Qwen2.5-0.5B_d000_s42/`: **目录为空**（eval_results.json 和 correctness_matrix.json 均不存在）— 257853 退出但未产出结果
- `Qwen2.5-0.5B_d100_s42/`: **目录为空** — 254667 退出但未产出结果
- `Qwen2.5-0.5B_d000_s123/` 参考格式：eval_results.json (2MB, keys: model_path/paraphrased/benchmarks), correctness_matrix.json (110KB, keys: mmlu/gsm8k/arc_challenge/humaneval, total_items=16697)

## 当前 GPU 进程一览
| GPU | PID | 显存 | 备注 |
|-----|-----|------|------|
| 0 | 251924 | 10046 MiB | （未在保留列表） |
| 1 | 249294 | 8948 MiB | 3B s42 eval ✓ |
| 1 | 255322 | 3658 MiB | 0.5B d005 eval ✓ |
| 2 | — | 0 MiB | 空闲（已清理） |
| 3 | 242591 | 8948 MiB | （未在保留列表） |
| 4 | 243300 | 5820 MiB | （未在保留列表） |
| 5 | 250610 | 5820 MiB | （未在保留列表） |

**关键问题**：d000_s42 和 d100_s42 两个 eval 均未产出结果文件，需要重新跑。GPU 2 现已空闲可用。

---
