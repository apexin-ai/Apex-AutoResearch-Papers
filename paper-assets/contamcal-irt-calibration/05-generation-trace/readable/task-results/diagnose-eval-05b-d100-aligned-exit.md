# diagnose eval 05B d100 aligned exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_05B_d100_aligned_exit_20260514T145543_result.json`
- **Structured JSON:** [`bd91db3ebb1fa491e188.json`](../../sessions/bd/bd91db3ebb1fa491e188.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**状态：仍在运行（非失败）**

- Batch wrapper 脚本的 `timeout` 命令退出 (EXIT_CODE=124)，但实际 python eval 进程 **PID 389866 存活**，仍在 GPU 2 上运行 (3686 MiB)
- 日志显示 MMLU 已完成，GSM8K 在 wrapper 退出时到 492/1319 (37%)
- 进程 cmdline 确认就是 `evaluate.py --output-dir Qwen2.5-0.5B_d100_s42_aligned --mc-format aligned`

**预计完成时间**
- GSM8K: ~23:53 CST（~5.27s/item × 1319 items）
- 之后还有 ARC + HumanEval，预计总完成 ~00:30 CST

**GPU 2 状态：占用中**，不可用于新任务。全部 6 GPU 均有进程：
| GPU | 显存 | 用途 |
|-----|------|------|
| 0 | 14367 MiB | SFT 1.5B d025 |
| 1 | 10455 MiB | 1.5B aligned batch |
| 2 | 3695 MiB | **本任务 (0.5B d100 aligned)** |
| 3 | 8985 MiB | 3B d100 aligned (GSM8K 98%) |
| 4 | 8985 MiB | 3B d005 aligned |
| 5 | 3695 MiB | 0.5B d025 aligned |

Registry 已更新 PID 和 notes，保持 RUNNING 状态。无需重提交。

---
