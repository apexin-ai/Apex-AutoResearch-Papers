# Citation Verification Report
> 验证时间: 2026-05-18
> 验证方法: WebSearch + WebFetch (arXiv abs + HTML full text + OpenReview)

## 验证结果摘要

| # | 论文 | arXiv/URL | 状态 | 说明 |
|---|------|-----------|------|------|
| 1 | IRC | 2604.02869 | ✅ verified | 论文存在，Table 1 A^I/A^O 方向不一致和 14pp 下降均确认 |
| 2 | MC-GRPO | 2601.22582 | ✅ verified | 论文存在，"5% sign-flip → ~4% accuracy drop" 原文原话 |
| 3 | G-RA | 2508.10548 | ✅ verified | 论文存在，sign divergence 和 47.6%→1.4% 均确认 |
| 4 | GRPO-λ | 2510.00194 | ⚠️ partially accurate | Lemma 1 存在但内容是 value difference bound，非直接关于 "normalized advantage bias"；未使用 "systematic misattribution" 术语 |
| 5 | OAR | 2601.07408 | ⚠️ partially accurate | 论文存在，但未使用 "advantage misattribution" 术语，实际用 "coarse-grained credit assignment" 和 "reward aliasing" |
| 6 | Decoupled Credit | OpenReview Suja4AQ9Fo | ⚠️ partially accurate | 论文存在，内容匹配，但状态为 ICLR 2026 under review（非已录用） |
| 7 | GiGPO | 2505.10978 | ✅ verified | ALFWorld 86.1% vs GRPO 72.8%，step/episode ablation，NeurIPS 2025 均确认 |
| 8 | RAGEN | 2504.20073 | ⚠️ partially accurate | Echo Trap 确认，但 "20/10 步 collapse" 与原文不符（实际 collapse 在 training step 170/110 附近） |

**总结: 0 篇 hallucinated，4 篇完全准确，4 篇部分准确需修正引用措辞**

---

## 逐篇详细验证

### 1. IRC (arXiv 2604.02869)

- **搜索结果**: arXiv 页面存在，标题完全匹配
- **标题匹配**: ✅ "Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration"
- **内容匹配**: ✅
- **结论**: ✅ verified
- **详细说明**:
  - Table 1 确认存在，展示不同 action tier 下 A^I 和 A^I+A^O 的方向对比
  - 原文 Table 1 数据：Gold exact (+1.22/+1.22, aligned)，Soft match (+0.11/−0.11, misaligned)，Read-only (+0.05/−0.65, misaligned)
  - A^I（per-turn advantage）和 A^O（outcome advantage）的符号体系确认
  - 14pp 性能下降确认：原文 "dense rewards (V5) produced a 14pp degradation on Tau2-Bench compared to sparse rewards (V3): 54% vs. 68%"
  - 关于 "6.5pp"：未在 abstract/HTML 中找到这个确切数字。Table 1 中 read-only tier 的 A^I+A^O = −0.65（非 6.5pp）。建议核实此数字来源

### 2. MC-GRPO (arXiv 2601.22582)

- **搜索结果**: arXiv 页面存在，标题完全匹配
- **标题匹配**: ✅ "MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning"
- **内容匹配**: ✅
- **结论**: ✅ verified
- **详细说明**:
  - 原文明确声称 "even a 5% sign-flip rate induces a ~4% accuracy drop"，与我们的引用完全一致
  - GSM8K 结果确认：GRPO G=2 78.92% → MC-GRPO 83.54% (+4.62%)
  - Figure 3 展示了 controlled sign-flip injection 实验，证明因果关系
  - 作者：Youngeun Kim

### 3. G-RA (arXiv 2508.10548)

- **搜索结果**: arXiv 页面存在，标题完全匹配
- **标题匹配**: ✅ "Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards"
- **内容匹配**: ✅
- **结论**: ✅ verified
- **详细说明**:
  - Figure 3 确认展示 D-RA (Direct Reward Accumulation) 训练中 accumulated reward 与 outcome reward 的反向变化
  - 原文："accumulated reward keeps increasing during RL training, while the outcome reward is negatively correlated with the accumulated reward"（sign divergence 确认）
  - 47.6% → 1.4% completion rate collapse 确认：SFT baseline 47.6%，D-RA 100 steps 后降至 1.4%
  - 应用领域为 SWE tasks（SWE-bench），非一般 agentic tasks

### 4. GRPO-λ (arXiv 2510.00194)

- **搜索结果**: arXiv 页面存在，标题完全匹配
- **标题匹配**: ✅ "GRPO-λ: Credit Assignment improves LLM Reasoning"
- **内容匹配**: ⚠️ 部分准确
- **结论**: ⚠️ partially accurate
- **详细说明**:
  - Lemma 1 存在，但内容是关于 value difference bound：ΔV(s_t) = V(s_0) - V(s_t) <= 1 - prod_{k=0}^{t-1} sum_{a_k != a_EOS} pi_theta(a_k|s_k)
  - 论文确实讨论了 GRPO baseline 对非初始状态的偏差："GRPO's baseline mu_t only estimates the expected return when t=0, and is a biased estimate for all t>0"
  - 但 Lemma 1 本身不是直接关于 "normalized advantage estimation has increasing bias"，而是关于 value difference bound
  - 论文未使用 "systematic misattribution" 术语，使用的是 "bias"、"biased estimate"、"inaccurate estimates"
  - **建议修正**: 引用时应写 "Lemma 1 bounds the value estimation error that grows with sequence position" 而非 "proves normalized advantage estimation is increasingly biased for subsequent tokens"；删除 "systematic misattribution" 措辞

