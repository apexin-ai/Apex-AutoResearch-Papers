# Reviewer 2 coordination — Part 2 of 2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/5f/5f192c79fe2bd57ee0e6.json)

## Round 16

### Tool result

_source line 525 · 2026-05-25T21:19:11.930427+00:00_

1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=0.85\textwidth]{fig_overview.pdf}
4	\caption{Step-independent windowing (left) partitions the trajectory into fixed windows, each optimized independently. This introduces two failure mechanisms: M1 (information loss) truncates context at window boundaries, and M2 (sign misattribution) assigns all windows the same advantage sign based on episode outcome. Episode-level training (right) treats the full trajectory as a single sample, eliminating both mechanisms.}
5	\label{fig:overview}
6	\end{figure*}
7	
8	\section{Introduction}
9	\label{sec:introduction}
10	
11	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\citep{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\citep{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\citep{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern (decomposing trajectories into fixed-size windows, each optimized independently) and frequently report training instability without diagnosing its root cause.
12	
13	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Preliminary comparisons suggest that standard remedies (dense reward shaping, discount tuning) do not resolve the pathology (Appendix~\ref{app:additional}). Concurrent methods that improve per-step credit quality (GiGPO~
…[truncated 2706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-25T21:19:15.894638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-25T21:19:16.196394+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation and GRPO}
5	\label{sec:problem_formulation}
6	
7	We model the multi-turn agent as a partially observable Markov decision process (POMDP)~\citep{kaelbling1998planning} where the policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on interaction history $h_t = (o_1, a_1, \ldots, o_t)$. Episodes of $T$ steps terminate with binary reward $R \in \{0, r_+\}$ (our experiments use a penalty variant with $r_- = -0.1$ per invalid action; Section~\ref{sec:setup}). GRPO~\citep{shao2024deepseekmath} samples $K$ rollouts per task and computes group-relative advantages:
8	\begin{align}
9	\hat{A}_k &= \frac{R_k - \mu}{\sigma + \epsilon}, \notag \\
10	\mu &= \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
11	\label{eq:grpo_advantage}
12	\end{align}
13	GRPO is episode-level by design: each rollout receives one return and one advantage, with no inherent temporal discounting.
14	
15	\subsection{Step-Independent Windowing}
16	\label{sec:step_independent}
17	
18	Agent RL frameworks must reconcile GRPO's episode-level design with the memory constraints of long trajectories. RAGEN~\citep{ragen2025} introduces \textbf{step-independent training}: the trajectory is partitioned into non-overlapping $h$-step windows, each receiving a discounted return:
19	\begin{equation}
20	R_w = \gamma^{(N - w)} \cdot R_{\text{episode}}
21	\label{eq:step_return}
22	\end{equation}
23	where $w \in \{1, \ldots, N\}$ indexes windows and $N = \lceil T/h \rceil$ is the number of windows. Each window is optimized as an independent GRPO sample. This reduces sequence length from $O(T)$ to $O(h)$ and multiplies the effective batch size, but structurally alters credit assignment.
24	
25	\subsection{Dual Mechanism Analysis}
26	\label{sec:dual_mechanism}
27	
28	Two mechanisms jointly cause training failure under step-independent optimization.
29	
30	\subsubsection{Mechanism 1: Policy Information 
…[truncated 3515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-25T21:19:16.196801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-25T21:19:16.297461+00:00_

1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Sign misattribution is the more fundamental failure mechanism because it causes active divergence, not merely slow convergence. We derive the probability of incorrect gradient direction below; full proofs appear in Appendix~\ref{app:theory_full}.
5	
6	\textbf{Definition 1} (Locally correct action). \textit{An action $a_t$ is \textbf{locally correct} if it would receive positive advantage under an oracle that observes the full episode history $h_t$ and has access to the true action-value function. Equivalently,\footnote{This equivalence is approximate; it holds exactly when all trajectories within an episode are equally likely under the reference policy, and approximately under the mild assumption that policy drift remains small during early training. This approximation is most accurate when the policy has not yet diverged significantly from initialization (here, $p \approx 12.5\%$); at higher success rates, the bound may loosen.} window $w$ contains locally correct actions if replacing them (holding all other windows fixed) would decrease the probability of episode success.}
7	
8	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $w$'s advantage $\hat{A}_w$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
9	
10	\textit{Proof sketch.} In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_w = 0$. If any rollout in the group succeeded, $\mu > 0$, so every window in the failed episode receives $\hat{A}_w < 0$, including windows with locally correct actions. The probability of receiving the wrong sign in a failed episode is $1 - (1-p)^{K-1}$ (at least one group member succeeded). As $K$ grows, this approaches $1-p$, and the overall probability of correct sign approaches $p$. \hfill$\square$
11	
12	
…[truncated 5230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-25T21:22:22.966983+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Full Review\n\n**论文标题**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction\n**Venue**: EMNLP 2026 via ARR May 2026\n\n---\n\n## Summary\n\n本文诊断了 step-independent agent RL 训练中的两个失败机制：策略信息丢失（M1，上下文截断导致性能上限）和优势符号误归因（M2，group normalization 在 binary reward 下使梯度符号反映 episode 结果而非局部动作质量）。通过 2×2 部分析因实验分离两个机制的贡献，并提出 episode-level GRPO 作为结构性修复。诊断框架设计合理、实验方法学规范，但所提出的\"修复\"方法新颖性有限（本质是恢复标准 GRPO），且高 seed 变异性（仅 36% seed 泛化）削弱了实际影响力。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 — Findings\n\n**一句话总结**: 诊断贡献清晰且方法学规范，但 episode-level GRPO 缺乏方法论新颖性，实验范围偏窄且结果 seed 依赖严重，达不到主会议接收标准，适合 Findings。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0/5 | 理论分析在其假设内成立，但 binary theory 与 ternary 实际设定之间的 gap 未充分 bridge；Cell C 缺失削弱析因完整性；episode-level 评估因 seed 依赖而不稳定 |\n| **Excitement** | 2.5/5 | 诊断视角对社区有参考价值，但洞察本身在陈述后显得直觉性强；所提方案（恢复标准 GRPO）缺乏新颖性；实际影响受限于 seed 依赖 |\n| **Overall Assessment** | 3.0/5 | Findings 水平——诊断贡献有价值，实验方法学规范，诚实报告值得肯定，但新颖性不足、实验范围偏窄 |\n| **Confidence** | 4/5 | 对 agent RL、GRPO 及同期工作较为熟悉 |\n| **Reproducibility** | 4/5 | 提供匿名代码链接，超参数明确，但部分配置细节不全（如 Cell B 只有单 seed 评估） |\n\n---\n\n## Strengths\n\n**S1: 精心设计的部分析因实验。** 2×2 factorial（Cells A/B/C/D）通过 A→B（隔离 M2）和 B→D（隔离 M1）的对比，干净地分离了各机制的贡献（Section 3.5, Section 5.2-5.3）。这是严谨的实验方法学，在 agent RL 文献中较为少见。\n\n**S2: 科学诚实的报告标准。** 论文没有隐藏 36% 泛化率（Table 2）、seed 变异性（Figure 5）、Cell C 不稳定性（Section 5.2）或单次评估的局限（Limitations）。这种透明度在当前 agent RL 文献中值得表扬。\n\n**S3: 理论与实验的对照验证。** Propositions 1-2 给出了梯度符号正确性的形式化上界，Section 5.4 的三项指标（sign-episode correlation 99.6%, credit agreement 52.1%, P(correct|update) ≤19.1%）分别从不同角度验证了理论预测。特别是 break-even magnitude ratio 分析（实测 2.6 vs 理论需要 4.2, Section 5.4 最后一段）很有洞察力。\n\n**S4: 清晰的写作和可视化。** Figure 1 高效地解释了两个机制的区别；Figure 3 的训练动态图直观展示了析因结果；整体逻辑流畅从诊断到理论到实验。\n\n**S5: 跨环境和跨规模验证。** 8B 实验和 ScienceWorld 实验（Section 5.6）虽然是单 seed，但提供了 pathology 并非 ALFWorld/1.7B 特有的初步证据。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**W1** [critical] **Episode-level GRPO 的方法论新颖性极为有限**\n- 具体位置：Section 3.4\n- 问题：所提出的\"修复\"本质上是恢复 GRPO 的原始设计——将整个 episode 作为一个样本优化。论文自身明确承认：\"This restores GRPO's original per-sample granularity to the episode level; step-independent windowing is the deviation introduced by multi-turn agent frameworks.\"（Section 3.4）。换言之，\"新方法\"是\"不要使用 RAGEN 引入的 step-independent decomposition\"，这是一个设计选择的回退而非方法论创新。\n- 为什么影响接收：对于一篇以 \"Episode-Level Correction\" 作为标题核心部分的论文，解决方案的技术贡献需要达到一定门槛。本文将自身定位为\"primarily diagnostic\"，这是合理的策略，但即使如此，诊断类论文通常也需要提出具有独立价值的解决方案或 actionable insights 超越\"不要这样做\"。\n- 建议修改方向：（1）将标题和 framing 更彻底地聚焦于诊断贡献本身，降低对 episode-level GRPO 作为\"correction\"的强调；（2）或者在 episode-level 基础上加入真正的改进（例如解决 seed 依赖问题的机制），使方法论贡献实质化。\n\n**W2** [critical] **Abstract/Introduction 的 claims 与实验证据之间存在 overclaiming**\n- 具体位置：Abstract, Section 1\n- 问题：\n  - Abstract 称 \"structurally eliminates both failure modes\"——技术上正确，但在仅 36% seed 泛化的语境下具有误导性。一个 structurally 消除了失败模式的方法不应在 64% 的 seed 上停滞或坍塌。\n  - Introduction 称 \"achieving substantial OOD improvement where step-independent collapses to 0%\"——17.7% 均值被 4 个泛化 seed 显著拉高。Table 2 显示 7/11 seed 的 OOD 成绩与 SFT baseline（6.72%）无统计显著差异，**中位数**应远低于均值。\n  - 8B 结果 90.3% OOD 被呈现为\"cross-scale verification\"但仅为单 seed——在 1.7B 已证明强 seed 依赖的前提下，单 seed 8B 结果的证据强度极弱。\n- 为什么影响接收：overclaiming 是审稿中的重大问题。论文在 Limitations 中诚实承认了这些限制，但 abstract 和 introduction 的 framing 仍然给读者留下了过于乐观的第一印象。\n- 建议修改方向：（1）在 abstract 中报告中位数而非均值；（2）将 \"structurally eliminates\" 改为更谨慎的表述如 \"structurally removes the conditions for\"；（3）将 8B 结果明确标注为\"preliminary single-seed evidence\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W3** [warning] **不完整的析因设计削弱了核心分离声明**\n- 具体位置：Section 3.5, Section 5.2\n- 问题：Cell C（full trajectory + step-level advantage，仅 M2 active）在 6 组超参数下均出现 NaN 发散，导致 2×2 设计缺失一个关键 cell。论文无法展示 M2 在没有 M1 的情况下单独的效果。Discussion 承认\"our factorial interpretation assumes approximate separability\"（Section 6），但 Introduction 的 Contribution 2 仍称之为 \"controlled empirical separation\"，且 Cell C 的发散可能暗示一个第三机制：M1 的信息截断可能无意中通过限制梯度方差来\"稳定\"训练（Discussion 中提到但未深入分析）。\n- 建议：（1）在 Contribution 2 中更明确地标注析因是 partial（3-of-4）；（2）对 Cell C 的发散进行更深入的分析——它是否代表了 M1/M2 框架之外的独立现象？\n\n**W4** [warning] **实验范围相对于 claims 偏窄**\n- 具体位置：Section 5, Limitations\n- 问题：\n  - 主要评估：单一环境（ALFWorld）、单一规模（1.7B）、6 种任务类型\n  - 8B 验证：单 seed，无 seed 变异数据\n  - ScienceWorld：单 seed，仅展示 collapse（主文未报告 episode-level 对比）\n  - **未与同期方法做 head-to-head 比较**（GiGPO, HCAPO, Turn-PPO 等）——论文以贡献\"正交\"（诊断 vs 解决方案）为由省略，但实证展示诊断框架能正确预测这些方法的相对表现将大幅增强说服力\n  - 所有 OOD 评估为单次 τ=0.4\n- 建议：至少复现一个代表性的同期方法（如 GiGPO）作为 baseline，验证诊断框架的预测能力。\n\n**W5** [warning] **理论分析的假设限制性较强，且与实际实验设定之间存在 gap**\n- 具体位置：Section 4, Section 5.4\n- 问题：\n  - Propositions 1-2 假设 binary reward，但实际实验使用 ternary reward（r ∈ {−0.1, 0, 1}）\n  - Definition 1（locally correct action）的等价性是近似的（脚注 2 承认）\n  - 上界仅在\"episode success implies all constituent windows are locally correct\"时 tight——这是一个强假设\n  - Ternary reward 下实测 credit agreement 52.1% 与 binary bound 19.1% 差距巨大（Section 5.4），说明实际训练动态处于一个与理论分析显著不同的 regime\n- 建议：为 ternary/非 binary reward 场景提供形式化分析或更清楚地讨论理论与实践之间的 gap。\n\n**W6** [warning] **与同期工作的关系停留在声明层面，缺乏实证**\n- 具体位置：Section 2, Section 6\n- 问题：Related Work（Section 2）声称 \"our framework provides a unified explanation for why these finer-grained methods succeed: they eliminate M2\"，Discussion（Section 6）称 HCAPO 和 GiGPO \"succeed with h=2 by eliminating M2 through finer-grained credit, consistent with our framework's prediction\"。但这一核心声明完全未经实证验证。\n- 建议：增加一个分析（表格或图），展示 GiGPO/Turn-PPO/HCAPO 如何映射到 M1/M2 框架，以及框架预测与它们的实际表现是否一致。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** Table 1 中 Cell B 标注 \"Single seed; seed2 best checkpoint unavailable for re-evaluation\"——这意味着 A→B 对比的关键数据只有单 seed 支撑，应更突出说明。\n- **M2** Figure 3(b) 的 window size sweep 中，h=10 的两个 seed 差异巨大（6.25% vs 21.9%），但主文仅报告均值 14.1%，应报告两个 seed 的单独结果。\n- **M3** Section 5.1 提到 \"Qwen3-1.7B fine-tuned on expert demonstrations (SFT baseline: 12.5%)\"——12.5% in-distribution 的 SFT baseline 是否偏低？这可能影响诊断的普适性（在更强的 SFT baseline 上 sign misattribution 的严重程度会不同）。\n- **M4** Equation 2 中 R_w = γ^(N-w) · R_episode——γ 的具体值在主文未给出（Appendix B 中为 0.95），建议在主文中提及。\n- **M5** 论文 AI assistance 声明（page 16）提到使用 Claude，这很好的透明度实践。\n\n---\n\n## Questions\n\n**Q1**: 11 个 seed 的 OOD success rate **中位数**是多少？（相比均值 17.7%，中位数更能反映\"typical\"性能）\n\n**Q2**: 8B 实验（90.3% OOD）尝试了多少个 seed？是唯一的 seed 还是从多个中选出的？在 1.7B 已证明强 seed 依赖的前提下，这个问题直接影响该结果的可信度。\n\n**Q3**: Cell C 的 NaN 发散是否可能代表了 M1/M2 框架之外的独立现象？论文 Discussion 提到 \"M1 may unintentionally stabilize training by limiting gradient variance\"——这是否暗示 M1 除了是\"failure mechanism\"外，还起到了某种正则化作用？如果是这样，M1/M2 作为两个独立失败机制的框架是否需要修正？\n\n**Q4**: 理论分析给出 binary 下 P(correct|update) ≤ 19.1%，但实际 ternary 设定下 credit agreement 为 52.1%（Section 5.4）。哪个 regime 更准确地描述了实际训练动态？binary bound 能否有意义地预测 ternary 设定下的行为？\n\n**Q5**: 是否考虑过在具有更密 reward 信号的环境中评估（如中间步骤的 partial reward），以测试 M2 机制的边界条件？\n\n**Q6**: Appendix D 中 REINFORCE++ 实验显示 per-token normalization 不帮助——能否进一步分析为什么？这对理解 sign misattribution 的根本原因（是 normalization 方式还是 reward sparsity）有重要意义。\n\n---\n\n## Missing References\n\n以下相关工作可能被遗漏或值得讨论：\n\n1. **RLOO** (Ahmadian et al., 2024, \"Back to Basics: Revisiting REINFORCE-Style Optimization for Learning from Human Feedback in LLMs\") — 提出 REINFORCE Leave-One-Out baseline，与 GRPO 的 group normalization 直接相关，处理类似的 variance 问题。\n2. **合作多智能体 RL 的 credit assignment 文献** — Appendix A.4 提到了多智能体类比，但未引用标准文献如 COMA (Foerster et al., 2018) 或 QMIX (Rashid et al., 2020)，这些工作直接处理了\"shared team reward → individual credit\"的问题，与本文的核心问题高度相关。\n\n---\n\n## 主要优势总结\n\n1. 干净的析因实验设计是本文最大亮点，为 agent RL 社区提供了方法学模板\n2. 理论与实验的对照验证增强了诊断的可信度\n3. 科学诚实的报告标准——包括负面结果（Cell C 失败、seed 依赖）——值得鼓励\n4. 写作质量整体较高，结构清晰\n\n## 总体判断\n\n本文的核心贡献是诊断性的，这个定位是合理且有价值的。但两个关键问题制约了评分：（1）解决方案缺乏独立的方法论价值——episode-level GRPO 本质上是\"恢复默认设置\"；（2）实验范围偏窄且结果强 seed 依赖，削弱了诊断的普适性声明。论文在诚实度和方法学严谨性上表现出色，适合作为 Findings 发表以供社区参考，但未达到主会议接收的新颖性和影响力门槛。\n",
  "reviewer_id": "2",
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Full Review\n\n**论文标题**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction\n**Venue**: EMNLP 2026 via ARR May 2026\n\n---\n\n## Summary\n\n本文诊断了 step-independent agent RL 训练中的两个失败机制：策略信息丢失（M1，上下文截断导致性能上限）和优势符号误归因（M2，group normalization 在 binary reward 下使梯度符号反映 episode 结果而非局部动作质量）。通过 2×2 部分析因实验分离两个机制的贡献，并提出 episode-level GRPO 作为结构性修复。诊断框架设计合理、实验方法学规范，但所提出的\"修复\"方法新颖性有限（本质是恢复标准 GRPO），且高 seed 变异性（仅 36% seed 泛化）削弱了实际影响力。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 — Findings\n\n**一句话总结**: 诊断贡献清晰且方法学规范，但 episode-level GRPO 缺乏方法论新颖性，实验范围偏窄且结果 seed 依赖严重，达不到主会议接收标准，适合 Findings。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0/5 | 理论分析在其假设内成立，但 binary theory 与 ternary 实际设定之间的 gap 未充分 bridge；Cell C 缺失削弱析因完整性；episode-level 评估因 seed 依赖而不稳定 |\n| **Excitement** | 2.5/5 | 诊断视角对社区有参考价值，但洞察本身在陈述后显得直觉性强；所提方案（恢复标准 GRPO）缺乏新颖性；实际影响受限于 seed 依赖 |\n| **Overall Assessment** | 3.0/5 | Findings 水平——诊断贡献有价值，实验方法学规范，诚实报告值得肯定，但新颖性不足、实验范围偏窄 |\n| **Confidence** | 4/5 | 对 agent RL、GRPO 及同期工作较为熟悉 |\n| **Reproducibility** | 4/5 | 提供匿名代码链接，超参数明确，但部分配置细节不全（如 Cell B 只有单 seed 评估） |\n\n---\n\n## Strengths\n\n**S1: 精心设计的部分析因实验。** 2×2 factorial（Cells A/B/C/D）通过 A→B（隔离 M2）和 B→D（隔离 M1）的对比，干净地分离了各机制的贡献（Section 3.5, Section 5.2-5.3）。这是严谨的实验方法学，在 agent RL 文献中较为少见。\n\n**S2: 科学诚实的报告标准。** 论文没有隐藏 36% 泛化率（Table 2）、seed 变异性（Figure 5）、Cell C 不稳定性（Section 5.2）或单次评估的局限（Limitations）。这种透明度在当前 agent RL 文献中值得表扬。\n\n**S3: 理论与实验的对照验证。** Propositions 1-2 给出了梯度符号正确性的形式化上界，Section 5.4 的三项指标（sign-episode correlation 99.6%, credit agreement 52.1%, P(correct|update) ≤19.1%）分别从不同角度验证了理论预测。特别是 break-even magnitude ratio 分析（实测 2.6 vs 理论需要 4.2, Section 5.4 最后一段）很有洞察力。\n\n**S4: 清晰的写作和可视化。** Figure 1 高效地解释了两个机制的区别；Figure 3 的训练动态图直观展示了析因结果；整体逻辑流畅从诊断到理论到实验。\n\n**S5: 跨环境和跨规模验证。** 8B 实验和 ScienceWorld 实验（Section 5.6）虽然是单 seed，但提供了 pathology 并非 ALFWorld/1.7B 特有的初步证据。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**W1** [critical] **Episode-level GRPO 的方法论新颖性极为有限**\n- 具体位置：Section 3.4\n- 问题：所提出的\"修复\"本质上是恢复 GRPO 的原始设计——将整个 episode 作为一个样本优化。论文自身明确承认：\"This restores GRPO's original per-sample granularity to the episode level; step-independent windowing is the deviation introduced by multi-turn agent frameworks.\"（Section 3.4）。换言之，\"新方法\"是\"不要使用 RAGEN 引入的 step-independent decomposition\"，这是一个设计选择的回退而非方法论创新。\n- 为什么影响接收：对于一篇以 \"Episode-Level Correction\" 作为标题核心部分的论文，解决方案的技术贡献需要达到一定门槛。本文将自身定位为\"primarily diagnostic\"，这是合理的策略，但即使如此，诊断类论文通常也需要提出具有独立价值的解决方案或 actionable insights 超越\"不要这样做\"。\n- 建议修改方向：（1）将标题和 framing 更彻底地聚焦于诊断贡献本身，降低对 episode-level GRPO 作为\"correction\"的强调；（2）或者在 episode-level 基础上加入真正的改进（例如解决 seed 依赖问题的机制），使方法论贡献实质化。\n\n**W2** [critical] **Abstract/Introduction 的 claims 与实验证据之间存在 overclaiming**\n- 具体位置：Abstract, Section 1\n- 问题：\n  - Abstract 称 \"structurally eliminates both failure modes\"——技术上正确，但在仅 36% seed 泛化的语境下具有误导性。一个 structurally 消除了失败模式的方法不应在 64% 的 seed 上停滞或坍塌。\n  - Introduction 称 \"achieving substantial OOD improvement where step-independent collapses to 0%\"——17.7% 均值被 4 个泛化 seed 显著拉高。Table 2 显示 7/11 seed 的 OOD 成绩与 SFT baseline（6.72%）无统计显著差异，**中位数**应远低于均值。\n  - 8B 结果 90.3% OOD 被呈现为\"cross-scale verification\"但仅为单 seed——在 1.7B 已证明强 seed 依赖的前提下，单 seed 8B 结果的证据强度极弱。\n- 为什么影响接收：overclaiming 是审稿中的重大问题。论文在 Limitations 中诚实承认了这些限制，但 abstract 和 introduction 的 framing 仍然给读者留下了过于乐观的第一印象。\n- 建议修改方向：（1）在 abstract 中报告中位数而非均值；（2）将 \"structurally eliminates\" 改为更谨慎的表述如 \"structurally removes the conditions for\"；（3）将 8B 结果明确标注为\"preliminary single-seed evidence\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W3** [warning] **不完整的析因设计削弱了核心分离声明**\n- 具体位置：Section 3.5, Section 5.2\n- 问题：Cell C（full trajectory + step-level advantage，仅 M2 active）在 6 组超参数下均出现 NaN 发散，导致 2×2 设计缺失一个关键 cell。论文无法展示 M2 在没有 M1 的情况下单独的效果。Discussion 承认\"our factorial interpretation assumes approximate separability\"（Section 6），但 Introduction 的 Contribution 2 仍称之为 \"controlled empirical separation\"，且 Cell C 的发散可能暗示一个第三机制：M1 的信息截断可能无意中通过限制梯度方差来\"稳定\"训练（Discussion 中提到但未深入分析）。\n- 建议：（1）在 Contribution 2 中更明确地标注析因是 partial（3-of-4）；（2）对 Cell C 的发散进行更深入的分析——它是否代表了 M1/M2 框架之外的独立现象？\n\n**W4** [warning] **实验范围相对于 claims 偏窄**\n- 具体位置：Section 5, Limitations\n- 问题：\n  - 主要评估：单一环境（ALFWorld）、单一规模（1.7B）、6 种任务类型\n  - 8B 验证：单 seed，无 seed 变异数据\n  - ScienceWorld：单 seed，仅展示 collapse（主文未报告 episode-level 对比）\n  - **未与同期方法做 head-to-head 比较**（GiGPO, HCAPO, Turn-PPO 等）——论文以贡献\"正交\"（诊断 vs 解决方案）为由省略，但实证展示诊断框架能正确预测这些方法的相对表现将大幅增强说服力\n  - 所有 OOD 评估为单次 τ=0.4\n- 建议：至少复现一个代表性的同期方法（如 GiGPO）作为 baseline，验证诊断框架的预测能力。\n\n**W5** [warning] **理论分析的假设限制性较强，且与实际实验设定之间存在 gap**\n- 具体位置：Section 4, Section 5.4\n- 问题：\n  - Propositions 1-2 假设 binary reward，但实际实验使用 ternary reward（r ∈ {−0.1, 0, 1}）\n  - Definition 1（locally correct action）的等价性是近似的（脚注 2 承认）\n  - 上界仅在\"episode success implies all constituent windows are locally correct\"时 tight——这是一个强假设\n  - Ternary reward 下实测 credit agreement 52.1% 与 binary bound 19.1% 差距巨大（Section 5.4），说明实际训练动态处于一个与理论分析显著不同的 regime\n- 建议：为 ternary/非 binary reward 场景提供形式化分析或更清楚地讨论理论与实践之间的 gap。\n\n**W6** [warning] **与同期工作的关系停留在声明层面，缺乏实证**\n- 具体位置：Section 2, Section 6\n- 问题：Related Work（Section 2）声称 \"our framework provides a unified explanation for why these finer-grained methods succeed: they eliminate M2\"，Discussion（Section 6）称 HCAPO 和 GiGPO \"succeed with h=2 by eliminating M2 through finer-grained credit, consistent with our framework's prediction\"。但这一核心声明完全未经实证验证。\n- 建议：增加一个分析（表格或图），展示 GiGPO/Turn-PPO/HCAPO 如何映射到 M1/M2 框架，以及框架预测与它们的实际表现是否一致。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** Table 1 中 Cell B 标注 \"Single seed; seed2 best checkpoint unavailable for re-evaluation\"——这意味着 A→B 对比的关键数据只有单 seed 支撑，应更突出说明。\n- **M2** Figure 3(b) 的 window size sweep 中，h=10 的两个 seed 差异巨大（6.25% vs 21.9%），但主文仅报告均值 14.1%，应报告两个 seed 的单独结果。\n- **M3** Section 5.1 提到 \"Qwen3-1.7B fine-tuned on expert demonstrations (SFT baseline: 12.5%)\"——12.5% in-distribution 的 SFT baseline 是否偏低？这可能影响诊断的普适性（在更强的 SFT baseline 上 sign misattribution 的严重程度会不同）。\n- **M4** Equation 2 中 R_w = γ^(N-w) · R_episode——γ 的具体值在主文未给出（Appendix B 中为 0.95），建议在主文中提及。\n- **M5** 论文 AI assistance 声明（page 16）提到使用 Claude，这很好的透明度实践。\n\n---\n\n## Questions\n\n**Q1**: 11 个 seed 的 OOD success rate **中位数**是多少？（相比均值 17.7%，中位数更能反映\"typical\"性能）\n\n**Q2**: 8B 实验（90.3% OOD）尝试了多少个 seed？是唯一的 seed 还是从多个中选出的？在 1.7B 已证明强 seed 依赖的前提下，这个问题直接影响该结果的可信度。\n\n**Q3**: Cell C 的 NaN 发散是否可能代表了 M1/M2 框架之外的独立现象？论文 Discussion 提到 \"M1 may unintentionally stabilize training by limiting gradient variance\"——这是否暗示 M1 除了是\"failure mechanism\"外，还起到了某种正则化作用？如果是这样，M1/M2 作为两个独立失败机制的框架是否需要修正？\n\n**Q4**: 理论分析给出 binary 下 P(correct|update) ≤ 19.1%，但实际 ternary 设定下 credit agreement 为 52.1%（Section 5.4）。哪个 regime 更准确地描述了实际训练动态？binary bound 能否有意义地预测 ternary 设定下的行为？\n\n**Q5**: 是否考虑过在具有更密 reward 信号的环境中评估（如中间步骤的 partial reward），以测试 M2 机制的边界条件？\n\n**Q6**: Appendix D 中 REINFORCE++ 实验显示 per-token normalization 不帮助——能否进一步分析为什么？这对理解 sign misattribution 的根本原因（是 normalization 方式还是 reward sparsity）有重要意义。\n\n---\n\n## Missing References\n\n以下相关工作可能被遗漏或值得讨论：\n\n1. **RLOO** (Ahmadian et al., 2024, \"Back to Basics: Revisiting REINFORCE-Style Optimization for Learning from Human Feedback in LLMs\") — 提出 REINFORCE Leave-One-Out baseline，与 GRPO 的 group normalization 直接相关，处理类似的 variance 问题。\n2. **合作多智能体 RL 的 credit assignment 文献** — Appendix A.4 提到了多智能体类比，但未引用标准文献如 COMA (Foerster et al., 2018) 或 QMIX (Rashid et al., 2020)，这些工作直接处理了\"shared team reward → individual credit\"的问题，与本文的核心问题高度相关。\n\n---\n\n## 主要优势总结\n\n1. 干净的析因实验设计是本文最大亮点，为 agent RL 社区提供了方法学模板\n2. 理论与实验的对照验证增强了诊断的可信度\n3. 科学诚实的报告标准——包括负面结果（Cell C 失败、seed 依赖）——值得鼓励\n4. 写作质量整体较高，结构清晰\n\n## 总体判断\n\n本文的核心贡献是诊断性的，这个定位是合理且有价值的。但两个关键问题制约了评分：（1）解决方案缺乏独立的方法论价值——episode-level GRPO 本质上是\"恢复默认设置\"；（2）实验范围偏窄且结果强 seed 依赖，削弱了诊断的普适性声明。论文在诚实度和方法学严谨性上表现出色，适合作为 Findings 发表以供社区参考，但未达到主会议接收的新颖性和影响力门槛。\n",
    "reviewer_id": "2",
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-25T21:22:27.171920+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4204
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-25T21:22:32.759561+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-25T21:22:32.760023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-25T21:22:37.376691+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-25T21:22:37.377245+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 536 · 2026-05-25T21:22:45.469458+00:00_

审稿完成。核心结论：

- **Overall: 3.0 (Findings)**，Soundness 3.0，Excitement 2.5
- **两个 critical 问题**：(1) Episode-level GRPO 本质是恢复标准 GRPO，方法论新颖性不足；(2) Abstract/Intro 存在 overclaiming（"structurally eliminates" vs 36% seed 泛化率，均值 vs 中位数问题，单 seed 8B 结果）
- **三个 warning 问题**：Cell C 缺失削弱析因完整性、实验范围偏窄（无同期方法对比）、理论假设（binary）与实际设定（ternary）gap 大
- **主要优势**：析因实验设计精良、理论-实验对照验证扎实、科学诚实度高

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 537 · 2026-05-25T21:28:37.588696+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Strength/Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

### Summary
本文诊断了 step-independent agent RL（GRPO + 固定窗口分解）的两种结构性失败机制：M1 (Policy information loss) 和 M2 (Advantage sign misattribution)。部分析因实验（3/4 cells）在 ALFWorld 上分离两种机制，episode-level GRPO 作为修复。理论在 binary reward 假设下推导错误符号梯度上界。

### Overall: 3.0 (Findings), Soundness 3.0, Excitement 3.0, Confidence 4/5

### Strengths
S1: M1/M2 双机制分解是实质性概念贡献，有操作性诊断价值，能预测并发方法成功
S2: 部分析因设计 + 三类验证指标构成多角度证据体系，discount sweep 排除替代解释
S3: 11-seed 评估超过领域 3-5 seed 标准，统计方法严谨（Fisher exact, Wilson CI, unified step-5）
S4: Propositions 1-2 closed-form 上界 + sign-episode correlation/credit agreement 实证验证 + break-even 分析
S5: Limitations 坦诚

### Must-Fix
W1 [Critical]: Cell C 缺失严重削弱 "Dual Mechanism" 因果声称——无法独立验证 M1 效应、估计 M1×M2 交互效应、确认可分离性。Cell C NaN 不稳定暗示 M1 可能通过限制梯度方差稳定训练（非加性交互），若交互存在则 A→B→D 因果推断链不成立。建议弱化为 "dual mechanism hypothesis"。
W2 [Critical]: 析因条件仅 2 seeds，统计效力不足——Cell B OOD 实际仅 1 seed (5.97%)。n=2 无法计算有意义的置信区间。论文 11-seed 评估的高 seed 变异性反过来证明 2-seed 析因结论脆弱。
W3 [Critical]: Cell A 与 Cell B 的操作差异不够精确——由于 R_w = γ^(N-w) · R_episode，Cell A 窗口级 GRPO 归一化后 advantage 符号可能与 Cell B episode-level 近似相同。A→B 改善可能来自其他操作差异（per-window vs per-episode KL penalty、effective batch size、ε 缩放），而非 M2 消除。需提供 Cell A/B 实际 advantage 值统计比较。

### Should-Fix
W4 [Warning]: Binary theory vs ternary experiment gap——52.1% vs 19.1% "measure different quantities"，缺乏 ternary 下的 formal bound
W5 [Warning]: 跨环境验证薄弱——ScienceWorld 单 seed 且与 ALFWorld scale 不同，存在 scale 混淆
W6 [Warning]: 未与 HCAPO/GiGPO/TurnPPO 实验对比
W7 [Warning]: Proposition 1 中 p 的条件化不精确——locally correct actions 应提高 episode success probability，P(correct sign) 应为 p_w > p 而非 p。独立性假设未明确。

### Minor
M1: Cell A OOD 缺失、Cell B OOD 仅单 seed
M2: Cohen's h threshold 未显式引用 0.2
M3: Eq.6 假设 g+/g- 对称但实测非对称
M4: Abstract 数字偏低，贡献应更明确框定为 diagnostic
M5: Appendix H early signal analysis n=4 太小

### Questions
Q1: Cell B "episode-level advantage" 精确实现是什么？每个 episode 单个 Â 应用于所有 tokens，还是每个 window 不同 advantage？
Q2: 11 seed 中 "Collapsed" seeds 的失败模式是什么？episode-level 消除了 M2，坍塌来自第三种机制？
Q3: ALFWorld early training 中 action validity 比例？若 >80%，credit agreement 指标 discriminative power 低
Q4: 8B 90.3% OOD vs 1.7B 17.7%——差异来自 scale 还是方法？8B SFT baseline 80.6% 说明增量贡献 ~10pp，与 1.7B ~11pp 相似。

### Missing References
1. Ahmadian et al. (2024) RLOO — 与 episode-level GRPO 和 REINFORCE++ 的关系
2. Yu et al. (2025) DAPO — GRPO group normalization 改进与 M2

---

请逐条回应（[AGREE] 或 [REBUT]），并基于论文具体内容和你自己的专业判断给出理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-25T21:31:44.365639+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Strengths 回应\n\n**[AGREE] R1-S1**: M1/M2 双机制分解确实是本文最核心的概念贡献。但我要补充：这一贡献的价值取决于分解的干净程度——而 Cell C 缺失和 A→B 操作差异的 confound（见 W1/W3 回应）在一定程度上削弱了分解的可靠性。\n\n**[AGREE] R1-S2**: 析因设计 + 三类验证指标是本文方法学上的亮点。Discount sweep 排除替代解释的做法值得肯定（Appendix D）。\n\n**[AGREE] R1-S3**: 11-seed 评估确实超过领域标准。但我补充一点：这里的 11-seed 评估只针对 episode-level GRPO（Section 5.5, Table 2），析因条件本身仅用 2 seeds（R1 在 W2 中正确指出）。统计严谨性在不同部分的标准不一致。\n\n**[AGREE] R1-S4**: 理论与实证的对照验证是可信的。Break-even magnitude ratio 分析（实测 |Â_correct|/|Â_wrong| ≈ 2.6 vs 理论需要 ≥4.2, Section 5.4）特别有说服力——它排除了\"虽然错误符号多但正确符号幅度大所以可以补偿\"的替代解释。\n\n**[AGREE] R1-S5**: 与我的观点完全一致（我的 S2）。\n\n---\n\n## Must-Fix 回应\n\n**[AGREE] R1-W1**: Cell C 缺失确实是核心弱点。我在自己的审稿中将其列为 W3（Should-Fix），但现在倾向于同意 R1 将其提升至 Critical 级别。\n\n关键理由：\n1. R1 指出的\"M1 可能通过限制梯度方差稳定训练\"这一假说非常重要——论文 Discussion（Section 6）自身也提到 \"Cell C's qualitatively different failure mode suggests M1 may unintentionally stabilize training by limiting gradient variance\"，但未深入分析。如果 M1 同时是 failure mechanism 和 stabilizer，则 M1/M2 作为两个独立失败机制的框架需要根本性修正——它们可能是 non-additively interacting 的。\n2. 从 A→B→D 推断因果链确实需要可分离性假设，而 Cell C 的缺失使这个假设无法验证。\n\nR1 建议弱化为 \"dual mechanism hypothesis\" 非常合理。当前标题中的 \"Dual Mechanism Diagnosis\" 隐含了因果确认，但实际上只完成了 3/4 的析因。\n\n**[AGREE] R1-W2**: 这一点我在自己的审稿中未充分强调，R1 的论证更为精确。\n\n具体证据支撑：\n- Cell B OOD 结果实际只有 1 seed（Table 1 脚注：\"Single seed; seed2 best checkpoint unavailable for re-evaluation\"）\n- 而论文 11-seed 评估（Table 2）恰好证明了 seed 变异性之大——Collapsed 和 Generalized seeds 的 OOD 差异可达 20+ pp\n- 在这样的高变异性下，n=2（甚至 n=1）的析因结论缺乏统计置信度\n\n这意味着 A→B→D 的梯度不仅有 Cell C 缺失问题（W1），还有 Cell B 统计效力问题。这两个 critical 问题叠加使核心因果声明显著削弱。\n\n**[AGREE] R1-W3**: 这是三个 Must-Fix 中最锐利的技术批评，我在自己的审稿中未识别到这一点。\n\nR1 的论证链：\n1. Cell A 中 R_w = γ^(N-w) · R_episode（Equation 2），所有窗口的 return 是 episode return 的确定性单调函数\n2. 因此 Cell A 的 per-window GRPO 归一化后，advantage 符号完全由 episode 结果决定：Â_{w,k} = (γ^(N-w) · R_k - γ^(N-w) · μ) / (γ^(N-w) · σ + ε) ≈ (R_k - μ) / (σ + ε/γ^(N-w))\n3. 当 ε 相对 σ 较小时，Cell A 的 advantage **符号**与 Cell B 的 episode-level advantage **完全相同**\n4. 因此 A→B 的改善不能归因于\"消除 M2\"——因为 Cell B 同样具有符号误归因\n\n我进一步补充：论文对 Cell B \"eliminates M2\"（Section 3.5: \"only M1 active\"）的声明与 M2 的定义存在内在矛盾。M2 定义为\"advantage sign reflects episode outcome, not local action quality\"（Section 3.3.2）。Cell B 使用 episode-level advantage——一个失败 episode 的所有 token 仍然获得负 advantage——这**正是** sign misattribution 的定义。Cell B 并未消除 M2，只是改变了 M2 的传播方式（单次 episode-level 更新 vs N 次独立 window-level 更新）。\n\nA→B 的改善更可能来自：\n- 消除了 per-window 独立优化的**累积**错误放大效应（N 次独立错误梯度 → 1 次错误梯度）\n- Per-window vs per-episode KL penalty 的差异\n- Effective batch size 差异（N×K windows vs K episodes）\n- Clipping behavior 差异\n\n这不是\"消除 M2\"，而可能是\"减缓 M2 的累积伤害\"——这是一个重要的概念区分，论文未做出。\n\n---\n\n## Should-Fix 回应\n\n**[AGREE] R1-W4**: 与我的 W5 一致。52.1%（ternary 实测）vs 19.1%（binary 上界）的差距过大——说明 binary 假设下的理论分析与实际训练 regime 显著脱节。论文 Section 5.4 末尾承认两者\"measure different quantities\"，但未提供 ternary 下的形式化分析。这使得理论分析的 practical relevance 打折扣。\n\n**[AGREE] R1-W5**: ScienceWorld 验证确实存在 scale confound——ScienceWorld 使用不同规模的模型（未在主文明确报告规模），且仅展示 step-independent collapse 而未报告 episode-level 对比结果。如果 cross-environment 验证的价值仅限于\"step-independent 在另一个环境也 collapse\"，这并不令人惊讶（任何将 binary reward 广播到截断窗口的方法都预期会 collapse），作为验证贡献有限。\n\n**[AGREE] R1-W6**: 与我的 W4/W6 一致。论文声称框架能\"provide a unified explanation\"（Section 2），但纯属声明——缺乏任何实证验证。哪怕只复现一个 concurrent method（如 GiGPO）并展示其表现符合框架预测，说服力都会大幅提升。\n\n**[PARTIALLY AGREE] R1-W7**: R1 指出 Proposition 1 中 locally correct actions 应使 P(episode success | correct window) = p_w > p，因此 P(correct sign) 上界应更宽松。\n\n技术上这是正确的：如果 window w 含有 locally correct actions，那么 episode 成功的条件概率 p_w 应高于边际概率 p。但实际影响取决于 p_w - p 的大小。在低成功率 regime（p ≈ 12.5%），即使 p_w 高出数个百分点（如 15-20%），结论仍然成立——绝大多数更新携带错误符号。\n\n我认为这是论文应在脚注中 acknowledge 的技术瑕疵，但不改变核心结论的定性方向。将其保留在 Should-Fix 级别是恰当的。\n\n---\n\n## Minor 回应\n\n**[AGREE] R1-M1**: Cell A 缺少 OOD 评估是一个数据缺口。Table 1 脚注标注 Cell A \"OOD not evaluated at this checkpoint\"——如果 Cell A 在 step 5 就已 collapse 到 ~1.5% in-dist，OOD 评估可能确实无意义，但至少应报告以完整析因。\n\n**[AGREE] R1-M2**: Cohen's h ≈ 0.041 被描述为 \"below the small-effect threshold\"（Section 5.4），但未引用标准阈值 0.2（Cohen, 1988）。应显式引用。\n\n**[AGREE] R1-M3**: Equation 6 假设 g+ 和 g- 对称（方向相反但幅度固定），但 Section 5.4 实测 |Â_correct|/|Â_wrong| ≈ 2.6 说明幅度非对称。论文在此做了 break-even 分析来 bridge 这个 gap，但 Equation 6 本身的表述应注明对称假设的局限。\n\n**[AGREE] R1-M4**: Abstract 确实应更明确框定为 diagnostic contribution。当前 abstract 以 \"Episode-level GRPO... structurally eliminates both failure modes\" 结尾，给人方法论贡献的印象。与我的 W2 一致。\n\n**[AGREE] R1-M5**: Appendix H 中 early signal analysis 仅基于 n=4 generalized seeds，太小无法得出可靠的预测指标。论文应将其标注为 exploratory analysis 而非结论性发现。\n\n---\n\n## Questions 回应\n\n**[AGREE with concern behind Q1]**: Cell B 的精确实现确实需要澄清。如果 Cell B 对每个 episode 计算单个 Â 并统一应用于所有 tokens（包括截断的各窗口），那么 M2 在 Cell B 中仍然存在——失败 episode 的所有 locally correct actions 仍获得负 advantage。这与论文声称的 \"Cell B: only M1 active\" 矛盾。R1 这个问题实际上触及了 W3 的核心：Cell A 和 Cell B 在 advantage 符号上的差异到底是什么？\n\n**[AGREE with concern behind Q2]**: Episode-level 下 27% seed collapse 的失败模式确实值得解释。如果 episode-level 已\"消除 M2\"，collapse 的原因是什么？可能的解释：（1）M2 并未真正被消除（与 W3 一致）；（2）存在第三种机制（如初始化敏感性、reward hacking、response length inflation）；（3）episode-level 优化本身有固有的高方差问题。论文 Section 5.5 和 Appendix F 报告了 response length inflation，但未建立其与 collapse 的因果关系。\n\n**[PARTIALLY AGREE with Q3]**: Action validity 作为 locally correct 的 proxy 确实有局限——如果 >80% 的 actions 是 valid，则 credit agreement 指标的 discriminative power 低（大多数 actions 都是 \"correct\"，但 credit agreement 仍接近 50%，说明即使 proxy 保守也检测到了问题）。不过论文确实应报告 action validity 的基线比例以供读者评估 proxy 质量。\n\n**[AGREE with Q4]**: R1 的观察非常精准。8B 的 SFT baseline 已达 80.6%，episode-level 达 90.3%，增量贡献 ~10pp。1.7B 的增量也是 ~11pp（17.7% vs 6.72%）。这说明 episode-level fix 的 absolute 增量在两个 scale 上相似，90.3% 的 headline 数字主要反映 8B 模型本身的能力而非方法的优越性。论文应更清楚地分离 scale effect 和 method effect。\n\n---\n\n## Missing References 回应\n\n**[AGREE] RLOO (Ahmadian et al., 2024)**: 我在自己的审稿中也独立指出了这一遗漏。RLOO 与 GRPO 的 group normalization 直接相关——RLOO 使用 leave-one-out baseline 来减少 advantage estimate 的 variance，这与 M2 的 sign misattribution 问题有本质联系。\n\n**[PARTIALLY AGREE] DAPO**: 如果 DAPO 确实涉及 GRPO group normalization 的改进与 M2 类似的问题，则应引用。但我不确定 DAPO 的具体贡献是否与本文的 step-independent windowing 问题直接相关。我在自己的审稿中未将其列为 missing reference。建议作者确认相关性后决定是否引用。\n\n---\n\n## 综合评价\n\n在审阅 R1 的意见后，我对自己的评分进行以下调整：\n\n**维度变更**：\n- **Soundness**: 3.0 → 2.5/5。R1 的 W3 揭示了 A→B 对比的根本性 confound——Cell B 可能并未消除 M2，而是改变了 M2 的传播方式。这叠加 Cell C 缺失（W1）和 2-seed 不足（W2），使得核心因果声明 \"dual mechanism diagnosis\" 的实验基础显著削弱。\n- **Excitement**: 维持 2.5/5。\n- **Overall**: 3.0 → 2.5 (Borderline Findings)。R1 的 W3 是我未识别到的关键问题，它将论文从\"诊断有价值但方法新颖性不足\"降级为\"诊断的实验基础本身存疑\"。\n\n**核心判断**：论文的 M1/M2 概念框架仍有参考价值，但 R1 的 W3 指出 Cell B 在符号层面并未消除 M2 这一关键问题——如果 A→B 的改善来自操作差异而非 M2 消除，则整个析因分解的因果解释力大幅下降。结合 Cell C 缺失和 2-seed 统计效力不足，论文需要对析因条件的精确操作差异做更细致的分析，才能支撑其因果声明。\n",
  "reviewer_id": "2",
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Strengths 回应\n\n**[AGREE] R1-S1**: M1/M2 双机制分解确实是本文最核心的概念贡献。但我要补充：这一贡献的价值取决于分解的干净程度——而 Cell C 缺失和 A→B 操作差异的 confound（见 W1/W3 回应）在一定程度上削弱了分解的可靠性。\n\n**[AGREE] R1-S2**: 析因设计 + 三类验证指标是本文方法学上的亮点。Discount sweep 排除替代解释的做法值得肯定（Appendix D）。\n\n**[AGREE] R1-S3**: 11-seed 评估确实超过领域标准。但我补充一点：这里的 11-seed 评估只针对 episode-level GRPO（Section 5.5, Table 2），析因条件本身仅用 2 seeds（R1 在 W2 中正确指出）。统计严谨性在不同部分的标准不一致。\n\n**[AGREE] R1-S4**: 理论与实证的对照验证是可信的。Break-even magnitude ratio 分析（实测 |Â_correct|/|Â_wrong| ≈ 2.6 vs 理论需要 ≥4.2, Section 5.4）特别有说服力——它排除了\"虽然错误符号多但正确符号幅度大所以可以补偿\"的替代解释。\n\n**[AGREE] R1-S5**: 与我的观点完全一致（我的 S2）。\n\n---\n\n## Must-Fix 回应\n\n**[AGREE] R1-W1**: Cell C 缺失确实是核心弱点。我在自己的审稿中将其列为 W3（Should-Fix），但现在倾向于同意 R1 将其提升至 Critical 级别。\n\n关键理由：\n1. R1 指出的\"M1 可能通过限制梯度方差稳定训练\"这一假说非常重要——论文 Discussion（Section 6）自身也提到 \"Cell C's qualitatively different failure mode suggests M1 may unintentionally stabilize training by limiting gradient variance\"，但未深入分析。如果 M1 同时是 failure mechanism 和 stabilizer，则 M1/M2 作为两个独立失败机制的框架需要根本性修正——它们可能是 non-additively interacting 的。\n2. 从 A→B→D 推断因果链确实需要可分离性假设，而 Cell C 的缺失使这个假设无法验证。\n\nR1 建议弱化为 \"dual mechanism hypothesis\" 非常合理。当前标题中的 \"Dual Mechanism Diagnosis\" 隐含了因果确认，但实际上只完成了 3/4 的析因。\n\n**[AGREE] R1-W2**: 这一点我在自己的审稿中未充分强调，R1 的论证更为精确。\n\n具体证据支撑：\n- Cell B OOD 结果实际只有 1 seed（Table 1 脚注：\"Single seed; seed2 best checkpoint unavailable for re-evaluation\"）\n- 而论文 11-seed 评估（Table 2）恰好证明了 seed 变异性之大——Collapsed 和 Generalized seeds 的 OOD 差异可达 20+ pp\n- 在这样的高变异性下，n=2（甚至 n=1）的析因结论缺乏统计置信度\n\n这意味着 A→B→D 的梯度不仅有 Cell C 缺失问题（W1），还有 Cell B 统计效力问题。这两个 critical 问题叠加使核心因果声明显著削弱。\n\n**[AGREE] R1-W3**: 这是三个 Must-Fix 中最锐利的技术批评，我在自己的审稿中未识别到这一点。\n\nR1 的论证链：\n1. Cell A 中 R_w = γ^(N-w) · R_episode（Equation 2），所有窗口的 return 是 episode return 的确定性单调函数\n2. 因此 Cell A 的 per-window GRPO 归一化后，advantage 符号完全由 episode 结果决定：Â_{w,k} = (γ^(N-w) · R_k - γ^(N-w) · μ) / (γ^(N-w) · σ + ε) ≈ (R_k - μ) / (σ + ε/γ^(N-w))\n3. 当 ε 相对 σ 较小时，Cell A 的 advantage **符号**与 Cell B 的 episode-level advantage **完全相同**\n4. 因此 A→B 的改善不能归因于\"消除 M2\"——因为 Cell B 同样具有符号误归因\n\n我进一步补充：论文对 Cell B \"eliminates M2\"（Section 3.5: \"only M1 active\"）的声明与 M2 的定义存在内在矛盾。M2 定义为\"advantage sign reflects episode outcome, not local action quality\"（Section 3.3.2）。Cell B 使用 episode-level advantage——一个失败 episode 的所有 token 仍然获得负 advantage——这**正是** sign misattribution 的定义。Cell B 并未消除 M2，只是改变了 M2 的传播方式（单次 episode-level 更新 vs N 次独立 window-level 更新）。\n\nA→B 的改善更可能来自：\n- 消除了 per-window 独立优化的**累积**错误放大效应（N 次独立错误梯度 → 1 次错误梯度）\n- Per-window vs per-episode KL penalty 的差异\n- Effective batch size 差异（N×K windows vs K episodes）\n- Clipping behavior 差异\n\n这不是\"消除 M2\"，而可能是\"减缓 M2 的累积伤害\"——这是一个重要的概念区分，论文未做出。\n\n---\n\n## Should-Fix 回应\n\n**[AGREE] R1-W4**: 与我的 W5 一致。52.1%（ternary 实测）vs 19.1%（binary 上界）的差距过大——说明 binary 假设下的理论分析与实际训练 regime 显著脱节。论文 Section 5.4 末尾承认两者\"measure different quantities\"，但未提供 ternary 下的形式化分析。这使得理论分析的 practical relevance 打折扣。\n\n**[AGREE] R1-W5**: ScienceWorld 验证确实存在 scale confound——ScienceWorld 使用不同规模的模型（未在主文明确报告规模），且仅展示 step-independent collapse 而未报告 episode-level 对比结果。如果 cross-environment 验证的价值仅限于\"step-independent 在另一个环境也 collapse\"，这并不令人惊讶（任何将 binary reward 广播到截断窗口的方法都预期会 collapse），作为验证贡献有限。\n\n**[AGREE] R1-W6**: 与我的 W4/W6 一致。论文声称框架能\"provide a unified explanation\"（Section 2），但纯属声明——缺乏任何实证验证。哪怕只复现一个 concurrent method（如 GiGPO）并展示其表现符合框架预测，说服力都会大幅提升。\n\n**[PARTIALLY AGREE] R1-W7**: R1 指出 Proposition 1 中 locally correct actions 应使 P(episode success | correct window) = p_w > p，因此 P(correct sign) 上界应更宽松。\n\n技术上这是正确的：如果 window w 含有 locally correct actions，那么 episode 成功的条件概率 p_w 应高于边际概率 p。但实际影响取决于 p_w - p 的大小。在低成功率 regime（p ≈ 12.5%），即使 p_w 高出数个百分点（如 15-20%），结论仍然成立——绝大多数更新携带错误符号。\n\n我认为这是论文应在脚注中 acknowledge 的技术瑕疵，但不改变核心结论的定性方向。将其保留在 Should-Fix 级别是恰当的。\n\n---\n\n## Minor 回应\n\n**[AGREE] R1-M1**: Cell A 缺少 OOD 评估是一个数据缺口。Table 1 脚注标注 Cell A \"OOD not evaluated at this checkpoint\"——如果 Cell A 在 step 5 就已 collapse 到 ~1.5% in-dist，OOD 评估可能确实无意义，但至少应报告以完整析因。\n\n**[AGREE] R1-M2**: Cohen's h ≈ 0.041 被描述为 \"below the small-effect threshold\"（Section 5.4），但未引用标准阈值 0.2（Cohen, 1988）。应显式引用。\n\n**[AGREE] R1-M3**: Equation 6 假设 g+ 和 g- 对称（方向相反但幅度固定），但 Section 5.4 实测 |Â_correct|/|Â_wrong| ≈ 2.6 说明幅度非对称。论文在此做了 break-even 分析来 bridge 这个 gap，但 Equation 6 本身的表述应注明对称假设的局限。\n\n**[AGREE] R1-M4**: Abstract 确实应更明确框定为 diagnostic contribution。当前 abstract 以 \"Episode-level GRPO... structurally eliminates both failure modes\" 结尾，给人方法论贡献的印象。与我的 W2 一致。\n\n**[AGREE] R1-M5**: Appendix H 中 early signal analysis 仅基于 n=4 generalized seeds，太小无法得出可靠的预测指标。论文应将其标注为 exploratory analysis 而非结论性发现。\n\n---\n\n## Questions 回应\n\n**[AGREE with concern behind Q1]**: Cell B 的精确实现确实需要澄清。如果 Cell B 对每个 episode 计算单个 Â 并统一应用于所有 tokens（包括截断的各窗口），那么 M2 在 Cell B 中仍然存在——失败 episode 的所有 locally correct actions 仍获得负 advantage。这与论文声称的 \"Cell B: only M1 active\" 矛盾。R1 这个问题实际上触及了 W3 的核心：Cell A 和 Cell B 在 advantage 符号上的差异到底是什么？\n\n**[AGREE with concern behind Q2]**: Episode-level 下 27% seed collapse 的失败模式确实值得解释。如果 episode-level 已\"消除 M2\"，collapse 的原因是什么？可能的解释：（1）M2 并未真正被消除（与 W3 一致）；（2）存在第三种机制（如初始化敏感性、reward hacking、response length inflation）；（3）episode-level 优化本身有固有的高方差问题。论文 Section 5.5 和 Appendix F 报告了 response length inflation，但未建立其与 collapse 的因果关系。\n\n**[PARTIALLY AGREE with Q3]**: Action validity 作为 locally correct 的 proxy 确实有局限——如果 >80% 的 actions 是 valid，则 credit agreement 指标的 discriminative power 低（大多数 actions 都是 \"correct\"，但 credit agreement 仍接近 50%，说明即使 proxy 保守也检测到了问题）。不过论文确实应报告 action validity 的基线比例以供读者评估 proxy 质量。\n\n**[AGREE with Q4]**: R1 的观察非常精准。8B 的 SFT baseline 已达 80.6%，episode-level 达 90.3%，增量贡献 ~10pp。1.7B 的增量也是 ~11pp（17.7% vs 6.72%）。这说明 episode-level fix 的 absolute 增量在两个 scale 上相似，90.3% 的 headline 数字主要反映 8B 模型本身的能力而非方法的优越性。论文应更清楚地分离 scale effect 和 method effect。\n\n---\n\n## Missing References 回应\n\n**[AGREE] RLOO (Ahmadian et al., 2024)**: 我在自己的审稿中也独立指出了这一遗漏。RLOO 与 GRPO 的 group normalization 直接相关——RLOO 使用 leave-one-out baseline 来减少 advantage estimate 的 variance，这与 M2 的 sign misattribution 问题有本质联系。\n\n**[PARTIALLY AGREE] DAPO**: 如果 DAPO 确实涉及 GRPO group normalization 的改进与 M2 类似的问题，则应引用。但我不确定 DAPO 的具体贡献是否与本文的 step-independent windowing 问题直接相关。我在自己的审稿中未将其列为 missing reference。建议作者确认相关性后决定是否引用。\n\n---\n\n## 综合评价\n\n在审阅 R1 的意见后，我对自己的评分进行以下调整：\n\n**维度变更**：\n- **Soundness**: 3.0 → 2.5/5。R1 的 W3 揭示了 A→B 对比的根本性 confound——Cell B 可能并未消除 M2，而是改变了 M2 的传播方式。这叠加 Cell C 缺失（W1）和 2-seed 不足（W2），使得核心因果声明 \"dual mechanism diagnosis\" 的实验基础显著削弱。\n- **Excitement**: 维持 2.5/5。\n- **Overall**: 3.0 → 2.5 (Borderline Findings)。R1 的 W3 是我未识别到的关键问题，它将论文从\"诊断有价值但方法新颖性不足\"降级为\"诊断的实验基础本身存疑\"。\n\n**核心判断**：论文的 M1/M2 概念框架仍有参考价值，但 R1 的 W3 指出 Cell B 在符号层面并未消除 M2 这一关键问题——如果 A→B 的改善来自操作差异而非 M2 消除，则整个析因分解的因果解释力大幅下降。结合 Cell C 缺失和 2-seed 统计效力不足，论文需要对析因条件的精确操作差异做更细致的分析，才能支撑其因果声明。\n",
    "reviewer_id": "2",
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-25T21:31:48.027854+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3662
}
```

</details>

---


### Assistant

_source line 540 · 2026-05-25T21:31:54.899994+00:00_

交叉回应已提交。

核心变更：在审阅 R1 意见后，我将 Overall 从 3.0 下调至 2.5（Borderline Findings），Soundness 从 3.0 下调至 2.5。主要原因是 R1-W3 揭示了一个我原始审稿中未识别的关键问题——Cell B 在数学上并未消除 M2（advantage 符号仍由 episode 结果决定），因此 A→B 的改善可能来自操作层面的差异（KL penalty、batch size、clipping）而非 M2 的消除。这叠加 Cell C 缺失和 2-seed 统计效力不足，使析因分解的因果基础显著削弱。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2"
}
```

</details>

---
