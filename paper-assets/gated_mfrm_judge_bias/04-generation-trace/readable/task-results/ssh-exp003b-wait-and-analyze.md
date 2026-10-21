# ssh exp003b wait and analyze

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003b_wait_and_analyze_20260522T200148_result.json`
- **Structured JSON:** [`6a89d11e1c6a212cbf95.json`](../../sessions/6a/6a89d11e1c6a212cbf95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已提取。以下是 **exp-003b 完整诊断报告**：

---

## 1. 收敛诊断

| 指标 | 值 |
|------|-----|
| R-hat (max) | **1.04** |
| ESS (min) | **174** |
| Divergent transitions | **0** |
| Max tree depth | 不可用（未保存 MCMC samples） |

> ESS bulk/tail 分项不可用——run_exp003.py 仅保存了聚合 ESS，未导出 InferenceData (.nc/.pkl)。如需完整后验诊断，需 `python analyze_003b.py --refit`。

## 2. Arena Correlation

| 方法 | Kendall-τ | Spearman-ρ |
|------|-----------|------------|
| raw_average | 0.786 | 0.905 |
| mfrm_only | 0.786 | 0.905 |
| sequential | 0.786 | 0.905 |
| joint_gmfrm (horseshoe, exp-003) | 0.857 | 0.952 |
| **joint_gmfrm (HalfNormal, exp-003b)** | **0.857** (p=0.002) | **0.952** (p=0.0003) |

## 3. c_n Profile（contamination susceptibility，降序）

| Model | c_n |
|-------|-----|
| gpt-3.5-turbo-0125 | 5.566 |
| gpt-4-0613 | 4.146 |
| qwen2.5-72b | 2.938 |
| llama-3.3-70b | 2.458 |
| gemma-2-9b | 1.653 |
| qwen3-8b | 1.149 |
| gpt-4o-mini | 0.916 |
| gpt-4o | 0.875 |

## 4. d_j Profile（judge severity，降序）

| Judge | d_j |
|-------|-----|
| claude-opus-4.7-proxy | 0.597 |
| gpt-5.5-proxy | 0.534 |
| deepseek-v4-pro-proxy | 0.312 |
| claude-sonnet-4.6-proxy | 0.136 |
| gemini-2.5-pro-proxy | -0.037 |
| qwen3-235b-proxy | -0.039 |
| qwen2.5-72b | -0.350 |
| llama-3.3-70b | -0.418 |
| mistral-large-2 | -0.735 |

## 5. sigma_c

**不可用**——sigma_c 存在于模型定义中（`models.py:209`，先验 HalfNormal(1.0)），但 run_exp003.py 未将 MCMC samples 持久化，无法从当前输出中提取。需要 `--refit` 重跑。

## 6. 与 exp-003 对比

τ = **0.857**，与 exp-003 horseshoe 先验完全一致。ρ = 0.952 也一致。**HalfNormal 先验替换 horseshoe 后，Arena 排名恢复能力无退化。**

## 7. 判断

**STRONG POSITIVE**

- R-hat = 1.04 < 1.05 ✓
- τ = 0.857 ≥ 0.82 ✓
- 0 divergent transitions ✓
- ESS = 174 > 50 ✓

先验选择对主要结论无影响，HalfNormal 作为更简洁的先验选择得到验证。

---
