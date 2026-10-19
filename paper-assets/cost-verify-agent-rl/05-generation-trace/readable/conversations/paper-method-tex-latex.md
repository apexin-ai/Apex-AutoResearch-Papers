# paper method tex latex

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_paper_method-tex-latex_20260520T131951.jsonl`
- **Structured JSON:** [`ca488bd1974e405ab9bc.json`](../../sessions/ca/ca488bd1974e405ab9bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-20T13:26:00.060797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-tex-latex_20260520T131951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method_draft.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T13:26:00.061276+00:00_

1	# 3. Method
2	
3	## 3.1 Problem Formulation
4	
5	### Interactive Agent as POMDP
6	
7	We formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{O}, T, O, R, \gamma \rangle$, where $\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\mathcal{A}$ is the action space (e.g., natural language commands such as `go to shelf 1`, `take mug 2`), $\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \mathcal{S} \times \mathcal{A} \rightarrow \Delta(\mathcal{S})$ is the transition function, $O: \mathcal{S} \rightarrow \Delta(\mathcal{O})$ is the observation function, $R: \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$ is the reward function, and $\gamma$ is the discount factor.
8	
9	At each timestep $t$, the agent receives observation $o_t \in \mathcal{O}$ and selects action $a_t \in \mathcal{A}$ according to its policy $\pi_\phi(a_t \mid h_t)$, where $h_t = (o_1, a_1, \ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\max}$.
10	
11	### Verification Decision
12	
13	At each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:
14	$$d_t \in \{0, 1\}$$
15	where $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.
16	
17	We parameterize the verification policy as $\pi_\theta(d_t \mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\pi_\theta$ is realized by augmenting the agent's action space with a special control token $\langle\text{VERIFY}\rangle$ that precedes the action output, such
…[truncated 16145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-tex-latex_20260520T131951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T13:26:00.061476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-tex-latex_20260520T131951",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T13:26:00.061932+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-tex-latex_20260520T131951",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T13:26:00.062359+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method.tex",
  "content": "% method.tex — Method section for B-IAVR paper\n% Converted from method_draft.md\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{subsec:problem-formulation}\n\n\\subsubsection{Interactive Agent as POMDP}\n\nWe formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = \\langle \\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma \\rangle$, where $\\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\\mathcal{A}$ is the action space (e.g., natural language commands such as \\texttt{go to shelf 1}, \\texttt{take mug 2}), $\\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\Delta(\\mathcal{S})$ is the transition function, $O: \\mathcal{S} \\rightarrow \\Delta(\\mathcal{O})$ is the observation function, $R: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$ is the reward function, and $\\gamma$ is the discount factor.\n\nAt each timestep $t$, the agent receives observation $o_t \\in \\mathcal{O}$ and selects action $a_t \\in \\mathcal{A}$ according to its policy $\\pi_\\phi(a_t \\mid h_t)$, where $h_t = (o_1, a_1, \\ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\\max}$.\n\n\\subsubsection{Verification Decision}\n\nAt each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:\n\\begin{equation}\nd_t \\in \\{0, 1\\}\n\\label{eq:verify-decision}\n\\end{equation}\nwhere $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.\n\nWe parameterize the verification policy as $\\pi_\\theta(d_t \\mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\\pi_\\theta$ is realized by augmenting the agent's action space with a special control token $\\langle\\text{VERIFY}\\rangle$ that precedes the action output, such that the language model generates either $\\langle\\text{VERIFY}\\rangle\\, a_t$ or $\\langle\\text{SKIP}\\rangle\\, a_t$ at each step.\n\n\\subsubsection{Action-Change Signal}\n\nWe define the \\textbf{action-change indicator} as the primary signal for verification informativeness:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}\\left[a_t^{\\text{post}} \\neq a_t^{\\text{pre}}\\right]\n\\label{eq:action-change}\n\\end{equation}\nwhere $a_t^{\\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\\langle \\text{verb}, \\text{object}, \\text{receptacle} \\rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.\n\nThe key insight is that \\textbf{most self-verification is confirmatory rather than corrective}~\\cite{self-verification-dilemma-2026}. When $\\Delta a_t = 0$, the verification consumed compute without altering behavior; it was uninformative. When $\\Delta a_t = 1$, the verification produced a behavioral change, which indicates it carried decision-relevant information.\n\n\\subsubsection{Verification Cost Model}\n\nEach verification incurs a fixed cost $c_{\\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:\n\\begin{equation}\nC_{\\text{total}} = \\sum_{t=1}^{T} d_t \\cdot c_{\\text{verify}}\n\\label{eq:total-cost}\n\\end{equation}\n\nIn practice, $c_{\\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.\n\n\\subsubsection{Objective}\n\nThe goal of B-IAVR is to learn a verification policy $\\pi_\\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:\n\\begin{equation}\n\\max_\\theta \\; \\mathbb{E}_{\\pi_\\theta, \\pi_\\phi}\\left[\\sum_{t=1}^{T} R(s_t, a_t)\\right] \\quad \\text{s.t.} \\quad \\mathbb{E}_{\\pi_\\theta}\\left[C_{\\text{total}}\\right] \\leq C_{\\text{budget}}\n\\label{eq:objective}\n\\end{equation}\nwhere $C_{\\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section~\\ref{subsec:biavr}).\n\n\n\\subsection{B-IAVR: Selective Self-Verification via RL}\n\\label{subsec:biavr}\n\n\\subsubsection{Overview}\n\nB-IAVR (\\textbf{B}inary \\textbf{I}nformative \\textbf{A}ction \\textbf{V}erification via \\textbf{R}L) trains a language model agent to decide \\textit{when} to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.\n\n\\subsubsection{Selective Verification Policy}\n\nThe agent's generation at each step $t$ is structured as:\n\\begin{equation}\n\\pi(d_t, a_t \\mid h_t) = \\pi_\\theta(d_t \\mid h_t) \\cdot \\pi_\\phi(a_t \\mid h_t, d_t)\n\\label{eq:policy-factorization}\n\\end{equation}\n\nWhen the model generates $\\langle\\text{VERIFY}\\rangle$, a verification subroutine is triggered:\n\\begin{enumerate}\n    \\item The agent produces a preliminary action $a_t^{\\text{pre}}$ via greedy decoding from the current state.\n    \\item The verification module re-examines the observation $o_t$, the proposed action $a_t^{\\text{pre}}$, and the task goal $g$, then generates a verification rationale.\n    \\item Based on the rationale, the agent either confirms $a_t^{\\text{pre}}$ or revises it to $a_t^{\\text{post}}$.\n\\end{enumerate}\n\nWhen $\\langle\\text{SKIP}\\rangle$ is generated, $a_t^{\\text{pre}}$ is directly executed without verification.\n\nIn practice, $\\pi_\\theta$ and $\\pi_\\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.\n\n\\subsubsection{Reward Design}\n\nThe reward function combines three components to balance task performance, verification quality, and cost:\n\n\\paragraph{Task success reward.} A binary episode-level reward indicating whether the task was completed:\n\\begin{equation}\nr_{\\text{task}} = \\begin{cases} r_+ & \\text{if task completed successfully} \\\\ 0 & \\text{otherwise} \\end{cases}\n\\label{eq:task-reward}\n\\end{equation}\n\n\\paragraph{Action-change reward.} A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:\n\\begin{equation}\nr_{\\text{ac}, t} = \\alpha \\cdot d_t \\cdot \\Delta a_t\n\\label{eq:ac-reward}\n\\end{equation}\nwhere $\\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\\Delta a_t = 1$).\n\n\\paragraph{Verification cost penalty.} A step-level penalty for each verification invocation:\n\\begin{equation}\nr_{\\text{cost}, t} = -\\gamma_c \\cdot d_t\n\\label{eq:cost-penalty}\n\\end{equation}\nwhere $\\gamma_c > 0$ is the per-verification cost coefficient.\n\nThe \\textbf{combined reward} for an episode is:\n\\begin{align}\nR &= r_{\\text{task}} + \\sum_{t=1}^{T}\\left(\\beta \\cdot r_{\\text{ac}, t} + r_{\\text{cost}, t}\\right) \\nonumber \\\\\n  &= r_{\\text{task}} + \\sum_{t=1}^{T} d_t \\left(\\beta \\cdot \\alpha \\cdot \\Delta a_t - \\gamma_c\\right)\n\\label{eq:combined-reward}\n\\end{align}\nwhere $\\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:\n\\begin{equation}\n\\gamma_c \\leftarrow \\gamma_c + \\eta_\\gamma \\left(\\mathbb{E}[C_{\\text{total}}] - C_{\\text{budget}}\\right)\n\\label{eq:lagrangian-update}\n\\end{equation}\n\nThis Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\\gamma_c$.\n\n\\paragraph{Interaction between action-change reward and task success.} Note that $r_{\\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome; even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain and provide useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low.\n% TODO: cite exp013f gaming / D012-D013 analysis\n\n\\subsubsection{Training with GRPO}\n\nWe train $\\pi_\\theta$ using Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.\n\nFor each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:\n\\begin{equation}\n\\hat{A}^{(g)}_k = \\frac{R^{(g)}_k - \\text{mean}(\\{R^{(g)}_j\\}_{j=1}^K)}{\\text{std}(\\{R^{(g)}_j\\}_{j=1}^K) + \\epsilon}\n\\label{eq:grpo-advantage}\n\\end{equation}\n\nThe GRPO objective with KL regularization is:\n\\begin{multline}\n\\mathcal{L}_{\\text{GRPO}}(\\theta) = -\\mathbb{E}_{g,k}\\left[\\min\\left(\\rho_t \\hat{A}^{(g)}_k, \\; \\text{clip}(\\rho_t, 1-\\varepsilon, 1+\\varepsilon) \\hat{A}^{(g)}_k\\right)\\right] \\\\\n+ \\lambda_{\\text{KL}} \\, D_{\\text{KL}}(\\pi_\\theta \\| \\pi_{\\text{ref}})\n\\label{eq:grpo-objective}\n\\end{multline}\nwhere $\\rho_t = \\frac{\\pi_\\theta(a_t | h_t)}{\\pi_{\\text{ref}}(a_t | h_t)}$ is the importance ratio and $\\pi_{\\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).\n\n\\paragraph{Step-independent context.} Following the rollout design of verl-agent~\\cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps, a critical factor for training stability in interactive agent settings.\n\n\\subsubsection{Extension: GiGPO for Step-Level Credit Assignment}\n\n% TODO: GiGPO details\n\nA known limitation of episode-level GRPO is that the advantage $\\hat{A}^{(g)}_k$ is shared across all steps within a rollout and provides no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning. A single failed step can assign negative advantage to all preceding correct actions.\n\nGiGPO (Group-in-Group Policy Optimization)~\\cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a \\textit{step-level group} by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:\n\\begin{equation}\n\\hat{A}^{\\text{step}}_t = \\frac{R_t^{>} - \\text{mean}(\\{R^{>}_j\\})}{\\text{std}(\\{R^{>}_j\\}) + \\epsilon}\n\\label{eq:gigpo-advantage}\n\\end{equation}\nwhere $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.\n\nIn the B-IAVR context, GiGPO is particularly well-suited because:\n\\begin{enumerate}\n    \\item \\textbf{Verification decisions are step-level.} The verify/skip decision at step $t$ has localized impact. GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.\n    \\item \\textbf{Action-change reward is already step-level.} The reward $r_{\\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure and provides dense reward signal at the granularity where credit assignment operates.\n    \\item \\textbf{Sparse task reward benefits from decomposition.} When the episode-level task reward $r_{\\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components and mitigate the cold-start problem observed with pure GRPO on sparse rewards.\n\\end{enumerate}\n\n% TODO: exp result — GiGPO vs GRPO training curves, convergence speed comparison\n\n\\subsubsection{Self-Guide Integration}\n\nB-IAVR builds upon the Self-Guide framework~\\cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\\pi_\\phi$ alongside an internal evaluator $V_\\psi$ that scores intermediate states and provides denser reward signal than the sparse environment reward alone.\n\nWe extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\\psi(s_t)$ serves as an additional input feature to the verification policy $\\pi_\\theta(d_t \\mid s_t, V_\\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:\n\\begin{equation}\nP(d_t = 1) \\uparrow \\quad \\text{when} \\quad V_\\psi(s_t) \\text{ is low (uncertain)}\n\\label{eq:selfguide-trigger}\n\\end{equation}\n\nThe co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates. This leads to a progressively refined verification trigger that adapts to the agent's evolving competence.\n\n% TODO: exp result — Self-Guide internal reward correlation with action-change frequency\n\n\n\\subsection{Comparison with Related Methods}\n\\label{subsec:comparison}\n\nWe position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.\n\n\\subsubsection{vs ARES: Adaptive Reasoning Effort Selection}\n\nARES~\\cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison of B-IAVR with ARES across key design dimensions.}\n\\label{tab:ares-comparison}\n\\begin{tabular}{lp{3.2cm}p{3.2cm}}\n\\toprule\n\\textbf{Dimension} & \\textbf{ARES} & \\textbf{B-IAVR (Ours)} \\\\\n\\midrule\n\\textbf{Decision type} & Continuous effort level & Binary verify/skip \\\\\n\\textbf{Training signal} & Pre-defined quality metrics + token efficiency & Action change (behavioral) \\\\\n\\textbf{Data requirement} & Difficulty-annotated data for SFT bootstrap & Environment interaction only \\\\\n\\textbf{Scope} & General reasoning tasks & Interactive agent tasks \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe binary decision in B-IAVR offers two advantages: (1) it is more interpretable, as one can directly audit \\textit{which steps} were verified and \\textit{whether} the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.\n\nConversely, ARES's continuous allocation is more flexible for tasks where ``partial verification'' makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.\n\n\\subsubsection{vs Thinkless: Learning When to Think}\n\nThinkless~\\cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:\n\\begin{itemize}\n    \\item \\textbf{Single-turn vs multi-turn.} Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.\n    \\item \\textbf{Computation type.} Thinkless controls \\textit{internal reasoning} (thinking tokens); B-IAVR controls \\textit{external verification} (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.\n    \\item \\textbf{Reward signal.} Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.\n\\end{itemize}\n\n\\subsubsection{vs Derailer-Rerailer: Adaptive Verification for Reasoning}\n\nDerailer-Rerailer~\\cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect ``derailed'' reasoning steps and trigger correction. Compared to B-IAVR:\n\\begin{itemize}\n    \\item \\textbf{Heuristic vs learned.} Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.\n    \\item \\textbf{Reasoning chains vs agent trajectories.} Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.\n    \\item \\textbf{Correction scope.} Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action and preserves the trajectory structure.\n\\end{itemize}\n\n\\subsubsection{vs Sherlock: Reliable Agentic Workflow Execution}\n\nSherlock~\\cite{sherlock2025} applies selective verification to agentic \\textit{workflows} (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary: Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.\n\n% TODO: exp result — ablation table comparing B-IAVR with always-on / no-verify / random-p / confidence-threshold baselines\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_method-tex-latex_20260520T131951",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method.tex",
    "content": "% method.tex — Method section for B-IAVR paper\n% Converted from method_draft.md\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{subsec:problem-formulation}\n\n\\subsubsection{Interactive Agent as POMDP}\n\nWe formalize the interactive agent task as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = \\langle \\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma \\rangle$, where $\\mathcal{S}$ is the state space of the environment (e.g., object locations and states in a household), $\\mathcal{A}$ is the action space (e.g., natural language commands such as \\texttt{go to shelf 1}, \\texttt{take mug 2}), $\\mathcal{O}$ is the observation space (textual descriptions of the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\Delta(\\mathcal{S})$ is the transition function, $O: \\mathcal{S} \\rightarrow \\Delta(\\mathcal{O})$ is the observation function, $R: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$ is the reward function, and $\\gamma$ is the discount factor.\n\nAt each timestep $t$, the agent receives observation $o_t \\in \\mathcal{O}$ and selects action $a_t \\in \\mathcal{A}$ according to its policy $\\pi_\\phi(a_t \\mid h_t)$, where $h_t = (o_1, a_1, \\ldots, o_t)$ is the interaction history. The episode terminates upon task completion (success) or after a maximum number of steps $T_{\\max}$.\n\n\\subsubsection{Verification Decision}\n\nAt each step $t$, in addition to the primary action $a_t$, the agent makes a binary verification decision:\n\\begin{equation}\nd_t \\in \\{0, 1\\}\n\\label{eq:verify-decision}\n\\end{equation}\nwhere $d_t = 1$ triggers a self-verification subroutine and $d_t = 0$ skips verification. When $d_t = 1$, the agent re-examines its current observation and proposed action, potentially revising $a_t$ to an alternative $a_t'$.\n\nWe parameterize the verification policy as $\\pi_\\theta(d_t \\mid s_t)$, where $s_t$ is a compact representation of the agent's state at step $t$ (including the current observation, proposed action, and task context). In practice, $\\pi_\\theta$ is realized by augmenting the agent's action space with a special control token $\\langle\\text{VERIFY}\\rangle$ that precedes the action output, such that the language model generates either $\\langle\\text{VERIFY}\\rangle\\, a_t$ or $\\langle\\text{SKIP}\\rangle\\, a_t$ at each step.\n\n\\subsubsection{Action-Change Signal}\n\nWe define the \\textbf{action-change indicator} as the primary signal for verification informativeness:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}\\left[a_t^{\\text{post}} \\neq a_t^{\\text{pre}}\\right]\n\\label{eq:action-change}\n\\end{equation}\nwhere $a_t^{\\text{pre}}$ is the action the agent would have taken without verification (obtained via a single greedy decode pass), and $a_t^{\\text{post}}$ is the action after the verification subroutine. Equality is assessed via semantic canonicalization (e.g., mapping actions to $\\langle \\text{verb}, \\text{object}, \\text{receptacle} \\rangle$ tuples in ALFWorld) to avoid spurious mismatches from surface-form variation.\n\nThe key insight is that \\textbf{most self-verification is confirmatory rather than corrective}~\\cite{self-verification-dilemma-2026}. When $\\Delta a_t = 0$, the verification consumed compute without altering behavior; it was uninformative. When $\\Delta a_t = 1$, the verification produced a behavioral change, which indicates it carried decision-relevant information.\n\n\\subsubsection{Verification Cost Model}\n\nEach verification incurs a fixed cost $c_{\\text{verify}}$ (proportional to the additional inference tokens required). The total verification cost for an episode of length $T$ is:\n\\begin{equation}\nC_{\\text{total}} = \\sum_{t=1}^{T} d_t \\cdot c_{\\text{verify}}\n\\label{eq:total-cost}\n\\end{equation}\n\nIn practice, $c_{\\text{verify}}$ corresponds to the additional forward pass needed for the verification subroutine (re-observation, re-reasoning, and potential action revision), which approximately doubles the per-step inference cost.\n\n\\subsubsection{Objective}\n\nThe goal of B-IAVR is to learn a verification policy $\\pi_\\theta$ that maximizes task success while minimizing verification cost. We formulate this as a constrained optimization problem:\n\\begin{equation}\n\\max_\\theta \\; \\mathbb{E}_{\\pi_\\theta, \\pi_\\phi}\\left[\\sum_{t=1}^{T} R(s_t, a_t)\\right] \\quad \\text{s.t.} \\quad \\mathbb{E}_{\\pi_\\theta}\\left[C_{\\text{total}}\\right] \\leq C_{\\text{budget}}\n\\label{eq:objective}\n\\end{equation}\nwhere $C_{\\text{budget}}$ is the verification budget constraint. In practice, we relax this to an unconstrained objective via Lagrangian relaxation (Section~\\ref{subsec:biavr}).\n\n\n\\subsection{B-IAVR: Selective Self-Verification via RL}\n\\label{subsec:biavr}\n\n\\subsubsection{Overview}\n\nB-IAVR (\\textbf{B}inary \\textbf{I}nformative \\textbf{A}ction \\textbf{V}erification via \\textbf{R}L) trains a language model agent to decide \\textit{when} to invoke self-verification, using action change as a reward signal for verification informativeness. The method consists of three components: (1) a selective verification policy that makes per-step binary verify/skip decisions, (2) a composite reward function combining task success, verification informativeness, and cost, and (3) an RL training procedure based on GRPO with optional GiGPO extension for step-level credit assignment.\n\n\\subsubsection{Selective Verification Policy}\n\nThe agent's generation at each step $t$ is structured as:\n\\begin{equation}\n\\pi(d_t, a_t \\mid h_t) = \\pi_\\theta(d_t \\mid h_t) \\cdot \\pi_\\phi(a_t \\mid h_t, d_t)\n\\label{eq:policy-factorization}\n\\end{equation}\n\nWhen the model generates $\\langle\\text{VERIFY}\\rangle$, a verification subroutine is triggered:\n\\begin{enumerate}\n    \\item The agent produces a preliminary action $a_t^{\\text{pre}}$ via greedy decoding from the current state.\n    \\item The verification module re-examines the observation $o_t$, the proposed action $a_t^{\\text{pre}}$, and the task goal $g$, then generates a verification rationale.\n    \\item Based on the rationale, the agent either confirms $a_t^{\\text{pre}}$ or revises it to $a_t^{\\text{post}}$.\n\\end{enumerate}\n\nWhen $\\langle\\text{SKIP}\\rangle$ is generated, $a_t^{\\text{pre}}$ is directly executed without verification.\n\nIn practice, $\\pi_\\theta$ and $\\pi_\\phi$ share the same language model backbone, with the verification decision encoded as a special token prefix. This avoids the overhead of maintaining separate models and allows end-to-end RL training.\n\n\\subsubsection{Reward Design}\n\nThe reward function combines three components to balance task performance, verification quality, and cost:\n\n\\paragraph{Task success reward.} A binary episode-level reward indicating whether the task was completed:\n\\begin{equation}\nr_{\\text{task}} = \\begin{cases} r_+ & \\text{if task completed successfully} \\\\ 0 & \\text{otherwise} \\end{cases}\n\\label{eq:task-reward}\n\\end{equation}\n\n\\paragraph{Action-change reward.} A step-level reward given when verification produces a behavioral change, serving as a proxy for verification informativeness:\n\\begin{equation}\nr_{\\text{ac}, t} = \\alpha \\cdot d_t \\cdot \\Delta a_t\n\\label{eq:ac-reward}\n\\end{equation}\nwhere $\\alpha > 0$ controls the magnitude of the informativeness bonus. This reward is only assigned at steps where verification is triggered ($d_t = 1$) and the action changes ($\\Delta a_t = 1$).\n\n\\paragraph{Verification cost penalty.} A step-level penalty for each verification invocation:\n\\begin{equation}\nr_{\\text{cost}, t} = -\\gamma_c \\cdot d_t\n\\label{eq:cost-penalty}\n\\end{equation}\nwhere $\\gamma_c > 0$ is the per-verification cost coefficient.\n\nThe \\textbf{combined reward} for an episode is:\n\\begin{align}\nR &= r_{\\text{task}} + \\sum_{t=1}^{T}\\left(\\beta \\cdot r_{\\text{ac}, t} + r_{\\text{cost}, t}\\right) \\nonumber \\\\\n  &= r_{\\text{task}} + \\sum_{t=1}^{T} d_t \\left(\\beta \\cdot \\alpha \\cdot \\Delta a_t - \\gamma_c\\right)\n\\label{eq:combined-reward}\n\\end{align}\nwhere $\\beta$ balances the informativeness bonus against the cost penalty. The cost coefficient $\\gamma_c$ is updated via dual gradient ascent to enforce the budget constraint:\n\\begin{equation}\n\\gamma_c \\leftarrow \\gamma_c + \\eta_\\gamma \\left(\\mathbb{E}[C_{\\text{total}}] - C_{\\text{budget}}\\right)\n\\label{eq:lagrangian-update}\n\\end{equation}\n\nThis Lagrangian formulation allows the agent to learn a cost-performance tradeoff without hand-tuning $\\gamma_c$.\n\n\\paragraph{Interaction between action-change reward and task success.} Note that $r_{\\text{ac}}$ is not gated on task success. A verification that changes the action is informative regardless of episode outcome; even in failed episodes, action changes driven by verification reveal that the agent's initial action was uncertain and provide useful training signal. This design choice avoids the bootstrap problem encountered with success-gated rewards when base success rates are low.\n% TODO: cite exp013f gaming / D012-D013 analysis\n\n\\subsubsection{Training with GRPO}\n\nWe train $\\pi_\\theta$ using Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, which estimates advantages from groups of rollouts without requiring a learned value function.\n\nFor each training step, we sample $G$ groups of $K$ rollouts per task instance. Within each group $g$, the advantage of rollout $k$ is computed as:\n\\begin{equation}\n\\hat{A}^{(g)}_k = \\frac{R^{(g)}_k - \\text{mean}(\\{R^{(g)}_j\\}_{j=1}^K)}{\\text{std}(\\{R^{(g)}_j\\}_{j=1}^K) + \\epsilon}\n\\label{eq:grpo-advantage}\n\\end{equation}\n\nThe GRPO objective with KL regularization is:\n\\begin{multline}\n\\mathcal{L}_{\\text{GRPO}}(\\theta) = -\\mathbb{E}_{g,k}\\left[\\min\\left(\\rho_t \\hat{A}^{(g)}_k, \\; \\text{clip}(\\rho_t, 1-\\varepsilon, 1+\\varepsilon) \\hat{A}^{(g)}_k\\right)\\right] \\\\\n+ \\lambda_{\\text{KL}} \\, D_{\\text{KL}}(\\pi_\\theta \\| \\pi_{\\text{ref}})\n\\label{eq:grpo-objective}\n\\end{multline}\nwhere $\\rho_t = \\frac{\\pi_\\theta(a_t | h_t)}{\\pi_{\\text{ref}}(a_t | h_t)}$ is the importance ratio and $\\pi_{\\text{ref}}$ is the reference policy (initialized from the SFT checkpoint).\n\n\\paragraph{Step-independent context.} Following the rollout design of verl-agent~\\cite{selfguide2026}, we employ step-independent context for multi-turn rollouts: at each step, the model receives only the current observation and task context rather than the full interaction history. This prevents context length explosion in long-horizon tasks and maintains consistent inference quality across steps, a critical factor for training stability in interactive agent settings.\n\n\\subsubsection{Extension: GiGPO for Step-Level Credit Assignment}\n\n% TODO: GiGPO details\n\nA known limitation of episode-level GRPO is that the advantage $\\hat{A}^{(g)}_k$ is shared across all steps within a rollout and provides no step-level credit assignment. In multi-turn agent tasks where episodes span 10--30 steps, this leads to high variance and slow learning. A single failed step can assign negative advantage to all preceding correct actions.\n\nGiGPO (Group-in-Group Policy Optimization)~\\cite{feng2025gigpo} addresses this via a nested group structure. For each step $t$ within a rollout, GiGPO constructs a \\textit{step-level group} by comparing the outcomes of rollouts that share the same prefix up to step $t-1$ but diverge at step $t$:\n\\begin{equation}\n\\hat{A}^{\\text{step}}_t = \\frac{R_t^{>} - \\text{mean}(\\{R^{>}_j\\})}{\\text{std}(\\{R^{>}_j\\}) + \\epsilon}\n\\label{eq:gigpo-advantage}\n\\end{equation}\nwhere $R_t^{>}$ denotes the cumulative reward from step $t$ onward. This provides dense, step-level learning signal without requiring a learned critic.\n\nIn the B-IAVR context, GiGPO is particularly well-suited because:\n\\begin{enumerate}\n    \\item \\textbf{Verification decisions are step-level.} The verify/skip decision at step $t$ has localized impact. GiGPO can attribute the outcome change to the specific verification decision rather than spreading credit across the entire episode.\n    \\item \\textbf{Action-change reward is already step-level.} The reward $r_{\\text{ac},t}$ naturally aligns with GiGPO's step-level advantage structure and provides dense reward signal at the granularity where credit assignment operates.\n    \\item \\textbf{Sparse task reward benefits from decomposition.} When the episode-level task reward $r_{\\text{task}}$ is binary and sparse, GiGPO's step-level groups break the learning signal into denser components and mitigate the cold-start problem observed with pure GRPO on sparse rewards.\n\\end{enumerate}\n\n% TODO: exp result — GiGPO vs GRPO training curves, convergence speed comparison\n\n\\subsubsection{Self-Guide Integration}\n\nB-IAVR builds upon the Self-Guide framework~\\cite{selfguide2026}, which co-evolves a task policy and an internal reward model through iterative RL training. Specifically, Self-Guide trains a policy $\\pi_\\phi$ alongside an internal evaluator $V_\\psi$ that scores intermediate states and provides denser reward signal than the sparse environment reward alone.\n\nWe extend Self-Guide by introducing the verification decision layer: the internal evaluator $V_\\psi(s_t)$ serves as an additional input feature to the verification policy $\\pi_\\theta(d_t \\mid s_t, V_\\psi(s_t))$. Intuitively, when the internal evaluator assigns low confidence to the current state (indicating the agent is uncertain about its action), verification is more likely to be informative. This creates a natural trigger mechanism:\n\\begin{equation}\nP(d_t = 1) \\uparrow \\quad \\text{when} \\quad V_\\psi(s_t) \\text{ is low (uncertain)}\n\\label{eq:selfguide-trigger}\n\\end{equation}\n\nThe co-evolution property of Self-Guide ensures that as the task policy improves, the internal evaluator also calibrates. This leads to a progressively refined verification trigger that adapts to the agent's evolving competence.\n\n% TODO: exp result — Self-Guide internal reward correlation with action-change frequency\n\n\n\\subsection{Comparison with Related Methods}\n\\label{subsec:comparison}\n\nWe position B-IAVR against three categories of related methods: adaptive reasoning effort, selective verification, and self-correction in agents.\n\n\\subsubsection{vs ARES: Adaptive Reasoning Effort Selection}\n\nARES~\\cite{yang2026ares} trains an SFT-initialized router to allocate continuous reasoning effort per step, optimized via GRPO with a combined outcome and token-efficiency reward. B-IAVR differs in three fundamental aspects:\n\n\\begin{table}[t]\n\\centering\n\\caption{Comparison of B-IAVR with ARES across key design dimensions.}\n\\label{tab:ares-comparison}\n\\begin{tabular}{lp{3.2cm}p{3.2cm}}\n\\toprule\n\\textbf{Dimension} & \\textbf{ARES} & \\textbf{B-IAVR (Ours)} \\\\\n\\midrule\n\\textbf{Decision type} & Continuous effort level & Binary verify/skip \\\\\n\\textbf{Training signal} & Pre-defined quality metrics + token efficiency & Action change (behavioral) \\\\\n\\textbf{Data requirement} & Difficulty-annotated data for SFT bootstrap & Environment interaction only \\\\\n\\textbf{Scope} & General reasoning tasks & Interactive agent tasks \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe binary decision in B-IAVR offers two advantages: (1) it is more interpretable, as one can directly audit \\textit{which steps} were verified and \\textit{whether} the verification changed behavior, and (2) it avoids the need for difficulty annotations, as the action-change signal is self-supervised from the agent's own behavioral variation.\n\nConversely, ARES's continuous allocation is more flexible for tasks where ``partial verification'' makes sense. B-IAVR's binary design is motivated by the interactive agent setting, where verification is a discrete subroutine (re-observe environment, re-reason, potentially revise) that is either invoked or not.\n\n\\subsubsection{vs Thinkless: Learning When to Think}\n\nThinkless~\\cite{du2025thinkless} uses RL to train a control token that decides whether to invoke extended thinking (chain-of-thought) before answering. While methodologically parallel to B-IAVR (both learn a binary computation trigger via RL), they address different settings:\n\\begin{itemize}\n    \\item \\textbf{Single-turn vs multi-turn.} Thinkless operates on single-turn QA; B-IAVR on multi-step interactive agent trajectories where each decision depends on environment feedback.\n    \\item \\textbf{Computation type.} Thinkless controls \\textit{internal reasoning} (thinking tokens); B-IAVR controls \\textit{external verification} (re-observation of the environment), grounding the signal in behavioral change rather than token-level computation.\n    \\item \\textbf{Reward signal.} Thinkless uses task correctness; B-IAVR introduces the action-change signal as a verification-specific informativeness measure.\n\\end{itemize}\n\n\\subsubsection{vs Derailer-Rerailer: Adaptive Verification for Reasoning}\n\nDerailer-Rerailer~\\cite{wan2025derailer-rerailer} uses a heuristic instability signal to detect ``derailed'' reasoning steps and trigger correction. Compared to B-IAVR:\n\\begin{itemize}\n    \\item \\textbf{Heuristic vs learned.} Derailer-Rerailer relies on hand-designed instability metrics; B-IAVR learns the verification trigger end-to-end via RL. This eliminates the need for task-specific heuristic engineering and allows the trigger to adapt as the policy improves.\n    \\item \\textbf{Reasoning chains vs agent trajectories.} Derailer-Rerailer operates on single-turn reasoning chains; B-IAVR on multi-turn agent trajectories with environment interaction. The environment provides a concrete grounding signal (observation changes) absent in pure reasoning settings.\n    \\item \\textbf{Correction scope.} Derailer-Rerailer re-generates from the derailed step; B-IAVR's verification may confirm or revise a single action and preserves the trajectory structure.\n\\end{itemize}\n\n\\subsubsection{vs Sherlock: Reliable Agentic Workflow Execution}\n\nSherlock~\\cite{sherlock2025} applies selective verification to agentic \\textit{workflows} (DAG-structured task plans) using offline counterfactual analysis and speculative execution. The key distinction is the level of abstraction: Sherlock verifies workflow nodes (coarse-grained, offline planning); B-IAVR verifies individual agent actions (fine-grained, online decision-making). The two approaches are complementary: Sherlock could serve as a workflow-level planner while B-IAVR handles step-level verification within each workflow node.\n\n% TODO: exp result — ablation table comparing B-IAVR with always-on / no-verify / random-p / confidence-threshold baselines\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T13:26:00.062805+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_method-tex-latex_20260520T131951",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T13:26:00.062995+00:00_

已写入 `method.tex`。转换要点：

- Markdown 标题 → `\section` / `\subsection` / `\subsubsection`，均加 `\label`
- 所有 display math → `equation` / `align` / `multline` 环境，带编号和 label（共 15 个公式）
- 加粗段落标题（Task success reward 等） → `\paragraph{}`
- 表格 → booktabs 格式（`\toprule` / `\midrule` / `\bottomrule`），`p{3.2cm}` 列宽自动换行
- 有序/无序列表 → `enumerate` / `itemize`
- 行内代码 → `\texttt{}`，强调 → `\textit{}`，加粗 → `\textbf{}`
- 引用 `\cite{}` 前加 `~` 防断行
- em-dash（`---`）已替换为分号/句号（遵守写作规范 §5.1）
- `-ing` 短语结尾处做了最小化改写（如 "indicating..." → "which indicates..."）
- HTML 注释（Director 决策点）已删除
- `[TBD]` 标记转为 `% TODO:` LaTeX 注释
- 引号 → LaTeX 格式（` `` '' `）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_method-tex-latex_20260520T131951"
}
```

</details>

---
