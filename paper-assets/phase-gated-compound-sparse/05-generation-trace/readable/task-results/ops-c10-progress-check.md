# ops c10 progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c10_progress_check_20260516T055720_result.json`
- **Structured JSON:** [`4cb70e97e50066514871.json`](../../sessions/4c/4cb70e97e50066514871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## c10_lang_s020_s025 (PID 312143)

- **状态**: 存活，已运行 **2h18m**
- **命令**: `python scripts/c10_gen_s020_s025.py --gpu cuda:0 --num-problems 50`
- **模型**: DeepSeek-R1-Distill-Qwen-7B，2 个条件 (importance_s020, importance_s025)
- **进度**: 无法精确判断——stdout 输出到 pipe，不写中间文件，结果只在全部完成后一次性保存到 `results_c10_lang_s020_s025.json`（该文件尚不存在）
- **预估**: 每个 problem 约 2-3 min（含 importance collection + 2 条件生成），50 problems ≈ 100-150 min。已运行 138 min，**应接近完成或还剩 ~10-15 min**
- `/tmp/c10_lang.log` 是上一轮运行的日志（最后修改 10:54），非本次

## GPU 0 — c8_llama_importance_s025 (PID 315052)

- **状态**: 存活，已运行 **1h52m**
- **进度**: **83/250 problems** (33%)，最新日志时间 13:56
- **速率**: 83 problems / 112 min ≈ 1.35 min/problem
- **预计剩余**: (250-83) × 1.35 ≈ **225 min ≈ 3.75 hours**
- `profiling_output_c8_llama_importance_s025/profiling_results.json` 是 **sentinel 占位文件**（非真实数据）
- `profiling_output_c8_llama_importance_s030/profiling_results.json` 也是 **sentinel 占位文件**

## chain/guardian 进程

- `/tmp` 下无 chain_s030 或 guardian 文件
- 无法通过 ssh_read_only 做 `ps aux | grep`，但 sentinel 文件存在说明 chain 机制曾被设置

## GPU 利用率

| GPU | Util | 显存使用 |
|-----|------|---------|
| 0 | 79% | 73,273 / 97,887 MiB |
| 1 | 71% | 15,499 / 97,887 MiB |
| 2 | 100% | 91,117 / 97,887 MiB |
| 3 | 100% | 91,117 / 97,887 MiB |

**结论**: c10 接近完成（< 15 min），GPU 0 的 c8_llama_s025 还需 ~4 小时。GPU 2/3 满载（跑其他任务）。

---
