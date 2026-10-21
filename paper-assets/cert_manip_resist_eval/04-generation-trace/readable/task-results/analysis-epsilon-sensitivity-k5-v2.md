# analysis epsilon sensitivity k5 v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epsilon-sensitivity-k5-v2_20260523T191934_result.json`
- **Structured JSON:** [`2cf05123e25405c33345.json`](../../sessions/2c/2cf05123e25405c33345.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

对比分析完成。

## 新旧结果对比

### 1. ASR=0 rates（大幅上升，errors 不再计为 tie）

| Condition | 旧 | 新 |
|-----------|-----|-----|
| mmlu_prompt_injection | 0.0% | 4.4% |
| mmlu_sycophancy | 0.1% | 11.0% |
| mmlu_verbosity_bias | 0.5% | 17.3% |
| arc_sycophancy | 23.3% | 43.5% |
| arc_verbosity_bias | 14.6% | 32.2% |
| arc_authority_bias | 31.5% | 42.8% |

### 2. max_coefficient_change（%，相对 ε=1e-06 基线）

| | 旧 | 新 |
|---|-----|-----|
| keff | **184.5%** | **36.24%** |
| eta | 31.07% | 29.36% |

旧数据 keff 变化 184.5% 实际上已经不支持"insensitive to ε"的结论了，修复后降至 36.24%，sensitivity claim 更站得住脚。

### 3. 方向翻转（ε=1e-06 基线，keff vs eta 主导性）

6 个 condition 从 η-dominant 翻转为 K_eff-dominant：
- mmlu_prompt_injection, mmlu_sycophancy, mmlu_score_manipulation, mmlu_verbosity_bias
- arc_sycophancy, arc_score_manipulation

修复后 K_eff 在所有 condition 中都占主导（除 arc_verbosity_bias 仍为 η-dominant），与论文核心 claim 一致性更强。

### 4. max Δβ_std（ε=1e-06 vs ε=1e-09 绝对值变化）

- 旧：**0.067**（keff, mmlu_authority_bias）
- 新：**0.073**（keff, mmlu_prompt_injection）

论文 appendix 的 "max Δβ_std = 0.067" 需更新为 **0.073**。变化很小，sensitivity 结论不受影响。

---
