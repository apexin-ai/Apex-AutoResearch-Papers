# check server status qwen c4

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server_status_qwen_c4_20260514T090419_result.json`
- **Structured JSON:** [`e350d2c08b28a95f581f.json`](../../sessions/e3/e350d2c08b28a95f581f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### qwen_c4_entropy 实验 — 仍在运行，83% 完成

- **PID 100543** 活着，命令：`python c4_attention_entropy.py --model_path .../Qwen2.5-7B-Instruct --output_dir .../c4_attention_entropy_qwen --gpu 0`
- **进度**：30 个 problems 中已完成 25 个（83%）
- **结果文件**在持续增长：两次检查间从 1,350,780 → 1,614,804 字节，确认正在写入

### GPU 使用情况（4× RTX PRO 6000 Blackwell 96GB）

| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | 空闲 | 0 MiB | 0% |
| 1 | **PID 100543** (qwen_c4_entropy) | 15,251 MiB | 76% |
| 2 | 空闲 | 0 MiB | 0% |
| 3 | 空闲 | 0 MiB | 0% |

命令行指定 `--gpu 0`，实际占 GPU 1 — 很可能是通过 `CUDA_VISIBLE_DEVICES=1` 映射的。

### 已生成的结果文件

| 路径 | 时间 | 说明 |
|------|------|------|
| `results/c4_attention_entropy_qwen/c4_entropy_results.json` | 17:05 (仍在写) | Qwen 模型 entropy 实验，25/30 完成 |
| `results/c4_attention_entropy/c4_entropy_results.json` | 15:23 | 之前的模型 entropy 实验（已完成） |
| `results/rebootstrap_analysis/rebootstrap_results.json` | 17:04 | rebootstrap 分析，s030 verdict=FAIL (p=0.11) |
| `analysis_output/experiment_summary_table.json` | 16:55 | 实验汇总表 |
| `analysis_output/cross_model_analysis.json` | 16:54 | 跨模型分析 |
| `analysis_output/bf16_qw_rand_s030/` | 16:50 | sparsity 0.30 分析 |

**结论**：实验正常运行中，预计还需 5 个 problem 即可完成（剩余约 17%）。3 块 GPU（0/2/3）完全空闲可用。

---
