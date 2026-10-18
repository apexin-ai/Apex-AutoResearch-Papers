# research literature linkage depth extension

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-linkage-depth-extension_20260515T051604_result.json`
- **Structured JSON:** [`229588d2123d16e13e1b.json`](../../sessions/22/229588d2123d16e13e1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据足够，开始整理报告。

---

## 文献联动报告：Depth Extension (d4-d5) 实验

### 一、现有 map 中可直接对比的论文

| 论文 | 测试代数 | 任务/指标 | 与我们的对比点 |
|------|----------|-----------|---------------|
| **shumailov2024_nature** | ~9代（部分实验40代） | perplexity 单调递增 | 测collapse程度，**不做代际分类**。仅用标准采样(T=1)，无策略对比 |
| **drayson2025** | 99代 (GPT-2, SmolLM2) | 多样性下降、perplexity退化 | τ=0.9 最repetitive。**二分类检测**（合成vs真实），不做深度估计 |
| **dohmatob2024_tale_of_tails** | 理论分析 | tail narrowing vs tail cutting | 提供 temp/top-p 产生不同统计指纹的理论解释，**无实验代际分类** |
| **marchi2024_heat_death** | 理论证明（渐近） | T≠1 → 退化 | 支持τ=0.9加速收敛的发现，**无有限代数实验** |
| **editlens2026** | 单次编辑 | 编辑程度连续分数 | 最近的概念邻居（超越二分类），但只看**单次**编辑，不涉及多代递归 |
| **diveye2026** | 二分类 | surprisal diversity特征 | 特征体系有重叠，但**仅二分类**，不做序数深度 |

**关键发现：map 中没有任何论文做过 d4/d5 级别的代际分类实验。** 绝大多数工作要么是理论分析，要么是二分类检测（human vs. machine），要么是测量 aggregate degradation（perplexity/diversity 随代数变化曲线），但从不试图区分相邻代（d3 vs d4 vs d5）。

### 二、新发现的相关论文

**1. "LLM as a Broken Telephone: Iterative Generation Distorts Information"**
- 作者：Mohamed, Geng, Vazirgiannis, Shang
- 发表：ACL 2025
- arXiv: 2502.20258
- 相关性：**中等**。研究迭代生成中的信息失真累积（翻译/改写链），证明失真随迭代单调增长。但任务是翻译链而非递归训练，不做深度分类。
- 对我们的价值：支持"迭代信号可累积"的论点，可在 discussion 中引用作为跨任务佐证。

**2. SIGMA: Scalable Spectral Insights for LLM Model Collapse**
- arXiv: 2601.03385 (2026)
- 相关性：**高**。用 Gram 矩阵谱分析量化 50 代递归训练中的表征空间收缩。提出 Sigma-UB 指标追踪几何退化。
- 对我们的价值：**如果我们的 EDD≥5，SIGMA 的谱分析可作为互补证据**——他们测量表征空间收缩，我们测量可区分性。两个不同视角看同一现象。且 SIGMA 测了 50 代，但不做分类——他们只追踪指标变化趋势。可在 discussion 中引用。

**3. "Model Collapse Does Not Mean What You Think" (Position paper)**
- arXiv: 2503.03150 (2025)
- 相关性：**低-中**。澄清 model collapse 概念，区分不同类型退化。可用于精确定义我们的"depth signal"与"collapse"的关系。

### 三、Novelty 评估：若 EDD≥5

**评分：4/5（强 novelty）**

理由：

1. **任务层面的唯一性**：文献中**没有人**将递归生成深度估计作为序数分类问题。现有工作全部停留在二分类（human vs. machine）或 aggregate 统计趋势观察。我们的 EDD 指标本身就是新定义。

2. **深度范围的突破**：大多数实证工作的分类/检测仅涉及 d0-d1（真实 vs. 单次生成）。即便 Shumailov 跑了 9-40 代，也只报告 perplexity 曲线，不做相邻代区分。证明 d4 vs d5 仍然可区分（AUC > 阈值）在文献中无先例。

3. **未达满分的原因**：
   - Shumailov/Drayson/SIGMA 都间接暗示深代信号存在（perplexity/多样性/谱指标持续变化到很高代数），只是没人做过分类验证
   - 如果 EDD=5 但 accuracy 显著下降（比如从 d3 的 80% 降到 d5 的 60%），novelty 会稍弱——说明信号在衰减，只是还未消失
   - 若 EDD≥5 且 accuracy 保持稳定（~70%+），则 novelty 可上调至 4.5/5

### 四、建议补充到 literature_map 的论文

| 建议 key | 论文 | cite_in | 理由 |
|----------|------|---------|------|
| `mohamed2025_broken_telephone` | LLM as a Broken Telephone (ACL 2025) | discussion | 跨任务佐证迭代信号累积 |
| `sigma2026_spectral` | SIGMA: Spectral Insights for Model Collapse (2026) | discussion, related-work | 50代谱分析，互补视角 |

（待你确认后再修改 yaml）

Sources:
- [LLM as a Broken Telephone (ACL 2025)](https://aclanthology.org/2025.acl-long.371/)
- [SIGMA: Scalable Spectral Insights for LLM Model Collapse](https://arxiv.org/abs/2601.03385)
- [Model Collapse Does Not Mean What You Think](https://arxiv.org/abs/2503.03150)
- [Shumailov et al. Nature 2024](https://www.nature.com/articles/s41586-024-07566-y)
- [Drayson et al. 2025](https://arxiv.org/abs/2502.15654)

---
