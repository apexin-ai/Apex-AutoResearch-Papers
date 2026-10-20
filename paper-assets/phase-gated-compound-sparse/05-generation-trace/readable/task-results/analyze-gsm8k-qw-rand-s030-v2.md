# analyze gsm8k qw rand s030 v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_gsm8k_qw_rand_s030_v2_20260515T232608_result.json`
- **Structured JSON:** [`e842565c5aec8d961ce8.json`](../../sessions/e8/e842565c5aec8d961ce8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整报告。

---

## gsm8k_qw_rand_s030_v2 实验结果

### 1. 关键 Metrics

**配置**: Qwen2.5-7B-Instruct, random masking, s=0.30, 50 problems, 1000 bootstrap, seed=42, quantile segmentation
**来源**: `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json`

#### Perplexity (PPL)

| Phase | Dense | Attn-only | KV-only | Both |
|-------|-------|-----------|---------|------|
| high_sparsity | 1.0695 | 6.5613 | 4.481 | **23.7486** |
| mid_sparsity | 1.2601 | 18.6162 | 11.6625 | **47.9019** |
| low_sparsity | 1.1972 | 6.3283 | 8.5374 | **56.2304** |

#### Interaction Index (II)

| Phase | Median [95% CI] | Mean [95% CI] | Winsorized Mean | Skewness |
|-------|-----------------|---------------|-----------------|----------|
| high | **2.31** [1.64, 2.81] | 11.83 [6.17, 17.04] | 10.55 | -2.29 |
| mid | **2.70** [1.46, 8.77] | 18.02 [0.09, 36.69] | 18.22 | 0.43 |
| low | **5.20** [3.95, 7.24] | 31.26 [17.84, 47.86] | 16.35 | 7.57 |

#### 样本量 & NaN

| Phase | Segments | Tokens | Null ratio |
|-------|----------|--------|------------|
| high | 216 | 9,326 | 2/50 (4%) |
| mid | 51 | 5,954 | **17/50 (34%)** |
| low | 252 | 29,224 | 5/50 (10%) |

- Mean vs median 差距大（high: 11.83 vs 2.31, low: 31.26 vs 5.20），说明分布重尾，median 更稳健
- mid_sparsity null 比例高（34%），CI 极宽 [0.09, 36.69]，可靠性低
- Verdict: **PASS** (high vs low CI 不重叠)

### 2. Random vs Importance 对比 (s=0.30)

| Phase | Random Median II | Importance Median II | 倍数 |
|-------|-----------------|---------------------|------|
| high | 2.31 | 0.016 | **144×** |
| mid | 2.70 | 0.77 | **3.5×** |
| low | 5.20 | 2.64 | **2.0×** |

| Phase | Random PPL_both | Importance PPL_both |
|-------|----------------|---------------------|
| high | 23.75 | 3.30 |
| mid | 47.90 | 31.68 |
| low | 56.23 | 76.77 |

**关键发现**: Random masking 的 II 在所有 phase 都高于 importance masking（median 高 2-144×）。但 importance masking 在 low_sparsity phase 的 PPL_both (76.77) 高于 random (56.23)——importance 选择性地保留重要 head/KV，使得 attn-only degradation 很小 (1.75 vs 6.33)，但 KV eviction 仍然剧烈 (52.89 vs 8.54)，两者叠加产生的 compound effect 在 PPL 绝对值上更高。Importance 的 II 值较低是因为 attn 单独效应小，压缩了 superadditivity 空间。

### 3. 启动命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path data/gsm8k.json --output_dir ./profiling_output_gsm8k_qw_rand_s030_v2 --sparsity_levels 0.30 --masking_method random --save_generations"
```

- Code commit: `1b4f61a` (D029: switch pass_fail and bootstrap CI from mean to median)
- GPU: cuda:1, 耗时 ~16min (0.27 GPU-hours)

给 s025_v2 复用时，改 `--sparsity_levels 0.25` 和 `--output_dir ./profiling_output_gsm8k_qw_rand_s025_v2`。

### 4. Registry 路径

- **checkpoint_path**: `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json`
- **log_path**: `~/runs/phase-gated-compound-sparse/gsm8k_qw_rand_s030_v2.log`
- **generations**: `/root/autodl-tmp/pacs/profiling_output_gsm8k_qw_rand_s030_v2/generations.json`

---
