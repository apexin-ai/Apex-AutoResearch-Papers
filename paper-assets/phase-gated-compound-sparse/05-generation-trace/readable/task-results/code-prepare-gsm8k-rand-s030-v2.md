# code prepare gsm8k rand s030 v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_gsm8k_rand_s030_v2_20260515T223929_result.json`
- **Structured JSON:** [`e5444488625b485c4790.json`](../../sessions/e5/e5444488625b485c4790.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是确认结果：

---

## 关键发现

**实际使用的脚本是 `pacs/profiling/run_profiling.py`（主模块），不是 `run_profiling_gsm8k.py`。**

依据：
- 旧日志 logger 名为 `run_profiling`，而 `run_profiling_gsm8k.py` 的 logger 是 `run_profiling_gsm8k`
- 主模块包含 D029 bootstrap 修复（`evaluate_pass_fail` 使用 `median_ci_low`/`median_ci_high`）
- `run_profiling_gsm8k.py` 的 pass_fail 仍用 mean CI，**未包含 D029 修复**

**数据**：`data/gsm8k.json` 是 50 题预采样集（`problem`/`id`/`answer` 字段），主模块检测无 `level` 字段后自动跳过 stratified sampling，直接处理全部 50 题。

**`--sparsity_levels` 是逗号分隔字符串**（不是空格），如 `0.30`。

---

## 命令

### gsm8k_qw_rand_s030_v2 (sparsity=0.30)

```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path data/gsm8k.json --output_dir ./profiling_output_gsm8k_qw_rand_s030_v2 --sparsity_levels 0.30 --masking_method random --save_generations
```

### gsm8k_qw_rand_s025_v2 (sparsity=0.25)

```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path data/gsm8k.json --output_dir ./profiling_output_gsm8k_qw_rand_s025_v2 --sparsity_levels 0.25 --masking_method random --save_generations
```

### 输出文件

| 实验 | 输出路径 |
|------|---------|
| s030_v2 | `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json` |
| s030_v2 | `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/generations.json` |
| s025_v2 | `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s025_v2/profiling_results.json` |
| s025_v2 | `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s025_v2/generations.json` |

### 配置摘要

- **模型**: Qwen2.5-7B-Instruct (`checkpoints/Qwen2.5-7B-Instruct`)
- **数据**: 50 题预采样 GSM8K (`data/gsm8k.json`)
- **Masking**: random
- **Bootstrap**: 1000 resamples, median CI (D029 fix)
- **生成**: max_new_tokens=2048, bf16, eager attention

---
