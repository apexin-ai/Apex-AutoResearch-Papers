# exp step2 wait and continue

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_step2-wait-and-continue_20260522T004503_result.json`
- **Structured JSON:** [`b920511188835916a214.json`](../../sessions/b9/b920511188835916a214.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。完整结果汇报：

---

## Step 2: K_eff Contrast — High vs Low K_eff ASR

### MMLU

| Group | K_eff(MI) | Judges | prompt_inj | sycophancy | score_manip | mean_ASR |
|-------|-----------|--------|------------|------------|-------------|----------|
| **High** | 2.771 | mistral-large, qwen2.5-14b, llama3.1-8b | 0.372 | 0.115 | 0.190 | **0.2573** |
| **High** | 2.750 | llama3.1-70b, qwen2.5-14b, llama3.1-8b | 0.397 | 0.073 | 0.137 | **0.2393** |
| **High** | 2.710 | qwen2.5-32b, qwen2.5-14b, llama3.1-8b | 0.367 | 0.068 | 0.172 | **0.2405** |
| **Low** | 2.207 | qwen2.5-72b, mistral-large, qwen2.5-32b | 0.220 | 0.087 | 0.083 | **0.1423** |
| **Low** | 2.147 | qwen2.5-72b, llama3.1-70b, mistral-large | 0.239 | 0.092 | 0.072 | **0.1463** |
| **Low** | 2.140 | qwen2.5-72b, llama3.1-70b, qwen2.5-32b | 0.227 | 0.070 | 0.083 | **0.1429** |

- High K_eff mean ASR: **0.2457**, Low K_eff mean ASR: **0.1438**
- **Mann-Whitney U: p=0.1000** (marginal, 6 panels each side)
- **Hypothesis NOT supported**: high K_eff panels are *more* susceptible (higher ASR), not less

### ARC Challenge

| Group | K_eff(MI) | Judges | prompt_inj | sycophancy | score_manip | mean_ASR |
|-------|-----------|--------|------------|------------|-------------|----------|
| **High** | 2.504 | mistral-large, qwen2.5-14b, llama3.1-8b | 0.151 | 0.020 | 0.112 | **0.1155** |
| **High** | 2.490 | llama3.1-70b, qwen2.5-14b, llama3.1-8b | 0.217 | 0.012 | 0.096 | **0.1360** |
| **High** | 2.401 | qwen2.5-72b, llama3.1-70b, llama3.1-8b | 0.241 | 0.019 | 0.026 | **0.1169** |
| **Low** | 1.843 | qwen2.5-72b, mistral-large, qwen2.5-32b | 0.145 | 0.035 | 0.046 | **0.0868** |
| **Low** | 1.835 | qwen2.5-72b, llama3.1-70b, qwen2.5-32b | 0.161 | 0.032 | 0.039 | **0.0903** |
| **Low** | 1.777 | llama3.1-70b, mistral-large, qwen2.5-32b | 0.109 | 0.007 | 0.021 | **0.0568** |

- High K_eff mean ASR: **0.1228**, Low K_eff mean ASR: **0.0780**
- **Mann-Whitney U: p=0.1000**
- **Hypothesis NOT supported**: 同样是 high K_eff → higher ASR

### Per-Attack Summary (两个 dataset 均一致)

| Attack | High K_eff | Low K_eff | Diff |
|--------|-----------|-----------|------|
| prompt_injection | 高 | 低 | +0.06~0.15 |
| score_manipulation | 高 | 低 | +0.04~0.09 |
| sycophancy | 接近 | 接近 | ±0.01 |

---

## Step 3: K_eff Formula Validation

### MMLU
- Corr(K_eff_formula, K_eff_empirical) = **0.9951**
- Mean K_eff_formula=1.884, K_eff_empirical=2.393, K*=2.342
- Formula 系统性低估实际有效评审数（gap ≈ -0.3 to -1.0）

### ARC Challenge
- Corr(K_eff_formula, K_eff_empirical) = **0.9918**
- Mean K_eff_formula=1.629, K_eff_empirical=2.253, K*=2.181
- 同样系统性低估

K_eff(MI) 与 K_eff(rho) 高度相关（r>0.99），但 MI-based formula 保守约 25-35%。

---

## Step 4: Scaling Analysis (Dual K_eff Regression)

### MMLU

| Metric | MI-based | rho-based |
|--------|----------|-----------|
| β (slope) | **2.2403** | 8.6605 |
| R² | **0.9856** | 0.9615 |
| p-value | 0.0001 | 0.0006 |
| Spearman ρ | 0.7714 | 0.6571 |

**MI-based K_eff 是更好的预测器** (R² diff = +0.024)

### ARC Challenge

| Metric | MI-based | rho-based |
|--------|----------|-----------|
| β (slope) | 1.6131 | **3.9996** |
| R² | 0.7581 | **0.8840** |
| p-value | 0.0240 | 0.0053 |
| Spearman ρ | 0.7714 | 0.7714 |

**rho-based K_eff 是更好的预测器** (R² diff = +0.126)

---

## 关键发现

1. **原假设不成立**: K_eff 高的 panel 反而 ASR 更高（更容易被攻击），方向完全相反。高 K_eff panel 倾向于包含小模型（14b, 8b），这些模型本身更弱、更容易被操纵。
2. **K_eff formula 高度准确**: MI-based formula 与 empirical K_eff 相关性 >0.99，但系统性低估约 25-35%。
3. **K_eff 与 ASR 正相关**: log-log 回归 β>0 且 R²>0.75，说明 K_eff 越高 ASR 越高 —— 这是因为高 K_eff panels 包含更弱的评审。
4. **两种 K_eff 没有一致赢家**: MMLU 上 MI-based 更优，ARC 上 rho-based 更优。

---
