# analysis phase2 3method results

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_3method_results_20260513T092435_result.json`
- **Structured JSON:** [`075e39e6732ba495a650.json`](../../sessions/07/075e39e6732ba495a650.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。以下是 Phase 2 主实验完整分析。

---

## Phase 2 实验结果：3-method self-iterate (GPT2-125M, 8 代)

### 1. Perplexity (PPL) — 越低越好

| Gen | uncurated | rgds | external_only |
|-----|-----------|------|---------------|
| 0 | 37.10 | 37.09 | 37.04 |
| 1 | 44.89 | 45.36 | 44.29 |
| 2 | 51.32 | 50.51 | 50.12 |
| 3 | 56.25 | 53.82 | 53.55 |
| 4 | 55.88 | 53.97 | 52.27 |
| 5 | 50.08 | **61.75** | 47.37 |
| 6 | 48.25 | **64.12** | 46.11 |
| 7 | 50.28 | **75.07** | **45.51** |

**external_only** gen 3 后 PPL 持续下降（53.55→45.51），出现"自修复"效应。
**rgds** gen 4 后 PPL 爆炸式增长至 75.07——典型 model collapse。

### 2. Rare n-gram ratio — 越高越好（多样性保留）

| Gen | uncurated | rgds | external_only |
|-----|-----------|------|---------------|
| 0 | 0.0290 | 0.0290 | 0.0290 |
| 1 | 0.0192 | 0.0202 | 0.0184 |
| 2 | 0.0139 | 0.0151 | 0.0141 |
| 3 | 0.0118 | 0.0124 | 0.0117 |
| 4 | 0.0102 | 0.0099 | 0.0102 |
| 5 | 0.0099 | 0.0082 | 0.0100 |
| 6 | 0.0094 | **0.0067** | **0.0103** |
| 7 | 0.0090 | **0.0051** | **0.0099** |

**external_only** gen 4 后稳定在 ~0.010，gen 6 甚至回升。
**rgds** 单调下降至 0.0051——多样性崩塌最严重，仅剩 external_only 的一半。

### 3. Selection Ratio（alignment gap 核心指标）

| Gen | rgds | external_only |
|-----|------|---------------|
| 0 | 1.037 | **1.137** |
| 1 | 0.910 | **1.211** |
| 2 | 0.927 | **1.116** |
| 3 | 0.941 | **1.196** |
| 4 | 0.896 | **1.282** |
| 5 | 0.811 | **1.109** |
| 6 | 0.717 | **1.123** |
| 7 | **0.517** | **1.095** |

**external_only 全 8 代 ratio > 1.0**（范围 1.095–1.282），证明外部参考 consistently 偏好高多样性样本。

**rgds 仅 gen 0 > 1.0，随后单调下降至 0.517**——RGDS 在自迭代中逐渐偏好同质化内容，ratio < 1 意味着选出的数据比丢弃的数据**更不多样**。

### 4. Rank Correlation — 越接近 0 越好

| Gen | uncurated | rgds | external_only |
|-----|-----------|------|---------------|
| 0 | -0.023 | -0.012 | +0.003 |
| 4 | -0.035 | -0.048 | -0.017 |
| 7 | **-0.088** (p=0.049) | -0.039 | **+0.011** |

**external_only** 从 +0.003 到 +0.011，几乎无分布漂移。
**uncurated** 漂移至 -0.088（已达统计显著），分布系统性偏移。

### 5. RankMe & k-NN

- **k-NN accuracy**：三种方法全部 0.988，无区分度。
- **RankMe**：三者 gen 7 收敛至 290–293，区分度低。uncurated 早期最高（303），但最终无优势。

---

## 核心结论

| 维度 | 排名 | 说明 |
|------|------|------|
| PPL 稳定性 | external_only >> uncurated >> rgds | external_only 自修复，rgds 崩塌 |
| 多样性保留 | external_only > uncurated >> rgds | rgds 仅存 uncurated 57%、external_only 52% 的多样性 |
| Selection ratio | external_only 全程 >1.0 | rgds 从 1.04 崩至 0.52 |
| 分布漂移 | external_only ≈ 0 < rgds < uncurated | uncurated 漂移最大且显著 |

**三条关键发现：**

1. **RGDS 在 self-iterate 中有害**——验证 D008 结论。因为 RGDS 的参考分布来自模型自身（随代数退化），导致 selection ratio 单调下降，主动选出低多样性数据，加速崩塌。

2. **external_only 是唯一能抑制多样性崩塌的方法**——外部锚点（real data embedding）不随迭代退化，selection ratio 全程 > 1.0，rare n-gram 稳定在 0.010，PPL 在后期反而改善。

3. **uncurated 表现居中**——不做任何选择，多样性仍缓慢衰减，但不如 rgds 那样灾难性崩塌。这说明"不选择"优于"错误的选择"。

---
