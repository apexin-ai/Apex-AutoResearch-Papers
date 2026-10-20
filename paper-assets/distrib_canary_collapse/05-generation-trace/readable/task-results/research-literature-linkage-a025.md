# research literature linkage a025

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-linkage-a025_20260515T042907_result.json`
- **Structured JSON:** [`8c1fa48918935737c1c1.json`](../../sessions/8c/8c1fa48918935737c1c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 文献联动分析报告

### 1. 我们的相变发现在文献中的位置

**与 chen2025scales 高度一致**：他们报告 ≤20% 稳定、≥30% 加速退化。我们的 α=0.25 恰好落在其 20-30% 过渡带内，从 canary 指标层面独立验证了这个阈值区间的存在。但 Chen 等人只看 task performance 和 calibration，没有分析 distinct-n 级别的 diversity collapse——我们的 13× 加速（distinct_3）是全新的粒度。

**与 dohmatob2025strong 不矛盾**：Dohmatob 的"1/1000 也导致 collapse"是在 scaling law 框架下的理论结论（线性回归 + 随机特征映射），指的是"增加数据量不再提升性能"。我们 α=0.00 下的 drift（distinct_1 -13.8%）来自 fine-tuning 本身的 distributional shift，不是 synthetic contamination。两个发现度量的是不同层面的现象：Dohmatob 关注 asymptotic scaling breakdown，我们关注 finite-step canary drift 的非线性加速。

### 2. 可能遗漏的文献

| ID | Title | URL | Key Findings | 与我们的关系 |
|---|---|---|---|---|
| gambetta2024surplexity | Learning by Surprise: Surplexity for Mitigating Model Collapse | [arXiv 2410.12341](https://arxiv.org/abs/2410.12341) | 用 semantic network + next-token probability 表征 collapse；分析了 synthetic token 比例对 collapse 严重度的影响 | **直接相关**——他们也研究了 synthetic 比例对 diversity 的影响，但没有识别出非线性相变或 canary 指标的差异化响应 |
| schaeffer2025position | Position: Model Collapse Does Not Mean What You Think | [arXiv 2503.03150](https://arxiv.org/abs/2503.03150) | 指出 model collapse 有 8 种互相冲突的定义；认为多数 collapse 场景可避免 | **框架性参考**——我们应在论文中明确定义所度量的 collapse 类型，避免歧义 |
| yi2025escaping | Escaping Model Collapse via Synthetic Data Verification | [arXiv 2510.16657](https://arxiv.org/abs/2510.16657) | 通过 verifier 过滤合成数据可逆转 collapse 趋势 | 间接相关——mitigation 方向，非竞争者 |
| gerstgrasser2024accumulate | Is Model Collapse Inevitable? | [arXiv 2404.01413](https://arxiv.org/abs/2404.01413) | replace 场景 collapse、accumulate 场景稳定 | 间接相关——我们的 iterative 设定是 replace 场景 |

**建议优先加入 literature_map**：gambetta2024surplexity（最直接的方法论竞争者）和 schaeffer2025position（定义框架）。

### 3. Novelty 判断

**这个非线性相变发现增强了我们的 novelty。** 理由：

- Chen2025 在 task performance/ECE 层面观察到 20-30% 阈值，但没有下沉到 distinct-n canary 级别
- Gambetta2024 分析了 synthetic 比例的影响，但没有映射出 α-regime 边界或识别指标间的差异化响应
- 没有任何现有工作报告过：**同一 α 变化下，distinct_3 加速 13× 而 token entropy 几乎不变**——这种 canary 指标的分层响应模式是全新的
- 我们的 Granger causality + 多指标 panel + α-regime map 组合在文献中无先例

核心 selling point：**不是"发现了 collapse"（所有人都知道），而是"在 canary 层面精确刻画了 collapse 的相变边界和指标分层响应"**。

Sources:
- [Chen et al. 2025 - Characterizing Model Behavior Under Synthetic Data Training](https://arxiv.org/abs/2510.05133)
- [Dohmatob et al. 2025 - Strong Model Collapse (ICLR 2025)](https://arxiv.org/abs/2410.04840)
- [He et al. 2025 - A Closer Look at Model Collapse (NeurIPS 2025)](https://arxiv.org/abs/2509.16499)
- [Gambetta et al. 2024 - Learning by Surprise: Surplexity](https://arxiv.org/abs/2410.12341)
- [Schaeffer et al. 2025 - Position: Model Collapse Does Not Mean What You Think](https://arxiv.org/abs/2503.03150)
- [Yi et al. 2025 - Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)
- [Gerstgrasser et al. 2024 - Is Model Collapse Inevitable?](https://arxiv.org/abs/2404.01413)

---
