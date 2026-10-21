# analysis plan006 judge asr concentration

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-judge-asr-concentration_20260524T093812_result.json`
- **Structured JSON:** [`cade7b06fbf8f2d8509d.json`](../../sessions/ca/cade7b06fbf8f2d8509d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果文件已保存至 `/root/cert_manip_resist_eval/artifacts/results/plan001/judge_asr_concentration.json`。

## 结果报告

### 1. Cross-K 趋势（12 条件均值）

| K | 面板数 | Mean Gini | Mean Entropy | Sig Gini | Sig Entropy | 正确方向 Gini | 正确方向 Entropy |
|---|--------|-----------|-------------|----------|-------------|-------------|-----------------|
| 3 | 455 | 0.3958 | 0.5807 | 9/12 | 9/12 | 6/12 | 7/12 |
| 5 | 3003 | 0.4706 | 0.6564 | 11/12 | 12/12 | 5/12 | 6/12 |
| 7 | 6435 | 0.5037 | 0.6891 | 12/12 | 12/12 | 6/12 | 6/12 |

**K 增大 → Gini 升高、Entropy 升高**：随着面板规模增大，ASR 分布变得更不均等（Gini 从 0.40→0.50），但信息量也增加（Entropy 从 0.58→0.69），反映更多 judge 各自有不同的脆弱性。

### 2. K_eff 与集中度的相关性

整体中位数相关：**median ρ(K_eff, Gini) = -0.028**，**median ρ(K_eff, Entropy) = +0.061**。方向符合假设但效应极弱，原因是**条件高度分化**：

**假设成立的条件**（异质性攻击——不同 judge ASR 差异大）：
| 条件 | K=7 ρ(K_eff,Gini) | K=7 ρ(K_eff,Entropy) |
|------|-------------------|---------------------|
| mmlu×prompt_injection | **-0.56*** | **+0.55*** |
| mmlu×sycophancy | **-0.56*** | **+0.58*** |
| mmlu×verbosity_bias | **-0.44*** | **+0.49*** |
| mmlu×authority_bias | **-0.42*** | **+0.44*** |
| mmlu×score_manipulation | **-0.25*** | **+0.28*** |
| arc×prompt_injection | **-0.07*** | **+0.06*** |

这些攻击中，个体 judge ASR 方差大（例如 prompt_injection：min=0, max=0.82），高 K_eff 面板包含更多独立 judge，攻击成功更分散。

**假设反转的条件**（同质性攻击——所有 judge ASR 接近）：
| 条件 | K=7 ρ(K_eff,Gini) | K=7 ρ(K_eff,Entropy) |
|------|-------------------|---------------------|
| mmlu×position_bias | **+0.23*** | **-0.17*** |
| arc×position_bias | **+0.88*** | **-0.76*** |
| arc×sycophancy | **+0.25*** | **-0.20*** |
| arc×authority_bias | **+0.42*** | **-0.43*** |
| arc×verbosity_bias | **+0.26*** | **-0.26*** |
| arc×score_manipulation | **+0.23*** | **-0.19*** |

position_bias 是最极端的例子：所有 15 个 judge ASR 都在 0.46-0.83 之间（几乎所有 judge 都被攻破），Gini 极低（~0.06-0.08），K_eff 的变化不影响集中度。

### 3. 假设检验结论

**条件依赖性成立**：
- 对**异质性攻击**（judge 脆弱性差异大，主要是 MMLU 上的 prompt_injection/sycophancy/verbosity_bias/authority_bias），假设**强烈成立**：高 K_eff → 攻击分散（ρ 达 -0.56）
- 对**同质性攻击**（所有 judge 都易受攻击，如 position_bias），假设**不成立甚至反转**：K_eff 无法改善集中度，因为所有 judge 共享同一弱点

### 4. 关键发现

1. **攻击类型决定了 K_eff 的防御机制**：K_eff 的"独立 judge 创造多样攻击面"机制仅在 judge 间存在异质性脆弱性时有效
2. **position_bias 是"共模失效"**：所有 judge 的 ASR 都 ~50%，独立性无法对冲这种系统性弱点
3. **MMLU vs arc_challenge 的不对称**：MMLU 上大多数攻击的 judge ASR 方差更大，K_eff 效应更强；arc_challenge 上多数攻击 ASR 偏低且同质，K_eff 效应弱或反转
4. **Gini 随 K 单调升高**（0.40→0.50），说明更大的面板自然包含更多 ASR 分化的 judge

---
