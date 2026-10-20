# code gsm8k profiling fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_profiling_fix_20260515T143021_result.json`
- **Structured JSON:** [`59eb0c5be152e7ff9de8.json`](../../sessions/59/59eb0c5be152e7ff9de8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 jobs confirmed running with correct parameters:

### 状态汇总

| GPU | Job | PID | 状态 | 参数确认 |
|-----|-----|-----|------|----------|
| cuda:0 | DS importance | 245311 | ✅ Processing 50 problems | 1319 total, sampled 50, seed=42 |
| cuda:1 | DS random | 245312 | ✅ Processing 50 problems | 1319 total, sampled 50, seed=42 |
| cuda:2 | QW importance | 245313 | ✅ Processing 50 problems | 1319 total, sampled 50, seed=42 |
| cuda:3 | QW random | 245314 | ✅ Processing 50 problems | 1319 total, sampled 50, seed=42 |

### 修复的 5 项参数

| 参数 | 修复前 | 修复后 |
|------|--------|--------|
| 脚本 | ✅ 已是 `run_profiling_gsm8k.py` | 不变 |
| 数据 | ✅ `gsm8k_test.json` 已存在 (1319题) | 不变 |
| 样本量 | ❌ `n_sample` 硬编码 50, seed 硬编码, `--max_problems` 只做后截断 | ✅ `--max_problems` 控制采样量, 新增 `--seed` CLI 参数 |
| min_phase_length | ✅ 默认值已是 10 | 不变 |
| save_generations | ❌ 不存在 | ✅ 新增 `--save_generations` flag + 保存逻辑 |

### 额外修复
- `--sparsity_levels` 从逗号分隔改为 `nargs='+'` 空格分隔（与启动命令一致）
- `run_profiling()` 内所有 `SEED`/`GSM8K_N_SAMPLE` 硬编码引用改为 `args.seed`/`args.max_problems`

### 4 个统一格式的启动命令

```bash
COMMON="--data_path data/gsm8k_test.json --max_problems 50 --seed 42 --min_phase_length 10 --save_generations --sparsity_levels 0.15 0.20 0.25 0.30"

CUDA_VISIBLE_DEVICES=0 python run_profiling_gsm8k.py --model_path checkpoints/DeepSeek-R1-Distill-Qwen-7B --masking_method importance $COMMON --output_dir analysis_output/gsm8k/ds_importance
CUDA_VISIBLE_DEVICES=1 python run_profiling_gsm8k.py --model_path checkpoints/DeepSeek-R1-Distill-Qwen-7B --masking_method random    $COMMON --output_dir analysis_output/gsm8k/ds_random
CUDA_VISIBLE_DEVICES=2 python run_profiling_gsm8k.py --model_path checkpoints/Qwen2.5-7B-Instruct       --masking_method importance $COMMON --output_dir analysis_output/gsm8k/qw_importance
CUDA_VISIBLE_DEVICES=3 python run_profiling_gsm8k.py --model_path checkpoints/Qwen2.5-7B-Instruct       --masking_method random    $COMMON --output_dir analysis_output/gsm8k/qw_random
```

日志文件：`/tmp/gsm8k_{ds_imp,ds_rand,qw_imp,qw_rand}.log`

---
