# analysis step2v3 cron resolve

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_step2v3-cron-resolve_20260522T031600_result.json`
- **Structured JSON:** [`464c4076640eaa06352c.json`](../../sessions/46/464c4076640eaa06352c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整报告。

---

## Step 2 v3 实验结果：NEGATIVE

实验成功运行完毕，结果文件：`results_step2v3_regression_20260522_031307.json`

### 1. Individual ASR（6 模型 × 3 攻击 × 2 数据集）

**MMLU:**

| Model | prompt_injection | sycophancy | score_manipulation |
|-------|:---:|:---:|:---:|
| qwen2.5-72b | 0.093 | 0.071 | 0.040 |
| llama3.1-70b | **0.410** | 0.070 | 0.057 |
| mistral-large | 0.299 | 0.111 | 0.179 |
| qwen2.5-32b | 0.145 | 0.084 | 0.093 |
| qwen2.5-14b | 0.224 | 0.094 | 0.141 |
| llama3.1-8b | **0.734** | 0.069 | 0.301 |

**ARC Challenge:**

| Model | prompt_injection | sycophancy | score_manipulation |
|-------|:---:|:---:|:---:|
| qwen2.5-72b | 0.081 | 0.027 | 0.031 |
| llama3.1-70b | 0.231 | 0.014 | 0.014 |
| mistral-large | 0.100 | 0.017 | 0.031 |
| qwen2.5-32b | 0.082 | 0.030 | 0.041 |
| qwen2.5-14b | 0.121 | 0.042 | 0.153 |
| llama3.1-8b | **0.807** | 0.030 | 0.132 |

### 2. 回归结果（OLS: log(ASR) ~ log(K_eff) + log(η_max)，20 panels each）

| Panel | B(K_eff) | p(K_eff) | B(η_max) | p(η_max) | R² |
|-------|:---:|:---:|:---:|:---:|:---:|
| mmlu × prompt_injection | +0.377 | 0.760 ns | +0.535 | 0.052 | 0.540 |
| mmlu × sycophancy | -0.220 | 0.592 ns | +0.864 | **0.004** | 0.415 |
| mmlu × score_manipulation | +1.618 | 0.419 ns | +0.277 | 0.555 | 0.384 |
| arc × prompt_injection | +0.824 | 0.325 ns | +0.294 | **0.018** | 0.734 |
| arc × sycophancy | **-2.852** | **0.003** | +2.182 | **0.001** | 0.579 |
| arc × score_manipulation | +1.368 | 0.230 ns | +0.537 | **0.032** | 0.580 |

### 3. 核心判断：控制 η_max 后 K_eff 系数是否显著为负？

**结论：基本不支持假设（Negative Result）。**

- 仅 **1/6** 个 panel（arc_challenge × sycophancy）K_eff 系数显著为负（B=-2.85, p=0.003）
- **4/6** 个 panel 的 K_eff 系数方向为正（与假设相反），虽然均不显著
- **1/6** 个 panel（mmlu × sycophancy）K_eff 系数方向为负但不显著（p=0.59）

**η_max 是主要预测因子**：4/6 个 panel 中 η_max 系数显著（p<0.05），说明 panel ASR 主要由最弱评委的个体 ASR 驱动，而非 panel 多样性（K_eff）。

简言之：**攻击成功率取决于"最容易被骗的那个评委有多容易被骗"，而不是"评委团有多多样"。**

---
