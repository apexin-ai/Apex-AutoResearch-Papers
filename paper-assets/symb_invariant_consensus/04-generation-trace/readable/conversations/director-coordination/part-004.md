# Director coordination — Part 4 of 9

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/bd/bdd0e6c8e8a0a8a81e76.json)

## Round 68

### Tool result

_source line 1043 · 2026-05-21T07:44:44.738345+00:00_

1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. $K_{\text{eff}}$ should be interpreted as an ordinal diagnostic---ranking which conditions have genuine vote diversity---rather than as a literal effective sample size. Fleiss' $\kappa$ is a chance-corrected agreement measure, not identical to the ICC ($\rho$) in \citeauthor{kish1965survey}'s (\citeyear{kish1965survey}) original formula; we validated their monotonic relationship empirically (mean pairwise $r = 0.625$ across model families). This \emph{independence bottleneck} motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K
…[truncated 5124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-21T07:44:44.738836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-21T07:44:45.643722+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions (sorted by SC). No non-degenerate condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; $\dagger$\,$n < 100$; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.112$); {***}\,oracle $p < 0.001$; $^{4s}$\,4-seed confirmatory (unmarked: sing
…[truncated 3803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-21T07:44:45.644212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-21T07:44:46.096454+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	We test the three predictions of the Symbolic Mirage hypothesis (\S\ref{sec:mirage}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. Across four Mistral-7B seeds, $\kappa \in [0.41, 0.51]$ yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp, indicating seed-level constraint quality matters beyond independence. Positive $\Delta$ requires both sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ degrades). All four model families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3pt}
15	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$ (uncorrected; BH adj.\ $p = 0.112$, $m{=}16$); positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
16	\label{tab:independence}
17	\begin{tabular}{@{}llccrr@{}}
18	\toprule
19	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $\Delta$ (pp) \\
20	\midrule
21	Qwen3 (think) & FOLIO & 0.91 & 1.09 & ${\sim}$84 & ${\sim}$0 \\
22	Qwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\
23	Qwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\
24	Qwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\
25	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\
26	\addlinespace
27	Mistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\
28	Mistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\
29	Mistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\
30	Mi
…[truncated 4143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-21T07:44:46.097060+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-21T07:44:46.198002+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 126\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-21T07:44:52.880638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-21T07:44:53.367529+00:00_

1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), whose (premise, conclusion) structure suits NLI classification.
7	
8	\paragraph{Main result.}
9	DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo mode yields $+0.49$\,pp at $w{=}1$ and $+2.94$\,pp at $w{=}3$ (both n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.112$; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). We report $w{=}3$ as primary. After BH correction ($m{=}12$), Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$) remain significant; all other conditions are non-significant.
10	
11	\paragraph{Why it works.}
12	Three conditions jointly enable the escape: (i) \emph{structural independence}---encoder-only DeBERTa (406M) and decoder-only Mistral (7B) share no architecture or training data, satisfying the independence condition that same-model sampling cannot provide (\S\ref{sec:mirage}); (ii) \emph{positive capability gap}---the verifier's standalone accuracy exceeds the generator's SC (Observation~2); (iii) \emph{task-verifier alignment}---the NLI classification format naturally matches the premise-conclusion structure of logical reasoning tasks. Per-label complementarity emerges:
…[truncated 4091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 486
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-21T07:44:53.367932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-21T07:44:53.870532+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Self-verification generalization.}
5	The Symbolic Mirage operates through two channels: correlated constraints compress $K_{\text{eff}} < 2$ (\emph{direct}), while answer-coupled constraints collapse MAX-SAT to vote counting (\emph{indirect}; Eq.~\ref{eq:degenerate}). \citet{huang2024selfcorrect} and \citet{stechly2025selfverification} observe that LLMs cannot self-correct without external feedback; our bias ratio ($4.97\times$ Mistral, $3.93\times$ Qwen, $2.88\times$ LLaMA) quantifies why: extraction and generation share the same distributional biases. $\text{BR} > 1$ across three families predicts that any self-verification pipeline deriving criteria from the same model faces this bottleneck, whether formal constraints, natural-language critiques, or code assertions.
6	
7	\paragraph{Test-time scaling and ensemble diversity.}
8	$K_{\text{eff}} = 1.20$--$3.62$ for nominal $K = 12$ means sampling beyond a dozen traces yields diminishing independent information, and the pattern intensifies with capability: Qwen3 thinking mode ($\kappa = 0.91$, $K_{\text{eff}} = 1.09$) produces near-deterministic traces, creating a scaling paradox for o1/R1-style reasoning models \citep{guo2025deepseekr1}. The $\kappa$ floor is universal---all non-destructive interventions cluster at $\kappa \geq 0.40$ (Table~\ref{tab:kappa_generalization}), confirming a structural ceiling. This instantiates the classic ensemble tension \citep{krogh1994neural, brown2005diversity}: Debate raises $K_{\text{eff}}$ from ${\sim}1.8$ to ${\sim}4.5$ but collapses accuracy ($-18.6$\,pp, $p < 0.001$), because diversity-inducing perturbations degrade predictions rather than introducing independent reasoning. Cross-architecture escape succeeds (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$) precisely because encoder-only DeBERTa and decoder-only LLMs have structurally different error profiles. If traces do not faithfully reflect reasoning \citep{turpin
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-21T07:44:53.870898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-21T07:44:54.322931+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We identify the Symbolic Mirage: self-extracted constraints inherit the generating model's biases ($\text{BR} = 4.97\times$, 83.3\%), explaining why twenty-seven remediation strategies fail. Oracle controls ($+29.90$/$+14.22$\,pp) confirm the mechanism is sound; the bottleneck is extraction quality, not the formal channel. Three diagnostics predict failure ($C_0 < 5\%$, SC $\leq 40\%$, process similarity). Cross-architecture NLI escapes the mirage when the verifier exceeds the generator ($\rho = 1.0$, $p = 0.003$); DRC recovers 90\% of this gain at 39\% cost.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-21T07:44:54.323301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-21T07:44:55.127019+00:00_

1	\paragraph{Scale and language.}
2	All models range from 7B to 32B parameters; whether the independence bottleneck persists at larger scales (70B+) or with reasoning-specialized models is untested. All datasets are English-language logical reasoning benchmarks with discrete answer spaces. We do not evaluate trained symbolic extractors, external solvers with verified grounding, or multilingual settings. Oracle analysis is limited to FOLIO and ProofWriter (gold annotations available); extending to commonsense reasoning requires constructing comparable gold constraint sets. The cross-architecture NLI verifier (\S\ref{sec:cross-arch}) provides no benefit on LogiQA (combo $\Delta \leq +1$\,pp, all $p > 0.5$), indicating that cross-architecture escape requires task-verifier alignment---NLI is effective only when the task naturally decomposes into premise-conclusion entailment. Even on compatible tasks, NLI gain vanishes when the capability gap is large (Qwen3-14B ProofWriter: SC 85.83\% vs.\ DeBERTa 55\%, gap $= -30.83$\,pp, $\Delta \leq +0.50$\,pp, n.s.), and moderate negative gaps yield small, non-significant gains (LLaMA-3.1-8B: gap $= -17.50$\,pp, $+0.83$\,pp, n.s.; \S\ref{sec:cross-arch}). Scaling the cross-architecture approach---via trained verifiers, code-based symbolic execution, or multi-verifier ensembles---remains unexplored and may extend the escape to stronger generators and broader task types.
3	
4	\paragraph{Statistical power.}
5	McNemar power for detecting $|\Delta| = 2$\,pp is below 21\% at $n{=}200$--$600$; our tests are adequately powered only for $|\Delta| \geq 5$\,pp, meaning small true effects may go undetected. The per-label complementarity analysis of the cross-architecture NLI result (\S\ref{sec:cross-arch}) involves small cell sizes (e.g., 42 \textsc{False} problems, 69 \textsc{Unknown} problems); per-label McNemar tests would be underpowered. The bias ratio metric ($4.97\times$) was initially computed on a single condition (Mistral-7B FOLIO, $
…[truncated 1490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-21T07:44:55.127508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-21T07:44:55.178106+00:00_

1	
2	\section{Regime Scatter Plot}
3	\label{app:regime-scatter}
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{f2_regime_scatter}
8	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.112$).}
9	\label{fig:regime-scatter}
10	\end{figure}
11	
12	\section{Prompt Templates}
13	\label{app:prompts}
14	
15	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
16	
17	\paragraph{System Prompt.}
18	
19	\begin{lstlisting}
20	You are a constraint extraction tool. Output ONLY
21	valid JSON. Do NOT solve problems, reason about
22	correctness, or think step-by-step. Extract
23	constraints from the given trace exactly as stated.
24	\end{lstlisting}
25	
26	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
27	
28	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
29	
30	\begin{lstlisting}
31	Extract mathematical constraints from this reasoning
32	trace as a JSON object.
33	
34	Rules:
35	- type: "equation", "inequality", or "predicate"
36	- expression: human-readable, e.g. "x + y == 14"
37	- z3_formula: a single comparison expression in
38	  Python Z3 syntax
39	- source_step: step number where the constraint
40	  appears
41	- Use variable names from the trace
42	
43	z3_formula MUST follow these rules:
44	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
45	  /, **, %
46	- Use individual named varia
…[truncated 3292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-21T07:45:00.613172+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ROADMAP.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "ROADMAP.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-21T07:45:02.023196+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ROADMAP.md\", \"content\": \"# symb_invariant_consensus — Research Dashboard\\n\\n> 最后更新: 2026-05-21 07:38 UTC | 更新原因: Revert LLaMA BR 3.87→2.88 (bootstrap used wrong error definition)\\n\\n> 核心方向详见 paper_framing.md。\\n\\n## 核心方向\\n**Symbolic Mirage**: Self-extracted logical constraints project model bias, not independent verification. Quantified via BR (4.97×), Eff-K (ordinal), process-κ diagnostics. Cross-architecture NLI escape: narrow PoC — only Mistral (positive gap) shows significant gains after BH correction.\\n\\n## 当前阶段\\n**V14 → V15 修复中** — R10 fresh review 3.0 (Findings)，17 项修复 + 计算任务完成，Paper Agent 整合最终数据中。目标 3.5 Borderline Conference。\\n\\n**论文状态（V14→V15 进行中）**：\\n- Batch 1-3 (C1-C5, W1-W8) ✅\\n- TOST 5/5/6 → 4/2/10 修正中（Lakens 2017 标准）\\n- BR CI 整合中（Mistral [3.98,6.37], Qwen [2.44,7.11]; LLaMA raw CI 需重算）\\n- LLaMA BR revert 3.87→2.88（bootstrap 用了错误定义，M057）\\n- 3 missing citations 整合中\\n- DRC §6.1: τ=0.7 recovers 90% gain at 39% NLI cost\\n\\n**关键统计（corrected）**：\\n- PW 6-point (3 NLI verifiers × Mistral + DeBERTa × 4 generators): Spearman ρ=1.0, exact p=0.003\\n- BH m=12: only Mistral w=3 (adj p=6.78e-05) + w=5 (adj p=7.41e-06) survive\\n- Cross-arch: 1/4 generators significant (Mistral)\\n- TOST ±2pp: 4 equivalent / 2 different / 10 underpowered\\n- BR: 4.97× (Mistral, CI [3.98,6.37]), 3.93× (Qwen, CI [2.44,7.11]), 2.88× (LLaMA, 4-trace†)\\n- Weighted BR: 4.24× (Mistral), 3.69× (Qwen), 2.66× (LLaMA, CI [2.19,3.28]) — 同一实验设计\\n\\n## 进行中\\n**Paper Agent**（最终整合）：\\n- TOST 4/2/10 修正 + sensitivity table\\n- LLaMA BR revert 3.87→2.88 + 数据来源脚注\\n- 3 missing citations (wan2025, jhaveri2026, miya2025)\\n- 编译 V15\\n\\n## 近期任务\\n- [x] Paper Agent: Batch 1-3 (C1-C5, W1-W8)\\n- [x] Agent: BR CI + TOST sensitivity + missing citations\\n- [ ] Paper Agent: TOST 修正 + LLaMA BR revert + citations → V15\\n- [ ] 编译 V15 + consistency check\
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-21T07:45:02.531139+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-21T07:45:03.486622+00:00_

&lt;persisted-output>
Output too large (35.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-review-director-9c155b71/8e74cb1a-2ae1-4982-b955-c4990bc93aec/tool-results/bjsfeunjt.txt

Preview (first 2KB):
# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-21T07:45:03.990109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/config*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/*.yaml 2>/dev/null | head -20",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/config*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/*.yaml 2>/dev/null | head -20",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-21T07:45:04.746067+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-21T07:45:04.796735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-21T07:45:04.847653+00:00_

1	% References for SICA paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% SAT-Based Reasoning %%%
5	
6	@inproceedings{ye2024satlm,
7	  title={SatLM: Satisfiability-Aided Language Models Using Declarative Prompting},
8	  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},
9	  booktitle={Advances in Neural Information Processing Systems},
10	  volume={36},
11	  year={2024}
12	}
13	
14	%%% Program-Aided Reasoning %%%
15	
16	@inproceedings{gao2023pal,
17	  title={{PAL}: Program-aided Language Models},
18	  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
19	  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},
20	  year={2023}
21	}
22	
23	@article{chen2023program,
24	  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
25	  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
26	  journal={Transactions on Machine Learning Research},
27	  year={2023}
28	}
29	
30	@inproceedings{lyu2023faithful,
31	  title={Faithful Chain-of-Thought Reasoning},
32	  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},
33	  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
34	  year={2023}
35	}
36	
37	%%% Theoretical Foundations %%%
38	
39	@book{condorcet1785,
40	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
41	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
42	  year={1785},
43	  publisher={Imprimerie Royale},
44	  address={Paris}
45	}
46	
47	@article{austensmith1996,
48	  title={Information Aggregation, Rationality
…[truncated 143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-21T07:45:11.285530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config in project config"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-21T07:45:12.141003+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-21T07:45:12.141513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex 2>/dev/null",
  "description": "List all paper tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex 2>/dev/null",
    "description": "List all paper tex files"
  }
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-21T07:45:12.243271+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-21T07:45:30.389704+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"status: (open|in_progress)\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -30",
  "description": "Find open/in_progress review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"status: (open|in_progress)\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -30",
    "description": "Find open/in_progress review issues"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-21T07:45:30.841664+00:00_

  status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
      status: in_progress
  status: in_progress
  status: in_progress
      status: in_progress

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-21T07:45:30.943089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-21T07:45:30.993905+00:00_

150	 "source_step": -1}
151	\end{lstlisting}
152	
153	\paragraph{Prompt Selection Logic.}
154	
155	Domain assignment is determined by dataset: FOLIO and ProofWriter use \textsc{Logic\_Extraction\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \textsc{Extraction\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.
156	
157	
158	\section{Z3 MaxSAT Evaluation Pseudocode}
159	\label{app:z3-pseudocode}
160	
161	Algorithm~\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\ref{alg:scorer} describes the source-trace attribution scoring.
162	
163	Domain constraint variables (e.g., \texttt{x + y == 14}) and answer assertion variables (e.g., \texttt{\_\_sica\_answer\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.
164	
165	\begin{algorithm}[h]
166	\caption{Z3 Weighted Partial MAX-SAT}
167	\label{alg:maxsat}
168	\begin{algorithmic}[1]
169	\Require Deduplicated constraint set $\mathcal{C} = \{(c_m, w_m, S_m)\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices
170	\Ensure Partition $(\mathcal{C}^*, \mathcal{C}^{\setminus})$ where $\mathcal{C}^*$ is the max-weight satisfiable subset
171	\State $\textit{opt} \gets \textsc{Z3.Optimize()}$
172	\For{$m = 1, \ldots, M$}
173	    \State $b_m \gets$ fresh Boolean indicator
174	    \State $\textit{opt}.\textsc{Add}(b_m \Rightarrow c_m)$ \Comment{soft clause guarded by indicator}
175	    \State $\textit{opt}.\textsc{AddSoft}(b_m,\; \text{weight}=w_m)$
176	\EndFor
177	\State $\textit{result} \gets \textit{opt}.\textsc{Check}()$
178	\State 
…[truncated 13462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-21T07:45:42.066010+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B3 \"status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"(id:|summary:)\" | head -40",
  "description": "Get in_progress issue IDs and summaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B3 \"status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"(id:|summary:)\" | head -40",
    "description": "Get in_progress issue IDs and summaries"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-21T07:45:42.116768+00:00_

  summary: "Eff-K Kish (1965) attribution / κ→ICC proxy rigor"
  summary: "CJT novelty / Huang-Stechly distinction insufficient"
  summary: "Novelty vs self-correction literature (Huang/Stechly/Amonkar)"
  summary: "'Symbolic Mirage' terminology too marketing-like"
  summary: "Cross-architecture PoC underpowered: single generator × inconsistent dataset results"
  summary: "κ→Effective-K 映射形式化不足"
  summary: "NLI combo weight parameter w 未交叉验证"
  summary: "Capability Gap Hypothesis 基于极小样本 (n=6)"
  summary: "T_ext=0.3 extraction temperature 缺 sensitivity analysis"
  summary: "相对于 Huang/Stechly 的增量新颖性不足"
  summary: "Independence-Accuracy Trade-off 作为贡献存在部分同义反复"
  summary: "遗漏关键相关工作：SatLM 对比不充分"
  summary: "Abstract 'sixteen' vs §4.2 'fifteen' 数字不一致"
  summary: "Cross-architecture escape 实验规模不足"
  summary: "术语品牌化过多"
  summary: "σ(c,a) provenance-based 设计未作为 design limitation 讨论"
  summary: "Pages 1-3 连续 3 页纯文本无 display item"
  summary: "Page 8 Conclusion 仓促"
  summary: "Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem"
  summary: "κ→K_eff 映射理论基础不足——r=0.625 验证弱，ordinal caveat 与 quantitative usage 矛盾"
  summary: "Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点"
  summary: "DRC τ 阈值无 held-out 评估"
  summary: "Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)"
  summary: "四种子复制方差大 + 统计功效 <21%"
  summary: "TOST ±2pp margin 缺少显式理由"
  summary: "Bias Ratio 无置信区间"
  summary: "SatLM specification-generation vs SICA trace-extraction 对比不充分"
  summary: "'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分"
  summary: "Related Work 过度压缩——引用列表而非文献讨论"
  summary: "27 种修复策略在正文中展示不足"
  summary: "Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑"
  summary: "缺失引用：CoT confirmation bias 文献 + Eidoku + Tree of Thoughts"
  summary: "Pages 3-5 连续无 display item；page 7 display items 过度拥挤"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1078 · 2026-05-21T07:45:58.677759+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-21T07:46:17.644069+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18966
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-21T07:46:17.846068+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验可靠性**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（strict），参考文献不限，Limitations 必须但不计入页数\n- **模板**: ACL 2023 style（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/symb_invariant_consensus/docs/paper/main.tex`\nPDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 你的审查侧重\n1. **方法论严谨性**：SICA pipeline 的形式化是否完备？Eq.(1)-(5) 的推导和假设是否合理？Symbolic Mirage Hypothesis 的理论基础是否充分？Proposition 1 / Observation 2 的数学形式是否严格？\n2. **统计分析**：McNemar 检验 + BH 校正是否恰当？TOST 等价性检验的 margin 选择 (±2pp) 是否有依据？Bootstrap CI 计算方法是否正确？统计功效是否在论文中充分讨论？\n3. **实验设计**：模型覆盖 (6 models, 7B-32B) 和数据集选择 (FOLIO/ProofWriter/LogiQA) 是否充分？$K=12$, $T=0.7$, $\\alpha=0.5$ 等超参数选择是否合理？Oracle 控制实验是否设计良好？27 种 remediation 策略的覆盖面和公平性如何？\n4. **Cross-architecture NLI 实验**：Spearman ρ=1.0 (n=6) 的统计可靠性？DRC 方法的 τ 阈值选择方式？NLI combo 的 w 参数设置？BH 校正后仅 2/12 条件显著——claim 是否过度？\n5. **可复现性**：是否提供了足够的实验细节（prompt templates, hyperparameters, random seeds, computational cost）？\n\n请按 ARR 审稿标准给出完整审稿报告，包括 Summary、Strengths、Weaknesses（按 critical/warning/info 分级）、Questions、Overall Assessment（使用 EMNLP 2026 评分标准 1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验可靠性**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（strict），参考文献不限，Limitations 必须但不计入页数\n- **模板**: ACL 2023 style（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/symb_invariant_consensus/docs/paper/main.tex`\nPDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 你的审查侧重\n1. **方法论严谨性**：SICA pipeline 的形式化是否完备？Eq.(1)-(5) 的推导和假设是否合理？Symbolic Mirage Hypothesis 的理论基础是否充分？Proposition 1 / Observation 2 的数学形式是否严格？\n2. **统计分析**：McNemar 检验 + BH 校正是否恰当？TOST 等价性检验的 margin 选择 (±2pp) 是否有依据？Bootstrap CI 计算方法是否正确？统计功效是否在论文中充分讨论？\n3. **实验设计**：模型覆盖 (6 models, 7B-32B) 和数据集选择 (FOLIO/ProofWriter/LogiQA) 是否充分？$K=12$, $T=0.7$, $\\alpha=0.5$ 等超参数选择是否合理？Oracle 控制实验是否设计良好？27 种 remediation 策略的覆盖面和公平性如何？\n4. **Cross-architecture NLI 实验**：Spearman ρ=1.0 (n=6) 的统计可靠性？DRC 方法的 τ 阈值选择方式？NLI combo 的 w 参数设置？BH 校正后仅 2/12 条件显著——claim 是否过度？\n5. **可复现性**：是否提供了足够的实验细节（prompt templates, hyperparameters, random seeds, computational cost）？\n\n请按 ARR 审稿标准给出完整审稿报告，包括 Summary、Strengths、Weaknesses（按 critical/warning/info 分级）、Questions、Overall Assessment（使用 EMNLP 2026 评分标准 1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-21T07:46:30.374115+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12528
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-21T07:46:30.525169+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（strict），参考文献不限，Limitations 必须但不计入页数\n- **模板**: ACL 2023 style（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/symb_invariant_consensus/docs/paper/main.tex`\nPDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 你的审查侧重\n1. **新颖性与贡献定位**：相对于 Huang et al. (2024 self-correction)、Stechly et al. (2025 self-verification)、Amonkar et al. (2025 reality check) 等已有负面结果工作，本文的增量贡献是什么？\"Symbolic Confirmation Bias\" 是否是一个真正新的发现？\"Independence-Accuracy Trade-off\" 是否只是 bias-variance trade-off 的重述？四个 contributions 是否都 substantial？\n2. **Related Work 覆盖**：是否遗漏了重要的相关工作？与 SatLM (Ye et al., 2024) 的对比是否充分？是否有与 CoT confirmation bias (Wan et al., 2025; Jhaveri et al., 2026) 的充分区分？引用格式是否符合 ACL 规范？是否存在过度引用列表而非文献讨论的问题？\n3. **叙事结构与写作质量**：Abstract 是否准确反映论文内容？Introduction 的 narrative flow 是否清晰？术语命名（Symbolic Mirage, Symbolic Confirmation Bias, Independence Bottleneck）是否过度品牌化？Discussion 是否有足够的 forward-looking insight？Limitations 是否充分？\n4. **格式合规**：是否严格遵守 8 页正文限制？匿名规则是否满足（无自引暴露身份）？Table/Figure 编号和引用是否一致？参考文献格式是否完整？\n5. **Missing References**：主动搜索可能遗漏的 2024-2026 年相关工作，特别是 neuro-symbolic reasoning、self-correction、test-time compute 领域的最新论文。\n\n请按 ARR 审稿标准给出完整审稿报告，包括 Summary、Strengths、Weaknesses（按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准 1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（strict），参考文献不限，Limitations 必须但不计入页数\n- **模板**: ACL 2023 style（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n`projects/symb_invariant_consensus/docs/paper/main.tex`\nPDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 你的审查侧重\n1. **新颖性与贡献定位**：相对于 Huang et al. (2024 self-correction)、Stechly et al. (2025 self-verification)、Amonkar et al. (2025 reality check) 等已有负面结果工作，本文的增量贡献是什么？\"Symbolic Confirmation Bias\" 是否是一个真正新的发现？\"Independence-Accuracy Trade-off\" 是否只是 bias-variance trade-off 的重述？四个 contributions 是否都 substantial？\n2. **Related Work 覆盖**：是否遗漏了重要的相关工作？与 SatLM (Ye et al., 2024) 的对比是否充分？是否有与 CoT confirmation bias (Wan et al., 2025; Jhaveri et al., 2026) 的充分区分？引用格式是否符合 ACL 规范？是否存在过度引用列表而非文献讨论的问题？\n3. **叙事结构与写作质量**：Abstract 是否准确反映论文内容？Introduction 的 narrative flow 是否清晰？术语命名（Symbolic Mirage, Symbolic Confirmation Bias, Independence Bottleneck）是否过度品牌化？Discussion 是否有足够的 forward-looking insight？Limitations 是否充分？\n4. **格式合规**：是否严格遵守 8 页正文限制？匿名规则是否满足（无自引暴露身份）？Table/Figure 编号和引用是否一致？参考文献格式是否完整？\n5. **Missing References**：主动搜索可能遗漏的 2024-2026 年相关工作，特别是 neuro-symbolic reasoning、self-correction、test-time compute 领域的最新论文。\n\n请按 ARR 审稿标准给出完整审稿报告，包括 Summary、Strengths、Weaknesses（按 critical/warning/info 分级）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准 1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-21T07:46:32.336174+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1811
}
```

</details>

---


### Assistant

_source line 1084 · 2026-05-21T07:46:44.249349+00:00_

已启动：
- **视觉审查 Agent** — 已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验可靠性）— Round 1 已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）— Round 1 已分配

等待两名 Reviewer 提交独立初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 1085 · 2026-05-21T07:52:08.846971+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性 + 实验可靠性

**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning
**Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## 总体评分

**Overall**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 一篇方法论扎实、实验覆盖广泛的负面结果论文，但核心统计证据（n=6 的 Spearman ρ=1.0、普遍欠功效的检验）与论文中反复强调的强断言之间存在张力，需要收敛 claim 幅度。

---

## 官方维度打分（来自 ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法选择恰当（McNemar + BH + TOST + Bootstrap），但 n=6 相关性被过度依赖，K_eff 理论基础有缝隙，BR 指标有循环论证倾向 |
| Excitement | 3.5/5 | "Symbolic Mirage"概念有用且可推广，27策略全失败的系统性探索有社区价值，但负面结果天然 excitement 受限，constructive contribution (DRC) 适用面窄 |
| Reproducibility | 4/5 | prompt templates 完整公开（Appendix B），超参数明确，承诺 code release；扣分项：多数条件为 single-seed |
| Confidence | 4/5 | 仔细通读全文及全部附录，对方法论和统计检验逐项核查 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Spearman ρ=1.0 (n=6) 的统计可靠性不足以支撑论文的核心 claim 强度
- 具体位置：Section 6 (Cross-Architecture Proof-of-Concept), Figure 3, Appendix P
- 问题：capability gap hypothesis 是论文唯一的 constructive contribution，核心证据是 Spearman ρ=1.0, p=0.003, n=6。但论文自己承认 "Four of six pairs share the DeBERTa verifier; this dependence reduces effective degrees of freedom"（Section 6 第15段）。6个数据点中4个共享同一 verifier，真正独立的 verifier 只有3个（DeBERTa, RoBERTa, BART），且全部只在 Mistral-7B 上显著。这意味着：(1) 有效自由度远低于 n=6；(2) 单调性可能是 DeBERTa 特有现象；(3) 其他三个 generator（LLaMA, Qwen2.5, Qwen3）全部不显著。然而 "strongly monotonic" "ρ=1.0, p=0.003" 在论文中重复出现至少 **7次**（Abstract, Introduction Contribution 2, Section 3.3 Observation 2, Section 6, Section 7 Discussion×2, Conclusion），大幅膨胀了一个 small-sample 观察的证据强度。
- 为什么影响接收：这是论文从负面结果转向正面贡献的关键桥梁。如果这个 claim 的统计基础不牢固，论文退化为一篇纯粹的负面结果论文，Excitement 和 Overall 会显著下降。
- 建议修改方向：(1) 诚实报告有效独立观测数（≤4），将 "strongly monotonic" 降级为 "consistent with a monotonic trend"；(2) 减少重复频次（3次以内）；(3) 增加至少2个 non-DeBERTa verifier 或 additional generator 来增加 n；(4) 在 Section 6 添加一段明确讨论：permutation test 的 p=0.003 依赖于所有6点独立的假设，而该假设被 shared-verifier 结构违反。

**N2** [critical] 论文的中心 claim "SICA fails" 与统计功效不匹配——absence of evidence ≠ evidence of absence
- 具体位置：Section 4.2 (Main Results), Appendix E (Power Analysis, Table 6), Appendix F (Bootstrap CIs, Table 7)
- 问题：论文反复断言 SICA "不能改善" majority voting（Abstract: "self-extracted constraints do not improve majority voting at any capacity level"），但 power analysis 显示所有确认性条件的观测功效均低于 21%（Table 6）。最大研究（Qwen-14B, n=804）的 MDE 为 1.86pp，而观测 Δ 仅 +0.25pp——功效仅 5.7%。这意味着即使存在 1-2pp 的真实效应，此研究也大概率检测不到。TOST 分析部分缓解了这个问题（4/16 条件在 ±2pp 等价），但 **10/16 条件被归类为 "underpowered"**（Section 4.2 最后一段），即既不能证明有效也不能证明无效。论文在 Limitations 中提到了功效问题，但正文的 claim 语气并未相应软化。
- 为什么影响接收：这是方法论严谨性的核心问题。在功效不足时做出强否定 claim 是统计推断错误。
- 建议修改方向：(1) 将 Abstract 中的 "do not improve" 改为 "we find no evidence that self-extracted constraints improve...within the detectable range of our study (MDE ≈ 2pp)"；(2) Section 4.2 的结论应明确：对于确认为等价的4个条件，SICA确实无效（±2pp）；对于10个 underpowered 条件，结论是 inconclusive；(3) 在 Discussion 中添加一段讨论：如果真实效应在 0.5-1.5pp 范围内，可能需要 n≥2000 才能检测到。

**N3** [critical] TOST ±2pp 等价性 margin 的选择缺乏充分论证
- 具体位置：Section 4.2, Appendix S (TOST)
- 问题：论文将 ±2pp 描述为 "reflecting the smallest Δ we consider practically meaningful given SC baselines of 39–86%"。但问题在于：(1) 对于 SC=39.33% 的 Mistral-7B ProofWriter，2pp 意味着 ~5% 的相对改善，这在实践中可能是有意义的；(2) 对于 SC=86% 的 Qwen3-thinking，2pp 只是 ~2.3% 的相对改善。一个固定的绝对 margin 跨越如此大的 baseline 范围是有问题的。Appendix S Table 20 的 margin sensitivity 分析显示：±1pp 时 0 条件等价，±3pp 时 10 条件等价——等价结论对 margin 选择高度敏感。
- 为什么影响接收：TOST 是论文区分 "真正等价" 和 "功效不足" 的关键工具，margin 选择不当直接影响分类结果的可信度。
- 建议修改方向：(1) 提供一个 principled 的 margin 选择理由——例如根据 practical significance 文献或领域共识（如果有的话）；(2) 考虑使用 relative margin（如 ±3% relative to SC baseline）而非绝对 margin；(3) 至少在正文中报告 ±1pp 和 ±3pp 的敏感性结果（不仅放在附录）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Proposition 1 和 Observation 2 的形式化程度与实际严格性不匹配
- 具体位置：Section 3.3 (The Symbolic Mirage Hypothesis), \paragraph{Empirical Bound 1} 和 \paragraph{Empirical Observation 2}
- 问题：这两个结果用了数学不等式/命题风格（$\Delta_\text{max}^\text{self} \lesssim \Delta_\text{oracle} / \text{BR}(M)$），但既无形式化证明也无严格的数学推导。Bound 1 中的 "≲" 未定义；Observation 2 中 "combo gain is monotonically increasing in the capability gap" 是一个关于6个数据点的经验观察，不是数学命题。这些标签（"Bound"、"Observation"）避开了 \newtheorem 环境，显示作者有一定自觉，但数学符号的使用仍创造了不当的形式化印象。
- 建议：(1) 明确标注 "Empirical Claim" 或 "Hypothesis"，而非 "Bound"；(2) 对 Bound 1 提供推导过程，或降级为 heuristic；(3) 对 Observation 2 去掉 "monotonically increasing" 的数学语气，改为 "we observe a trend consistent with..."。

**W2** [warning] 跨架构 NLI 实验的范围窄于论文暗示的通用性
- 具体位置：Section 6, Table 3, Table 4
- 问题：Cross-architecture escape 仅在 ProofWriter（premise-conclusion 结构天然匹配 NLI）和 FOLIO（marginal, BH correction 后仅 n.s.）上有效；LogiQA 无效（Limitations 中承认）。三个 NLI verifier（DeBERTa, RoBERTa, BART）全部是 encoder-only + MNLI-finetuned 同一范式。论文标题暗示 "cross-architecture"，但实际是 "NLI verification on NLI-shaped tasks"。Conclusion 中 "Cross-architecture NLI escapes the mirage" 的表述过度泛化。
- 建议：(1) 将 "cross-architecture escape" 重新框架为 "NLI-based external verification on tasks with premise-conclusion structure"；(2) Discussion 中明确讨论 generalization 的限制；(3) 如果可能，增加非 NLI 类型的 external verifier（如 code execution, trained reward model）做初步探索。

**W3** [warning] "27 strategies" 的计数方式膨胀了实际覆盖面
- 具体位置：Abstract, Section 5.5, Appendix J-K (Tables 11-13)
- 问题：论文声称 "twenty-seven remediation strategies spanning fifteen families"，但细看：(1) 部分是同一方法的超参变体（T=0.3/0.5/0.7/1.0）；(2) 部分在 n≤60 的极小样本上无统计功效（Table 5 中标 † 的条件）；(3) Table 13 包含 "ASCII perturbation" (Δ=0.0) 和 "κ-aware SC" (11/11 conditions Δ=0) 等 ad hoc 尝试。更关键的是，论文未尝试 trained constraint extractors、retrieval-augmented extraction、或 RL-based extraction——这些可能从根本上改变 extraction quality。论文的 "exhaustive" 暗示是不准确的。
- 建议：(1) 坦诚区分 principled strategies 和 exploratory attempts；(2) 将 T/K 变体合并为 "sensitivity analysis"，不计入策略总数；(3) Discussion 中明确讨论未尝试的方向（trained extractors 等）。

**W4** [warning] DRC 的 τ 阈值在 evaluation set 上选择
- 具体位置：Section 6.1, Table 4
- 问题：τ=0.7 在 evaluation set 上选择，论文自己标注 "deployment would require a held-out validation split"。DRC 声称的 "90% gain at 39% cost" 是对 evaluation set 过拟合的乐观估计。
- 建议：(1) 使用交叉验证或留一法来估计 DRC 性能；(2) 或在 FOLIO 上设 τ、在 ProofWriter 上测试（cross-dataset validation）。

**W5** [warning] 多数条件为 single-seed，而 4-seed 复现显示高变异
- 具体位置：Section 4.2, Table 1 (4s 标注), Table 2 (多 seed 行)
- 问题：仅 Mistral-7B FOLIO 有 4-seed 复现。4个 seed 中2个产生 null 或 negative Δ，aggregate +3.43pp 不显著 (p=0.092)。Seed 间 Δ 从 +3.43 到 -0.49pp，range 接近 4pp。这说明 single-seed 结果可能在 ±2pp 内波动，而这恰好是 TOST margin 的量级。其他条件全部是 single-seed，其 Δ 的可信度存疑。
- 建议：(1) 对 Table 1 中至少 3-4 个关键条件（如 Qwen2.5-14B ProofWriter, LLaMA FOLIO）做 multi-seed 复现；(2) 如无法补做，在 Limitations 中明确声明 single-seed 结果的置信度限制。

**W6** [warning] Bias Ratio (BR) 指标存在循环论证倾向
- 具体位置：Section 3.3 (Eq. 5), Section 5.2
- 问题：BR 只在模型答错的题上计算 (a_M ≠ a*)。在模型答错时，其 CoT 推导多数指向错误答案；从这些推导中提取的约束自然也指向错误答案。BR=4.97× 说的本质是"模型错的时候，它从自己的推理中提取的约束也是错的"——这是 self-extraction 的定义性结果，而非独立发现。更有信息量的问题是：在模型答对时，约束是否提供了 beyond-majority-vote 的辨别力？论文的 ablation (Appendix I, Table 10) 更好地回答了这个问题（MAX-SAT vs count-only 在 773/804 上一致），但 BR 得到了不成比例的强调。
- 建议：(1) Discussion 中承认 BR 的 tautological 倾向；(2) 将 ablation 结果（Table 10）提升到正文；(3) 减少 BR=4.97× 的重复频次。

---

## 小问题（不影响接收）

- Abstract 过于密集：10行文字中包含 15+ 个数字/统计量，可读性低。建议简化，将部分数字移至正文。
- "3,000 condition-evaluations (∼1,250 unique instances)" 的表述方式可能误导——实际 unique 实例量 ≈1,250，3,000 是条件×实例的组合数。建议在首次出现时明确说明。
- 相同关键数字（BR=4.97×, ρ=1.0 p=0.003, +29.90pp, 83.3%）在 Abstract/Intro/Method/Experiments/Analysis/Discussion/Conclusion 中每处都出现，冗余感强。
- Figure 3 (capability gap scatter) 仅6个点，视觉上不够有说服力；建议在图注中坦诚标注 n=6。
- K_eff 的推导使用 Fleiss' κ 作为 ICC 的代理，但二者的单调关系验证（r=0.625）只是中等相关。Section 3.1 "should be interpreted as an ordinal diagnostic" 的声明是正确的，但后续使用中偶有当作定量指标的倾向。
- 引用验证：60条引用全部有对应 bib 条目，无 orphan/missing。10条 not_found 均为近期 arXiv 预印本或经典著作（如 Condorcet 1785），可接受。10条 first_author mismatch 均为格式差异（如 "de Moura" vs "Moura"），非实质性错误。
- 页数合规：正文 8 页（Section 1-8 + Limitations），References 2 页，Appendix 14 页。符合 EMNLP 2026 要求。

---

## 主要优势

1. **系统性前所未有**：6 models × 3 datasets × 27 strategies × oracle controls × cross-arch escape，覆盖面远超同类工作。这是我见过的对 self-extraction 范式最全面的实证研究。
2. **统计方法论成熟**：McNemar paired test + BH FDR correction + TOST equivalence + Bootstrap CI + Power analysis，构成了一个完整的统计推断链条。Appendix E/F 的 power 和 CI 分析尤其值得赞赏。
3. **"Symbolic Mirage" 概念定义清晰**：三个可测试预测（BR>1 across architectures, no same-model intervention breaks BR, only external verification escapes）全部被数据确认，概念框架完整。
4. **Oracle 控制实验设计精妙**：用 FOLIO gold annotations 和 ProofWriter DSL 作为 oracle constraints，干净地隔离了 extraction quality 和 aggregation mechanism，这是论文最强的方法论贡献。
5. **Case studies (Appendix G) 提供了机制性理解**：三个 discordant case 分别展示 SICA-wins、SC-wins、non-discriminative 三种模式，超越统计汇总数字。
6. **Comprehensive appendix**：24 页总量中 14 页为附录，包含 prompt templates、pseudocode、ablation、error analysis、sub-population analysis，reproducibility 条件好。

---

## Questions for Authors

1. 如果用 relative TOST margin（如 ±3% of SC baseline）替代 absolute ±2pp，等价/underpowered/different 的分类会如何变化？
2. 是否考虑过 trained constraint extractor（如 fine-tuned on oracle annotations from FOLIO/ProofWriter）？这是打破 self-extraction 瓶颈的最自然路径。
3. Observation 2 的 permutation test：如果只用3个独立 verifier（collapsing 4 DeBERTa pairs into 1），p值是多少？
4. 为什么不在 Mistral-7B FOLIO 之外的条件做 multi-seed 复现？这是资源限制还是设计决策？
5. Process similarity (Eq. 6) 用 TF-IDF——如果用 sentence embedding (如 SBERT) 会不会得到不同的 gap 估计？TF-IDF 对推理结构的表示能力有限。

---

**审稿人签名**: Reviewer 1 (方法严谨性 + 实验可靠性)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1086 · 2026-05-21T07:52:15.870948+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 70

## Round 70

2 recorded events


### User

_source line 1087 · 2026-05-21T07:52:29.879621+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成。

**评分**: Overall 3.5/5 (Borderline Conference)，Soundness 3.5/5，Excitement 3.5/5，Reproducibility 4/5。

**核心判断**: 论文是一篇覆盖面极广的系统性负面结果研究（6模型×3数据集×27策略×oracle控制），统计方法论成熟。但存在三个 must-fix 问题：

1. **Spearman ρ=1.0 (n=6) 被过度依赖** — 6个数据点中4个共享同一 verifier，有效自由度远低于6，但 "strongly monotonic ρ=1.0 p=0.003" 在论文中重复7次
2. **"SICA fails" 的断言与统计功效不匹配** — 所有条件观测功效<21%，10/16条件 underpowered，absence of evidence ≠ evidence of absence
3. **TOST ±2pp margin 缺乏 principled 论证** — 跨 39-86% baseline 使用固定绝对 margin 有问题，等价结论对 margin 高度敏感

报告已提交给 Review Director，包含 3 个 Must-Fix、6 个 Should-Fix、若干小问题、5 个 Questions for Authors。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1088 · 2026-05-21T07:52:39.420543+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 71

## Round 71

6 recorded events


### User

_source line 1089 · 2026-05-21T07:53:15.258595+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告：Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），一个从 LLM 推理 trace 中提取逻辑约束、通过加权部分 MAX-SAT 聚合答案的管线。在 6 个开源 LLM（7B-32B）、5 个推理基准、3,000+ 条件评估上，作者发现自提取符号约束在任何模型能力水平上都无法改进 Self-Consistency（SC）。论文识别了三个现象：(1) Symbolic Confirmation Bias（约束镜像模型已有错误，BR > 1.97），(2) Independence-Accuracy Trade-off（有效样本量 K_eff ≈ 1.2-3.6），(3) Process-Level Independence（TF-IDF 相似性分析）。作为建设性贡献，论文提出 DRC（Disagreement-Routed Cascade），通过跨架构 NLI 验证在 39% 成本下恢复 90% 的 full-combo 精度。

---

## 总体评分

**Overall**: 3.0 / 5（Findings）
**一句话总结**: 方法论扎实、统计严谨的实证研究，但核心负面结果在已有工作（self-correction 失败、CoT confirmation bias）的基础上增量有限，建设性贡献（DRC）评估不够充分。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法严谨（TOST、McNemar、bootstrap CI、FDR 校正），但模型规模受限（≤14B），部分条件统计功效不足 |
| Excitement | 2.5/5 | 重要的研究问题，但负面结果可从先验工作预测；DRC 贡献过于简单，不足以撑起论文的 excitement |
| Reproducibility | 4.0/5 | 提取 prompt 完整（Appendix B）、参数设置清晰、数据集公开；但代码和实验脚本尚未释出 |
| Reviewer Confidence | 4/5 | 对 neuro-symbolic reasoning、self-consistency、ensemble theory 领域熟悉，仔细阅读了全文及附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心负面结果的增量新颖性不足
- 具体位置：Section 1 (contributions 1-3), Section 5.2, Section 5.5
- 问题：论文的三个分析性贡献——Symbolic Confirmation Bias、Independence-Accuracy Trade-off、Process-Level Independence——在概念层面可从已有工作组合中预测：
  - Huang et al. (2024) 和 Stechly et al. (2025) 已证明 LLM 在无外部反馈时无法自纠错；
  - Wan et al. (2025) 和 Jhaveri et al. (2026) 已明确识别 CoT 中的 confirmation bias；
  - Amonkar et al. (2025) 已在约束满足问题上展示形式化失败；
  - Chan et al. (2026) 已论证逻辑健全性对 neurosymbolic 事实检查不可靠。
  "Symbolic Confirmation Bias" 本质上是已知的 self-verification 失败在符号约束提取这一特定管线上的实例化。论文需要更清晰地论证：为什么在符号约束提取这一特定场景中重新验证这一现象构成了 substantial contribution，而非仅仅是已知现象的又一个数据点。
- 为什么影响接收：ARR review form 的 Excitement 维度要求论文提供 "new insights"。如果三个分析性贡献都可以从先验工作推导，论文的核心价值被大幅削弱。
- 建议修改方向：(a) 更明确地论述与上述先验工作的区别——不只是"我们在新设置中验证了"，而是"我们发现了先验工作未预测到的新机制/新边界条件"；(b) 如果新颖性主要在实证粒度上（K_eff 量化、BR 指标），需要将此定位为论文的核心卖点，而非将已知现象的重新发现包装为"新发现"。

**N2** [critical] 模型规模限制削弱了结论的普适性
- 具体位置：Section 4.1, Limitations (p.9)
- 问题：论文仅测试了 ≤14B 参数的开源模型（最大为 Qwen2.5-14B 和 QwQ-32B thinking model）。标题声称 "Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning"——这是一个非常强的、未经限定的否定命题。然而：
  - 约束提取质量很可能随模型规模提升（论文自身 Table 1 显示 QwQ-32B 的提取率最高 96.10%）；
  - Capability gap 分析（Section 6.1, Table 3）显示 combo gain 随能力单调递增，暗示更强模型可能跨越某个阈值；
  - 近期 frontier 模型（GPT-4o、Claude 3.5、Llama-3 70B/405B）的推理能力远超 14B 模型。
  论文在 Limitations 中简短提及了这一局限，但标题和 Abstract 的措辞没有反映这一重大限制。
- 为什么影响接收：如果结论在 70B+ 模型上不成立，论文的核心 claim 就需要重新限定。一个有条件的负面结果（"在 ≤14B 模型上不成立"）和一个普适性的负面结果（"不成立"）是完全不同级别的贡献。
- 建议修改方向：(a) 将标题限定为反映实际测试范围，或 (b) 增加至少一个 70B+ 模型的实验（即使只在一个数据集上），或 (c) 提供理论论证说明为什么规模不应改变结论。

**N3** [critical] "Independence-Accuracy Trade-off" 与经典 ensemble diversity-accuracy dilemma 区分不足
- 具体位置：Section 3.1, Section 5.4, Section 7 (Discussion)
- 问题：论文提出的 "Independence-Accuracy Trade-off" 与 ensemble learning 中经典的 diversity-accuracy dilemma（Krogh & Vedelsby, 1994; Brown et al., 2005）在概念上高度重叠。论文在 Section 7 的 Discussion 中引用了这两篇经典工作，但仅用一句话提及，未充分论证自己的 framing 相对于经典 framing 的增量价值。
  - 经典 framing：ensemble error = average error - diversity。更多样化的成员降低 ensemble error，但个体精度也很重要。
  - 论文 framing：使投票者更独立（不同架构）倾向于降低个体精度，CJT 要求独立性和 p > 0.5 同时成立。
  核心张力（独立性 vs. 精度）是相同的基本权衡，CJT framing 增加的主要是 p > 0.5 的阈值效应和 K_eff 指标。如果这只是将已知 trade-off 用 CJT 语言重述，则不构成独立贡献。
- 为什么影响接收：这是论文四个贡献之一（Contribution 2）。如果它实质上是已知概念的重述，论文的贡献数量从四个降为三个。
- 建议修改方向：在 Section 3.1 或 Section 7 中明确讨论与经典 ensemble diversity-accuracy dilemma 的关系，论证 CJT framing 带来了哪些经典 framing 无法提供的新洞见（例如 K_eff 的具体量化、阈值效应的实证验证）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 术语过度品牌化
- 具体位置：全文（"Symbolic Mirage" §3.3, "Symbolic Confirmation Bias" §5.2, "Independence Bottleneck" §5.4）
- 问题：论文为相对直接的现象赋予了多个品牌化术语。"Symbolic Mirage" 描述的是自提取约束继承模型偏差——这在已有文献中被称为 self-verification failure（Stechly et al., 2025）或 confirmation bias（Wan et al., 2025）。为已知现象在新场景中引入新名称可能被视为 term proliferation 而非概念创新。"Independence Bottleneck" 同样如此——这本质上是 correlated voters in ensemble。
- 建议：保留一个最核心的术语（如 "Symbolic Confirmation Bias"），对其他术语改用描述性语言而非品牌化命名。

**W2** [warning] DRC 评估不够充分
- 具体位置：Section 6, Tables 3-4
- 问题：DRC 是论文唯一的建设性贡献（Contribution 4），但评估受限：
  - 仅在 DeBERTa-large-mnli 上评估 NLI 组件（单一架构、单一训练数据）
  - 仅在 FOLIO 和 ProofWriter 上评估（2/5 数据集）
  - 未与其他 cross-model verification 方法对比（如 multi-agent debate, verifier-guided search）
  - 阈值 τ 的选择（τ=0.7）缺乏系统分析——Appendix M.1 提供了 K 的敏感性但非 τ 的
  作为论文的核心正面贡献，DRC 需要更充分的评估来支撑 "recovers 90% of full-combo accuracy at 39% cost" 这一 claim 的普适性。
- 建议：(a) 在至少 3 个数据集上评估，(b) 与 multi-agent debate baseline 对比，(c) 加入 τ 的敏感性分析。

**W3** [warning] Related Work 存在重要遗漏
- 具体位置：Section 2
- 问题：通过搜索发现以下高度相关的近期工作未被引用：
  1. **Byerly & Khashabi (2026, TACL)** "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems" — 直接展示 SC 在 long-context 设置中反而降低性能，与本文的负面结果互补但分析了不同的失败机制（positional bias vs. confirmation bias）。
  2. **arxiv 2604.07650 (April 2026)** "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles" — 开发了审计 LLM 行为纠缠的统计框架，直接相关于本文的 independence 分析。提出的 de-entangled verifier reweighting 方法与 DRC 的动机相同。
  3. **arxiv 2506.07962** "Correlated Errors in Large Language Models" — 系统分析 LLM 之间的错误相关性，发现同族模型错误高度相关，直接支撑本文的 independence bottleneck 发现。
  4. **arxiv 2510.01499** "Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information" — 提出利用高阶信息的聚合方法，可作为 MAX-SAT 之外的 aggregation baseline。
  注意：#2 和 #4 可能在本文提交时尚未公开，但 #1（TACL 2026）和 #3 应在写作时已经可引用。
- 建议：补充引用 #1 和 #3，在 Related Work 中讨论它们与本文发现的关系。

**W4** [warning] Related Work 讨论深度不足
- 具体位置：Section 2
- 问题：Section 2 的三个子段落（Self-Consistency and extensions, Neuro-symbolic reasoning, Test-time compute and verification）每段都包含大量 parenthetical citation list（如 "(Pan et al., 2023; Olausson et al., 2023; Ye et al., 2024; ... Miya, 2025)"），呈现为引用列表而非文献讨论。ACL 的 reviewer guidelines 倾向于 "critical discussion" 而非 "citation listing"。特别是：
  - 与 SatLM (Ye et al., 2024) 的区别仅隐含在管线描述中，未显式论述
  - Neuro-symbolic reasoning 段落引用了 13 篇工作但每篇仅用短语或半句提及
- 建议：减少引用数量，对 3-4 篇最相关工作进行深入对比讨论。

**W5** [warning] Abstract 未限定结论范围
- 具体位置：Abstract
- 问题：Abstract 声称 "self-extracted constraints do not improve majority voting at any capability level"，但实际测试范围仅为 7B-32B 开源模型。Abstract 未提及模型规模限制。此外，"across six open-source LLMs (7B-32B)" 未提及 QwQ-32B 是 thinking model，其行为模式与标准 LLM 有本质差异。
- 建议：在 Abstract 中加入 "on models up to 32B parameters" 或类似限定。

---

## 小问题（不影响接收）

- **引用格式**：verify_references 工具检测到 10 条 author name mismatch（如 li2025aristotle 的 first author bib=Li vs API=Xu，liang2023encouraging 的 bib=Liang vs API=Tian）。建议核实这些条目的作者顺序是否正确。
- **Table 2 (p.6)**："Effective-K" 列的 dash (—) 符号含义未在 caption 中说明。
- **Figure 1 (p.2)**：红色虚线框标注的 "independence bottleneck" 在印刷版可能不够清晰，建议改用更高对比度的标注方式。
- **Appendix 体量**：附录 A-Z 共 ~14 页，部分内容（如 Appendix I: Constraint Ablation Details, Appendix L: Extraction Error Taxonomy）包含了对主要论点重要的支撑材料。考虑将关键结果上提到正文。

---

## 主要优势

1. **实验设计的系统性**：6 个模型 × 5 个数据集 × 多条件设计，加上 27 种 remediation 策略的穷举测试，充分排除了"只是没找到正确配置"的反驳。
2. **统计方法论严谨**：使用 TOST 等价性检验（而非仅依赖"未拒绝零假设"来声称无效果）是正确的统计实践，在 NLP 实证研究中少见且值得肯定。
3. **K_eff 诊断指标**：将 Kish's design effect 引入 LLM 投票分析是一个有用的方法论贡献，为社区提供了量化 same-model 投票独立性的工具。
4. **Bias Ratio (BR) 分析**：Table 2 的分析清晰展示了约束与错误答案的共变关系，比简单的"提取失败率"更有洞察力。
5. **DRC 的实用价值**：虽然评估有限，但"仅在不一致时调用外部验证"的 routing 思想在实际部署中有明确的成本效益价值。
6. **诚实的负面结果报告**：论文没有为了"正面故事"而隐瞒负面发现，这在学术诚信上值得肯定。

---

## Questions to Authors

1. 在 70B+ 模型（如 Llama-3-70B 或 Qwen2.5-72B）上，约束提取质量和 BR 是否可能跨越某个质变阈值？你们是否有任何初步数据支持或反驳这一可能性？
2. K_eff 分析（Section 3.1）中，你们使用了 Fleiss' κ 作为 intra-class correlation 的 proxy。Fleiss' κ 是一个 nominal-scale agreement 指标，将其直接代入 Kish 的 design effect 公式（为连续变量设计）在统计上是否严格合理？是否考虑过使用其他相关性度量？
3. DRC 中阈值 τ = 0.7 的选择依据是什么？不同 τ 值如何影响精度-成本 trade-off 曲线？
4. 论文测试了 27 种 same-model remediation 策略，但所有策略都假设约束来自与生成 trace 相同的模型。是否考虑过"自提取约束 + 不同模型的 MAX-SAT 权重估计"这类 hybrid 方案？
5. "Symbolic Confirmation Bias" 与 Wan et al. (2025) 识别的 CoT confirmation bias 在机制上有何本质区别？是否可能前者只是后者在形式化管线中的自然传递？

---

## Missing References（主动搜索结果）

1. Byerly & Khashabi (2026). "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems." *TACL*, 14:292-317. — SC 在 long-context 场景失败的系统性研究。
2. arxiv 2604.07650 (2026). "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles." — LLM 独立性审计框架，直接相关。
3. arxiv 2506.07962 (2025). "Correlated Errors in Large Language Models." — LLM 错误相关性分析。
4. arxiv 2510.01499 (2025). "Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information." — 超越 majority voting 的聚合方法。
5. arxiv 2501.19306 (2025). "SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling." — Self-verification + self-correction 在 test-time scaling 中的应用。

---

## 引用验证结果摘要

- 总计 60 条 bib 条目，96 处引用，0 orphan，0 missing citation key
- 40 条 OpenAlex 验证通过，10 条 not_found（主要为古典著作和最新 preprint），10 条 minor mismatch（作者名格式差异）
- 未发现虚假引用（fabricated citations）
- 建议核查的条目：li2025aristotle（first author 可能有误）、liang2023encouraging（first author 可能有误）

---

## Overall Assessment 详细理由

给分 **3.0（Findings）**。

**支持 Conference (4.0) 的因素**：实验设计系统、统计方法论优秀、K_eff 和 BR 指标有方法论价值、27 种策略穷举排除了偶然性、DRC 有实用潜力。

**拉低至 Findings 的因素**：(1) 核心负面发现（confirmation bias、independence failure）可从 Huang et al. 2024 + Stechly et al. 2025 + Wan et al. 2025 的组合中预测，概念新颖性有限；(2) 标题和结论未限定模型规模（≤14B），claim 的普适性存疑；(3) "Independence-Accuracy Trade-off" 与经典 ensemble diversity-accuracy dilemma 的区分不足；(4) DRC 作为唯一建设性贡献，评估不够充分。

如果作者能解决 N1（明确论证增量新颖性）、N2（限定结论范围或增加大模型实验）、N3（与经典 trade-off 的区分），论文可上调至 3.5（Borderline Conference）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-21T07:53:48.986013+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 / 5（Findings）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n\n### Must-Fix 问题\n\n**N1** [critical] 核心负面结果的增量新颖性不足\n- 论文的三个分析性贡献（Symbolic Confirmation Bias、Independence-Accuracy Trade-off、Process-Level Independence）在概念层面可从已有工作组合中预测：Huang et al. (2024) + Stechly et al. (2025) 已证明无外部反馈时无法自纠错；Wan et al. (2025) + Jhaveri et al. (2026) 已识别 CoT confirmation bias；Amonkar et al. (2025) 已在约束满足问题上展示形式化失败；Chan et al. (2026) 已论证逻辑健全性不可靠。\"Symbolic Confirmation Bias\" 本质上是已知 self-verification 失败在符号约束提取上的实例化。\n\n**N2** [critical] 模型规模限制削弱结论普适性\n- 仅测试 ≤14B 模型（最大 QwQ-32B thinking model）。标题 \"Do Not Improve LLM Reasoning\" 是未经限定的否定命题。约束提取质量可能随规模提升。近期 frontier 模型远超 14B。标题和 Abstract 未反映这一限制。\n\n**N3** [critical] \"Independence-Accuracy Trade-off\" 与经典 ensemble diversity-accuracy dilemma 区分不足\n- 与 Krogh & Vedelsby (1994), Brown et al. (2005) 的经典 framing 高度重叠。论文仅用一句话提及，未充分论证 CJT framing 的增量价值。\n\n### Should-Fix 问题\n\n**W1** [warning] 术语过度品牌化（\"Symbolic Mirage\", \"Independence Bottleneck\" 等为已知现象赋予新品牌）\n**W2** [warning] DRC 评估不充分（仅2数据集、单一 NLI 架构、未与 debate 等方法对比、τ 无系统分析）\n**W3** [warning] Related Work 存在重要遗漏（Byerly & Khashabi 2026 TACL; arxiv 2604.07650; arxiv 2506.07962; arxiv 2510.01499）\n**W4** [warning] Related Work 讨论深度不足（引用列表而非文献讨论，与 SatLM 对比不充分）\n**W5** [warning] Abstract 未限定结论范围（未提及模型规模限制）\n\n### Questions\n1. 70B+ 模型上 BR 是否可能跨越质变阈值？\n2. Fleiss' κ 代入 Kish design effect 公式是否统计上合理？\n3. DRC τ=0.7 选择依据？\n4. 是否考虑过 hybrid 方案（自提取约束 + 不同模型的权重估计）？\n5. SCB 与 Wan et al. (2025) CoT confirmation bias 本质区别？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall**: 3.0 / 5（Findings）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n\n### Must-Fix 问题\n\n**N1** [critical] 核心负面结果的增量新颖性不足\n- 论文的三个分析性贡献（Symbolic Confirmation Bias、Independence-Accuracy Trade-off、Process-Level Independence）在概念层面可从已有工作组合中预测：Huang et al. (2024) + Stechly et al. (2025) 已证明无外部反馈时无法自纠错；Wan et al. (2025) + Jhaveri et al. (2026) 已识别 CoT confirmation bias；Amonkar et al. (2025) 已在约束满足问题上展示形式化失败；Chan et al. (2026) 已论证逻辑健全性不可靠。\"Symbolic Confirmation Bias\" 本质上是已知 self-verification 失败在符号约束提取上的实例化。\n\n**N2** [critical] 模型规模限制削弱结论普适性\n- 仅测试 ≤14B 模型（最大 QwQ-32B thinking model）。标题 \"Do Not Improve LLM Reasoning\" 是未经限定的否定命题。约束提取质量可能随规模提升。近期 frontier 模型远超 14B。标题和 Abstract 未反映这一限制。\n\n**N3** [critical] \"Independence-Accuracy Trade-off\" 与经典 ensemble diversity-accuracy dilemma 区分不足\n- 与 Krogh & Vedelsby (1994), Brown et al. (2005) 的经典 framing 高度重叠。论文仅用一句话提及，未充分论证 CJT framing 的增量价值。\n\n### Should-Fix 问题\n\n**W1** [warning] 术语过度品牌化（\"Symbolic Mirage\", \"Independence Bottleneck\" 等为已知现象赋予新品牌）\n**W2** [warning] DRC 评估不充分（仅2数据集、单一 NLI 架构、未与 debate 等方法对比、τ 无系统分析）\n**W3** [warning] Related Work 存在重要遗漏（Byerly & Khashabi 2026 TACL; arxiv 2604.07650; arxiv 2506.07962; arxiv 2510.01499）\n**W4** [warning] Related Work 讨论深度不足（引用列表而非文献讨论，与 SatLM 对比不充分）\n**W5** [warning] Abstract 未限定结论范围（未提及模型规模限制）\n\n### Questions\n1. 70B+ 模型上 BR 是否可能跨越质变阈值？\n2. Fleiss' κ 代入 Kish design effect 公式是否统计上合理？\n3. DRC τ=0.7 选择依据？\n4. 是否考虑过 hybrid 方案（自提取约束 + 不同模型的权重估计）？\n5. SCB 与 Wan et al. (2025) CoT confirmation bias 本质区别？"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-21T07:54:14.895985+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25909
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-21T07:54:15.148068+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Spearman ρ=1.0 (n=6) 的统计可靠性不足以支撑核心 claim 强度\n- 6个数据点中4个共享 DeBERTa verifier，有效自由度远低于6。\"strongly monotonic ρ=1.0 p=0.003\" 在论文中重复至少7次。这是论文从负面结果转向正面贡献的关键桥梁。建议：降级为 \"consistent with a monotonic trend\"，减少重复频次（≤3次），增加 non-DeBERTa verifier，添加讨论 shared-verifier 对 permutation test 假设的违反。\n\n**N2** [critical] \"SICA fails\" 的断言与统计功效不匹配——absence of evidence ≠ evidence of absence\n- 所有条件观测功效 <21%，10/16 条件 underpowered。Abstract \"do not improve\" 应改为 \"we find no evidence that...within the detectable range\"。功效不足时做强否定 claim 是统计推断错误。\n\n**N3** [critical] TOST ±2pp margin 缺乏 principled 论证\n- 跨 39-86% baseline 使用固定绝对 margin 有问题。Appendix S sensitivity 显示 ±1pp 时 0 条件等价，±3pp 时 10 条件等价——高度敏感。建议考虑 relative margin。\n\n### Should-Fix 问题\n\n**W1** [warning] Proposition 1 / Observation 2 形式化程度与实际严格性不匹配（\"Bound\" 用于 empirical claim，\"≲\" 未定义）\n**W2** [warning] 跨架构 NLI 实验范围窄于论文暗示的通用性（仅 NLI-shaped tasks 有效，3个 verifier 全是 encoder-only MNLI-finetuned）\n**W3** [warning] \"27 strategies\" 计数膨胀（含超参变体、ad hoc 尝试、n≤60 条件；未尝试 trained extractors）\n**W4** [warning] DRC τ 在 evaluation set 上选择（过拟合风险）\n**W5** [warning] 多数条件 single-seed，4-seed 复现显示高变异（Δ from +3.43 to -0.49pp）\n**W6** [warning] BR 指标存在循环论证倾向（模型错时提取约束也错是 self-extraction 的定义性结果）\n\n### Questions\n1. 用 relative TOST margin 替代 absolute ±2pp，分类如何变化？\n2. 是否考虑过 trained constraint extractor？\n3. 仅用3个独立 verifier 时 permutation test p值？\n4. 为什么不在其他条件做 multi-seed 复现？\n5. Process similarity 用 SBERT 替代 TF-IDF 会否改变结论？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5\n\n### Must-Fix 问题\n\n**N1** [critical] Spearman ρ=1.0 (n=6) 的统计可靠性不足以支撑核心 claim 强度\n- 6个数据点中4个共享 DeBERTa verifier，有效自由度远低于6。\"strongly monotonic ρ=1.0 p=0.003\" 在论文中重复至少7次。这是论文从负面结果转向正面贡献的关键桥梁。建议：降级为 \"consistent with a monotonic trend\"，减少重复频次（≤3次），增加 non-DeBERTa verifier，添加讨论 shared-verifier 对 permutation test 假设的违反。\n\n**N2** [critical] \"SICA fails\" 的断言与统计功效不匹配——absence of evidence ≠ evidence of absence\n- 所有条件观测功效 <21%，10/16 条件 underpowered。Abstract \"do not improve\" 应改为 \"we find no evidence that...within the detectable range\"。功效不足时做强否定 claim 是统计推断错误。\n\n**N3** [critical] TOST ±2pp margin 缺乏 principled 论证\n- 跨 39-86% baseline 使用固定绝对 margin 有问题。Appendix S sensitivity 显示 ±1pp 时 0 条件等价，±3pp 时 10 条件等价——高度敏感。建议考虑 relative margin。\n\n### Should-Fix 问题\n\n**W1** [warning] Proposition 1 / Observation 2 形式化程度与实际严格性不匹配（\"Bound\" 用于 empirical claim，\"≲\" 未定义）\n**W2** [warning] 跨架构 NLI 实验范围窄于论文暗示的通用性（仅 NLI-shaped tasks 有效，3个 verifier 全是 encoder-only MNLI-finetuned）\n**W3** [warning] \"27 strategies\" 计数膨胀（含超参变体、ad hoc 尝试、n≤60 条件；未尝试 trained extractors）\n**W4** [warning] DRC τ 在 evaluation set 上选择（过拟合风险）\n**W5** [warning] 多数条件 single-seed，4-seed 复现显示高变异（Δ from +3.43 to -0.49pp）\n**W6** [warning] BR 指标存在循环论证倾向（模型错时提取约束也错是 self-extraction 的定义性结果）\n\n### Questions\n1. 用 relative TOST margin 替代 absolute ±2pp，分类如何变化？\n2. 是否考虑过 trained constraint extractor？\n3. 仅用3个独立 verifier 时 permutation test p值？\n4. 为什么不在其他条件做 multi-seed 复现？\n5. Process similarity 用 SBERT 替代 TF-IDF 会否改变结论？"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-21T07:54:16.961060+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1812
}
```

</details>

---


### Assistant

_source line 1094 · 2026-05-21T07:54:21.873141+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 72

## Round 72

2 recorded events


### User

_source line 1095 · 2026-05-21T07:54:24.632710+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**评分：Overall 3.0（Findings）**

核心判断：
- **方法论扎实**：TOST 等价性检验、K_eff 诊断、27 种策略穷举——统计实践在 NLP 实证研究中属上乘
- **新颖性不足**：三个分析性贡献（Symbolic Confirmation Bias、Independence-Accuracy Trade-off、Process-Level Independence）在概念上可从 Huang et al. 2024 + Stechly et al. 2025 + Wan et al. 2025 的已有结论组合中预测
- **结论过度泛化**：标题声称"不改进"但仅测试 ≤14B 模型，未涵盖 70B+ frontier 模型
- **DRC 评估有限**：唯一的建设性贡献仅在 2/5 数据集上评估，未与 multi-agent debate 等方法对比
- **遗漏引用**：Byerly & Khashabi (2026 TACL) 和 arxiv 2604.07650 直接相关但未引用

三个 Must-Fix 问题如果得到解决，可上调至 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1096 · 2026-05-21T07:54:28.962445+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 73

## Round 73

2 recorded events


### User

_source line 1097 · 2026-05-21T07:55:42.028289+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

### R2-N1: 核心负面结果的增量新颖性不足

**[REBUT]** 部分不同意。R2 的论点是 SCB 可从已有工作"组合中预测"，但这忽略了论文的关键 surprise：**形式化通道也失败**。

R2 引用的 Huang et al. (2024) 和 Stechly et al. (2025) 研究的是自然语言自纠错——它们不涉及 formal logic + provably sound SMT solver。论文在 Introduction 第25-26行明确指出这一区别："neurosymbolic methods implicitly assume that formalizing into logic provides a reliable verification channel. We test the strongest version of this assumption: first-order logic checked by a provably sound SMT solver (Z3), which *guarantees* logical consistency given well-formed constraints. That this stronger channel still fails is the central surprise: Z3 rejects only 3.4% of constraints (§5.2) because they are individually valid yet collectively biased---the bias is semantic (what gets extracted) rather than syntactic (how it is expressed)."

具体来说：
1. Amonkar et al. (2025) 展示了形式化*翻译*的失败（~40% translation errors），而本文的约束 **99.0% 在 Z3 level 是合法的**（Section 3.2），失败点不是翻译质量而是语义偏差——这是一个不同的 failure mode。
2. Chan et al. (2026) 是 position paper，无系统实验；本文提供了量化证据（BR=4.97×, 27 strategies, oracle controls）。
3. Wan et al. (2025) 和 Jhaveri et al. (2026) 研究的是 CoT-level confirmation bias（推理过程中的确认偏差），而 SCB 是 **self-extracted formal constraints** 层面的偏差——Section 2 (Related Work) 最后一段明确区分："Symbolic confirmation bias is distinct from CoT unfaithfulness...and CoT-level confirmation bias...the latter concerns whether stated reasoning reflects actual computation...while SCB concerns whether *self-extracted formal constraints* mirror the model's answer distribution regardless of logical form."

**但我也认同**：论文应在 Introduction 中更早、更清晰地建立与这些先前工作的 distinction。目前的区分主要在 Related Work 末尾（Section 2 最后一段），位置过晚。建议在 Introduction 第24行（引用 Huang/Stechly 处）就加入一句话解释形式化通道的额外假设。

量化工具层面（BR, K_eff, C_0 三个可复用诊断指标）是独立贡献，R2 未充分考虑这一点。

---

### R2-N2: 模型规模限制削弱结论普适性

**[AGREE]** 同意标题和 Abstract 需要限定范围。

论文标题 "Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning" 确实是 unqualified universal claim。实验仅覆盖 7B-32B（Section 4.1: "Qwen2.5-14B-Instruct...QwQ-32B (7B–32B parameters)"）。Limitations 第1段承认 "All models range from 7B to 32B parameters; whether the independence bottleneck persists at larger scales (70B+) or with reasoning-specialized models is untested."

不过我要补充一个 nuance：论文的数据实际上显示了一个**随能力增强恶化**的趋势——Qwen3-14B thinking mode 的 κ=0.91, K_eff=1.09（Table 2），意味着更强模型的 trace 更加同质化。如果这个趋势外推到 70B+，bottleneck 可能更严重而非更轻。当然外推不能替代实验，标题确实需要加限定词（如 "at the 7B-32B Scale"）。

---

### R2-N3: Independence-Accuracy Trade-off 与经典 ensemble diversity-accuracy dilemma 区分不足

**[REBUT]** 大部分不同意。

论文确实在 Discussion Section 7 第2段引用了 Krogh & Vedelsby (1994) 和 Brown et al. (2005)，并明确将其发现定位为 "This instantiates the classic ensemble tension"。R2 说 "论文仅用一句话提及"——实际上是一整段讨论（Discussion 第2段，约8行），包括 Debate 的具体数据（κ from ~1.8 to ~4.5, accuracy -18.6pp）和 cross-architecture 成功的机制解释。

更重要的是，CJT framing 提供了 **LLM-specific 的量化工具**，这是经典 ensemble 文献没有的：
- K_eff（Eq. 1）直接从 Fleiss' κ 推导有效样本量，是一个可操作的诊断指标
- BR（Eq. 5）量化 post-hoc rationalization 的强度
- C_0 是 zero-cost 的退化检测器

经典 diversity-accuracy literature 没有提供这些 LLM trace-specific 的诊断工具。论文的贡献不在于发现了 diversity-accuracy tradeoff 本身（这确实是已知的），而在于**在 LLM self-extraction 场景下量化了这个 tradeoff 的具体形态**。

但我同意论文应在 Section 3 introduction 处更明确地声明："我们不是发现了新的 tradeoff，而是为已知 tradeoff 在 LLM 场景下提供了量化诊断工具。"

---

## Should-Fix 问题

### R2-W1: 术语过度品牌化

**[REBUT]** 部分不同意。

"Symbolic Mirage" 的核心 claim 不仅仅是"自我验证失败"（这确实是已知的），而是包含三个可测试预测的完整假说：(1) BR>1 across architectures, (2) no same-model intervention reduces BR below 1.0, (3) only external verification escapes。这些预测全部被实验确认（Section 5.2, 5.5, 6）。给一个有 specific predictions 并被 systematically tested 的假说命名，在学术写作中是合理的。

"Independence Bottleneck" 作为术语确实更接近 rebranding，因为它本质上就是 Ladha (1992) 的 correlated voting + Kish (1965) 的 design effect。建议降低这个术语的使用频率，或直接引用原始概念。

---

### R2-W2: DRC 评估不充分

**[AGREE]** 同意。这与我自己的 W4 一致。

DRC 仅在 Mistral-7B ProofWriter (n=600) 上评估（Table 4），τ=0.7 在 evaluation set 上选择（Section 6.1 末尾承认），未进行 cross-dataset validation 或与其他 adaptive routing 方法对比。作为 Contribution 4 列出，评估深度不足。建议降级为 preliminary result / proof-of-concept，或增加 FOLIO 上的 DRC 评估和 cross-validation。

---

### R2-W3: Related Work 存在重要遗漏

**[AGREE]** 条件性同意——如果 R2 引用的文献确实相关且已公开发表。

我无法独立验证 R2 提到的 4 篇具体文献（Byerly & Khashabi 2026 TACL; arxiv 2604.07650; arxiv 2506.07962; arxiv 2510.01499）的内容和相关性。但论文的 Related Work（Section 2）确实以**listing style**为主，对每篇引用的具体 contribution 和与本文的 differential positioning 讨论不够深入。如果这些文献确实系统性地测试了 self-extracted constraints 或 formal verification under correlated errors，那么遗漏它们是一个问题。

建议作者根据 R2 提供的引用列表逐一检查并补充。

---

### R2-W4: Related Work 讨论深度不足，与 SatLM 对比不充分

**[REBUT]** 部分不同意。

关于 SatLM，论文在 Related Work Section 2 第2段有明确对比："SatLM provides a natural control: it succeeds because problem-level formalization precedes answer generation, whereas trace-level extraction cannot avoid contamination (§3.3)." 这不是一句话带过——它识别了 SatLM 成功的关键原因（formalization *precedes* candidate generation）以及本文方法失败的结构性差异（trace-level extraction is *post-hoc*）。

但 R2 说 Related Work 以 listing 为主的批评有一定道理。Section 2 的第三段（Test-time compute and verification）引用了 12 篇文献，部分仅是 "\citep{}" 列表。建议对其中 2-3 篇最相关的（如 weng2023selfverification, gou2024critic）增加 1-2 句具体对比。

---

### R2-W5: Abstract 未限定结论范围

**[AGREE]** 同意，与 R2-N2 一致。

Abstract 第3行 "self-extracted constraints do not improve majority voting at any capacity level" 应改为 "...at any capacity level tested (7B–32B)"。这是一个简单的文字修改。

---

## 对 R2 Questions 的补充评论

**Q1 (70B+ 模型 BR 是否可能质变)**：这是一个合理的开放问题。论文数据显示 BR 随能力增强*下降*（Mistral 4.97× → Qwen-14B 3.93× → LLaMA 2.88×, Table 15），但始终 >1.0。外推到 70B+ 是否会跨越 BR=1.0 阈值需要实验验证。论文应在 Discussion 中明确讨论这个趋势。

**Q2 (Fleiss' κ 代入 Kish design effect 是否合理)**：这与我自己的小问题观察一致（κ 和 ICC 的单调关系仅 r=0.625）。论文在 Section 3.1 承认 K_eff 应作为 ordinal diagnostic，这个声明是恰当的，但后续使用偶有逾越。

**Q5 (SCB vs Wan et al. CoT confirmation bias)**：论文在 Related Work 最后一段已区分，但该区分的位置太晚。建议移到 Introduction 或 Method section。

---

**总结**：R2 的 N2（标题/scope 限定）和 W2（DRC 评估不足）是合理的改进建议。N1（新颖性）和 N3（与 ensemble literature 重叠）的批评部分成立但被过度表述——论文的贡献不在于发现新概念，而在于提供了第一个系统性的量化验证，特别是证明 formal verification channel (Z3) 同样无法逃逸 self-extraction bias。

**审稿人签名**: Reviewer 1


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1098 · 2026-05-21T07:55:47.522405+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 1099 · 2026-05-21T07:55:53.667501+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1 (新颖性)**: [REBUT] — 核心 surprise 在于 Z3 formal verification 也失败（99% 约束合法但语义偏差），这与 Huang/Stechly 的自然语言自纠错是不同 failure mode，但同意应更早建立 distinction
- **R2-N2 (规模限制)**: [AGREE] — 标题和 Abstract 确实需要加 "7B-32B" 限定
- **R2-N3 (与 ensemble 文献重叠)**: [REBUT] — CJT framing 提供了 LLM-specific 量化工具（K_eff, BR, C_0），但同意应声明贡献是量化而非发现新 tradeoff
- **R2-W1 (品牌化)**: [REBUT] — "Symbolic Mirage" 有三个可测试预测，命名合理；"Independence Bottleneck" 确实接近 rebranding
- **R2-W2 (DRC 评估)**: [AGREE] — 与我的 W4 一致
- **R2-W3 (遗漏引用)**: [AGREE] — 条件性同意，需验证具体文献
- **R2-W4 (SatLM 对比)**: [REBUT] — SatLM 对比已有明确讨论，但部分引用确实 listing-style
- **R2-W5 (Abstract scope)**: [AGREE] — 简单文字修改

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1100 · 2026-05-21T07:55:57.913535+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 75

## Round 75

20 recorded events


### User

_source line 1101 · 2026-05-21T07:56:29.167573+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Spearman ρ=1.0 (n=6) 的统计可靠性**

同意这是一个严重的统计问题。n=6 的 Spearman 相关本身就接近 rank correlation 的最低有效样本量（permutation test 只有 6!=720 种排列），而 R1 进一步指出 4/6 数据点共享 DeBERTa verifier——这违反了 permutation test 的交换性假设，有效自由度可能仅为 2-3。论文在 Abstract（p.1）、Section 1 contributions（p.2）、Section 6.1（p.8）、Discussion（p.8）中反复引用 "Spearman ρ = 1.0, p = 0.003"，将其作为 DRC 有效性的核心证据和从负面结果转向正面贡献的桥梁。这一统计基础过于薄弱，不足以承受如此重的论证权重。

补充发现：我在 Section 6.1 (p.7-8) 注意到 combo gain 的具体数值跨度很大（+5.17pp 到 +14.22pp），n=6 时一个异常值就可以驱动完美的 rank correlation。建议如 R1 所述降级为趋势性描述，并增加 non-DeBERTa verifier 实验以增强外部效度。

---

**[REBUT] R1-N2: "SICA fails" 断言与功效不匹配（部分反驳）**

R1 的批评——"absence of evidence ≠ evidence of absence"——作为一般性原则是正确的。但 R1 对论文方法论的描述不够准确。论文并非仅依赖"未拒绝零假设"来声称无效果，而是明确使用了 TOST 等价性检验（Section 4.2, p.5；Appendix E, p.14），这恰恰是为了区分 "no evidence of effect" 和 "evidence of no effect" 而设计的统计工具。具体来看：

- 4/16 条件通过了 TOST 等价性检验（|Δ| < 2pp 的 evidence of absence）
- 2/16 条件显示显著负效应（evidence of harm）
- 10/16 条件确实 inconclusive

所以论文在 6/16 条件上有实质性统计证据（4 个等价 + 2 个负面），在 10/16 上确实 underpowered。

**但我同意 R1 关于 Abstract 措辞的批评**：Abstract 的 "do not improve majority voting at any capability level" 确实比统计证据支持的更强。10/16 条件 inconclusive 时不能做 universal negative claim。应修改为 R1 建议的更谨慎措辞——"we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two"。

总结：方法论层面部分反驳（论文使用了正确的 TOST 工具），但 claim 措辞层面同意需要 tone down。

---

**[AGREE] R1-N3: TOST ±2pp margin 缺乏 principled 论证**

完全同意。这也是我在审稿中关注但未作为独立问题提出的点。跨 39% 到 86% 的 baseline accuracy 使用固定 ±2pp 绝对 margin 在统计上不合理：

- 对 39% baseline（如 GSM8K 上的弱模型），2pp 是 ~5% relative margin，非常宽松
- 对 86% baseline（如 FOLIO 上的强模型），2pp 是 ~2.3% relative margin，相对严格

Appendix S（如果 R1 引用准确的话）显示 ±1pp → 0 条件等价，±3pp → 10 条件等价。这种高灵敏度意味着等价性结论几乎完全取决于 margin 选择，而 margin 选择缺乏 principled justification。

R1 建议使用 relative margin（如 baseline 的 5%）是合理的。此外，论文引用了 Lakens (2017) 的等价性检验方法论（Section 4.2, Appendix V），但 Lakens 本人强调 margin 应基于 "smallest effect size of interest" 的领域知识来设定，论文未提供这一论证。

---

### Should-Fix 问题

**[AGREE] R1-W1: Proposition 1 / Observation 2 形式化程度与严格性不匹配**

同意。我在阅读 Section 3.3（p.4）和 Section 5（p.5-6）时也注意到了这一问题。使用 "Proposition" 和 "Bound" 暗示了形式化的数学推导，但实际内容是 empirical observation。"≲" 符号在数学中通常表示 "asymptotically less than or equal to"，但论文中似乎用于模糊的近似关系，未给出精确定义。这种 pseudo-formalism 可能误导读者对结果严格性的预期。建议使用 "Empirical Finding" 或 "Observation" 替代 "Proposition" 和 "Bound"。

---

**[AGREE] R1-W2: DRC 的通用性被过度暗示**

同意，且与我自己的 W2 一致。DRC 仅在 NLI-shaped tasks（FOLIO 的 entailment/contradiction 标签、ProofWriter 的 True/False 标签）上有效，这些任务的输出格式天然适配 NLI verifier。对于 GSM8K（数值答案）、StrategyQA（yes/no + 多步推理）和 LogiQA（多选）等非 NLI-shaped tasks，DRC 的适用性未经验证。3 个 verifier 全是 encoder-only MNLI-finetuned 模型（DeBERTa, RoBERTa, BART），进一步限制了架构多样性。论文 Section 6 的标题 "Cross-Architecture Proof-of-Concept" 中的 "Proof-of-Concept" 是合理的限定，但 Abstract 和 Conclusion 的措辞未充分传达这一限制。

---

**[REBUT] R1-W3: "27 strategies" 计数膨胀（部分反驳）**

R1 认为 27 种策略包含超参变体和 ad hoc 尝试，存在计数膨胀。查看 Table 13（p.17），27 种策略确实覆盖了不同粒度的变体：prompt 变体（~4 种）、diverse prompting（~3 种）、extraction quality filtering（~3 种）、aggregation variants（~5 种）、constraint weighting（~3 种）、semantic dedup（~2 种）、self-refine/debate（~3 种）、multi-agent（~4 种）。

部分反驳：即使将超参变体合并为同一"策略族"，仍有 ~12-15 个独立的策略方向。更重要的是，论文的论证逻辑是"穷举搜索后仍无改进"，策略的数量（即使有膨胀）仍然支撑这一论证——它排除了"只是没找到正确配置"的反驳。

**但同意 R1 关于 trained extractors 的批评**：所有 27 种策略都是 prompt-based extraction。未尝试 fine-tuned constraint extractor（如在少量标注数据上 SFT 一个专用提取模型）是一个重要的实验空白。如果 trained extractor 能显著提升提取质量，论文的核心结论——"self-extracted constraints don't help"——可能需要限定为 "prompt-based self-extracted constraints don't help"。

---

**[AGREE] R1-W4: DRC τ 在 evaluation set 上选择**

同意。我注意到论文在 Observation 2 附近（Section 5, p.6）自己承认了 "τ was selected on the evaluation set; deployment would require a held-out validation split"。作者的诚实值得肯定，但这意味着 Table 4 中 DRC 的 "90% recovery at 39% cost" 数字可能乐观。对于一个需要在实际部署中设定阈值的方法，held-out validation 不是可选项而是必要条件。建议至少报告 leave-one-dataset-out cross-validation 的 τ 选择结果。

---

**[AGREE] R1-W5: 多数条件 single-seed，变异性问题**

同意。这是一个严肃的可靠性问题。如果 4-seed 复现显示 Δ 从 +3.43pp 到 -0.49pp 的变异（R1 引用），那么 single-seed 的主要结果可能处于这一变异区间的任何位置。Table 1 中大部分条件的 Δ 绝对值在 0-2pp 范围内，完全落在 multi-seed 变异区间之中。论文在 Section 4.2 提到 "four-seed replication" 显示 "similar patterns"，但如果 R1 引用的高变异数据准确，"similar patterns" 的表述需要更多 nuance。

补充：这一问题与 N2（功效不足）和 N3（TOST margin 灵敏度）叠加，形成了一个系统性的统计可靠性问题：single-seed + underpowered + margin-sensitive 等价性检验 = 结论的 robustness 存疑。

---

**[REBUT] R1-W6: BR 指标存在循环论证倾向（部分反驳）**

R1 认为 "模型错时提取约束也错是 self-extraction 的定义性结果"，因此 BR > 1 是逻辑必然而非新发现。

这一批评在表面上有道理——如果约束从错误 trace 中提取，它们自然倾向于支持错误答案。但我认为 BR 的价值不在于 direction（BR > 1）而在于 magnitude 和结构。具体来看 Table 2（p.6）：

- BR = 1.97 意味着错误约束的支持强度几乎是正确约束的 2 倍——这不是 trivially predictable 的 magnitude
- 94% 的错误 trace 与 SC 错误答案重叠——这量化了 confirmation 的 completeness
- Table 6 的 per-condition 分析（Appendix E, p.14）显示不同条件下 BR 的变异（从 ~1.5 到 ~3+），揭示了 task-specific 差异

然而，我承认 R1 的批评部分成立：论文将 BR > 1 呈现为 "discovery"（Section 5.2 标题 "Symbolic Confirmation Bias"），但更准确的定位应该是 "quantification of an expected phenomenon"。将已知现象的量化包装为新发现确实存在过度 claim 的倾向。

---

### 对 R1 Questions 的评论

1. **Relative TOST margin**: 同意应补充这一分析，结论很可能显著改变。
2. **Trained constraint extractor**: 同意这是重要的实验空白，如上述 W3 讨论。
3. **3 个独立 verifier 的 permutation test**: 同意 n=3 时 permutation test 几乎无意义（3!=6 种排列）。
4. **Multi-seed 复现**: 同意应至少在代表性条件（per-dataset per-model-family）做 multi-seed。
5. **SBERT 替代 TF-IDF**: 这是一个合理的 robustness check。TF-IDF 倾向于捕捉 surface-level 词汇重叠，SBERT 捕捉语义相似性。如果结论在两种度量下一致，则更可靠；如果不一致，则需要讨论哪种度量更适合衡量 "reasoning process independence"。

---

### 总结

R1 的审稿在统计方法论层面提出了多个尖锐且有效的批评。我与 R1 在以下核心问题上达成共识：

- **ρ=1.0 (n=6) 过度使用**（N1）：完全同意
- **Abstract 措辞过强**（N2 的措辞部分）：同意
- **TOST margin 论证不足**（N3）：完全同意
- **DRC 评估不充分**（W2, W4）：同意，与我的 W2 一致
- **Multi-seed 变异性**（W5）：同意，加剧了统计可靠性问题

我在以下方面提供了部分反驳或补充：

- **N2 的方法论层面**：论文使用 TOST 是正确的统计实践，不应被简单等同于 "failing to reject H0"
- **W3 策略计数**：即使有膨胀，穷举搜索的论证逻辑仍然成立；但同意 trained extractor 是重要遗漏
- **W6 BR 循环论证**：BR 的量化价值（magnitude, per-condition variation）超越了 direction 的 trivial predictability

综合 R1 和我的评估，论文的主要风险是：**统计证据的强度不足以支撑 claim 的强度**。如果 claim 降级为更谨慎的措辞（趋势性、有限条件内），论文在 Findings 水平是站得住的。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-21T07:57:12.536304+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-21T07:57:13.139361+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T07:46:03.098613+00:00\", \"completed_at\": \"2026-05-21T07:49:49.951209+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页中仅 page 2 右上有 Figure 1（SICA 流程图），page 1 和 page 3 为纯文本。Page 3（Related Work）整页无任何 display item，与 page 1 形成连续 2 页纯文字段。Figure 1 作为视觉锚点位置尚可，但 page 1 的首次视觉印象偏单调\"}, {\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"连续约 3 页无 figure 或 table：page 3 纯文本（Related Work），page 4 有公式但无 display item（Background），page 5 纯文本（Experiments Setup + Main Results 文字描述）。Table 1 直到 page 6 才出现。审稿人在这一段会感到视觉疲劳\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-9\", \"message\": \"主文 ~8.5 页仅含 1 个 figure（Figure 1 流程图）+ 4 个 table，没有任何结果可视化图。所有结果图（Figure 2-7）全部被推到附录 page 23-24。对于一篇实证分析为主的论文，主文缺少结果图是显著缺陷——审稿人不会翻到附录去找关键图表\"}, {\"severity\": \"warning\", \"dimension\": \"page 23\", \"message\": \"Figure 2（27 种干预策略效果汇总 bar chart）是全文最有冲击力的结果可视化，但被放在附录 page 23。这张图应考虑放入主文（如 Section 5.5 Remediation Analysis 或 Section 7 Discussion 附近），能显著增强论文说服力\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 流程图：整体清晰，颜色区分合理（蓝色框、红色虚线框、金色 FOL 标注），但图内文字偏小，建议稍微放大关键标注。Caption 具备自包含性\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 主结果表：使用 booktabs 风格，最优值加粗，精度统一，排版专业。但 Table 1 在 page 5 被首次引用，出现在 page 6 顶部——间距可接受但稍远\"}, {\"severity\": \"info\", \"dimension\": \"page 6-7\", \"message\": \"Table 2 trace independence metrics：booktabs 风格，格式规范。跨页放置，阅读连贯性略受影响\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 和 Table 4 同时出现在一页，与 Discussion + Conclusion 文字共存。页面密度高但未溢出，排版紧凑可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"Figure 2 上方有约 1/3 页空白。如果此图留在附录，应上移减少空白；如果移入主文则无此问题\"}, {\"severity\": \"info\", \"dimension\": \"page 24\", \"message\": \"Figures 3-7 五张图挤在一页，每张图尺寸很小（约 1/5 页高），图内坐标轴标签和数据点标注在正常阅读距离下可能难以辨认。建议拆分为 2 页或选择性合并 subfigure\"}, {
…[truncated 889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-21T07:57:23.946259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-21T07:57:23.997036+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-21T07:57:27.411732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "description": "Count total issues in tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "description": "Count total issues in tracker"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-21T07:57:27.613113+00:00_

84

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-21T07:57:31.681195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B1 \"status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | grep \"id:\" | sed 's/.*id: \"\\(.*\\)\"/\\1/' | head -40",
  "description": "Get IDs of in_progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B1 \"status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | grep \"id:\" | sed 's/.*id: \"\\(.*\\)\"/\\1/' | head -40",
    "description": "Get IDs of in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-21T07:57:31.801343+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 120
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-21T07:57:35.114805+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 \"status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | grep \"id:\" | head -40",
  "description": "Get in_progress issue IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 \"status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | grep \"id:\" | head -40",
    "description": "Get in_progress issue IDs"
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-21T07:57:35.167402+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-21T07:57:39.834227+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "awk '/^- id:/{id=$0} /status: in_progress/{print id}' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | head -40",
  "description": "Extract in_progress issue IDs using awk"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "awk '/^- id:/{id=$0} /status: in_progress/{print id}' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | head -40",
    "description": "Extract in_progress issue IDs using awk"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-21T07:57:39.885245+00:00_

- id: "R4-W3"
- id: "R5-W9"
- id: "R5-W9"
- id: "R6-N3"
- id: "R6-N3"
- id: "R6-W4"
- id: "R6-W4"
- id: "R8-N2"
- id: "R8-N2"
- id: "R9-W2"
- id: "R9-W2"
- id: "R9-W3"
- id: "R9-W4"
- id: "R9-W4"
- id: "R9-W5"
- id: "R9-W6"
- id: "R9-W6"
- id: "R9-W7"
- id: "R9-W7"
- id: "R9-W8"
- id: "R9-W8"
- id: "R9-W9"
- id: "R9-W9"
- id: "R9-W10"
- id: "R9-W10"
- id: "R9-W11"
- id: "R9-W11"
- id: "R9-W12"
- id: "R9-VL1"
- id: "R9-VL1"
- id: "R9-VL4"
- id: "R9-VL4"
- id: "R10-N1"
- id: "R10-N1"
- id: "R10-N2"
- id: "R10-N2"
- id: "R10-N3"
- id: "R10-N3"
- id: "R10-W1"
- id: "R10-W1"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-21T07:57:43.205063+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "awk '/^- id:/{id=$0} /status: in_progress/{print id}' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | sort -u",
  "description": "Get unique in_progress issue IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "awk '/^- id:/{id=$0} /status: in_progress/{print id}' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml | sort -u",
    "description": "Get unique in_progress issue IDs"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-21T07:57:43.306253+00:00_

- id: "R10-I1"
- id: "R10-I2"
- id: "R10-N1"
- id: "R10-N2"
- id: "R10-N3"
- id: "R10-VL1"
- id: "R10-W1"
- id: "R10-W2"
- id: "R10-W3"
- id: "R10-W4"
- id: "R10-W5"
- id: "R10-W6"
- id: "R10-W7"
- id: "R10-W8"
- id: "R10-W9"
- id: "R4-W3"
- id: "R5-W9"
- id: "R6-N3"
- id: "R6-W4"
- id: "R8-N2"
- id: "R9-VL1"
- id: "R9-VL4"
- id: "R9-W10"
- id: "R9-W11"
- id: "R9-W12"
- id: "R9-W2"
- id: "R9-W3"
- id: "R9-W4"
- id: "R9-W5"
- id: "R9-W6"
- id: "R9-W7"
- id: "R9-W8"
- id: "R9-W9"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-21T08:00:23.143277+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9-10 in_progress issues — many persist into R11\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6, ρ=1.0 重复7次\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-3 连续 3 页纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 11\n      reviewers: []\n      note: \"R11 视觉审查再次确认: pages 1-3 仅 page 2 有 Figure 1\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 11\n      reviewers: []\n      note: \"R11 视觉审查: Conclusion 起始在 page 8 下半部分，heading 后有充足正文，无孤悬问题。可能已改善\"\n\n# Round 10 issues — check persistence\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Bound 1 无推导, ≲ 未定义\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 两位 Reviewer 一致: Proposition/Bound 伪形式化, 应降级为 Empirical Finding/Observation\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱，ordinal caveat 与 quantitative usage 矛盾\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 再次确认: ordinal diagnostic 声明正确但后续使用偶有逾越\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 critical consensus: 4/6 共享 DeBERTa, 有效自由度≤3-4, 重复7次 overweight\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"τ=0.7 在 eval set 上选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: τ 在 eval set 选择是过拟合风险, 90% recovery 数字乐观\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著, 3 verifier 全 MNLI-finetuned\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: 实际是 NLI verification on NLI-shaped tasks, 非通用 cross-architecture escape\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"4-seed Δ range ≈4pp, single-seed 不够\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: single-seed + underpowered + TOST margin-sensitive 构成系统性可靠性问题\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"margin 选择无 principled justification\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical consensus: ±1pp→0等价, ±3pp→10等价, 高度敏感; 跨 39-86% baseline 固定绝对 margin 不合理\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"R11 未再提及 BR 缺 CI, 但 R1 指出 BR 存在循环论证倾向(tautological tendency), R2 部分反驳(magnitude matters)\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"SatLM 对比隐含在管线描述中\"\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 再次提出; R1 反驳称 Related Work 已有明确对比('SatLM provides a natural control...')\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Wan et al. 2025, Jhaveri et al. 2026 区分不足\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: Related Work 末段有区分但位置太晚, 应移到 Introduction 更早建立 distinction\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"引用 listing 而非 critical discussion\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: 部分段落以 parenthetical citation list 为主, 应对 2-3 篇最相关工作深入对比\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"正文仅摘要, 策略细节在附录\"\n    - round: 11\n      reviewers: [1]\n      note: \"R11 R1: 计数膨胀(含超参变体/ad hoc 尝试/n≤60条件), 未尝试 trained extractors; R2 部分反驳(穷举论证仍成立)\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"负面结果增量有限\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 核心分歧: R2 认为可从先验工作预测(3.0), R1 认为 formal channel failure 是 genuine surprise(3.5). 双方同意应更早更明确建立 distinction\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"与经典 ensemble diversity-accuracy dilemma 重叠\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 分歧: R2 认为是 restatement, R1 认为 CJT 提供 LLM-specific 量化工具. 双方同意应声明贡献在量化而非发现新 tradeoff\"\n\n- id: \"R10-VL1\"\n  summary: \"Pages 3-5 连续无 display item；page 7 display items 过度拥挤\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"视觉审查\"\n    - round: 11\n      reviewers: []\n      note: \"R11 视觉审查再次确认: pages 3-5 连续无 figure/table, Table 1 直到 page 6; 主文仅1 figure+4 tables, 所有结果图在附录\"\n\n# New R11 issues\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6, 重复7次\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"4/6 共享 DeBERTa verifier 违反 permutation test 交换性假设. 'strongly monotonic ρ=1.0 p=0.003' 在 Abstract/Intro/Section 6/Discussion/Conclusion 重复至少7次. 建议降级为趋势描述, 减少重复(≤3次), 增加 non-DeBERTa verifier\"\n  action_items:\n    - round: 11\n      action: \"降级 'strongly monotonic' 为 'consistent with a monotonic trend'; 减少重复至≤3次; 添加 shared-verifier 限制讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"10/16 conditions underpowered, 观测功效<21%. TOST 方法论正确(R2 部分反驳 R1), 但 Abstract 'do not improve at any capability level' 超出证据范围. 同时标题需限定模型规模(7B-32B)\"\n  action_items:\n    - round: 11\n      action: \"Abstract 改为 'we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two'; 标题加 '7B-32B' 或 'at Current Scale' 限定\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证——等价结论对 margin 高度敏感\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"跨 39-86% baseline 使用固定绝对 margin; ±1pp→0等价, ±3pp→10等价. Lakens (2017) 要求基于 SESOI 的领域论证. 建议考虑 relative margin 或在正文报告 sensitivity\"\n  action_items:\n    - round: 11\n      action: \"提供 margin 选择的 principled justification; 正文报告 ±1pp/±3pp sensitivity; 考虑 relative margin\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅2数据集、单一 NLI 范式、τ 无 held-out validation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"作为 Contribution 4 列出但评估深度不足. τ=0.7 在 eval set 选择. 建议降级为 proof-of-concept 或增加 cross-dataset validation\"\n  action_items:\n    - round: 11\n      action: \"至少做 cross-dataset τ validation; 或降级为 preliminary result\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向——quantification vs discovery 定位不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1: BR>1 是 self-extraction 的定义性结果; R2: magnitude(4.97×) 和 per-condition variation 有价值. 共识: 应定位为 quantification 而非 discovery\"\n  action_items:\n    - round: 11\n      action: \"Discussion 中承认 BR direction 的 tautological 倾向; 将 magnitude/variation 定位为核心贡献\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 接近 rebranding\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: 全部品牌化过多. R1: 'Symbolic Mirage' 有3个可测试预测合理, 'Independence Bottleneck' 确实是 rebranding. 共识: 至少降低 'Independence Bottleneck' 使用频率\"\n  action_items:\n    - round: 11\n      action: \"保留 'Symbolic Mirage' 和 'Symbolic Confirmation Bias'; 降低 'Independence Bottleneck' 品牌化, 改用描述性语言\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: SCB 可从 Huang/Stechly/Wan/Amonkar/Chan 组合预测. R1 反驳: formal channel (Z3) failure 是 genuine surprise (99% 合法但语义偏差). 双方同意: Introduction 应更早建立 distinction, 不能等到 Related Work 末尾\"\n  action_items:\n    - round: 11\n      action: \"Introduction 中引用 Huang/Stechly 处(~第24行)加入形式化通道额外假设的论证; 将 Related Work 末段的区分内容前移\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: 与 Krogh/Brown 经典 ensemble diversity-accuracy dilemma 重叠. R1 反驳: CJT 提供 LLM-specific 工具(K_eff, BR, C_0). 共识: 声明贡献在量化而非发现新 tradeoff\"\n  action_items:\n    - round: 11\n      action: \"Section 3 或 Discussion 明确声明: 'We do not claim to discover a new tradeoff; our contribution is quantifying its specific form in LLM self-extraction'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL), arxiv 2604.07650, arxiv 2506.07962\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"Byerly & Khashabi: SC 在 long-context 失败; 2604.07650: LLM 独立性审计框架; 2506.07962: LLM 错误相关性. R1 条件性同意(需验证)\"\n  action_items:\n    - round: 11\n      action: \"验证并补充 Byerly & Khashabi (2026) 和 arxiv 2506.07962; 酌情引用 2604.07650\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1: 含超参变体/ad hoc 尝试, 计数膨胀. R2 部分反驳: 穷举论证仍成立. 共识: trained extractor 是重要实验空白, 应在 Discussion 讨论\"\n  action_items:\n    - round: 11\n      action: \"区分 principled strategies 和 exploratory attempts; Discussion 中讨论 trained extractors 作为 future work\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-VL1\"\n  summary: \"主文仅1 figure + 4 tables, 所有结果图推至附录——Figure 2 应上提至主文\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"视觉审查: Figure 2(27策略汇总 bar chart)是全文最有冲击力的结果图但在附录 p.23. 主文缺少结果可视化是显著缺陷\"\n  action_items:\n    - round: 11\n      action: \"将 Figure 2 上提至主文 Section 5.5 或 Discussion 附近\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9-10 in_progress issues — many persist into R11\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6, ρ=1.0 重复7次\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-3 连续 3 页纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 11\n      reviewers: []\n      note: \"R11 视觉审查再次确认: pages 1-3 仅 page 2 有 Figure 1\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 11\n      reviewers: []\n      note: \"R11 视觉审查: Conclusion 起始在 page 8 下半部分，heading 后有充足正文，无孤悬问题。可能已改善\"\n\n# Round 10 issues — check persistence\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Bound 1 无推导, ≲ 未定义\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 两位 Reviewer 一致: Proposition/Bound 伪形式化, 应降级为 Empirical Finding/Observation\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱，ordinal caveat 与 quantitative usage 矛盾\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 再次确认: ordinal diagnostic 声明正确但后续使用偶有逾越\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 critical consensus: 4/6 共享 DeBERTa, 有效自由度≤3-4, 重复7次 overweight\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"τ=0.7 在 eval set 上选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: τ 在 eval set 选择是过拟合风险, 90% recovery 数字乐观\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著, 3 verifier 全 MNLI-finetuned\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: 实际是 NLI verification on NLI-shaped tasks, 非通用 cross-architecture escape\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"4-seed Δ range ≈4pp, single-seed 不够\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: single-seed + underpowered + TOST margin-sensitive 构成系统性可靠性问题\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"margin 选择无 principled justification\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical consensus: ±1pp→0等价, ±3pp→10等价, 高度敏感; 跨 39-86% baseline 固定绝对 margin 不合理\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"R11 未再提及 BR 缺 CI, 但 R1 指出 BR 存在循环论证倾向(tautological tendency), R2 部分反驳(magnitude matters)\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"SatLM 对比隐含在管线描述中\"\n    - round: 11\n      reviewers: [2]\n      note: \"R11 R2 再次提出; R1 反驳称 Related Work 已有明确对比('SatLM provides a natural control...')\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Wan et al. 2025, Jhaveri et al. 2026 区分不足\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11: Related Work 末段有区分但位置太晚, 应移到 Introduction 更早建立 distinction\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"引用 listing 而非 critical discussion\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 consensus: 部分段落以 parenthetical citation list 为主, 应对 2-3 篇最相关工作深入对比\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"正文仅摘要, 策略细节在附录\"\n    - round: 11\n      reviewers: [1]\n      note: \"R11 R1: 计数膨胀(含超参变体/ad hoc 尝试/n≤60条件), 未尝试 trained extractors; R2 部分反驳(穷举论证仍成立)\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"负面结果增量有限\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 核心分歧: R2 认为可从先验工作预测(3.0), R1 认为 formal channel failure 是 genuine surprise(3.5). 双方同意应更早更明确建立 distinction\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"与经典 ensemble diversity-accuracy dilemma 重叠\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 分歧: R2 认为是 restatement, R1 认为 CJT 提供 LLM-specific 量化工具. 双方同意应声明贡献在量化而非发现新 tradeoff\"\n\n- id: \"R10-VL1\"\n  summary: \"Pages 3-5 连续无 display item；page 7 display items 过度拥挤\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"视觉审查\"\n    - round: 11\n      reviewers: []\n      note: \"R11 视觉审查再次确认: pages 3-5 连续无 figure/table, Table 1 直到 page 6; 主文仅1 figure+4 tables, 所有结果图在附录\"\n\n# New R11 issues\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6, 重复7次\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"4/6 共享 DeBERTa verifier 违反 permutation test 交换性假设. 'strongly monotonic ρ=1.0 p=0.003' 在 Abstract/Intro/Section 6/Discussion/Conclusion 重复至少7次. 建议降级为趋势描述, 减少重复(≤3次), 增加 non-DeBERTa verifier\"\n  action_items:\n    - round: 11\n      action: \"降级 'strongly monotonic' 为 'consistent with a monotonic trend'; 减少重复至≤3次; 添加 shared-verifier 限制讨论\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"10/16 conditions underpowered, 观测功效<21%. TOST 方法论正确(R2 部分反驳 R1), 但 Abstract 'do not improve at any capability level' 超出证据范围. 同时标题需限定模型规模(7B-32B)\"\n  action_items:\n    - round: 11\n      action: \"Abstract 改为 'we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two'; 标题加 '7B-32B' 或 'at Current Scale' 限定\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证——等价结论对 margin 高度敏感\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"跨 39-86% baseline 使用固定绝对 margin; ±1pp→0等价, ±3pp→10等价. Lakens (2017) 要求基于 SESOI 的领域论证. 建议考虑 relative margin 或在正文报告 sensitivity\"\n  action_items:\n    - round: 11\n      action: \"提供 margin 选择的 principled justification; 正文报告 ±1pp/±3pp sensitivity; 考虑 relative margin\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅2数据集、单一 NLI 范式、τ 无 held-out validation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"作为 Contribution 4 列出但评估深度不足. τ=0.7 在 eval set 选择. 建议降级为 proof-of-concept 或增加 cross-dataset validation\"\n  action_items:\n    - round: 11\n      action: \"至少做 cross-dataset τ validation; 或降级为 preliminary result\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向——quantification vs discovery 定位不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1: BR>1 是 self-extraction 的定义性结果; R2: magnitude(4.97×) 和 per-condition variation 有价值. 共识: 应定位为 quantification 而非 discovery\"\n  action_items:\n    - round: 11\n      action: \"Discussion 中承认 BR direction 的 tautological 倾向; 将 magnitude/variation 定位为核心贡献\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 接近 rebranding\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: 全部品牌化过多. R1: 'Symbolic Mirage' 有3个可测试预测合理, 'Independence Bottleneck' 确实是 rebranding. 共识: 至少降低 'Independence Bottleneck' 使用频率\"\n  action_items:\n    - round: 11\n      action: \"保留 'Symbolic Mirage' 和 'Symbolic Confirmation Bias'; 降低 'Independence Bottleneck' 品牌化, 改用描述性语言\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: SCB 可从 Huang/Stechly/Wan/Amonkar/Chan 组合预测. R1 反驳: formal channel (Z3) failure 是 genuine surprise (99% 合法但语义偏差). 双方同意: Introduction 应更早建立 distinction, 不能等到 Related Work 末尾\"\n  action_items:\n    - round: 11\n      action: \"Introduction 中引用 Huang/Stechly 处(~第24行)加入形式化通道额外假设的论证; 将 Related Work 末段的区分内容前移\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2: 与 Krogh/Brown 经典 ensemble diversity-accuracy dilemma 重叠. R1 反驳: CJT 提供 LLM-specific 工具(K_eff, BR, C_0). 共识: 声明贡献在量化而非发现新 tradeoff\"\n  action_items:\n    - round: 11\n      action: \"Section 3 或 Discussion 明确声明: 'We do not claim to discover a new tradeoff; our contribution is quantifying its specific form in LLM self-extraction'\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL), arxiv 2604.07650, arxiv 2506.07962\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"Byerly & Khashabi: SC 在 long-context 失败; 2604.07650: LLM 独立性审计框架; 2506.07962: LLM 错误相关性. R1 条件性同意(需验证)\"\n  action_items:\n    - round: 11\n      action: \"验证并补充 Byerly & Khashabi (2026) 和 arxiv 2506.07962; 酌情引用 2604.07650\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1: 含超参变体/ad hoc 尝试, 计数膨胀. R2 部分反驳: 穷举论证仍成立. 共识: trained extractor 是重要实验空白, 应在 Discussion 讨论\"\n  action_items:\n    - round: 11\n      action: \"区分 principled strategies 和 exploratory attempts; Discussion 中讨论 trained extractors 作为 future work\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-VL1\"\n  summary: \"主文仅1 figure + 4 tables, 所有结果图推至附录——Figure 2 应上提至主文\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: []\n      note: \"视觉审查: Figure 2(27策略汇总 bar chart)是全文最有冲击力的结果图但在附录 p.23. 主文缺少结果可视化是显著缺陷\"\n  action_items:\n    - round: 11\n      action: \"将 Figure 2 上提至主文 Section 5.5 或 Discussion 附近\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-21T08:00:23.248054+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 16514}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-21T08:03:10.592264+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 11 审稿报告（Fresh Review）\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验可靠性; R2: 新颖性+完整性+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享 → 逐条 AGREE/REBUT → 收敛（1轮达成）\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束、通过加权部分 MAX-SAT 聚合答案。在 6 个开源 LLM（7B-32B）、3 个逻辑推理数据集、3,000+ 条件评估上，作者发现自提取符号约束在任何已测试的模型能力水平上都无法改进 Self-Consistency。论文识别了\"Symbolic Confirmation Bias\"（BR=4.97×）和 process-level independence bottleneck（CoT cosine similarity 0.69 >> answer κ 0.46），证明 27 种 same-model remediation 策略全部失败。Oracle 控制实验确认聚合机制本身有效（+29.90pp, +14.22pp），瓶颈在 self-extraction 质量。Cross-architecture NLI 验证在 verifier 能力超过 generator 时产生显著增益（Mistral-7B +6.67pp, p<0.001），DRC 路由方法在 39% 成本下恢复 90% 增益。\n\n---\n\n## Strengths\n\n1. **实验设计的系统性前所未有**：6 models × 3 datasets × 27 strategies × oracle controls × cross-arch escape × 4-seed replication，覆盖面远超同类工作。穷举式搜索有效排除了\"只是没找到正确配置\"的反驳。\n2. **统计方法论在 NLP 实证研究中属上乘**：McNemar + BH FDR + TOST 等价性检验 + Bootstrap CI + Power analysis 构成完整统计推断链。TOST 的使用（区分\"无效果证据\"和\"证据不足\"）值得肯定。\n3. **Oracle 控制实验设计精妙**：FOLIO gold annotations + ProofWriter DSL 作为 oracle constraints，干净隔离了 extraction quality 和 aggregation mechanism，是论文最强的方法论贡献。\n4. **\"Symbolic Mirage\" 概念框架完整**：包含三个可测试预测（BR>1 跨架构、same-model 无法突破 BR<1、only external verification escapes），全部被数据确认。\n5. **K_eff 和 BR 诊断指标有方法论可复用价值**：将 Kish design effect 引入 LLM 投票分析，为社区提供了量化 same-model 独立性的工具。\n6. **Case studies（Appendix G）提供机制性理解**：三个 discordant case 超越统计汇总数字。\n7. **诚实的负面结果报告**：未为\"正面故事\"隐瞒负面发现，学术诚信值得肯定。\n8. **Comprehensive appendix**：14 页附录含 prompt templates、pseudocode、ablation、error analysis，reproducibility 条件好。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, consensus AGREE] **Spearman ρ=1.0 (n=6) 被过度使用，统计基础不足以承受论证权重**\n- 6 个数据点中 4 个共享 DeBERTa verifier，违反 permutation test 的交换性假设，有效自由度仅 2-3。然而 \"strongly monotonic ρ=1.0, p=0.003\" 在论文中重复至少 7 次（Abstract, Introduction Contribution 2, Section 3.3, Section 6, Discussion×2, Conclusion）。这是论文从负面结果转向正面贡献的关键桥梁——如果统计基础不牢固，论文退化为纯粹的负面结果论文。\n- **建议**：(1) 降级为 \"consistent with a monotonic trend\"；(2) 减少重复至 ≤3 次；(3) 增加 non-DeBERTa verifier；(4) 添加讨论 shared-verifier 对 p 值有效性的影响。\n\n**N2** [critical, consensus AGREE] **中心 claim 强度超出统计证据——标题和 Abstract 需限定范围**\n- Abstract \"do not improve majority voting at any capability level\" 在 10/16 条件 underpowered（观测功效 <21%）的情况下是过强的否定命题。TOST 方法论本身是正确的（4 条件等价 + 2 条件负面 = 6/16 有实质证据），但措辞未反映 10/16 条件的 inconclusive 状态。同时标题未限定模型规模（仅测 7B-32B），而约束提取质量可能随规模提升。\n- **建议**：(1) Abstract 改为 \"we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two\"；(2) 标题加限定（如 \"at the 7B-32B Scale\"）。\n\n**N3** [critical, consensus AGREE] **TOST ±2pp 等价性 margin 缺乏 principled 论证**\n- 跨 39-86% SC baseline 使用固定绝对 margin 不合理（39% baseline 的 2pp ≈5% relative vs 86% baseline 的 2pp ≈2.3% relative）。Sensitivity analysis（±1pp → 0 等价, ±3pp → 10 等价）显示等价结论对 margin 高度敏感。Lakens (2017) 要求基于 SESOI 的领域论证，论文未提供。\n- **建议**：(1) 提供 margin 的 principled justification；(2) 考虑 relative margin（如 baseline 的 ±5%）；(3) 正文报告 sensitivity 结果。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, consensus AGREE] **Proposition 1 / Observation 2 伪形式化——empirical claim dressed as math**\n- \"Bound 1\" 中 \"≲\" 未定义，无证明推导；\"Observation 2\" 基于 n=6 经验观察但用了数学命题格式。建议改用 \"Empirical Finding\" 或 \"Observation\"，去除数学化包装。\n\n**W2** [warning, consensus AGREE] **DRC 评估不充分——不足以作为 Contribution 4**\n- 仅在 ProofWriter 上完整评估；τ=0.7 在 evaluation set 上选择（过拟合风险）；3 个 verifier 全是 encoder-only MNLI-finetuned；未与 multi-agent debate 等方法对比。建议降级为 proof-of-concept 或增加 cross-dataset validation。\n\n**W3** [warning, consensus AGREE] **Single-seed 变异性与统计可靠性问题叠加**\n- 4-seed 复现 Δ 从 +3.43 到 -0.49pp（range ≈4pp），完全覆盖 TOST ±2pp margin。多数条件 single-seed，Δ 可信度存疑。Single-seed + underpowered + margin-sensitive TOST 构成系统性可靠性风险。\n\n**W4** [warning, 分歧 — R2 critical / R1 rebut] **核心负面结果的增量新颖性定位需改善**\n- R2 认为 SCB 可从 Huang/Stechly/Wan/Amonkar/Chan 组合预测；R1 反驳称 formal channel (Z3) failure 是 genuine surprise——99% 约束语法合法但语义偏差，与 NL self-correction 失败是不同 failure mode。双方共识：论文应在 Introduction 中更早、更明确地建立 formal channel 的额外假设和区分。\n\n**W5** [warning, 分歧 — R2 critical / R1 rebut] **Independence-Accuracy Trade-off 与经典 ensemble dilemma 的区分**\n- R2 认为是 Krogh/Brown diversity-accuracy dilemma 的 CJT 语言重述；R1 认为 CJT 提供了 LLM-specific 量化工具（K_eff, BR, C_0）。双方共识：应明确声明贡献在于量化而非发现新 tradeoff。\n\n**W6** [warning, consensus partial] **BR 指标的循环论证倾向**\n- R1 指出 \"模型错时约束也错\" 是 self-extraction 的定义性结果。R2 反驳称 magnitude (4.97×) 和 per-condition variation 有价值。共识：应定位为 \"quantification of expected phenomenon\" 而非 \"discovery\"，减少 BR=4.97× 的重复频次。\n\n**W7** [warning, consensus partial] **术语品牌化过度——\"Independence Bottleneck\" 接近 rebranding**\n- R2 认为所有品牌化术语过多；R1 认为 \"Symbolic Mirage\"（有3个可测试预测）命名合理，但 \"Independence Bottleneck\" 确实是 Ladha (1992) correlated voting 的 rebranding。建议保留核心术语，降低次要术语的品牌化。\n\n**W8** [warning, R2 raised, R1 conditional agree] **Related Work 遗漏引用**\n- Byerly & Khashabi (2026 TACL) \"Self-Consistency Falls Short!\" 和 arxiv 2506.07962 \"Correlated Errors in Large Language Models\" 高度相关但未引用。Related Work 部分段落以 citation listing 为主，缺乏 critical discussion。\n\n**W9** [warning, R1 raised, R2 partial rebut] **27 策略计数膨胀 + 未尝试 trained extractor**\n- 含超参变体（T=0.3/0.5/0.7/1.0）和 n≤60 条件。R2 反驳称穷举论证仍成立。但双方同意 trained constraint extractor（如在 oracle annotations 上 SFT）是重要实验空白，应在 Discussion 中讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致 [AGREE]：\n\n1. ρ=1.0 (n=6) 被过度使用，需降级描述并减少重复 [N1]\n2. 标题/Abstract 需限定模型规模（7B-32B）[N2]\n3. Abstract 措辞 \"do not improve at any capability level\" 过强 [N2]\n4. TOST ±2pp margin 需 principled justification 和 sensitivity 分析 [N3]\n5. DRC 评估不足（τ 过拟合、范围窄）[W2]\n6. Single-seed 变异性构成系统性可靠性风险 [W3]\n7. Proposition/Bound 应降级为 Empirical Finding [W1]\n8. SCB 与 CoT confirmation bias 的区分应在 Introduction 前移 [W4]\n9. 应声明 Independence-Accuracy Trade-off 贡献在量化而非发现 [W5]\n\n---\n\n## Reviewer Divergence\n\n以下问题存在分歧（未完全调和但可记录）：\n\n1. **新颖性评价**（R1: 3.5 Excitement vs R2: 2.5 Excitement）\n   - R2：核心负面发现可从先验工作组合预测，增量有限\n   - R1：formal channel (Z3) failure 是 genuine surprise——与 NL self-correction 是不同 failure mode\n   - 调和方向：论文需更早、更清晰地建立 formal channel 的额外假设\n\n2. **BR 指标价值**（R1: tautological tendency vs R2: magnitude matters）\n   - 调和方向：定位为 quantification 而非 discovery\n\n3. **27 策略计数**（R1: 膨胀 vs R2: 穷举仍成立）\n   - 调和方向：区分 principled 和 exploratory，但补充 trained extractors 讨论\n\n---\n\n## Questions（需作者澄清）\n\n1. 用 relative TOST margin（如 baseline 的 ±5%）替代 absolute ±2pp，等价/underpowered/different 的分类如何变化？\n2. 是否考虑过 trained constraint extractor（如在 FOLIO/ProofWriter oracle annotations 上 SFT）？这是打破 self-extraction 瓶颈的最自然路径。\n3. 仅用 3 个独立 verifier（collapsing 4 DeBERTa pairs into 1）时，permutation test p 值是多少？\n4. 在 70B+ 模型上，BR 是否可能跨越 BR<1.0 阈值？论文数据显示 BR 随能力下降（4.97× → 3.93× → 2.88×），外推趋势是否有限？\n5. Process similarity 用 SBERT 替代 TF-IDF 是否改变 gap 估计？\n6. \"Symbolic Confirmation Bias\" 与 Wan et al. (2025) CoT confirmation bias 在机制上的本质区别是什么？\n\n---\n\n## Missing References\n\n1. **Byerly & Khashabi (2026, TACL)** \"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\" — SC 在 long-context 场景失败，互补分析\n2. **arxiv 2604.07650 (2026)** \"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles\" — LLM 独立性审计框架\n3. **arxiv 2506.07962 (2025)** \"Correlated Errors in Large Language Models\" — LLM 错误相关性分析\n4. **arxiv 2510.01499 (2025)** \"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information\" — 超越 majority voting 的聚合方法\n5. **arxiv 2501.19306 (2025)** \"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling\" — Self-verification 在 test-time scaling 中的应用\n\n注：#2 和 #4 可能在本文提交时尚未公开，需核实时间线。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 中 external_review 未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（4 warnings, 0 critical, 12 info）。主要发现：\n\n1. **[warning] 主文严重缺乏结果可视化**：~8.5 页主文仅含 1 个 figure（Figure 1 流程图）+ 4 个 table，没有任何结果可视化图。所有结果图（Figure 2-7）全部推至附录 page 23-24。对于实证分析为主的论文，审稿人不会翻到附录去找关键图表。\n2. **[warning] Figure 2（27 策略汇总 bar chart）应上提至主文**：这是全文最有冲击力的结果图，但在附录 p.23。建议放入 Section 5.5 或 Discussion。\n3. **[warning] Pages 3-5 连续无 display item**：page 3 纯文本（Related Work），page 4 有公式但无 display item，page 5 纯文本。Table 1 直到 page 6 才出现。\n4. **[warning] Pages 1-3 视觉锚点不足**：仅 page 2 有 Figure 1，page 1 和 page 3 纯文字。\n5. **[info] 附录 page 24 五张图挤在一页**：每张约 1/5 页高，标签在正常距离下可能难辨认。\n\n---\n\n## Overall Assessment\n\n### 评分：3.0 / 5（Findings）\n\n**置信度**：4/5（两位 Reviewer 仔细通读全文及全部附录，对统计方法和领域文献逐项核查）\n\n### 各维度评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n### 评分理由\n\n**支持 Conference (3.5-4.0) 的因素**：\n- 实验设计系统性在同类工作中无出其右\n- 统计方法论优秀（TOST + McNemar + Bootstrap + Power），在 NLP 社区少见\n- Oracle 控制实验干净隔离了 extraction 和 aggregation\n- K_eff, BR, C_0 三个诊断指标有方法论可复用价值\n- 负面结果的诚实报告有社区价值\n\n**拉低至 Findings (3.0) 的因素**：\n- **统计证据与 claim 强度的系统性不匹配**：ρ=1.0 (n=6) 过度使用、TOST margin 无 principled justification、single-seed 高变异、10/16 条件 underpowered——这些问题叠加形成系统性可靠性风险\n- **新颖性定位需改善**：formal channel failure 是一个值得报告的发现，但论文未在 Introduction 中及时建立与 NL self-correction 文献的清晰区分，导致贡献被低估\n- **标题/Abstract 未限定范围**：7B-32B 的结论被表述为无条件的否定命题\n- **DRC 作为唯一 constructive contribution 评估不足**\n- **主文缺少结果可视化**（所有关键图在附录）\n\n### 上调路径（→ 3.5 Borderline Conference）\n\n1. **N1**：降级 ρ=1.0 为趋势描述，减少重复，添加 shared-verifier 限制讨论\n2. **N2**：标题加限定词，Abstract 措辞校准\n3. **N3**：TOST margin 提供 justification + sensitivity 在正文报告\n4. **W4**：Introduction 中更早建立 formal channel distinction\n5. **W2**：DRC 降级为 proof-of-concept 或增加 cross-dataset validation\n6. **VL**：Figure 2 上提至主文\n\n如果以上 6 项全部解决，论文可达到 3.5 (Borderline Conference)。Excitement 的上限受限于负面结果本身的天然约束——即使定位完善，概念新颖性不超过 3.5。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过于密集：10 行含 15+ 数字/统计量，可读性低\n- \"at any capacity level\" 需加 \"tested (7B-32B)\"\n- 关键数字（BR=4.97×, ρ=1.0, +29.90pp, 83.3%）在全文各处重复，冗余感强\n\n### Introduction\n- Narrative flow 清晰，从 SC plateau → CJT independence → SICA → failure → escape\n- 但 formal channel (Z3) vs NL self-correction 的区分出现太晚（需从 Related Work 末段前移）\n- 四个 contributions 中 Contribution 2（Independence-Accuracy Trade-off）应声明为量化而非发现\n\n### Related Work\n- 与 SatLM 的对比已有（\"provides a natural control\"），但部分段落以 citation listing 为主\n- 遗漏 Byerly & Khashabi (2026 TACL) 和 arxiv 2506.07962\n- SCB vs CoT confirmation bias 区分在此段末尾，建议前移\n\n### Method\n- Eq.(1)-(5) 形式化完备，Algorithm 1-2 清晰\n- Bound 1 \"≲\" 未定义，应降级为 Empirical Finding\n- C_0 diagnostic 简洁有用\n\n### Experiments\n- Table 1 排列合理（按 SC baseline 排序，分 regime）\n- 多数条件 single-seed，4-seed 复现显示高变异\n- TOST margin sensitivity 应在正文报告\n\n### Analysis\n- K_eff, BR, process similarity 三层诊断结构完整\n- BR 的 tautological tendency 应在 Discussion 中承认\n\n### Cross-Architecture\n- NLI escape 仅在 NLI-shaped tasks（ProofWriter, FOLIO 边缘）有效\n- ρ=1.0 需降级，添加 shared-verifier caveat\n- DRC τ 需 held-out validation\n\n### Discussion\n- 涵盖了 self-verification 泛化、test-time scaling、trained reasoning 三个维度\n- 但 ensemble diversity-accuracy 关系的讨论应更明确声明贡献定位\n\n### Limitations\n- 覆盖面适当（规模、语言、功效、成本），篇幅合理（~2/3 栏）\n- 建议添加 trained extractor 作为未探索方向\n\n### Format Compliance\n- 页数合规：正文 ~8 页 + Limitations + References 2 页 + Appendix 14 页\n- 使用 \\usepackage[review]{acl}，double-blind（author = Anonymous）\n- 无自引暴露身份\n- 引用格式完整，60 条 bib 条目，0 orphan，0 missing key\n",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 11 审稿报告（Fresh Review）\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验可靠性; R2: 新颖性+完整性+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享 → 逐条 AGREE/REBUT → 收敛（1轮达成）\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束、通过加权部分 MAX-SAT 聚合答案。在 6 个开源 LLM（7B-32B）、3 个逻辑推理数据集、3,000+ 条件评估上，作者发现自提取符号约束在任何已测试的模型能力水平上都无法改进 Self-Consistency。论文识别了\"Symbolic Confirmation Bias\"（BR=4.97×）和 process-level independence bottleneck（CoT cosine similarity 0.69 >> answer κ 0.46），证明 27 种 same-model remediation 策略全部失败。Oracle 控制实验确认聚合机制本身有效（+29.90pp, +14.22pp），瓶颈在 self-extraction 质量。Cross-architecture NLI 验证在 verifier 能力超过 generator 时产生显著增益（Mistral-7B +6.67pp, p<0.001），DRC 路由方法在 39% 成本下恢复 90% 增益。\n\n---\n\n## Strengths\n\n1. **实验设计的系统性前所未有**：6 models × 3 datasets × 27 strategies × oracle controls × cross-arch escape × 4-seed replication，覆盖面远超同类工作。穷举式搜索有效排除了\"只是没找到正确配置\"的反驳。\n2. **统计方法论在 NLP 实证研究中属上乘**：McNemar + BH FDR + TOST 等价性检验 + Bootstrap CI + Power analysis 构成完整统计推断链。TOST 的使用（区分\"无效果证据\"和\"证据不足\"）值得肯定。\n3. **Oracle 控制实验设计精妙**：FOLIO gold annotations + ProofWriter DSL 作为 oracle constraints，干净隔离了 extraction quality 和 aggregation mechanism，是论文最强的方法论贡献。\n4. **\"Symbolic Mirage\" 概念框架完整**：包含三个可测试预测（BR>1 跨架构、same-model 无法突破 BR<1、only external verification escapes），全部被数据确认。\n5. **K_eff 和 BR 诊断指标有方法论可复用价值**：将 Kish design effect 引入 LLM 投票分析，为社区提供了量化 same-model 独立性的工具。\n6. **Case studies（Appendix G）提供机制性理解**：三个 discordant case 超越统计汇总数字。\n7. **诚实的负面结果报告**：未为\"正面故事\"隐瞒负面发现，学术诚信值得肯定。\n8. **Comprehensive appendix**：14 页附录含 prompt templates、pseudocode、ablation、error analysis，reproducibility 条件好。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical, consensus AGREE] **Spearman ρ=1.0 (n=6) 被过度使用，统计基础不足以承受论证权重**\n- 6 个数据点中 4 个共享 DeBERTa verifier，违反 permutation test 的交换性假设，有效自由度仅 2-3。然而 \"strongly monotonic ρ=1.0, p=0.003\" 在论文中重复至少 7 次（Abstract, Introduction Contribution 2, Section 3.3, Section 6, Discussion×2, Conclusion）。这是论文从负面结果转向正面贡献的关键桥梁——如果统计基础不牢固，论文退化为纯粹的负面结果论文。\n- **建议**：(1) 降级为 \"consistent with a monotonic trend\"；(2) 减少重复至 ≤3 次；(3) 增加 non-DeBERTa verifier；(4) 添加讨论 shared-verifier 对 p 值有效性的影响。\n\n**N2** [critical, consensus AGREE] **中心 claim 强度超出统计证据——标题和 Abstract 需限定范围**\n- Abstract \"do not improve majority voting at any capability level\" 在 10/16 条件 underpowered（观测功效 <21%）的情况下是过强的否定命题。TOST 方法论本身是正确的（4 条件等价 + 2 条件负面 = 6/16 有实质证据），但措辞未反映 10/16 条件的 inconclusive 状态。同时标题未限定模型规模（仅测 7B-32B），而约束提取质量可能随规模提升。\n- **建议**：(1) Abstract 改为 \"we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two\"；(2) 标题加限定（如 \"at the 7B-32B Scale\"）。\n\n**N3** [critical, consensus AGREE] **TOST ±2pp 等价性 margin 缺乏 principled 论证**\n- 跨 39-86% SC baseline 使用固定绝对 margin 不合理（39% baseline 的 2pp ≈5% relative vs 86% baseline 的 2pp ≈2.3% relative）。Sensitivity analysis（±1pp → 0 等价, ±3pp → 10 等价）显示等价结论对 margin 高度敏感。Lakens (2017) 要求基于 SESOI 的领域论证，论文未提供。\n- **建议**：(1) 提供 margin 的 principled justification；(2) 考虑 relative margin（如 baseline 的 ±5%）；(3) 正文报告 sensitivity 结果。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [warning, consensus AGREE] **Proposition 1 / Observation 2 伪形式化——empirical claim dressed as math**\n- \"Bound 1\" 中 \"≲\" 未定义，无证明推导；\"Observation 2\" 基于 n=6 经验观察但用了数学命题格式。建议改用 \"Empirical Finding\" 或 \"Observation\"，去除数学化包装。\n\n**W2** [warning, consensus AGREE] **DRC 评估不充分——不足以作为 Contribution 4**\n- 仅在 ProofWriter 上完整评估；τ=0.7 在 evaluation set 上选择（过拟合风险）；3 个 verifier 全是 encoder-only MNLI-finetuned；未与 multi-agent debate 等方法对比。建议降级为 proof-of-concept 或增加 cross-dataset validation。\n\n**W3** [warning, consensus AGREE] **Single-seed 变异性与统计可靠性问题叠加**\n- 4-seed 复现 Δ 从 +3.43 到 -0.49pp（range ≈4pp），完全覆盖 TOST ±2pp margin。多数条件 single-seed，Δ 可信度存疑。Single-seed + underpowered + margin-sensitive TOST 构成系统性可靠性风险。\n\n**W4** [warning, 分歧 — R2 critical / R1 rebut] **核心负面结果的增量新颖性定位需改善**\n- R2 认为 SCB 可从 Huang/Stechly/Wan/Amonkar/Chan 组合预测；R1 反驳称 formal channel (Z3) failure 是 genuine surprise——99% 约束语法合法但语义偏差，与 NL self-correction 失败是不同 failure mode。双方共识：论文应在 Introduction 中更早、更明确地建立 formal channel 的额外假设和区分。\n\n**W5** [warning, 分歧 — R2 critical / R1 rebut] **Independence-Accuracy Trade-off 与经典 ensemble dilemma 的区分**\n- R2 认为是 Krogh/Brown diversity-accuracy dilemma 的 CJT 语言重述；R1 认为 CJT 提供了 LLM-specific 量化工具（K_eff, BR, C_0）。双方共识：应明确声明贡献在于量化而非发现新 tradeoff。\n\n**W6** [warning, consensus partial] **BR 指标的循环论证倾向**\n- R1 指出 \"模型错时约束也错\" 是 self-extraction 的定义性结果。R2 反驳称 magnitude (4.97×) 和 per-condition variation 有价值。共识：应定位为 \"quantification of expected phenomenon\" 而非 \"discovery\"，减少 BR=4.97× 的重复频次。\n\n**W7** [warning, consensus partial] **术语品牌化过度——\"Independence Bottleneck\" 接近 rebranding**\n- R2 认为所有品牌化术语过多；R1 认为 \"Symbolic Mirage\"（有3个可测试预测）命名合理，但 \"Independence Bottleneck\" 确实是 Ladha (1992) correlated voting 的 rebranding。建议保留核心术语，降低次要术语的品牌化。\n\n**W8** [warning, R2 raised, R1 conditional agree] **Related Work 遗漏引用**\n- Byerly & Khashabi (2026 TACL) \"Self-Consistency Falls Short!\" 和 arxiv 2506.07962 \"Correlated Errors in Large Language Models\" 高度相关但未引用。Related Work 部分段落以 citation listing 为主，缺乏 critical discussion。\n\n**W9** [warning, R1 raised, R2 partial rebut] **27 策略计数膨胀 + 未尝试 trained extractor**\n- 含超参变体（T=0.3/0.5/0.7/1.0）和 n≤60 条件。R2 反驳称穷举论证仍成立。但双方同意 trained constraint extractor（如在 oracle annotations 上 SFT）是重要实验空白，应在 Discussion 中讨论。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致 [AGREE]：\n\n1. ρ=1.0 (n=6) 被过度使用，需降级描述并减少重复 [N1]\n2. 标题/Abstract 需限定模型规模（7B-32B）[N2]\n3. Abstract 措辞 \"do not improve at any capability level\" 过强 [N2]\n4. TOST ±2pp margin 需 principled justification 和 sensitivity 分析 [N3]\n5. DRC 评估不足（τ 过拟合、范围窄）[W2]\n6. Single-seed 变异性构成系统性可靠性风险 [W3]\n7. Proposition/Bound 应降级为 Empirical Finding [W1]\n8. SCB 与 CoT confirmation bias 的区分应在 Introduction 前移 [W4]\n9. 应声明 Independence-Accuracy Trade-off 贡献在量化而非发现 [W5]\n\n---\n\n## Reviewer Divergence\n\n以下问题存在分歧（未完全调和但可记录）：\n\n1. **新颖性评价**（R1: 3.5 Excitement vs R2: 2.5 Excitement）\n   - R2：核心负面发现可从先验工作组合预测，增量有限\n   - R1：formal channel (Z3) failure 是 genuine surprise——与 NL self-correction 是不同 failure mode\n   - 调和方向：论文需更早、更清晰地建立 formal channel 的额外假设\n\n2. **BR 指标价值**（R1: tautological tendency vs R2: magnitude matters）\n   - 调和方向：定位为 quantification 而非 discovery\n\n3. **27 策略计数**（R1: 膨胀 vs R2: 穷举仍成立）\n   - 调和方向：区分 principled 和 exploratory，但补充 trained extractors 讨论\n\n---\n\n## Questions（需作者澄清）\n\n1. 用 relative TOST margin（如 baseline 的 ±5%）替代 absolute ±2pp，等价/underpowered/different 的分类如何变化？\n2. 是否考虑过 trained constraint extractor（如在 FOLIO/ProofWriter oracle annotations 上 SFT）？这是打破 self-extraction 瓶颈的最自然路径。\n3. 仅用 3 个独立 verifier（collapsing 4 DeBERTa pairs into 1）时，permutation test p 值是多少？\n4. 在 70B+ 模型上，BR 是否可能跨越 BR<1.0 阈值？论文数据显示 BR 随能力下降（4.97× → 3.93× → 2.88×），外推趋势是否有限？\n5. Process similarity 用 SBERT 替代 TF-IDF 是否改变 gap 估计？\n6. \"Symbolic Confirmation Bias\" 与 Wan et al. (2025) CoT confirmation bias 在机制上的本质区别是什么？\n\n---\n\n## Missing References\n\n1. **Byerly & Khashabi (2026, TACL)** \"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\" — SC 在 long-context 场景失败，互补分析\n2. **arxiv 2604.07650 (2026)** \"How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles\" — LLM 独立性审计框架\n3. **arxiv 2506.07962 (2025)** \"Correlated Errors in Large Language Models\" — LLM 错误相关性分析\n4. **arxiv 2510.01499 (2025)** \"Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information\" — 超越 majority voting 的聚合方法\n5. **arxiv 2501.19306 (2025)** \"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling\" — Self-verification 在 test-time scaling 中的应用\n\n注：#2 和 #4 可能在本文提交时尚未公开，需核实时间线。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（项目 config 中 external_review 未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（4 warnings, 0 critical, 12 info）。主要发现：\n\n1. **[warning] 主文严重缺乏结果可视化**：~8.5 页主文仅含 1 个 figure（Figure 1 流程图）+ 4 个 table，没有任何结果可视化图。所有结果图（Figure 2-7）全部推至附录 page 23-24。对于实证分析为主的论文，审稿人不会翻到附录去找关键图表。\n2. **[warning] Figure 2（27 策略汇总 bar chart）应上提至主文**：这是全文最有冲击力的结果图，但在附录 p.23。建议放入 Section 5.5 或 Discussion。\n3. **[warning] Pages 3-5 连续无 display item**：page 3 纯文本（Related Work），page 4 有公式但无 display item，page 5 纯文本。Table 1 直到 page 6 才出现。\n4. **[warning] Pages 1-3 视觉锚点不足**：仅 page 2 有 Figure 1，page 1 和 page 3 纯文字。\n5. **[info] 附录 page 24 五张图挤在一页**：每张约 1/5 页高，标签在正常距离下可能难辨认。\n\n---\n\n## Overall Assessment\n\n### 评分：3.0 / 5（Findings）\n\n**置信度**：4/5（两位 Reviewer 仔细通读全文及全部附录，对统计方法和领域文献逐项核查）\n\n### 各维度评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n\n### 评分理由\n\n**支持 Conference (3.5-4.0) 的因素**：\n- 实验设计系统性在同类工作中无出其右\n- 统计方法论优秀（TOST + McNemar + Bootstrap + Power），在 NLP 社区少见\n- Oracle 控制实验干净隔离了 extraction 和 aggregation\n- K_eff, BR, C_0 三个诊断指标有方法论可复用价值\n- 负面结果的诚实报告有社区价值\n\n**拉低至 Findings (3.0) 的因素**：\n- **统计证据与 claim 强度的系统性不匹配**：ρ=1.0 (n=6) 过度使用、TOST margin 无 principled justification、single-seed 高变异、10/16 条件 underpowered——这些问题叠加形成系统性可靠性风险\n- **新颖性定位需改善**：formal channel failure 是一个值得报告的发现，但论文未在 Introduction 中及时建立与 NL self-correction 文献的清晰区分，导致贡献被低估\n- **标题/Abstract 未限定范围**：7B-32B 的结论被表述为无条件的否定命题\n- **DRC 作为唯一 constructive contribution 评估不足**\n- **主文缺少结果可视化**（所有关键图在附录）\n\n### 上调路径（→ 3.5 Borderline Conference）\n\n1. **N1**：降级 ρ=1.0 为趋势描述，减少重复，添加 shared-verifier 限制讨论\n2. **N2**：标题加限定词，Abstract 措辞校准\n3. **N3**：TOST margin 提供 justification + sensitivity 在正文报告\n4. **W4**：Introduction 中更早建立 formal channel distinction\n5. **W2**：DRC 降级为 proof-of-concept 或增加 cross-dataset validation\n6. **VL**：Figure 2 上提至主文\n\n如果以上 6 项全部解决，论文可达到 3.5 (Borderline Conference)。Excitement 的上限受限于负面结果本身的天然约束——即使定位完善，概念新颖性不超过 3.5。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 过于密集：10 行含 15+ 数字/统计量，可读性低\n- \"at any capacity level\" 需加 \"tested (7B-32B)\"\n- 关键数字（BR=4.97×, ρ=1.0, +29.90pp, 83.3%）在全文各处重复，冗余感强\n\n### Introduction\n- Narrative flow 清晰，从 SC plateau → CJT independence → SICA → failure → escape\n- 但 formal channel (Z3) vs NL self-correction 的区分出现太晚（需从 Related Work 末段前移）\n- 四个 contributions 中 Contribution 2（Independence-Accuracy Trade-off）应声明为量化而非发现\n\n### Related Work\n- 与 SatLM 的对比已有（\"provides a natural control\"），但部分段落以 citation listing 为主\n- 遗漏 Byerly & Khashabi (2026 TACL) 和 arxiv 2506.07962\n- SCB vs CoT confirmation bias 区分在此段末尾，建议前移\n\n### Method\n- Eq.(1)-(5) 形式化完备，Algorithm 1-2 清晰\n- Bound 1 \"≲\" 未定义，应降级为 Empirical Finding\n- C_0 diagnostic 简洁有用\n\n### Experiments\n- Table 1 排列合理（按 SC baseline 排序，分 regime）\n- 多数条件 single-seed，4-seed 复现显示高变异\n- TOST margin sensitivity 应在正文报告\n\n### Analysis\n- K_eff, BR, process similarity 三层诊断结构完整\n- BR 的 tautological tendency 应在 Discussion 中承认\n\n### Cross-Architecture\n- NLI escape 仅在 NLI-shaped tasks（ProofWriter, FOLIO 边缘）有效\n- ρ=1.0 需降级，添加 shared-verifier caveat\n- DRC τ 需 held-out validation\n\n### Discussion\n- 涵盖了 self-verification 泛化、test-time scaling、trained reasoning 三个维度\n- 但 ensemble diversity-accuracy 关系的讨论应更明确声明贡献定位\n\n### Limitations\n- 覆盖面适当（规模、语言、功效、成本），篇幅合理（~2/3 栏）\n- 建议添加 trained extractor 作为未探索方向\n\n### Format Compliance\n- 页数合规：正文 ~8 页 + Limitations + References 2 页 + Appendix 14 页\n- 使用 \\usepackage[review]{acl}，double-blind（author = Anonymous）\n- 无自引暴露身份\n- 引用格式完整，60 条 bib 条目，0 orphan，0 missing key\n",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-21T08:03:15.318159+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4725
}
```

</details>

---


### Assistant

_source line 1120 · 2026-05-21T08:03:26.163612+00:00_

审稿报告已投递。

**Round 11 审稿完成**：

- **Overall**: 3.0 / 5（Findings）
- **Soundness**: 3.5 | **Excitement**: 3.0 | **Reproducibility**: 4.0
- **3 个 Must-Fix**：ρ=1.0 (n=6) 过度使用、claim 与功效不匹配 + 标题/Abstract 未限定范围、TOST margin 无 principled 论证
- **9 个 Should-Fix**：Proposition 伪形式化、DRC 评估不足、single-seed 变异性、新颖性定位、Independence-Accuracy 贡献声明、BR 循环论证、术语品牌化、遗漏引用、27策略计数
- **明确上调路径**：6 项修复可达 3.5（Borderline Conference）

Issue tracker 已同步更新（新增 R11-N1~N3, R11-W1~W9, R11-VL1），历史 in_progress 问题已追加本轮 mentions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 1121 · 2026-05-21T08:03:28.981981+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心共识：R1 的统计方法论批评大多有效——ρ=1.0 (n=6) 过度使用、TOST margin 论证不足、single-seed 变异性、Abstract 措辞过强。我在 N2（TOST 方法论本身是正确的）、W3（穷举搜索论证仍成立）、W6（BR 量化价值超越方向性预测）上提供了部分反驳。两位 Reviewer 一致认为论文的核心风险是 **claim 强度超出统计证据支撑范围**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1122 · 2026-05-21T08:03:45.103132+00:00_

Round 11 审稿已完成并投递。

**最终评分：3.0 / 5（Findings）**

**核心结论**：方法论扎实（TOST + Oracle controls + 27 策略穷举）、实验覆盖面在同类工作中无出其右，但 claim 强度系统性超出统计证据支撑范围。三个 Must-Fix：(1) ρ=1.0 (n=6) 过度使用，(2) 标题/Abstract 未限定范围且措辞过强，(3) TOST margin 无 principled justification。明确的上调路径（→3.5）：校准 claim 强度 + 改善新颖性定位 + Figure 2 上提主文。

审稿报告已通过 `submit_review_report_to_research_director` 投递，Issue Tracker 已同步更新（3 new critical, 7 new warning, 多项历史 issue 追加 R11 mentions）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 1123 · 2026-05-21T08:04:04.997833+00:00_

[飞书用户 曹晓玉 (ou_fe906a2a0b37a0531edeaa0539755598)]: hi

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "feishu:oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

---


### Assistant

_source line 1124 · 2026-05-21T08:04:17.684268+00:00_

圆桌审稿已完成，报告已投递给 Research Director。

**本轮结果**：Overall 3.0 / 5（Findings）

核心问题：
1. **ρ=1.0 (n=6) 过度使用** — 4/6 共享 DeBERTa verifier，有效自由度不足，但在论文中重复 7 次
2. **claim 强度超出统计证据** — 10/16 条件 underpowered，标题/Abstract 未限定模型规模（7B-32B）
3. **TOST ±2pp margin 缺 principled justification** — ±1pp→0 等价，±3pp→10 等价，高度敏感

上调至 3.5 的路径已在报告中列出（6 项修改）。报告已投递，后续由 Research Director 处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 78

## Round 78

156 recorded events


### User

_source line 1125 · 2026-05-22T00:55:59.116577+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1126 · 2026-05-22T00:56:07.969787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-22T00:56:08.021078+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-22T00:56:14.384070+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-22T00:56:14.434805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-22T00:56:16.644701+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-22T00:56:16.695496+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-22T00:56:20.362240+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-22T00:56:20.362648+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-22T00:56:31.110039+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-22T00:56:31.361418+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-22T00:56:31.613409+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (159 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-d126-70b-sica | Symbolic confirmation bias persists at 72B scale: Qwen2.5-72B self-extracted constraints will show BR > 1 and κ ≥ 0.40, with SICA ≈ SC (no significant improvement), demonstrating that the independence bottleneck is scale-invariant beyond the 7B-14B range tested so far. | — | — | — |\n\n## 待处理\n- exp-folio-2x2-crossmodel（准备中）\n- exp-013-constraint-ablation: MaxSAT satisfiability checking contributes minimal accuracy gains over naive constraint counting, because extracted constraints are too homogeneous (trace co-sourcing) to provide discriminative satisfiability signals. If SICA-MaxSAT ≈ SICA-count-only, the SAT solver is not the bottleneck — constraint quality is.（准备中）\n- exp-d135-frontier-scb: 2026 frontier closed-source models (Claude/GPT/Gemini via OpenRouter) also exhibit SCB: self-extracted constraints will show BR≥2× with SICA≈SC, extending the scale-invariance finding from open-source 7B-72B to frontier closed-source models.（准备中）\n- exp-d126-r1-distill-sica: Reasoning-distilled model (DeepSeek-R1-Distill-LLaMA-8B) does not escape SCB: self-extracted constraints will show BR≥2× and SICA≈SC, dem
…[truncated 1732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 503
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-22T00:56:31.664606+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/memory.md\", \"content\": \"# Memory — symb_invariant_consensus\\n\\n## 项目核心发现\\n\\n### Regime-Dependent Capability Trap\\n- SICA 在 SC 准确率 50-60% 区间（Mistral-7B）可能有效，但不稳定\\n- SC > 75%（Qwen2.5-14B, Qwen3-14B）时 SICA 几乎无效或负向\\n- Oracle FOL (exp-031) delta=+14.22pp 证明上限存在，但 LLM extraction 质量是瓶颈\\n\\n### D080 全方向探索（2026-05-20 完成，12方向 8 negative / 3 positive-informational）\\n\\n**攻击 independence bottleneck 的全部路径均失败：**\\n\\n| 方向 | 类别 | 结果 | 核心发现 |\\n|------|------|------|----------|\\n| Wild1 MAX-UNSAT | 聚合规则 | ❌ | 排除约束太少(1.3/题), MIN-UNSAT Δ=-6.5pp |\\n| Wild6 κ-aware SC | 投票加权 | ❌ | accuracy与agreement单调递增, SC已最优 |\\n| Wild2 ASCII pad | 表面扰动 | ❌ | κ不变, 模型偏差非表面驱动 |\\n| Wild3 Perturbation | 语义扰动 | ❌ | κ反而上升, 变量重命名无效 |\\n| Wild4 Process-κ | 过程分析 | ❌ | 过程cos=0.69, 与答案不相关(r=-0.06, p=0.36) |\\n| DirA PROVE | 代码验证 | ❌ | 代码生成率15.2%, 结论性准确率50%(随机) |\\n| DirB DeepConf | 置信过滤 | ❌ | logprob与正确性无关(-0.135 vs -0.141) |\\n| DirD CEGIS | 迭代约束 | ❌ | R1 +2.4pp后饱和, 无迭代改善 |\\n| DirE Abstention | 选择性弃权 | ⚡ | AUROC=0.673, 80%cov +4.4pp |\\n| Cross-model κ | κ降低 | ✅ | κ_cross=0.422<κ_within=0.532, 但无accuracy增益 |\\n| Confirmation Bias | 因果分析 | ✅ | bias ratio 4.97x, 83.3%约束指向错误答案 |\\n\\n**关键教训：**\\n- **Logprob 不是质量信号**: Mistral-7B 对正确/错误答案同样过度自信, logprob 分布极度压缩(median=-0.06)\\n- **PROVE 需要强模型**: 7B 级模型无法为自然语言逻辑问题生成有效 verify() 函数, 这是能力门槛问题\\n- **CEGIS 单轮就饱和**: counterexample 引导的迭代优化在第一轮后即无新信息, 因为模型在 R1 就倾向于生成最容易的修补\\n- **Process similarity ≠ answer agreement**: 推理文本 cosine=0.69 高度相似但与答案一致性无统计相关, 说明 traces 在\\\"表面\\\"雷同但在推理关键步骤上分歧\\n- **Confirmation Bias 是因果解释**: 4.97x bias ratio 量化了为什么 self-extracted constraints 无法纠正多数票——它们本身就是多数票的产物\\n\\n### Wave 3 补充结果（2026-05-20）\\n\\n| 方向 | 结果 | 核心发现 |\\n|------|------|----------|\\n| I (Z3 Filter) | ❌ | filter precision 49.12%，Z3 SAT/UNSAT 无判别力 |\\n| J (Bootstrap Gold) | ❌ | R1 +2.45pp 后振荡，迭代无改善 |\\n| K (Minority Report) | ❌ | c
…[truncated 7132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-22T00:56:39.765209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-22T00:56:40.218090+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Do Not Improve LLM Reasoning from 7B to Frontier Scale}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\input{conclusion}
75	
76	\section*{Limitations}
77	\input{limitations_content}
78	
79	\bibliography{references}
80	
81
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-22T00:56:40.218660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-22T00:56:40.871688+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-22T00:56:40.922432+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f3_entropy_delta.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f3_entropy_delta.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f3_k_sensitivity.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f2_regime_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f2_regime_scatter.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/gen_f6_kappa_accuracy_scatter.py
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f6_kappa_accuracy_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/f6_kappa_accuracy_scatter.png
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/fig3_process_kappa_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/fig_app_interventions_summary.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/v8_outline_drafts.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/v9_aggregation_ceiling.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/gen_capability_gap_scatter.py
/home/ubuntu/.agent-ml-research-idea_
…[truncated 5137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-22T00:56:47.507345+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

The search results don't contain a specific EMNLP 2026 main conference call for papers. Ho
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7288
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-22T00:56:57.060804+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1145 · 2026-05-22T00:56:58.116245+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-22T00:56:58.518550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-22T00:56:58.519096+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B, from Mistral-7B at 54\% SC to Qwen3-14B thinking mode at 86\% SC) and five frontier models (gpt-4o through Gemini-2.5-Pro), on three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find no evidence of improvement, with equivalence established in four conditions, significant degradation in two (both in the lowest-accuracy regime), and ten conditions remaining underpowered (none of sixteen non-degenerate conditions shows a significant positive effect after FDR control; Benjamini--Hochberg, $m{=}16$).
4	We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
5	Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.46$), indicating that traces share reasoning processes even when they diverge on answers.
6	Twenty-seven same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off from 7B to frontier scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$); same-model self-extraction
…[truncated 570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-22T00:56:58.871247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-22T00:56:58.923219+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ that reveals near-deterministic voting dynamic
…[truncated 6502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1150 · 2026-05-22T00:57:02.196657+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit format requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"}]

Based on the search results, here is the information about EMNLP 2026 submission requirements:

## Submission Deadline

The ARR submission deadline is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format Requirements

EMNLP uses the standard ACL s
…[truncated 447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5135
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-22T00:57:03.725905+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author instructions page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"}]

I found the search results for ACL Rolling Review 2026 submission guidelines. Here are the key findings regarding submission guidelines, author instructions, and page limits:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. For short papers, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Limit
…[truncated 752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5609
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-22T00:57:11.710658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-22T00:57:12.213486+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early; \citet{byerly2026selfconsistency} further analyze SC's limitations in mathematical reasoning. Alternative aggregation strategies beyond majority voting \citep{ai2025beyondmajority} have been proposed but do not address the underlying correlation problem. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	We distinguish three paradigms. \emph{Specification-generation} (Logic-LM \citep{pan2023logiclm}, LINC \citep{olausson2023linc}, SatLM \citep{ye2024satlm}) translates problem descriptions into formal specifications before any answer is generated; LINC documents ${\sim}$40\% translation errors even at this level. \emph{Program-generation} \citep{gao2023pal,chen2023program,lyu2023faithful} produces executable code from problem statements. Both paradigms access the problem before generating candidate answers. \emph{Trace-extraction} (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). SatLM provides a natural control: it succeeds because problem-level formalization precedes answer generation, whereas trace-level extraction cannot avoid contamination (\S\ref{sec:mirage}). Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logic
…[truncated 3211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-22T00:57:12.213843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-22T00:57:12.704195+00:00_

1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. $K_{\text{eff}}$ should be interpreted as an ordinal diagnostic---ranking which conditions have genuine vote diversity---rather than as a literal effective sample size. Fleiss' $\kappa$ is a chance-corrected agreement measure, not identical to the ICC ($\rho$) in \citeauthor{kish1965survey}'s (\citeyear{kish1965survey}) original formula; we validated their monotonic relationship empirically (mean pairwise $r = 0.625$ across model families). This independence limitation motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at 
…[truncated 5569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 490
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-22T00:57:12.704682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-22T00:57:13.107518+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). Frontier extension (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro) evaluates SCB universality (Table~\ref{tab:frontier-scb}).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions (sorted by SC). No non-degenerate condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; $\dagger$\,$n < 100$; \textbf{bold}: $p < 0.05$; {*}\,unco
…[truncated 4562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-22T00:57:13.107953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-22T00:57:13.158530+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	We test the three predictions of the confirmation bias hypothesis (\S\ref{sec:mirage}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	\looseness=-1 Table~\ref{tab:independence} (Appendix) reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. Across four Mistral-7B seeds, $\kappa \in [0.41, 0.51]$ yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp, indicating seed-level constraint quality matters beyond independence. Positive $\Delta$ requires both sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ degrades). All four model families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
10	
11	
12	\subsection{Symbolic Confirmation Bias}
13	\label{sec:confirmation-bias}
14	
15	\looseness=-1 Self-extracted constraints systematically confirm the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, confirming degeneration (Eq.~\ref{eq:degenerate}).
16	
17	\looseness=-1 Bias generalizes across scale: $4.97\times$ [3.98, 6.37] (Mistral, 12-trace), $3.93\times$ [2.44, 7.11] (Qwen-14B, 12-trace), $2.88\times$ (LLaMA, 4-trace$^{\dag}$), all $> 1.0$ (95\% bootstrap CIs for Mistral/Qwen; Table~\ref{tab:cross-model-bias}; weighted BRs in Appendix~\ref{app:cross-model-bias}). SCB persists across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}). Constraints use trace-specific variables (56.4\% zero cross-answer overlap), collapsing aggregation to majority voting.
18	
19	\looseness=-1 Two controls rule out answer leakage. First, BR is uniform across earl
…[truncated 5036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-22T00:57:17.478264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-22T00:57:17.832180+00:00_

1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	\looseness=-1 We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), whose (premise, conclusion) structure suits NLI classification.
7	
8	\paragraph{Main result.}
9	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo mode yields $+0.49$\,pp at $w{=}1$ and $+2.94$\,pp at $w{=}3$ (both n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.112$; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). We report $w{=}3$ as primary. After BH correction ($m{=}12$), Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$) remain significant; all other conditions are non-significant.
10	
11	\paragraph{Why it works.}
12	\looseness=-1 Three conditions jointly enable the escape: (i)~\emph{structural independence}---encoder-only DeBERTa and decoder-only Mistral share no architecture or training data (\S\ref{sec:mirage}); (ii)~\emph{positive capability gap}---verifier standalone accuracy exceeds generator SC (Finding~2); (iii)~\emph{task-verifier alignment}---NLI classification naturally matches premise-conclusion structure. Per-label complementarity: NLI excels on \textsc{False} (71.43\% vs.\ 38.10\%), SC dominates \textsc{Unknown} (68.12\% vs.\ 18.84\%). All thr
…[truncated 2463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-22T00:57:17.882958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-22T00:57:18.385659+00:00_

1	\vspace{-1mm}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Self-verification and BR magnitude.}
6	\looseness=-1 Our bias ratio ($1.66$--$4.97\times$ across nine models from 7B to frontier; Table~\ref{tab:frontier-scb}) quantifies why self-correction fails without external feedback \citep{huang2024selfcorrect, stechly2025selfverification, chen2025sets}: extraction and generation share distributional biases, with nearly 5:1 on incorrect problems. Cross-model extraction gain requires both diverse traces (low $\kappa_{\text{proc}}$) and substantial self-bias (high BR); neither alone suffices (Table~\ref{tab:process-gradient}). Any self-verification pipeline deriving criteria from the same model faces this bottleneck.
7	
8	\paragraph{Test-time scaling and practitioner implications.}
9	\looseness=-1 $K_{\text{eff}} = 1.20$--$3.62$ for nominal $K = 12$ means sampling beyond a dozen traces yields diminishing independent information; the pattern intensifies with capability (Qwen3 thinking: $\kappa = 0.91$, $K_{\text{eff}} = 1.09$), creating a scaling paradox for o1/R1-style models \citep{guo2025deepseekr1}. All non-destructive interventions cluster at $\kappa \geq 0.40$ \citep{krogh1994neural}; Debate reaches $\kappa = 0.15$ but collapses accuracy ($-18.6$\,pp). Cross-architecture escape succeeds ($p = 0.003$) because encoder-only and decoder-only models have structurally different error profiles. Two diagnostics predict failure: $C_0 < 5\%$ means SICA reduces to SC; SC $\leq 40\%$ risks error amplification ($-2.83$\,pp). For intermediate-SC models, gain tracks the capability gap monotonically ($p = 0.003$); the bottleneck is extraction quality, as oracle constraints succeed ($+29.90$\,pp, $+14.22$\,pp).
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-22T00:57:18.386080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-22T00:57:18.838216+00:00_

1	\vspace{-2mm}
2	\section{Conclusion}\label{sec:conclusion}
3	
4	\looseness=-1 We identify symbolic confirmation bias: self-extracted constraints inherit the generating model's biases ($\text{BR} = 4.97\times$, 83.3\%), explaining why twenty-seven remediation strategies fail. Oracle controls ($+29.90$/$+14.22$\,pp) confirm the mechanism is sound; the bottleneck is extraction quality, not the formal channel. Three diagnostics predict failure ($C_0 < 5\%$, SC $\leq 40\%$, process similarity). Cross-architecture NLI escapes the bias when the verifier exceeds the generator ($p = 0.003$); DRC recovers 83--90\% of this gain at 35--39\% cost.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-22T00:57:18.989641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-22T00:57:18.990271+00:00_

1	\paragraph{Scale and language.}
2	Open-source models range from 7B to 32B parameters; frontier extension (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro) confirms SCB universality (BR $1.66$--$4.97\times$) but uses cross-model extraction via Mistral-7B rather than self-extraction, as closed-source APIs do not expose internal traces. All datasets are English-language logical reasoning benchmarks with discrete answer spaces. We do not evaluate trained symbolic extractors, external solvers with verified grounding, or multilingual settings. Oracle analysis is limited to FOLIO and ProofWriter (gold annotations available); extending to commonsense reasoning requires constructing comparable gold constraint sets. The cross-architecture NLI verifier (\S\ref{sec:cross-arch}) provides no benefit on LogiQA (combo $\Delta \leq +1$\,pp, all $p > 0.5$), indicating that cross-architecture escape requires task-verifier alignment---NLI is effective only when the task naturally decomposes into premise-conclusion entailment. Even on compatible tasks, NLI gain vanishes when the capability gap is large (Qwen3-14B ProofWriter: SC 85.83\% vs.\ DeBERTa 55\%, gap $= -30.83$\,pp, $\Delta \leq +0.50$\,pp, n.s.), and moderate negative gaps yield small, non-significant gains (LLaMA-3.1-8B: gap $= -17.50$\,pp, $+0.83$\,pp, n.s.; \S\ref{sec:cross-arch}). Scaling the cross-architecture approach---via trained verifiers, code-based symbolic execution, or multi-verifier ensembles---remains unexplored and may extend the escape to stronger generators and broader task types.
3	
4	\paragraph{Capability-gap analysis.}
5	The capability-gap analysis rests on $n{=}6$ verifier--generator conditions, of which four share the same DeBERTa verifier. While each condition pairs the verifier with a different generator (producing gains ranging from $+0.5$\,pp to $+6.67$\,pp), the shared verifier component may inflate apparent consistency. A verifier-collapsed analysis with only three independent verifiers (DeBERTa-poo
…[truncated 2722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-22T00:57:30.087324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-22T00:57:30.489446+00:00_

File content (26622 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-22T00:57:30.489983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-22T00:57:30.541049+00:00_

1	% References for SICA paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% SAT-Based Reasoning %%%
5	
6	@inproceedings{ye2024satlm,
7	  title={SatLM: Satisfiability-Aided Language Models Using Declarative Prompting},
8	  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},
9	  booktitle={Advances in Neural Information Processing Systems},
10	  volume={36},
11	  year={2024}
12	}
13	
14	%%% Program-Aided Reasoning %%%
15	
16	@inproceedings{gao2023pal,
17	  title={{PAL}: Program-aided Language Models},
18	  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
19	  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},
20	  year={2023}
21	}
22	
23	@article{chen2023program,
24	  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
25	  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
26	  journal={Transactions on Machine Learning Research},
27	  year={2023}
28	}
29	
30	@inproceedings{lyu2023faithful,
31	  title={Faithful Chain-of-Thought Reasoning},
32	  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},
33	  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
34	  year={2023}
35	}
36	
37	%%% Theoretical Foundations %%%
38	
39	@book{condorcet1785,
40	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
41	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
42	  year={1785},
43	  publisher={Imprimerie Royale},
44	  address={Paris}
45	}
46	
47	@article{austensmith1996,
48	  title={Information Aggregation, Rationality
…[truncated 143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-22T00:57:32.655759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-22T00:57:32.706724+00:00_

1	\section{Regime Scatter Plot}
2	\label{app:regime-scatter}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{f2_regime_scatter}
7	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.112$).}
8	\label{fig:regime-scatter}
9	\end{figure}
10	
11	\section{Prompt Templates}
12	\label{app:prompts}
13	
14	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
15	
16	\paragraph{System Prompt.}
17	
18	\begin{lstlisting}
19	You are a constraint extraction tool. Output ONLY
20	valid JSON. Do NOT solve problems, reason about
21	correctness, or think step-by-step. Extract
22	constraints from the given trace exactly as stated.
23	\end{lstlisting}
24	
25	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
26	
27	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
28	
29	\begin{lstlisting}
30	Extract mathematical constraints from this reasoning
31	trace as a JSON object.
32	
33	Rules:
34	- type: "equation", "inequality", or "predicate"
35	- expression: human-readable, e.g. "x + y == 14"
36	- z3_formula: a single comparison expression in
37	  Python Z3 syntax
38	- source_step: step number where the constraint
39	  appears
40	- Use variable names from the trace
41	
42	z3_formula MUST follow these rules:
43	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
44	  /, **, %
45	- Use individual named variables
…[truncated 6530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-22T00:57:36.682785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-22T00:57:36.683532+00:00_

200	
201	\section{Capability-Accuracy Constraint Diagnostics}
202	\label{app:diagnostics}
203	\label{app:cil}
204	
205	\paragraph{Cumulative Information Lift.}
206	We define \textit{Cumulative Information Lift} (CIL) to unify our diagnostics under a single information-theoretic quantity:
207	\begin{equation}
208	\label{eq:cil}
209	\text{CIL}(V, G) = \log \frac{P(V \text{ correct} \mid G \text{ wrong})}{P(V \text{ correct} \mid G \text{ correct})}.
210	\end{equation}
211	$\text{CIL} > 0$ means $V$ preferentially corrects $G$'s errors; $\text{CIL} < 0$ indicates shared bias. CIL subsumes our findings: (1)~SCB corresponds to $\text{CIL}(\text{self}, G) \approx 0$; (2)~Finding~2 predicts $\text{CIL}(V, G) > 0$ when $V$ is independent and capable; (3)~DRC routes to $V$ where expected CIL is highest.
212	
213	\paragraph{Empirical CIL across verifier--generator pairs.}
214	Table~\ref{tab:cil_empirical} reports CIL for eight verifier--generator--dataset conditions, sorted by CIL descending. All three cross-architecture NLI pairs on ProofWriter yield $\text{CIL} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\text{CIL} < 0$ (shared bias). CIL strongly predicts combo gain: Spearman $\rho = 0.881$ ($p = 0.004$), Pearson $r = 0.854$ ($p = 0.008$).
215	
216	\begin{table}[h]
217	\centering
218	\small
219	\caption{Empirical CIL across eight verifier--generator conditions (sorted by CIL descending). $\text{CIL} > 0$: cross-architecture NLI verifiers on ProofWriter. $\text{CIL} < 0$: same-model SICA or mismatched capability gap.}
220	\label{tab:cil_empirical}
221	\begin{tabular}{@{}lllrr@{}}
222	\toprule
223	Generator & Verifier & Dataset & CIL (bits) & $\Delta$ (pp) \\
224	\midrule
225	Mistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\
226	Mistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\
227	Mistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\
228	\addlinespace
229	Qwen2.5-14B & DeBERTa-MNLI & PW-600 & $
…[truncated 12999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-22T00:57:44.017409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": "400",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "offset": "400",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-22T00:57:44.018201+00:00_

400	SC (majority vote) & 76.24 & --- \\
401	SICA (MAX-SAT) & 76.49 & 773\,/\,804 \\
402	Count-only & 76.62 & 774\,/\,804 \\
403	Random-weight & 75.87 & 764\,/\,804 \\
404	\bottomrule
405	\end{tabular}
406	\end{table}
407	
408	
409	\section{Remediation Strategy Details}
410	\label{app:remediation}
411	
412	\begin{table}[h]
413	\centering
414	\small
415	\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.49\%$, $\Delta = -0.98$\,pp. None reaches significance. Three method-level strategies are reported in Table~\ref{tab:method_interventions}.}
416	\label{tab:remediation}
417	\begin{tabular}{@{}llrl@{}}
418	\toprule
419	Strategy & Target & $\Delta$ (pp) & Key finding \\
420	\midrule
421	Contrastive$^a$ & Prompt & $-$1.10 & non-disc.\ 6.0\% ($\downarrow$ from 8.2\%) \\
422	Cross-model$^b$ & Architecture & 0.00 & disc.\ 0\% (weak$\to$strong); $\pm$1\,pp (strong$\to$weak) \\
423	Qwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\
424	Z3 feedback & Solver & --- & 0.9\% UNSAT trigger \\
425	Cons.\ filtering & Noise & 0.00 & $T{\geq}4 \to$ SC \\
426	Cross-trace UNSAT & Independence & --- & 56.4\% $\emptyset$ vars \\
427	$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\
428	Multi-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\
429	Disc.\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\
430	\bottomrule
431	\end{tabular}\\[2pt]
432	{\footnotesize $^a$\,$n{=}182$ (extraction failures excluded). $^b$\,Weak$\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\to$weak: Qwen3-14B (60.29\%) and Qwen2.5-14B (58.33\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\%. $^c$\,$n{=}204$, SC $= 84.80\%$. $^d$\,Mistral-7B FOLIO, $n{=}204$. $^e$\,Mistral-7B FOLIO, $T \in \{0.3, 0.7, 1.2\}$, 4 traces each, $n{=}204$. $^f$\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}
433	\end{table}
434	
435	
436	\begin{table}[h]
437	\centering
438	\small
439	\cap
…[truncated 18326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-22T00:57:48.942417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": "649",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "offset": "649",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-22T00:57:49.043949+00:00_

649	\section{Independence-Accuracy Scatter Plot}
650	\label{app:kappa-scatter}
651	
652	\begin{figure}[h]
653	\centering
654	\includegraphics[width=\columnwidth]{figures/f6_kappa_accuracy_scatter}
655	\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\kappa \approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}
656	\label{fig:kappa-accuracy}
657	\end{figure}
658	
659	\begin{table}[h]
660	\centering
661	\small
662	\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\kappa \geq 0.41$, confirming an architecture-independent ceiling. $\kappa$: Fleiss' kappa on raw answers.}
663	\label{tab:kappa_generalization}
664	\setlength{\tabcolsep}{3.5pt}
665	\begin{tabular}{@{}llccrr@{}}
666	\toprule
667	Model & Aggregation & $\kappa$ & Eff-$K$ & $K$ & Acc.\ (\%) \\
668	\midrule
669	Mistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\
670	& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\
671	& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\
672	& ICG & 0.47 & 1.93 & 10 & 51.96 \\
673	\addlinespace
674	LLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\
675	Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\
676	Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\
677	\bottomrule
678	\end{tabular}
679	\end{table}
680	
681	\paragraph{Trace independence metrics.}
682	\label{app:trace-independence}
683	
684	Table~\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\kappa$ and Effective-K at $K = 12$, referenced in \S\ref{sec:effective-k}.
685	
686	\begin{table}[h]
687	\centering
6
…[truncated 15475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-22T00:58:03.378443+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-22T00:58:03.429199+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-22T00:58:05.258082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-22T00:58:05.810528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" submission deadline commitment page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for papers\" submission deadline commitment page limit anonymity"
  }
}
```

</details>

---


### Tool result

_source line 1184 · 2026-05-22T00:58:05.961842+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf (624.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-22T00:58:14.158251+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" submission deadline commitment page limit anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal
…[truncated 2082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 8347
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-22T00:58:42.131752+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-22T00:58:42.585071+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 144\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 11002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-22T00:58:43.491831+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-22T00:58:44.397255+00:00_

Found 13 files
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_970d5ea3f54df81296b97321fcded892_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/archive/feishu_group_oc_319977a04ca60b6c4c69a2a8d4141a75_20260521T175626_814334.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/archive/feishu_group_oc_970d5ea3f54df81296b97321fcded892_director_20260521T013002_576521.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/logs/review_worst.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-22T00:58:50.432591+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "glob": "*.yaml",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
    "glob": "*.yaml",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-22T00:58:50.483464+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-22T00:58:59.393369+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find external review config",
  "subagent_type": "Explore",
  "prompt": "Search for the project configuration file for project \"symb_invariant_consensus\" that might contain \"external_review\" or \"paperreview\" settings. Look in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ directory. Check files like config.yaml, project.yaml, settings.yaml or any yaml/json config file. Report what you find — specifically whether external_review.paperreview_ai.enabled is true or false. Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Find external review config",
    "subagent_type": "Explore",
    "prompt": "Search for the project configuration file for project \"symb_invariant_consensus\" that might contain \"external_review\" or \"paperreview\" settings. Look in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ directory. Check files like config.yaml, project.yaml, settings.yaml or any yaml/json config file. Report what you find — specifically whether external_review.paperreview_ai.enabled is true or false. Quick search."
  }
}
```

</details>

---


### Tool call

_source line 1193 · 2026-05-22T00:59:01.255927+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | grep -E \"(config|project|settings)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | grep -E \"(config|project|settings)\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1194 · 2026-05-22T00:59:01.509241+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/_last_visual_review.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_e660d20289ab9bbb488d128f5d99bf46.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_83ba13f19a2bf382207991b32ac820f6.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_review_reviewer_1.jso
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 1195 · 2026-05-22T00:59:03.640250+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ | grep -E \"\\.(yaml|yml|json)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ | grep -E \"\\.(yaml|yml|json)$\""
  }
}
```

</details>

---


### Tool result

_source line 1196 · 2026-05-22T00:59:03.769463+00:00_

-rw-r--r--  1 ubuntu ubuntu    100 May 21 20:50 _last_visual_review.json
-rw-------  1 ubuntu ubuntu    434 May 18 17:54 constraints.yaml
-rw-------  1 ubuntu ubuntu 140973 May 21 23:04 decisions.yaml
-rw-------  1 ubuntu ubuntu   6916 May 19 04:55 dream_registry.yaml
-rw-------  1 ubuntu ubuntu  11825 May 19 17:32 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  38532 May 20 10:17 literature_map.yaml
-rw-------  1 ubuntu ubuntu  69464 May 21 21:32 mistakes.yaml
-rw-------  1 ubuntu ubuntu  68342 May 20 12:12 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 266483 May 21 23:46 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  16748 May 20 12:20 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 129
}
```

</details>

---


### Tool call

_source line 1197 · 2026-05-22T00:59:05.378105+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-22T00:59:05.630237+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config -name \"*.yaml\" -o -name \"*.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config -name \"*.yaml\" -o -name \"*.json\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-22T00:59:05.731119+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_e660d20289ab9bbb488d128f5d99bf46.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_83ba13f19a2bf382207991b32ac820f6.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_review_reviewer_1.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_f265de7a9796688b878083fef59f9d4c.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_f5d680d1394a02be4b502c5606a34a84.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_7452874ce81eb89ffd857f072209b08f.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_b5b42865db9e25c090239f4ff8686b1b.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_worker_2921eca0fda86834cdecdf4269c86dd3.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_paper_agent.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_dream_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_director.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1200 · 2026-05-22T00:59:06.283569+00:00_

Found 13 files
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_970d5ea3f54df81296b97321fcded892_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/archive/feishu_group_oc_319977a04ca60b6c4c69a2a8d4141a75_20260521T175626_814334.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/archive/feishu_group_oc_970d5ea3f54df81296b97321fcded892_director_20260521T013002_576521.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/logs/review_worst.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-22T00:59:08.091837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1202 · 2026-05-22T00:59:08.092238+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0513-3
5	  my_token: 319ef9df883bc682ba43106b8d80616c1363f58f791c3250efad6bae0311eec4
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1203 · 2026-05-22T00:59:08.143577+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 2 -name \"*.yaml\" | grep -v projects | grep -v config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 2 -name \"*.yaml\" | grep -v projects | grep -v config"
  }
}
```

</details>

---


### Tool result

_source line 1204 · 2026-05-22T00:59:08.244497+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1205 · 2026-05-22T00:59:09.703330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1206 · 2026-05-22T00:59:10.005142+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-22T00:59:10.055915+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -maxdepth 2 -type f \\( -name \"config*\" -o -name \"project*\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -maxdepth 2 -type f \\( -name \"config*\" -o -name \"project*\" \\)"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-22T00:59:10.357775+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-22T00:59:11.814771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/CLAUDE.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/CLAUDE.md",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1210 · 2026-05-22T00:59:12.016196+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/review_director_9c155b71.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1211 · 2026-05-22T00:59:12.067281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/AGENTS.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/AGENTS.md",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1212 · 2026-05-22T00:59:12.067758+00:00_

1	## 当前项目
2	当前绑定项目：**symb_invariant_consensus**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("symb_invariant_consensus")` 或 `load_project_config("symb_invariant_consensus", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## 用户自定义规则（必须遵守）
11	### 审稿规则
12	
13	- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
14	- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.
15	
16	### 写作规则
17	
18	- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
19	- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
20	
21	> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
22	
23	## Worker 操作规范
24	
25	### ssh-env-setup
26	
27	# 远程服务器环境搭建规范
28	
29	## 核心原则
30	
31	**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。
32	
33	**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。
34	
35	**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**
36	
37	## Phase 1: 环境探测（用 ssh_read_only）
38	
39	连接到服务器后，第一步永远是收集信息，不要直接装东西：
40	
41	```bash
42	# 1. Python 环境
43	which py
…[truncated 2087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1213 · 2026-05-22T00:59:14.222725+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-22T00:59:14.373772+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-22T00:59:14.576408+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-22T00:59:14.577126+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 1217 · 2026-05-22T00:59:16.034089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/registry.yaml",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/registry.yaml",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1218 · 2026-05-22T00:59:16.034495+00:00_

1	baseline: null
2	experiments:
3	  crd_folio_main:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-15T09:35:42.037Z'
7	    updated_at: '2026-05-15T09:36:24.832Z'
8	    spec:
9	      command: python run_pipeline.py (CRD dual-representation pipeline)
10	      server: westd-32608
11	      data_path: /root/autodl-tmp/crdd/results/mvp_v4_full.jsonl
12	      data_count: 204
13	      model_name: Qwen3-32B-AWQ
14	      seed: 42
15	      method: CRD
16	      checkpoint_path: N/A
17	      log_path: /root/autodl-tmp/crdd/results/
18	    conclusion: success
19	    completed_at: '2026-05-15T09:36:03.793Z'
20	    hypothesis: 'CRD: 双表征(FOL+SymPy)分歧检测+定向修复能提升逻辑推理准确率（非SICA方法）'
21	    metrics:
22	      divergence_rate: 0.422
23	      diagnosis_rate: 0.872
24	      error_types: 4
25	      directed_advantage_pp: 4.7
26	      directed_p_value: 0.63
27	      localization_accuracy: 0.946
28	      fol_accuracy: 0.789
29	      code_accuracy: 0.598
30	      oracle_accuracy: 0.878
31	      pipeline_accuracy: 0.814
32	      baseline_accuracy: 0.74
33	      cost_multiplier: 5.76
34	      dataset: FOLIO
35	      n: 204
36	  smoke-test-5q:
37	    status: PREPARING
38	    retry_count: 0
39	    created_at: '2026-05-15T11:22:09.665Z'
40	    updated_at: '2026-05-15T11:22:09.666Z'
41	    conclusion: failed
42	  sica_smoke_5q:
43	    status: DONE
44	    retry_count: 0
45	    created_at: '2026-05-15T11:38:43.996Z'
46	    updated_at: '2026-05-15T11:39:13.456Z'
47	    spec:
48	      command: python3 smoke_test_5q.py (nohup)
49	      server: westd-32608
50	      data_path: /root/symb_invariant_consensus/data/math500_subset.json
51	      data_count: 5
52	      model_name: QwQ-32B
53	      seed: 42
54	      method: SICA
55	      checkpoint_path: N/A
56	      log_path: /tmp/smoke_test_5q.log
57	    hypothesis: 'SICA smoke test: 验证端到端 pipeline 可行性（5题 MATH-500, K=12, QwQ-32B）'
58	    conclusion: success
59	    completed_at: '2026-05-15T11:39:07.006Z'
60	    metrics:
61	      sica_accuracy: 0
…[truncated 3037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1219 · 2026-05-22T00:59:17.892443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/registry.yaml 2>/dev/null | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/registry.yaml 2>/dev/null | head -100"
  }
}
```

</details>

---


### Tool result

_source line 1220 · 2026-05-22T00:59:17.993599+00:00_

baseline: null
experiments:
  exp-010-mistral-v3:
    status: DONE
    retry_count: 0
    created_at: '2026-05-17T08:21:11.401Z'
    updated_at: '2026-05-17T08:21:36.306Z'
    hypothesis: 'Cross-family validation: Mistral-7B-Instruct-v0.3 on D012 (30PW+30FOLIO)
      reproduces SICA≈SC pattern, confirming capability trap generalizes across model
      families'
    parent: sica_expanded_14b
    spec:
      command: bash ~/runs/symb_invariant_consensus/run_exp010_mistral_v3.sh
      server: westd-32608
      data_path: data/D012
      data_count: 60
      model_name: Mistral-7B-Instruct-v0.3
      seed: 42
      checkpoint_source: N/A - inference only
      eval_data: D012 (30 ProofWriter + 30 FOLIO)
    log_path: ~/runs/symb_invariant_consensus/exp-010-mistral-v3.log
    checkpoint_path: N/A - inference only
    conclusion: success
    completed_at: '2026-05-17T08:21:32.459Z'
    metrics:
      sc_accuracy: 0.4833
      sica_accuracy: 0.4833
      delta_pp: 0
      n: 60
      k: 12
      discordant_pairs: 4
      sica_wins: 2
      sc_wins: 2
      pw_sica: 0.4
      pw_sc: 0.4
      folio_sica: 0.567
      folio_sc: 0.567
      extraction_rate: 0.882
      contradiction_rate: 0.056
      avg_unique_constraints: 20.5
      maxsat_mean_sat_ratio: 0.948
      low_conf_sc_problems: 12
      wall_time_min: 19.3
  exp-014-deepseek-r1-7b:
    status: RUNNING
    retry_count: 0
    created_at: '2026-05-17T11:57:23.633Z'
    updated_at: '2026-05-17T11:57:43.837Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/symb_invariant_consensus && bash scripts/run_exp014_deepseek_r1_7b.sh"
      server: westd-32608
      data_path: /root/symb_invariant_consensus/data/proofwriter_30.json + folio_30.json
      data_count: 60
      model_name: DeepSeek-R1-Distill-Qwen-7B
      seed: 42
      gpu:
      - cuda:0
      pid: '324400'
  exp-015-logic-lm-baseline:
    status: DONE
    retry_count: 0
    created_at: 
…[truncated 1563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-22T00:59:21.311082+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/ 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1222 · 2026-05-22T00:59:21.462148+00:00_

total 28
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 08:44 .
drwxr-xr-x 12 ubuntu ubuntu  4096 May 22 00:55 ..
-rw-r--r--  1 ubuntu ubuntu 15038 May 22 00:55 CLAUDE.md
drwxr-xr-x 67 ubuntu ubuntu  4096 May 21 22:20 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1223 · 2026-05-22T00:59:21.563423+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"*.json\" -o -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"*.json\" -o -name \"*.yaml\" | xargs grep -l \"external_review\\|paperreview\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-22T00:59:21.714642+00:00_

Exit code 123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1225 · 2026-05-22T00:59:23.022119+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1226 · 2026-05-22T00:59:55.709994+00:00_

&lt;persisted-output>
Output too large (53.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-review-director-9c155b71/324a7c83-24a7-416d-bd61-946df89b10a6/tool-results/bwupzah3k.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl:{"ts": "2026-05-17T17:41:44.808222+00:00", "role": "tool_result", "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director", "text": "1\t---\n2\tname: review-director-session-start\n3\tdescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\n4\tpriority: 9\n5\tscope: global\n6\ttags:\n7\t- workflow\n8\t- review\n9\t- session\n10\tversion: 3\n11\troles:\n12\t- review_director\n13\t---\n14\t\n15\t# Review Director Session 启动流程（圆桌会议模式）\n16\t\n17\t## 初始化\n18\t\n19\t1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n20\t2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n21\t3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n22\t4. 向用户简要汇报：\n23\t   - **投稿目标**：venue 和 deadline\n24\t   - **论文状态**：当前草稿位置和版本\n25\t   - **资料完整性**：提交的材料是否齐全\n26\t   - **下一步**：即将开始的圆桌审稿流程\n27\t\n28\t## 评审流程（收到论文提交后执行）\n29\t\n30\t### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n31\t\n32\t1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n33\t2. 确认目标投稿 venue（从提交消息中获取）\n34\t3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n35\t   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n36\t   - `\"&lt;venue name> 2026 submission deadline\"`\n37\t   - `\"&lt;venue name> 2026 author guidelines\"`\n38\t4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续\n39\t5. 提取当前版本的格式要求：\n40\t   - 页数限制（正文 / 附录 / 参考文献）\n41\t   - 模板（ACL / IEEE / NeurIPS / ICML / ...）\n42\t   - 匿名规则（double-blind / single-blind / open）\n43\t   - 附录规则（是否允许、是否参与审稿）\n44\t   - 引用格式（natbib / biblatex / 特定 .bst）\n45\t6. 将以
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 32687
}
```

</details>

---


### Tool call

_source line 1227 · 2026-05-22T01:00:00.945522+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 -B5 \"external_review.paperreview_ai.enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 -B5 \"external_review.paperreview_ai.enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl 2>/dev/null | head -50"
  }
}
```

</details>

---


### Tool result

_source line 1228 · 2026-05-22T01:00:01.046259+00:00_

&lt;persisted-output>
Output too large (94.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-review-director-9c155b71/324a7c83-24a7-416d-bd61-946df89b10a6/tool-results/bna87o5hx.txt

Preview (first 2KB):
{"ts": "2026-05-17T17:41:27.778038+00:00", "role": "user", "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director", "text": "[Reviewer 2 审稿意见]:\n## 总体评分\n**Overall**: 3/6 (Weak Reject)\n**一句话总结**: 论文研究了一个有意义的问题（self-extracted symbolic aggregation 何时优于 majority voting），但核心发现（\"capability trap\"）与已有文献高度重叠，关键相关工作严重缺失，且 novelty 不足以达到 top venue 录用标准。\n\n---\n\n## 官方维度打分（6 分制，top ML venue 通用标准）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Novelty/Originality | 2/6 | \"Capability trap\" 本质上是 Huang et al. (ICLR 2024) \"LLMs Cannot Self-Correct Reasoning Yet\" 的领域特化重述；oracle 实验是 sanity check 而非新发现；C0-precision diagnostic 是直觉性的两阶段过滤器 |\n| Soundness | 3/6 | 论证逻辑基本自洽，但 oracle 仅在 FOLIO 一个 domain 做，泛化性不足；~31% 统计量来自特定 14 个实验条件，论文倾向于作为一般性结论呈现 |\n| Significance | 3/6 | 实践指导有一定价值（C0-precision 部署诊断），但最终 takeaway（\"用外部 verifier\"）是已知结论 |\n| Related Work | 2/6 | 至少 6 篇关键引用缺失（详见下方），总引用量 ~18 篇远低于 top venue 常规水平（30-50+） |\n| Clarity/Presentation | 4/6 | 结构清晰，叙事线可追踪（非本次审查重点，仅基于摘要信息粗评） |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心 novelty 与 Huang et al. (ICLR 2024) 严重重叠，未引用、未区分\n\n- 具体位置：Section 5 (Discussion)、Section 1 (Introduction) 对 \"capability trap\" 的定义和论证\n- 问题：Huang et al. \"Large Language Models Cannot Self-Correct Reasoning Yet\" (ICLR 2024) 已经系统性地证明 LLMs 无法在没有外部反馈的情况下可靠地自我纠正推理。该论文的核心结论是：当 generator 和 evaluator 共享 failure modes 时，self-evaluation 提供的信号极弱（correlated error problem）。本文的 \"capability trap\"（自提取约束质量受限于模型自身能力）本质上是这一现象在 symbolic constraint extraction 场景下的特化实例。然而本文完全未引用、未讨论这一直接先驱工作。\n- 为什么影响接收：如果核心发现可以被已有 ICLR oral-level 论文解释为其推论，则 novelty claim 不成立。审稿人会立刻质疑独立贡献。\n- 建议修改方向：必须引用并明确区分。可论证的差异点包括：(1) Huang et al. 研究 intrinsic sel
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1229 · 2026-05-22T01:00:03.217103+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -type f -name \"*.yaml\" -not -path \"*/logs/*\" -not -path \"*/.claude/*\" | xargs grep -l \"external_review\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -type f -name \"*.yaml\" -not -path \"*/logs/*\" -not -path \"*/.claude/*\" | xargs grep -l \"external_review\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1230 · 2026-05-22T01:00:03.318101+00:00_

Exit code 123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-22T01:00:04.711097+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -type f \\( -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -type f \\( -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-22T01:00:04.862259+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1233 · 2026-05-22T01:00:06.471446+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/ | grep -E \"\\.(yaml|json|config)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/ | grep -E \"\\.(yaml|json|config)\""
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-22T01:00:06.572293+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1235 · 2026-05-22T01:00:08.884949+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/approvals.yaml 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/approvals.yaml 2>/dev/null | head -50"
  }
}
```

</details>

---


### Tool result

_source line 1236 · 2026-05-22T01:00:08.935728+00:00_

approvals:
  apr_20260517T193104_lw9x:
    approval_id: apr_20260517T193104_lw9x
    context:
      chat_id: oc_970d5ea3f54df81296b97321fcded892
      deadline: '2026-05-25'
      has_prior_review: true
      mode_reason: Round 1 审稿后大量修复（Table 3 数字、σ 定义、DeepSeek-R1 C0、Δ 范围等），需要验证 Round
        1 的 14 个 issues 是否全部 resolved。
      paper_path: projects/symb_invariant_consensus/docs/paper/main.tex
      paper_title: EMNLP 2026
      reason: 全文终审 PASS。8pp 正文 + 4pp appendix/references，编译 0 errors。历史 9 项 CRITICAL/WARNING
        全部验证修复。数据一致性、AI 风格、EMNLP 格式合规均通过。Phase 2 写作完成（Abstract/Intro/Discussion/Conclusion），所有实验数据（含
        T=0.7 同源补跑）已入论文。唯一残留 WARNING 为 11.5% discriminative constraints 数据溯源（数据文件存在但未在远程服务器同步，artifact
        已注册）。
      recommended_review_mode: continue
      review_chat_id: oc_c338e034cbffa10b9cc723e731d288d8
      review_mode: fresh
      review_round: 0
      supplementary_paths: ''
      track: Main Conference
      venue: EMNLP 2026
    created_at: '2026-05-17T19:31:04.894Z'
    feishu_card_message_id: om_x100b6f95397648a0c37dcfc5f123971
    project: symb_invariant_consensus
    reject_reason: null
    resolved_at: '2026-05-18T01:30:31.503059+00:00'
    resolved_by: feishu:ou_fe906a2a0b37a0531edeaa0539755598
    risk_score:
      auto_approve: false
      dimensions: []
      overall: low
      reason: 需要人工审批。（无维度数据）
    status: approved
    subject_id: symb_invariant_consensus-emnlp-2026
    type: submission
  apr_20260518T031500_i3lu:
    approval_id: apr_20260518T031500_i3lu
    context:
      chat_id: oc_970d5ea3f54df81296b97321fcded892
      deadline: '2026-05-25'
      has_prior_review: true
      mode_reason: 12 项 Round 2 修复需逐条验证是否到位，continue 模式让 Reviewer 对比上轮报告高效确认。
      paper_path: projects/symb_invariant_consensus/docs/paper/main.tex
      paper_title: EMNLP 2026
      reason: Round 2 审稿 12 项修复全部完成：σ(c,a) 描述修正为 source-trace indicator + 伪代码、Stechly/Valmeekam/Kambhampati
        引用、model family wording 统一、oracle claim scope 限定、confirmato
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-22T01:00:10.996688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_review_director.json",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/mcp_config_review_director.json",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-22T01:00:11.047574+00:00_

1	{
2	  "mcpServers": {
3	    "agent-ml-research": {
4	      "command": "/home/ubuntu/agent-ml-research/.venv/bin/python",
5	      "args": [
6	        "-m",
7	        "core.mcp_server",
8	        "--review-director"
9	      ],
10	      "cwd": "/home/ubuntu/agent-ml-research",
11	      "env": {
12	        "AGENT_ML_WORKSPACE": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
13	        "REVIEW_DIRECTOR_MODE": "1"
14	      }
15	    }
16	  }
17	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1239 · 2026-05-22T01:00:12.739109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | grep -i config | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | grep -i config | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-22T01:00:13.734133+00:00_

/home/ubuntu/agent-ml-research/docs/demo/tsconfig.json
/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/portal/tsconfig.app.json
/home/ubuntu/agent-ml-research/portal/tsconfig.json
/home/ubuntu/agent-ml-research/portal/tsconfig.node.json
/home/ubuntu/agent-ml-research/config/venue_rules/aaai-2027.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/icml-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/neurips-2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 995
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-22T01:00:15.040693+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/ 2>/dev/null | grep symb"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/ 2>/dev/null | grep symb"
  }
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-22T01:00:15.091979+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1243 · 2026-05-22T01:00:16.247571+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1244 · 2026-05-22T01:00:16.301096+00:00_

total 12
drwxrwxr-x 2 ubuntu ubuntu 4096 May  9 09:00 .
drwxrwxr-x 3 ubuntu ubuntu 4096 May 13 11:22 ..
-rw-rw-r-- 1 ubuntu ubuntu  337 May  9 09:00 LLM-Calibration.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1245 · 2026-05-22T01:00:17.909790+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*.py\" | xargs grep -l \"external_review\\|paperreview_ai\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"*.py\" | xargs grep -l \"external_review\\|paperreview_ai\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-22T01:00:30.166598+00:00_

/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py
/home/ubuntu/agent-ml-research/tests/test_paper_review_handoff.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_simple.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_no_continue.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 12256
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-22T01:00:31.774833+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A10 -B5 \"external_review\\|paperreview_ai\" /home/ubuntu/agent-ml-research/tests/test_paper_review_handoff.py | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A10 -B5 \"external_review\\|paperreview_ai\" /home/ubuntu/agent-ml-research/tests/test_paper_review_handoff.py | head -50"
  }
}
```

</details>

---


### Tool result

_source line 1248 · 2026-05-22T01:00:31.825763+00:00_

        ), patch(
            "core.approvals.hooks._send_to_session",
        ), patch(
            "core.approvals.hooks._reset_review_sessions",
        ), patch(
            "core.tools.external_review.reset_state",
        ), patch(
            "threading.Thread",
            new=_InlineThread,
        ):
            ApprovalManager().approve(approval_id, by="human_test")

        # Existing chat must NOT be re-created
        create_mock.assert_not_called()

        from core.tools.project_config import load_review_chat_id, load_review_round

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1249 · 2026-05-22T01:00:33.287106+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/core -name \"*.py\" | xargs grep -l \"external_review\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research/core -name \"*.py\" | xargs grep -l \"external_review\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1250 · 2026-05-22T01:00:33.337740+00:00_

/home/ubuntu/agent-ml-research/core/tool_registry.py
/home/ubuntu/agent-ml-research/core/tools/visual_check.py
/home/ubuntu/agent-ml-research/core/tools/project_config.py
/home/ubuntu/agent-ml-research/core/tools/external_review.py
/home/ubuntu/agent-ml-research/core/tools/dream.py
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/api/routers/projects.py
/home/ubuntu/agent-ml-research/core/feishu_webhook.py
/home/ubuntu/agent-ml-research/core/approvals/hooks.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1251 · 2026-05-22T01:00:34.705099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"paperreview_ai.enabled\\|external_review\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"paperreview_ai.enabled\\|external_review\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1252 · 2026-05-22T01:00:34.755755+00:00_

459:def is_external_review_enabled(project_name: str) -> bool:
462:    Reads ``external_review.paperreview_ai.enabled`` from project config.
468:    ext = result.data["config"].get("external_review", {})

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1253 · 2026-05-22T01:00:36.315706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-22T01:00:36.316207+00:00_

1	"""Project configuration loader — reads config/projects/{name}.yaml.
2	
3	Each project config declares server, codebase paths, evaluation metrics,
4	and W&B settings. The orchestrator injects this into the system prompt
5	and MCP tool defaults at session startup.
6	"""
7	
8	from __future__ import annotations
9	
10	from pathlib import Path
11	
12	import yaml
13	
14	from core.tools.result import ToolResult
15	
16	# ---------------------------------------------------------------------------
17	# Paths
18	# ---------------------------------------------------------------------------
19	
20	from core import paths as _paths
21	
22	
23	# ---------------------------------------------------------------------------
24	# Path expansion — resolve ~ in config values so non-interactive shells work
25	# ---------------------------------------------------------------------------
26	
27	# Top-level keys whose string values may contain ~
28	_PATH_KEYS = {"root", "project_path", "log_dir"}
29	
30	
31	def _expand_paths(config: dict) -> None:
32	    """In-place expand ~ in known path fields using the remote account's home.
33	
34	    These paths refer to remote servers, NOT the local machine.
35	    ``~`` is resolved to ``/home/{account}`` (standard Linux layout)
36	    using the account from ``execution.servers[0].account`` or
37	    ``execution.account``.
38	    """
39	    # Determine remote account for ~ expansion
40	    exec_cfg = config.get("execution", {})
41	    account = exec_cfg.get("account", "")
42	    if not account:
43	        servers = exec_cfg.get("servers")
44	        if isinstance(servers, list) and servers:
45	            first = servers[0]
46	            if isinstance(first, dict):
47	                account = first.get("account", "")
48	    # Fallback: extract account from resources.yaml server host (user@ip)
49	    if not account:
50	        server_name = exec_cfg.get("server", "")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-22T01:00:37.722637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py",
  "offset": "450",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py",
    "offset": "450",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 1256 · 2026-05-22T01:00:37.773687+00:00_

450	        return "", "", ""
451	    feishu = result.data["config"].get("feishu", {})
452	    return (
453	        feishu.get("review_paper_path", "") or "",
454	        feishu.get("review_paper_pdf_path", "") or "",
455	        feishu.get("review_supplementary_paths", "") or "",
456	    )
457	
458	
459	def is_external_review_enabled(project_name: str) -> bool:
460	    """Check if external review (paperreview.ai) is enabled for a project.
461	
462	    Reads ``external_review.paperreview_ai.enabled`` from project config.
463	    Returns False if not configured.
464	    """
465	    result = load_project_config(project_name)
466	    if not result.success:
467	        return False
468	    ext = result.data["config"].get("external_review", {})
469	    return bool(ext.get("paperreview_ai", {}).get("enabled", False))
470	
471	
472	def save_project_study_config(
473	    project_name: str,
474	    study_chat_id: str,
475	) -> ToolResult:
476	    """Save feishu.study_chat_id to project config YAML (Group D).
477	
478	    Args:
479	        project_name: Project identifier.
480	        study_chat_id: Study phase group chat_id (Group D).
481	
482	    Returns:
483	        ToolResult with updated feishu config on success.
484	    """
485	    path = _paths.projects_config_dir() / f"{project_name}.yaml"
486	    try:
487	        with open(path) as f:
488	            config = yaml.safe_load(f) or {}
489	    except FileNotFoundError:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1257 · 2026-05-22T01:00:39.380695+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/symb_invariant_consensus.yaml 2>/dev/null || echo \"NOT FOUND\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/agent-ml-research/workspace/config/projects/symb_invariant_consensus.yaml 2>/dev/null || echo \"NOT FOUND\""
  }
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-22T01:00:39.532096+00:00_

NOT FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-22T01:00:41.042120+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"projects_config_dir\" /home/ubuntu/agent-ml-research/core/tools/project_config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"projects_config_dir\" /home/ubuntu/agent-ml-research/core/tools/project_config.py"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-22T01:00:41.092944+00:00_

87:    if not _paths.projects_config_dir().exists():
89:    projects = sorted(p.stem for p in _paths.projects_config_dir().glob("*.yaml"))
109:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
111:        available = sorted(p.stem for p in _paths.projects_config_dir().glob("*.yaml"))
221:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
242:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
270:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
305:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
356:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
391:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
420:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
485:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
563:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
687:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
809:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
969:    path = _paths.projects_config_dir() / f"{project_name}.yaml"
1085:    path = _paths.projects_config_dir() / f"{project_name}.yaml"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-22T01:00:42.349150+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"def projects_config_dir\" /home/ubuntu/agent-ml-research/core/paths.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"def projects_config_dir\" /home/ubuntu/agent-ml-research/core/paths.py"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-22T01:00:42.399794+00:00_

def projects_config_dir() -> Path:
    return WORKSPACE_ROOT / "config" / "projects"


def global_dir() -> Path:
    """Cross-project operational data (logs, worker registry, approvals)."""

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1263 · 2026-05-22T01:00:43.806460+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B5 \"WORKSPACE_ROOT\" /home/ubuntu/agent-ml-research/core/paths.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B5 \"WORKSPACE_ROOT\" /home/ubuntu/agent-ml-research/core/paths.py | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1264 · 2026-05-22T01:00:43.857377+00:00_

"""Centralized path resolution & tiny shared helpers.

Separates framework code (REPO_ROOT) from user data (WORKSPACE_ROOT).

REPO_ROOT:       Always the git repository root (framework code, skills/, CLAUDE.md).
WORKSPACE_ROOT:  User data root, resolved as:
--
    if env:
        return Path(env).expanduser().resolve()
    return _DEFAULT_WORKSPACE


WORKSPACE_ROOT: Path = _resolve_workspace()


def _override_workspace_root(path: Path) -> None:
    """Test-only: redirect all workspace paths to *path*."""
    global WORKSPACE_ROOT
    WORKSPACE_ROOT = path.resolve()  # resolve symlinks (macOS /var → /private/var)
--

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-22T01:00:45.415202+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"AGENT_ML_WORKSPACE\\|DEFAULT_WORKSPACE\" /home/ubuntu/agent-ml-research/core/paths.py | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"AGENT_ML_WORKSPACE\\|DEFAULT_WORKSPACE\" /home/ubuntu/agent-ml-research/core/paths.py | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1266 · 2026-05-22T01:00:45.415650+00:00_

7:                   1. Environment variable AGENT_ML_WORKSPACE
40:_DEFAULT_WORKSPACE = Path.home() / ".agent-ml-research"
45:    env = os.environ.get("AGENT_ML_WORKSPACE")
48:    return _DEFAULT_WORKSPACE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-22T01:00:47.676018+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1268 · 2026-05-22T01:00:48.279397+00:00_

total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 May 15 08:44 .
drwxrwxr-x 5 ubuntu ubuntu 4096 May 22 00:57 ..
-rw-r--r-- 1 ubuntu ubuntu  680 May 15 08:13 cross_representation_disagreement_diagno.yaml
-rw-r--r-- 1 ubuntu ubuntu 1040 May 22 00:55 symb_invariant_consensus.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1269 · 2026-05-22T01:00:49.637983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-22T01:00:49.638424+00:00_

1	execution:
2	  gpu_constraint: westd-25068:cuda:0,cuda:1,cuda:2,cuda:3
3	  gpu_ids:
4	  - westd-25068:cuda:0
5	  - westd-25068:cuda:1
6	  - westd-25068:cuda:2
7	  - westd-25068:cuda:3
8	  - westd-16639:cuda:0
9	  - westd-16639:cuda:1
10	  - westd-16639:cuda:2
11	  - westd-16639:cuda:3
12	  project_path: /root/symb_invariant_consensus
13	  servers:
14	  - westd-25068
15	  - westd-16639
16	feishu:
17	  chat_id: oc_970d5ea3f54df81296b97321fcded892
18	  operational_chat_id: oc_319977a04ca60b6c4c69a2a8d4141a75
19	  review_mode: fresh
20	  review_paper_path: projects/symb_invariant_consensus/docs/paper/main.tex
21	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf
22	  review_round: 9
23	  review_supplementary_paths: ''
24	  submission_chat_id: oc_c338e034cbffa10b9cc723e731d288d8
25	project:
26	  created_at: '2026-05-15T08:44:44.820Z'
27	  description: Formally-Verified Intermediate Constraint Consensus Across Reasoning
28	    Paths
29	  name: symb_invariant_consensus
30	  phase: research
31	  source_idea_id: idea_013
32	venue: emnlp-2026
33	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-22T01:00:53.355111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review:\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review:\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1272 · 2026-05-22T01:01:32.703425+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/chats/feishu_group_oc_c338e034cbffa10b9cc723e731d288d8_director.jsonl:{"ts": "2026-05-20T12:56:59.484470+00:00", "role": "tool_result", "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director", "text": "Based on my investigation, I now have a comprehensive understanding of the external review configuration for the symb_invariant_consensus project. Let me provide a final summary report.\n\n## Final Report: External Review Configuration for symb_invariant_consensus Project\n\n**Project Configuration File Location:**\n`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml`\n\n**Current Configuration Content:**\n\nThe project configuration file currently contains the following sections:\n1. **execution** - GPU and server constraints\n2. **feishu** - Feishu (internal communication) configuration\n3. **project** - Basic project metadata\n4. **venue** - Target venue specification (EMNLP-2026)\n\n**External Review Configuration Status:**\n\n**IMPORTANT**: The `external_review` section is **NOT currently defined** in the symb_invariant_consensus.yaml file. \n\nAccording to the codebase analysis (specifically `/home/ubuntu/agent-ml-research/core/tools/project_config.py`), the expected structure for external review configuration should be:\n\n```yaml\nexternal_review:\n  paperreview_ai:\n    enabled: true|false\n    # Additional settings would go here\n```\n\n**Where Configuration is Expected:**\n- **File**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml`\n- **Section path**: `external_review.paperreview_ai.enabled`\n\n**How External Review Works (from code analysis):**\n\n1. The project uses Stanford Agentic Reviewer (paperreview.ai) for external review functionality\n2. When `external_review.paperreview_ai.enabled` is set to `true`, the system:\n   - Sends Feishu cards requesting manual su
…[truncated 3078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 39348
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-22T01:01:36.783570+00:00_

Perfect! The grep output from the logs shows that past review director sessions have already investigated this. Based on all the evidence I've collected, I can now provide a clear report:

## Summary: External Review Configuration for symb_invariant_consensus

**Configuration File Location:**
`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml`

**Finding - external_review.paperreview_ai.enabled:**

**Status: NOT CONFIGURED (defaults to FALSE)**

The project configuration file at `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml` does NOT contain an `external_review` section. 

**Current Configuration Sections Present:**
- `execution` - GPU constraints and server allocation
- `feishu` - Internal communication channels
- `project` - Basic metadata
- `venue` - Target venue (EMNLP 2026)

**Missing Configuration:**
There is no `external_review.paperreview_ai.enabled` setting in the file. According to the codebase (file: `/home/ubuntu/agent-ml-research/core/tools/project_config.py`, function `is_external_review_enabled()`), when this setting is absent, the system defaults to **FALSE**, meaning external review via paperreview.ai is **DISABLED**.

**To enable external review**, the configuration would need to be added as:
```yaml
external_review:
  paperreview_ai:
    enabled: true
```

This finding is consistent with evidence from previous review director sessions (logged May 20, 2026) which noted "No external_review config found" and confirmed the status as "not_requested".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Agent",
  "elapsed_ms": 157390
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-22T01:01:55.285982+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-22T01:02:27.047645+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 31761
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-22T01:02:27.249004+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析 + 可复现性**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 Main（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 不计页数\n- **模板**: ACL style (`acl.sty`)\n- **匿名**: Double-blind\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, conclusion.tex, limitations_content.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning from 7B to Frontier Scale\"\n\n这是一篇负面结果（negative result）论文，研究 LLM 自提取符号约束是否能改善 Self-Consistency 推理。核心发现是\"symbolic confirmation bias\"——自提取约束继承模型偏差（bias ratio 4.97×），27种修复策略全部失败。提出跨架构 NLI 验证作为逃逸路径（+6.67pp on ProofWriter），以及 DRC 自适应路由方法。\n\n## 你的审查重点\n\n### 1. 方法严谨性\n- SICA pipeline 的形式化是否严谨（MAX-SAT formulation, scoring function, degeneration condition）\n- \"Symbolic Mirage Hypothesis\" 和两个 \"Empirical Finding\" 的理论基础是否站得住脚\n- Effective-K 公式(Eq.1)用 Fleiss' κ 代替 ICC 是否合理，作者的 monotonic relationship 验证(r=0.625)是否充分\n- CIL (Cumulative Information Lift) 定义是否有 information-theoretic 问题\n- Bias Ratio 的定义和计算是否有 confounding factors\n\n### 2. 实验设计\n- 6个开源模型 + 5个 frontier 模型覆盖是否足够\n- 3个 dataset (FOLIO 204, ProofWriter 600, LogiQA 200) 样本量是否足够支撑结论\n- K=12, T=0.7 的参数选择是否合理，sensitivity analysis 是否充分\n- 4-seed replication 只在 Mistral-7B FOLIO 上做，是否足够\n- Oracle control 的设计是否合理（仅 FOLIO 和 ProofWriter 有 gold annotations）\n- 27个 remediation 策略的覆盖性——是否有明显遗漏的重要方向\n\n### 3. 统计分析\n- McNemar exact test 的选择是否合理\n- BH 多重比较校正（m=16）是否恰当\n- TOST equivalence test 的 ±2pp margin 设定是否合理\n- Bootstrap CI 方法是否正确\n- 统计功效（power analysis 报告 <21%）对结论的影响\n- capability-gap 分析仅 n=6 条件、4/6 共享同一 DeBERTa verifier——这对结论有多大影响\n- process-κ gradient 的 Spearman ρ=-1.0, n=5 的统计效力\n\n### 4. 可复现性\n- 实验参数是否完整披露\n- 代码/数据承诺是否可信\n- 是否有足够的 ablation 支撑结论\n\n请给出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，这是重点), Questions (需要作者回答的), Minor Issues, 以及你建议的 Overall Assessment score（使用 EMNLP 2026 评分标准）+ Confidence (1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计分析 + 可复现性**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 Main（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 不计页数\n- **模板**: ACL style (`acl.sty`)\n- **匿名**: Double-blind\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, conclusion.tex, limitations_content.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning from 7B to Frontier Scale\"\n\n这是一篇负面结果（negative result）论文，研究 LLM 自提取符号约束是否能改善 Self-Consistency 推理。核心发现是\"symbolic confirmation bias\"——自提取约束继承模型偏差（bias ratio 4.97×），27种修复策略全部失败。提出跨架构 NLI 验证作为逃逸路径（+6.67pp on ProofWriter），以及 DRC 自适应路由方法。\n\n## 你的审查重点\n\n### 1. 方法严谨性\n- SICA pipeline 的形式化是否严谨（MAX-SAT formulation, scoring function, degeneration condition）\n- \"Symbolic Mirage Hypothesis\" 和两个 \"Empirical Finding\" 的理论基础是否站得住脚\n- Effective-K 公式(Eq.1)用 Fleiss' κ 代替 ICC 是否合理，作者的 monotonic relationship 验证(r=0.625)是否充分\n- CIL (Cumulative Information Lift) 定义是否有 information-theoretic 问题\n- Bias Ratio 的定义和计算是否有 confounding factors\n\n### 2. 实验设计\n- 6个开源模型 + 5个 frontier 模型覆盖是否足够\n- 3个 dataset (FOLIO 204, ProofWriter 600, LogiQA 200) 样本量是否足够支撑结论\n- K=12, T=0.7 的参数选择是否合理，sensitivity analysis 是否充分\n- 4-seed replication 只在 Mistral-7B FOLIO 上做，是否足够\n- Oracle control 的设计是否合理（仅 FOLIO 和 ProofWriter 有 gold annotations）\n- 27个 remediation 策略的覆盖性——是否有明显遗漏的重要方向\n\n### 3. 统计分析\n- McNemar exact test 的选择是否合理\n- BH 多重比较校正（m=16）是否恰当\n- TOST equivalence test 的 ±2pp margin 设定是否合理\n- Bootstrap CI 方法是否正确\n- 统计功效（power analysis 报告 <21%）对结论的影响\n- capability-gap 分析仅 n=6 条件、4/6 共享同一 DeBERTa verifier——这对结论有多大影响\n- process-κ gradient 的 Spearman ρ=-1.0, n=5 的统计效力\n\n### 4. 可复现性\n- 实验参数是否完整披露\n- 代码/数据承诺是否可信\n- 是否有足够的 ablation 支撑结论\n\n请给出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，这是重点), Questions (需要作者回答的), Minor Issues, 以及你建议的 Overall Assessment score（使用 EMNLP 2026 评分标准）+ Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-22T01:02:57.406592+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30157
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-22T01:02:57.909446+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责**新颖性 + 定位 + Related Work 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 Main（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 不计页数\n- **模板**: ACL style (`acl.sty`)\n- **匿名**: Double-blind\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, conclusion.tex, limitations_content.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning from 7B to Frontier Scale\"\n\n这是一篇负面结果论文，核心贡献是：(1) Symbolic Confirmation Bias 现象的发现和量化（BR=4.97×），(2) Independence-Accuracy Trade-off 在 LLM 自提取中的具体量化（K_eff, BR, C_0），(3) Process-Level Independence 分析（CoT cosine similarity vs answer-level κ），(4) DRC 自适应路由方法。涉及 6 个开源模型 + 5 个 frontier 模型，3 个逻辑推理数据集，27 种修复策略。\n\n## 你的审查重点\n\n### 1. 新颖性和贡献\n- \"Symbolic Confirmation Bias\" 是否真正是新发现？与 Huang et al. 2024（self-correction fails without external feedback）、Stechly et al. 2025（self-verification unreliable）、Wan et al. 2025 / Jhaveri et al. 2026（CoT confirmation bias）的区别是否足够\n- 负面结果（SICA 不 work）本身是否有足够的学术价值\n- \"Independence-Accuracy Trade-off\" 是否只是 diversity-accuracy tradeoff (Krogh & Vedelsby 1994) 的 restatement\n- 四个 contribution 是否各自独立且都有足够深度\n- CIL (Cumulative Information Lift) 是否有足够的理论贡献，还是只是一个 ad-hoc diagnostic\n- DRC 方法的贡献——简单的 threshold-based routing 是否有足够的 novelty\n\n### 2. 定位和 Framing\n- 标题是否准确反映论文内容（\"Do Not Improve\" 是否过于绝对，考虑到 frontier 模型用的是 cross-model extraction 而非 self-extraction）\n- Abstract 信息密度很高，是否过载\n- Introduction 的叙事结构——从 SC 瓶颈 → CJT 框架 → SICA → 失败 → 诊断 → 逃逸——是否清晰\n- \"Symbolic Mirage Hypothesis\" 的命名和表述——是否有 overclaiming\n- 正面结果（cross-architecture escape, DRC）在论文定位中的权重——是否为负面结果论文加了太多正面内容导致叙事失焦\n\n### 3. Related Work 完整性\n- 是否遗漏了重要的相关工作（特别是 2025-2026 的最新工作）\n- 与 Kuai et al. 2026 (BEI, CIG for cross-model behavioral dependencies) 的关系是否讨论充分\n- SatLM 作为对照的讨论是否公平\n- 是否应该讨论更多 trained verifier / reward model 文献\n- Neuro-symbolic reasoning 的三分类法（Specification-generation / Program-generation / Trace-extraction）是否完整\n\n### 4. 写作质量\n- 论文 8 页限制下信息密度是否过高\n- Section 结构是否合理——8个 section（含 Discussion 和 Conclusion 分开）是否过多\n- 图表安排——Figure 1 pipeline 图、Figure 2 interventions summary、Table 1 main results、Table 2 cross-generator 的放置和引用是否合理\n- Appendix 体量（约 18 页）是否过大，关键信息是否应该在正文\n- 数学符号使用的一致性\n- 语法、拼写、引用格式\n\n### 5. 格式合规\n- 是否符合 ACL style\n- 正文是否控制在 8 页\n- Limitations section 是否符合 ARR 要求（是否涵盖关键局限性）\n- 匿名性检查（是否有 de-anonymization 风险）\n- 引用格式（natbib）是否一致\n\n请给出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，这是重点), Questions (需要作者回答的), Minor Issues, 以及你建议的 Overall Assessment score（使用 EMNLP 2026 评分标准）+ Confidence (1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 2，负责**新颖性 + 定位 + Related Work 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 Main（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限制，Limitations 不计页数\n- **模板**: ACL style (`acl.sty`)\n- **匿名**: Double-blind\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`（含 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, conclusion.tex, limitations_content.tex, appendix.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n## 论文概要\n标题: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning from 7B to Frontier Scale\"\n\n这是一篇负面结果论文，核心贡献是：(1) Symbolic Confirmation Bias 现象的发现和量化（BR=4.97×），(2) Independence-Accuracy Trade-off 在 LLM 自提取中的具体量化（K_eff, BR, C_0），(3) Process-Level Independence 分析（CoT cosine similarity vs answer-level κ），(4) DRC 自适应路由方法。涉及 6 个开源模型 + 5 个 frontier 模型，3 个逻辑推理数据集，27 种修复策略。\n\n## 你的审查重点\n\n### 1. 新颖性和贡献\n- \"Symbolic Confirmation Bias\" 是否真正是新发现？与 Huang et al. 2024（self-correction fails without external feedback）、Stechly et al. 2025（self-verification unreliable）、Wan et al. 2025 / Jhaveri et al. 2026（CoT confirmation bias）的区别是否足够\n- 负面结果（SICA 不 work）本身是否有足够的学术价值\n- \"Independence-Accuracy Trade-off\" 是否只是 diversity-accuracy tradeoff (Krogh & Vedelsby 1994) 的 restatement\n- 四个 contribution 是否各自独立且都有足够深度\n- CIL (Cumulative Information Lift) 是否有足够的理论贡献，还是只是一个 ad-hoc diagnostic\n- DRC 方法的贡献——简单的 threshold-based routing 是否有足够的 novelty\n\n### 2. 定位和 Framing\n- 标题是否准确反映论文内容（\"Do Not Improve\" 是否过于绝对，考虑到 frontier 模型用的是 cross-model extraction 而非 self-extraction）\n- Abstract 信息密度很高，是否过载\n- Introduction 的叙事结构——从 SC 瓶颈 → CJT 框架 → SICA → 失败 → 诊断 → 逃逸——是否清晰\n- \"Symbolic Mirage Hypothesis\" 的命名和表述——是否有 overclaiming\n- 正面结果（cross-architecture escape, DRC）在论文定位中的权重——是否为负面结果论文加了太多正面内容导致叙事失焦\n\n### 3. Related Work 完整性\n- 是否遗漏了重要的相关工作（特别是 2025-2026 的最新工作）\n- 与 Kuai et al. 2026 (BEI, CIG for cross-model behavioral dependencies) 的关系是否讨论充分\n- SatLM 作为对照的讨论是否公平\n- 是否应该讨论更多 trained verifier / reward model 文献\n- Neuro-symbolic reasoning 的三分类法（Specification-generation / Program-generation / Trace-extraction）是否完整\n\n### 4. 写作质量\n- 论文 8 页限制下信息密度是否过高\n- Section 结构是否合理——8个 section（含 Discussion 和 Conclusion 分开）是否过多\n- 图表安排——Figure 1 pipeline 图、Figure 2 interventions summary、Table 1 main results、Table 2 cross-generator 的放置和引用是否合理\n- Appendix 体量（约 18 页）是否过大，关键信息是否应该在正文\n- 数学符号使用的一致性\n- 语法、拼写、引用格式\n\n### 5. 格式合规\n- 是否符合 ACL style\n- 正文是否控制在 8 页\n- Limitations section 是否符合 ARR 要求（是否涵盖关键局限性）\n- 匿名性检查（是否有 de-anonymization 风险）\n- 引用格式（natbib）是否一致\n\n请给出完整审稿意见，包含：Summary (2-3句), Strengths (逐条), Weaknesses (逐条，这是重点), Questions (需要作者回答的), Minor Issues, 以及你建议的 Overall Assessment score（使用 EMNLP 2026 评分标准）+ Confidence (1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-22T01:02:59.470120+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1560
}
```

</details>

---


### Assistant

_source line 1280 · 2026-05-22T01:03:09.261745+00:00_

圆桌审稿已启动，当前状态：

| 任务 | 状态 |
|------|------|
| **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析） | 已分配，审稿中 |
| **Reviewer 2**（新颖性 + 定位 + Related Work + 写作 + 格式） | 已分配，审稿中 |
| **视觉审查 Agent** | 已派发，渲染中 |
| **外部审稿（Stanford Agentic Reviewer）** | 未配置，跳过 |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 1281 · 2026-05-22T01:08:23.828748+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计分析 + 可复现性

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），通过从 LLM 推理 trace 中自提取逻辑约束并用 MAX-SAT 聚合来扩展 Self-Consistency。核心发现是负面结果：自提取约束继承模型偏差（"symbolic confirmation bias"，BR=4.97×），27 种修复策略全部失败。文章同时提出跨架构 NLI 验证作为逃逸路径（ProofWriter +6.67pp）和 DRC 自适应路由方法。研究范围广（11 模型、3 数据集、27 策略），oracle 控制实验设计合理，但统计功效不足以支撑"无效果"的强结论。

## 总体评分
**Overall**: 3.5（Borderline Conference）
**一句话总结**: 一项范围广泛、诊断细致的负面结果研究，但统计功效不足以支撑核心"无效果"结论，正面贡献（跨架构逃逸）的证据基础偏薄。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claim 有实验支撑，但负面结果的统计功效<21%是根本性弱点；capability-gap 分析 n=6 且 4/6 共享 verifier |
| Excitement | 3/5 | 负面结果有价值但新颖性有限；跨架构逃逸方向有趣但证据不够强 |
| Reproducibility | 3.5/5 | 参数披露完整，但无匿名代码仓库；仅承诺"发表后公开" |
| Overall Assessment | 3.5 | Borderline Conference——适合 Findings 或经修改后可冲 Conference |
| Confidence | 4 | 仔细阅读了全文和 appendix，对评估有较高信心 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 统计功效不足以支撑"SICA 无效果"的核心结论
- 具体位置：Section 4.2 (Main Results), Appendix E (Power Analysis), Table 5
- 问题：论文的核心 claim 是 SICA 不改善 Self-Consistency。但 Appendix E 的 power analysis 显示，McNemar 检验在 n=200–600 条件下检测 |Δ|=2pp 效应的统计功效低于 21%。最大的研究（Qwen-14B, n=804）MDE=1.86pp，但观测 Δ=+0.25pp——这意味着即使存在 1.5pp 的真实正效果，该研究也很可能检测不到。16 个非退化条件中 10 个在 TOST 中属于"underpowered"。论文在 Limitations 中承认了这一点，但正文的叙述（如 abstract "we find no evidence of improvement"）将"检测不到效果"等同于"没有效果"，这在方法论上不严谨。
- 为什么影响接收：一篇负面结果论文的核心价值在于排除假设，但功效<21% 无法可靠地排除小但有意义的正效果。这是论文逻辑链条的根基问题。
- 建议修改方向：(1) 在 abstract 和 introduction 中使用更审慎的措辞，如 "we find no statistically detectable improvement at our sample sizes" 而非 "no evidence of improvement"；(2) 明确报告各条件下可排除的效应大小范围（如 "我们可以排除超过 X pp 的效果"）；(3) 考虑增加更多 seed 以缩小 CI 宽度。

**N2** [critical] 单 seed 复制严重不足，主要结论建立在不稳定的基础上
- 具体位置：Section 4.2, Table 1; Appendix M (K Sensitivity); Limitations §"Single-seed replication"
- 问题：Table 1 中大多数条件仅使用单个随机 seed。唯一进行 4-seed 复制的条件（Mistral-7B FOLIO）显示 Δ 范围从 +3.43 到 -0.49pp，跨度约 4pp——这已经超过 TOST 等价性边界 ±2pp。也就是说，同一实验条件在不同 seed 下可以从"正面趋势"翻转为"零效果"或"轻微负面"。温度敏感性分析（Appendix M.2）也显示 T=0.7 是一个"孤立峰"。在如此高 seed 敏感性下，其他 single-seed 条件的结果可靠性存疑。
- 为什么影响接收：如果 Mistral-7B FOLIO 这个条件的方差是典型的，那么 Table 1 中每个 single-seed 条件的 Δ 都可能在 ±4pp 范围内波动。这使得区分"真实效果"和"seed 噪声"几乎不可能。
- 建议修改方向：至少对 3-4 个关键条件（如 Qwen2.5-14B FOLIO、Qwen2.5-14B PW-D5、LLaMA-3.1-8B FOLIO）进行 4-seed 复制，报告均值±标准差。如果资源不允许，应在正文（不仅是 Limitations）中明确标注 single-seed 的局限性，并降低结论的强度。

**N3** [critical] Capability-gap 分析的证据基础过于薄弱
- 具体位置：Section 6 (Cross-Architecture Proof-of-Concept), Table 2; Limitations §"Capability-gap analysis"
- 问题：论文声称 combo gain 与 capability gap 单调递增（Spearman ρ=1.0, p=0.003, n=6），但 6 个条件中 4 个共享同一 DeBERTa verifier。Limitations 中的 verifier-collapsed 分析（仅 3 个独立 verifier）p 值降至 0.167，不显著。同时，process-κ gradient（Appendix Table 16）也只有 n=5 个数据点，任何 5 点的单调排列都会给出 ρ=±1.0。这两个核心分析的样本量都不足以支撑因果性声称。
- 为什么影响接收：Empirical Finding 2 和 §6 的结论（"cross-architecture escape works when verifier exceeds generator"）是论文最重要的正面贡献。如果证据基础不足，论文就仅剩负面结果部分，学术价值减半。
- 建议修改方向：(1) 增加更多 NLI verifier 架构（如 ELECTRA-NLI、T5-NLI），使独立 verifier 数量 ≥5；(2) 降低 Finding 2 的措辞强度——从 "monotonically increasing" 改为 "consistent empirical pattern"（实际上 Limitations 已经这样说了，但正文 §6 和 abstract 仍然用了强措辞）；(3) 报告 bootstrap 或 permutation test 而非仅 Spearman。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Bias Ratio 的定义可能存在循环论证
- 具体位置：Section 3.3, Eq. 5
- 问题：BR(M,T) = P(c supports a_M | a_M ≠ a*) / P(c supports a* | a_M ≠ a*)。但论文同时指出约束与 source trace 高度耦合：56.4% 的约束与其他答案的约束零变量重叠（Section 5.2）。这意味着从 trace_i 提取的约束几乎按定义"支持" trace_i 的答案。BR 高（4.97×）可能部分是提取设计的产物（约束绑定 trace→答案），而非模型偏差的独立证据。论文需要更清楚地区分"约束继承了 trace 的答案方向"（设计产物）和"约束独立验证了模型的偏差方向"（实质发现）。
- 建议：(1) 定义 "supports" 的操作化标准（是 trace-level 还是 Z3 semantics-level）；(2) 报告一个控制实验：如果随机打乱约束-trace 映射后 BR 是多少？这能量化 BR 中"设计产物"成分的比例。

**W2** [warning] CIL 名称和 information-theoretic 声称有误导
- 具体位置：Section 5.4, Eq. 7; Appendix D
- 问题：CIL(V,G) = log₂ [P(V correct | G wrong) / P(V correct | G correct)] 被称为 "Cumulative Information Lift"，暗示信息论基础。但这实际上是一个条件概率的对数比（log-odds ratio），不是互信息、KL 散度或任何标准信息论量。使用 log₂ 和 "bits" 单位进一步强化了这个误导。此外，"Cumulative" 一词没有在定义中体现——它不是对什么的累积。
- 建议：重命名为更准确的名称（如 "Corrective Signal Ratio" 或 "Conditional Accuracy Ratio"），或者提供严格的信息论推导证明这确实是某种信息量度。

**W3** [warning] Frontier 模型的 SCB 评估使用了不同的实验范式
- 具体位置：Table 15 (Appendix); Limitations §"Scale and language"
- 问题：开源模型使用自提取（模型从自己的 trace 中提取约束），而 frontier 模型使用跨模型提取（Mistral-7B 从 frontier trace 中提取）。论文声称 "SCB universality (BR 1.66–4.97×)"（Section 7, Introduction contribution 1），但跨模型提取的 BR 反映的是 Mistral-7B 的提取偏差+目标模型的 trace 偏差的混合，不是纯粹的自提取偏差。这两种范式的 BR 不能直接比较。
- 建议：(1) 在声称 "SCB universality" 时明确区分自提取和跨模型提取两类 BR；(2) 讨论跨模型提取 BR 可能高估或低估自提取 BR 的原因。

**W4** [warning] 27 策略中缺失最有可能成功的方向——训练式约束提取器
- 具体位置：Section 5.6 (Remediation Analysis); Conclusion
- 问题：论文测试了 27 种修复策略，但明确排除了在 oracle 数据上微调约束提取器这一方向。oracle 控制显示 +29.90pp 的提升空间，论文也承认这是 "most promising future direction"。排除这个最有前途的方向后声称 "27 strategies all fail" 有些误导——这像是在说 "我们试了所有方法都不行"，但实际上跳过了最可能有效的方法。
- 建议：(1) 在 abstract/introduction 中明确 27 strategies 是 "prompt-level and architecture-level zero-shot strategies"，不包括 fine-tuned extractors；(2) 更突出地讨论 fine-tuned extractor 作为 open question。

**W5** [warning] Effective-K (Eq.1) 用 Fleiss' κ 替代 ICC 的验证不充分
- 具体位置：Section 3.1, Eq. 1
- 问题：Kish design effect 公式原始形式使用 ICC (ρ)，但论文用 Fleiss' κ 替代。验证是 "mean pairwise r = 0.625 across model families" 的单调关系。但 r=0.625 只是中等相关，而且 Fleiss' κ 测量的是名义分类的一致性，ICC 测量的是连续/有序数据的类内相关。两者在理论上测量不同的东西。论文说 K_eff "should be interpreted as an ordinal diagnostic"，但正文多处（Introduction §1, Discussion §7）将其作为字面有效样本量使用（如 "traces beyond a dozen add negligible independent information"）。
- 建议：(1) 始终明确 K_eff 是序数诊断指标，避免 "effective sample size" 的字面解读；(2) 报告 ICC 本身作为参考。

---

## 小问题（不影响接收）

- Section 3.2, Eq.3: scoring 函数中 σ(c,a) = 1 "if c was extracted from any trace producing answer a"——这使得 score 本质上等于按 answer 分组的加权 vote count，弱化了 MAX-SAT 的理论价值。建议在正文讨论这一点（目前仅在 Appendix I ablation 中体现）。
- Table 1: GSM8K n=30 和 AIME n=22 样本量极小，放在主表中可能给读者错误的统计印象。建议移至 appendix 或标注更显著。
- Section 4.1: "McNemar exact test (α=0.05); 95% bootstrap CIs (10,000 resamples) for n ≥ 200"——n<200 的条件没有 CI，但主文没有明确说明。
- Figure 2: 27 个策略的条形图很有用，但无法看出每个策略的 p 值或置信区间。建议添加显著性标记。
- Appendix B/C: prompt template 披露完整，有助于复现，这是优点。
- 正文第 8 页末的 "Conclusion" 仅 4 行，对一篇 26 页的论文来说过于简短。建议扩展讨论 implications。
- FOLIO n=204 中 gold annotation 包含 "Unknown" 类别，在 FOL 形式化中如何处理 open-world semantics 的 Unknown？论文未明确说明。

---

## Questions（需要作者回答）

**Q1**: 如果随机打乱约束与 source-trace 的映射关系（即约束不再绑定产生它们的 trace），BR 会变成多少？这能帮助区分 "约束内容偏差" vs. "约束-答案耦合的设计产物"。

**Q2**: 论文报告 99.0% 的约束在 Z3 层面是命题逻辑的，仅 1.0% 使用量词。如果模型能生成更丰富的一阶逻辑约束（如量化推理），BR 和 SICA 效果是否可能改变？作者是否尝试过引导模型生成非命题约束？

**Q3**: Oracle 控制仅在 FOLIO 和 ProofWriter 上进行（有 gold annotation）。对于 LogiQA 等无 gold annotation 的数据集，如何确认 SICA 失败是因为约束质量而非机制本身？

**Q4**: DRC 的阈值 τ=0.7 在 ProofWriter 上选择并在 FOLIO 上验证。如果反过来（FOLIO 上选择 τ），最优 τ 是否相同？DRC 对 τ 的敏感性如何？

**Q5**: 4-seed 复制中，seed 对 Δ 的影响（+3.43 到 -0.49pp）大于大多数条件的 Δ 本身。作者是否考虑过种子方差可能在其他条件中同样存在，从而使 Table 1 中的单 seed 结果基本不可解释？

---

## 主要优势

- **范围广泛**：11 个模型（7B 到 frontier）、6 个数据集、27 种修复策略、4-seed 复制——对负面结果论文来说覆盖面非常出色。
- **Oracle 控制设计精巧**：通过 gold annotation 控制清晰地将瓶颈定位到自提取环节（+29.90pp oracle vs. +3.43pp self-extracted），是本文最有说服力的实验。
- **诊断框架有实用价值**：C₀ 诊断（< 5% 意味着 SICA 退化为 SC）、三类 failure mode（Type A/B/C）、process-level 独立性分析——这些工具对后续研究有参考价值。
- **诚实的局限性披露**：论文在 Limitations 中详细讨论了统计功效、单 seed、capability-gap 分析的弱点，这种透明性值得肯定。
- **建设性逃逸路径**：不仅报告负面结果，还提出跨架构 NLI + DRC 作为实际可行的方向，使论文从纯负面变为有建设性。
- **BH 多重比较校正**使用恰当，TOST 等价性检验和 margin sensitivity 分析是良好的统计实践。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1282 · 2026-05-22T01:08:32.552335+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 1283 · 2026-05-22T01:08:38.379638+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：我以 Reviewer 1 身份完成了对论文 "Beyond Self-Consistency" 的全面审查，聚焦方法严谨性、实验设计、统计分析和可复现性四个维度。

**Overall 评分：3.5（Borderline Conference）**

三个 Must-Fix 问题：
1. **统计功效 <21%** 无法支撑 "无效果" 的核心结论——这是负面结果论文的根基问题
2. **单 seed 复制** 导致大多数条件的结果可靠性存疑（4-seed 复制显示 ~4pp 跨 seed 波动）
3. **Capability-gap 分析** 证据薄弱（n=6, 4/6 共享 verifier, collapsed 分析 p=0.167）

五个 Should-Fix 问题涉及 Bias Ratio 可能的循环论证、CIL 名称误导、frontier 模型评估范式不一致、缺失训练式提取器评估、以及 K_eff 公式验证不充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1284 · 2026-05-22T01:08:56.199224+00:00_

收到 Reviewer 1 的审稿意见。等待 Reviewer 2 完成后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 81

## Round 81

6 recorded events


### User

_source line 1285 · 2026-05-22T01:10:19.538293+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning from 7B to Frontier Scale"
**Venue**: EMNLP 2026 Main (via ARR)
**审查侧重**: 新颖性 + 定位 + Related Work 完整性 + 写作质量 + 格式合规

---

## 总体评分

**Overall Assessment**: 3.0 / 5 (Findings)
**一句话总结**: 实验设计扎实、诊断体系完整的负面结果论文，但核心发现（自提取信号继承模型偏差）在现有 self-correction failure 文献基础上新颖性增量有限，正面贡献（DRC、cross-architecture escape）偏弱，整体达到 Findings 水平。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论严谨（oracle controls、4-seed replication、TOST equivalence tests、27种修复策略），但部分统计检验 underpowered（McNemar power <21% at n=200），正面贡献的证据基础偏窄（n=6 verifier-generator pairs，4/6 共用同一 verifier） |
| Excitement | 2.5/5 | 核心负面结果（自提取约束继承模型偏差）在 Huang et al. 2024、Stechly et al. 2025 的基础上可预期；CJT 框架和量化诊断有价值但属于 expected application；DRC 过于简单 |
| Reproducibility | 4/5 | 实验细节充分（模型版本、超参数、数据集大小均明确），承诺开源代码和数据，oracle 控制实验设计良好 |
| Confidence | 4/5 | 熟悉 LLM reasoning、self-consistency、neuro-symbolic 方法文献，仔细阅读了全文及 18 页附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **核心新颖性不足——"Symbolic Confirmation Bias" 与已有 self-correction failure 文献的区分不够清晰**

- 具体位置：Section 1 (Introduction, 第24行), Section 2 (Related Work, CJT and positioning 段落), Section 5.2
- 问题：论文将 SCB 定义为"自提取的形式化约束继承生成模型的分布偏差"。但 Huang et al. (2024) 已经证明 "LLMs cannot self-correct reasoning without external feedback"，Stechly et al. (2025) 证明 self-verification 在 reasoning/planning 上不可靠，Wan et al. (2025) 和 Jhaveri et al. (2026) 直接研究了 CoT confirmation bias。论文在 Related Work §2 最后一段声称 "SCB is distinct from CoT unfaithfulness and CoT-level confirmation bias: the latter concern whether stated reasoning reflects actual computation, while SCB concerns whether self-extracted formal constraints mirror the model's answer distribution"——但这个区分本质上只是**同一机制（自生成信号继承模型偏差）在不同载体（自然语言 vs FOL 约束）上的实例化**。Z3 验证通道的 provable soundness 确实是一个有趣的切入点（证明瓶颈在提取而非验证），但这更接近一个实验发现而非概念突破。
- 为什么影响接收：对于负面结果论文，如果核心发现可以从已有文献中合理预期（给定 Huang 2024 + Stechly 2025 的结论，自提取 FOL 约束同样失败是 expected outcome），则学术贡献主要在于量化深度而非发现本身。当前 framing 将 SCB 作为"新发现"（Contribution 1）过度抬高了新颖性。
- 建议修改方向：(1) 明确承认 SCB 是 self-correction failure 的一个特定实例，降低 novelty claim 的调门；(2) 重新定位贡献重心为**量化诊断体系**（K_eff, BR, C_0, CIL）和**实验规模**（27 策略全部失败的系统性证伪），而非"新现象的发现"；(3) 强化论证 formal verification channel 下 SCB 的 non-obvious 之处——例如，99% 的约束通过 Z3 语法检查却仍然无用，这一点比 SCB 本身更有趣，应当在 framing 中更突出。

**N2** [critical] **标题 overclaiming——"Do Not Improve ... from 7B to Frontier Scale" 但 frontier 模型实验设计不支持 self-extraction 结论**

- 具体位置：Title, Section 4.1 (Experiments Setup), Table 15 (Appendix, frontier SCB)
- 问题：标题声称 "from 7B to Frontier Scale" 的约束不 improve reasoning。但对 frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro），论文使用的是 **cross-model extraction**（Mistral-7B 提取约束应用于 frontier 模型的 trace），而非 self-extraction，原因是 "closed-source APIs do not expose internal traces"（Limitations §Z.1）。这意味着 frontier 实验测量的是 **cross-model** SCB（Mistral-7B 的偏差投射到 frontier traces 上），而非 frontier 模型的 **self-extraction** SCB。标题中 "Self-Extracted" 修饰的是 "Symbolic Constraints"，但 frontier 实验并非 self-extraction。
- 为什么影响接收：标题是论文最核心的 claim。如果 frontier 结果基于 cross-model extraction 而非 self-extraction，那么 "from 7B to Frontier Scale" 这一范围声明对 self-extraction 不成立。Reviewer 和读者会认为这是 overclaiming。
- 建议修改方向：(1) 修改标题，去掉 "to Frontier Scale" 或加限定词（如 "from 7B to 32B, with Cross-Model Evidence at Frontier Scale"）；(2) 在 Abstract 和 Introduction 中更明确地区分 self-extraction（7B-32B 开源模型）和 cross-model extraction（frontier 模型）的实验范围。

**N3** [critical] **四个 contributions 中 DRC（Contribution 4）作为独立贡献不够充分**

- 具体位置：Introduction Contribution 4, Section 6.1, Table 24 (Appendix)
- 问题：DRC 本质上是基于 trace agreement 阈值 τ 的 confidence-based routing：高一致时用 SC，低一致时调用外部 NLI verifier。这是一个极其标准的 cascade/routing 设计（类似 speculative decoding 中的 confidence threshold），不构成方法论创新。在 n=6 verifier-generator pairs（其中 4/6 共用同一 DeBERTa verifier）上验证 τ=0.7 的 generalization，样本量也不足以支撑 "Pareto-efficient" 的强宣称。
- 为什么影响接收：将一个 trivial routing rule 提升为四大贡献之一，与前三个实质性贡献并列，削弱了论文的整体贡献质量。如果 reviewer 期望每个 contribution 都有足够深度，DRC 会成为弱点。
- 建议修改方向：(1) 将 DRC 降级为 Section 6 的 practical observation / ablation，不作为独立 contribution 编号；(2) 或者增加更多的 routing 策略对比（entropy-based、calibrated probability-based 等），使 DRC 成为一个更完整的 contribution。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Independence-Accuracy Trade-off（Contribution 2）的 framing 问题**

- 具体位置：Introduction Contribution 2, Section 5.1-5.2
- 问题：论文声称 "Rather than discovering a new diversity-accuracy tradeoff (Krogh and Vedelsby, 1994), we quantify its specific form in LLM self-extraction via three diagnostics"。但 K_eff 本质上是 Kish (1965) design effect 的直接应用（用 κ 替代 ICC），BR 是条件概率比，C_0 是一个 zero-cost filter。这些诊断工具各自简单且直观，它们的价值在于组合应用到 LLM 自提取场景，而非方法论本身的新颖性。当前 framing 暗示这是一个独立贡献，但实际上它更像是 Contribution 1（SCB）的量化工具集。
- 建议：将 Contribution 2 重新措辞为 "量化诊断工具集"，降低 "trade-off" 的发现性措辞。

**W2** [warning] **CIL（Cumulative Information Lift）的理论贡献被高估**

- 具体位置：Section 5.4, Appendix D
- 问题：CIL 定义为 log₂(P(V correct | G wrong) / P(V correct | G correct))——本质上是一个 log-odds ratio，衡量 verifier 在 generator 出错时的纠正率 vs 正确时的确认率。论文称其 "unify the preceding diagnostics" 并报告与 combo gain 的 Spearman ρ=0.881。但 (1) CIL 是 post-hoc 定义的，仅在 8 个 verifier-generator pairs 上计算，且这些 pairs 并非独立（共享 generator 或 verifier）；(2) "unify" 的说法过强——CIL 与 K_eff、BR 之间没有推导出的数学关系，只是经验相关；(3) 在如此小的样本上，ρ=0.881 可能受 outlier 影响。
- 建议：将 CIL 定位为 "empirical diagnostic"，删除 "unify" 的措辞，添加 leave-one-out sensitivity analysis。

**W3** [warning] **Cross-architecture escape 的证据基础偏窄**

- 具体位置：Section 6, Table 2, Limitations
- 问题：Cross-architecture NLI 仅在 ProofWriter（premise-conclusion 结构天然适配 NLI）上显著有效（+6.67pp, p<0.001）。FOLIO 上 +2.94pp 不显著，LogiQA 上 ≤+1pp 不显著。Capability-gap 分析基于 n=6 pairs，其中 4/6 共用同一 DeBERTa verifier；verifier-collapsed analysis（n=3 独立 verifier）的 p=0.167 不显著。Limitations 节已承认这一点，但 Introduction 和 Conclusion 中仍以 "p=0.003" 呈现，可能给读者留下比实际更强的印象。
- 建议：(1) 在 Introduction/Conclusion 引用 p=0.003 时，添加 caveat 说明这包含 shared verifier 的 non-independence；(2) 报告 verifier-collapsed p=0.167 作为 robustness check。

**W4** [warning] **Figure 2（27 intervention strategies 汇总图）placement 问题**

- 具体位置：Figure 2 出现在 PDF 第 25 页，但在 Section 5.6（第 7 页正文）中引用
- 问题：这张图是论文 "27 种策略全部失败" 核心论点的视觉支撑，但被 LaTeX float 机制推到了附录之后（第 25 页）。在审稿时，reviewer 需要在正文和附录之间来回翻页，影响阅读体验。
- 建议：调整 LaTeX placement（如用 [h!] 或手动 \clearpage），确保 Figure 2 出现在 Section 5.6 附近的正文页面。

**W5** [warning] **Appendix 体量过大，关键信息分配不合理**

- 具体位置：Appendix A-Z（约 18 页）
- 问题：主文 8 页 vs 附录 ~18 页。部分重要内容（如 frontier model SCB Table 15、K_eff 详细分析 Table 18、cross-model kappa Table 19）被放在附录中，但这些是支撑核心论点的关键证据。同时，主文中有些内容可以压缩（如 Section 7 Discussion 与 Section 8 Conclusion 可以合并）。
- 建议：(1) 合并 Discussion 和 Conclusion 为一个 section，节省 ~0.3 页空间；(2) 将 frontier SCB 结果（Table 15）移入正文，因为 "从 7B 到 frontier" 是标题级 claim。

---

## 小问题（不影响接收）

1. **"Symbolic Mirage Hypothesis" 命名偏 dramatic**：这个名字暗示了一种"幻觉"般的现象，但实际上 self-extracted constraints 不是"海市蜃楼"——它们确实是有效的 FOL 约束（99% 通过 Z3 语法检查），只是继承了模型偏差。"Symbolic Bias Inheritance" 或 "Extraction Bias Hypothesis" 可能更准确。

2. **Orphan bib entry**: `brown2005diversity`（"Diversity Creation Methods: A Survey and Categorisation"）在 .bib 中但未被引用。应删除或引用。

3. **Abstract 信息密度偏高**：在一个段落中包含了 BR=4.97×、K_eff、C_0、27 种策略、cross-architecture escape、DRC 等大量数字和概念。建议精简数字，保留核心 message。

4. **\looseness=-1 大量使用**：正文中几乎每段都有 \looseness=-1，这是空间紧凑的信号，但不影响审稿。

5. **Neuro-symbolic 三分类法（Specification-generation / Program-generation / Trace-extraction）**：这是论文自己提出的分类，"Trace-extraction" 类别目前只包含本文的 SICA。建议在 Related Work 中承认这一分类是本文的组织框架而非 established taxonomy。

6. **数学符号一致性**：主文中 $C_0$ 和 $C_D$ 似乎指代同一概念（multi-candidate rate），但在不同 sections 中交替使用（Introduction 用 $C_0$，CIL 部分提到 $C_D$）。需确认并统一。

---

## 主要优势

1. **实验规模和系统性出色**：6 个开源模型 + 5 个 frontier 模型、3 个推理数据集、27 种修复策略、4-seed replication、TOST equivalence tests——这是一个 thorough 的负面结果论证，实验设计的严谨程度值得肯定。

2. **Oracle control 设计精妙**：用 FOLIO/ProofWriter 的 gold FOL annotations 替换自提取约束，展示 +29.90pp/+17.17pp 的增益，精确定位瓶颈在 extraction 而非 MAX-SAT/Z3 mechanism。这是论文最有说服力的部分。

3. **CJT 框架提供了清晰的理论语言**：用 Condorcet Jury Theorem 的 independence assumption 来解释 SC 的 plateau 和 SICA 的失败，比纯经验描述更有洞察力。K_eff 作为 ordinal diagnostic 的定位也恰当。

4. **Related Work 覆盖面广**：涵盖了 2024-2026 的最新工作，包括 concurrent work (Kuai et al. 2026)，neuro-symbolic 方法的三分类法虽是自创但组织清晰。与 Huang 2024、Stechly 2025、Wan 2025 的对比虽可以更深入，但已给出明确的区分论证。

5. **Limitations 节全面且诚实**：明确承认了统计 power 不足、single-seed 问题、capability-gap 分析的 verifier-collapsed p=0.167、计算成本等局限性，展现了良好的学术诚信。

---

## Questions（需要作者回答）

1. **关于 frontier self-extraction**: 是否有可能通过 API 的 logprobs 或 structured output 功能对 frontier 模型进行真正的 self-extraction 实验（即使无法获取 CoT traces）？如果不能，标题中 "to Frontier Scale" 的依据是什么？

2. **关于 trained extractors**: 论文承认 "we do not evaluate trained constraint extractors" (Section 5.6)。如果用 oracle annotations 微调一个小模型作为 extractor，SCB 是否会消失？这个 gap 是否构成本文最重要的 limitation？

3. **CIL 与 combo gain 的相关性**: ρ=0.881 在 n=8 上是否做过 bootstrap CI？如果去掉最强的 pair（Mistral-7B + DeBERTa on ProofWriter），相关性是否仍然成立？

4. **关于 Figure 2 中 Debate 的 -18.6pp**: 这个极端负面结果的原因是什么？是因为 debate 生成了更多样但更低质量的约束，还是 debate 本身降低了推理质量？

---

## 建议的 Overall Assessment

**Overall: 3.0 (Findings)**

理由：论文的实验工作量和方法论严谨程度值得肯定（Soundness 3.5），但核心发现的新颖性有限——"自生成信号继承模型偏差"在 self-correction failure 文献基础上是 expected outcome，贡献主要在量化深度而非新发现。正面贡献（DRC、cross-architecture escape）证据基础偏窄。建议作为 Findings paper 接收，条件是：(1) 修改标题避免 frontier overclaiming；(2) 降低 SCB 的 "新发现" 调门；(3) 将 DRC 从独立贡献降级。

**Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-22T01:11:08.519674+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**审查侧重**: 新颖性 + 定位 + Related Work 完整性 + 写作质量 + 格式合规\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心新颖性不足——\"Symbolic Confirmation Bias\" 与已有 self-correction failure 文献的区分不够清晰\n- SCB 定义为\"自提取的形式化约束继承生成模型的分布偏差\"。但 Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback，Stechly et al. (2025) 证明 self-verification 不可靠，Wan et al. (2025) / Jhaveri et al. (2026) 直接研究 CoT confirmation bias。SCB 只是同一机制在不同载体（自然语言 vs FOL 约束）上的实例化。Z3 验证通道的 provable soundness 是有趣切入点，但更接近实验发现而非概念突破。\n- 建议：降低 novelty claim 调门，重新定位贡献重心为量化诊断体系和实验规模。\n\n**N2** [critical] 标题 overclaiming——\"Do Not Improve ... from 7B to Frontier Scale\" 但 frontier 模型用 cross-model extraction 而非 self-extraction\n- frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro）使用 Mistral-7B 做跨模型提取，不是 self-extraction。标题中 \"Self-Extracted\" 修饰 \"Symbolic Constraints\"，但 frontier 实验并非 self-extraction。\n- 建议：修改标题去掉 \"to Frontier Scale\" 或加限定词。\n\n**N3** [critical] DRC（Contribution 4）作为独立贡献不够充分\n- DRC 本质是基于 trace agreement 阈值 τ 的 confidence-based routing，极其标准的 cascade 设计。在 n=6 pairs 上验证不足以支撑 \"Pareto-efficient\" 宣称。\n- 建议：降级为 Section 6 的 practical observation，不作为独立 contribution。\n\n### Should-Fix 问题\n\n**W1** Independence-Accuracy Trade-off（Contribution 2）的 framing：K_eff 是 Kish design effect 的直接应用，BR 是条件概率比，C_0 是 zero-cost filter——各自简单直观，价值在组合应用而非方法论创新。更像 Contribution 1 的量化工具集。\n\n**W2** CIL 理论贡献被高估：post-hoc 定义、仅 8 个 pairs（非独立）、\"unify\" 过强。\n\n**W3** Cross-architecture escape 证据偏窄：仅 ProofWriter 显著，FOLIO/LogiQA 不显著；verifier-collapsed p=0.167。\n\n**W4** Figure 2 placement 问题：被推到第 25 页但在第 7 页引用。\n\n**W5** Appendix 体量过大（~18页），关键信息分配不合理（如 frontier SCB Table 15 应在正文）。\n\n### 小问题\n1. \"Symbolic Mirage Hypothesis\" 命名偏 dramatic，\"Symbolic Bias Inheritance\" 可能更准确\n2. Orphan bib entry: brown2005diversity 未被引用\n3. Abstract 信息密度偏高\n4. \\looseness=-1 大量使用\n5. Neuro-symbolic 三分类法是自创分类，应承认\n6. $C_0$ 和 $C_D$ 符号不一致\n\n### Questions\n1. frontier 模型能否通过 API logprobs/structured output 做真正的 self-extraction？\n2. 用 oracle annotations 微调小模型作为 extractor，SCB 是否会消失？\n3. CIL ρ=0.881 在 n=8 上的 bootstrap CI？去掉最强 pair 后是否成立？\n4. Debate -18.6pp 的原因——约束质量还是推理质量？\n\n### 主要优势\n1. 实验规模和系统性出色\n2. Oracle control 设计精妙\n3. CJT 框架提供清晰理论语言\n4. Related Work 覆盖面广\n5. Limitations 全面诚实\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**审查侧重**: 新颖性 + 定位 + Related Work 完整性 + 写作质量 + 格式合规\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心新颖性不足——\"Symbolic Confirmation Bias\" 与已有 self-correction failure 文献的区分不够清晰\n- SCB 定义为\"自提取的形式化约束继承生成模型的分布偏差\"。但 Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback，Stechly et al. (2025) 证明 self-verification 不可靠，Wan et al. (2025) / Jhaveri et al. (2026) 直接研究 CoT confirmation bias。SCB 只是同一机制在不同载体（自然语言 vs FOL 约束）上的实例化。Z3 验证通道的 provable soundness 是有趣切入点，但更接近实验发现而非概念突破。\n- 建议：降低 novelty claim 调门，重新定位贡献重心为量化诊断体系和实验规模。\n\n**N2** [critical] 标题 overclaiming——\"Do Not Improve ... from 7B to Frontier Scale\" 但 frontier 模型用 cross-model extraction 而非 self-extraction\n- frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro）使用 Mistral-7B 做跨模型提取，不是 self-extraction。标题中 \"Self-Extracted\" 修饰 \"Symbolic Constraints\"，但 frontier 实验并非 self-extraction。\n- 建议：修改标题去掉 \"to Frontier Scale\" 或加限定词。\n\n**N3** [critical] DRC（Contribution 4）作为独立贡献不够充分\n- DRC 本质是基于 trace agreement 阈值 τ 的 confidence-based routing，极其标准的 cascade 设计。在 n=6 pairs 上验证不足以支撑 \"Pareto-efficient\" 宣称。\n- 建议：降级为 Section 6 的 practical observation，不作为独立 contribution。\n\n### Should-Fix 问题\n\n**W1** Independence-Accuracy Trade-off（Contribution 2）的 framing：K_eff 是 Kish design effect 的直接应用，BR 是条件概率比，C_0 是 zero-cost filter——各自简单直观，价值在组合应用而非方法论创新。更像 Contribution 1 的量化工具集。\n\n**W2** CIL 理论贡献被高估：post-hoc 定义、仅 8 个 pairs（非独立）、\"unify\" 过强。\n\n**W3** Cross-architecture escape 证据偏窄：仅 ProofWriter 显著，FOLIO/LogiQA 不显著；verifier-collapsed p=0.167。\n\n**W4** Figure 2 placement 问题：被推到第 25 页但在第 7 页引用。\n\n**W5** Appendix 体量过大（~18页），关键信息分配不合理（如 frontier SCB Table 15 应在正文）。\n\n### 小问题\n1. \"Symbolic Mirage Hypothesis\" 命名偏 dramatic，\"Symbolic Bias Inheritance\" 可能更准确\n2. Orphan bib entry: brown2005diversity 未被引用\n3. Abstract 信息密度偏高\n4. \\looseness=-1 大量使用\n5. Neuro-symbolic 三分类法是自创分类，应承认\n6. $C_0$ 和 $C_D$ 符号不一致\n\n### Questions\n1. frontier 模型能否通过 API logprobs/structured output 做真正的 self-extraction？\n2. 用 oracle annotations 微调小模型作为 extractor，SCB 是否会消失？\n3. CIL ρ=0.881 在 n=8 上的 bootstrap CI？去掉最强 pair 后是否成立？\n4. Debate -18.6pp 的原因——约束质量还是推理质量？\n\n### 主要优势\n1. 实验规模和系统性出色\n2. Oracle control 设计精妙\n3. CJT 框架提供清晰理论语言\n4. Related Work 覆盖面广\n5. Limitations 全面诚实\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-22T01:11:41.628121+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33108
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-22T01:11:41.779404+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析 + 可复现性\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 统计功效不足以支撑\"SICA 无效果\"的核心结论\n- McNemar 在 n=200-600 下检测 |Δ|=2pp 的功效 <21%。最大研究 MDE=1.86pp，观测 Δ=+0.25pp。16个非退化条件中10个 TOST \"underpowered\"。Abstract \"we find no evidence of improvement\" 将\"检测不到效果\"等同于\"没有效果\"。\n- 建议：使用更审慎措辞、报告可排除的效应大小范围、增加 seed。\n\n**N2** [critical] 单 seed 复制严重不足\n- Table 1 大多数条件仅单 seed。唯一 4-seed 复制（Mistral-7B FOLIO）Δ 范围 +3.43 到 -0.49pp（跨度 ~4pp）。温度敏感性也显示 T=0.7 是\"孤立峰\"。单 seed 条件的可靠性存疑。\n- 建议：至少对 3-4 个关键条件做 4-seed 复制。\n\n**N3** [critical] Capability-gap 分析证据过于薄弱\n- Spearman ρ=1.0, p=0.003, 但 n=6 且 4/6 共享 DeBERTa verifier。Verifier-collapsed 分析 p=0.167。Process-κ gradient 也只有 n=5。\n- 建议：增加更多 NLI verifier 架构、降低措辞强度、报告 bootstrap/permutation test。\n\n### Should-Fix 问题\n\n**W1** Bias Ratio 可能存在循环论证：56.4% 约束零变量重叠，约束几乎按定义\"支持\"source trace 的答案。BR 高可能部分是提取设计的产物。建议做控制实验（随机打乱约束-trace 映射后 BR 是多少）。\n\n**W2** CIL 名称和 information-theoretic 声称有误导：实际是 log-odds ratio，不是互信息/KL 散度。\"Cumulative\" 无体现。建议重命名。\n\n**W3** Frontier 模型 SCB 评估使用不同实验范式：self-extraction vs cross-model extraction 的 BR 不可直接比较。\n\n**W4** 27 策略缺失最有可能成功的方向——训练式约束提取器。Oracle +29.90pp 但排除了最有前途的方向后声称 \"all fail\" 有误导。\n\n**W5** K_eff 用 κ 替代 ICC 验证不充分：r=0.625 只是中等相关，κ 和 ICC 理论上测量不同东西。\n\n### 小问题\n- Eq.3 scoring 函数本质等于按答案分组的加权 vote count\n- GSM8K n=30, AIME n=22 放主表可能误导\n- n<200 条件无 CI 但未说明\n- Figure 2 无 p 值/CI\n- Conclusion 过于简短（4行）\n- FOLIO Unknown 类在 FOL 中如何处理未说明\n\n### Questions\nQ1: 随机打乱约束-trace 映射后 BR 变化？\nQ2: 引导模型生成非命题约束是否改善？\nQ3: 无 gold annotation 数据集如何确认失败原因？\nQ4: DRC τ=0.7 的敏感性？\nQ5: seed 方差是否使 Table 1 单 seed 结果不可解释？\n\n### 主要优势\n1. 范围广泛（11模型、6数据集、27策略）\n2. Oracle 控制设计精巧\n3. 诊断框架有实用价值\n4. 诚实的局限性披露\n5. 建设性逃逸路径\n6. BH 校正和 TOST 使用恰当\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：用 [AGREE] 表示同意并说明理由，或用 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析 + 可复现性\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 统计功效不足以支撑\"SICA 无效果\"的核心结论\n- McNemar 在 n=200-600 下检测 |Δ|=2pp 的功效 <21%。最大研究 MDE=1.86pp，观测 Δ=+0.25pp。16个非退化条件中10个 TOST \"underpowered\"。Abstract \"we find no evidence of improvement\" 将\"检测不到效果\"等同于\"没有效果\"。\n- 建议：使用更审慎措辞、报告可排除的效应大小范围、增加 seed。\n\n**N2** [critical] 单 seed 复制严重不足\n- Table 1 大多数条件仅单 seed。唯一 4-seed 复制（Mistral-7B FOLIO）Δ 范围 +3.43 到 -0.49pp（跨度 ~4pp）。温度敏感性也显示 T=0.7 是\"孤立峰\"。单 seed 条件的可靠性存疑。\n- 建议：至少对 3-4 个关键条件做 4-seed 复制。\n\n**N3** [critical] Capability-gap 分析证据过于薄弱\n- Spearman ρ=1.0, p=0.003, 但 n=6 且 4/6 共享 DeBERTa verifier。Verifier-collapsed 分析 p=0.167。Process-κ gradient 也只有 n=5。\n- 建议：增加更多 NLI verifier 架构、降低措辞强度、报告 bootstrap/permutation test。\n\n### Should-Fix 问题\n\n**W1** Bias Ratio 可能存在循环论证：56.4% 约束零变量重叠，约束几乎按定义\"支持\"source trace 的答案。BR 高可能部分是提取设计的产物。建议做控制实验（随机打乱约束-trace 映射后 BR 是多少）。\n\n**W2** CIL 名称和 information-theoretic 声称有误导：实际是 log-odds ratio，不是互信息/KL 散度。\"Cumulative\" 无体现。建议重命名。\n\n**W3** Frontier 模型 SCB 评估使用不同实验范式：self-extraction vs cross-model extraction 的 BR 不可直接比较。\n\n**W4** 27 策略缺失最有可能成功的方向——训练式约束提取器。Oracle +29.90pp 但排除了最有前途的方向后声称 \"all fail\" 有误导。\n\n**W5** K_eff 用 κ 替代 ICC 验证不充分：r=0.625 只是中等相关，κ 和 ICC 理论上测量不同东西。\n\n### 小问题\n- Eq.3 scoring 函数本质等于按答案分组的加权 vote count\n- GSM8K n=30, AIME n=22 放主表可能误导\n- n<200 条件无 CI 但未说明\n- Figure 2 无 p 值/CI\n- Conclusion 过于简短（4行）\n- FOLIO Unknown 类在 FOL 中如何处理未说明\n\n### Questions\nQ1: 随机打乱约束-trace 映射后 BR 变化？\nQ2: 引导模型生成非命题约束是否改善？\nQ3: 无 gold annotation 数据集如何确认失败原因？\nQ4: DRC τ=0.7 的敏感性？\nQ5: seed 方差是否使 Table 1 单 seed 结果不可解释？\n\n### 主要优势\n1. 范围广泛（11模型、6数据集、27策略）\n2. Oracle 控制设计精巧\n3. 诊断框架有实用价值\n4. 诚实的局限性披露\n5. 建设性逃逸路径\n6. BH 校正和 TOST 使用恰当\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-22T01:11:43.342072+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1562
}
```

</details>

---


### Assistant

_source line 1290 · 2026-05-22T01:11:47.152147+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 82

## Round 82

2 recorded events


### User

_source line 1291 · 2026-05-22T01:11:49.790516+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心评判**：Overall 3.0 (Findings level)。

三个 Must-Fix：
1. **新颖性**——SCB 本质上是 self-correction failure 的 FOL 实例化，与 Huang 2024 / Stechly 2025 的区分不够清晰，当前 framing 过度抬高了"新发现"的调门
2. **标题 overclaiming**——"to Frontier Scale" 但 frontier 实验用的是 cross-model extraction 而非 self-extraction
3. **DRC 贡献过弱**——简单的 threshold routing 不应作为四大贡献之一

主要优势：实验规模出色（27 策略全部失败的系统性证伪）、oracle control 设计精妙、CJT 框架提供了清晰的理论语言、Limitations 节诚实全面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1292 · 2026-05-22T01:11:59.430983+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 1293 · 2026-05-22T01:13:20.052173+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R2-N1: SCB 与已有 self-correction failure 文献的区分不够清晰**

同意 R2 的核心判断。SCB 确实可以视为 Huang et al. (2024) self-correction failure 在形式化约束载体上的实例化。论文 Introduction（§1, para 4）试图通过 "provably sound formal channel (Z3)" 来区分，论点是 Z3 验证通道本身是可靠的，所以失败可精确定位到提取步骤——这比自然语言 self-correction 的归因更清晰。但这是一个实验性区分，而非概念性突破。

不过，我认为 R2 略有低估论文的量化贡献：(1) BR=4.97× 是对 bias 程度的首次精确量化（不仅仅是"有偏差"而是"4.97:1"）；(2) 27 种策略的系统排除在规模上超越了现有文献；(3) Oracle 控制（+29.90pp, §4.3）将瓶颈精确定位到提取质量而非形式化通道。建议作者按 R2 建议将贡献重心从概念新颖性转向诊断体系和实验规模。

**[AGREE] R2-N2: 标题 overclaiming "from 7B to Frontier Scale"**

完全同意。我在审稿中也提出了相关问题（我的 W3）。Table 15（Appendix）显示 frontier 模型使用 Mistral-7B 做跨模型提取（标记为 $^b$），不是 self-extraction。标题中 "Self-Extracted" 修饰 "Symbolic Constraints"，但 frontier 实验的提取主体是 Mistral-7B 而非目标模型自身。这构成了标题与实验设计之间的不匹配。

补充一点：即使在开源模型中，论文的 "7B to 32B" 范围也主要覆盖 7B-14B 级别（Table 1），QwQ-32B 仅在退化条件（AIME n=22, GSM8K n=30）上测试且 C₀<5% 导致 SICA 退化为 SC。真正有信息量的对比集中在 7B-14B 范围。

**[AGREE] R2-N3: DRC 作为独立贡献不够充分**

同意。DRC（§6.1）本质上是：if majority_fraction < τ then invoke NLI else use SC。这是标准的 confidence-based cascade/routing 设计。论文声称 "Pareto-efficient"，但仅在 2 个数据集（ProofWriter 选择 τ，FOLIO held-out）上验证，且 τ=0.7 这个阈值的敏感性分析（我的 Q4）未提供。

从我（方法严谨性）的角度补充：DRC 的 "recovery rate"（83-90%）看起来很好，但基数是 full-combo gain（ProofWriter +6.67pp），所以 DRC 实际恢复的是约 +6.00pp——而这本身的显著性依赖于 Mistral-7B 这个最弱模型的特殊条件。对更强模型（LLaMA-8B、Qwen2.5-14B），full-combo gain 本身就不显著（Table 2, all p>0.45），DRC 无从发挥。将 DRC 降级为 §6 的 practical observation 是合理的。

---

## Should-Fix 问题

**[AGREE] R2-W1: Independence-Accuracy Trade-off 的 framing**

同意。K_eff 是 Kish (1965) design effect 的直接应用（我的 W5 已指出 Fleiss' κ 替代 ICC 的验证不充分），BR 是简单的条件概率比，C₀ 是零成本二值过滤器。每个指标单独看都很直接。价值确实在组合应用和系统化诊断，而非方法论创新。将 Contribution 2 定位为 "Contribution 1 的量化工具集" 是更准确的描述。

**[AGREE] R2-W2: CIL 理论贡献被高估**

完全同意，这与我的 W2 一致。CIL 是 post-hoc 定义的条件概率对数比（不是标准信息论量），仅在 8 个 pairs 上计算（其中 3 对共享 Mistral-7B generator，3 对共享 DeBERTa verifier），"unify" 的表述过强。Appendix D 的 Spearman ρ=0.881 (p=0.004) 看似强，但 n=8 且非独立样本——R2 提出的 "去掉最强 pair 后是否成立" 是一个好的 robustness check。

**[REBUT] R2-W3: Cross-architecture escape 证据偏窄**

部分反驳。R2 说 "仅 ProofWriter 显著"，这是事实（§6, Table 2：BH 校正后仅 Mistral-7B w=3 和 w=5 在 ProofWriter 上显著）。但需要公平看待为什么 FOLIO 不显著：FOLIO n=204 比 ProofWriter n=600 小得多，我的 power analysis 审查（N1）已指出 n=204 的 MDE≈4.84pp，而 FOLIO 上的 combo Δ=+2.94pp 低于 MDE。也就是说，FOLIO 上 "不显著" 可能是 underpowered 而非真正无效。LogiQA 不显著则有实质性原因——论文明确说 LogiQA 的问题不分解为 premise-conclusion 结构（§7 Limitations "NLI is effective only when the task naturally decomposes into premise-conclusion entailment"）。

所以证据确实偏窄，但原因是混合的（power + task alignment），不全是方法本身的问题。verifier-collapsed p=0.167 的问题我已在 N3 中标记为 critical。

**[AGREE] R2-W4: Figure 2 placement 问题**

同意。Figure 2（27 strategies summary）在 §5.6（page 7）引用但实际出现在 page 25，读者需要翻阅 18 页才能看到被引用的图表。这严重影响可读性。应移至 §5.6 附近或创建一个简化版放在正文。

**[AGREE] R2-W5: Appendix 体量过大，关键信息分配不合理**

同意。约 18 页 appendix 中，Table 15（frontier SCB, 9 models）支撑论文的核心 claim 之一（"SCB universality"），却放在 appendix。Table 18/19（trace independence 全表）和 Table 16（process-κ gradient）也直接支撑正文 claim。建议将 Table 15 和至少一个 process-level independence 表移入正文。

反过来，Case Studies（Appendix G，约 1 页）和 Extraction Error Taxonomy（Appendix L，约 1 页）的重要性较低，可考虑精简。

---

## 小问题

1. **"Symbolic Mirage" 命名**：[AGREE] "Mirage" 偏文学化，"Symbolic Bias Inheritance" 或 "Extraction Bias Propagation" 更准确地描述机制（约束继承了提取源的偏差，而非"幻象"）。但这是 minor issue。

2. **Orphan bib entry (brown2005diversity)**：[AGREE] 如果确实未被引用则应清理。我未逐条核查 bib，信任 R2 的检查。

3. **Abstract 信息密度偏高**：[REBUT] 对负面结果论文来说，abstract 需要同时传达 (1) 研究问题 (2) 负面结果及规模 (3) 机制解释 (4) 正面逃逸路径。当前 abstract 确实密集，但核心信息完整且没有遗漏关键发现。这对读者快速评估论文价值是必要的。

4. **\looseness=-1 大量使用**：[AGREE] 技术上合法但过度使用可能导致行距不一致。Minor formatting issue。

5. **Neuro-symbolic 三分类法是自创分类**：[AGREE] §3（page 3）的 "Specification-generation, Extraction, Hybrid" 三分类未引用来源。应标注为作者的组织框架而非领域共识，或引用支持文献。

6. **C₀ 和 C_D 符号不一致**：[REBUT] 检查论文后，C₀ 在 §3.2（Eq. 后的 paragraph）定义为 multi-candidate rate，C_D 在 §3.2（degeneration condition 段落的 C₀ diagnostic）出现——但实际上我在 LaTeX 源码中只看到 C_0（$C_0$），未找到 $C_D$。如果 R2 指的是其他符号，需要具体指出位置。

---

## Questions 回应

**Q1: frontier 模型能否通过 API logprobs/structured output 做真正的 self-extraction？**
[AGREE 这是好问题] 从方法严谨性角度，这确实是 frontier SCB 声称的关键漏洞。gpt-4o 支持 structured JSON output，理论上可以做自提取。论文 Table 15 中 gpt-4o 实际上标记为 $^a$（self-extraction），但其他 frontier 模型标记为 $^b$（cross-model）。如果部分 frontier 模型可以做 self-extraction 但作者选择了 cross-model，需要解释原因。

**Q2: 用 oracle annotations 微调小模型作为 extractor，SCB 是否会消失？**
[AGREE] 这与我的 W4 一致。Oracle 控制的 +29.90pp 显示机制本身有效，瓶颈在提取质量。微调 extractor 是最直接的下一步。论文在 §5.6 末尾承认这是 "most promising future direction" 但未尝试。这是 27 策略中最明显的缺失。

**Q3: CIL ρ=0.881 在 n=8 上的 bootstrap CI？去掉最强 pair 后是否成立？**
[AGREE 需要回答] n=8 的 Spearman ρ 的 bootstrap CI 可能很宽。去掉 Mistral×DeBERTa-PW（CIL=+1.67, Δ=+6.67pp）这个最强 pair 后 ρ 是否仍显著，是检验 CIL 预测力的关键 robustness check。从 Table 23（Appendix）看，去掉后 n=7，且 CIL 值分布可能仍保持大致单调，但需要作者报告具体数字。

**Q4: Debate -18.6pp 的原因——约束质量还是推理质量？**
[REBUT — 论文已部分回答] Appendix（§Error Categorization, page 21-22）分析了 Debate 的 discordant predictions：60 correct→wrong flips vs. 22 wrong→correct flips，且 discordant 问题平均 2.93 effective debate rounds（高于 concordant 的 2.52）。论文的解释是：更长的 debate 产生更自信但仍然错误的约束，因为 critic 和 proposer 共享分布（§Debate discordant analysis）。这说明问题主要在约束质量（biased constraints from same-model debate），而非推理过程崩溃。但我同意论文可以更清晰地在正文中总结这一分析，目前它被深埋在 Appendix 中。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1294 · 2026-05-22T01:13:29.864148+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 84

## Round 84

4 recorded events


### User

_source line 1295 · 2026-05-22T01:13:38.632744+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条回应。

汇总：对 R2 的 3 个 Must-Fix 全部 AGREE，5 个 Should-Fix 中 AGREE 4 个、REBUT 1 个（W3 部分反驳，FOLIO 不显著可能是 power 问题而非方法问题），6 个小问题中 AGREE 4 个、REBUT 2 个（abstract 密度和 C₀/C_D 符号），4 个 Questions 中对 Q4 指出论文已在 Appendix 中部分回答。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-22T01:13:44.844031+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-22T01:13:44.944789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 1298 · 2026-05-22T01:13:46.790586+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 85

## Round 85

14 recorded events


### User

_source line 1299 · 2026-05-22T01:14:01.417576+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 统计功效不足以支撑"无效果"结论**

同意这是一个 legitimate concern，但需区分两个层面：

(1) **论文正文的措辞实际上比 R1 描述的更审慎**。Abstract 原文是 "we find no evidence of improvement, with equivalence established in four conditions, significant degradation in two ... and ten conditions remaining underpowered"——这已经区分了 "没有证据" 和 "没有效果"。Section 4.2 进一步报告了 TOST 在 ±1pp/±2pp/±3pp 三个 margin 下的结果和 relative TOST（Appendix），方法论上是恰当的。

(2) **但标题和 Contribution framing 确实 overclaim**。标题 "Do Not Improve" 是一个绝对否定命题，而非 "We find no evidence that ... improve"。在 power <21% 的条件下，这种绝对措辞不被统计证据支撑。这与我自己的 N2（标题 overclaiming）一致。

**补充**：R1 建议 "增加 seed" 来提升 power。但我认为更根本的问题是 n=200-204 对于检测 2pp 效应本身就不够——增加 seed（4→8）帮助有限，真正需要的是更大的数据集或 pooled analysis。论文在 ProofWriter (n=600) 上 power 更好，且恰好在该数据集检测到了两个显著负面结果，这反而支撑了 "有足够 power 时能检测到真实效应" 的论点。

---

**[AGREE] R1-N2: 单 seed 复制不足**

完全同意。4-seed 复制的 Δ 范围 ~4pp（+3.43 到 -0.49）意味着单 seed 结果的 noise floor 约为 ±2pp，而论文试图检测的效应大小恰好在这个量级。这使 Table 1 中所有单 seed 条件的正负号都不可靠。

但我要补充一个 nuance：**论文的核心论点不完全依赖 Table 1 中的个别条件**。即使每个条件有 ±2pp noise，**16 个条件中 0 个显著正面** 这一 aggregate pattern 在 seed variance 下仍然有信息量。如果 SICA 真的有 2-3pp 的正面效应，在 16 个条件中完全看不到任何显著正面结果是不太可能的（尽管单个条件 power 低，aggregate 的 sign test 仍有一定说服力）。论文没有做这种 meta-analytic 分析，建议补充。

---

**[AGREE] R1-N3: Capability-gap 分析证据薄弱**

完全同意，这与我的 W3 一致。n=6 且 4/6 共享 verifier 的情况下，Spearman ρ=1.0 的 p=0.003 是 inflated 的。Verifier-collapsed p=0.167 才是更诚实的检验。论文在 Limitations 中承认了这一点（"We therefore characterize the capability-gap relationship as a consistent empirical pattern rather than a statistically confirmed law"），但 Introduction Contribution 2 和 Conclusion 中仍以 p=0.003 作为 evidence，存在 framing 不一致。

---

### Should-Fix 问题

**[AGREE] R1-W1: BR 可能存在循环论证**

这是 R1 提出的一个**我自己没有注意到的重要问题**。论文报告 56.4% 的约束零变量重叠（Section 5.2），这意味着超过一半的约束在变量命名层面就只能"支持"其来源 trace 的答案——不是因为模型有偏差，而是因为提取设计使约束和 source answer 在变量层面耦合。在这种情况下 BR 自然偏高，部分反映的是**提取粒度的产物**而非**模型级别的 confirmation bias**。

R1 建议的控制实验（随机打乱约束-trace 映射后计算 BR）是一个好的 sanity check：如果 shuffled BR 仍然远低于 observed BR，那说明 BR 确实反映了 beyond-variable-coupling 的 bias；如果 shuffled BR 接近 observed BR，那 SCB 的核心证据就被削弱了。

不过也需注意：论文的 degeneration 论证（Eq. 4）本身就承认了这种耦合是 SICA 失败的直接机制——只是论文将其归因于 "confirmation bias" 而非 "extraction design artifact"，这两者的区分确实不够清晰。

---

**[AGREE] R1-W2: CIL 命名和 information-theoretic 声称有误导**

完全同意，与我的 W2 一致。CIL 是一个 log-odds ratio（条件概率的对数比），不是互信息或 KL 散度。"Information Lift" 这个名字暗示了 information-theoretic 基础，但实际推导中没有用到 entropy/mutual information 的任何性质。"Cumulative" 在公式中也没有体现（没有累积操作）。建议重命名为 "Conditional Correction Ratio" 或类似。

---

**[AGREE] R1-W3: Frontier SCB cross-model extraction 与 self-extraction 不可直接比较**

完全同意，与我的 N2 一致。Frontier 模型使用 Mistral-7B 作为 extractor，测量的是 Mistral-7B 的 extraction bias 投射到 frontier traces 上的效果，而非 frontier 模型自身的 self-extraction SCB。将这两者放在同一个 "from 7B to Frontier Scale" 叙事下是 misleading。

---

**[REBUT] R1-W4: 27 策略缺失训练式约束提取器**

R1 的观察是准确的——训练式提取器确实是最有可能成功的方向，论文也在 Section 5.6 明确承认 "we do not evaluate trained constraint extractors ... we consider trained extractors the most promising future direction"。但我不同意这构成一个 should-fix 级别的问题，理由如下：

(1) **论文的研究问题是明确界定的**：能否以 zero-cost 方式（同一模型、无额外训练数据）通过自提取约束改善推理？这是一个有意义的独立问题。训练式提取器改变了问题的 setup（需要 supervised data 和额外训练），属于一个不同的研究方向。

(2) **论文的 "all fail" 措辞指的是 27 种 self-extraction 修复策略**，不是所有可能的 constraint-based 方法。Section 5.6 的措辞是 "twenty-seven remediation strategies spanning fifteen families all produce neutral-to-negative results"——这对 scope 是准确的。

(3) **Oracle 控制实验 (+29.90pp) 本身就隐含了对训练式方法的 upper bound estimation**，这是比实际训练一个 extractor 更有信息量的分析——它告诉我们 constraint quality 是唯一瓶颈。

不过我同意 Abstract 中 "twenty-seven-same-model remediation strategies spanning fifteen families all fail" 的措辞可以更精确，应强调 scope 限于 training-free interventions。

---

**[REBUT] R1-W5: K_eff 用 κ 替代 ICC 验证不充分**

R1 指出 κ 和 ICC 理论上测量不同东西（κ 是 chance-corrected agreement，ICC 是方差分解），r=0.625 只是中等相关。这个统计学观察是正确的，但我认为这不影响论文的核心论点，因为：

(1) 论文已明确将 K_eff 定位为 **ordinal diagnostic** 而非精确估计值（Section 3.1: "K_eff should be interpreted as an ordinal diagnostic—ranking which conditions have genuine vote diversity—rather than as a literal effective sample size"）。对于排序用途，r=0.625 的 monotonic relationship 是足够的。

(2) K_eff 不是论文的核心结论——SCB（BR=4.97×）和 oracle gap (+29.90pp) 才是。K_eff 只是一个辅助诊断工具，用于解释为什么增加 K 收益递减。即使 K_eff 的具体数值不够精确，"K=12 but effective independence much lower" 的 qualitative 结论仍然成立。

(3) r=0.625 是 **across model families** 的平均值。对于 within-family ranking（论文的主要用途），monotonicity 可能更好。

---

### 小问题

**[AGREE] Eq.3 scoring 等于加权 vote count**：正确。论文自己也在 Eq.4 (degeneration condition) 中承认了这一点。但这恰恰是论文的论点——SICA 在实践中退化为 majority voting。

**[AGREE] GSM8K n=30, AIME n=22 在主表可能误导**：同意。这些 degenerate 条件应移到脚注或 appendix，因为 C_0<5% 意味着它们不可能提供信息。

**[AGREE] n<200 条件无 CI 未说明**：合理的格式问题。

**[AGREE] Figure 2 无 p 值/CI**：考虑到这是一张 27 策略的汇总图，添加 CI 会使图表过于拥挤。但至少应在 caption 中说明 "see Tables X-Y for statistical tests"。

**[REBUT] Conclusion 过于简短**：4 行的 Conclusion 在 8 页限制下是合理的——论文已有独立的 Discussion section (Section 7)。合并 Discussion+Conclusion 并扩展是一个可选方案（与我的 W5 建议一致），但当前分离的结构也可接受。

**[AGREE] FOLIO Unknown 类 FOL 处理未说明**：这是一个有 substance 的问题。FOLIO 有 True/False/Unknown 三类标签，FOL 约束如何处理 Unknown（本质上是证据不足）值得在方法或 appendix 中说明。

---

### Questions

**Q1 (随机打乱 BR)**：好问题，应当回答。如上述 W1 回应，这是验证 SCB 是否为 extraction design artifact 的关键控制实验。

**Q2 (非命题约束)**：有趣但优先级较低。论文报告 99% 约束是命题级的，这可能是 LLM 在 FOL 生成能力上的上限而非提取 prompt 的限制。

**Q3 (无 gold annotation 数据集)**：重要问题。LogiQA 没有 gold FOL，无法做 oracle 控制，因此失败原因无法确认。论文只能在 FOLIO/ProofWriter 上做机制分析，这限制了结论的推广性。

**Q4 (DRC τ 敏感性)**：论文在 Appendix Table M.1 有 K sensitivity 分析，但 τ 本身的 sensitivity 分析似乎缺失。应补充 τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9} 的 Pareto 曲线。

**Q5 (seed 方差 vs Table 1)**：如我在 N2 回应中所述，单个条件不可靠，但 aggregate pattern（16/16 无显著正面）仍有信息量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-22T01:14:28.074192+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-22T01:14:28.074625+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T01:01:59.242585+00:00\", \"completed_at\": \"2026-05-22T01:05:37.703109+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（title/abstract/intro），无任何 display item。审稿人前 2 分钟看到的全是文字墙，缺乏视觉锚点。第一个 display item（Figure 1 pipeline 图）直到 page 3 顶部才出现。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（SICA pipeline）作为全文首个视觉锚点，位置尚可但非最优。图中文字在 150 dpi 下可读，彩色框和箭头清晰，caption 自包含。红色虚线框标注的变体可辨识。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-9\", \"message\": \"主正文 8 页仅 3 个 display items（1 figure + 2 tables）。作为实证为主的论文，display items 密度偏低（通常 5-8 个）。关键可视化（如 Figure 2 — 27 种 remediation 策略的汇总图）被放在 appendix page 25，未在主文中出现。\"}, {\"severity\": \"info\", \"dimension\": \"page 4-5\", \"message\": \"连续 2 页纯文本（Section 3 Background + Section 4 开头），但 page 4 包含数学公式（eq. 3-5），属于形式化推导，节奏尚可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1（主结果表）使用 booktabs 风格，最优值加粗，行分组清晰（Type C/B/A + degenerate + oracle）。表格密度较高但结构合理。Symbols（†, ‡, ***, **）标注清楚。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页纯文本（Sections 5.3-5.6 分析），位于 Table 1（p6）和 Table 2（p8）之间。单页纯文本在分析段落中可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 2 排版整洁。Discussion 和 Conclusion 压缩在同一页下半部分，Conclusion 仅占约 1/4 页空间，较紧凑但无溢出。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落占大半页，覆盖 6 个方面（capability gap、single-seed、capability-accuracy、computational trade-off、reproducibility），篇幅适中。References 从页面底部开始。\"}, {\"severity\": \"info\", \"dimension\": \"page 12-13\", \"message\": \"Appendix B（Prompt Templates）包含大段 monospace 代码文本，排版清晰。代码块与正文字体区分明确。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Algorithm 1 和 Algorithm 2 使用标准算法排版环境，伪代码清晰可读，行号标注正确。\"}, {\"severity\": \"warning\", \"dimension\": \"page 25\", \"message\": \"Figure 2 上方约
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-22T01:14:28.125789+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-22T01:14:28.226980+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-22T01:14:29.684605+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ".*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "output_mode": "content",
  "head_limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": ".*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "output_mode": "content",
    "head_limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-22T01:14:29.785697+00:00_

1:# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2:- id: "R1-C1"
3:  summary: "Method Stage 3 sat() implementation undescribed"
4:  category: method
5:  severity: critical

[Showing results with pagination = limit: 5]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-22T01:14:33.955065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-22T01:14:34.056419+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 19025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-22T01:17:24.569645+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9-10 in_progress issues\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及，但 DRC 贡献不足的共识间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认 critical 共识: verifier-collapsed p=0.167 不显著. 正文用 p=0.003 而 Limitations 用 p=0.167, framing 不一致\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 12\n      reviewers: []\n      note: \"R12 视觉审查确认: pages 1-2 纯文本, Figure 1 在 page 3 顶部\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 确认 Conclusion 仅 4 行. R2 建议合并 Discussion+Conclusion. R1 反驳称 8 页限制下可接受\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Bound 1 无推导, ≲ 未定义\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"应降级为 Empirical Finding/Observation\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及——可能已修复(当前论文使用 'Empirical Finding 1/2'). 待 Research Director 确认\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"ordinal diagnostic 声明正确但后续使用偶有逾越\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 分歧: R1 维持 W5(验证不充分); R2 REBUT(ordinal diagnostic 足够). 论文已加 ordinal caveat 但正文多处仍作字面使用\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"critical consensus: 4/6 共享 DeBERTa, collapsed p=0.167\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次 critical 共识. R1: Introduction/Conclusion 仍以 p=0.003 呈现, framing 不一致. R2: 完全同意\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"τ=0.7 在 eval set 上选择\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: DRC 整体贡献不足以作为独立 Contribution 4\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 分歧: R1 partial REBUT(FOLIO 可能 underpowered 而非无效); R2 维持证据偏窄\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"4-seed Δ range ≈4pp\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识升级 critical: 单 seed + <21% power 构成系统性问题. R2 补充: aggregate pattern(16/16无正面)仍有信息量, 建议 meta-analytic sign test\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"margin 选择无 principled justification\"\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 维持; R2 未单独提及但 power 批评覆盖\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Wan et al. 2025, Jhaveri et al. 2026 区分不足\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识升级: SCB 本质是 self-correction failure 在 FOL 载体上的实例化, 非概念突破. R1 补充: 量化贡献(BR=4.97×, 27策略)和 oracle 定位有价值, 应重新定位贡献重心\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及. R2 Related Work 覆盖面广列为优势\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: 区分 principled vs parameter variations; Figure 2 应在正文而非 page 25\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 核心共识: SCB 是 expected outcome given prior work. R1(3.5) vs R2(3.0) 仍有分歧但方向一致. R2 Excitement 2.5/5\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: 贡献在量化而非新发现. K_eff/BR/C_0 各自简单, 组合有价值\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 视觉审查: 主文8页仅3个display items(1 figure + 2 tables), 密度偏低. Figure 2在page 25\"\n\n# R11 issues\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"4/6 共享 DeBERTa verifier. ρ=1.0 p=0.003 出现11次\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认. 与 R9-W3/R10-N3 同一问题\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"10/16 underpowered. Abstract/title 超出证据范围\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: 标题 'Do Not Improve' 绝对否定不被 power<21% 支撑. R2补充: Abstract 措辞实际较审慎但标题仍 overclaim. 另: frontier 用 cross-model extraction 加剧标题不匹配\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 维持; 论文已提供 SC 文献 2-5pp 锚点和 sensitivity 分析\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: DRC 不应作为独立贡献. τ=0.7 敏感性分析缺失\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"BR>1 方向 expected\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 R1 新增重要发现: 56.4%零变量重叠意味BR高部分是提取设计产物(约束按定义绑定source answer). R2 AGREE 这是重要遗漏. 需控制实验(shuffle 约束-trace 映射)\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 和 'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 R2 提出 'Symbolic Mirage' 偏文学化, 建议 'Symbolic Bias Inheritance'. R1 AGREE 但认为 minor\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: formal channel distinction 是 SCB 的 non-obvious 之处(99% 通过 Z3 语法检查却无用). 应更突出\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识维持\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独检查引用完整性\"\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 分歧: R1 维持(排除最有前途方向后 'all fail' 有误导); R2 REBUT(scope 限定为 zero-cost 修复是合理研究问题). 共识: Abstract 应明确 scope 限于 training-free interventions\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 视觉审查再次确认: 主文仅3个display items. Figure 2(27策略汇总)在page 25但§5.6引用. R1/R2共识应移入正文\"\n\n# R12 新 issues\n- id: \"R12-N1\"\n  summary: \"标题 'Do Not Improve...from 7B to Frontier Scale' overclaiming——frontier 用 cross-model extraction 而非 self-extraction\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1/R2 共识: 标题中 'Self-Extracted' 但 frontier 实验用 Mistral-7B 做跨模型提取. 另: 7B-32B 中 QwQ-32B 仅退化条件(C₀<5%). 实际有效范围 7B-14B\"\n  action_items:\n    - round: 12\n      action: \"修改标题去掉 'to Frontier Scale' 或加限定词; Abstract/Introduction 区分 self-extraction(7B-14B) 和 cross-model extraction(frontier)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——本质是 self-correction failure(Huang 2024)在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. 区分在于 Z3 provable soundness 定位瓶颈到 extraction 而非 verification——但这是实验发现非概念突破. R1补充: 量化深度(BR=4.97×, 27策略)和 oracle 定位有价值, 贡献重心应从'新发现'转向诊断体系+实验规模\"\n  action_items:\n    - round: 12\n      action: \"(1) 降低 Contribution 1 的 novelty claim 调门; (2) 重新定位贡献重心为量化诊断体系和实验规模; (3) 突出 formal channel 下 SCB 的 non-obvious 之处(99% Z3 valid 却无用)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分——标准 confidence-based routing\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. DRC = if majority_fraction < τ then NLI else SC. 标准 cascade 设计. 'Pareto-efficient' 宣称在 n=2 datasets 上不充分\"\n  action_items:\n    - round: 12\n      action: \"将 DRC 从独立 Contribution 降级为 §6 的 practical observation/ablation; 或增加更多 routing 策略对比\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义'支持'source answer\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 首提, R2 AGREE 重要遗漏. BR=4.97×中多少是提取设计产物(约束-trace 耦合)vs 模型级 bias 需通过控制实验区分\"\n  action_items:\n    - round: 12\n      action: \"做控制实验: 随机 shuffle 约束-trace 映射后计算 BR, 量化 'design artifact' 成分\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导——实际是 log-odds ratio\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1/R2 共识: 'Cumulative Information Lift' 暗示信息论基础但实际是条件概率对数比. 'Cumulative' 无体现. 'unify' 过强(仅经验相关, 无数学推导). n=8 非独立样本上 ρ=0.881 可能受 outlier 影响\"\n  action_items:\n    - round: 12\n      action: \"重命名 CIL; 删除 'unify' 措辞; 添加 leave-one-out sensitivity\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——page 25 但 §5.6(page 7)引用\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. 视觉审查也确认. 核心贡献的视觉支撑不应在 appendix\"\n  action_items:\n    - round: 12\n      action: \"将 Figure 2 移至 §5.6 附近正文页面\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"Appendix ~18页 vs 主文 8页——关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. Table 15(frontier SCB)支撑标题级 claim 却在 appendix. 建议: 合并 Discussion+Conclusion 省空间, 上提 Table 15 和 capability-gap scatter\"\n  action_items:\n    - round: 12\n      action: \"Table 15 移入正文; 考虑合并 Discussion+Conclusion; 精简 Case Studies 和 Extraction Error Taxonomy\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9-10 in_progress issues\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及，但 DRC 贡献不足的共识间接涵盖\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认 critical 共识: verifier-collapsed p=0.167 不显著. 正文用 p=0.003 而 Limitations 用 p=0.167, framing 不一致\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 12\n      reviewers: []\n      note: \"R12 视觉审查确认: pages 1-2 纯文本, Figure 1 在 page 3 顶部\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 确认 Conclusion 仅 4 行. R2 建议合并 Discussion+Conclusion. R1 反驳称 8 页限制下可接受\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Bound 1 无推导, ≲ 未定义\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"应降级为 Empirical Finding/Observation\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及——可能已修复(当前论文使用 'Empirical Finding 1/2'). 待 Research Director 确认\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"ordinal diagnostic 声明正确但后续使用偶有逾越\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 分歧: R1 维持 W5(验证不充分); R2 REBUT(ordinal diagnostic 足够). 论文已加 ordinal caveat 但正文多处仍作字面使用\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"critical consensus: 4/6 共享 DeBERTa, collapsed p=0.167\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次 critical 共识. R1: Introduction/Conclusion 仍以 p=0.003 呈现, framing 不一致. R2: 完全同意\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"τ=0.7 在 eval set 上选择\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: DRC 整体贡献不足以作为独立 Contribution 4\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 分歧: R1 partial REBUT(FOLIO 可能 underpowered 而非无效); R2 维持证据偏窄\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"4-seed Δ range ≈4pp\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识升级 critical: 单 seed + <21% power 构成系统性问题. R2 补充: aggregate pattern(16/16无正面)仍有信息量, 建议 meta-analytic sign test\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"margin 选择无 principled justification\"\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 维持; R2 未单独提及但 power 批评覆盖\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"与 Wan et al. 2025, Jhaveri et al. 2026 区分不足\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识升级: SCB 本质是 self-correction failure 在 FOL 载体上的实例化, 非概念突破. R1 补充: 量化贡献(BR=4.97×, 27策略)和 oracle 定位有价值, 应重新定位贡献重心\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及. R2 Related Work 覆盖面广列为优势\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: 区分 principled vs parameter variations; Figure 2 应在正文而非 page 25\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 核心共识: SCB 是 expected outcome given prior work. R1(3.5) vs R2(3.0) 仍有分歧但方向一致. R2 Excitement 2.5/5\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: 贡献在量化而非新发现. K_eff/BR/C_0 各自简单, 组合有价值\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 视觉审查: 主文8页仅3个display items(1 figure + 2 tables), 密度偏低. Figure 2在page 25\"\n\n# R11 issues\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"4/6 共享 DeBERTa verifier. ρ=1.0 p=0.003 出现11次\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认. 与 R9-W3/R10-N3 同一问题\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"10/16 underpowered. Abstract/title 超出证据范围\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: 标题 'Do Not Improve' 绝对否定不被 power<21% 支撑. R2补充: Abstract 措辞实际较审慎但标题仍 overclaim. 另: frontier 用 cross-model extraction 加剧标题不匹配\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"R12 R1 维持; 论文已提供 SC 文献 2-5pp 锚点和 sensitivity 分析\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: DRC 不应作为独立贡献. τ=0.7 敏感性分析缺失\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"BR>1 方向 expected\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 R1 新增重要发现: 56.4%零变量重叠意味BR高部分是提取设计产物(约束按定义绑定source answer). R2 AGREE 这是重要遗漏. 需控制实验(shuffle 约束-trace 映射)\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 和 'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 R2 提出 'Symbolic Mirage' 偏文学化, 建议 'Symbolic Bias Inheritance'. R1 AGREE 但认为 minor\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识: formal channel distinction 是 SCB 的 non-obvious 之处(99% 通过 Z3 语法检查却无用). 应更突出\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 共识维持\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独检查引用完整性\"\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 分歧: R1 维持(排除最有前途方向后 'all fail' 有误导); R2 REBUT(scope 限定为 zero-cost 修复是合理研究问题). 共识: Abstract 应明确 scope 限于 training-free interventions\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 视觉审查再次确认: 主文仅3个display items. Figure 2(27策略汇总)在page 25但§5.6引用. R1/R2共识应移入正文\"\n\n# R12 新 issues\n- id: \"R12-N1\"\n  summary: \"标题 'Do Not Improve...from 7B to Frontier Scale' overclaiming——frontier 用 cross-model extraction 而非 self-extraction\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1/R2 共识: 标题中 'Self-Extracted' 但 frontier 实验用 Mistral-7B 做跨模型提取. 另: 7B-32B 中 QwQ-32B 仅退化条件(C₀<5%). 实际有效范围 7B-14B\"\n  action_items:\n    - round: 12\n      action: \"修改标题去掉 'to Frontier Scale' 或加限定词; Abstract/Introduction 区分 self-extraction(7B-14B) 和 cross-model extraction(frontier)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——本质是 self-correction failure(Huang 2024)在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. 区分在于 Z3 provable soundness 定位瓶颈到 extraction 而非 verification——但这是实验发现非概念突破. R1补充: 量化深度(BR=4.97×, 27策略)和 oracle 定位有价值, 贡献重心应从'新发现'转向诊断体系+实验规模\"\n  action_items:\n    - round: 12\n      action: \"(1) 降低 Contribution 1 的 novelty claim 调门; (2) 重新定位贡献重心为量化诊断体系和实验规模; (3) 突出 formal channel 下 SCB 的 non-obvious 之处(99% Z3 valid 却无用)\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分——标准 confidence-based routing\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. DRC = if majority_fraction < τ then NLI else SC. 标准 cascade 设计. 'Pareto-efficient' 宣称在 n=2 datasets 上不充分\"\n  action_items:\n    - round: 12\n      action: \"将 DRC 从独立 Contribution 降级为 §6 的 practical observation/ablation; 或增加更多 routing 策略对比\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义'支持'source answer\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 首提, R2 AGREE 重要遗漏. BR=4.97×中多少是提取设计产物(约束-trace 耦合)vs 模型级 bias 需通过控制实验区分\"\n  action_items:\n    - round: 12\n      action: \"做控制实验: 随机 shuffle 约束-trace 映射后计算 BR, 量化 'design artifact' 成分\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导——实际是 log-odds ratio\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1/R2 共识: 'Cumulative Information Lift' 暗示信息论基础但实际是条件概率对数比. 'Cumulative' 无体现. 'unify' 过强(仅经验相关, 无数学推导). n=8 非独立样本上 ρ=0.881 可能受 outlier 影响\"\n  action_items:\n    - round: 12\n      action: \"重命名 CIL; 删除 'unify' 措辞; 添加 leave-one-out sensitivity\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——page 25 但 §5.6(page 7)引用\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. 视觉审查也确认. 核心贡献的视觉支撑不应在 appendix\"\n  action_items:\n    - round: 12\n      action: \"将 Figure 2 移至 §5.6 附近正文页面\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R12-W4\"\n  summary: \"Appendix ~18页 vs 主文 8页——关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2 首提, R1 AGREE. Table 15(frontier SCB)支撑标题级 claim 却在 appendix. 建议: 合并 Discussion+Conclusion 省空间, 上提 Table 15 和 capability-gap scatter\"\n  action_items:\n    - round: 12\n      action: \"Table 15 移入正文; 考虑合并 Discussion+Conclusion; 精简 Case Studies 和 Extraction Error Taxonomy\"\n      assigned_to: \"paper_agent\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-22T01:17:24.670823+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 17282}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-22T01:20:27.490959+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 12 审稿报告\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），通过从 LLM 推理 trace 中自提取逻辑约束并用 MAX-SAT 聚合来扩展 Self-Consistency。核心发现是负面结果：自提取约束继承模型偏差（\"symbolic confirmation bias\"，BR=4.97×），27 种修复策略全部失败。跨架构 NLI 验证提供逃逸路径（ProofWriter +6.67pp），DRC 自适应路由方法恢复 83-90% 增益。实验规模令人印象深刻（11 模型、3 数据集、27 策略），oracle 控制设计精妙（+29.90pp），但核心新颖性不足、统计功效偏低、标题 overclaiming 制约了论文水平。\n\n## Strengths\n\n1. **实验规模和系统性出色**：6 个开源模型 + 5 个 frontier 模型、3 个逻辑推理数据集、27 种修复策略（12 principled + 15 参数变体）、4-seed replication、TOST equivalence tests——对负面结果论文来说覆盖面突出。[R1/R2 共识]\n\n2. **Oracle 控制设计精妙**：用 FOLIO/ProofWriter 的 gold FOL annotations 替换自提取约束，展示 +29.90pp/+17.17pp 增益，精确定位瓶颈在 extraction 而非 MAX-SAT/Z3 mechanism。自提取仅捕获 ~12% 的 oracle ceiling。这是论文最有说服力的部分。[R1/R2 共识]\n\n3. **CJT 框架提供清晰理论语言**：Condorcet Jury Theorem 的 independence assumption 解释了 SC plateau 和 SICA 失败，比纯经验描述更有洞察力。K_eff 作为 ordinal diagnostic 的定位恰当。[R2 首提，R1 同意]\n\n4. **诊断框架有实用价值**：C₀ < 5% 意味 SICA 退化为 SC、三类 failure mode（Type A/B/C）、process-level independence 分析——对后续研究有参考价值。[R1]\n\n5. **诚实的局限性披露**：论文在 Limitations 中详细讨论了统计功效、单 seed、capability-gap 分析弱点、计算成本等。学术诚信值得肯定。[R1/R2 共识]\n\n6. **BH 多重比较校正和 TOST 等价性检验**使用恰当，sensitivity 分析（±1/±2/±3pp margins, relative TOST）是良好的统计实践。[R1]\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, 共识]** **标题 \"Do Not Improve...from 7B to Frontier Scale\" overclaiming**\n- Frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro）使用 Mistral-7B 做跨模型提取，不是 self-extraction。标题中 \"Self-Extracted\" 与 frontier 实验设计不匹配。\n- 开源模型中 QwQ-32B 仅在退化条件（AIME n=22, GSM8K n=30, C₀<5%）上测试。有效实验范围集中在 7B-14B。\n- **建议**：修改标题去掉 \"to Frontier Scale\" 或加限定词（如 \"from 7B to 14B, with Cross-Model Evidence at Frontier Scale\"）；Abstract/Introduction 明确区分 self-extraction 和 cross-model extraction。\n- [R2 首提 N2, R1 AGREE]\n\n**W2 [critical, 共识]** **SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化**\n- Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback；Stechly et al. (2025) 证明 self-verification 不可靠；Wan et al. (2025) / Jhaveri et al. (2026) 研究了 CoT confirmation bias。SCB 是同一机制在不同载体（FOL 约束 vs 自然语言）上的实例化，非概念突破。\n- Z3 验证通道的 provable soundness 是有趣切入点（证明瓶颈在提取而非验证），但更接近实验发现而非概念突破。99% 约束通过 Z3 语法检查却仍无用——这一点比 SCB 本身更有趣，应在 framing 中更突出。\n- **建议**：(1) 降低 Contribution 1 的 novelty claim 调门；(2) 重新定位贡献重心为量化诊断体系（BR=4.97×, K_eff, C₀）和实验规模（27 策略系统排除）；(3) 突出 formal channel 下 SCB 的 non-obvious 之处。\n- [R2 首提 N1, R1 AGREE with nuance: 量化贡献不应低估]\n\n**W3 [critical, 共识]** **统计功效 <21% 无法支撑\"无效果\"核心结论**\n- McNemar 在 n=200-600 条件下检测 |Δ|=2pp 效应的功效 <21%。16 个非退化条件中 10 个 TOST \"underpowered\"。最大研究（n=804）MDE=1.86pp，但观测 Δ=+0.25pp。\n- 标题 \"Do Not Improve\" 将\"检测不到效果\"等同于\"没有效果\"，不被 power<21% 支撑。\n- R2 补充 nuance：Abstract 正文措辞（\"no evidence of improvement...ten conditions remaining underpowered\"）实际较审慎；aggregate pattern（16/16 无显著正面）仍有信息量，可补充 meta-analytic sign test。\n- **建议**：(1) 标题和 Contribution framing 使用更审慎措辞；(2) 报告各条件可排除的效应大小范围；(3) 补充 aggregate sign test。\n- [R1 首提 N1, R2 AGREE]\n\n**W4 [critical, 共识]** **单 seed 复制严重不足**\n- 唯一 4-seed 复制（Mistral-7B FOLIO）Δ 范围 +3.43 到 -0.49pp（~4pp 跨度），超过 TOST ±2pp 边界。温度敏感性也显示 T=0.7 是\"孤立峰\"。其他单 seed 条件可靠性存疑。\n- R2 补充：aggregate pattern（16/16 无正面）在 seed variance 下仍有信息量——如果 SICA 真有 2-3pp 正效果，16 条件全无显著正面不太可能。建议补充 meta-analytic 分析。\n- **建议**：至少对 3-4 个关键条件做多 seed 复制，或明确降低单 seed 结论强度。\n- [R1 首提 N2, R2 AGREE]\n\n**W5 [critical, 共识]** **Capability-gap 分析证据过于薄弱**\n- Spearman ρ=1.0, p=0.003, 但 n=6 且 4/6 共享 DeBERTa verifier。Verifier-collapsed 分析（n=3 独立 verifier）p=0.167，不显著。Process-κ gradient 也只有 n=5。\n- Introduction/Conclusion 以 p=0.003 呈现，但 Limitations 承认 p=0.167——framing 不一致。\n- **建议**：(1) 增加更多独立 NLI verifier 架构（≥5 独立 verifier）；(2) 正文中引用 p=0.003 时同步报告 collapsed p=0.167 作为 robustness check；(3) 使用 \"consistent empirical pattern rather than statistically confirmed law\" 的措辞（论文 Limitations 已有，需一致化到正文）。\n- [R1 首提 N3, R2 AGREE = R2-W3]\n\n**W6 [critical, 共识]** **DRC 作为 Contribution 4 不够充分**\n- DRC 本质是基于 trace agreement 阈值 τ 的 confidence-based routing，标准 cascade 设计。τ=0.7 仅在 2 个数据集验证（ProofWriter 选择, FOLIO held-out），τ 敏感性分析缺失。\n- full-combo gain 本身仅在 Mistral-7B（最弱模型）上显著；对更强模型 full-combo 就不显著，DRC 无从发挥。\n- **建议**：将 DRC 降级为 §6 的 practical observation，不作为独立 Contribution 编号；或增加 routing 策略对比和 τ 敏感性分析。\n- [R2 首提 N3, R1 AGREE]\n\n### Should-Fix（影响评分但不一票否决）\n\n**S1 [warning, 共识]** **BR 可能存在循环论证**\n- 56.4% 约束零变量重叠，约束几乎按定义\"支持\"source trace 的答案。BR=4.97× 中多少是提取设计产物 vs 模型级 bias 未被区分。\n- **建议**：做控制实验——随机 shuffle 约束-trace 映射后计算 BR，量化 \"design artifact\" 成分比例。\n- [R1 首提 W1, R2 AGREE: 重要遗漏]\n\n**S2 [warning, 共识]** **CIL 名称和 information-theoretic 声称有误导**\n- \"Cumulative Information Lift\" 实际是 log-odds ratio，非互信息/KL 散度。\"Cumulative\" 无体现。\"unify\" 过强（仅经验相关，无数学推导关联 K_eff/BR）。n=8 非独立样本上 ρ=0.881 可能受 outlier 影响。\n- **建议**：重命名为 \"Conditional Correction Ratio\" 或类似；删除 \"unify\" 措辞；添加 leave-one-out sensitivity。\n- [R1 首提 W2, R2 AGREE]\n\n**S3 [warning, 共识]** **Independence-Accuracy Trade-off（Contribution 2）framing 问题**\n- K_eff 是 Kish design effect 的直接应用，BR 是条件概率比，C₀ 是 zero-cost filter。各自简单直观，价值在组合应用到 LLM 自提取场景，更像 Contribution 1 的量化工具集。\n- **建议**：将 Contribution 2 重新措辞为\"量化诊断工具集\"，降低 \"trade-off\" 的发现性措辞。引用 Krogh & Vedelsby (1994) 明确不是新发现。\n- [R2 首提 W1, R1 AGREE]\n\n**S4 [warning, 共识]** **Figure 2（27 strategies summary）placement 问题**\n- 在 §5.6（page 7）引用但实际出现在 page 25。核心贡献的视觉支撑不应在 appendix。\n- **建议**：调整 LaTeX placement 确保 Figure 2 出现在 §5.6 附近。\n- [R2 首提 W4, R1 AGREE; 视觉审查也确认]\n\n**S5 [warning, 共识]** **Appendix ~18 页，关键信息分配不合理**\n- Table 15（frontier SCB, 9 models）支撑标题级 claim 却在 appendix。主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低。\n- **建议**：合并 Discussion+Conclusion 省空间；将 Table 15 和 capability-gap scatter plot 移入正文；精简 Case Studies 和 Extraction Error Taxonomy。\n- [R2 首提 W5, R1 AGREE; 视觉审查也确认]\n\n**S6 [warning, 分歧]** **27 策略 scope 限定——排除 trained extractor**\n- R1 观点：Oracle +29.90pp 显示 trained extractor 最有前途，排除后 \"all fail\" 有误导。\n- R2 反驳：研究问题明确界定为 zero-cost 自提取修复，trained extractor 改变 setup。\"all fail\" 指 27 种自提取策略，scope 准确。\n- **Director 判断**：R2 反驳有理——研究问题的 scope 限定是合理的。但 Abstract 中应明确 scope 限于 training-free interventions，避免读者误解。\n- [R1 W4 vs R2 REBUT; 部分共识]\n\n**S7 [warning, 分歧]** **K_eff 用 κ 替代 ICC 验证充分性**\n- R1 观点：κ 和 ICC 测量不同东西，r=0.625 只是中等相关，正文多处将 K_eff 作字面有效样本量使用。\n- R2 反驳：论文已定位为 ordinal diagnostic，r=0.625 对排序足够，K_eff 不是核心结论。\n- **Director 判断**：R2 反驳有理——K_eff 作为 ordinal diagnostic 的定位已足够审慎。但正文中偶有逾越（如 \"traces beyond a dozen add negligible independent information\"），应统一限定为排序用途。\n- [R1 W5 vs R2 REBUT; 部分共识]\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n\n1. 标题 overclaiming（frontier 用 cross-model extraction, \"Do Not Improve\" 过于绝对）\n2. SCB 新颖性不足（self-correction failure 的 FOL 实例化，非概念突破）\n3. DRC 贡献不足以作为独立 Contribution\n4. 统计功效 <21% 制约\"无效果\"结论的强度\n5. 单 seed 复制不足（~4pp 跨 seed 波动）\n6. Capability-gap n=6 证据薄弱（collapsed p=0.167）\n7. CIL 名称误导（log-odds ratio ≠ information-theoretic quantity）\n8. BR 可能存在循环论证（提取设计产物 vs 模型级 bias）\n9. Figure 2 和 Table 15 应在正文而非 appendix\n10. Oracle 控制设计精妙（论文最有说服力的部分）\n11. 实验规模和 Limitations 诚实性值得肯定\n\n## Reviewer Divergence\n\n以下问题存在分歧：\n\n1. **27 策略是否应包含 trained extractor**：R1 认为排除最有前途方向后 \"all fail\" 有误导（W4）；R2 认为 zero-cost scope 限定合理（REBUT）。**Director 倾向 R2**——研究问题 scope 合理，但 Abstract 应明确限定。\n\n2. **K_eff 验证充分性**：R1 认为 κ→ICC 替代验证不充分（W5）；R2 认为 ordinal diagnostic 定位已足够（REBUT）。**Director 倾向 R2**——但正文应避免将 K_eff 作字面有效样本量使用。\n\n3. **Cross-architecture escape 证据宽度**：R2 认为仅 ProofWriter 显著（W3）；R1 partial REBUT（FOLIO 不显著可能是 power 问题而非方法问题）。**Director 判断**——两者都有道理，原因是混合的（power + task alignment）。\n\n4. **Conclusion 长度**：R1 认为 4 行过短；R2 认为 8 页限制下 Discussion+Conclusion 分离可接受。**Director 倾向 R2**——但合并可省空间给更重要的 display items。\n\n5. **Abstract 信息密度**：R2 认为偏高；R1 REBUT（负面结果论文需完整传达核心信息）。**Director 倾向 R1**——当前密度对快速评估论文价值是必要的。\n\n## Questions（需要作者澄清）\n\n1. **BR 循环论证控制实验**：如果随机打乱约束-trace 映射后 BR 是多少？这能量化 BR 中\"提取设计产物\"的比例。[R1 Q1, R2 AGREE]\n\n2. **Frontier self-extraction 可行性**：gpt-4o 在 Table 15 标记为 self-extraction ($^a$)，其他 frontier 标记为 cross-model ($^b$)。为什么不对所有支持 structured output 的 frontier 模型做 self-extraction？[R2 Q1]\n\n3. **Trained extractor 是否消除 SCB**：用 oracle annotations 微调小模型作为 extractor，SCB 是否会消失？这是否是本文最重要的 limitation？[R2 Q2, R1 同意]\n\n4. **CIL robustness**：ρ=0.881 (n=8) 的 bootstrap CI？去掉最强 pair（Mistral×DeBERTa-PW）后相关性是否保持？[R2 Q3, R1 AGREE]\n\n5. **DRC τ 敏感性**：τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9} 的 Pareto 曲线？ProofWriter 选择 τ=0.7 在 FOLIO 上的最优 τ 是否相同？[R1 Q4]\n\n6. **Seed 方差 vs Table 1**：4-seed ~4pp 波动是否使 Table 1 单 seed 结果基本不可解释？是否考虑 aggregate sign test 补充 meta-analytic 证据？[R1 Q5, R2 nuance]\n\n7. **FOLIO Unknown 类处理**：FOL 约束如何处理 open-world semantics 的 Unknown？[R1 minor]\n\n8. **非命题约束**：99% 约束是命题级的。引导模型生成真正的一阶逻辑约束是否可能改善结果？[R1 Q2]\n\n## Missing References\n\nR2 在 Round 11 中标记了遗漏引用（Byerly & Khashabi 2026 TACL, arxiv:2604.07650 等），本轮未重新核查引用完整性。论文当前 ~48 citations，Related Work 覆盖面整体较广。[R2 优势 #4]\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**。项目配置中外部审稿未启用。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 13 info, 0 critical）。\n\n**Warnings：**\n1. Pages 1-2 连续纯文本无 display item，第一个视觉锚点（Figure 1）在 page 3 顶部。\n2. 主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低（通常 5-8 个）。Figure 2 被放在 appendix page 25。\n3. Page 25 Figure 2 上方 ~1/3 空白。\n\n**Info（摘要）：**\n- Table 1 (page 6) 使用 booktabs 风格，行分组清晰。\n- Appendix 排版整洁（Algorithm 1-2、prompt templates、多个 tables）。\n- References 无未解析引用 [?]。\n- Page 26 有 5 个 figures 密集排列，axis labels 偏小。\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 加权共识 |\n|------|----|----|----------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | 3.5 | 4.0 | 3.5 |\n| Overall | 3.5 | 3.0 | 3.0 |\n| Confidence | 4 | 4 | 4 |\n\n**评分理由：**\n\n论文的实验规模和方法论严谨程度值得肯定（Soundness 3.5），oracle 控制设计精妙，Limitations 节诚实全面。但多个关键弱点将论文限制在 Findings 水平：\n\n1. **新颖性不足**（Excitement 2.5）：SCB 是 self-correction failure（Huang 2024）在 FOL 载体上的实例化，可从已有文献合理预期。主要贡献在量化深度（BR=4.97×, 27 策略系统排除）而非新现象发现。DRC 是标准 cascade 设计，不构成方法论创新。\n\n2. **标题和 framing overclaiming**：标题声称 \"from 7B to Frontier Scale\" 但 frontier 实验非 self-extraction；\"Do Not Improve\" 绝对否定不被 power<21% 支撑；Contribution 2 是 Kish design effect 的直接应用而非新发现。\n\n3. **统计证据基础偏弱**：(a) 16/16 无显著正面但 power<21%，aggregate pattern 有信息量但未做 meta-analytic 分析；(b) 4-seed 复制仅 1 个条件，~4pp 跨 seed 波动使单 seed 结果不可靠；(c) capability-gap 核心正面贡献的 collapsed p=0.167 不显著。\n\n4. **正面贡献证据偏窄**：Cross-architecture NLI 仅在 ProofWriter (Mistral-7B) 上显著（BH 校正后）；DRC 在 2 个数据集上验证不足。\n\n**接收建议**：建议作为 **Findings paper** 接收，条件是修复标题 overclaiming、降低 SCB novelty claim、将 DRC 降级、统一正文与 Limitations 的 statistical framing。如果完成这些修改并补充 BR 控制实验和 aggregate sign test，有潜力升级为 Borderline Conference。\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息密度高但核心信息完整。需要：(1) 修改 \"from 7B to Frontier Scale\" 措辞；(2) 明确 27 strategies 的 scope 限于 training-free interventions；(3) \"we find no evidence of improvement\" 虽比标题审慎但应加 underpowered caveat。\n\n**Introduction (§1)**: 叙事结构清晰（SC 瓶颈 → CJT → SICA → 失败 → 诊断 → 逃逸）。需要：(1) 更早建立 formal channel distinction（Z3 provably sound, failure in extraction not verification）；(2) Contribution 2 承认是量化而非新发现；(3) Contribution 4 (DRC) 降级或加深。\n\n**Related Work (§2)**: 覆盖面广，~48 citations，5 个段落。Neuro-symbolic 三分类法（Specification/Program/Trace）是有用的组织框架，但应标注为作者分类而非 established taxonomy。与 Huang 2024 / Stechly 2025 / Wan 2025 的区分需在 Introduction 更早建立。\n\n**Background & Setup (§3)**: SICA pipeline 形式化完整（Eq. 1-5, Algorithm 1-2）。\"Empirical Finding 1/2\" 的定位恰当（相比此前版本的 Proposition/Bound 已改善）。\"Symbolic Mirage Hypothesis\" 命名偏 dramatic，建议改为 \"Symbolic Bias Inheritance\" 或 \"Extraction Bias Hypothesis\"。CIL 应重命名并降低 \"unify\" 声称。\n\n**Experiments (§4)**: Table 1 结构清晰，regime 分组有信息量。GSM8K (n=30) 和 AIME (n=22) 作为 degenerate 条件放在主表中可能给读者统计错觉——建议移至 appendix 或脚注。4-seed replication 仅 1 个条件，是最大统计弱点。\n\n**Analysis (§5)**: SCB 分析（BR=4.97×, 83.3% 约束支持错误答案）是论文最有力的分析，但 BR 可能存在循环论证。Process-level independence（cosine 0.69 > κ 0.46）分析有洞察力。27 策略汇总 Figure 应在正文。\n\n**Cross-Architecture (§6)**: ProofWriter +6.67pp (p<0.001) 是实质性结果。Capability-gap 分析有趣但 n=6 + shared verifier 制约结论强度。DRC τ=0.7 缺 sensitivity 分析。\n\n**Discussion (§7)**: 简洁有效。可与 Conclusion 合并省空间。\n\n**Conclusion (§8)**: 4 行过于简短。建议合并到 Discussion 末尾。\n\n**Limitations**: 全面诚实，覆盖 power、single-seed、capability-gap、计算成本等。是论文的优点。\n\n**Appendix**: ~18 页，内容丰富但 Table 15（frontier SCB）和 Figure 2（27 strategies）应在正文。Page 26 的 5 个 figures 偏小偏密。\n",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 12 审稿报告\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），通过从 LLM 推理 trace 中自提取逻辑约束并用 MAX-SAT 聚合来扩展 Self-Consistency。核心发现是负面结果：自提取约束继承模型偏差（\"symbolic confirmation bias\"，BR=4.97×），27 种修复策略全部失败。跨架构 NLI 验证提供逃逸路径（ProofWriter +6.67pp），DRC 自适应路由方法恢复 83-90% 增益。实验规模令人印象深刻（11 模型、3 数据集、27 策略），oracle 控制设计精妙（+29.90pp），但核心新颖性不足、统计功效偏低、标题 overclaiming 制约了论文水平。\n\n## Strengths\n\n1. **实验规模和系统性出色**：6 个开源模型 + 5 个 frontier 模型、3 个逻辑推理数据集、27 种修复策略（12 principled + 15 参数变体）、4-seed replication、TOST equivalence tests——对负面结果论文来说覆盖面突出。[R1/R2 共识]\n\n2. **Oracle 控制设计精妙**：用 FOLIO/ProofWriter 的 gold FOL annotations 替换自提取约束，展示 +29.90pp/+17.17pp 增益，精确定位瓶颈在 extraction 而非 MAX-SAT/Z3 mechanism。自提取仅捕获 ~12% 的 oracle ceiling。这是论文最有说服力的部分。[R1/R2 共识]\n\n3. **CJT 框架提供清晰理论语言**：Condorcet Jury Theorem 的 independence assumption 解释了 SC plateau 和 SICA 失败，比纯经验描述更有洞察力。K_eff 作为 ordinal diagnostic 的定位恰当。[R2 首提，R1 同意]\n\n4. **诊断框架有实用价值**：C₀ < 5% 意味 SICA 退化为 SC、三类 failure mode（Type A/B/C）、process-level independence 分析——对后续研究有参考价值。[R1]\n\n5. **诚实的局限性披露**：论文在 Limitations 中详细讨论了统计功效、单 seed、capability-gap 分析弱点、计算成本等。学术诚信值得肯定。[R1/R2 共识]\n\n6. **BH 多重比较校正和 TOST 等价性检验**使用恰当，sensitivity 分析（±1/±2/±3pp margins, relative TOST）是良好的统计实践。[R1]\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, 共识]** **标题 \"Do Not Improve...from 7B to Frontier Scale\" overclaiming**\n- Frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro）使用 Mistral-7B 做跨模型提取，不是 self-extraction。标题中 \"Self-Extracted\" 与 frontier 实验设计不匹配。\n- 开源模型中 QwQ-32B 仅在退化条件（AIME n=22, GSM8K n=30, C₀<5%）上测试。有效实验范围集中在 7B-14B。\n- **建议**：修改标题去掉 \"to Frontier Scale\" 或加限定词（如 \"from 7B to 14B, with Cross-Model Evidence at Frontier Scale\"）；Abstract/Introduction 明确区分 self-extraction 和 cross-model extraction。\n- [R2 首提 N2, R1 AGREE]\n\n**W2 [critical, 共识]** **SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化**\n- Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback；Stechly et al. (2025) 证明 self-verification 不可靠；Wan et al. (2025) / Jhaveri et al. (2026) 研究了 CoT confirmation bias。SCB 是同一机制在不同载体（FOL 约束 vs 自然语言）上的实例化，非概念突破。\n- Z3 验证通道的 provable soundness 是有趣切入点（证明瓶颈在提取而非验证），但更接近实验发现而非概念突破。99% 约束通过 Z3 语法检查却仍无用——这一点比 SCB 本身更有趣，应在 framing 中更突出。\n- **建议**：(1) 降低 Contribution 1 的 novelty claim 调门；(2) 重新定位贡献重心为量化诊断体系（BR=4.97×, K_eff, C₀）和实验规模（27 策略系统排除）；(3) 突出 formal channel 下 SCB 的 non-obvious 之处。\n- [R2 首提 N1, R1 AGREE with nuance: 量化贡献不应低估]\n\n**W3 [critical, 共识]** **统计功效 <21% 无法支撑\"无效果\"核心结论**\n- McNemar 在 n=200-600 条件下检测 |Δ|=2pp 效应的功效 <21%。16 个非退化条件中 10 个 TOST \"underpowered\"。最大研究（n=804）MDE=1.86pp，但观测 Δ=+0.25pp。\n- 标题 \"Do Not Improve\" 将\"检测不到效果\"等同于\"没有效果\"，不被 power<21% 支撑。\n- R2 补充 nuance：Abstract 正文措辞（\"no evidence of improvement...ten conditions remaining underpowered\"）实际较审慎；aggregate pattern（16/16 无显著正面）仍有信息量，可补充 meta-analytic sign test。\n- **建议**：(1) 标题和 Contribution framing 使用更审慎措辞；(2) 报告各条件可排除的效应大小范围；(3) 补充 aggregate sign test。\n- [R1 首提 N1, R2 AGREE]\n\n**W4 [critical, 共识]** **单 seed 复制严重不足**\n- 唯一 4-seed 复制（Mistral-7B FOLIO）Δ 范围 +3.43 到 -0.49pp（~4pp 跨度），超过 TOST ±2pp 边界。温度敏感性也显示 T=0.7 是\"孤立峰\"。其他单 seed 条件可靠性存疑。\n- R2 补充：aggregate pattern（16/16 无正面）在 seed variance 下仍有信息量——如果 SICA 真有 2-3pp 正效果，16 条件全无显著正面不太可能。建议补充 meta-analytic 分析。\n- **建议**：至少对 3-4 个关键条件做多 seed 复制，或明确降低单 seed 结论强度。\n- [R1 首提 N2, R2 AGREE]\n\n**W5 [critical, 共识]** **Capability-gap 分析证据过于薄弱**\n- Spearman ρ=1.0, p=0.003, 但 n=6 且 4/6 共享 DeBERTa verifier。Verifier-collapsed 分析（n=3 独立 verifier）p=0.167，不显著。Process-κ gradient 也只有 n=5。\n- Introduction/Conclusion 以 p=0.003 呈现，但 Limitations 承认 p=0.167——framing 不一致。\n- **建议**：(1) 增加更多独立 NLI verifier 架构（≥5 独立 verifier）；(2) 正文中引用 p=0.003 时同步报告 collapsed p=0.167 作为 robustness check；(3) 使用 \"consistent empirical pattern rather than statistically confirmed law\" 的措辞（论文 Limitations 已有，需一致化到正文）。\n- [R1 首提 N3, R2 AGREE = R2-W3]\n\n**W6 [critical, 共识]** **DRC 作为 Contribution 4 不够充分**\n- DRC 本质是基于 trace agreement 阈值 τ 的 confidence-based routing，标准 cascade 设计。τ=0.7 仅在 2 个数据集验证（ProofWriter 选择, FOLIO held-out），τ 敏感性分析缺失。\n- full-combo gain 本身仅在 Mistral-7B（最弱模型）上显著；对更强模型 full-combo 就不显著，DRC 无从发挥。\n- **建议**：将 DRC 降级为 §6 的 practical observation，不作为独立 Contribution 编号；或增加 routing 策略对比和 τ 敏感性分析。\n- [R2 首提 N3, R1 AGREE]\n\n### Should-Fix（影响评分但不一票否决）\n\n**S1 [warning, 共识]** **BR 可能存在循环论证**\n- 56.4% 约束零变量重叠，约束几乎按定义\"支持\"source trace 的答案。BR=4.97× 中多少是提取设计产物 vs 模型级 bias 未被区分。\n- **建议**：做控制实验——随机 shuffle 约束-trace 映射后计算 BR，量化 \"design artifact\" 成分比例。\n- [R1 首提 W1, R2 AGREE: 重要遗漏]\n\n**S2 [warning, 共识]** **CIL 名称和 information-theoretic 声称有误导**\n- \"Cumulative Information Lift\" 实际是 log-odds ratio，非互信息/KL 散度。\"Cumulative\" 无体现。\"unify\" 过强（仅经验相关，无数学推导关联 K_eff/BR）。n=8 非独立样本上 ρ=0.881 可能受 outlier 影响。\n- **建议**：重命名为 \"Conditional Correction Ratio\" 或类似；删除 \"unify\" 措辞；添加 leave-one-out sensitivity。\n- [R1 首提 W2, R2 AGREE]\n\n**S3 [warning, 共识]** **Independence-Accuracy Trade-off（Contribution 2）framing 问题**\n- K_eff 是 Kish design effect 的直接应用，BR 是条件概率比，C₀ 是 zero-cost filter。各自简单直观，价值在组合应用到 LLM 自提取场景，更像 Contribution 1 的量化工具集。\n- **建议**：将 Contribution 2 重新措辞为\"量化诊断工具集\"，降低 \"trade-off\" 的发现性措辞。引用 Krogh & Vedelsby (1994) 明确不是新发现。\n- [R2 首提 W1, R1 AGREE]\n\n**S4 [warning, 共识]** **Figure 2（27 strategies summary）placement 问题**\n- 在 §5.6（page 7）引用但实际出现在 page 25。核心贡献的视觉支撑不应在 appendix。\n- **建议**：调整 LaTeX placement 确保 Figure 2 出现在 §5.6 附近。\n- [R2 首提 W4, R1 AGREE; 视觉审查也确认]\n\n**S5 [warning, 共识]** **Appendix ~18 页，关键信息分配不合理**\n- Table 15（frontier SCB, 9 models）支撑标题级 claim 却在 appendix。主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低。\n- **建议**：合并 Discussion+Conclusion 省空间；将 Table 15 和 capability-gap scatter plot 移入正文；精简 Case Studies 和 Extraction Error Taxonomy。\n- [R2 首提 W5, R1 AGREE; 视觉审查也确认]\n\n**S6 [warning, 分歧]** **27 策略 scope 限定——排除 trained extractor**\n- R1 观点：Oracle +29.90pp 显示 trained extractor 最有前途，排除后 \"all fail\" 有误导。\n- R2 反驳：研究问题明确界定为 zero-cost 自提取修复，trained extractor 改变 setup。\"all fail\" 指 27 种自提取策略，scope 准确。\n- **Director 判断**：R2 反驳有理——研究问题的 scope 限定是合理的。但 Abstract 中应明确 scope 限于 training-free interventions，避免读者误解。\n- [R1 W4 vs R2 REBUT; 部分共识]\n\n**S7 [warning, 分歧]** **K_eff 用 κ 替代 ICC 验证充分性**\n- R1 观点：κ 和 ICC 测量不同东西，r=0.625 只是中等相关，正文多处将 K_eff 作字面有效样本量使用。\n- R2 反驳：论文已定位为 ordinal diagnostic，r=0.625 对排序足够，K_eff 不是核心结论。\n- **Director 判断**：R2 反驳有理——K_eff 作为 ordinal diagnostic 的定位已足够审慎。但正文中偶有逾越（如 \"traces beyond a dozen add negligible independent information\"），应统一限定为排序用途。\n- [R1 W5 vs R2 REBUT; 部分共识]\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n\n1. 标题 overclaiming（frontier 用 cross-model extraction, \"Do Not Improve\" 过于绝对）\n2. SCB 新颖性不足（self-correction failure 的 FOL 实例化，非概念突破）\n3. DRC 贡献不足以作为独立 Contribution\n4. 统计功效 <21% 制约\"无效果\"结论的强度\n5. 单 seed 复制不足（~4pp 跨 seed 波动）\n6. Capability-gap n=6 证据薄弱（collapsed p=0.167）\n7. CIL 名称误导（log-odds ratio ≠ information-theoretic quantity）\n8. BR 可能存在循环论证（提取设计产物 vs 模型级 bias）\n9. Figure 2 和 Table 15 应在正文而非 appendix\n10. Oracle 控制设计精妙（论文最有说服力的部分）\n11. 实验规模和 Limitations 诚实性值得肯定\n\n## Reviewer Divergence\n\n以下问题存在分歧：\n\n1. **27 策略是否应包含 trained extractor**：R1 认为排除最有前途方向后 \"all fail\" 有误导（W4）；R2 认为 zero-cost scope 限定合理（REBUT）。**Director 倾向 R2**——研究问题 scope 合理，但 Abstract 应明确限定。\n\n2. **K_eff 验证充分性**：R1 认为 κ→ICC 替代验证不充分（W5）；R2 认为 ordinal diagnostic 定位已足够（REBUT）。**Director 倾向 R2**——但正文应避免将 K_eff 作字面有效样本量使用。\n\n3. **Cross-architecture escape 证据宽度**：R2 认为仅 ProofWriter 显著（W3）；R1 partial REBUT（FOLIO 不显著可能是 power 问题而非方法问题）。**Director 判断**——两者都有道理，原因是混合的（power + task alignment）。\n\n4. **Conclusion 长度**：R1 认为 4 行过短；R2 认为 8 页限制下 Discussion+Conclusion 分离可接受。**Director 倾向 R2**——但合并可省空间给更重要的 display items。\n\n5. **Abstract 信息密度**：R2 认为偏高；R1 REBUT（负面结果论文需完整传达核心信息）。**Director 倾向 R1**——当前密度对快速评估论文价值是必要的。\n\n## Questions（需要作者澄清）\n\n1. **BR 循环论证控制实验**：如果随机打乱约束-trace 映射后 BR 是多少？这能量化 BR 中\"提取设计产物\"的比例。[R1 Q1, R2 AGREE]\n\n2. **Frontier self-extraction 可行性**：gpt-4o 在 Table 15 标记为 self-extraction ($^a$)，其他 frontier 标记为 cross-model ($^b$)。为什么不对所有支持 structured output 的 frontier 模型做 self-extraction？[R2 Q1]\n\n3. **Trained extractor 是否消除 SCB**：用 oracle annotations 微调小模型作为 extractor，SCB 是否会消失？这是否是本文最重要的 limitation？[R2 Q2, R1 同意]\n\n4. **CIL robustness**：ρ=0.881 (n=8) 的 bootstrap CI？去掉最强 pair（Mistral×DeBERTa-PW）后相关性是否保持？[R2 Q3, R1 AGREE]\n\n5. **DRC τ 敏感性**：τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9} 的 Pareto 曲线？ProofWriter 选择 τ=0.7 在 FOLIO 上的最优 τ 是否相同？[R1 Q4]\n\n6. **Seed 方差 vs Table 1**：4-seed ~4pp 波动是否使 Table 1 单 seed 结果基本不可解释？是否考虑 aggregate sign test 补充 meta-analytic 证据？[R1 Q5, R2 nuance]\n\n7. **FOLIO Unknown 类处理**：FOL 约束如何处理 open-world semantics 的 Unknown？[R1 minor]\n\n8. **非命题约束**：99% 约束是命题级的。引导模型生成真正的一阶逻辑约束是否可能改善结果？[R1 Q2]\n\n## Missing References\n\nR2 在 Round 11 中标记了遗漏引用（Byerly & Khashabi 2026 TACL, arxiv:2604.07650 等），本轮未重新核查引用完整性。论文当前 ~48 citations，Related Work 覆盖面整体较广。[R2 优势 #4]\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**。项目配置中外部审稿未启用。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 13 info, 0 critical）。\n\n**Warnings：**\n1. Pages 1-2 连续纯文本无 display item，第一个视觉锚点（Figure 1）在 page 3 顶部。\n2. 主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低（通常 5-8 个）。Figure 2 被放在 appendix page 25。\n3. Page 25 Figure 2 上方 ~1/3 空白。\n\n**Info（摘要）：**\n- Table 1 (page 6) 使用 booktabs 风格，行分组清晰。\n- Appendix 排版整洁（Algorithm 1-2、prompt templates、多个 tables）。\n- References 无未解析引用 [?]。\n- Page 26 有 5 个 figures 密集排列，axis labels 偏小。\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 加权共识 |\n|------|----|----|----------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.5 |\n| Reproducibility | 3.5 | 4.0 | 3.5 |\n| Overall | 3.5 | 3.0 | 3.0 |\n| Confidence | 4 | 4 | 4 |\n\n**评分理由：**\n\n论文的实验规模和方法论严谨程度值得肯定（Soundness 3.5），oracle 控制设计精妙，Limitations 节诚实全面。但多个关键弱点将论文限制在 Findings 水平：\n\n1. **新颖性不足**（Excitement 2.5）：SCB 是 self-correction failure（Huang 2024）在 FOL 载体上的实例化，可从已有文献合理预期。主要贡献在量化深度（BR=4.97×, 27 策略系统排除）而非新现象发现。DRC 是标准 cascade 设计，不构成方法论创新。\n\n2. **标题和 framing overclaiming**：标题声称 \"from 7B to Frontier Scale\" 但 frontier 实验非 self-extraction；\"Do Not Improve\" 绝对否定不被 power<21% 支撑；Contribution 2 是 Kish design effect 的直接应用而非新发现。\n\n3. **统计证据基础偏弱**：(a) 16/16 无显著正面但 power<21%，aggregate pattern 有信息量但未做 meta-analytic 分析；(b) 4-seed 复制仅 1 个条件，~4pp 跨 seed 波动使单 seed 结果不可靠；(c) capability-gap 核心正面贡献的 collapsed p=0.167 不显著。\n\n4. **正面贡献证据偏窄**：Cross-architecture NLI 仅在 ProofWriter (Mistral-7B) 上显著（BH 校正后）；DRC 在 2 个数据集上验证不足。\n\n**接收建议**：建议作为 **Findings paper** 接收，条件是修复标题 overclaiming、降低 SCB novelty claim、将 DRC 降级、统一正文与 Limitations 的 statistical framing。如果完成这些修改并补充 BR 控制实验和 aggregate sign test，有潜力升级为 Borderline Conference。\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息密度高但核心信息完整。需要：(1) 修改 \"from 7B to Frontier Scale\" 措辞；(2) 明确 27 strategies 的 scope 限于 training-free interventions；(3) \"we find no evidence of improvement\" 虽比标题审慎但应加 underpowered caveat。\n\n**Introduction (§1)**: 叙事结构清晰（SC 瓶颈 → CJT → SICA → 失败 → 诊断 → 逃逸）。需要：(1) 更早建立 formal channel distinction（Z3 provably sound, failure in extraction not verification）；(2) Contribution 2 承认是量化而非新发现；(3) Contribution 4 (DRC) 降级或加深。\n\n**Related Work (§2)**: 覆盖面广，~48 citations，5 个段落。Neuro-symbolic 三分类法（Specification/Program/Trace）是有用的组织框架，但应标注为作者分类而非 established taxonomy。与 Huang 2024 / Stechly 2025 / Wan 2025 的区分需在 Introduction 更早建立。\n\n**Background & Setup (§3)**: SICA pipeline 形式化完整（Eq. 1-5, Algorithm 1-2）。\"Empirical Finding 1/2\" 的定位恰当（相比此前版本的 Proposition/Bound 已改善）。\"Symbolic Mirage Hypothesis\" 命名偏 dramatic，建议改为 \"Symbolic Bias Inheritance\" 或 \"Extraction Bias Hypothesis\"。CIL 应重命名并降低 \"unify\" 声称。\n\n**Experiments (§4)**: Table 1 结构清晰，regime 分组有信息量。GSM8K (n=30) 和 AIME (n=22) 作为 degenerate 条件放在主表中可能给读者统计错觉——建议移至 appendix 或脚注。4-seed replication 仅 1 个条件，是最大统计弱点。\n\n**Analysis (§5)**: SCB 分析（BR=4.97×, 83.3% 约束支持错误答案）是论文最有力的分析，但 BR 可能存在循环论证。Process-level independence（cosine 0.69 > κ 0.46）分析有洞察力。27 策略汇总 Figure 应在正文。\n\n**Cross-Architecture (§6)**: ProofWriter +6.67pp (p<0.001) 是实质性结果。Capability-gap 分析有趣但 n=6 + shared verifier 制约结论强度。DRC τ=0.7 缺 sensitivity 分析。\n\n**Discussion (§7)**: 简洁有效。可与 Conclusion 合并省空间。\n\n**Conclusion (§8)**: 4 行过于简短。建议合并到 Discussion 末尾。\n\n**Limitations**: 全面诚实，覆盖 power、single-seed、capability-gap、计算成本等。是论文的优点。\n\n**Appendix**: ~18 页，内容丰富但 Table 15（frontier SCB）和 Figure 2（27 strategies）应在正文。Page 26 的 5 个 figures 偏小偏密。\n",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-22T01:20:32.112275+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4621
}
```

</details>

---


### Assistant

_source line 1312 · 2026-05-22T01:20:45.142512+00:00_

审稿报告已投递。

**Round 12 审稿完成。**

- **Overall Score: 3.0 (Findings)**
- **Reviewer 1**: 3.5 (Borderline Conference)
- **Reviewer 2**: 3.0 (Findings)
- **共识评分**: 3.0

**6 个 Must-Fix**：标题 overclaiming、SCB 新颖性不足、统计功效 <21%、单 seed 复制不足、Capability-gap 证据薄弱、DRC 贡献不足

**7 个 Should-Fix**：BR 循环论证、CIL 命名误导、Contribution 2 framing、Figure 2 placement、Appendix 信息分配、27 策略 scope 限定、K_eff 使用一致性

**核心判断**：实验规模和 oracle 控制设计精妙，但 SCB 是 self-correction failure 的 expected outcome，正面贡献（cross-arch escape, DRC）证据偏窄。建议 Findings 接收，修复标题和 framing 后有升级潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 86

## Round 86

2 recorded events


### User

_source line 1313 · 2026-05-22T01:20:47.855378+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。汇总：

- **Must-Fix N1-N3**: 全部 [AGREE]，特别是统计 power 不足和 capability-gap 证据薄弱
- **Should-Fix W1-W3**: 全部 [AGREE]，其中 W1（BR 循环论证）是 R1 提出的我之前未注意到的重要问题
- **Should-Fix W4**: [REBUT] — 训练式提取器超出论文界定的 zero-cost self-extraction 研究范围，且论文已明确承认这是最重要的未来方向
- **Should-Fix W5**: [REBUT] — κ 作为 ordinal diagnostic 使用时 r=0.625 足够，且 K_eff 不是核心结论的支柱
- **小问题**: 大部分 [AGREE]，Conclusion 简短 [REBUT]（8 页限制下合理）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1314 · 2026-05-22T01:21:05.158482+00:00_

审稿报告已投递完成。

**Round 12 审稿总结：**

- **Overall Score: 3.0 (Findings)**
- **2 位 Reviewer**：R1 给 3.5（Borderline Conference），R2 给 3.0（Findings）
- **6 个 Must-Fix 共识**：标题 overclaiming（frontier 非 self-extraction）、SCB 新颖性不足、统计功效 <21%、单 seed 复制不足、capability-gap 证据薄弱（collapsed p=0.167）、DRC 贡献不足
- **7 个 Should-Fix**（5 共识 + 2 分歧）：BR 循环论证、CIL 命名误导、Contribution 2 framing、Figure 2 placement、Appendix 信息分配、trained extractor scope（分歧）、K_eff 验证（分歧）
- **视觉审查**：3 warnings（display item 密度偏低、Figure 2 在 page 25）
- **外部审稿**：未请求
- **Issue Tracker**：已同步更新，新增 7 个 open issues（R12-N1 至 R12-W4）

报告已通过 `submit_review_report_to_research_director` 投递给 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 87

## Round 87

78 recorded events


### User

_source line 1315 · 2026-05-22T07:38:16.957866+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-22T07:38:23.438073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-22T07:38:23.489385+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-22T07:38:26.505079+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,WebSearch",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,WebSearch",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-22T07:38:26.505526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-22T07:38:30.632797+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-22T07:38:30.633320+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-22T07:38:37.263969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-22T07:38:37.265030+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-22T07:38:42.088032+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-22T07:38:43.143567+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (161 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-multi-seed-qwen25: Multi-seed replication (seeds 123,456,789) of Qwen2.5-14B × FOLIO-204 and ProofWriter-600 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42: FOLIO Δ=-1.96pp, PW Δ=-2.00pp. Addresses W4 reviewer concern.（准备中）\n- exp-multi-seed-mistral-pw: Multi-seed replication (seeds 42,123,456,789) of Mistral-7B × ProofWriter-600 shows consistent Δ(SICA-SC) direction across seeds, confirming single-seed results are not artifacts of random sampling. Addresses W4 reviewer concern about reproducibility.（准备中）\n- exp-013-constraint-ablation: MaxSAT satisfiability checking contributes minimal accuracy gains over naive constraint counting, because extracted constraints are too homogeneous (trace co-sourcing) to provide discriminative satisfiability signals. If SICA-MaxSAT ≈ SICA-count-only, the SAT solver is not the bottleneck — constraint quality is.（准备中）\n- exp-d135-frontier-scb: 2026 frontier closed-source models (Claude/GPT/Gemini via OpenRouter) also exhibit SCB: self-extracted constraints will show BR≥2× with SICA≈SC, extending the scale-invariance finding from open-source 7B-72B to frontier closed-source models.（准备中）\n- exp-d126-r1-distill-sica: Reasoning
…[truncated 1730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-22T07:38:43.294761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-22T07:38:46.012400+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Show No Evidence of Improving LLM Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\vspace{-1mm}
75	\section*{Limitations}
76	\input{limitations_content}
77	
78	\bibliography{references}
79	
80	\appendix
81	\input
…[truncated 36 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 2717
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-22T07:38:46.164101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1329 · 2026-05-22T07:38:46.417110+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1330 · 2026-05-22T07:38:46.618535+00:00_

-rw-r--r-- 1 ubuntu ubuntu 632016 May 22 05:54 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-22T07:38:55.561231+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

Based on the search results from aclweb.org, here are the key submission guidelines and author instructions for ACL Rolling Review (ARR) 2026:

## Paper Format and Templates

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can also be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. All submissions must be in PDF format.

## Anonymity Policy

Under the new policy, submissions will remain anonymous during peer review, but authors are free to post and discuss non-anonymous preprints at any time. To protect
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 9397
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-22T07:39:01.148994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 1333 · 2026-05-22T07:39:02.567433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-22T07:39:02.971256+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-22T07:39:07.317471+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here's the key information about EMNLP 2026 call for papers submission deadline and ARR commitment:

## ARR Submission Deadline

The ARR submission dea
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6168
}
```

</details>

---


### Tool result

_source line 1336 · 2026-05-22T07:39:09.330509+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines aclrollingreview.org"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format, page limits, and guidelines:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages. Sections on ethical considerations and limitations do not count towards the page limit.

Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references. Similarly, final versions of short papers may have up to five (5) pages, plus unlimited pages fo
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6763
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-22T07:39:09.331176+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 147\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6359
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-22T07:39:21.230387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-22T07:39:21.732710+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B) on three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find no evidence of improvement (aggregate sign test: 5+/10$-$, $p = 0.30$; none of sixteen non-degenerate conditions shows a significant positive effect after FDR control), with equivalence established in four conditions, significant degradation in two, and ten remaining underpowered for effects below ${\sim}$5\,pp.
4	We trace the failure to \emph{symbolic confirmation bias} (SCB): on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), but a shuffle control shows this bias is structural---it reflects trace-count distributions rather than extraction-specific error ($\text{BR}_\text{obs} \approx \text{BR}_\text{null}$, $p > 0.7$). MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems, confirming that the formal verification layer adds no information beyond majority voting despite 99\% of constraints passing Z3 validation.
5	Cross-model extraction confirms SCB universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$), though frontier models use cross-model rather than self-extraction.
6	Twenty-seven training-free remediation strategies spanning fifteen families all fail, confirming a persistent independence-accuracy trade-off.
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp, $+14.22$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures only ${\sim}$12\% of this c
…[truncated 217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-22T07:39:21.733549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-22T07:39:22.135081+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ as an ordinal diagnostic of vote diversity ($K
…[truncated 6332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-22T07:39:22.135441+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-22T07:39:22.637513+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). We additionally evaluate SCB universality via cross-model extraction on five frontier models (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro; Table~\ref{tab:frontier-scb}), where Mistral-7B extracts constraints from the target model's traces since closed-source APIs do not expose internals suitable for self-extraction.
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions (sorted by SC). N
…[truncated 4715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-22T07:39:23.072579+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-22T07:39:23.095043+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 22
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-22T07:39:33.711688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-22T07:39:33.912771+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\looseness=-1 We test the three predictions of the symbolic mirage hypothesis (\S\ref{sec:mirage}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	\looseness=-1 Table~\ref{tab:independence} (Appendix) reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$ as an ordinal diagnostic: higher $K_{\text{eff}}$ indicates greater vote diversity, though it should not be interpreted as a literal effective sample size (\S\ref{sec:condorcet}). Across four Mistral-7B seeds, $\kappa \in [0.41, 0.51]$ yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp, indicating seed-level constraint quality matters beyond independence. Positive $\Delta$ requires both sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ degrades). All four model families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
10	
11	
12	\subsection{Symbolic Confirmation Bias}
13	\label{sec:confirmation-bias}
14	
15	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. A shuffle control reveals this bias is \emph{structural}: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate})
…[truncated 6005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-22T07:39:33.913301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-22T07:39:33.913693+00:00_

1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	\looseness=-1 We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), whose (premise, conclusion) structure suits NLI classification.
7	
8	\paragraph{Main result.}
9	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo $w{=}3$ yields $+2.94$\,pp (n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). After BH correction ($m{=}12$), only Mistral-7B ProofWriter conditions ($w{=}3$, $w{=}5$) remain significant.
10	
11	\paragraph{Why it works.}
12	\looseness=-1 Three conditions jointly enable the escape: (i)~\emph{structural independence}---encoder-only DeBERTa and decoder-only Mistral share no architecture or training data (\S\ref{sec:mirage}); (ii)~\emph{positive capability gap}---verifier standalone accuracy exceeds generator SC; (iii)~\emph{task-verifier alignment}---NLI classification naturally matches premise-conclusion structure. Per-label complementarity shows NLI and SC excel on complementary labels (Appendix~\ref{app:multi-nli}); all three NLI architectures produce significant gains at $w \geq 3$.
13	
14	\enlargethispage{2\baselineskip}
15	\paragraph{Capability gap hypothesis.}
16	\looseness=-1 Four generators spanning a 46-point SC range on ProofWriter ($n{=}600$),
…[truncated 2842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-22T07:39:34.466208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-22T07:39:34.918216+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early; \citet{byerly2026selfconsistency} further analyze SC's limitations in mathematical reasoning. Alternative aggregation strategies beyond majority voting \citep{ai2025beyondmajority} have been proposed but do not address the underlying correlation problem. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	We distinguish three paradigms. \emph{Specification-generation} (Logic-LM \citep{pan2023logiclm}, LINC \citep{olausson2023linc}, SatLM \citep{ye2024satlm}) translates problem descriptions into formal specifications before any answer is generated; LINC documents ${\sim}$40\% translation errors even at this level. \emph{Program-generation} \citep{gao2023pal,chen2023program,lyu2023faithful} produces executable code from problem statements. Both paradigms access the problem before generating candidate answers. \emph{Trace-extraction} (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). SatLM provides a natural control: it succeeds because problem-level formalization precedes answer generation, whereas trace-level extraction cannot avoid contamination (\S\ref{sec:mirage}). Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logic
…[truncated 3211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-22T07:39:35.069577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-22T07:39:35.170467+00:00_

1	\vspace{-2mm}
2	\section{Discussion and Conclusion}
3	\label{sec:discussion}
4	\label{sec:conclusion}
5	\enlargethispage{2\baselineskip}
6	
7	\paragraph{Self-verification and the formal-layer bottleneck.}
8	\looseness=-1 Our bias ratio ($1.66$--$4.97\times$ across nine models; Table~\ref{tab:frontier-scb}) quantifies why self-correction fails without external feedback \citep{huang2024selfcorrect, stechly2025selfverification, chen2025sets}: extraction and generation share distributional biases. The shuffle control shows this bias is structural, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems---the formal layer is vacuous despite being provably sound. Cross-model extraction gain requires both diverse traces (low $\kappa_{\text{proc}}$) and substantial self-bias (high BR); neither alone suffices (Table~\ref{tab:process-gradient}).
9	
10	\paragraph{Test-time scaling and practitioner implications.}
11	\looseness=-1 Vote diversity is low ($K_{\text{eff}} = 1.20$--$3.62$ for nominal $K = 12$), intensifying with capability ($K_{\text{eff}} = 1.09$ for Qwen3 thinking), creating a scaling challenge for o1/R1-style models \citep{guo2025deepseekr1}. All training-free interventions cluster at $\kappa \geq 0.40$ \citep{krogh1994neural}; cross-architecture escape succeeds ($p = 0.003$) because encoder-only and decoder-only models have structurally different error profiles. In sum, SCB renders the formal layer redundant ($\text{BR} = 4.97\times$); three diagnostics ($K_\text{eff}$, BR, $C_0$) predict failure and when cross-architecture escape succeeds.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-22T07:39:40.249246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-22T07:39:40.550988+00:00_

1	\looseness=-1 Open-source models range from 7B to 32B parameters with self-extraction; frontier models confirm SCB universality but use cross-model extraction via Mistral-7B, as closed-source APIs do not expose internals---whether self-extraction on frontier models would yield different BR values remains untested. All datasets are English-language logical reasoning benchmarks; we do not evaluate trained symbolic extractors, multilingual settings, or commonsense domains lacking gold annotations. McNemar power is below 21\% for $|\Delta| = 2$\,pp at $n{=}200$--$600$, meaning small true effects may go undetected; most conditions use a single seed (four-seed $\Delta$ range spans ${\sim}4$\,pp). The capability-gap analysis rests on $n{=}6$ conditions sharing verifier components ($p = 0.167$ after collapsing); we characterize it as a consistent pattern rather than a confirmed law. SICA requires $4.5\times$ the wall-clock time of SC with no significant accuracy gain. Extended limitations are discussed in Appendix~\ref{app:limitations-extended}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-22T07:39:40.551365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1357 · 2026-05-22T07:39:40.954411+00:00_

1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. $K_{\text{eff}}$ should be interpreted as an ordinal diagnostic---ranking which conditions have genuine vote diversity---rather than as a literal effective sample size. Fleiss' $\kappa$ is a chance-corrected agreement measure, not identical to the ICC ($\rho$) in \citeauthor{kish1965survey}'s (\citeyear{kish1965survey}) original formula; we validated their monotonic relationship empirically (mean pairwise $r = 0.625$ across model families). This independence limitation motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at 
…[truncated 5543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-22T07:39:40.954919+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-22T07:39:41.005347+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-22T07:39:45.483965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-22T07:39:46.288370+00:00_

1	\section{Regime Scatter Plot}
2	\label{app:regime-scatter}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{f2_regime_scatter}
7	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.112$).}
8	\label{fig:regime-scatter}
9	\end{figure}
10	
11	\section{Prompt Templates}
12	\label{app:prompts}
13	
14	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
15	
16	\paragraph{System Prompt.}
17	
18	\begin{lstlisting}
19	You are a constraint extraction tool. Output ONLY
20	valid JSON. Do NOT solve problems, reason about
21	correctness, or think step-by-step. Extract
22	constraints from the given trace exactly as stated.
23	\end{lstlisting}
24	
25	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
26	
27	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
28	
29	\begin{lstlisting}
30	Extract mathematical constraints from this reasoning
31	trace as a JSON object.
32	
33	Rules:
34	- type: "equation", "inequality", or "predicate"
35	- expression: human-readable, e.g. "x + y == 14"
36	- z3_formula: a single comparison expression in
37	  Python Z3 syntax
38	- source_step: step number where the constraint
39	  appears
40	- Use variable names from the trace
41	
42	z3_formula MUST follow these rules:
43	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
44	  /, **, %
45	- Use individual named variables
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-22T07:39:46.339639+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-22T07:39:47.194619+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-22T07:39:47.346153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-22T07:39:47.999788+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf (617.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-22T07:39:55.712375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-22T07:39:56.616599+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-22T07:39:56.667332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
  "description": "Find config files in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
    "description": "Find config files in workspace"
  }
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-22T07:39:56.768809+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-22T07:40:00.592079+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
  "description": "Search for config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10",
    "description": "Search for config files"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-22T07:40:01.094788+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/cross_representation_disagreement_diagno.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-22T07:40:01.349080+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/ -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -i config | head -10",
  "description": "Search agent-ml-research config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research/ -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -i config | head -10",
    "description": "Search agent-ml-research config"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-22T07:40:01.450143+00:00_

/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-22T07:40:05.026094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-22T07:40:05.227541+00:00_

1	execution:
2	  gpu_constraint: westd-25068:cuda:0,cuda:1,cuda:2,cuda:3
3	  gpu_ids:
4	  - westd-25068:cuda:0
5	  - westd-25068:cuda:1
6	  - westd-25068:cuda:2
7	  - westd-25068:cuda:3
8	  - westd-16639:cuda:0
9	  - westd-16639:cuda:1
10	  - westd-16639:cuda:2
11	  - westd-16639:cuda:3
12	  project_path: /root/symb_invariant_consensus
13	  servers:
14	  - westd-25068
15	  - westd-16639
16	feishu:
17	  chat_id: oc_970d5ea3f54df81296b97321fcded892
18	  check_references: false
19	  operational_chat_id: oc_319977a04ca60b6c4c69a2a8d4141a75
20	  review_mode: fresh
21	  review_paper_path: projects/symb_invariant_consensus/docs/paper/main.tex
22	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf
23	  review_round: 10
24	  review_supplementary_paths: ''
25	  submission_chat_id: oc_c338e034cbffa10b9cc723e731d288d8
26	project:
27	  created_at: '2026-05-15T08:44:44.820Z'
28	  description: Formally-Verified Intermediate Constraint Consensus Across Reasoning
29	    Paths
30	  name: symb_invariant_consensus
31	  phase: research
32	  source_idea_id: idea_013
33	venue: emnlp-2026
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-22T07:40:05.228016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-22T07:40:05.280112+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-22T07:40:24.033211+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-22T07:40:24.083948+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-22T07:40:27.447991+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-22T07:40:27.649087+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-22T07:40:51.465959+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 任务并等待审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 任务并等待审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-22T07:40:51.466457+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-22T07:41:03.834097+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 任务并等待审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 任务并等待审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-22T07:41:03.834518+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-22T07:41:05.996022+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-22T07:41:32.417271+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26421
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-22T07:41:32.569109+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long paper（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind review\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- **LaTeX**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf`\n\n### 论文概要\n\"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\" — 一篇负面结果论文。提出 SICA（Symbolic Invariant Consensus Aggregation），从推理 trace 中提取逻辑约束并通过 MAX-SAT 选择答案，但在 6 个模型、3 个领域、3000+ 条件评估中未发现显著改善。核心发现是 symbolic confirmation bias (SCB)：自提取约束系统性地支持模型错误答案（BR 4.97×）。27 种无训练修复策略均失败。跨架构 NLI 验证可突破瓶颈（+6.67pp, p<0.001）。\n\n### 你的审查侧重（方法严谨性 + 实验有效性）\n请重点审查以下方面：\n\n1. **SICA 管线设计**：\n   - MAX-SAT 公式化是否合理？权重方案是否有理论依据？\n   - 约束提取 prompt 设计是否存在系统偏差？\n   - α=0.5 参数选择是否充分论证？\n   - Deduplication 策略（syntactic equivalence）是否足够？\n\n2. **统计方法**：\n   - McNemar 检验是否适用于此场景？样本量是否充分？\n   - BH 校正的 m=16 选择是否合理？\n   - TOST 等价检验的 ±2pp margin 是否有充分理由？\n   - Bootstrap CI 和 sign test 的使用是否正确？\n   - 4-seed replication 是否足以支撑结论？\n\n3. **实验控制**：\n   - Oracle control 是否充分证明了机制的正确性？\n   - Shuffle control 对 SCB 的论证是否严密？\n   - Cross-model extraction 是否真正控制了混杂因素？\n   - Degenerate regime (C₀ < 5%) 的处理是否合理？\n\n4. **Claims vs Evidence**：\n   - \"no evidence of improvement\" 的表述是否与统计结果匹配（注意 underpowered 问题）？\n   - BR 4.97× 的计算方法是否无偏？\n   - 94.4% MAX-SAT≡count-only 的结论是否过度简化？\n   - Cross-architecture proof-of-concept (n=6) 的 capability gap hypothesis 证据是否充分？\n\n5. **可重复性**：\n   - 实验参数（K=12, T=0.7, T_ext=0.3）的选择是否充分论证？\n   - 代码/数据是否可复现？\n\n请按 ARR 标准出具完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long paper（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind review\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- **LaTeX**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf`\n\n### 论文概要\n\"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\" — 一篇负面结果论文。提出 SICA（Symbolic Invariant Consensus Aggregation），从推理 trace 中提取逻辑约束并通过 MAX-SAT 选择答案，但在 6 个模型、3 个领域、3000+ 条件评估中未发现显著改善。核心发现是 symbolic confirmation bias (SCB)：自提取约束系统性地支持模型错误答案（BR 4.97×）。27 种无训练修复策略均失败。跨架构 NLI 验证可突破瓶颈（+6.67pp, p<0.001）。\n\n### 你的审查侧重（方法严谨性 + 实验有效性）\n请重点审查以下方面：\n\n1. **SICA 管线设计**：\n   - MAX-SAT 公式化是否合理？权重方案是否有理论依据？\n   - 约束提取 prompt 设计是否存在系统偏差？\n   - α=0.5 参数选择是否充分论证？\n   - Deduplication 策略（syntactic equivalence）是否足够？\n\n2. **统计方法**：\n   - McNemar 检验是否适用于此场景？样本量是否充分？\n   - BH 校正的 m=16 选择是否合理？\n   - TOST 等价检验的 ±2pp margin 是否有充分理由？\n   - Bootstrap CI 和 sign test 的使用是否正确？\n   - 4-seed replication 是否足以支撑结论？\n\n3. **实验控制**：\n   - Oracle control 是否充分证明了机制的正确性？\n   - Shuffle control 对 SCB 的论证是否严密？\n   - Cross-model extraction 是否真正控制了混杂因素？\n   - Degenerate regime (C₀ < 5%) 的处理是否合理？\n\n4. **Claims vs Evidence**：\n   - \"no evidence of improvement\" 的表述是否与统计结果匹配（注意 underpowered 问题）？\n   - BR 4.97× 的计算方法是否无偏？\n   - 94.4% MAX-SAT≡count-only 的结论是否过度简化？\n   - Cross-architecture proof-of-concept (n=6) 的 capability gap hypothesis 证据是否充分？\n\n5. **可重复性**：\n   - 实验参数（K=12, T=0.7, T_ext=0.3）的选择是否充分论证？\n   - 代码/数据是否可复现？\n\n请按 ARR 标准出具完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-22T07:41:53.608819+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21039
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-22T07:41:53.812667+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long paper（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind review\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- **LaTeX**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf`\n\n### 论文概要\n\"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\" — 一篇负面结果论文。提出 SICA，在 6 个模型、3 个领域上系统评估自提取符号约束的效果，发现 symbolic confirmation bias (SCB) 导致约束退化为多数投票。提出诊断工具包（K_eff, BR, C₀）和跨架构逃逸方案。\n\n### 你的审查侧重（新颖性 + 完整性 + 写作质量）\n请重点审查以下方面：\n\n1. **贡献新颖性与显著性**：\n   - 作为负面结果论文，SCB 的发现是否足够 novel？是否已有先验工作预示了这个结论？\n   - \"Symbolic Mirage Hypothesis\" 是否提供了超越 Huang et al. (2024) self-correction 和 Stechly et al. (2025) 的新见解？\n   - 三个诊断指标（K_eff, BR, C₀）是否真正原创，还是已有概念的简单适配？\n   - Cross-architecture proof-of-concept 是否足够成为独立贡献？\n   - 对 EMNLP 社区的影响力评估——这项工作改变了什么？\n\n2. **Related Work 完整性**：\n   - 是否遗漏了重要的 neuro-symbolic reasoning 工作？\n   - Self-correction / self-verification 文献是否覆盖充分？\n   - CJT 在 LLM 中的应用是否有遗漏的 concurrent work？\n   - 与 CoT unfaithfulness 文献的区分是否清晰？\n\n3. **论文结构与叙事**：\n   - 8 页内容密度极高——信息过载还是恰到好处？\n   - Introduction 的 story arc 是否清晰？动机 → 方法 → 发现 → 意义 的流畅度如何？\n   - Figure 1 (pipeline) 和 Figure 2 (interventions) 是否有效传达核心信息？\n   - Table 1 (main results) 的排版和可读性如何？\n   - Empirical Finding 1 和 2 的 tcolorbox 框——是否适合负面结果论文的语境？\n   - Discussion/Conclusion 是否过于简短？是否充分讨论了 implications？\n\n4. **写作质量**：\n   - 术语一致性（SCB, BR, K_eff, C₀ 等缩写是否在首次使用时定义）\n   - 数学符号的清晰度\n   - 过度压缩（\\looseness=-1 等 TeX hacks）是否影响可读性？\n   - Limitations 部分是否充分覆盖关键局限？\n\n5. **格式合规性**：\n   - 正文是否在 8 页内？\n   - 匿名是否完整（无 GitHub 链接、致谢等泄漏身份的内容）？\n   - 引用格式是否符合 ACL 规范？\n   - 附录规则是否遵守？\n\n请按 ARR 标准出具完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long paper（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献无限，Limitations/Ethics 不计入页数\n- **模板**: ACL style template（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind review\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文文件\n- **LaTeX**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf`\n\n### 论文概要\n\"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\" — 一篇负面结果论文。提出 SICA，在 6 个模型、3 个领域上系统评估自提取符号约束的效果，发现 symbolic confirmation bias (SCB) 导致约束退化为多数投票。提出诊断工具包（K_eff, BR, C₀）和跨架构逃逸方案。\n\n### 你的审查侧重（新颖性 + 完整性 + 写作质量）\n请重点审查以下方面：\n\n1. **贡献新颖性与显著性**：\n   - 作为负面结果论文，SCB 的发现是否足够 novel？是否已有先验工作预示了这个结论？\n   - \"Symbolic Mirage Hypothesis\" 是否提供了超越 Huang et al. (2024) self-correction 和 Stechly et al. (2025) 的新见解？\n   - 三个诊断指标（K_eff, BR, C₀）是否真正原创，还是已有概念的简单适配？\n   - Cross-architecture proof-of-concept 是否足够成为独立贡献？\n   - 对 EMNLP 社区的影响力评估——这项工作改变了什么？\n\n2. **Related Work 完整性**：\n   - 是否遗漏了重要的 neuro-symbolic reasoning 工作？\n   - Self-correction / self-verification 文献是否覆盖充分？\n   - CJT 在 LLM 中的应用是否有遗漏的 concurrent work？\n   - 与 CoT unfaithfulness 文献的区分是否清晰？\n\n3. **论文结构与叙事**：\n   - 8 页内容密度极高——信息过载还是恰到好处？\n   - Introduction 的 story arc 是否清晰？动机 → 方法 → 发现 → 意义 的流畅度如何？\n   - Figure 1 (pipeline) 和 Figure 2 (interventions) 是否有效传达核心信息？\n   - Table 1 (main results) 的排版和可读性如何？\n   - Empirical Finding 1 和 2 的 tcolorbox 框——是否适合负面结果论文的语境？\n   - Discussion/Conclusion 是否过于简短？是否充分讨论了 implications？\n\n4. **写作质量**：\n   - 术语一致性（SCB, BR, K_eff, C₀ 等缩写是否在首次使用时定义）\n   - 数学符号的清晰度\n   - 过度压缩（\\looseness=-1 等 TeX hacks）是否影响可读性？\n   - Limitations 部分是否充分覆盖关键局限？\n\n5. **格式合规性**：\n   - 正文是否在 8 页内？\n   - 匿名是否完整（无 GitHub 链接、致谢等泄漏身份的内容）？\n   - 引用格式是否符合 ACL 规范？\n   - 附录规则是否遵守？\n\n请按 ARR 标准出具完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-22T07:41:55.748531+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1935
}
```

</details>

---


### Assistant

_source line 1392 · 2026-05-22T07:42:01.101194+00:00_

已完成以下并行派发：
- ✅ 视觉审查 Agent 已启动（fire-and-forget）
- ✅ Reviewer 1（方法严谨性 + 实验有效性）已分配
- ✅ Reviewer 2（新颖性 + 完整性 + 写作质量）已分配

等待两位 Reviewer 返回 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 88

## Round 88

4 recorded events


### User

_source line 1393 · 2026-05-22T07:49:08.675945+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1（新颖性 + 完整性 + 写作质量）

**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论扎实、统计严谨的负面结果论文，SCB 机制的系统性表征对社区有实用价值，但核心发现部分被先验工作预示，跨架构逃逸方案过于初步，整体新颖性不足以稳进主会议。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 实验设计严谨（FDR校正、bootstrap CI、TOST等价检验、shuffle/oracle控制）；但部分条件统计功效不足（Appendix E, Table 6），且模型范围限于开源7B-32B（主实验） |
| Excitement | 2.5 / 5 | 负面结果本身有价值，但核心发现（自提取无法提供独立验证信号）部分被 Huang et al. (2024) 的 self-correction 局限和 Stechly et al. (2025) 的 LLM 生成逻辑不可靠结论所预示；诊断工具实用但概念上是已有统计量的直接适配 |
| Reproducibility | 4 / 5 | 附录极详尽（14+页），含完整 prompt 模板（Appendix B）、算法伪代码（Appendix C Algorithm 1-2）、per-condition 分析；受匿名限制未提供代码 |
| Overall Assessment | 3.5 / 5 | Borderline Conference — Findings 级别确定达标（方法论扎实+有用的负面结果），主会议需要更强的新颖性/影响力信号 |
| Confidence | 4 / 5 | 仔细阅读全文及全部附录，熟悉 SC / neuro-symbolic reasoning 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 跨架构逃逸方案（Section 6）作为独立贡献证据不足

- 具体位置：Section 6 (page 8), Table 3
- 问题：Section 6 的跨架构 proof-of-concept 被列为三大贡献之一（page 2, Contribution 3: "Process-level independence analysis"），但实证基础极为有限：仅测试了一个 NLI 验证器（DeBERTa-large-mnli）在两个数据集（FOLIO, ProofWriter）上的表现。虽然结果正向（Table 3: Mistral-7B FOLIO combo gain +29.90 pp），但存在关键缺口：(1) 仅当生成器能力显著弱于验证器时有效——论文自己承认 "significant gains exist only when the verifier exceeds the generator"（page 8），这本质上是在说引入更强模型就能改善结果，这不意外；(2) 未测试不同规模/类型的验证器（如小型 NLI 模型、不同预训练范式的模型），无法判断 "跨架构" 中哪个因素（架构差异 vs. 能力差距 vs. 训练数据分布差异）起决定性作用；(3) 未讨论验证器自身错误的传播——如果验证器在某些问题类型上有系统性偏差，是否会引入新的 bias？
- 为什么影响接收：如果这只是一个 preliminary observation，将其列为正式贡献会过度承诺（overclaim）。审稿人和读者期望一个被声称为贡献的结果有足够的实验支撑。
- 建议修改方向：(a) 将贡献声明调整为 "preliminary evidence suggesting cross-architecture verification as a promising direction"，在 page 2 的贡献列表中用更谨慎的措辞；或 (b) 增加至少 2-3 个不同验证器的实验（如 RoBERTa-MNLI, BART-MNLI，附录 Table 25-26 中已有部分数据但未纳入正式贡献论述），并讨论什么条件下跨架构验证失效。

**N2** [critical] "No Evidence" 标题声明与统计功效之间存在张力

- 具体位置：Title, Abstract (page 1), Appendix E Table 6 (page 14), Appendix F Table 7 (page 14)
- 问题：标题 "Show No Evidence of Improving" 是一个强的否定性声明。然而论文自身的功效分析（Appendix E）揭示了显著的检测力局限：
  - Table 6：16 个条件中，7 个条件的 minimum detectable effect (MDE) 在 80% power 下为 ≥4.64 pp，意味着这些条件无法检测到 4 个百分点以下的改进
  - 剩余 2 个条件（Qwen2.5-14B FOLIO/PW, n=200）功效极低（observed power < 20%），论文自己标注为 "serve only as regime characterization"
  - TOST 等价检验（Table 7, ±2pp margin）中，所有 3 个被检验条件的 95% CI 均包含零，但也包含正值——最窄的 CI 为 Qwen-14B FOLIO [-1.12, +1.62]，无法排除 +1.6pp 的小正效果
  - 论文正文（Section 4.2, page 5）确实说 "no non-degenerate condition shows a significant positive effect after FDR control"，这是准确的，但标题的 "No Evidence" 在修辞力度上超出了统计结论所能支撑的范围
- 为什么影响接收：对负面结果论文而言，声明与证据的匹配度是核心评审标准。"No evidence" 在日常学术用语中容易被理解为 "效果已被排除"，而实际上论文只是 "未检测到显著效果"——在部分条件下检测力本身就不足以区分无效果与小正效果。这个 framing gap 会被专业审稿人注意到。
- 建议修改方向：(1) 标题可调整为 "Show No Reliable Evidence" 或 "Fail to Improve"（更准确反映实际发现）；(2) 在 Abstract 中增加一句关于 MDE 的限定（如 "with minimum detectable effects of 2-5 percentage points"）；(3) 将 Appendix E 的功效讨论提升到正文（至少在 Section 4.2 中增加一段）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 符号/指标过载——8 页内引入过多定量工具

- 具体位置：Sections 3-5, Equations (1)-(7)
- 问题：正文 8 页内引入了至少 7 个定量指标：K_eff (Eq. 1), Fleiss' κ, BR (Eq. 5), C₀ (Eq. 4), CCR (Eq. 7), ProcessSim (Eq. 6), ρ_same。每个指标都有独立定义、解释和实证分析。对读者的认知负担很重——首次阅读到 Section 5.4 的 CCR (Eq. 7) 时，已经需要同时在脑中维持 6 个不同指标的含义和关系。部分指标间的层次关系（如 K_eff 是 κ 的推导、C₀ 是 BR 的简化版）在首次出现时不够清晰。
- 建议：考虑将 ProcessSim (Section 5.3) 和 CCR (Section 5.4) 移至附录。正文聚焦 K_eff（独立性诊断）、BR（偏差方向）、C₀（退化检测）三个核心指标即可支撑全部核心论点。释放的空间可用于扩展 Discussion（见 W2）。

**W2** [warning] Discussion/Conclusion 过于压缩，与负面结果论文的预期不符

- 具体位置：Section 7 (page 8, 约半页)
- 问题：Section 7 试图在约半页内讨论三个重要话题：(1) self-verification 与 formal layer bottleneck, (2) test-time scaling 含义, (3) capability gap hypothesis。每个话题仅 1-3 句话。对于一篇声称 "改变我们对自提取约束理解" 的论文，这不够充分。具体缺失：
  - 对 test-time compute scaling 社区（o1, QwQ-32B 等 thinking models）的具体含义未展开——这些模型是否因为内部推理链更长而更容易逃逸 SCB？Table 1 已包含 QwQ-32B 数据但未在 Discussion 中深入分析
  - 对 neuro-symbolic 实践者的可操作建议缺失——什么条件下值得尝试 symbolic extraction？论文数据显示能力差距（Empirical Finding 2）是关键，但未给出明确的决策框架
  - SCB 与 CoT unfaithfulness (Turpin et al., 2023; Lanham et al., 2023) 的关系未讨论——SCB 是 CoT unfaithfulness 的一种特殊表现形式（约束反映答案分布而非推理过程），还是一个独立现象？
- 建议：将 W1 中建议移至附录的内容腾出的空间用于扩展 Discussion，至少覆盖上述三点中的前两点。

**W3** [warning] "Symbolic Mirage Hypothesis" 定位不一致

- 具体位置：Section 3.3 (page 4) vs. Section 5 (pages 6-7)
- 问题：Section 3.3 以 "Hypothesis" 形式提出 Symbolic Mirage（自提取约束是模型分布的投影），给出三个 "testable predictions"。但 Section 5 的分析直接以 "confirming SCB universality" (Section 5.1)、"SCB reflects a distributional prior" (Section 5.2) 等结论性措辞呈现结果，未在分析后显式回溯假设并宣布验证状态。这造成了认知上的不连贯：读者在 Section 3.3 被告知这是一个待验证的假设，但到 Section 5 时它已被默默当作事实使用。
- 建议：在 Section 5 结尾增加一个总结段落，显式回应 Section 3.3 的三个 predictions，声明哪些被验证（附证据引用）、哪些部分验证、哪些仍开放。

**W4** [warning] Table 1 核心结果表可读性不足

- 具体位置：Table 1 (page 6)
- 问题：作为论文最重要的结果表，Table 1 存在以下可读性问题：(1) 三个子区域（Type C: error amplification SC < 40%, Type A: confirmation bias SC < 60%, Degenerate: C₀ < 5%）的分隔仅靠 italic 小标题行，视觉层次不够——首次阅读时容易混淆三个区域的边界；(2) 显著性标记系统复杂：bold（p < 0.05）、* (†CI)、‡ (triple asterisk)、以及 "4-seed confirmatory" 脚注标记 a，需要反复查看表注才能理解；(3) Oracle 下界行（italic）与常规条件行混排，功能上是 calibration reference 但视觉上不容易区分。
- 建议：(a) 用更强的水平线或浅色底纹分隔三个子区域；(b) 简化显著性标记——考虑只保留 bold + asterisk 两种，其他移至附录详表。

**W5** [warning] CJT 适用性的边界条件讨论不足

- 具体位置：Section 3.1 (pages 3-4)
- 问题：CJT 需要两个前提：(1) 投票者准确率 p > 0.5，(2) 投票者独立性。论文详细分析了独立性违反（核心贡献），但对 p > 0.5 条件的适用边界讨论不足。具体地：
  - 当 SC accuracy 很高时（> 80%，如 Mistral-7B PW:D5 at 60.0% 其实不高... 但某些 easier subsets），CJT 已经快速收敛，增加约束的边际收益本身就很小——此时 SICA 无法改善 SC 不是因为 SCB，而是因为 ceiling effect
  - 当 SC accuracy < 50%（Type C 条件），p < 0.5 直接导致 CJT 反向运作（更多投票者反而更差），此时 SICA 失败的原因不仅是 SCB，还包括 CJT 前提本身不满足
  - 论文的 Empirical Finding 2 (Capability Gap Condition, page 5) 触及了这一点但未在 CJT 框架内显式讨论
- 建议：在 Section 3.1 增加 2-3 句，明确讨论 p > 0.5 条件对 high-accuracy 和 low-accuracy 两端的含义，以及这如何影响对 SICA 失败原因的归因。

---

## 小问题（不影响接收）

- **M1** (Related Work 缺引): Section 2 未引用 Chain-of-Verification (Dhuliawala et al., 2023)——该工作直接研究 LLM 自验证的局限，与 SCB 发现高度相关。
- **M2** (符号解释): Equation (1) 中 K_eff 的 κ 仅以括号引用 "(Fleiss, 1971)" 形式给出，对不熟悉该统计量的 NLP 读者缺少直觉解释。建议增加一句 "where κ measures pairwise agreement among traces, with κ = 0 indicating independence"。
- **M3** (Figure 2 标注): Figure 2 的 grey band "±1 pp noise zone" 在 caption 中未解释具体含义（是 measurement noise？random baseline variation？）。
- **M4** (Limitations 与实验范围不一致): Limitations (page 9) 称 "open-source models range from 7B to 128B parameters"（含 Table 2 frontier 测试），但标题/摘要仅提 "6 open-source LLMs (7B-32B)"。Table 2 (page 6) 实际还包含 gpt-4o, gpt-4.1, gpt-3.5, o3, Gemini-2.5-Pro 的跨模型提取结果，这些 frontier 模型的角色（作为约束提取源而非生成器）在正文中可以更明确地说明。
- **M5** (排版): 多处段落使用 `\looseness=-1`，Section 5 的 Analysis 子节（5.1-5.5）行间距偏紧，视觉上稍显拥挤。建议在最终版本中重新平衡内容分布。
- **M6** (术语): "Symbolic Mirage" 作为一个命名是否最准确？"Mirage" 暗示约束是幻觉/不存在的，但论文发现约束是真实存在的——只是它们反映了答案分布而非独立验证信号。"Symbolic Echo" 或 "Constraint Echo" 可能更准确地捕捉 "回声/复制" 的含义。（minor suggestion, 不要求修改。）

---

## Missing References

1. **Dhuliawala et al., 2023** — "Chain-of-Verification Reduces Hallucination in Large Language Models" — 直接研究 LLM 自验证策略的效果与局限，与 SCB 发现互补。
2. **Lightman et al., 2024** — Process reward models 相关工作——论文讨论了 process-level independence (Section 5.3, ProcessSim) 但未引用 process supervision 文献，这是 test-time compute scaling 中的核心方法。（注：论文引用列表中有一个 "Lightman" 在 page 2 cited inline，但我在 References 中未确认完整条目——如果已引用请忽略。）
3. 建议检查是否有 2025-2026 年的 concurrent work 研究 SC 的理论极限或 self-verification 的信息论分析。

---

## 主要优势

- **S1 实验覆盖与统计严谨**: 6 个主模型 + 5 个 frontier 模型、3 个推理领域、3000+ 条件评估，配合 FDR 校正、bootstrap CI、TOST 等价检验、shuffle/oracle 控制。这是负面结果论文的标杆级实验设计。特别赞赏 oracle control（Section 4.3）和 shuffle control（Section 5.2）的设计——前者建立了效果上界，后者证明偏差是结构性的而非提取错误。
- **S2 SCB 机制的发现**: BR > 1 across all nine architectures (Table 2) 是一个清晰、可复现的发现。"83.3% of self-extracted constraints support the wrong majority answer" (page 4) 配合 shuffle control 证明这是模型分布的结构性投影，而非约束提取模块的工程缺陷——这一区分对后续研究方向有重要指导意义。
- **S3 CJT 理论框架**: 将 SC/SICA 统一在 Condorcet Jury Theorem 的分析框架下，K_eff 将 "有效独立样本数" 这一直觉量化，为理解为什么简单增加采样数收益递减提供了理论解释。
- **S4 附录质量**: 14+ 页附录包含完整 prompt 模板（Appendix B）、MAX-SAT 算法伪代码（Appendix C）、per-condition 统计分析（Appendix E-F）、case studies（Appendix G）、failure mode taxonomy（Appendix O）、constraint quality analysis（Appendix T）。这对可复现性极为有利。
- **S5 叙事框架**: 作为负面结果论文，没有简单报告 "方法 X 不 work"，而是提出了机制性解释（SCB）+ 理论框架（CJT violation）+ 可操作诊断工具（K_eff, BR, C₀）+ 初步逃逸方案（cross-architecture）。这个叙事层次超越了多数负面结果论文。

---

## 格式合规性检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✅ | Sections 1-7 在 pages 1-8 内，Section 7 结束于 page 8 |
| Limitations | ✅ | 始于 page 8 底部，延续至 page 9 顶部，不计入页数限制 |
| 参考文献 | ✅ | Pages 9-11，无页数限制 |
| 匿名性 | ✅ | Title page 标注 "Anonymous ACL submission"，未发现 GitHub 链接、致谢或作者身份泄漏 |
| 引用格式 | ✅ | 使用 ACL 标准括号引用 + 文本引用格式 |
| 附录 | ✅ | Pages 11-24，Appendix A-Z + extended limitations |

---

**总结**: 这是一篇方法论上达到高标准的负面结果论文，SCB 的系统性表征和 CJT 框架对 test-time reasoning 社区有实际参考价值。主要短板在于：(1) 核心发现的新颖性增量有限（部分被先验工作预示），(2) 跨架构逃逸作为贡献证据不足，(3) Discussion 过于压缩。建议 Findings 接收，如能解决 N1-N2 并扩展 Discussion 则有可能升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-22T07:49:27.528101+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 收集 Reviewer 2 意见', 'status': 'completed', 'activeForm': '收集 Reviewer 2 审稿意见'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 意见', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 提交审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 收集 Reviewer 2 意见', 'status': 'completed', 'activeForm': '收集 Reviewer 2 审稿意见'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 1 意见', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 提交审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-22T07:49:27.578948+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1396 · 2026-05-22T07:49:32.569611+00:00_

Reviewer 2 关键发现已记录：
- **N1** [critical]: 跨架构逃逸方案作为独立贡献证据不足
- **N2** [critical]: "No Evidence" 标题与统计功效之间存在张力
- **W1-W5**: 符号过载、Discussion 压缩、Mirage Hypothesis 定位不一致、Table 1 可读性、CJT 边界条件
- **Overall**: 3.5（Borderline Conference），建议 Findings 接收

等待 Reviewer 1 回复中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 1397 · 2026-05-22T07:49:35.257464+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交至 Review Director。

核心判断：**Overall 3.5/5 (Borderline Conference)**，Soundness 4/5，Excitement 2.5/5。

两个 Must-Fix 问题：
1. **跨架构逃逸（Section 6）作为独立贡献证据不足** — 仅测试了一个 NLI 验证器在两个数据集上，无法支撑正式贡献声明
2. **"No Evidence" 标题与统计功效的张力** — 7/16 条件 MDE > 4.64pp，TOST CI 均包含正值，措辞力度超出证据支撑范围

五个 Should-Fix：符号过载（7 个指标挤在 8 页）、Discussion 过短（半页）、Symbolic Mirage Hypothesis 验证状态不清、Table 1 可读性、CJT 适用边界讨论不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1398 · 2026-05-22T07:49:41.623293+00:00_

已记录。仍在等待 Reviewer 1 提交审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 90

## Round 90

8 recorded events


### User

_source line 1399 · 2026-05-22T07:50:12.742363+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验有效性）

---

## 总体评分

**Overall**: 3.5 — Borderline Conference
**一句话总结**: 一篇方法论严谨、规模可观的负面结果论文，SCB 诊断是真正的贡献；但统计效力不足削弱了"无效"主张的说服力，跨架构 NLI 的建设性发现证据链尚不完整。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 实验设计严密（oracle/shuffle/cross-model 三重控制），统计方法总体正确，但 10/16 条件 underpowered 且 TOST margin 论证不够充分 |
| Excitement | 3/5 (Interesting) | SCB 现象的定量刻画和诊断工具（BR、CCR）有价值，但负面结果 + 初步的正面方向限制了影响力 |
| Reproducibility | 4/5 | 关键参数（K=12, T=0.7, T_ext=0.3）均有报告，prompt 模板完整列出（Appendix B），Z3 求解器配置清晰；但受 double-blind 限制未提供代码 |
| Confidence | 4/5 | 仔细阅读全文含 24 页附录，熟悉 Self-Consistency、CJT、MAX-SAT 相关工作 |

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束并通过加权 MAX-SAT 聚合来选择答案，试图突破 Self-Consistency (SC) 的瓶颈。在 6 个模型、3 个领域、3000+ 条件评估中未发现显著改善。论文将失败归因于 Symbolic Confirmation Bias (SCB)：自提取约束系统性地支持模型的多数答案（BR 最高达 4.97×），导致 MAX-SAT 在 94.4% 的情况下退化为简单计数。27 种无训练修复策略均失败。跨架构 NLI 验证在 ProofWriter 上获得 +6.67pp 提升（p<0.001）。

---

## 主要优势

**S1. 实验规模和系统性令人印象深刻。** 6 个开源模型 + 5 个前沿模型，3 个推理领域，~1,250 unique 实例，4-seed 复制，27 种修复策略——这远超典型负面结果论文的评估力度。Table 1（p6）和 Table 13（p18）清晰展示了这一规模。

**S2. 实验控制设计精巧。** Oracle control（§4.3, p5）用 gold 约束证明机制本身有效（+29.90pp），精准定位了瓶颈在约束质量而非聚合机制。Shuffle control（§5.2, p6-7）通过保持 trace-count 分布不变但随机化约束-答案映射，证明 SCB 是结构性偏差而非提取特异性错误（BR_shuffle ≈ BR_real, p>0.7）。这两个控制实验的设计水平高于大多数负面结果论文。

**S3. 诊断框架具有独立贡献。** Bias Ratio (BR)、Conditional Correction Ratio (CCR, Eq. 7, p7)、Process-level cosine similarity（§5.5, p7）构成了一套可复用的诊断工具包，可用于评估任何"自提取+聚合"范式。CCR 在 Table 23（Appendix）中展示了 cross-architecture 对 CCR>0 vs. same-model CCR<0 的清晰分离。

**S4. CJT 理论框架提供了原则性解释。** §3.1 和 §3.3 将 SC 和 SICA 放在 Condorcet Jury Theorem 框架下分析，Empirical Finding 1-2（p5）明确了有效性边界条件——独立性假设何时成立、能力差距如何调节增益——这比简单报告"不管用"更有理论深度。

**S5. 写作诚实审慎。** 标题措辞 "Show No Evidence" 而非 "Cannot Improve" 准确反映了统计结论的力度。Limitations 章节和 Appendix E 的 power analysis 坦诚承认了 underpowered 条件。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 摘要和正文中的 BR 数值选择性报告，有夸大嫌疑

- **具体位置**：Abstract（p1）, §5.2（p6）
- **问题**：摘要报告 "bias ratio 4.97×" 和 "83.3% of self-extracted constraints support the wrong majority answer"，但未说明这是 Mistral-7B/FOLIO 的**单一最极端条件**。Table 2（p7）显示 BR 的跨模型范围为 1.05（Gemini-2.5-Pro）到 4.97（Mistral-7B），前沿模型 o3 和 Gemini 的 BR 仅略高于 1（1.06 和 1.05）。将最极端值放在摘要中给读者造成"所有模型偏差都很严重"的印象，但实际上前沿模型的 SCB 几乎不存在。
- **为什么影响接收**：作为负面结果论文，SCB 是核心发现。如果 BR 在强模型上接近 1，说明 SCB 可能是弱模型的特有问题而非普遍规律，这直接影响论文 claim 的普适性。
- **建议修改方向**：摘要中报告 median BR 或范围（如 "BR ranges from 1.05 to 4.97, median X.X"），并明确前沿模型 SCB 显著弱于开源小模型。在 §5.2 中增加按模型规模/能力分层的 BR 分析。

**N2** [critical] 统计效力不足，但主张和呈现方式不够谨慎

- **具体位置**：§4.2（p5），Table 1（p6），Appendix E（p14）
- **问题**：16 个非退化条件中 10 个 underpowered（n≈200，MDE 远大于 2pp）。TOST 仅确认 4 个条件等价于零效应。Sign test 结果为 8/15 positive, p=0.21——这是**不确定**而非**否定**。但正文 §4.2 的表述 "No non-degenerate condition shows a significant SICA effect after FDR control" 虽然技术正确，却容易被读者误读为"confirmed null"。Appendix E 的 power analysis 是关键信息，但被埋在附录中。
- **为什么影响接收**：论文的核心价值在于说服读者"自提取约束确实无效"。如果效力分析不够显著地呈现在正文中，怀疑论者会认为这只是 underpowered study 而非 true null。
- **建议修改方向**：在 §4.2 主结果段落中增加一句明确的 power statement，如 "For the 10 underpowered conditions (n≈200), we cannot rule out effects smaller than ±X pp; our claim of no evidence applies to effects ≥2pp"。将 Appendix E 的 Table 6 power analysis 的核心数字（MDE per condition group）提到正文。

**N3** [critical] α=0.5 参数无敏感性分析，MAX-SAT 退化结论可能受此影响

- **具体位置**：§3.2（p4），Appendix M（p17）
- **问题**：α=0.5 控制答案断言权重（answer assertion weight）与约束权重的相对影响。论文在 Appendix M 中提供了 K 和 T 的敏感性分析（Figure 5, p17; Table 30, p23），但**完全缺少 α 的消融实验**。94.4% MAX-SAT≡count-only 的核心发现（§7, p8）可能依赖于 α 的特定取值：当 α 较小时，约束权重相对于投票权重更大，MAX-SAT 可能产生与简单计数不同的结果；当 α 较大时，投票主导。
- **为什么影响接收**：如果 94.4% 退化率在 α=0.1 时下降到 70%，论文的核心 narrative——"约束完全不提供额外信息"——就需要修正为"在默认 α 设置下约束不提供额外信息"。
- **建议修改方向**：在一个代表性条件（如 Mistral-7B/FOLIO）上跑 α∈{0.1, 0.3, 0.5, 0.7, 0.9} 的消融，报告 MAX-SAT≡count-only 的比例变化。如果退化率对 α 不敏感（如始终>85%），这反而更强力地支持 SCB 结论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 跨架构 NLI 验证（§6）的 claim 范围超出证据覆盖

- **具体位置**：Abstract（p1），§6（p8），Table 24-26（p22）
- **问题**：摘要声称 "Cross-architecture NLI verification escapes the bottleneck"，但证据仅限于命题逻辑任务（FOLIO, ProofWriter）。在 FOLIO 上增益仅 +2.94pp（p=0.092，未达显著）。论文未在 AIME、LogiQA、StrategyQA 等非逻辑域测试 NLI 验证。NLI 模型天然擅长文本蕴含判断，与命题逻辑任务高度对齐，因此观测到的增益可能是 task-specific 而非 generalizable。
- **建议**：将摘要中的 claim 限定为 "on propositional-logic benchmarks"；在 §6 或 Limitations 中明确讨论 NLI verifier 在数学/常识推理域的预期局限。

**W2** [warning] 语法去重（syntactic equivalence）可能系统性膨胀确认偏差

- **具体位置**：§3.2（p4），Appendix L.1（p16）
- **问题**：语法去重比率 46.6% 意味着超过一半的约束被保留，但语义等价但语法不同的约束仍被分别计数。如果模型在多条 trace 中以不同措辞生成同一约束，这些约束会获得独立权重，系统性膨胀支持多数答案的约束权重。Appendix L.1 中 Z3-based 语义去重 "adds an additional ~10% of constraints"，但论文未报告语义去重后 BR 是否下降。
- **建议**：在 Appendix L.1 增加一组对照：报告 Z3 语义去重后的 BR 值和 MAX-SAT≡count-only 比率。如果差异不大，这会加强 SCB 的结构性论断。

**W3** [warning] Process-level cosine similarity（§5.5）使用 TF-IDF 作为 trace 独立性代理指标，粒度较粗

- **具体位置**：§5.5（p7）
- **问题**：TF-IDF 在推理 trace 上的余弦相似度只能捕捉词汇层面的重叠，无法衡量深层推理结构的相似性。两条 trace 可能使用不同词汇但遵循相同的推理路径（低 TF-IDF 相似度但高逻辑相似度），反之亦然。论文用这个指标支持 "same-model traces share reasoning processes"（p7），但这个结论需要更强的证据。
- **建议**：补充 1-2 个定性案例分析，展示高/低 TF-IDF 相似度的 trace 对在推理结构上的实际差异。或使用 sentence-level embedding（如 SBERT）作为 robustness check。

**W4** [warning] TOST ±2pp 等价边界缺乏独立论证

- **具体位置**：§4.2（p5），Appendix V（p21-22）
- **问题**：±2pp 边界被声称基于 SC 文献中 2-5pp 的典型效应范围（引用 Wang et al., 2023），但这个论证有循环性：试图改进 SC 的论文用 SC 自身的效应量来定义什么算"可忽略"。更根本的问题是，TOST 的 equivalence margin 理想上应在看到数据前预注册。Table 22（p22）显示 ±1pp 和 ±2pp 结果相同，但 ±3pp 时所有条件均为 equivalent——这说明结论对 margin 选择敏感。
- **建议**：在正文中增加对 margin 选择的 sensitivity analysis（已有的 Table 22 数据），明确说明 ±2pp 是 conservative choice，并讨论在更宽 margin 下结论是否变化。

**W5** [warning] 4-seed replication 的充分性

- **具体位置**：§4.1（p5）
- **问题**：4 seeds 的复制在计算成本约束下可以理解，但对于声称"无效果"的论文，变异性的充分表征尤为重要。Table 7（Appendix F, p14）显示 bootstrap CI 跨越零点，但这些 CI 是基于 seed=42 的单次运行还是聚合了 4 seeds？如果是单次运行，seed 间的变异性被低估了。
- **建议**：明确报告 4-seed 间的 accuracy variance，并讨论 seed 选择是否可能影响 sign test 的结果。

---

## 小问题（不影响接收）

1. **Table 1（p6）排版密集**：Type A/B/C 的分类需要反复查看脚注才能理解。建议在表格标题或脚注中简化解释。

2. **Figure 2（p7）信息密度高但可读性一般**：27 种策略的结果全部压缩在一张图中，难以区分个别策略。建议 highlight 最有代表性的 3-5 种策略，其余放入附录。

3. **§3.3 "Symbolic Mirage Hypothesis"（p4）术语引入略突兀**：这个假设名称在后续分析中几乎未再被引用，可以考虑精简为更直接的表述。

4. **引用格式**：部分引用使用 arXiv preprint 而非正式出版版本（如 Wang et al., 2023 的 SC 论文在 ICLR 2023 发表，但 abstract 中引用格式未确认是否为正式版）。建议统一为最终发表版。

5. **Eq (1) Fleiss' κ 公式（p4）**：公式中变量 k 与正文中的 K（trace 数量）容易混淆，建议用不同符号区分。

---

## Questions to Authors

**Q1**：Table 2 中 o3 和 Gemini-2.5-Pro 的 BR 接近 1（1.06, 1.05），且 Table 2 中这两个模型的 cosine similarity (σ_proc) 也较低。这是否暗示 SCB 是弱模型特有的问题？如果只在强模型上测试 SICA，结论是否会改变？

**Q2**：94.4% MAX-SAT≡count-only 的统计来自哪些条件的聚合？是否包括退化条件？如果仅看非退化条件，这个比率是否下降？

**Q3**：在跨架构 NLI 实验（§6）中，DeBERTa 的 standalone accuracy 在 FOLIO 上低于 SC baseline（49.51% vs. 55.88%），但 combo 仍有增益。这是否意味着即使 verifier 本身弱于 generator，架构多样性也能提供价值？这与 Empirical Finding 2 的 capability gap hypothesis 似乎矛盾。

**Q4**：27 种修复策略（Table 13, p18）中，是否有任何策略在个别条件上显示显著正面效果（即使总体不显著）？如果有，这些 "pocket of success" 的特征是什么？

---

## Missing References

1. **Weng et al. (2023)**, "Large Language Models Are Better Reasoners with Self-Verification" — 与本文的自验证方向高度相关，paper 引用列表中似乎有但建议确认其在 Related Work 中的讨论是否充分（特别是 Table 1 的 self-verification 对比）。

2. 建议在 Related Work 中更明确地讨论 **trained verifier** 与 **self-extracted constraint** 的区别——目前 §2 将多种方法混在一起介绍，但本文的核心洞见恰恰是这两类方法的本质差异（CCR 的正负方向不同），值得更早、更清晰地建立这个对比框架。

---

## 总结

本文是一篇执行质量高于平均水平的负面结果论文。SCB 的定量诊断和三重控制实验是真正的贡献。主要问题集中在：(1) 摘要中 BR 数值的选择性报告可能误导读者；(2) 统计效力不足但呈现方式不够审慎；(3) α 参数缺少消融实验。这些问题均可在修改中解决。跨架构 NLI 作为 proof-of-concept 虽然初步，但 CCR 诊断工具的引入为后续研究提供了清晰方向。

评分 3.5 的主要原因：实验方法论够强（Soundness 4），但作为负面结果论文，建设性贡献（§6）偏弱且 claim 范围需收窄，限制了 excitement（3）。如果 N1-N3 的修改能落实，论文可以从 borderline 提升到 solid conference paper。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-22T07:50:33.055840+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 1 (3.5) + Reviewer 2 (3.5)', 'status': 'completed', 'activeForm': '收集两位 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享 — 转发意见并收集 AGREE/REBUT 回应', 'status': 'in_progress', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 1 (3.5) + Reviewer 2 (3.5)', 'status': 'completed', 'activeForm': '收集两位 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享 — 转发意见并收集 AGREE/REBUT 回应', 'status': 'in_progress', 'activeForm': '转发审稿意见进行交叉回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-22T07:50:33.056359+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-22T07:51:07.176133+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性 + 完整性 + 写作质量）的完整审稿意见。请逐条以 `[AGREE]` 或 `[REBUT]` 回应，并说明理由（cite 具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 2 Overall**: 3.5 / 5 (Borderline Conference), Soundness 4/5, Excitement 2.5/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] 跨架构逃逸方案（Section 6）作为独立贡献证据不足\n- 仅测试了一个 NLI 验证器（DeBERTa-large-mnli）在两个数据集上\n- 仅当生成器能力显著弱于验证器时有效\n- 未测试不同规模/类型的验证器，无法判断跨架构中哪个因素起决定性作用\n- 未讨论验证器自身错误的传播\n\n**R2-N2** [critical] \"No Evidence\" 标题声明与统计功效之间存在张力\n- 7/16 条件 MDE ≥ 4.64pp（80% power）\n- TOST ±2pp CI 均包含正值\n- 标题 \"No Evidence\" 修辞力度超出统计结论支撑范围\n- 建议改为 \"Show No Reliable Evidence\" 或 \"Fail to Improve\"\n\n### Should-Fix 问题\n\n**R2-W1** 符号/指标过载——8 页内引入 7 个定量工具（K_eff, κ, BR, C₀, CCR, ProcessSim, ρ_same），建议将 ProcessSim 和 CCR 移至附录\n\n**R2-W2** Discussion/Conclusion 过于压缩（约半页），缺少对 test-time scaling 含义、neuro-symbolic 实践者可操作建议、SCB vs CoT unfaithfulness 关系的讨论\n\n**R2-W3** \"Symbolic Mirage Hypothesis\" 定位不一致——§3.3 提出假设但 §5 直接以结论性措辞使用，未显式回溯验证状态\n\n**R2-W4** Table 1 核心结果表可读性不足——子区域分隔视觉层次不够，显著性标记系统复杂\n\n**R2-W5** CJT 适用性边界条件讨论不足——p > 0.5 条件对 high-accuracy 和 low-accuracy 两端的含义未讨论\n\n### 小问题\n- M1: 未引用 Chain-of-Verification (Dhuliawala et al., 2023)\n- M2: Eq (1) κ 缺少直觉解释\n- M3: Figure 2 grey band \"±1pp noise zone\" 未解释\n- M4: Limitations 称 \"7B-128B\" 但标题/摘要仅提 \"7B-32B\"\n- M5: 多处 `\\looseness=-1`，行间距偏紧\n- M6: \"Symbolic Mirage\" 术语是否准确（vs \"Symbolic Echo\"）\n\n### Missing References\n1. Dhuliawala et al., 2023 — Chain-of-Verification\n2. Lightman et al., 2024 — Process reward models\n\n### 主要优势\n- S1: 实验覆盖与统计严谨（标杆级）\n- S2: SCB 机制发现清晰可复现\n- S3: CJT 理论框架\n- S4: 附录质量极高\n- S5: 叙事框架超越多数负面结果论文\n\n---\n\n请对上述每个 Must-Fix（R2-N1, R2-N2）和 Should-Fix（R2-W1 到 R2-W5）逐条回应 [AGREE] 或 [REBUT]。对小问题可选择性回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性 + 完整性 + 写作质量）的完整审稿意见。请逐条以 `[AGREE]` 或 `[REBUT]` 回应，并说明理由（cite 具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 2 Overall**: 3.5 / 5 (Borderline Conference), Soundness 4/5, Excitement 2.5/5\n\n### Must-Fix 问题\n\n**R2-N1** [critical] 跨架构逃逸方案（Section 6）作为独立贡献证据不足\n- 仅测试了一个 NLI 验证器（DeBERTa-large-mnli）在两个数据集上\n- 仅当生成器能力显著弱于验证器时有效\n- 未测试不同规模/类型的验证器，无法判断跨架构中哪个因素起决定性作用\n- 未讨论验证器自身错误的传播\n\n**R2-N2** [critical] \"No Evidence\" 标题声明与统计功效之间存在张力\n- 7/16 条件 MDE ≥ 4.64pp（80% power）\n- TOST ±2pp CI 均包含正值\n- 标题 \"No Evidence\" 修辞力度超出统计结论支撑范围\n- 建议改为 \"Show No Reliable Evidence\" 或 \"Fail to Improve\"\n\n### Should-Fix 问题\n\n**R2-W1** 符号/指标过载——8 页内引入 7 个定量工具（K_eff, κ, BR, C₀, CCR, ProcessSim, ρ_same），建议将 ProcessSim 和 CCR 移至附录\n\n**R2-W2** Discussion/Conclusion 过于压缩（约半页），缺少对 test-time scaling 含义、neuro-symbolic 实践者可操作建议、SCB vs CoT unfaithfulness 关系的讨论\n\n**R2-W3** \"Symbolic Mirage Hypothesis\" 定位不一致——§3.3 提出假设但 §5 直接以结论性措辞使用，未显式回溯验证状态\n\n**R2-W4** Table 1 核心结果表可读性不足——子区域分隔视觉层次不够，显著性标记系统复杂\n\n**R2-W5** CJT 适用性边界条件讨论不足——p > 0.5 条件对 high-accuracy 和 low-accuracy 两端的含义未讨论\n\n### 小问题\n- M1: 未引用 Chain-of-Verification (Dhuliawala et al., 2023)\n- M2: Eq (1) κ 缺少直觉解释\n- M3: Figure 2 grey band \"±1pp noise zone\" 未解释\n- M4: Limitations 称 \"7B-128B\" 但标题/摘要仅提 \"7B-32B\"\n- M5: 多处 `\\looseness=-1`，行间距偏紧\n- M6: \"Symbolic Mirage\" 术语是否准确（vs \"Symbolic Echo\"）\n\n### Missing References\n1. Dhuliawala et al., 2023 — Chain-of-Verification\n2. Lightman et al., 2024 — Process reward models\n\n### 主要优势\n- S1: 实验覆盖与统计严谨（标杆级）\n- S2: SCB 机制发现清晰可复现\n- S3: CJT 理论框架\n- S4: 附录质量极高\n- S5: 叙事框架超越多数负面结果论文\n\n---\n\n请对上述每个 Must-Fix（R2-N1, R2-N2）和 Should-Fix（R2-W1 到 R2-W5）逐条回应 [AGREE] 或 [REBUT]。对小问题可选择性回应。"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-22T07:51:32.870672+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25694
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-22T07:51:33.023154+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿意见。请逐条以 `[AGREE]` 或 `[REBUT]` 回应，并说明理由（cite 具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 1 Overall**: 3.5 (Borderline Conference), Soundness 4/5, Excitement 3/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] 摘要和正文中的 BR 数值选择性报告，有夸大嫌疑\n- 摘要报告 \"bias ratio 4.97×\" 和 \"83.3%\"，但这是 Mistral-7B/FOLIO 的单一最极端条件\n- Table 2 显示 BR 范围为 1.05（Gemini-2.5-Pro）到 4.97（Mistral-7B）\n- 前沿模型 o3 和 Gemini BR 仅略高于 1\n- 建议摘要报告 median BR 或范围\n\n**R1-N2** [critical] 统计效力不足，但主张和呈现方式不够谨慎\n- 16 个条件中 10 个 underpowered（MDE 远大于 2pp）\n- TOST 仅确认 4 个条件等价\n- Sign test 8/15 positive, p=0.21 是\"不确定\"而非\"否定\"\n- Appendix E power analysis 是关键但被埋在附录中\n- 建议在 §4.2 增加明确 power statement\n\n**R1-N3** [critical] α=0.5 参数无敏感性分析，MAX-SAT 退化结论可能受此影响\n- 94.4% MAX-SAT≡count-only 可能依赖于 α 的特定取值\n- α 较小时约束权重更大，MAX-SAT 可能产生不同结果\n- 建议在代表性条件上跑 α∈{0.1, 0.3, 0.5, 0.7, 0.9} 消融\n\n### Should-Fix 问题\n\n**R1-W1** 跨架构 NLI 验证 claim 范围超出证据——仅在命题逻辑任务上测试，NLI 模型天然对齐\n\n**R1-W2** 语法去重可能膨胀确认偏差——语义等价但语法不同的约束被分别计数，未报告语义去重后 BR 是否下降\n\n**R1-W3** TF-IDF 作为 process independence 代理粒度较粗——只能捕捉词汇层面重叠，无法衡量深层推理结构\n\n**R1-W4** TOST ±2pp margin 缺乏独立论证——用 SC 自身效应量定义\"可忽略\"有循环性，且 ±3pp 时所有条件均 equivalent\n\n**R1-W5** 4-seed replication 充分性——seed 间变异性表征不够，bootstrap CI 是否聚合了 4 seeds 不清楚\n\n### 小问题\n1. Table 1 排版密集\n2. Figure 2 信息密度高但可读性一般\n3. \"Symbolic Mirage Hypothesis\" 术语引入略突兀\n4. 部分引用使用 arXiv 而非正式出版版\n5. Eq (1) 中 κ 与 K 容易混淆\n\n### Questions to Authors\n- Q1: Table 2 中 o3/Gemini BR≈1，SCB 是否是弱模型特有问题？\n- Q2: 94.4% MAX-SAT≡count-only 聚合自哪些条件？是否含退化条件？\n- Q3: FOLIO 上 DeBERTa standalone < SC baseline 但 combo 仍有增益，与 Empirical Finding 2 是否矛盾？\n- Q4: 27 种修复策略中是否有任何在个别条件上显著正面？\n\n### Missing References\n1. Weng et al. (2023) — Self-Verification（建议确认 Related Work 讨论是否充分）\n2. 建议更明确讨论 trained verifier vs self-extracted constraint 的区别\n\n### 主要优势\n- S1: 实验规模令人印象深刻\n- S2: 实验控制设计精巧（oracle + shuffle + cross-model 三重控制）\n- S3: 诊断框架（BR, CCR）具有独立贡献\n- S4: CJT 理论框架提供原则性解释\n- S5: 写作诚实审慎\n\n---\n\n请对上述每个 Must-Fix（R1-N1, R1-N2, R1-N3）和 Should-Fix（R1-W1 到 R1-W5）逐条回应 [AGREE] 或 [REBUT]。对 Questions 和小问题可选择性回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性 + 实验有效性）的完整审稿意见。请逐条以 `[AGREE]` 或 `[REBUT]` 回应，并说明理由（cite 具体 Section/Table/Figure 作为证据）。\n\n---\n\n**Reviewer 1 Overall**: 3.5 (Borderline Conference), Soundness 4/5, Excitement 3/5\n\n### Must-Fix 问题\n\n**R1-N1** [critical] 摘要和正文中的 BR 数值选择性报告，有夸大嫌疑\n- 摘要报告 \"bias ratio 4.97×\" 和 \"83.3%\"，但这是 Mistral-7B/FOLIO 的单一最极端条件\n- Table 2 显示 BR 范围为 1.05（Gemini-2.5-Pro）到 4.97（Mistral-7B）\n- 前沿模型 o3 和 Gemini BR 仅略高于 1\n- 建议摘要报告 median BR 或范围\n\n**R1-N2** [critical] 统计效力不足，但主张和呈现方式不够谨慎\n- 16 个条件中 10 个 underpowered（MDE 远大于 2pp）\n- TOST 仅确认 4 个条件等价\n- Sign test 8/15 positive, p=0.21 是\"不确定\"而非\"否定\"\n- Appendix E power analysis 是关键但被埋在附录中\n- 建议在 §4.2 增加明确 power statement\n\n**R1-N3** [critical] α=0.5 参数无敏感性分析，MAX-SAT 退化结论可能受此影响\n- 94.4% MAX-SAT≡count-only 可能依赖于 α 的特定取值\n- α 较小时约束权重更大，MAX-SAT 可能产生不同结果\n- 建议在代表性条件上跑 α∈{0.1, 0.3, 0.5, 0.7, 0.9} 消融\n\n### Should-Fix 问题\n\n**R1-W1** 跨架构 NLI 验证 claim 范围超出证据——仅在命题逻辑任务上测试，NLI 模型天然对齐\n\n**R1-W2** 语法去重可能膨胀确认偏差——语义等价但语法不同的约束被分别计数，未报告语义去重后 BR 是否下降\n\n**R1-W3** TF-IDF 作为 process independence 代理粒度较粗——只能捕捉词汇层面重叠，无法衡量深层推理结构\n\n**R1-W4** TOST ±2pp margin 缺乏独立论证——用 SC 自身效应量定义\"可忽略\"有循环性，且 ±3pp 时所有条件均 equivalent\n\n**R1-W5** 4-seed replication 充分性——seed 间变异性表征不够，bootstrap CI 是否聚合了 4 seeds 不清楚\n\n### 小问题\n1. Table 1 排版密集\n2. Figure 2 信息密度高但可读性一般\n3. \"Symbolic Mirage Hypothesis\" 术语引入略突兀\n4. 部分引用使用 arXiv 而非正式出版版\n5. Eq (1) 中 κ 与 K 容易混淆\n\n### Questions to Authors\n- Q1: Table 2 中 o3/Gemini BR≈1，SCB 是否是弱模型特有问题？\n- Q2: 94.4% MAX-SAT≡count-only 聚合自哪些条件？是否含退化条件？\n- Q3: FOLIO 上 DeBERTa standalone < SC baseline 但 combo 仍有增益，与 Empirical Finding 2 是否矛盾？\n- Q4: 27 种修复策略中是否有任何在个别条件上显著正面？\n\n### Missing References\n1. Weng et al. (2023) — Self-Verification（建议确认 Related Work 讨论是否充分）\n2. 建议更明确讨论 trained verifier vs self-extracted constraint 的区别\n\n### 主要优势\n- S1: 实验规模令人印象深刻\n- S2: 实验控制设计精巧（oracle + shuffle + cross-model 三重控制）\n- S3: 诊断框架（BR, CCR）具有独立贡献\n- S4: CJT 理论框架提供原则性解释\n- S5: 写作诚实审慎\n\n---\n\n请对上述每个 Must-Fix（R1-N1, R1-N2, R1-N3）和 Should-Fix（R1-W1 到 R1-W5）逐条回应 [AGREE] 或 [REBUT]。对 Questions 和小问题可选择性回应。"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-22T07:51:34.783496+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1760
}
```

</details>

---


### Assistant

_source line 1406 · 2026-05-22T07:51:38.991252+00:00_

交叉分享任务已分配给两位 Reviewer，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 1407 · 2026-05-22T07:51:41.747115+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心评分：**Overall 3.5（Borderline Conference）**，Soundness 4/5，Excitement 3/5。

提出 3 个 Must-Fix（BR 选择性报告、统计效力呈现不足、α 无消融）、5 个 Should-Fix（NLI claim 超范围、语法去重膨胀偏差、TF-IDF 粒度粗、TOST margin 循环论证、4-seed 充分性）、4 个 Questions to Authors。总体判断：方法论执行质量高于平均负面结果论文，SCB 诊断是独立贡献，但建设性发现（§6 跨架构 NLI）偏弱且需收窄 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1408 · 2026-05-22T07:51:48.497719+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 1409 · 2026-05-22T07:54:07.727106+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: 摘要 BR 数值选择性报告**

同意这是一个 framing 问题。摘要报告 "bias ratio 4.97×" 和 "83.3%" 确实来自 Mistral-7B/FOLIO 这一最极端条件。Table 2 (page 7) 清楚显示 BR 的跨模型分布：Mistral-7B BR=4.97, LLaMA-3B BR≈3.88, 但 frontier 模型 Gemini-2.5-Pro BR≈1.05, o3 BR≈2.79。摘要应报告中位数或范围（如 "BR ranges from 1.05 to 4.97, median ≈ 2.6"），而非最极端值。

补充发现：这个问题与 R1-Q1 直接相关——frontier 模型 BR 接近 1 意味着 SCB 严重性与模型能力可能负相关。论文通过 Empirical Finding 2 (page 5) 部分触及了这一点（"combo gain decreases monotonically with the capability gap"），但摘要/标题的 framing 没有反映这一梯度。如果 SCB 主要是弱模型问题，那么论文的 universal 结论需要更强的限定。

**[AGREE] R1-N2: 统计效力不足但主张不够谨慎**

强烈同意。这与我的 N2 高度重叠。R1 的分析甚至比我更细致——指出 sign test 8/15 positive (p=0.21) 的结果本质上是 "inconclusive" 而非 "negative"，这一点我在初审中未充分强调。

具体证据补充：
- Table 6 (Appendix E, page 14): 10 个条件的 observed power < 80%，其中 Qwen2.5-14B 的两个条件 power < 20%
- TOST (Table 7, Appendix F): 仅 4 个条件的 CI 完全落在 ±2pp margin 内；其余条件的 CI 上界达 +1.62pp (Qwen-14B FOLIO)，无法排除小正效果
- Section 4.2 (page 5) 的 aggregate sign test (8/15, p=0.21) 被论文解释为 "confirms seed-level noise"，但 p=0.21 在统计学上只是 "failure to reject the null"，不能作为 null 成立的证据

R1 建议在 §4.2 增加明确 power statement，我认为这是最低限度的修改要求。

**[AGREE with nuance] R1-N3: α=0.5 参数无敏感性分析**

同意缺少 α 敏感性分析是一个方法论缺口，但我认为其影响范围可能比 R1 预估的更有限。

理由：94.4% MAX-SAT≡count-only 的根本原因是 SCB（约束方向与多数投票一致，BR > 1），而非 α 的特定取值。当 BR > 1 时，约束加权后仍然支持多数答案，调整 α 改变的是约束与投票的相对权重，但如果两者方向一致，权重比例不影响最终选择。只有当 α 极小（如 0.1）且存在少量高权重的 disagreeing constraints 时，MAX-SAT 才可能产生不同结果——但这恰好是 SCB 不严重（BR ≈ 1）的条件，而在这些条件下（如 frontier 模型），SICA 本身就更接近 SC。

建议的折中方案：在 2-3 个代表性条件上（如 Mistral-7B FOLIO 高 BR + Qwen2.5-14B 低 BR）跑 α∈{0.1, 0.3, 0.7} 消融即可，不需要全面网格搜索。如果结果验证了上述推理（高 BR 条件下 α 不影响结论），可以增强论证；如果 α=0.1 下 MAX-SAT 产生了显著不同的结果，则需要修改核心论述。

---

### Should-Fix 问题

**[AGREE] R1-W1: 跨架构 NLI 验证仅在命题逻辑任务上测试**

同意。这与我的 N1 互补——我的 N1 关注验证器多样性不足，R1-W1 关注任务域偏差。FOLIO 和 ProofWriter 都是命题/一阶逻辑任务，NLI 模型（DeBERTa-large-mnli, trained on MNLI）天然擅长 textual entailment，这与形式逻辑推理高度对齐。在 StrategyQA（常识推理）或 LogiQA（自然语言逻辑）上，NLI 验证器的优势可能大幅下降。论文 Section 6 (page 8) 未讨论这一 domain alignment confound。

**[AGREE] R1-W2: 语法去重可能膨胀确认偏差**

同意这是一个未被充分讨论的方法论问题。Section 3.2 (page 4) 描述了 "syntactic equivalence" 去重（全局去重率 46.0%），但未讨论语义等价。例如，"if A then B"、"A implies B"、"not A or B" 在逻辑上等价但语法不同，会被分别计数。这意味着 Table 2 中的 BR 值可能因语法冗余被膨胀。

不过我也注意到，约束是通过 Z3 求解的（Section 3.2, page 4, Appendix C Algorithm 1），Z3 内部会处理逻辑等价性。所以 MAX-SAT 的求解结果可能不受语法冗余影响，但 BR 作为诊断指标的值确实可能被膨胀。建议作者报告语义去重后的 BR 值——如果仍然 > 1，则结论不变；如果显著下降（如 BR ≈ 1），则需要重新评估 SCB 的严重程度。

**[AGREE with reservation] R1-W3: TF-IDF 作为 process independence 代理粒度较粗**

同意 TF-IDF cosine similarity (ProcessSim, Eq. 6, Section 5.3, page 7) 只能捕捉词汇层面的重叠，无法衡量深层推理结构的相似性。两条 trace 可能用不同措辞表达相同的推理步骤（低 ProcessSim 但实际不独立），或用相似措辞达到不同结论（高 ProcessSim 但实际独立）。

但我的 reservation 是：ProcessSim 不是论文核心论证的承重墙。论文的核心证据链是 BR > 1 (Table 2) + shuffle control (Section 5.2) + oracle control (Section 4.3)。ProcessSim 只是 Section 5.3 中的辅助证据，用于说明 process-level 也缺乏多样性。即使完全移除 ProcessSim 分析，论文的核心结论仍然成立。建议作者在正文中明确 ProcessSim 的定位（supplementary evidence），降低读者对其精确性的预期。

**[AGREE] R1-W4: TOST ±2pp margin 缺乏独立论证**

同意这是一个方法论循环性问题。Appendix F (page 14) 使用 ±2pp 作为等价边界，理由似乎来自 SC 自身的 seed-to-seed 变异性。用被测方法自身的噪声水平定义 "negligible effect" 确实有循环性——如果 SC 的 seed 变异恰好是 2pp，那么任何 ≤2pp 的效果都会被判为等价，但这可能掩盖实际有意义的小改进。

R1 指出 "±3pp 时所有条件均 equivalent" 更进一步强化了这一担忧。建议作者引用领域内公认的最小实际意义差异（如 reasoning benchmarks 上 1-2pp 的改进通常被认为 marginal），或用一个外部基准来论证 margin 的选择。

**[PARTIALLY AGREE] R1-W5: 4-seed replication 充分性**

部分同意。4 seeds 在 ML 实验中是常见做法，但对负面结果论文（需要排除效果而非证明效果），更多 seeds 确实能增强说服力。

不过我认为这个问题的严重性取决于 seed 间变异性的实际大小。论文 Table 1 (page 6) 的 "4-seed confirmatory" 条件标注了 a，但 seed 间变异的量化（如 inter-seed standard deviation）确实不够透明。如果 seed 间变异很小（< 1pp），4 seeds 足够；如果很大（> 3pp），则 4 seeds 不够。建议作者在 Table 1 或附录中报告 seed 间标准差。

---

### 对 Questions 的回应

**Q1 (o3/Gemini BR≈1，SCB 是否弱模型特有):**
这是 R1 提出的最重要的问题。Table 2 (page 7) 清楚显示 BR 与模型能力负相关：Mistral-7B (4.97) > LLaMA-3B (3.88) > R1-Distill-8B (2.45) > gpt-4.1 (1.47) > Gemini (1.05)。如果 SCB 是弱模型特有现象，论文的 "universal" framing 就有问题。我在初审中也通过 N2 间接触及了这一点（frontier 模型上效果未被充分测试），但 R1 更直接地指出了这个核心问题。作者需要在 Discussion 中明确讨论 SCB 严重性与模型能力的关系。

**Q3 (DeBERTa standalone < SC baseline 但 combo 有增益):**
这是一个尖锐的问题。Table 3 (page 8) 显示 DeBERTa standalone 在某些条件下低于 SC baseline，但 combo (SC + DeBERTa NLI) 仍有增益。Empirical Finding 2 (page 5) 声称 "gains exist only when the verifier exceeds the generator"。如果 DeBERTa standalone accuracy < SC accuracy，那么 verifier 并没有 "exceed" generator，但 combo 仍然有效——这表明关键因素不是 verifier 的绝对准确率，而是 verifier 提供了独立信号（即使不那么准确）。这与 CJT 框架一致（独立性比准确率更重要），但与 Finding 2 的措辞存在张力。作者需要澄清 "exceed" 的具体含义——是指 standalone accuracy 还是 independence-adjusted effective accuracy？

**Q4 (27 种修复策略是否有任何在个别条件上正面):**
从 Figure 2 (page 7) 和 Table 13 (Appendix K, page 18) 来看，27 种策略在 aggregate 层面全部为 neutral-to-negative。但 Table 13 显示个别策略在特定条件上有正效果（如 "Debate" Δ = +0.01 on certain conditions），不过统计上不显著。如果有任何策略在特定条件上通过了显著性检验，作者应该报告。

---

### 对小问题的回应

1. **Table 1 排版密集**: [AGREE] 与我的 W4 一致。
2. **Figure 2 可读性**: [AGREE] 与我的 M3 部分重叠。
3. **"Symbolic Mirage Hypothesis" 术语突兀**: [AGREE] 与我的 W3 一致——我进一步指出了 hypothesis vs. confirmed conclusion 的定位不清问题。
4. **部分引用用 arXiv 而非正式出版版**: [AGREE] 这是小问题但值得检查，尤其对已有正式出版版本的论文。
5. **Eq (1) κ 与 K 混淆**: [AGREE] 希腊字母 κ (kappa) 和拉丁字母 K (大写 K) 在排版上确实接近，且两者在同一公式中出现（K 是样本数，κ 是 Fleiss' kappa）。建议用不同符号或在首次出现时加粗区分。

---

### 与 R1 评分的对比

| 维度 | R1 | R2 (我) | 差异说明 |
|------|-----|---------|---------|
| Soundness | 4/5 | 4/5 | 一致 |
| Excitement | 3/5 | 2.5/5 | R1 比我更积极；我认为 SCB 发现被先验工作更多预示 |
| Overall | 3.5 | 3.5 | 一致 |

**主要分歧点**: Excitement。R1 给 3/5，我给 2.5/5。差异来源于对新颖性增量的判断——R1 似乎更看重系统性实验的价值（"实验规模令人印象深刻"），而我更关注发现本身是否超越了先验预期。Huang et al. (2024) 已经建立了 "LLMs cannot self-correct without external feedback" 的结论，本文将其扩展到 symbolic constraint extraction 领域并提供了 mechanistic explanation (SCB)，但核心 insight（自提取 = 非独立 = 无增量信息）在概念层面不算意外。

**共识点**: 两位 reviewer 在 Must-Fix 问题上高度一致：统计功效的 framing (R1-N2 / R2-N2)、跨架构证据不足 (R1-W1 / R2-N1)。这强化了这两个问题必须在 revision 中解决的优先级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1410 · 2026-05-22T07:54:21.787218+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 93

## Round 93

18 recorded events


### User

_source line 1411 · 2026-05-22T07:54:22.989394+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：与 R1 在绝大多数问题上达成共识（特别是统计功效 framing 和跨架构证据不足），唯一分歧在 Excitement 评分（我给 2.5 vs R1 给 3），原因是我认为 SCB 发现被 Huang et al. (2024) 等先验工作更多预示。两位 reviewer 的 Overall 评分一致为 3.5 (Borderline Conference)。

---

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 跨架构逃逸方案（§6）作为独立贡献证据不足**

R2 的核心事实判断有误。

(1) **"仅测试了一个 NLI 验证器"——事实错误。** §6 正文明确写道 "all three NLI architectures produce significant gains at w = 3"（p8）。Table 25（p22）报告了 **三个** NLI 验证器（DeBERTa-MNLI, RoBERTa-MNLI, BART-MNLI）× 三种权重设置在 ProofWriter 上的完整矩阵。Table 26（p22）进一步对 3 verifiers × 5 weights = 15 组合做了 BH 校正，10/15 条件在 α=0.05 后仍显著。这不是"一个验证器"，而是三个不同架构（encoder-only DeBERTa、encoder-only RoBERTa、encoder-decoder BART）的系统测试。

(2) **"仅当生成器能力显著弱于验证器时有效"——部分正确但需要精确化。** Table 3（p8）测试了 4 个生成器（Mistral-7B, LLaMA-3.1-4B, Qwen2.5-7B, Qwen2.5-14B），跨越 4B-14B 参数范围。Figure 7（p23）显示 combo gain 与 capability gap 单调递减，这是一个连续梯度关系而非二元阈值。更关键的是，Table 3 中 Qwen2.5-14B 在 ProofWriter 上仅 +1.17pp（边缘），说明论文已展示了 capability gap 缩小时增益递减的完整图景。

(3) **"未讨论验证器自身错误的传播"——同意，这是合理关切。** 论文确实未显式分析 verifier false positive/negative 的分布及其对 combo 结果的影响。但 Table 4（p14）的 CCR 分析间接涉及了这一点：CCR > 0 表示 verifier preferentially corrects generator errors，而非随机引入自身错误。仍建议作者增加 verifier error breakdown 的简要分析。

**我的判断**：R2-N1 的前两个子论点建立在对论文内容的不完整阅读上。§6 作为 proof-of-concept 的证据虽然有限（仅覆盖命题逻辑任务——这是我在 R1-W1 中提出的问题），但 3 architectures × 4 generators × 5 weight settings 的评估规模已超出典型 proof-of-concept 的标准。Verifier error propagation 是唯一成立的子论点。

---

**[AGREE] R2-N2: "No Evidence" 标题与统计功效的张力**

这与我的 R1-N2 一致。核心问题相同：10/16 条件 underpowered，sign test 不确定（8/15 positive, p=0.21），标题的修辞力度与统计结论之间确实存在 gap。

但我不同意 R2 的具体修改建议：

- **"Show No Reliable Evidence"**——"reliable" 是冗余的，evidence 本身就应该是 reliable 的，否则不算 evidence。
- **"Fail to Improve"**——暗示方法的目标是改进但未能达成，而论文的贡献是诊断性的（为什么不改进），这个标题丢失了因果维度。

**我的建议**：标题可以保持不变（"Show No Evidence" 在统计学中是标准用法，等同于 "we found no statistically significant evidence"），但正文 §4.2 需要增加 power statement（如我在 R1-N2 中建议的），让读者能准确理解 "no evidence" 的统计含义和适用范围。

---

### Should-Fix 问题

**[AGREE] R2-W1: 符号/指标过载**

8 页正文引入 K_eff、κ、BR、C₀、CCR、ProcessSim、ρ_same 共 7 个定量工具确实增加了认知负担。但我与 R2 的优先级判断不同：

- **必须留在正文的**：BR（核心发现的量化支撑）和 C₀（退化条件的判据）——这两个是理解 SCB 和实验分区的基础。
- **可移至附录的**：CCR 虽然是独立贡献，但其主要作用是在 §6 跨架构分析中，可以在 §6 引入时简述定义而非在 §5.4 单独设一小节。ProcessSim（§5.5）的 TF-IDF 方法本身粒度较粗（见我的 R1-W3），更适合放在附录作为辅助证据。
- K_eff 和 κ 是 CJT 框架的标准工具，简化定义即可。

---

**[AGREE] R2-W2: Discussion/Conclusion 过于压缩**

§7（p8）确实不到半页。作为一篇提出新现象（SCB）的论文，Discussion 应至少涵盖：

1. **SCB 与 CoT unfaithfulness 的关系**——Turpin et al. (2023) 和 Lanham et al. (2023) 的 CoT unfaithfulness 发现与 SCB 有何异同？约束提取是否只是 unfaithful CoT 的下游投射？这个连接对读者理解 SCB 的本质很重要。
2. **对 neuro-symbolic 实践者的可操作建议**——论文证明自提取约束无效，但未告诉读者"那该怎么做"（除了跨架构 NLI 这一初步方向）。
3. **Test-time scaling 含义**——SICA 增加了 4.5× 的推理成本（p8 Limitations 提到），但无增益。这对 test-time compute scaling 的研究议程意味着什么？

---

**[AGREE] R2-W3: "Symbolic Mirage Hypothesis" 定位不一致**

§3.3（p4）将其定义为假设（"We hypothesize that..."），但 §5 的标题和措辞直接使用结论性语气（如 "Symbolic confirmation bias across nine models"），中间缺少一个显式的"假设验证"过渡。建议在 §5 开头增加一句话，如 "We now test the three testable predictions of the symbolic mirage hypothesis (§3.3)"——实际上论文在 §5 开头有类似表述（p6: "We test the three predictions of the symbolic mirage hypothesis"），但后续小节标题（§5.1-5.5）没有回溯到假设的具体预测编号，导致验证逻辑链不够显式。

R2 的观察是准确的，但问题严重程度较低——论文的逻辑链客观上是完整的，只是呈现上可以更清晰。

---

**[AGREE] R2-W4: Table 1 可读性不足**

与我的小问题 #1 一致。Table 1（p6）承载了全文最核心的结果，但 Type A/B/C 分区、显著性标记系统（bold/†/*/***）、以及密集的数字排列确实增加了读者的认知成本。建议增加视觉分隔（如水平线或颜色区分）和一个简化的 summary panel（如 forest plot）。

---

**[REBUT] R2-W5: CJT 适用性边界条件讨论不足**

R2 认为论文未讨论 CJT 的 p > 0.5 条件在 high-accuracy 和 low-accuracy 两端的含义。但论文实际上涉及了这两端：

- **High-accuracy 端**：§4.2（p5）和 Table 1 的 Type C 区域（degenerate regime, SC > 60%）明确分析了高准确率条件下 SICA 退化的原因——当 SC 已经很高时，约束几乎全部支持正确答案，MAX-SAT 无额外信息可加。
- **Low-accuracy 端**：§4.2（p5）讨论了 intermediate-SC region (50-55%) 是唯一可能出现正面趋势的区域，但效应不显著。Appendix Y（p24）进一步分析了 sub-population 中 mid-constraint tertile 的结果。
- **CJT 的 p < 0.5 情况**（多数投票反而有害）：Eq (1) 的 K_eff 和 κ 分析（p4）通过 Fleiss' κ 测量 trace 间相关性，说明有效独立 voter 数远小于 K，但论文确实没有显式讨论当 per-trace accuracy < 0.5 时 SC 本身是否有害——不过这已超出本文范围（本文研究的是约束能否改进 SC，而非 SC 何时有害）。

**我的判断**：论文对 CJT 的使用是 framing device 而非完整的理论推导，在这个定位下，边界条件的讨论已足够。R2 的建议更适合作为 Discussion 中的一个扩展点（与 R2-W2 合并），而非独立的 should-fix。

---

### 小问题选择性回应

**[AGREE] M1: 缺少 Chain-of-Verification (Dhuliawala et al., 2023) 引用。** 与本文的验证方向直接相关，应在 §2 Related Work 中讨论。

**[REBUT] M2: Eq (1) κ 缺少直觉解释。** 这是一个公允的建议，但 Fleiss' κ 是标准统计量，在 NLP 领域读者中不需要从头解释。增加一句 "κ measures the excess of inter-rater agreement beyond chance" 即可。

**[AGREE] M4: "7B-128B" vs "7B-32B" 不一致。** 这是事实错误，需要统一。正文/摘要提到 "7B-32B"（6 个开源模型中最大的是 Qwen2.5-14B，thinking 模型 QwQ-32B 也被包括），而 Limitations 中 "7B-128B" 的 "128B" 来源不明——可能是将前沿模型（gpt-4o 等）的推测参数量计入，但在 blind review 中不应出现未经证实的参数估计。

**[AGREE] M6: "Symbolic Mirage" 术语是否准确。** R2 建议 "Symbolic Echo" 更准确地捕捉了约束回声模型自身偏差的本质。"Mirage"（海市蜃楼）强调"看起来有用但其实无用"，"Echo" 强调"约束只是模型自身信号的反射"。两者各有道理，但 "Echo" 与论文的因果发现（约束反映而非独立验证）更匹配。不过这是 terminology preference，不影响接收。

---

### 对 R2 Missing References 的回应

**[REBUT] Lightman et al., 2024 — Process reward models。** 论文已引用。参考文献列表（p11）包含 "Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. 2024. Let's verify step by step. In ICLR." R2 可能未注意到。

**[AGREE] Dhuliawala et al., 2023 — Chain-of-Verification。** 确认论文引用列表中未见此篇。

---

### 综合评价

R2 的审稿整体质量较高，尤其是 W1（指标过载）、W2（Discussion 压缩）和 W3（假设定位）的观察点有价值。但 **R2-N1 存在明显的事实错误**（误称"仅一个验证器"），这削弱了其 must-fix 判断的可信度。R2 的 Excitement 评分 2.5/5 偏低——ARR guidelines 明确指出负面结果论文不应因结论方向而被降分，而本文的 SCB 诊断和三重控制实验在方法论贡献上超过了多数正面结果论文。

**我对 R2 评分的看法**：Soundness 4/5 我完全同意。Excitement 2.5 我认为应为 3（Interesting），因为 SCB 现象的定量刻画对 neuro-symbolic 和 test-time scaling 社区有直接参考价值。Overall 3.5 与我一致。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-22T07:55:03.561809+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化 + Round 1 审稿', 'status': 'completed', 'activeForm': '完成初始化和 Round 1 审稿'}, {'content': 'Step 2: 交叉分享 — R1 和 R2 已完成互评', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化 + Round 1 审稿', 'status': 'completed', 'activeForm': '完成初始化和 Round 1 审稿'}, {'content': 'Step 2: 交叉分享 — R1 和 R2 已完成互评', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '分析共识与分歧'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-22T07:55:03.613048+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-22T07:55:21.548142+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-2: 初始化 + Round 1 + 交叉分享', 'status': 'completed', 'activeForm': '完成全部审稿轮次'}, {'content': 'Step 3: 收敛判断 — 关键问题已达成共识', 'status': 'completed', 'activeForm': '完成收敛判断'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '合成最终审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-2: 初始化 + Round 1 + 交叉分享', 'status': 'completed', 'activeForm': '完成全部审稿轮次'}, {'content': 'Step 3: 收敛判断 — 关键问题已达成共识', 'status': 'completed', 'activeForm': '完成收敛判断'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '合成最终审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-22T07:55:21.560207+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 12
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-22T07:55:26.525570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-22T07:55:26.678238+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 18594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1418 · 2026-05-22T07:55:26.678735+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1419 · 2026-05-22T07:55:26.980823+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T07:41:10.038846+00:00\", \"completed_at\": \"2026-05-22T07:45:45.640807+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"主文 Section 7 (Discussion and Conclusion) 有约 3-4 行文字溢出到 page 9 顶部，Limitations 从 page 9 中段才开始。EMNLP 2026 主文限 8 页（Limitations 豁免），当前主文约 8.05-8.1 页。ACL/ARR 对页数限制零容忍，建议压缩 Discussion 或前文以确保 Section 7 在 page 8 内结束\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"从 Related Work 到 Experiment Setup 连续约 2.5 页视觉密度较低（无 figure/table），虽然 page 4 有公式穿插，但审稿人快速翻阅时可能感到单调。建议考虑将 Table 1 或一个精简的 setup overview 提前\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 尺寸偏小（约占右栏 1/3 高度），内部文字标签在打印时可能偏小。如有空间可适当放大\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 axis label 字号约为正文的 65-70%，接近可读下限。建议稍增大坐标轴字号\"}, {\"severity\": \"info\", \"dimension\": \"pages 14,16,23\", \"message\": \"附录单页表格密度极高（page 14 有 4 个表，page 16 有 3 个表 + 4 个 section header），虽不影响主文评审，但审稿人查阅附录时可能体验较差\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"附录 14 页含 29 个表 + 5 个图 + 2 个算法，材料充实但体量大。建议在附录开头加一个 \\\"Appendix Overview\\\" 导航段帮助审稿人定位\"}, {\"severity\": \"info\", \"dimension\": \"page 12-13\", \"message\": \"Prompt template 以纯文本代码块呈现，格式清晰。Algorithm 1-2 使用标准算法环境，排版正确\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1420 · 2026-05-22T07:55:26.982058+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-22T07:55:27.082927+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---
