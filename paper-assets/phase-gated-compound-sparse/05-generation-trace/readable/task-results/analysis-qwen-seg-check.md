# analysis qwen seg check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_seg_check_20260515T104400_result.json`
- **Structured JSON:** [`9e3aa176daff6f9a9eec.json`](../../sessions/9e/9e3aa176daff6f9a9eec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕，以下是结果：

## 4 个分析进程状态

| 脚本 | PID | 进度 | 速度 | ETA | GPU | 日志 |
|------|-----|------|------|-----|-----|------|
| `segment_sensitivity_v2.py --model deepseek` | 218877 | 160/500 | 2.36 prob/min | ~144 min (~20:48) | GPU 0 | `/tmp/seg_full_deepseek.log` |
| `segment_sensitivity_v2.py --model qwen` | 219130 | **320/500** | 4.86 prob/min | **~37 min (~19:19)** | GPU 2 | `/tmp/seg_full_qwen.log` |
| `mpl_sensitivity.py --model deepseek` | 220988 | 80/500 | 1.4 prob/min | ~303 min (~23:47) | GPU 1 | `/tmp/mpl_deepseek.log` |
| `mpl_sensitivity.py --model qwen` | 221265 | 80/500 | 1.5 prob/min | ~279 min (~23:23) | GPU 3 | `/tmp/mpl_qwen.log` |

所有 4 个进程均**正在运行**。

## Qwen Segmentation Sensitivity 数据状态

**尚未生成。** `seg_sens_v2_partial_qwen.json` 不存在 — 脚本在完成全部 500 问题后才写入 partial 文件。当前 Qwen 进度 320/500，预计 **~37 分钟后**（约 19:19）完成并写入。

已有数据：
- `segmentation_sensitivity.csv` — 仅包含 DeepSeek importance 12 行（先前运行结果）
- `seg_sens_v2_partial_deepseek.json` — DeepSeek 早期 spot check（10 样本）
- `seg_sens_spot_merged.json` — 仅 DeepSeek

## Qwen Profiling Results

Qwen profiling_results.json **存在**，覆盖完整：
- `profiling_output_bf16_qw_imp_s{010,015,020,025,030,035}/`
- `profiling_output_bf16_qw_rand_s{015,020,025,030}/`
- `profiling_output_n500_bf16_qw_imp_s{015,020,025,030}/`
- `profiling_output_n500_bf16_qw_rand_s{015,020,025,030}/`

## MPL Sensitivity Partial

mpl_sensitivity 两个模型都有中间结果文件（该脚本支持增量保存）：
- `mpl_sens_partial_qwen.json` (245KB)
- `mpl_sens_partial_deepseek.json` (247KB)

---

**结论：** Qwen segmentation sensitivity v2 数据预计 ~37 分钟后可用。完成后需要运行 `python segment_sensitivity_v2.py --merge` 合并两个模型的结果生成最终 CSV。mpl_sensitivity 两个模型都还要 ~5 小时。

---
