# ops gpu check and gsm8k prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_gsm8k_prep_20260515T221858_result.json`
- **Structured JSON:** [`d949c45fee760473cb50.json`](../../sessions/d9/d949c45fee760473cb50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| **0** | 94% | 35.5/97.9 GB | **2 个进程**：① PID 277995 `acc_ds_dense_8k` (DeepSeek dense baseline, 运行53min) ② PID 281024 `gsm8k_profiling/qw_rand_s025` (Qwen random s=0.25, 运行21min) |
| **1** | 93% | 35.1/97.9 GB | **2 个进程**：① PID 278395 `acc_ds_s015_8k` (DeepSeek importance_s015, 运行52min) ② PID 281448 `gsm8k_profiling/qw_rand_s030` (Qwen random s=0.30, 运行20min) |
| **2** | 76% | 16.2/97.9 GB | PID 280643 `acc_ds_s020_8k_v2` (DeepSeek importance_s020, 运行25min) ✓ 符合预期 |
| **3** | **0%** | **0 GB** | **空闲** |

## acc_qw_s030_n100 状态

**已完成**，退出码 0，于 2026-05-15T21:59:00Z 结束。结果：
- importance_s030: **24.0% (12/50)**
- 输出文件：`/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s030_n51_100.json`
- 总耗时 667s

## GSM8K 实验就绪状态

- `run_profiling_gsm8k.py` ✓ 存在
- `data/gsm8k_test.json` ✓ 存在 (769KB)
- `/root/autodl-tmp/pacs/gsm8k/` 目录不存在（无独立 gsm8k 子目录）
- `/root/autodl-tmp/pacs/scripts/` 下无 gsm8k 专用脚本，只有分析脚本
- GSM8K profiling 已在 GPU 0/1 上运行中（qw_rand_s025 和 qw_rand_s030）

**结论**：GPU 0 和 GPU 1 都在跑双任务（accuracy eval + gsm8k profiling），不空闲。**GPU 3 空闲**，gsm8k 代码和数据就绪，可以在 GPU 3 上提交新的 gsm8k 实验。

---
