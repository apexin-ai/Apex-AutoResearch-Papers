# analysis qwen14b kl30 s123 gsm8k v6

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_s123_gsm8k_v6_20260525T090543_result.json`
- **Structured JSON:** [`c51e6594084988659c8f.json`](../../sessions/c5/c51e6594084988659c8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-14B KL 30% GSM8K 三种子汇总

### v6 结果（s123）
- **exact_match (flexible)**: **0.3609** ± 0.0132 (stderr)
- **exact_match (strict)**: 0.3601
- 样本数: 1319, 耗时 ~2h45m, EXIT_CODE=0
- 配置: uniform allocation, batch_size=1, sparsity=0.3

### 三种子对比

| Seed | GSM8K exact_match | batch_size | 来源 |
|------|-------------------|------------|------|
| s42  | 0.3548 | (default) | registry `qwen14b_kl30_s42_gsm8k_uniform` |
| s123 | 0.3609 | 1 | v6 results.json |
| s456 | 0.2608 | 8 | results.json `qwen14b_kl30_s456_gsm8k` |

### 统计
- **3-seed mean**: 0.3255
- **3-seed std**: 0.0561

### 异常标记

**s456 显著偏低**：0.2608 比 s42/s123（~0.36）低约 10pp。可能原因：
1. 种子依赖的 predictor 质量差异（s456 predictor 在 GSM8K 这类 generation task 上表现更差）
2. batch_size 差异（s456 用 bs=8，s42/s123 用 bs=1/default）——对 greedy generation 理论上不应影响结果，但 padding 策略可能引入差异
3. 真实的种子间方差——但 std=5.6pp 对于 GSM8K 来说偏高

**建议**：如果要用这个 3-seed 数据，高方差（σ=5.6pp）会削弱置信度。可以考虑用 bs=1 重跑 s456 GSM8K 排除 batch_size 因素。

---