### 5. Outcome-Grounded Reshaping / OAR (arXiv 2601.07408)

- **搜索结果**: arXiv 页面存在，标题完全匹配
- **标题匹配**: ✅ "Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning"
- **内容匹配**: ⚠️ 部分准确
- **结论**: ⚠️ partially accurate
- **详细说明**:
  - 全文搜索确认：**"advantage misattribution" 一词不存在于论文中**
  - **"misattribution" 一词也不存在**
  - 论文实际使用的术语：
    - "coarse-grained credit assignment"（粗粒度信用分配）
    - "reward aliasing"（奖励混叠）
    - "mismatch between coarse sequence-level credit assignment and the desired token-level reallocation"
  - **建议修正**: 不应声称 OAR 将问题命名为 "advantage misattribution"。应改为 "OAR identifies the problem as 'reward aliasing' arising from coarse-grained credit assignment"

### 6. Decoupled Credit Assignment (OpenReview Suja4AQ9Fo)

- **搜索结果**: OpenReview 页面存在，标题完全匹配
- **标题匹配**: ✅ "Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning"
- **内容匹配**: ⚠️ 部分准确
- **结论**: ⚠️ partially accurate
- **详细说明**:
  - Invalid actions 在 positive trajectories 中被分配 positive credit：✅ 确认
  - Multiplicative Gated Rewards (MGR)：✅ 确认
  - 作者：Wenxuan Lu, Zhanqiu Zhang, Steven Y. Guo, Tianning Zang
  - **但 ICLR 2026 状态需修正**：提交于 2025-09-19，修改于 2026-02-11，当前状态为 **under review**（在审），非已录用
  - **建议修正**: 引用时注明 "(under review)" 或改用 "submitted to ICLR 2026"，不可写 "(ICLR 2026)" 暗示已录用

### 7. GiGPO (arXiv 2505.10978)

- **搜索结果**: arXiv 页面存在，NeurIPS 2025 poster 页面存在（neurips.cc/virtual/2025/poster/118123）
- **标题匹配**: ✅ "Group-in-Group Policy Optimization for LLM Agent Training"
- **内容匹配**: ✅
- **结论**: ✅ verified
- **详细说明**:
  - ALFWorld 86.1% vs GRPO 72.8% (+13.3pp)：✅ Table 1 确认，原文 "surpasses GRPO by 13.3% on ALFWorld"
  - Step vs episode ablation：✅ Section 5.4 + Figure 4 确认，含 GiGPO_{w/o A^S} 和 GiGPO_{w/o A^E} 对比
  - NeurIPS 2025：✅ 确认（arXiv Comments: "NeurIPS 2025"，neurips.cc poster 页面存在）
  - 作者：Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An

### 8. RAGEN Echo Trap (arXiv 2504.20073)

- **搜索结果**: arXiv 页面存在，标题完全匹配
- **标题匹配**: ✅ "RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning"
- **内容匹配**: ⚠️ 部分准确
- **结论**: ⚠️ partially accurate
- **详细说明**:
  - Echo Trap 现象：✅ 确认，定义为 "agents overfit to locally rewarded reasoning patterns, marked by reward variability collapse, entropy drop, and gradient spikes"
  - GRPO 在 Bandit/Sokoban 上 collapse：✅ 确认
  - **但 "20/10 步 collapse" 与原文不符**：
    - Bandit: gradient norm spike 出现在 training step ~170，非 20 步
    - Sokoban: collapse 出现在 training step ~110，reward std 早期（step ~10）即开始下降
    - "20/10" 可能指环境的 max episode length（Bandit 20 turns，Sokoban 10 turns），非 training step 到 collapse 的步数
  - **建议修正**: 明确区分 environment interaction steps 和 training steps。若指 episode length 应改为 "with 20/10-turn episodes"；若指 collapse 时间点，需改为实际 training step 数

---

## 需修正项汇总

| # | 论文 | 问题 | 修正建议 |
|---|------|------|----------|
| 1 | IRC | "6.5pp" 数字未找到确切来源 | 核实是否为 14pp 范围的下界或其他表格数据 |
| 4 | GRPO-λ | Lemma 1 内容描述不够精确；使用了论文中不存在的 "systematic misattribution" 术语 | 改为 "Lemma 1 bounds value estimation error growing with position"；删除 "systematic misattribution" |
| 5 | OAR | 论文不使用 "advantage misattribution" 术语 | 改为 "identifies 'reward aliasing' from coarse-grained credit assignment" |
| 6 | Decoupled Credit | ICLR 2026 under review，非已录用 | 标注 "(under review)" 或 "submitted to ICLR 2026" |
| 8 | RAGEN | "20/10 步 collapse" 含义不清/不准确 | 明确是 episode length 还是 training steps，修正为准确数字 |
