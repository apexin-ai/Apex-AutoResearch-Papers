# Director coordination — Part 3 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 63

### Tool result

_source line 597 · 2026-05-23T01:25:14.398292+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse th
…[truncated 6777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-23T01:25:18.774254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-23T01:25:19.326902+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary coefficient does not reverse in any tested configuration---an empirical regularity driven by magnitude dominance rather than algebraic structure---while 61\% of exposure configurations reverse a secondary coefficient. Our analytical results assume linear SEMs; Appendix~\ref{sec:logistic_dgp} demonstrates that topology rankings and sign-flip patterns are preserved under logistic DGP ($|\Delta\,\text{SF}_\tau| < 0.02$), though FWL invariance is specific to linear models. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinea
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-23T01:25:19.327344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-23T01:25:19.679099+00:00_

File content (34321 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-23T01:25:19.679517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-23T01:25:19.730275+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-20
3	
4	@article{cinelli2020making,
5	  author    = {Cinelli, Carlos and Hazlett, Chad},
6	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
7	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
8	  year      = {2020},
9	  volume    = {82},
10	  number    = {1},
11	  pages     = {39--67},
12	  doi       = {10.1111/rssb.12348},
13	}
14	
15	@article{gilardi2023chatgpt,
16	  author    = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma\"{e}l},
17	  title     = {{ChatGPT} Outperforms Crowd Workers for Text-Annotation Tasks},
18	  journal   = {Proceedings of the National Academy of Sciences},
19	  year      = {2023},
20	  volume    = {120},
21	  number    = {30},
22	  pages     = {e2305016120},
23	  doi       = {10.1073/pnas.2305016120},
24	}
25	
26	@article{ziems2024can,
27	  author    = {Ziems, Caleb and Held, William and Shaikh, Omar and Chen, Jiaao and Zhang, Zhehao and Yang, Diyi},
28	  title     = {Can Large Language Models Transform Computational Social Science?},
29	  journal   = {Computational Linguistics},
30	  year      = {2024},
31	  volume    = {50},
32	  number    = {1},
33	  pages     = {237--291},
34	  doi       = {10.1162/coli\_a\_00502},
35	}
36	
37	@incollection{bound2001measurement,
38	  author    = {Bound, John and Brown, Charles and Mathiowetz, Nancy},
39	  title     = {Measurement Error in Survey Data},
40	  booktitle = {Handbook of Econometrics},
41	  editor    = {Heckman, James J. and Leamer, Edward E.},
42	  year      = {2001},
43	  volume    = {5},
44	  chapter   = {59},
45	  pages     = {3705--3843},
46	  publisher = {Elsevier},
47	}
48	
49	@article{richardson1993bayesian,
50	  author    = {Richardson, Sylvia and Gilks, Walter R.},
51	  title     = {A {Bayesian} Approach to Measurement Error Problems in Epidemiology Using Conditional Independence Models},
52	  journal   = {Amer
…[truncated 16857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-23T01:25:24.749550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-23T01:25:24.800714+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 8490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-23T01:25:34.690664+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'artifacts/review_round_8/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf 2>/dev/null || echo \"pdfinfo not available, trying alternative\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'artifacts/review_round_8/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf 2>/dev/null || echo \"pdfinfo not available, trying alternative\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-23T01:25:34.793459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-23T01:25:34.894683+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 00:29:52 2026 UTC
ModDate:         Sat May 23 00:29:52 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           26
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       897145 bytes
Optimized:       no
PDF version:     1.7
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 204
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-23T01:25:34.895787+00:00_

issues:
  # === Carried from Round 1-5 (resolved issues kept as history) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 6
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Proposition 2（数值验证）和 Conjecture 1 覆盖。R6-M1 的拆分已完成。"
    resolution_round: 7
    mentions:
      - round: 7
        reviewers: [R1]
        note: "R7-R1 确认 Theorem 1 (K=2) 证明完整正确。新 concern 转移到 Proposition 2 的命名问题（见 R7-SF1）。"

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写：83.4% 作为 K≥3 结构转变呈现，与 2.1% 并列。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。
…[truncated 19070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-23T01:26:11.280777+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-23T01:26:11.331451+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-23T01:26:15.304011+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4023
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-23T01:26:15.304488+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3973
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-23T01:26:46.038290+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（引用不限，附录不计入但审稿人不必阅读）\n- **模板**: ACL 2026（LaTeX，\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n**理论正确性与方法严谨性**，具体包括：\n\n1. **证明正确性**：\n   - Proposition 1 (sign preservation) 的三个子命题 (a)(b)(c) 是否正确\n   - Theorem 1 (envelope monotonicity, K=2) 的证明是否完整\n   - Lemma (bias decomposition) 的推导\n   - Appendix 中的完整证明链\n\n2. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM 标注场景中是否合理\n   - Linear SEM 假设的局限性是否充分讨论\n   - Proportional effects (f=λg) 条件的强度——在 NLP 场景中何时成立/何时违反\n   - Dirichlet(1,1,1) 先验的合理性\n\n3. **关键声称的验证层次**：\n   - 论文建立了 Proved/Numerically Verified/Conjectured 三级层次，层次划分是否准确\n   - \"Primary coefficient never reverses\" 是否被恰当定位（经验规律 vs 理论保证）\n   - Conjecture 1 (ε-approximate monotonicity) 的数值验证是否充分\n\n4. **实验方法论**：\n   - MC 验证的设计是否合理（N=10,000, 100,000 matrices）\n   - 实证验证（23 LLM configurations × 7 topologies）的设计\n   - MAPE 1.6% 的报告是否恰当\n   - FWL invariance 在非线性模型下的 breakdown 分析\n\n5. **ASV 框架**：\n   - 三种 ASV 类型的定义是否严谨\n   - C(δ) 参数化的合理性\n   - Bootstrap CI 的解释是否恰当（特别是 IV 的宽 CI）\n\n请按以下格式输出审稿报告：\n\n### Summary（2-3 句）\n### Strengths（S1, S2, ...）\n### Weaknesses（W1, W2, ...，标注 CRITICAL/MAJOR/MINOR）\n### Questions（Q1, Q2, ...）\n### Missing References\n### Detailed Comments（按 Section 逐条）\n### Overall Assessment（评分 + 置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（引用不限，附录不计入但审稿人不必阅读）\n- **模板**: ACL 2026（LaTeX，\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n**理论正确性与方法严谨性**，具体包括：\n\n1. **证明正确性**：\n   - Proposition 1 (sign preservation) 的三个子命题 (a)(b)(c) 是否正确\n   - Theorem 1 (envelope monotonicity, K=2) 的证明是否完整\n   - Lemma (bias decomposition) 的推导\n   - Appendix 中的完整证明链\n\n2. **假设合理性**：\n   - Non-differential misclassification 假设在 LLM 标注场景中是否合理\n   - Linear SEM 假设的局限性是否充分讨论\n   - Proportional effects (f=λg) 条件的强度——在 NLP 场景中何时成立/何时违反\n   - Dirichlet(1,1,1) 先验的合理性\n\n3. **关键声称的验证层次**：\n   - 论文建立了 Proved/Numerically Verified/Conjectured 三级层次，层次划分是否准确\n   - \"Primary coefficient never reverses\" 是否被恰当定位（经验规律 vs 理论保证）\n   - Conjecture 1 (ε-approximate monotonicity) 的数值验证是否充分\n\n4. **实验方法论**：\n   - MC 验证的设计是否合理（N=10,000, 100,000 matrices）\n   - 实证验证（23 LLM configurations × 7 topologies）的设计\n   - MAPE 1.6% 的报告是否恰当\n   - FWL invariance 在非线性模型下的 breakdown 分析\n\n5. **ASV 框架**：\n   - 三种 ASV 类型的定义是否严谨\n   - C(δ) 参数化的合理性\n   - Bootstrap CI 的解释是否恰当（特别是 IV 的宽 CI）\n\n请按以下格式输出审稿报告：\n\n### Summary（2-3 句）\n### Strengths（S1, S2, ...）\n### Weaknesses（W1, W2, ...，标注 CRITICAL/MAJOR/MINOR）\n### Questions（Q1, Q2, ...）\n### Missing References\n### Detailed Comments（按 Section 逐条）\n### Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-23T01:27:05.725992+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19687
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-23T01:27:05.877082+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（引用不限，附录不计入但审稿人不必阅读）\n- **模板**: ACL 2026（LaTeX，\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性评估、相关工作完整性、格式合规与写作质量**，具体包括：\n\n1. **新颖性与贡献定位**：\n   - 三个贡献（bias taxonomy, ASV, correction guidance）的新颖性评估\n   - ASV 与 E-value/partial-R² 的方法论差异是否充分——是否仅为重新参数化\n   - \"首次跨 7 种拓扑系统比较\"的声称是否成立\n   - FWL invariance 作为 negative result 的价值\n   - 与 Teblunthuis (2024)、Lee & Wood-Doughty (2024)、Audinet et al. (2025) 的差异化\n\n2. **相关工作覆盖**：\n   - 流行病学测量误差文献（Carroll 2006, Gustafson 2004, Buonaccorsi 2010）\n   - NLP text-as-data / 因果推断文献（Feder et al. 2022, Keith et al. 2020）\n   - LLM 标注质量文献（Baumann 2025, Kim & Garg 2025, Gligorić et al. 2025）\n   - PPI / correction 方法（Angelopoulos 2023, Zrnić & Candès 2024, Cadei et al. 2025, Demirel et al. 2024）\n   - 是否有重要遗漏\n\n3. **格式合规**：\n   - 正文是否 ≤ 8 页\n   - ACL 模板使用是否正确\n   - Double-blind 匿名是否完整（无自引暴露、无致谢暴露身份）\n   - 引用格式（natbib 风格、一致性）\n   - Preprint 引用是否标注状态\n\n4. **写作质量**：\n   - Abstract 是否准确反映论文内容，声称是否过度\n   - Introduction 叙事是否清晰（问题动机 → gap → contribution）\n   - 数字密度是否过高（特别是 Abstract/Introduction）\n   - 符号使用是否一致\n   - Figure/Table 的信息传达效率\n   - Limitations 节是否充分\n\n5. **EMNLP 2026 特定要求**：\n   - 检查是否有 Responsible NLP Checklist 相关内容（注意：此 checklist 在 OpenReview 表单中填写，不在论文中）\n   - 是否有 Ethics Statement（可选）\n   - Limitations 节（mandatory，不计入页数限制）\n\n请按以下格式输出审稿报告：\n\n### Summary（2-3 句）\n### Strengths（S1, S2, ...）\n### Weaknesses（W1, W2, ...，标注 CRITICAL/MAJOR/MINOR）\n### Questions（Q1, Q2, ...）\n### Missing References\n### Detailed Comments（按 Section 逐条）\n### Overall Assessment（评分 + 置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（引用不限，附录不计入但审稿人不必阅读）\n- **模板**: ACL 2026（LaTeX，\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性评估、相关工作完整性、格式合规与写作质量**，具体包括：\n\n1. **新颖性与贡献定位**：\n   - 三个贡献（bias taxonomy, ASV, correction guidance）的新颖性评估\n   - ASV 与 E-value/partial-R² 的方法论差异是否充分——是否仅为重新参数化\n   - \"首次跨 7 种拓扑系统比较\"的声称是否成立\n   - FWL invariance 作为 negative result 的价值\n   - 与 Teblunthuis (2024)、Lee & Wood-Doughty (2024)、Audinet et al. (2025) 的差异化\n\n2. **相关工作覆盖**：\n   - 流行病学测量误差文献（Carroll 2006, Gustafson 2004, Buonaccorsi 2010）\n   - NLP text-as-data / 因果推断文献（Feder et al. 2022, Keith et al. 2020）\n   - LLM 标注质量文献（Baumann 2025, Kim & Garg 2025, Gligorić et al. 2025）\n   - PPI / correction 方法（Angelopoulos 2023, Zrnić & Candès 2024, Cadei et al. 2025, Demirel et al. 2024）\n   - 是否有重要遗漏\n\n3. **格式合规**：\n   - 正文是否 ≤ 8 页\n   - ACL 模板使用是否正确\n   - Double-blind 匿名是否完整（无自引暴露、无致谢暴露身份）\n   - 引用格式（natbib 风格、一致性）\n   - Preprint 引用是否标注状态\n\n4. **写作质量**：\n   - Abstract 是否准确反映论文内容，声称是否过度\n   - Introduction 叙事是否清晰（问题动机 → gap → contribution）\n   - 数字密度是否过高（特别是 Abstract/Introduction）\n   - 符号使用是否一致\n   - Figure/Table 的信息传达效率\n   - Limitations 节是否充分\n\n5. **EMNLP 2026 特定要求**：\n   - 检查是否有 Responsible NLP Checklist 相关内容（注意：此 checklist 在 OpenReview 表单中填写，不在论文中）\n   - 是否有 Ethics Statement（可选）\n   - Limitations 节（mandatory，不计入页数限制）\n\n请按以下格式输出审稿报告：\n\n### Summary（2-3 句）\n### Strengths（S1, S2, ...）\n### Weaknesses（W1, W2, ...，标注 CRITICAL/MAJOR/MINOR）\n### Questions（Q1, Q2, ...）\n### Missing References\n### Detailed Comments（按 Section 逐条）\n### Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-23T01:27:07.336392+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 618 · 2026-05-23T01:27:20.522189+00:00_

Round 1 已启动：

- **Reviewer 1**（方法严谨性）已分配——审查理论证明、假设合理性、实验方法论、ASV 框架
- **Reviewer 2**（新颖性/完整性）已分配——审查贡献定位、相关工作、格式合规、写作质量
- **视觉审查 Agent** 已派发（并行，不阻塞）
- **外部审稿**：未启用

等待两位 Reviewer 返回独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 619 · 2026-05-23T01:33:49.395402+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告（方法严谨性）

### Summary
本文系统性地刻画了 K≥3 多分类标注误差在七种典型因果 DAG 拓扑下的传播机制。在线性 SEM 下推导了偏差表达式，证明了 confounding 和 collider 的 sign preservation，引入了 ASV 敏感性框架，并证明了一个 FWL 不变性结果（matrix-based correction 对四种拓扑完全无效）。论文诚实地建立了三级认识论层次（Proved/Verified/Conjectured），且所有声称 "proved" 的结果经逐步验证均正确。

---

### 总体评分
**Overall**: 3.5（Borderline Conference）
**一句话总结**: 理论框架严谨、层次分明，但核心形式化保证（Theorem 1）仅限 K=2+proportional effects，与论文标题/框架暗示的 K≥3 一般性之间存在落差。

### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 所有 proved claims 经逐步验证正确；认识论三层分级诚实清晰 |
| Excitement | 3.5/5 | 问题重要 timely，FWL不变性是真正新发现，但线性SEM+proportional effects限制了impact |
| Reproducibility | 4/5 | 承诺代码公开，DGP参数显式给出，实验设置描述充分 |
| Overall | 3.5/5 | 方法论上乘但形式化保证的scope需与框架一般性收窄 |
| Confidence | 4/5 | 逐步验证了全部附录证明，熟悉因果推断和measurement error文献 |

---

### Must-Fix 问题

**N1** [critical] Theorem 1 形式化保证的 scope 过窄，与论文定位不匹配
- 位置：Section 3.3 Theorem 1; Appendix A.4
- Theorem 1（envelope monotonicity）仅对 K=2 + proportional effects (f=λg) + (C₀)ⱼⱼ ≥ 1/2 成立。但论文核心创新是 K≥3 场景。对 K≥3，论文依赖 Observation 1（worst-case deviation < 0.005）和 Conjecture 1（ε < 0.06），无形式化保证。ASV 框架的理论基础——单调性——在 K≥3 regime 中缺乏保证。
- 建议：(1) Section 3.3 更显式讨论 K≥3 下 ASV 的理论地位；(2) 定量讨论 ε-approximate monotonicity 对 δ* precision 的影响（当前 "δ* uncertainty < 0.6" 过于简略）；(3) 或尝试推广 Theorem 1 到 K=3。

**N2** [critical] Proportional effects 假设 (f = λg) 过强且讨论不充分
- 位置：Theorem 1; Proposition 2; Appendix A.5
- f = λg 要求 A 对 Y 和 A 对 T 的效应完全成比例——在 NLP 因果推断中几乎不可验证。当 f ≠ λg 时，Proposition 4 显示 λ(C) 有 15-17% 概率超出 [0,1]，sign preservation 可失败。
- 建议：(1) 给出 proportional effects 在 NLP 中成立/不成立的具体例子；(2) 报告 general case 的详细统计；(3) 考虑弱化条件。

---

### Should-Fix 问题

**W1** [major] "Primary coefficient never reverses" 认识论定位模糊
- 位置：Section 3.2 Numerical Verification 2; Abstract
- 纯经验观察（100K矩阵 × |β₁|/|β₂| ∈ [1,50]）被 abstract 赋予了过高的 prominence。对 K≥4，精心构造的 C 可能打破此规律。建议降低表述强度并讨论反例可能性。

**W2** [major] Non-differential misclassification 在 LLM 场景中的合理性需更深入讨论
- 位置：Definition 1; Appendix B.5; Limitations
- LLM 的 pretraining data 本身可能包含 A-Y 的统计关联，导致即使无显式 Y access 也产生 differential misclassification。Stress test 未讨论 realistic ε 范围，也未提供估计 ε 的方法。

**W3** [major] δ* uncertainty bound 过宽
- 位置：Section 3.3
- δ* uncertainty < 0.6 在 δ* ∈ [0.1, 0.5] 时 relative uncertainty > 100%。Main text 应明确说明 point estimate 不精确性，推荐 Bootstrap CI。

**W4** [minor] Table 1 中 Collider "Amplification=100%" 与 "protective" 描述矛盾
- 位置：Table 1; Section 3.2
- "Violation" 和 "Amplification" 列的精确定义需要在 caption 中明确。

**W5** [minor] Conjecture 1 violation count（60-97%矩阵）与 "approximately monotonic" 表述的张力
- 位置：Appendix B.11, Table 10
- 建议明确指出"绝大多数矩阵违反 strict monotonicity，但所有违反幅度可忽略"。

---

### Questions
- Q1: Theorem 1 推广到 K=3 的具体障碍是什么？（Step 4 中 V_B'(1) ≤ 0 的 K=2 代数结构能否推广？）
- Q2: Primary coefficient preservation 能否形式化为 magnitude dominance 条件？
- Q3: ASV parameterization 中 C₀ 的选择如何影响 δ* 可比性？
- Q4: FWL breakdown 幅度 (~10⁻³) 是否随 N 或 K 增大而变化？

---

### Missing References
无明显遗漏。

### 主要优势
- S1: K=2→K≥3 的 structural transition 是真正的理论贡献
- S2: 三级认识论层次在 ML 论文中罕见且值得推广
- S3: FWL 不变性是优雅且实用的负面结果
- S4: 实验验证广度令人印象深刻（7 topologies × 23 LLM configs × cross-K × logistic DGP）
- S5: 所有声称 proved 的证明技术正确、自包含、可独立验证

---

### 证明验证详细记录

以下是我逐步验证的结果：

1. **Proposition 1(a) — Confounding sign preservation**: Proposition 2 (proportional, B(C) = (1-η)B_OV, η∈[0,1]) ✓; Proposition 3 (general, Cauchy-Schwarz bound |B| ≤ B̄) ✓
2. **Proposition 1(b) — Collider sign preservation**: Proposition 5 (proportional, |B(C)| ≤ |B(I)|) ✓; Proposition 6 (general, Cauchy-Schwarz) ✓
3. **Proposition 1(c) — Exposure counterexample**: Proposition 7, explicit construction verified: β₁=1, plim β̂₁=-1.903 ✓
4. **Theorem 1 — Envelope monotonicity K=2**:
   - Step 1 (V_B convexity via perspective function): ✓
   - Step 2 (derivative formula eq:dVB): ✓
   - Step 3 (V_B'(0)≤0): ✓
   - Step 4 (V_B'(1)≤0 for K=2 under a,b≥1/2): ✓, factoring verified
   - Step 5 (convexity + endpoint → global monotonicity): ✓
   - Step 6 (composition with increasing h): ✓
5. **Lemma (Bias decomposition)**: FWL derivation correct, D(C)>0 argument valid ✓
6. **Mediation monotonicity** (Appendix A.5): σ_ε² = E[Var(T|A)] constant via column-stochasticity ✓; structural identity with confounding ✓
7. **Proposition 4 (Mediation leakage)**: λ(C)∈[0,1] under proportional effects ✓; 15-17% out-of-bound for general f ✓

所有声称 proved 的结果均正确。Mediation/M-bias/front-door 的 sign preservation 正确标记为 numerical verification 而非 proof。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 620 · 2026-05-23T01:33:55.240460+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 621 · 2026-05-23T01:34:05.539098+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：Overall 3.5（Borderline Conference）。证明链在声称 proved 的部分全部正确，但两个 critical 问题影响接收：(1) Theorem 1 仅限 K=2 + proportional effects，ASV 框架在论文最关心的 K≥3 regime 缺乏形式化保证；(2) proportional effects 假设在 NLP 因果推断场景中几乎不可验证，且 general case 有 15-17% 的 sign preservation 失败率。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-23T01:34:10.147474+00:00_

收到 Reviewer 1 报告，等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 66

## Round 66

6 recorded events


### User

_source line 623 · 2026-05-23T01:34:51.220077+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告 — 新颖性与完整性

## Summary（2-3 句）

本文系统分析了 K 类（K≥3）非差异性误分类在七种因果 DAG 拓扑下对因果估计的影响，提出 Annotation Sensitivity Values（ASV）框架和拓扑感知的校正指南。论文在理论推导（bias 表达式、sign preservation 条件、envelope monotonicity）和实验验证（Monte Carlo + 真实 LLM confusion matrix）两个层面展开，并报告了 FWL 不变性这一负面结果。整体而言，这是一篇扎实的分析性工作，填补了多类标注误差在因果推断中传播行为的系统性空白，但 ASV 框架的方法论新颖性和实证验证范围存在可提升空间。

---

## Strengths

**S1. 系统性跨拓扑分析——填补真实空白。** 此前工作要么限于 binary treatment（Brenner 1993; Teblunthuis 2024），要么仅覆盖单一拓扑（Lee & Wood-Doughty 2024 只做 confounding）。本文首次在统一框架下比较 7 种 DAG 拓扑 × K≥3 类别的 bias 行为，揭示了同一 confusion matrix 在不同因果结构中产生定性不同偏差的现象。这一"首次跨拓扑系统比较"的声称经核查相关文献后**基本成立**。

**S2. K≥3 binarization collapse 发现。** Section B.1（Appendix）和正文 Section 4.2 展示了 K→binary 折叠引入额外 bias 的现象（从 M-bias 的 Δ=0.006 到 IV 的 Δ=0.926），这是一个对 NLP 实践有直接指导意义的发现：研究者不能简单将多类标注二值化后套用 binary 理论。

**S3. 理论-实验双重验证。** Proposition 1 的 sign preservation 条件和 Theorem 1 的 envelope monotonicity 均有：(i) 解析证明或数值验证（20,000+ random C matrices），(ii) 真实 LLM confusion matrix 验证（23 configurations × 4 LLMs）。这种双重验证增强了可信度。

**S4. FWL 不变性作为实用负面结果。** Section 4.4 证明对于 A 作为协变量的四种拓扑，任何对 C 的线性变换（包括 C⁻¹ 校正）无法改变 treatment coefficient。这一结果虽从 FWL 定理可代数推导，但显式指出其对 matrix-based 校正方法的 futility 意义，对不熟悉 FWL 的 NLP 实践者有切实价值。

**S5. 相关工作覆盖全面。** 流行病学测量误差（Carroll 2006, Gustafson 2004, Buonaccorsi 2010）、NLP text-as-data（Feder et al. 2022, Keith et al. 2020）、LLM 标注质量（Baumann 2025, Kim et al. 2025, Gligorić et al. 2025）、PPI 校正方法（Angelopoulos 2023, Zrnić & Candès 2024, Cadei et al. 2025, Demirel et al. 2024）均有引用。Audinet et al. (2025) 也被讨论。覆盖面在该交叉领域论文中属优秀水平。

**S6. 实用产出。** Algorithm 1（page 26）提供可操作的 topology→correction 映射流程；ASV 框架的三类指标（magnitude, significance, sign-flip）给出了分层决策逻辑。

---

## Weaknesses

**W1 [MAJOR] ASV 框架与现有 sensitivity analysis 工具的方法论差异界定不足。**
- 具体位置：Section 3.3, page 5
- 问题：ASV 的三个子指标（magnitude, significance, sign-flip）在结构上与 E-values（VanderWeele & Ding 2017）和 partial R²（Cinelli & Hazlett 2020）高度同构：均为"估计量能容忍多少未知干扰（此处为标注误差 δ）后翻转结论"的阈值分析。论文承认了与 E-values 的联系（"analogous to E-values", page 5），但未清晰阐述 ASV 在**方法论层面**（而非应用对象层面）有何结构性创新。当前的差异化论述主要是"parametrizes from annotation error severity rather than unified variable strength"——这是参数化对象的切换，不是方法论的突破。
- 为什么影响评分：对于 novelty 评估维度，如果 ASV 本质上是 sensitivity analysis 的标准模板应用于新参数化，则该贡献应被定位为"systematic application"而非"novel framework"。这会影响 Excitement 评分。
- 建议：明确列出 ASV 相对于 E-value/partial R² 的结构性差异（如 topology-dependent threshold behavior, 三类指标的分层语义），或降低 novelty 声称的力度。

**W2 [MAJOR] 非差异性误分类假设过强，主文讨论不足。**
- 具体位置：Definition 1 (page 3), Limitations (page 8), Appendix B.5
- 问题：全文理论建立在 P(A*|A,X,Y,Z) = P(A*|A) 的非差异性假设上。然而 LLM 标注器几乎必然违反这一假设：text features 与 Y 相关，LLM 的误分类率会随文本内容（进而随 Y）变化。例如，情感分析中讽刺性文本的误标率更高，且讽刺性与结果变量可能相关。Appendix B.5 的 stress test（Table 7）显示当 differential departure ε≥0.10 时 violation rate 升至 5.6-14.2%，但主文仅在 Limitations 用一句话带过。
- 为什么影响评分：这不是一个纯理论限制——它直接质疑框架在 LLM 标注场景中的适用性。考虑到论文的 motivation 正是 LLM 标注，这一张力需要在主文中正面讨论。
- 建议：在 Section 3.1 或 Method 结尾增加一段讨论，阐明：(a) 何时非差异性假设合理（如 LLM 仅根据 A 的表面特征而非 Y 相关信息做分类），(b) 违反时 bias 表达式如何定性改变，(c) 引导读者参考 Appendix B.5 的定量分析。

**W3 [MAJOR] 实证验证范围与理论通用性声称之间存在差距。**
- 具体位置：Section 4.3-4.4, Table 3
- 问题：理论覆盖 7 种拓扑 × 任意 K，但实证验证仅用 3 个 NLP 任务（HumAID K=10, VAST K=5, CivilComments K=2）× 4 LLMs。其中 CivilComments 是 K=2 即 binary case，不完全体现 multi-class 优势。Monte Carlo 模拟虽然广泛（100,000 matrices），但使用 Dirichlet(1,1,...,1) 生成 confusion matrix，这与真实 LLM 的 error structure 可能有系统性差异（真实 LLM 的 off-diagonal errors 通常呈现语义相似类别间的聚集模式，而非均匀分布）。
- 为什么影响评分：有限的实证验证使得从理论到实践的可推广性存疑。
- 建议：(a) 增加 1-2 个 K≥5 的真实 NLP task；(b) 在 Monte Carlo 中加入 structured confusion matrix（如近邻类别高误分类率）作为补充 DGP。

**W4 [MINOR] Conjecture 1 未证明，但被用作 ASV 分析的基础。**
- 具体位置：Section 3.3 (page 5), Conjecture 1
- 问题：Envelope monotonicity（对非 IV 拓扑 bias 是 δ 的近似单调函数，对 collider/M-bias 非递增）作为 Conjecture 而非 Theorem 出现。虽然数值验证覆盖 20,000+ 配置且 worst-case deviation ≤ 0.102，但 ASV 的 well-definedness 隐含依赖于这一单调性（否则 min{δ: |bias| > threshold} 可能不唯一或无意义）。
- 建议：明确讨论若 Conjecture 1 局部不成立时 ASV 的鲁棒性——例如 ASV 是否取 supremum 而非 min。

**W5 [MINOR] Abstract/Introduction 数字密度过高。**
- 具体位置：Abstract (page 1), Section 1 (pages 1-2)
- 问题：Abstract 中出现超过 20 个具体数字（K≥3, 3-4 categories, 37, 31%, 54%, K=2, 2×2, 100,000, K≥3, K=3, 61%, ≥0.7, 2.1%, R_F 0.614-0.690, 4.1%, ≤2.1% 等），核心信息被数据密度稀释。Introduction 的 contribution 列表（page 2）同样包含大量具体数值。
- 建议：Abstract 保留 3-5 个最关键的数字，其余移至正文。重点传达 qualitative insights（如"K≥3 breaks sign preservation guarantee"），而非精确数值。

**W6 [MINOR] FWL 不变性结果的 novelty 需要澄清。**
- 具体位置：Section 4.4 (page 8)
- 问题：对于熟悉 FWL 定理的读者，C⁻¹A 与 A 生成相同列空间因此 OLS 系数不变，这是 FWL 的直接推论。论文将其作为"finding"呈现，但未讨论此结果是否在 measurement error 文献中已被认知。如果是已知结果，贡献在于显式指出其对 NLP 校正实践的意义；如果是新结果，则应更强调其理论价值。
- 建议：增加一句说明此结果在 measurement error 文献中的状态（已知 vs. 新）。

**W7 [MINOR] 图表可读性。**
- Figure 2 (page 7): sign reversal 用红色标记，未考虑色盲可及性。
- Figure 3 (page 8): 拓扑示意图文字偏小，难以在打印版清晰辨认。
- Figure 4 (page 20, Appendix): 信息密度高但可读性可接受。

---

## Questions

**Q1.** ASV 能否提供 E-values 或 partial R² 无法给出的可操作指导？能否举一个具体示例，说明某个决策在 E-value 框架下不可达但在 ASV 框架下可以做出？

**Q2.** Monte Carlo 中 Dirichlet(1,1,...,1) 的参数化选择对结果的影响有多大？如果改用更集中的先验（如 Dirichlet(10,0.5,...,0.5) 模拟高 accuracy 场景），sign preservation 条件和 monotonicity 是否仍然成立？

**Q3.** 对于实证验证中的 23 个 LLM configurations（Section 4.2），是否存在任何配置使得理论预测失败？如果没有，是否因为验证范围太窄而遗漏了失败案例？

**Q4.** Exposure（IV）拓扑的 ASV 呈现 sharp phase transition（Section 4.3），Conjecture 1 对该拓扑也未能保证 monotonicity。这是否意味着 ASV 对 IV 拓扑本质上不可靠？

**Q5.** FWL 不变性在 logistic regression 下仅近似成立（|ΔSF_τ| < 0.02）。当非线性更强时（如高维交互项），这一近似是否会失效？

---

## Missing References

1. **Rosenbaum (2002)** "Observational Studies" — sensitivity analysis 领域的经典奠基著作。当前 ASV 的定位借鉴了 sensitivity analysis 传统但未引用此基础文献。
2. **Ding & VanderWeele (2016)** "Sensitivity analysis without assumptions on unmeasured confounding" — E-value 的前驱工作，与 ASV 的方法论对比相关。
3. 建议确认 **Teblunthuis (2024)** 的完整引用信息是否存在于参考文献列表中——正文 Related Work (Section 2) 多次引用但我在 References 中未能明确识别到对应条目（可能因 PDF 分辨率受限）。

---

## Detailed Comments（按 Section）

### Abstract (page 1)
- 数字密度问题（见 W5）。"across 37 annotation tasks, 31% of hypotheses yield incorrect conclusions" 虽然正确归因于 Baumann et al.，但在 abstract 中引入他人的数字 来支撑自己的动机略显冗余。
- "first to characterize" 声称经查证基本成立，但建议加限定词如 "first systematic analysis under K≥3"。

### Introduction (pages 1-2)
- 三个 contribution 的列表清晰。但 Contribution 2（ASV）的描述混合了定义和结果（"revealing a topology-dependent vulnerability spectrum from IV (maximally fragile, 52.6% sign reversal) to M-bias (immune, ASV → ∞)"），建议分离定义与发现。
- Footnote 1 定义 "computed as the ratio of maximum to minimum..." 放在脚注中不太合适，这是核心定义的一部分。

### Related Work (Section 2, pages 2-3)
- 覆盖面优秀（见 S5）。
- "These works either restrict to binary labels, cover a single topology, or diagnose quality without connecting it to causal validity" — 这一概括准确但略有 strawman 倾向，因为某些工作（如 Blackwell et al. 2017）的目标本就不包括多拓扑比较。

### Method (Section 3, pages 3-5)
- Definition 1（非差异性误分类）表述清晰。
- Proposition 1 的条件列表（sign preservation）涉及多个子条件（(a)-(e)），正文空间紧张下给出了足够的直觉解释。
- Theorem 1（envelope monotonicity，K=2）证明完整（Appendix A.4）。
- Section 3.3 ASV 定义中 "analogous to E-values" 的措辞需要加强（见 W1）。

### Experiments (Section 4, pages 5-8)
- **4.1 Setup** 清晰：Dirichlet(1,1,...,1) parameterization, N=10,000, 100,000 matrices。
- **4.2 Bias Taxonomy**: Table 1 的 topology × violation/sign-flip/amplification 展示有效。但 "Exposure DAG: sign reversed under multi-class misclassification" 的发现（violation rate 13.7%）是论文最重要的实证结果之一，值得更多讨论空间。
- **4.3 ASV Framework Validation**: Magnitude/significance/sign-flip ASV 的三层分析逻辑清晰。Figure 4（Appendix）的 ranking 可视化有效。
- **4.4 Correction Guidance**: Table 4 展示 5 种 correction 方法 × 7 种拓扑的 RMSE reduction，信息密度高但有效。FWL 不变性的 logistic breakdown 验证（Table 5）是重要的补充。
- **4.4 末尾 Method ranking**: "PPI++ achieves the highest grand mean RMSE reduction (47.0%) but requires gold labels" — 这一实用总结对读者有价值。

### Conclusion & Limitations (page 8)
- Conclusion 准确总结了三个贡献。
- Limitations 涵盖了非差异性假设、单标注器、拓扑不确定性、模型特异性。覆盖面合理但可更深入（见 W2）。
- "Code for ASV computation and all experiments will be publicly released" — 承诺合理。

### Appendix 
- 证明完整（A.1-A.5 for Proposition 1 各拓扑, A.4 for Theorem 1）。
- B.1 Binarization Collapse 是一个很好的补充分析。
- B.3 ClinicalBERT Case Study 展示了实际应用场景（Lee & Wood-Doughty 2024 的 smoking status），增强了实用性论证。
- B.5 Non-Differential Assumption Stress Test（Table 7）是关键补充——建议在主文中增加引导。
- B.7 Bootstrap Uncertainty of ASV（Table 8, Figure 8）展示了 ASV 的统计不确定性，方法论上合理。
- Algorithm 1 (page 26) 的 topology→correction 决策树是有价值的实用产出。

---

## Overall Assessment

**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 扎实的分析性工作，首次系统覆盖多类标注误差在七种因果拓扑下的传播行为，但 ASV 框架的方法论增量有限，实证验证范围偏窄。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 理论推导严谨，证明完整（Appendix 11 页），Monte Carlo 验证广泛。Conjecture 1 未证明但数值验证充分。主要扣分：非差异性假设对 LLM 场景的适用性讨论不足。 |
| Excitement | 3 / 5 | 填补了 NLP × 因果推断交叉领域的真实空白，但受众较窄（需要同时关注 measurement error theory 和 LLM annotation 的研究者）。ASV 是已有 sensitivity analysis 模板的新应用，非方法论突破。FWL 不变性是 FWL 的直接推论。 |
| Reproducibility | 4 / 5 | Monte Carlo setup 描述清晰，代码承诺公开，DGP 参数完整。真实 LLM 实验的 confusion matrix 来源和计算过程可复现。 |
| Overall Assessment | 3.5 / 5 | Borderline Conference。理论贡献扎实但增量（systematic extension > methodological innovation），适合 Findings 或 borderline main conference。 |
| Confidence | 4 / 5 | 熟悉 measurement error、sensitivity analysis 和因果推断文献，仔细阅读了全部正文和附录。 |

### 格式合规检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | 正文至第 8 页（含 Limitations），References 从第 8 页底部开始 |
| ACL 模板 | ✓ | 标准双栏格式，字体大小正确 |
| Double-blind 匿名 | ✓ | "Anonymous ACL submission"，无致谢，未发现自引暴露 |
| 引用格式 | ✓ | natbib 风格，parenthetical/textual 混用一致 |
| Preprint 标注 | ✓ | Baumann et al. 2025, Cadei et al. 2025 等标注为 arXiv preprint |
| Limitations 节 | ✓ | 存在，不计入页数限制 |
| Responsible NLP Checklist | N/A | 正确——在 OpenReview 表单中填写，非论文内容 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-23T01:35:46.774082+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也可对其 Strengths 和 Missing References 发表看法。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n### Summary\n本文系统分析了 K 类（K≥3）非差异性误分类在七种因果 DAG 拓扑下对因果估计的影响，提出 ASV 框架和拓扑感知的校正指南。论文在理论推导和实验验证两个层面展开，并报告了 FWL 不变性这一负面结果。整体而言，这是一篇扎实的分析性工作，填补了多类标注误差在因果推断中传播行为的系统性空白，但 ASV 框架的方法论新颖性和实证验证范围存在可提升空间。\n\n### Strengths\n- S1: 系统性跨拓扑分析——填补真实空白。\"首次跨拓扑系统比较\"声称经核查基本成立。\n- S2: K≥3 binarization collapse 发现——对 NLP 实践有直接指导意义。\n- S3: 理论-实验双重验证。\n- S4: FWL 不变性作为实用负面结果。\n- S5: 相关工作覆盖全面。\n- S6: 实用产出（Algorithm 1, ASV 三类指标）。\n\n### Weaknesses\n\n**W1 [MAJOR] ASV 框架与现有 sensitivity analysis 工具的方法论差异界定不足。**\n- ASV 的三个子指标在结构上与 E-values 和 partial R² 高度同构。论文承认了联系（\"analogous to E-values\"），但未清晰阐述 ASV 在方法论层面有何结构性创新。当前差异化论述主要是参数化对象的切换，不是方法论突破。如果 ASV 本质上是 sensitivity analysis 的标准模板应用于新参数化，则该贡献应被定位为\"systematic application\"而非\"novel framework\"。\n\n**W2 [MAJOR] 非差异性误分类假设过强，主文讨论不足。**\n- LLM 标注器几乎必然违反 P(A*|A,X,Y,Z)=P(A*|A)：text features 与 Y 相关，LLM 的误分类率会随文本内容变化。Stress test（Table 7）显示 ε≥0.10 时 violation rate 升至 5.6-14.2%，但主文仅在 Limitations 用一句话带过。\n\n**W3 [MAJOR] 实证验证范围与理论通用性声称之间存在差距。**\n- 理论覆盖 7 种拓扑 × 任意 K，但实证验证仅用 3 个 NLP 任务 × 4 LLMs。CivilComments 是 K=2。Monte Carlo 使用 Dirichlet(1,1,...,1)，与真实 LLM 的语义聚集 error structure 可能有系统性差异。\n\n**W4 [MINOR] Conjecture 1 未证明，但被用作 ASV 分析的基础。**\n- ASV 的 well-definedness 隐含依赖于单调性，若 Conjecture 1 局部不成立，min{δ: |bias|>threshold} 可能不唯一。\n\n**W5 [MINOR] Abstract/Introduction 数字密度过高。**\n- Abstract 中出现超过 20 个具体数字，核心信息被数据密度稀释。\n\n**W6 [MINOR] FWL 不变性结果的 novelty 需要澄清。**\n- 对熟悉 FWL 的读者，C⁻¹A 与 A 生成相同列空间因此 OLS 系数不变是直接推论。论文未讨论此结果在 measurement error 文献中是否已被认知。\n\n**W7 [MINOR] 图表可读性。**\n- Figure 2 未考虑色盲可及性；Figure 3 文字偏小。\n\n### Questions\n- Q1: ASV 能否提供 E-values 无法给出的可操作指导？能否举一个具体示例？\n- Q2: Dirichlet(1,1,...,1) 参数化对结果影响有多大？改用集中先验（如 Dirichlet(10,0.5,...,0.5)）后 sign preservation 是否仍成立？\n- Q3: 23 个 LLM configurations 是否存在理论预测失败的配置？\n- Q4: ASV 对 IV 拓扑本质上是否不可靠？\n- Q5: FWL 不变性在更强非线性下是否失效？\n\n### Missing References\n1. Rosenbaum (2002) \"Observational Studies\" — sensitivity analysis 经典奠基\n2. Ding & VanderWeele (2016) \"Sensitivity analysis without assumptions\" — E-value 前驱\n3. 建议确认 Teblunthuis (2024) 引用完整性\n\n### Overall Assessment\n3.5 / 5（Borderline Conference）。扎实的分析性工作，首次系统覆盖多类标注误差在七种因果拓扑下的传播行为，但 ASV 框架的方法论增量有限，实证验证范围偏窄。Excitement 3/5。\n\n### 格式合规检查\n正文 ≤ 8 页 ✓，ACL 模板 ✓，Double-blind ✓，引用格式 ✓，Preprint 标注 ✓，Limitations 节 ✓。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也可对其 Strengths 和 Missing References 发表看法。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n### Summary\n本文系统分析了 K 类（K≥3）非差异性误分类在七种因果 DAG 拓扑下对因果估计的影响，提出 ASV 框架和拓扑感知的校正指南。论文在理论推导和实验验证两个层面展开，并报告了 FWL 不变性这一负面结果。整体而言，这是一篇扎实的分析性工作，填补了多类标注误差在因果推断中传播行为的系统性空白，但 ASV 框架的方法论新颖性和实证验证范围存在可提升空间。\n\n### Strengths\n- S1: 系统性跨拓扑分析——填补真实空白。\"首次跨拓扑系统比较\"声称经核查基本成立。\n- S2: K≥3 binarization collapse 发现——对 NLP 实践有直接指导意义。\n- S3: 理论-实验双重验证。\n- S4: FWL 不变性作为实用负面结果。\n- S5: 相关工作覆盖全面。\n- S6: 实用产出（Algorithm 1, ASV 三类指标）。\n\n### Weaknesses\n\n**W1 [MAJOR] ASV 框架与现有 sensitivity analysis 工具的方法论差异界定不足。**\n- ASV 的三个子指标在结构上与 E-values 和 partial R² 高度同构。论文承认了联系（\"analogous to E-values\"），但未清晰阐述 ASV 在方法论层面有何结构性创新。当前差异化论述主要是参数化对象的切换，不是方法论突破。如果 ASV 本质上是 sensitivity analysis 的标准模板应用于新参数化，则该贡献应被定位为\"systematic application\"而非\"novel framework\"。\n\n**W2 [MAJOR] 非差异性误分类假设过强，主文讨论不足。**\n- LLM 标注器几乎必然违反 P(A*|A,X,Y,Z)=P(A*|A)：text features 与 Y 相关，LLM 的误分类率会随文本内容变化。Stress test（Table 7）显示 ε≥0.10 时 violation rate 升至 5.6-14.2%，但主文仅在 Limitations 用一句话带过。\n\n**W3 [MAJOR] 实证验证范围与理论通用性声称之间存在差距。**\n- 理论覆盖 7 种拓扑 × 任意 K，但实证验证仅用 3 个 NLP 任务 × 4 LLMs。CivilComments 是 K=2。Monte Carlo 使用 Dirichlet(1,1,...,1)，与真实 LLM 的语义聚集 error structure 可能有系统性差异。\n\n**W4 [MINOR] Conjecture 1 未证明，但被用作 ASV 分析的基础。**\n- ASV 的 well-definedness 隐含依赖于单调性，若 Conjecture 1 局部不成立，min{δ: |bias|>threshold} 可能不唯一。\n\n**W5 [MINOR] Abstract/Introduction 数字密度过高。**\n- Abstract 中出现超过 20 个具体数字，核心信息被数据密度稀释。\n\n**W6 [MINOR] FWL 不变性结果的 novelty 需要澄清。**\n- 对熟悉 FWL 的读者，C⁻¹A 与 A 生成相同列空间因此 OLS 系数不变是直接推论。论文未讨论此结果在 measurement error 文献中是否已被认知。\n\n**W7 [MINOR] 图表可读性。**\n- Figure 2 未考虑色盲可及性；Figure 3 文字偏小。\n\n### Questions\n- Q1: ASV 能否提供 E-values 无法给出的可操作指导？能否举一个具体示例？\n- Q2: Dirichlet(1,1,...,1) 参数化对结果影响有多大？改用集中先验（如 Dirichlet(10,0.5,...,0.5)）后 sign preservation 是否仍成立？\n- Q3: 23 个 LLM configurations 是否存在理论预测失败的配置？\n- Q4: ASV 对 IV 拓扑本质上是否不可靠？\n- Q5: FWL 不变性在更强非线性下是否失效？\n\n### Missing References\n1. Rosenbaum (2002) \"Observational Studies\" — sensitivity analysis 经典奠基\n2. Ding & VanderWeele (2016) \"Sensitivity analysis without assumptions\" — E-value 前驱\n3. 建议确认 Teblunthuis (2024) 引用完整性\n\n### Overall Assessment\n3.5 / 5（Borderline Conference）。扎实的分析性工作，首次系统覆盖多类标注误差在七种因果拓扑下的传播行为，但 ASV 框架的方法论增量有限，实证验证范围偏窄。Excitement 3/5。\n\n### 格式合规检查\n正文 ≤ 8 页 ✓，ACL 模板 ✓，Double-blind ✓，引用格式 ✓，Preprint 标注 ✓，Limitations 节 ✓。"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-23T01:36:17.093123+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30319
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-23T01:36:17.294655+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Must-Fix/Should-Fix 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也可对其 Strengths 和证明验证发表看法。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n### Summary\n本文系统性地刻画了 K≥3 多分类标注误差在七种典型因果 DAG 拓扑下的传播机制。在线性 SEM 下推导了偏差表达式，证明了 confounding 和 collider 的 sign preservation，引入了 ASV 敏感性框架，并证明了一个 FWL 不变性结果。论文诚实地建立了三级认识论层次（Proved/Verified/Conjectured），且所有声称 \"proved\" 的结果经逐步验证均正确。\n\n### Overall: 3.5（Borderline Conference）\n所有 proved claims 正确，但两个 critical 问题：(1) Theorem 1 仅限 K=2 + proportional effects，与论文定位不匹配；(2) proportional effects 假设过强。\n\n### Must-Fix\n\n**N1 [critical] Theorem 1 形式化保证的 scope 过窄，与论文定位不匹配**\n- Theorem 1（envelope monotonicity）仅对 K=2 + proportional effects (f=λg) + (C₀)ⱼⱼ ≥ 1/2 成立。论文核心创新是 K≥3 场景，但 K≥3 依赖 Observation 1（deviation < 0.005）和 Conjecture 1（ε < 0.06），无形式化保证。ASV 框架的理论基础在 K≥3 regime 中缺乏保证。\n- 建议：(1) 更显式讨论 K≥3 下 ASV 的理论地位；(2) 定量讨论 ε-approximate monotonicity 对 δ* precision 的影响；(3) 或推广 Theorem 1 到 K=3。\n\n**N2 [critical] Proportional effects 假设 (f=λg) 过强且讨论不充分**\n- f=λg 要求 A 对 Y 和 A 对 T 的效应完全成比例，在 NLP 中几乎不可验证。General case 有 15-17% 的 sign preservation 失败率。\n- 建议：给出 NLP 中成立/不成立的具体例子，报告 general case 详细统计，考虑弱化条件。\n\n### Should-Fix\n\n**W1 [major] \"Primary coefficient never reverses\" 认识论定位模糊**\n- 纯经验观察被 abstract 赋予过高 prominence。对 K≥4，精心构造的 C 可能打破此规律。\n\n**W2 [major] Non-differential misclassification 在 LLM 场景中的合理性需更深入讨论**\n- LLM pretraining data 可能包含 A-Y 统计关联，导致即使无显式 Y access 也产生 differential misclassification。Stress test 未讨论 realistic ε 范围。\n\n**W3 [major] δ* uncertainty bound 过宽**\n- δ* uncertainty < 0.6 在 δ* ∈ [0.1, 0.5] 时 relative uncertainty > 100%。\n\n**W4 [minor] Table 1 中 Collider \"Amplification=100%\" 与 \"protective\" 描述矛盾**\n\n**W5 [minor] Conjecture 1 violation count 与 \"approximately monotonic\" 表述的张力**\n\n### Questions\n- Q1: Theorem 1 推广到 K=3 的具体障碍？\n- Q2: Primary coefficient preservation 能否形式化为 magnitude dominance 条件？\n- Q3: ASV parameterization 中 C₀ 选择如何影响 δ* 可比性？\n- Q4: FWL breakdown 幅度是否随 N 或 K 增大？\n\n### Missing References\n无明显遗漏。\n\n### 主要优势\n- S1: K=2→K≥3 structural transition 是真正的理论贡献\n- S2: 三级认识论层次在 ML 论文中罕见\n- S3: FWL 不变性是优雅且实用的负面结果\n- S4: 实验验证广度令人印象深刻\n- S5: 所有 proved 证明技术正确、自包含\n\n### 证明验证记录\nProposition 1(a)(b)(c), Theorem 1 (全 6 步), Lemma, Mediation monotonicity, Proposition 4 — 全部正确。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Must-Fix/Should-Fix 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也可对其 Strengths 和证明验证发表看法。\n\n---\n\n## Reviewer 1 完整审稿报告\n\n### Summary\n本文系统性地刻画了 K≥3 多分类标注误差在七种典型因果 DAG 拓扑下的传播机制。在线性 SEM 下推导了偏差表达式，证明了 confounding 和 collider 的 sign preservation，引入了 ASV 敏感性框架，并证明了一个 FWL 不变性结果。论文诚实地建立了三级认识论层次（Proved/Verified/Conjectured），且所有声称 \"proved\" 的结果经逐步验证均正确。\n\n### Overall: 3.5（Borderline Conference）\n所有 proved claims 正确，但两个 critical 问题：(1) Theorem 1 仅限 K=2 + proportional effects，与论文定位不匹配；(2) proportional effects 假设过强。\n\n### Must-Fix\n\n**N1 [critical] Theorem 1 形式化保证的 scope 过窄，与论文定位不匹配**\n- Theorem 1（envelope monotonicity）仅对 K=2 + proportional effects (f=λg) + (C₀)ⱼⱼ ≥ 1/2 成立。论文核心创新是 K≥3 场景，但 K≥3 依赖 Observation 1（deviation < 0.005）和 Conjecture 1（ε < 0.06），无形式化保证。ASV 框架的理论基础在 K≥3 regime 中缺乏保证。\n- 建议：(1) 更显式讨论 K≥3 下 ASV 的理论地位；(2) 定量讨论 ε-approximate monotonicity 对 δ* precision 的影响；(3) 或推广 Theorem 1 到 K=3。\n\n**N2 [critical] Proportional effects 假设 (f=λg) 过强且讨论不充分**\n- f=λg 要求 A 对 Y 和 A 对 T 的效应完全成比例，在 NLP 中几乎不可验证。General case 有 15-17% 的 sign preservation 失败率。\n- 建议：给出 NLP 中成立/不成立的具体例子，报告 general case 详细统计，考虑弱化条件。\n\n### Should-Fix\n\n**W1 [major] \"Primary coefficient never reverses\" 认识论定位模糊**\n- 纯经验观察被 abstract 赋予过高 prominence。对 K≥4，精心构造的 C 可能打破此规律。\n\n**W2 [major] Non-differential misclassification 在 LLM 场景中的合理性需更深入讨论**\n- LLM pretraining data 可能包含 A-Y 统计关联，导致即使无显式 Y access 也产生 differential misclassification。Stress test 未讨论 realistic ε 范围。\n\n**W3 [major] δ* uncertainty bound 过宽**\n- δ* uncertainty < 0.6 在 δ* ∈ [0.1, 0.5] 时 relative uncertainty > 100%。\n\n**W4 [minor] Table 1 中 Collider \"Amplification=100%\" 与 \"protective\" 描述矛盾**\n\n**W5 [minor] Conjecture 1 violation count 与 \"approximately monotonic\" 表述的张力**\n\n### Questions\n- Q1: Theorem 1 推广到 K=3 的具体障碍？\n- Q2: Primary coefficient preservation 能否形式化为 magnitude dominance 条件？\n- Q3: ASV parameterization 中 C₀ 选择如何影响 δ* 可比性？\n- Q4: FWL breakdown 幅度是否随 N 或 K 增大？\n\n### Missing References\n无明显遗漏。\n\n### 主要优势\n- S1: K=2→K≥3 structural transition 是真正的理论贡献\n- S2: 三级认识论层次在 ML 论文中罕见\n- S3: FWL 不变性是优雅且实用的负面结果\n- S4: 实验验证广度令人印象深刻\n- S5: 所有 proved 证明技术正确、自包含\n\n### 证明验证记录\nProposition 1(a)(b)(c), Theorem 1 (全 6 步), Lemma, Mediation monotonicity, Proposition 4 — 全部正确。"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-23T01:36:18.764581+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1469
}
```

</details>

---


### Assistant

_source line 628 · 2026-05-23T01:36:21.866764+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 629 · 2026-05-23T01:36:24.506346+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。报告已提交至 Review Director，核心结论：

- **Overall 3.5/5（Borderline Conference）**，Soundness 4/5，Excitement 3/5
- **主要优势**：首次系统覆盖 7 种 DAG 拓扑 × K≥3 多类标注误差，理论推导严谨，FWL 不变性负面结果有实用价值
- **关键问题**：ASV 框架与 E-values/partial R² 的方法论差异界定不足（W1），非差异性假设对 LLM 场景过强且主文讨论不够（W2），实证验证仅 3 个 NLP 任务偏窄（W3）
- **格式合规**：全部通过（8 页正文、double-blind、Limitations 节均符合要求）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 630 · 2026-05-23T01:36:30.176782+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 631 · 2026-05-23T01:38:11.570915+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

### 对 Weaknesses 的回应

**[AGREE] R2-W1: ASV 框架方法论新颖性有限**
同意核心判断。ASV 在结构上是 sensitivity analysis 标准模板应用于新参数化。但补充：将 K²-维 confusion matrix 空间还原为 1D 路径需要 Theorem 1 (envelope monotonicity)，这个还原步骤非平凡——E-values 处理标量 sensitivity parameter 不需要类似降维。ASV 的技术贡献在证明 1D parameterization 合法，而非框架设计本身（尽管此证明也仅 K=2 完成）。建议作者定位为 "systematic application with non-trivial reduction theorem"。

**[AGREE] R2-W2: 非差异性误分类假设讨论不足**
与我的 W2 完全一致。补充：R2 引用的 "5.6-14.2%" 数字似乎不准确——Table 7 实际数据是 sign-flip 从 2.0%(ε=0) 到 22.9%(ε=0.50)，violation 从 13.3% 到 54.6%。两位 reviewer 共同遗漏了一个更隐蔽来源：LLM pretraining data 本身包含 A-Y 统计关联。

**[REBUT] R2-W3: 实证验证范围偏窄**
R2 低估了验证广度：23 LLM configs × 7 topologies = 161 scenarios；K 覆盖 2,3,10；cross-K checks at K=3,5,7 with 100K matrices (Appendix B.8)；logistic DGP robustness for all 7 topologies (Appendix B.6)。论文还用 23 个 real LLM confusion matrices 验证——这就是真实 "语义聚集" 误差结构。R2 的 Dirichlet 先验担忧部分被 diagonal-stratified analysis (Section 4.2) 和 real matrices 覆盖。CivilComments K=2 确实是弱点。

**[AGREE] R2-W4: Conjecture 1 用作 ASV 基础**
与我的 N1 一致。补充 R2 未提及的：Table 10 显示 60-97% 矩阵违反 strict monotonicity。如果局部违反，min{δ: |bias|>threshold} 不唯一，δ* 定义有歧义。

**[REBUT] R2-W5: Abstract 数字密度过高**
不同意。对分析性论文，abstract 中的具体数字（83.4%, MAPE 1.6%, 0% bias reduction）是精确声明的必要组成，帮助读者快速判断 scope。去掉会变成空洞定性声明。风格偏好，不影响质量。

**[REBUT] R2-W6: FWL 不变性 novelty**
部分不同意。数学事实 col(D*M)=col(D*) 确实 trivial，但论文贡献在于：(1) 识别所有主流 correction 方法（naive plug-in, MLA, SIMEX 极限）都落入此类；(2) 转化为实用路由规则 (Algorithm 1 Step 3)；(3) 验证 SIMEX 也被困住（非简单 D*M 变换）。我不知道 measurement error 文献中有先前工作明确指出此结果。Novelty 在识别和应用，非证明技巧。

**[AGREE] R2-W7: 图表可读性**
未深入审查，不评判。

### 对 Questions 的回应

Q1: ASV 和 E-values 回答不同问题——E-values 指导"是否需要更多控制变量"，ASV 指导"是否需要更好标注器/gold labels"。论文应更清楚阐述此实际差异。
Q2: Diagonal-stratified analysis + real LLM matrices 部分回应，但集中先验检查有价值。
Q3: MAPE 1.6%，无 qualitative 预测失败——论文的优势。
Q4: 同意 ASV 对 IV 本质不可靠。论文应比仅在 Conjecture 中排除更明确地说明。
Q5: 仅测试 logistic（breakdown ~10⁻³）。更强非线性下可能显著增大，应在 Limitations 提及。

### Missing References 回应
Ding & VanderWeele (2016) 应引用——论文显式类比 E-values 但未引用理论源头。Rosenbaum (2002) 合理但非必需。

### R1-R2 评分对比
| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Overall | 3.5 | 3.5 | ✓ |
| Excitement | 3.5/5 | 3/5 | R2 略低 |

主要共识：non-differential 假设不足 (R1-W2, R2-W2)；Conjecture 1 与 ASV 基础 (R1-N1, R2-W4)。
主要分歧：实证验证范围（我认为合理）、FWL novelty（我评价更高）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 632 · 2026-05-23T01:38:16.980675+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 633 · 2026-05-23T01:38:19.591468+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心结论：两位 reviewer 在 overall 3.5 和两个关键问题（non-differential 假设、Conjecture 1 作为 ASV 基础）上达成共识；在实证验证范围和 FWL novelty 上存在分歧——我认为 161 scenarios 的验证是合理的，FWL 不变性的贡献在于识别和应用而非证明本身。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 634 · 2026-05-23T01:38:23.745623+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 70

## Round 70

8 recorded events


### User

_source line 635 · 2026-05-23T01:39:10.796821+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix

**[AGREE] R1-N1: Theorem 1 scope 过窄（K=2 only），与论文 K≥3 定位不匹配**

同意这是论文的核心张力。我在自己的审稿中也提出了类似问题（我的 W4）：Conjecture 1 未证明但被用作 ASV 分析的基础。具体而言：

- Theorem 1 仅覆盖 K=2 + proportional effects，而论文的 selling point 恰恰是 K≥3。
- K≥3 的 monotonicity 依赖 Observation 1（deviation < 0.005, Appendix B.11）和 Conjecture 1（ε < 0.06），均为数值验证而非形式化证明。
- R1 提出的建议（定量讨论 ε-approximate monotonicity 对 δ* precision 的影响）非常到位——如果 monotonicity 有 ε=0.06 的偏差，ASV 的 δ* 估计可能有 ±0.06 的误差，这在 δ* 本身较小时（如 IV topology 的 δ*≈0.05）会完全淹没信号。

补充：论文的三级认识论框架（Proved/Verified/Conjectured）是诚实的，但 Abstract 和 Introduction 的措辞没有充分反映这一分层。ASV 被呈现为一个完整的 "framework"，但其理论基础在 K≥3 regime 中实际上是 conjectural。

**[AGREE] R1-N2: Proportional effects 假设 (f=λg) 过强**

同意。补充两点：

1. f=λg 要求 A 的各类别对 Y 和对 T 的效应向量完全共线。在 NLP 场景中，这意味着例如在 sentiment analysis 中，"positive/negative/neutral" 三类对 treatment 的影响方向和相对强度必须与对 outcome 的完全成比例——这几乎不可能成立。例如 "neutral" 类别可能对 treatment assignment 有较弱影响但对 outcome 有独立的 baseline 效应。
2. 论文在 Appendix A.4（Theorem 1 证明）确实讨论了 general case，指出 general case 需要 Cauchy-Schwarz bound 且条件更复杂。但正文未明确报告 general case 的 sign preservation 失败率。R1 引用的 15-17% 失败率如果准确，这是一个重要的数字，应该在正文中讨论。

不过我要指出：即使 proportional effects 假设过强，Proposition 1 的 sign preservation 条件（不依赖 f=λg）仍然是有价值的——它们给出了各拓扑的充分条件，即使 Theorem 1 的 monotonicity 保证需要加强假设。

---

## Should-Fix

**[AGREE] R1-W1: "Primary coefficient never reverses" 认识论定位模糊**

同意，且这与我的 W5（Abstract 数字密度过高）相关。Abstract 中 "the primary coefficient does not reverse" 的措辞隐含了一种比实际更强的保证。从正文 Section 4.2（page 6）来看，这是在 "across all 23 empirical configurations" 的观察——即仅 23 个 LLM confusion matrix 配置的实证结果，而非理论保证。

R1 正确指出，对 K≥4，精心构造的 C 可能打破此规律。论文自身也承认这一点（page 4："an empirical regularity consistent with magnitude dominance in the misclassification-induced weighted sum rather than an algebraic guarantee"），但 Abstract 的措辞未能传达这一限定。

**[AGREE] R1-W2: Non-differential misclassification 在 LLM 场景中的合理性**

强烈同意——这与我的 W2 完全一致，是我们两位 reviewer 的共识问题。

R1 补充了一个我未充分展开的角度：**LLM pretraining data 包含 A-Y 统计关联**。即使 LLM 在标注时没有显式 access 到 Y，其预训练语料中的统计模式可能使其对某些 A 类别的误分类率依赖于与 Y 相关的文本特征。例如，在政治立场分类中，LLM 可能对带有强情感色彩的文本（与 outcome 相关）有更低的误分类率，从而违反 P(A*|A,X,Y,Z) = P(A*|A)。

Appendix B.5 的 stress test（Table 7）是重要的补充，但 R1 正确指出未讨论 "realistic ε range"——我们不知道真实 LLM 的 differential departure 通常是多大。如果能引用已有文献（如 Baumann et al. 2025 的分析）来估计真实 ε 范围，将大幅增强这部分的说服力。

**[PARTIALLY AGREE] R1-W3: δ* uncertainty bound 过宽**

部分同意。R1 的数学论证是正确的：如果 δ* ∈ [0.1, 0.5] 而 uncertainty < 0.6，相对不确定性确实可能 > 100%。

但需要两点补充：
1. Appendix B.7（Table 8）的 bootstrap 结果显示，对 **confounding** topology，bootstrap 95% CI 不跨越 10% 阈值，即 δ* 的实际不确定性足够小以支撑实用决策。不确定性主要集中在 IV topology（本身就被标记为 "maximally fragile"）。
2. δ* uncertainty 的绝对值与 topology 相关：对于 M-bias（ASV → ∞，immune），uncertainty 大小无关紧要；对于 confounding/collider（δ* 较大），相对不确定性可控；仅对 exposure/IV（δ* 较小）构成实际问题。

因此 R1 的担忧在最需要精确 δ* 的 topology（IV/exposure）上是完全成立的，但对其他 topology 的影响有限。建议作者分 topology 讨论 δ* precision，而非报告跨 topology 的统一 bound。

**[REBUT] R1-W4: Table 1 Collider "Amplification=100%" 与 "protective" 矛盾**

基于正文的明确描述，我倾向于认为这可能是 R1 对 Table 1 的误读，或是 Table 1 存在呈现歧义。

证据：
- Section 4.2（page 6）明确写道："Confounding, mediation, and front-door show 100% amplification (Brenner, 1993; Dosemeci et al., 1990) but never reverse the sign. **Collider misclassification is protective**"——将 Collider 与 100% amplification 的三种拓扑明确对比区分。
- Section 3.2（page 4）在 Collider 小节中写道："Conditioning on A* instead of A attenuates the spurious path, so annotation error reduces collider bias (τ_sign_flip = 0)"——attenuation 意味着 amplification = 0%。
- Table 1 的 Collider 行应显示 Amplification ≈ 0%。如果表格显示 100%，那是**排版错误**而非理论矛盾，因为推导清楚支持 0%。

建议：如果确实存在 Table 1 排版问题，作者应修正；但这不影响实质性结论。

**[AGREE] R1-W5: Conjecture 1 violation count 与 "approximately monotonic" 的张力**

同意存在表述张力。论文使用 "approximately monotonic" 描述 Conjecture 1，同时报告了具体的 violation count 和 worst-case deviation（ε < 0.06）。问题在于 "approximately" 是一个模糊限定词——读者无法从中推断出误差的量级或分布。

不过我认为这是一个 **presentation issue** 而非 substantive issue。论文在 Appendix B.11 中给出了详细的数值验证（30,000 random matrices per topology, K ∈ {3,5,7}），violation counts 和 worst-case deviations 都被明确报告（Table 10）。建议正文中用更精确的表述（如 "monotonic up to ε=0.06 deviations across all tested configurations"）替代 "approximately monotonic"。

---

## Questions

**Q1: Theorem 1 推广到 K=3 的具体障碍**

R1 提出了一个好问题。从我阅读 Appendix A.4 的理解，核心障碍是：K=2 时 confusion matrix 的 bias attenuation 可以用单个参数（对角线概率）完全刻画，使得 monotonicity 证明简化为单变量分析。K≥3 时，confusion matrix 有 K(K-1) 个自由参数，bias 是这些参数的非线性组合，不同参数的交互效应使得全局 monotonicity 的证明变成高维优化问题。这与论文中 Conjecture 1 选择 δ parameterization（沿 C₀→identity 的插值路径）来降维的策略一致——即使沿这条一维路径，不同拓扑的 monotonicity 行为也不一致（IV 不满足）。

**Q2: Primary coefficient preservation 的形式化**

合理的问题。从论文的推导来看，primary coefficient 在 confounding 下的 bias 是 plim τ̂(A*) = Σ_k w_k τ_k，其中 w_k 依赖于 confusion matrix C 和 A 的边际分布。如果 τ_k 中存在 dominant category（magnitude dominance），则 sign preservation 成立。形式化条件可能类似于 |Σ_{k: sign(w_k τ_k)=sign(τ)} w_k τ_k| > |Σ_{k: sign(w_k τ_k)≠sign(τ)} w_k τ_k|，但这依赖于 C 的具体结构，难以给出不依赖 C 的充分条件。

**Q3: C₀ 选择对 δ* 可比性的影响**

这是 ASV 框架设计中的一个实际问题。论文选择 C₀ = (1-δ)I + δC_s（从 identity 到 reference matrix 的插值），这意味着 δ=0 对应完美分类，δ=1 对应 C_s。但 C_s 的选择（论文用 column-stochastic reference matrix）会影响 δ* 的数值。跨 topology 的 δ* 可比性确实依赖于 C_s 的一致性。论文在 Section 3.3 的 parameterization 小节（page 5）定义了 C_s 但未讨论替代选择的影响。

**Q4: FWL breakdown 随 N 或 K 的 scaling**

合理的问题。论文报告 |ΔSF_τ| < 0.02（Table 5, page 8），但这是在特定 N（N=10,000）和 K=3 下的结果。如果 K 增大，logistic regression 的非线性更强（更多类别的 dummy coding），FWL 近似可能恶化。论文未讨论这一点。

---

## 对 R1 Strengths 和证明验证的评价

**S1-S5：全部同意。** 特别赞同以下两点：

- **S2（三级认识论层次）**：这在 ML/NLP 论文中极为罕见。多数论文要么只展示 proved results，要么将 numerical evidence 混同于 proof。本文明确区分 Proved（Proposition 1, Theorem 1）、Verified（Observation 1, numerical checks）、Conjectured（Conjecture 1），这种诚实和精确是值得鼓励的学术实践。

- **S5（证明验证）**：R1 逐步验证了 Proposition 1(a)(b)(c)、Theorem 1 全 6 步、Lemma 1、Mediation monotonicity、Proposition 4，均确认正确。我未进行同等细致的证明验证，对 R1 的验证结果表示认可。这增强了我对论文理论基础可靠性的信心（Soundness 4/5 的评分部分基于此）。

---

## 综合评价

**两位 Reviewer 的共识问题（应优先处理）：**
1. 非差异性误分类假设在 LLM 场景中的合理性（R1-W2 = R2-W2）
2. K≥3 理论保证不足 vs. 论文定位（R1-N1 ≈ R2-W4）
3. Abstract/正文的认识论措辞过强（R1-W1 ≈ R2-W5 部分重叠）

**R1 独有但我同意的关键问题：**
- N2: Proportional effects 假设过强——我的原始审稿未充分关注这一点，但 R1 的分析说服了我
- W3: δ* uncertainty bound 过宽（尤其对 IV/exposure topology）

**我保留的独有关注（R1 未覆盖）：**
- 我的 W1: ASV 与 E-values/partial R² 的方法论差异界定不足
- 我的 W3: 实证验证范围（3 个 NLP tasks）与理论通用性声称的差距
- Missing references: Rosenbaum (2002), Ding & VanderWeele (2016)

**维持评分：Overall 3.5（Borderline Conference），Soundness 4/5，Excitement 3/5，Confidence 4/5。**

R1 的证明验证和 N1/N2 分析加强了我对论文理论层面 strengths 和 weaknesses 的理解，但未改变我的整体评分。论文的系统性分析有价值（适合 Findings），但 ASV 的方法论增量和 K≥3 理论保证的缺失使其 borderline for main conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-23T01:39:32.397389+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-23T01:39:32.498361+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T01:26:15.036700+00:00\", \"completed_at\": \"2026-05-23T01:26:18.690492+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-23T01:42:26.422552+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W3 再次提出实证验证范围偏窄（3 NLP tasks × 4 LLMs）。R1 REBUT：161 scenarios + real LLM matrices 已充分。共识降为 divergence point。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 8\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。标记为 resolved。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 两位 Reviewer 一致复发（R1-W2, R2-W2, MAJOR 共识）。指出 LLM pretraining data 隐含 A-Y 关联、stress test 缺少 realistic ε 范围估计。R5 的修复不充分——主文仍仅在 Limitations 一句话带过。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。标记为 resolved。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出 Abstract 数字密度过高（>20 个具体数字）。R1 REBUT：分析性论文需要精确数字。分歧点。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：应聚焦 monotonicity 非平凡性作为核心方法论贡献。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R2-W1 首发 MAJOR：ASV 与 E-values/partial R² 高度同构，差异仅在参数化对象。R1 AGREE with nuance：K²→1D 降维需 Theorem 1，此步骤非平凡，但证明仅 K=2 完成。共识：定位为 'systematic application with non-trivial reduction theorem' 而非 'novel framework'。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"MINOR——添加 appendix pointer 即可。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8-R2 格式合规检查通过：Preprint 标注 ✓。本轮可能已修复。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求 Abstract 标注 'empirical regularity' + sufficient condition。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-W1 MAJOR：Abstract 仍赋予过高 prominence。R2 AGREE。论文自身已在 Section 3.2 承认 'empirical regularity...rather than an algebraic guarantee'，但 Abstract 措辞未充分反映此限定。共识：继续要求降低声称强度。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R5-N3 合并跟踪。R8 共识继续要求降低声称。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"要求 NLP 场景合理性讨论 + Appendix A.4 引用。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-N2 CRITICAL：f=λg 在 NLP 中几乎不可验证，general case 15-17% sign preservation 失败率。R2 cross-share 中 AGREE，给出 sentiment analysis 具体反例。共识升为 CRITICAL——需在正文讨论 general case 失败率并给出 NLP 场景例子。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及 scope mismatch（但 R1-N1 隐含涉及）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并跟踪。R8 共识继续要求差异化。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-N1 将此升为 CRITICAL 核心张力：Theorem 1 仅 K=2，ASV 在 K≥3 理论基础为 conjectural。R2 AGREE。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 隐含涉及（R1-W2 要求 realistic ε 范围）但未单独提出扩展 ε 要求。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"R8-R1-W4 指出 Collider Amplification=100% 与 protective 描述矛盾。R2 REBUT：可能是排版错误或误读，正文推导明确支持 Collider attenuation（Amplif.≈0%）。需确认 Table 1 数据是否正确。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名与数值验证性质不匹配\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及——论文已改为 Observation 1。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 选择的敏感性未充分分析\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-W3 MAJOR：δ* uncertainty <0.6 在 δ*∈[0.1,0.5] 时 relative uncertainty >100%。R2 PARTIALLY AGREE：IV/exposure 上成立，其他拓扑影响有限。共识：分 topology 讨论 δ* precision。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 中 83.4% sign reversal 呈现顺序有误导性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及 Section 4.2 呈现顺序。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"Introduction '154×' binarization bias 倍数来源不透明\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。论文已添加脚注说明。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Wei et al. 2025, Demirel et al. 2024）\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8-R2 确认 Demirel et al. (2024) 已引用。Wei et al. 状态待确认。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 的 risk threshold (0.1) 缺乏选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 新发现 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力——ASV 在 K≥3 理论基础为 conjectural\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N1 首发 CRITICAL，R2 cross-share AGREE。Theorem 1 仅 K=2，K≥3 依赖 Observation 1 (deviation<0.005) 和 Conjecture 1 (ε<0.06)。当 δ* 较小（如 IV topology δ*≈0.05）时，ε=0.06 的 monotonicity 偏差可完全淹没 ASV 信号。共识升级自 R6-W4。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 显式讨论 K≥3 下 ASV 的理论地位和 ε-approximate monotonicity 对 δ* precision 的定量影响\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N2 首发 CRITICAL，R2 cross-share AGREE 并给出 sentiment analysis 反例。升级自 R6-M3。共识：正文需报告 general case 失败率 + NLP 场景合理性讨论。\"\n    action_items:\n      - round: 8\n        action: \"method.tex Theorem 1 后报告 general case 统计 + NLP 成立/不成立例子\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV 与 E-values/partial R² 的方法论差异界定不足——contribution 定位需调整\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R2-W1 首发 MAJOR，R1 AGREE with nuance：K²→1D 降维非平凡（需 Theorem 1），但此证明仅 K=2。共识：定位为 'systematic application with non-trivial reduction theorem'。升级自 R4-W6/R6-W2。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 调整 ASV novelty 定位 + 明确列出结构性差异\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"两位 Reviewer 独立提出（R1-W2, R2-W2）且 cross-share 互相 AGREE。LLM pretraining data 隐含 A-Y 关联，即使无显式 Y access 也可产生 differential misclassification。Stress test (Table 7) 存在但主文引导不足，realistic ε 范围未讨论。升级自 NEW-1。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.1 或 Method 结尾增加段落：何时非差异性合理、违反时 bias 如何变化、引导 Appendix B.5\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽，对 IV/exposure 拓扑 relative uncertainty >100%\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-W3 首发 MAJOR，R2 PARTIALLY AGREE：IV/exposure 上成立，confounding/collider 上可控。升级自 R7-SF5。共识：分 topology 讨论 δ* precision，推荐 Bootstrap CI。\"\n    action_items:\n      - round: 8\n        action: \"Section 4.3 分 topology 讨论 δ* precision + 推荐 Bootstrap CI\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Rosenbaum (2002) 和 Ding & VanderWeele (2016)\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"R2 提出，R1 cross-share AGREE Ding & VanderWeele (2016) 应引用（E-value 理论源头）。Rosenbaum (2002) 合理但非必需。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele (2016)，考虑引用 Rosenbaum (2002)\"\n        assigned_to: agent\n        status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W3 再次提出实证验证范围偏窄（3 NLP tasks × 4 LLMs）。R1 REBUT：161 scenarios + real LLM matrices 已充分。共识降为 divergence point。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 8\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。标记为 resolved。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 两位 Reviewer 一致复发（R1-W2, R2-W2, MAJOR 共识）。指出 LLM pretraining data 隐含 A-Y 关联、stress test 缺少 realistic ε 范围估计。R5 的修复不充分——主文仍仅在 Limitations 一句话带过。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 8\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。标记为 resolved。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出 Abstract 数字密度过高（>20 个具体数字）。R1 REBUT：分析性论文需要精确数字。分歧点。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：应聚焦 monotonicity 非平凡性作为核心方法论贡献。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R2-W1 首发 MAJOR：ASV 与 E-values/partial R² 高度同构，差异仅在参数化对象。R1 AGREE with nuance：K²→1D 降维需 Theorem 1，此步骤非平凡，但证明仅 K=2 完成。共识：定位为 'systematic application with non-trivial reduction theorem' 而非 'novel framework'。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"MINOR——添加 appendix pointer 即可。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8-R2 格式合规检查通过：Preprint 标注 ✓。本轮可能已修复。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求 Abstract 标注 'empirical regularity' + sufficient condition。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-W1 MAJOR：Abstract 仍赋予过高 prominence。R2 AGREE。论文自身已在 Section 3.2 承认 'empirical regularity...rather than an algebraic guarantee'，但 Abstract 措辞未充分反映此限定。共识：继续要求降低声称强度。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R5-N3 合并跟踪。R8 共识继续要求降低声称。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"要求 NLP 场景合理性讨论 + Appendix A.4 引用。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-N2 CRITICAL：f=λg 在 NLP 中几乎不可验证，general case 15-17% sign preservation 失败率。R2 cross-share 中 AGREE，给出 sentiment analysis 具体反例。共识升为 CRITICAL——需在正文讨论 general case 失败率并给出 NLP 场景例子。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及 scope mismatch（但 R1-N1 隐含涉及）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并跟踪。R8 共识继续要求差异化。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-N1 将此升为 CRITICAL 核心张力：Theorem 1 仅 K=2，ASV 在 K≥3 理论基础为 conjectural。R2 AGREE。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 隐含涉及（R1-W2 要求 realistic ε 范围）但未单独提出扩展 ε 要求。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"R8-R1-W4 指出 Collider Amplification=100% 与 protective 描述矛盾。R2 REBUT：可能是排版错误或误读，正文推导明确支持 Collider attenuation（Amplif.≈0%）。需确认 Table 1 数据是否正确。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名与数值验证性质不匹配\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及——论文已改为 Observation 1。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 选择的敏感性未充分分析\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8-R1-W3 MAJOR：δ* uncertainty <0.6 在 δ*∈[0.1,0.5] 时 relative uncertainty >100%。R2 PARTIALLY AGREE：IV/exposure 上成立，其他拓扑影响有限。共识：分 topology 讨论 δ* precision。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 中 83.4% sign reversal 呈现顺序有误导性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及 Section 4.2 呈现顺序。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"Introduction '154×' binarization bias 倍数来源不透明\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。论文已添加脚注说明。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Wei et al. 2025, Demirel et al. 2024）\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8-R2 确认 Demirel et al. (2024) 已引用。Wei et al. 状态待确认。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 的 risk threshold (0.1) 缺乏选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 新发现 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力——ASV 在 K≥3 理论基础为 conjectural\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N1 首发 CRITICAL，R2 cross-share AGREE。Theorem 1 仅 K=2，K≥3 依赖 Observation 1 (deviation<0.005) 和 Conjecture 1 (ε<0.06)。当 δ* 较小（如 IV topology δ*≈0.05）时，ε=0.06 的 monotonicity 偏差可完全淹没 ASV 信号。共识升级自 R6-W4。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 显式讨论 K≥3 下 ASV 的理论地位和 ε-approximate monotonicity 对 δ* precision 的定量影响\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N2 首发 CRITICAL，R2 cross-share AGREE 并给出 sentiment analysis 反例。升级自 R6-M3。共识：正文需报告 general case 失败率 + NLP 场景合理性讨论。\"\n    action_items:\n      - round: 8\n        action: \"method.tex Theorem 1 后报告 general case 统计 + NLP 成立/不成立例子\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV 与 E-values/partial R² 的方法论差异界定不足——contribution 定位需调整\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R2-W1 首发 MAJOR，R1 AGREE with nuance：K²→1D 降维非平凡（需 Theorem 1），但此证明仅 K=2。共识：定位为 'systematic application with non-trivial reduction theorem'。升级自 R4-W6/R6-W2。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 调整 ASV novelty 定位 + 明确列出结构性差异\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"两位 Reviewer 独立提出（R1-W2, R2-W2）且 cross-share 互相 AGREE。LLM pretraining data 隐含 A-Y 关联，即使无显式 Y access 也可产生 differential misclassification。Stress test (Table 7) 存在但主文引导不足，realistic ε 范围未讨论。升级自 NEW-1。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.1 或 Method 结尾增加段落：何时非差异性合理、违反时 bias 如何变化、引导 Appendix B.5\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽，对 IV/exposure 拓扑 relative uncertainty >100%\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-W3 首发 MAJOR，R2 PARTIALLY AGREE：IV/exposure 上成立，confounding/collider 上可控。升级自 R7-SF5。共识：分 topology 讨论 δ* precision，推荐 Bootstrap CI。\"\n    action_items:\n      - round: 8\n        action: \"Section 4.3 分 topology 讨论 δ* precision + 推荐 Bootstrap CI\"\n        assigned_to: agent\n        status: open\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Rosenbaum (2002) 和 Ding & VanderWeele (2016)\"\n    status: open\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"R2 提出，R1 cross-share AGREE Ding & VanderWeele (2016) 应引用（E-value 理论源头）。Rosenbaum (2002) 合理但非必需。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele (2016)，考虑引用 Rosenbaum (2002)\"\n        assigned_to: agent\n        status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-23T01:42:26.525524+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 20110}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-23T01:44:51.195510+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 Long Paper (ARR)\n**Reviewers**: R1（方法严谨性）, R2（新颖性/完整性）\n**审稿模式**: Fresh（无前轮记忆）\n\n---\n\n## Summary\n\n本文系统刻画了 K≥3 多分类标注误差在七种典型因果 DAG 拓扑下的传播机制。在线性 SEM 下推导了各拓扑的偏差表达式，证明了 confounding 和 collider 的 sign preservation（Proposition 1），引入 Annotation Sensitivity Values（ASV）框架并证明了 K=2 下的 envelope monotonicity（Theorem 1），报告了 FWL 不变性这一负面结果（matrix-based correction 对四种拓扑完全无效）。论文诚实地建立了 Proved/Verified/Conjectured 三级认识论层次。所有声称 proved 的结果经 R1 逐步验证均正确。\n\n---\n\n## Strengths\n\n**S1. 系统性跨拓扑分析——填补真实空白。** [R1-S1, R2-S1, 共识] 此前工作限于 binary treatment（Brenner 1993; Teblunthuis 2024）或单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下比较 7 种 DAG 拓扑 × K≥3 类别的 bias 行为，揭示同一 confusion matrix 在不同因果结构中产生定性不同偏差。经两位 Reviewer 独立核查相关文献，\"首次跨拓扑系统比较\"的声称基本成立。\n\n**S2. K=2→K≥3 的 structural transition 是真正的理论贡献。** [R1-S1, R2-S2, 共识] Binary case 的 \"toward-null\" 保证在 K≥3 下结构性失效（exposure 83.4% sign reversal, IV 52.6%）。Binarization collapse 发现（跨拓扑 bias 差异达 154×）对 NLP 实践有直接指导意义。\n\n**S3. 三级认识论层次在 ML/NLP 论文中罕见且值得推广。** [R1-S2, R2 cross-share 特别赞同] 明确区分 Proved（Proposition 1, Theorem 1）、Verified（Observation 1, numerical checks）、Conjectured（Conjecture 1），这种诚实和精确是优秀的学术实践。\n\n**S4. FWL 不变性是优雅且实用的负面结果。** [R1-S3, R2-S4, 共识] 对于 A 作为协变量的四种拓扑，任何线性变换（包括 C⁻¹ 校正）无法改变 treatment coefficient。贡献在于：(1) 识别所有主流 correction 方法均落入此类；(2) 转化为实用路由规则（Algorithm 1 Step 3）。\n\n**S5. 实验验证广度令人印象深刻。** [R1-S4, R2-S3, 共识] 7 topologies × 23 LLM configs × cross-K(3,5,7) × logistic DGP robustness × 100,000 Dirichlet matrices。理论-实验双重验证（MAPE 1.6% across 161 scenarios）增强可信度。所有 proved 证明经 R1 逐步验证均正确。\n\n**S6. 相关工作覆盖优秀，实用产出有价值。** [R2-S5, R2-S6] 跨流行病学、NLP、因果推断三个子领域的引用覆盖充分。Algorithm 1 提供可操作的 topology→correction 映射流程。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力。** [R1-N1 + R2-W4, 共识 CRITICAL]\n- Theorem 1（envelope monotonicity）仅对 K=2 + proportional effects (f=λg) + (C₀)ⱼⱼ ≥ 1/2 成立。论文核心创新是 K≥3 场景，但 K≥3 依赖 Observation 1（worst-case deviation < 0.005）和 Conjecture 1（ε < 0.06），无形式化保证。\n- ASV 框架的 well-definedness 隐含依赖 monotonicity——若局部违反，min{δ: |bias|>threshold} 可能不唯一，δ* 定义有歧义。当 δ* 较小时（如 IV topology δ*≈0.05），ε=0.06 的 monotonicity 偏差可完全淹没 ASV 信号。\n- 建议：(1) Section 3.3 显式讨论 K≥3 下 ASV 的理论地位；(2) 定量分析 ε-approximate monotonicity 对 δ* precision 的影响；(3) 明确 ASV 对 IV 拓扑本质不可靠。\n\n**C2. Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率。** [R1-N2, R2 cross-share AGREE, 共识 CRITICAL]\n- f=λg 要求 A 的各类别对 Y 和 T 的效应完全共线——在 NLP 因果推断中几乎不成立。例如 sentiment analysis 中 \"neutral\" 类别可能对 treatment 影响弱但对 outcome 有独立 baseline 效应。\n- General case 下 Proposition 4 显示 λ(C) 有 15-17% 概率超出 [0,1]，sign preservation 可失败，但正文未报告此统计。\n- 建议：(1) 正文报告 general case 失败率；(2) 给出 NLP 中 f=λg 成立/不成立的具体例子；(3) 考虑弱化条件或讨论 robustness。\n\n### Major\n\n**M1. Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足。** [R1-W2 + R2-W2, 强共识]\n- LLM pretraining data 包含 A-Y 统计关联，即使无显式 Y access 也可产生 differential misclassification（如政治立场分类中，强情感文本与 outcome 相关，LLM 对其误分类率更低）。\n- Appendix B.5 stress test（Table 7）显示 ε≥0.10 时 sign-flip rate 显著上升，但主文仅在 Limitations 一句话带过，未讨论 realistic ε 范围，也未提供估计 ε 的方法。\n- 建议：Section 3.1 增加段落讨论何时非差异性合理、违反时 bias 如何定性改变、引导 Appendix B.5。\n\n**M2. \"Primary coefficient never reverses\" 认识论定位模糊。** [R1-W1, R2 cross-share AGREE]\n- 纯经验观察（23 LLM configs + 100K matrices）被 Abstract 赋予过高 prominence。论文自身在 Section 3.2 承认 \"empirical regularity...rather than an algebraic guarantee\"，但 Abstract 措辞未充分反映此限定。\n- 对 K≥4，精心构造的 C 可能打破此规律。\n- 建议：降低 Abstract 表述强度，讨论反例可能性或 magnitude dominance 的形式化条件。\n\n**M3. ASV 框架与 E-values/partial R² 的方法论差异界定不足。** [R2-W1, R1 AGREE with nuance]\n- ASV 三个子指标在结构上与 E-values 高度同构，差异主要在参数化对象而非方法论。K²→1D 降维需要 Theorem 1（非平凡步骤），但此证明仅 K=2 完成。\n- 共识定位：应为 \"systematic application with non-trivial reduction theorem\" 而非 \"novel framework\"。\n- 建议：明确列出 ASV 相对于 E-value/partial R² 的结构性差异，或调整 novelty 声称力度。\n\n**M4. δ* uncertainty bound 过宽（IV/exposure 拓扑）。** [R1-W3, R2 PARTIALLY AGREE]\n- δ* uncertainty < 0.6 在 δ* ∈ [0.1, 0.5] 时 relative uncertainty > 100%。IV topology bootstrap 95% CI [0.44, 1.29] 跨越 δ=1。\n- R2 补充：uncertainty 问题主要集中在 IV/exposure（δ* 较小），confounding/M-bias 上可控。\n- 共识：分 topology 讨论 δ* precision，推荐 Bootstrap CI，避免跨 topology 统一 bound。\n\n### Minor\n\n**m1. Table 1 Collider \"Amplification\" 数据可能存在排版错误。** [R1-W4, R2 REBUT 认为正文推导支持 Collider attenuation]\n- Section 3.2 和 4.2 明确将 Collider 标记为 \"protective\"（attenuation），但 R1 报告 Table 1 Amplification=100%。如确为排版错误，需修正。\n\n**m2. Conjecture 1 \"approximately monotonic\" 表述模糊。** [R1-W5, R2 AGREE]\n- 建议用精确表述替代（如 \"monotonic up to ε=0.06 deviations across all tested configurations\"）。\n\n**m3. Figure 2 色盲可及性。** [R2-W7]\n- Sign reversal 仅用红色标记，未考虑色觉障碍读者。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识（均 [AGREE]）：\n\n1. **Non-differential misclassification 假设讨论不足** — 核心框架假设的 LLM 场景适用性需在主文正面讨论（非仅 Limitations 一句话）\n2. **K≥3 理论保证不足** — Theorem 1 仅 K=2，ASV 在 K≥3 理论基础为 conjectural，需显式承认并讨论影响\n3. **Proportional effects 假设过强** — 正文需报告 general case 失败率，给出 NLP 场景例子\n4. **Primary coefficient claim 定位过高** — Abstract 应降低表述强度\n5. **所有 proved claims 正确** — R1 逐步验证 Proposition 1(a)(b)(c)、Theorem 1 全 6 步、Lemma 1 均正确\n6. **三级认识论层次是优秀实践** — 在 ML/NLP 论文中罕见\n7. **FWL 不变性有实用价值** — 对 NLP 校正实践有直接指导意义\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 权衡 |\n|------|---------|---------|------|\n| 实证验证范围 | REBUT：161 scenarios + real LLM matrices 已充分 | MAJOR：仅 3 NLP tasks 偏窄，Dirichlet 先验与真实 error structure 有差异 | R1 的 REBUT 有力——论文确实有 cross-K、logistic DGP、real matrices 验证。但 R2 关于 structured confusion matrix 的建议有价值。降为 MINOR 建议。 |\n| Abstract 数字密度 | REBUT：分析性论文需要精确数字 | MINOR：>20 个数字过多 | 风格偏好分歧，不影响实质质量。 |\n| FWL novelty | REBUT：novelty 在识别和应用，非证明技巧 | MINOR：对熟悉 FWL 读者是直接推论 | R1 的分析更有说服力——贡献在于将代数事实转化为 correction method routing。 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. Theorem 1 推广到 K=3 的具体数学障碍是什么？K=2 的代数结构在哪一步不可推广？\n2. Primary coefficient preservation 能否形式化为 magnitude dominance 条件（如 Gershgorin-type bound）？\n3. ASV 能否提供 E-values 无法给出的可操作指导？请给出具体决策示例。\n4. C₀ 的选择如何影响跨 topology 的 δ* 可比性？\n5. FWL invariance 在更强非线性模型（如高维交互项）下 breakdown 幅度是否随 N 或 K scaling？\n6. 真实 LLM 的 differential misclassification departure ε 通常是多大？能否引用现有文献估计？\n\n---\n\n## Missing References\n\n- **Ding & VanderWeele (2016)** \"Sensitivity analysis without assumptions on unmeasured confounding\" — E-value 的前驱理论工作，与 ASV 方法论对比直接相关。[R2 提出, R1 AGREE]\n- **Rosenbaum (2002)** \"Observational Studies\" — sensitivity analysis 领域经典奠基。[R2 提出, R1 认为合理但非必需]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：错误。** 视觉审查 Agent 因 API 限额耗尽退出（\"You've hit your limit · resets 4pm (UTC)\"）。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 4/5 | **4/5** |\n| Excitement | 3.5/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**一句话总结**：理论框架严谨（所有 proved claims 正确）、系统性好（7 topologies × K≥3 是真正的空白填补）、认识论诚实（三级层次罕见），但存在两个结构性问题——(1) Theorem 1 的 K=2 scope 与论文 K≥3 定位之间的落差使 ASV 在最关键的 regime 缺乏理论保证，(2) proportional effects 和 non-differential misclassification 两个核心假设在 NLP 场景中的合理性讨论严重不足。ASV 的方法论增量有限（sensitivity analysis 标准模板的新参数化），实质创新集中在 bias taxonomy 和 FWL 不变性。\n\n**Findings 推荐**：论文填补了多类标注误差 × 因果推断交叉领域的系统性空白，bias taxonomy 和 FWL 不变性对 NLP 实践者有切实价值。如果作者能在 camera-ready 中充分讨论两个核心假设的适用性（non-differential + proportional effects），并在 ASV 的 K≥3 理论地位上做出诚实标注，本文具备 Findings 接收的水平。Main conference 需要更强的方法论创新或更充分的 K≥3 形式化保证。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"the primary coefficient does not reverse...an empirical regularity consistent with magnitude dominance rather than an algebraic guarantee\" — 措辞已部分改善，但 Abstract 仍将此作为核心卖点之一。建议进一步降低 prominence 或添加 \"in all tested configurations\" 限定。\n- 数字密度高（>15 个具体数字），两位 Reviewer 意见分歧。建议保留最关键的 5-7 个。\n\n### Section 3.1 (Setup)\n- Definition 1（非差异性误分类）定义清晰。但需在此处或 Method 结尾增加讨论：何时假设在 LLM 场景中合理、违反时 bias 如何定性改变。当前仅 Limitations 一句话，不足以应对审稿人质疑。\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 的三部分条件和证明均正确（R1 逐步验证）。\n- Numerical Verification 2（primary coefficient preservation）定位需改善——当前 \"Numerical Verification\" 标签合适，但 Abstract 引用时应保持同等谨慎。\n- Collider/M-bias/front-door 小节过于简略。建议添加一句指向 Appendix 完整推导的声明。\n\n### Section 3.3 (ASV)\n- Theorem 1 证明完整正确（K=2 confounding + proportional effects，R1 验证全 6 步）。\n- K≥3 的 ASV 理论基础为 conjectural——需显式标注此限制及对 δ* precision 的影响。\n- ASV 与 E-value 的差异化论述需加强：(1) K²→1D 降维非平凡性；(2) topology-dependent threshold behavior；(3) 三类指标的分层语义。或者降低 \"framework\" 声称的力度。\n- Conjecture 1 措辞建议改为 \"monotonic up to ε=0.06 deviations\" 替代模糊的 \"approximately monotonic\"。\n\n### Section 4 (Experiments)\n- Theory-MC agreement (MAPE 1.6%) 令人信服。\n- Table 1：确认 Collider 行的 Amplification 数值是否正确（正文推导支持 attenuation，但 R1 报告 Table 显示 100%）。Caption 需明确 \"Violation\" 和 \"Amplification\" 的精确定义。\n- Section 4.3 ASV validation：分 topology 讨论 δ* precision，IV/exposure 上 uncertainty 过大需显式承认。\n- Section 4.4 FWL：建议增加一句说明此结果在 measurement error 文献中的 novelty 状态。\n\n### Conclusion & Limitations\n- Limitations 覆盖面合理但需深化 non-differential 假设讨论。\n- 代码公开承诺合理。\n\n### Appendix\n- 证明完整、可独立验证（R1 确认）。\n- B.5 Non-Differential Stress Test 是关键补充，应在主文增加引导。\n- Algorithm 1 有实用价值。\n\n---\n\n## Issue Tracker 同步\n\n已更新 `review_issues.yaml`。本轮新增/升级 issues：\n- R8-C1 [CRITICAL]: Theorem 1 scope vs K≥3 定位（升级自 R6-W4）\n- R8-C2 [CRITICAL]: Proportional effects 假设过强（升级自 R6-M3）\n- R8-W1 [MAJOR]: ASV vs E-value novelty 差异不足（升级自 R4-W6/R6-W2）\n- R8-W2 [MAJOR]: Non-differential 假设讨论不足（复发自 NEW-1）\n- R8-W3 [MAJOR]: δ* uncertainty 过宽（升级自 R7-SF5）\n- R8-MR1 [MINOR]: 缺失 Ding & VanderWeele (2016)\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 Long Paper (ARR)\n**Reviewers**: R1（方法严谨性）, R2（新颖性/完整性）\n**审稿模式**: Fresh（无前轮记忆）\n\n---\n\n## Summary\n\n本文系统刻画了 K≥3 多分类标注误差在七种典型因果 DAG 拓扑下的传播机制。在线性 SEM 下推导了各拓扑的偏差表达式，证明了 confounding 和 collider 的 sign preservation（Proposition 1），引入 Annotation Sensitivity Values（ASV）框架并证明了 K=2 下的 envelope monotonicity（Theorem 1），报告了 FWL 不变性这一负面结果（matrix-based correction 对四种拓扑完全无效）。论文诚实地建立了 Proved/Verified/Conjectured 三级认识论层次。所有声称 proved 的结果经 R1 逐步验证均正确。\n\n---\n\n## Strengths\n\n**S1. 系统性跨拓扑分析——填补真实空白。** [R1-S1, R2-S1, 共识] 此前工作限于 binary treatment（Brenner 1993; Teblunthuis 2024）或单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下比较 7 种 DAG 拓扑 × K≥3 类别的 bias 行为，揭示同一 confusion matrix 在不同因果结构中产生定性不同偏差。经两位 Reviewer 独立核查相关文献，\"首次跨拓扑系统比较\"的声称基本成立。\n\n**S2. K=2→K≥3 的 structural transition 是真正的理论贡献。** [R1-S1, R2-S2, 共识] Binary case 的 \"toward-null\" 保证在 K≥3 下结构性失效（exposure 83.4% sign reversal, IV 52.6%）。Binarization collapse 发现（跨拓扑 bias 差异达 154×）对 NLP 实践有直接指导意义。\n\n**S3. 三级认识论层次在 ML/NLP 论文中罕见且值得推广。** [R1-S2, R2 cross-share 特别赞同] 明确区分 Proved（Proposition 1, Theorem 1）、Verified（Observation 1, numerical checks）、Conjectured（Conjecture 1），这种诚实和精确是优秀的学术实践。\n\n**S4. FWL 不变性是优雅且实用的负面结果。** [R1-S3, R2-S4, 共识] 对于 A 作为协变量的四种拓扑，任何线性变换（包括 C⁻¹ 校正）无法改变 treatment coefficient。贡献在于：(1) 识别所有主流 correction 方法均落入此类；(2) 转化为实用路由规则（Algorithm 1 Step 3）。\n\n**S5. 实验验证广度令人印象深刻。** [R1-S4, R2-S3, 共识] 7 topologies × 23 LLM configs × cross-K(3,5,7) × logistic DGP robustness × 100,000 Dirichlet matrices。理论-实验双重验证（MAPE 1.6% across 161 scenarios）增强可信度。所有 proved 证明经 R1 逐步验证均正确。\n\n**S6. 相关工作覆盖优秀，实用产出有价值。** [R2-S5, R2-S6] 跨流行病学、NLP、因果推断三个子领域的引用覆盖充分。Algorithm 1 提供可操作的 topology→correction 映射流程。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**C1. Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力。** [R1-N1 + R2-W4, 共识 CRITICAL]\n- Theorem 1（envelope monotonicity）仅对 K=2 + proportional effects (f=λg) + (C₀)ⱼⱼ ≥ 1/2 成立。论文核心创新是 K≥3 场景，但 K≥3 依赖 Observation 1（worst-case deviation < 0.005）和 Conjecture 1（ε < 0.06），无形式化保证。\n- ASV 框架的 well-definedness 隐含依赖 monotonicity——若局部违反，min{δ: |bias|>threshold} 可能不唯一，δ* 定义有歧义。当 δ* 较小时（如 IV topology δ*≈0.05），ε=0.06 的 monotonicity 偏差可完全淹没 ASV 信号。\n- 建议：(1) Section 3.3 显式讨论 K≥3 下 ASV 的理论地位；(2) 定量分析 ε-approximate monotonicity 对 δ* precision 的影响；(3) 明确 ASV 对 IV 拓扑本质不可靠。\n\n**C2. Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率。** [R1-N2, R2 cross-share AGREE, 共识 CRITICAL]\n- f=λg 要求 A 的各类别对 Y 和 T 的效应完全共线——在 NLP 因果推断中几乎不成立。例如 sentiment analysis 中 \"neutral\" 类别可能对 treatment 影响弱但对 outcome 有独立 baseline 效应。\n- General case 下 Proposition 4 显示 λ(C) 有 15-17% 概率超出 [0,1]，sign preservation 可失败，但正文未报告此统计。\n- 建议：(1) 正文报告 general case 失败率；(2) 给出 NLP 中 f=λg 成立/不成立的具体例子；(3) 考虑弱化条件或讨论 robustness。\n\n### Major\n\n**M1. Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足。** [R1-W2 + R2-W2, 强共识]\n- LLM pretraining data 包含 A-Y 统计关联，即使无显式 Y access 也可产生 differential misclassification（如政治立场分类中，强情感文本与 outcome 相关，LLM 对其误分类率更低）。\n- Appendix B.5 stress test（Table 7）显示 ε≥0.10 时 sign-flip rate 显著上升，但主文仅在 Limitations 一句话带过，未讨论 realistic ε 范围，也未提供估计 ε 的方法。\n- 建议：Section 3.1 增加段落讨论何时非差异性合理、违反时 bias 如何定性改变、引导 Appendix B.5。\n\n**M2. \"Primary coefficient never reverses\" 认识论定位模糊。** [R1-W1, R2 cross-share AGREE]\n- 纯经验观察（23 LLM configs + 100K matrices）被 Abstract 赋予过高 prominence。论文自身在 Section 3.2 承认 \"empirical regularity...rather than an algebraic guarantee\"，但 Abstract 措辞未充分反映此限定。\n- 对 K≥4，精心构造的 C 可能打破此规律。\n- 建议：降低 Abstract 表述强度，讨论反例可能性或 magnitude dominance 的形式化条件。\n\n**M3. ASV 框架与 E-values/partial R² 的方法论差异界定不足。** [R2-W1, R1 AGREE with nuance]\n- ASV 三个子指标在结构上与 E-values 高度同构，差异主要在参数化对象而非方法论。K²→1D 降维需要 Theorem 1（非平凡步骤），但此证明仅 K=2 完成。\n- 共识定位：应为 \"systematic application with non-trivial reduction theorem\" 而非 \"novel framework\"。\n- 建议：明确列出 ASV 相对于 E-value/partial R² 的结构性差异，或调整 novelty 声称力度。\n\n**M4. δ* uncertainty bound 过宽（IV/exposure 拓扑）。** [R1-W3, R2 PARTIALLY AGREE]\n- δ* uncertainty < 0.6 在 δ* ∈ [0.1, 0.5] 时 relative uncertainty > 100%。IV topology bootstrap 95% CI [0.44, 1.29] 跨越 δ=1。\n- R2 补充：uncertainty 问题主要集中在 IV/exposure（δ* 较小），confounding/M-bias 上可控。\n- 共识：分 topology 讨论 δ* precision，推荐 Bootstrap CI，避免跨 topology 统一 bound。\n\n### Minor\n\n**m1. Table 1 Collider \"Amplification\" 数据可能存在排版错误。** [R1-W4, R2 REBUT 认为正文推导支持 Collider attenuation]\n- Section 3.2 和 4.2 明确将 Collider 标记为 \"protective\"（attenuation），但 R1 报告 Table 1 Amplification=100%。如确为排版错误，需修正。\n\n**m2. Conjecture 1 \"approximately monotonic\" 表述模糊。** [R1-W5, R2 AGREE]\n- 建议用精确表述替代（如 \"monotonic up to ε=0.06 deviations across all tested configurations\"）。\n\n**m3. Figure 2 色盲可及性。** [R2-W7]\n- Sign reversal 仅用红色标记，未考虑色觉障碍读者。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上达成完全共识（均 [AGREE]）：\n\n1. **Non-differential misclassification 假设讨论不足** — 核心框架假设的 LLM 场景适用性需在主文正面讨论（非仅 Limitations 一句话）\n2. **K≥3 理论保证不足** — Theorem 1 仅 K=2，ASV 在 K≥3 理论基础为 conjectural，需显式承认并讨论影响\n3. **Proportional effects 假设过强** — 正文需报告 general case 失败率，给出 NLP 场景例子\n4. **Primary coefficient claim 定位过高** — Abstract 应降低表述强度\n5. **所有 proved claims 正确** — R1 逐步验证 Proposition 1(a)(b)(c)、Theorem 1 全 6 步、Lemma 1 均正确\n6. **三级认识论层次是优秀实践** — 在 ML/NLP 论文中罕见\n7. **FWL 不变性有实用价值** — 对 NLP 校正实践有直接指导意义\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 权衡 |\n|------|---------|---------|------|\n| 实证验证范围 | REBUT：161 scenarios + real LLM matrices 已充分 | MAJOR：仅 3 NLP tasks 偏窄，Dirichlet 先验与真实 error structure 有差异 | R1 的 REBUT 有力——论文确实有 cross-K、logistic DGP、real matrices 验证。但 R2 关于 structured confusion matrix 的建议有价值。降为 MINOR 建议。 |\n| Abstract 数字密度 | REBUT：分析性论文需要精确数字 | MINOR：>20 个数字过多 | 风格偏好分歧，不影响实质质量。 |\n| FWL novelty | REBUT：novelty 在识别和应用，非证明技巧 | MINOR：对熟悉 FWL 读者是直接推论 | R1 的分析更有说服力——贡献在于将代数事实转化为 correction method routing。 |\n\n---\n\n## Questions（需要作者澄清）\n\n1. Theorem 1 推广到 K=3 的具体数学障碍是什么？K=2 的代数结构在哪一步不可推广？\n2. Primary coefficient preservation 能否形式化为 magnitude dominance 条件（如 Gershgorin-type bound）？\n3. ASV 能否提供 E-values 无法给出的可操作指导？请给出具体决策示例。\n4. C₀ 的选择如何影响跨 topology 的 δ* 可比性？\n5. FWL invariance 在更强非线性模型（如高维交互项）下 breakdown 幅度是否随 N 或 K scaling？\n6. 真实 LLM 的 differential misclassification departure ε 通常是多大？能否引用现有文献估计？\n\n---\n\n## Missing References\n\n- **Ding & VanderWeele (2016)** \"Sensitivity analysis without assumptions on unmeasured confounding\" — E-value 的前驱理论工作，与 ASV 方法论对比直接相关。[R2 提出, R1 AGREE]\n- **Rosenbaum (2002)** \"Observational Studies\" — sensitivity analysis 领域经典奠基。[R2 提出, R1 认为合理但非必需]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目配置未启用外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：错误。** 视觉审查 Agent 因 API 限额耗尽退出（\"You've hit your limit · resets 4pm (UTC)\"）。用户可在限额重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 4/5 | 4/5 | **4/5** |\n| Excitement | 3.5/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**一句话总结**：理论框架严谨（所有 proved claims 正确）、系统性好（7 topologies × K≥3 是真正的空白填补）、认识论诚实（三级层次罕见），但存在两个结构性问题——(1) Theorem 1 的 K=2 scope 与论文 K≥3 定位之间的落差使 ASV 在最关键的 regime 缺乏理论保证，(2) proportional effects 和 non-differential misclassification 两个核心假设在 NLP 场景中的合理性讨论严重不足。ASV 的方法论增量有限（sensitivity analysis 标准模板的新参数化），实质创新集中在 bias taxonomy 和 FWL 不变性。\n\n**Findings 推荐**：论文填补了多类标注误差 × 因果推断交叉领域的系统性空白，bias taxonomy 和 FWL 不变性对 NLP 实践者有切实价值。如果作者能在 camera-ready 中充分讨论两个核心假设的适用性（non-differential + proportional effects），并在 ASV 的 K≥3 理论地位上做出诚实标注，本文具备 Findings 接收的水平。Main conference 需要更强的方法论创新或更充分的 K≥3 形式化保证。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"the primary coefficient does not reverse...an empirical regularity consistent with magnitude dominance rather than an algebraic guarantee\" — 措辞已部分改善，但 Abstract 仍将此作为核心卖点之一。建议进一步降低 prominence 或添加 \"in all tested configurations\" 限定。\n- 数字密度高（>15 个具体数字），两位 Reviewer 意见分歧。建议保留最关键的 5-7 个。\n\n### Section 3.1 (Setup)\n- Definition 1（非差异性误分类）定义清晰。但需在此处或 Method 结尾增加讨论：何时假设在 LLM 场景中合理、违反时 bias 如何定性改变。当前仅 Limitations 一句话，不足以应对审稿人质疑。\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 的三部分条件和证明均正确（R1 逐步验证）。\n- Numerical Verification 2（primary coefficient preservation）定位需改善——当前 \"Numerical Verification\" 标签合适，但 Abstract 引用时应保持同等谨慎。\n- Collider/M-bias/front-door 小节过于简略。建议添加一句指向 Appendix 完整推导的声明。\n\n### Section 3.3 (ASV)\n- Theorem 1 证明完整正确（K=2 confounding + proportional effects，R1 验证全 6 步）。\n- K≥3 的 ASV 理论基础为 conjectural——需显式标注此限制及对 δ* precision 的影响。\n- ASV 与 E-value 的差异化论述需加强：(1) K²→1D 降维非平凡性；(2) topology-dependent threshold behavior；(3) 三类指标的分层语义。或者降低 \"framework\" 声称的力度。\n- Conjecture 1 措辞建议改为 \"monotonic up to ε=0.06 deviations\" 替代模糊的 \"approximately monotonic\"。\n\n### Section 4 (Experiments)\n- Theory-MC agreement (MAPE 1.6%) 令人信服。\n- Table 1：确认 Collider 行的 Amplification 数值是否正确（正文推导支持 attenuation，但 R1 报告 Table 显示 100%）。Caption 需明确 \"Violation\" 和 \"Amplification\" 的精确定义。\n- Section 4.3 ASV validation：分 topology 讨论 δ* precision，IV/exposure 上 uncertainty 过大需显式承认。\n- Section 4.4 FWL：建议增加一句说明此结果在 measurement error 文献中的 novelty 状态。\n\n### Conclusion & Limitations\n- Limitations 覆盖面合理但需深化 non-differential 假设讨论。\n- 代码公开承诺合理。\n\n### Appendix\n- 证明完整、可独立验证（R1 确认）。\n- B.5 Non-Differential Stress Test 是关键补充，应在主文增加引导。\n- Algorithm 1 有实用价值。\n\n---\n\n## Issue Tracker 同步\n\n已更新 `review_issues.yaml`。本轮新增/升级 issues：\n- R8-C1 [CRITICAL]: Theorem 1 scope vs K≥3 定位（升级自 R6-W4）\n- R8-C2 [CRITICAL]: Proportional effects 假设过强（升级自 R6-M3）\n- R8-W1 [MAJOR]: ASV vs E-value novelty 差异不足（升级自 R4-W6/R6-W2）\n- R8-W2 [MAJOR]: Non-differential 假设讨论不足（复发自 NEW-1）\n- R8-W3 [MAJOR]: δ* uncertainty 过宽（升级自 R7-SF5）\n- R8-MR1 [MINOR]: 缺失 Ding & VanderWeele (2016)\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-23T01:44:55.363857+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4168
}
```

</details>

---


### Assistant

_source line 642 · 2026-05-23T01:45:03.900254+00:00_

审稿报告已投递至 Research Director。

**Round 8 审稿完成。** 两位 Reviewer 一致评分 **3.5（Borderline Conference）**，Soundness 4/5，Excitement 3/5。

核心发现：
- **2 个 CRITICAL**：(1) Theorem 1 仅 K=2，ASV 在论文最关心的 K≥3 regime 缺乏形式化保证；(2) Proportional effects 假设在 NLP 中不可验证，general case 有 15-17% 失败率
- **4 个 MAJOR**：non-differential 假设讨论不足、primary coefficient claim 过强、ASV vs E-value 差异化不足、δ* uncertainty 过宽
- **推荐 Findings 接收**：bias taxonomy 和 FWL 不变性填补真实空白，但 ASV 方法论增量有限，main conference 需要更强的 K≥3 理论保证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 71

## Round 71

2 recorded events


### User

_source line 643 · 2026-05-23T01:45:06.601827+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：与 R1 在三个关键问题上形成共识（非差异性假设、K≥3 理论保证不足、措辞过强），同意其 N1/N2 两个 critical 问题，仅对 W4（Table 1 Collider amplification）提出 REBUT（可能是 R1 误读或排版问题），对 W3（δ* uncertainty）给出 partially agree（问题集中在 IV/exposure topology，非全局性）。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 644 · 2026-05-23T01:45:18.846349+00:00_

审稿报告已投递至 Research Director。

**Round 8 审稿完成。** 两位 Reviewer 均评 3.5（Borderline Conference），核心共识：

1. **Theorem 1 仅 K=2** — ASV 在论文最关心的 K≥3 regime 缺乏形式化保证（CRITICAL）
2. **Proportional effects 假设过强** — NLP 中几乎不可验证，general case 15-17% 失败率未在正文报告（CRITICAL）
3. **Non-differential 假设讨论不足** — LLM pretraining 隐含 A-Y 关联，主文仅 Limitations 一句话（MAJOR 共识）
4. **ASV novelty 有限** — sensitivity analysis 标准模板的新参数化，建议定位调整（MAJOR 共识）

推荐 **Findings 接收**，main conference 需更强方法论创新或 K≥3 形式化保证。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 72

## Round 72

44 recorded events


### User

_source line 645 · 2026-05-23T02:40:30.532581+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-23T02:40:36.755897+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-23T02:40:36.756624+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-23T02:40:45.189309+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-23T02:40:45.239916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-23T02:40:48.503704+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-23T02:40:48.606456+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-23T02:40:52.823810+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-23T02:40:52.924741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-23T02:40:55.335133+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-23T02:40:57.093543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-23T02:40:57.997429+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\input{related_work}
38	
39	\input{method}
40	
41	% ── Figures ──
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
46	\vspace{-6pt}
47	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
48	\label{fig:dag_taxonomy}
49	\end{figure*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-23T02:40:58.600195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-23T02:40:59.159140+00:00_

-rw-r--r-- 1 ubuntu ubuntu 909303 May 23 02:32 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 558
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-23T02:40:59.486802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-23T02:40:59.540886+00:00_

issues:
  # === Round 1-7 历史 (resolved，保留摘要) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 7
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
    resolution_round: 7

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 8
    mentions:
      - round
…[truncated 19858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 54
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-23T02:41:02.928431+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines with ARR:

## Paper Submission

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

Papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP vi
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7593
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-23T02:41:22.308978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-23T02:41:22.811511+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), the sign reversal rate is 2.1\%, concentrated in secondary coefficients with small effect sizes. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-23T02:41:22.811963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-23T02:41:23.264225+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-23T02:41:23.415368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-23T02:41:24.168759+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 1997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-23T02:41:24.169143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-23T02:41:24.671548+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This holds when the LLM annotates from source documents without access to outcome information. Even without explicit $Y$ access, differential misclassification can arise if LLM pretraining data encodes $A$--$Y$ statistical associations---e.g., in political stance classification, strongly emotional texts correlating with the outcome may be misclassified at different rates, violating $P(A^*{\mid}A,Y) = P(A^*{\mid}A)$. Violations can also arise from outcome-conditional prompting, few-shot demonstrations encoding $A$--$Y$ associations, or retrieval-augmented pipelines surfacing $Y$-correlated documents. When violated, bias can deviate in either direction without the toward-null constraint. Practitioners can diagnose violations by testing $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on a gold-labeled subset, though $Y$-conditional validation sets are rarely available in practice; our stress test (Appendix~\ref{sec:nondiff_stress}) covers $\varepsilon$ up to $0.50$ as a conservative upper bound, with violations below $\varepsilon{=
…[truncated 13914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-23T02:41:24.822581+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-23T02:41:24.873430+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse th
…[truncated 7062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-23T02:41:24.873935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-23T02:41:24.924499+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary coefficient does not reverse in any tested configuration---an empirical regularity driven by magnitude dominance rather than algebraic structure---while 61\% of exposure configurations reverse a secondary coefficient. Our analytical results assume linear SEMs; Appendix~\ref{sec:logistic_dgp} demonstrates that topology rankings and sign-flip patterns are preserved under logistic DGP ($|\Delta\,\text{SF}_\tau| < 0.02$), though FWL invariance is specific to linear models. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinea
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-23T02:41:47.913914+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-23T02:41:48.416240+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-23T02:41:49.772982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-23T02:41:51.939344+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4025
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-23T02:41:51.990051+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3573
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-23T02:41:52.298258+00:00_

File content (36840 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 2525
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-23T02:41:58.979594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-23T02:41:59.833609+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 3331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-23T02:41:59.984811+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i pages || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-23T02:42:00.086292+00:00_

Pages:           28
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-23T02:42:30.346934+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验验证**。\n\n## 目标 Venue 信息\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: Long paper，正文 ≤ 8 页（不含参考文献、Limitations、Ethics）\n- **模板**: ACL 2023 style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **附录**: 允许，但审稿人没有义务阅读\n- **关键更新**: ARR May cycle 与 EMNLP 和 AACL 共享，提交时必须声明目标会议\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Theorem 1（K=2 envelope monotonicity）的证明是否完整正确？proportional effects 假设是否合理？\n- Proposition 1（sign preservation）的条件是否充分？confounding 和 collider 的解析证明是否正确？\n- Observation 1 和 Conjecture 1 的数值验证是否充分？K≥3 下 ASV 的理论基础是否依赖过强的 conjectural 假设？\n- λ(C) ∈ [0,1] 在 proportional effects 下的证明是否成立？non-proportional 时 23% failure rate 的讨论是否充分？\n- Bias expressions（Eq. 1-4）的推导是否正确？\n\n### 2. 实验验证\n- 100,000 Dirichlet 矩阵的实验设计是否合理？先验选择的 justification？\n- 23 个 LLM configurations 的实证验证是否充分？4 个开源 LLM 是否代表性足够？\n- Theory-MC MAPE 1.6% 的验证是否可靠？161 scenarios 的覆盖是否完整？\n- Table 1 的数据与文中叙述是否一致？\n- Correction methods 的评估是否公平？PPI++ 的 gold label 要求是否过度限制了比较的公平性？\n- FWL invariance 的实证验证（logistic DGP）是否充分？\n\n### 3. 假设合理性\n- Non-differential misclassification 假设在 LLM 场景中是否合理？讨论是否充分？\n- 线性 SEM 假设对 NLP 实践的适用性？\n- DAG 拓扑必须先验已知的限制是否讨论充分？\n\n### 4. 格式合规\n- 正文是否 ≤ 8 页？（PDF 共 28 页，含大量 appendix）\n- 是否 double-blind（作者匿名）？\n- Limitations 部分是否存在且合理？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 severity 分 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Overall Assessment（用 ARR 评分标准：1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验验证**。\n\n## 目标 Venue 信息\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: Long paper，正文 ≤ 8 页（不含参考文献、Limitations、Ethics）\n- **模板**: ACL 2023 style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **附录**: 允许，但审稿人没有义务阅读\n- **关键更新**: ARR May cycle 与 EMNLP 和 AACL 共享，提交时必须声明目标会议\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Theorem 1（K=2 envelope monotonicity）的证明是否完整正确？proportional effects 假设是否合理？\n- Proposition 1（sign preservation）的条件是否充分？confounding 和 collider 的解析证明是否正确？\n- Observation 1 和 Conjecture 1 的数值验证是否充分？K≥3 下 ASV 的理论基础是否依赖过强的 conjectural 假设？\n- λ(C) ∈ [0,1] 在 proportional effects 下的证明是否成立？non-proportional 时 23% failure rate 的讨论是否充分？\n- Bias expressions（Eq. 1-4）的推导是否正确？\n\n### 2. 实验验证\n- 100,000 Dirichlet 矩阵的实验设计是否合理？先验选择的 justification？\n- 23 个 LLM configurations 的实证验证是否充分？4 个开源 LLM 是否代表性足够？\n- Theory-MC MAPE 1.6% 的验证是否可靠？161 scenarios 的覆盖是否完整？\n- Table 1 的数据与文中叙述是否一致？\n- Correction methods 的评估是否公平？PPI++ 的 gold label 要求是否过度限制了比较的公平性？\n- FWL invariance 的实证验证（logistic DGP）是否充分？\n\n### 3. 假设合理性\n- Non-differential misclassification 假设在 LLM 场景中是否合理？讨论是否充分？\n- 线性 SEM 假设对 NLP 实践的适用性？\n- DAG 拓扑必须先验已知的限制是否讨论充分？\n\n### 4. 格式合规\n- 正文是否 ≤ 8 页？（PDF 共 28 页，含大量 appendix）\n- 是否 double-blind（作者匿名）？\n- Limitations 部分是否存在且合理？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 severity 分 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Overall Assessment（用 ARR 评分标准：1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-23T02:42:50.435109+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20088
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-23T02:42:50.586132+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作呈现**。\n\n## 目标 Venue 信息\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: Long paper，正文 ≤ 8 页（不含参考文献、Limitations、Ethics）\n- **模板**: ACL 2023 style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **附录**: 允许，但审稿人没有义务阅读\n- **关键更新**: ARR May cycle 与 EMNLP 和 AACL 共享，提交时必须声明目标会议\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 三个 contributions 的新颖性评估：(1) multi-class bias taxonomy 是否真的是 \"first systematic\"？(2) ASV framework 与 E-values/partial R² 的方法论差异是否足够？(3) FWL invariance 负结果的价值如何？\n- 与现有工作的区分度：特别是 Teblunthuis (2024)、Lee et al. (2024)、Brenner (1993) 的工作\n- \"topology-dependent\" 这个核心 insight 是否足够 novel？之前是否有人指出过类似的观察？\n- ASV 定位为 \"diagnostics\" 而非 \"framework\"——这是否削弱了方法论贡献？\n\n### 2. 相关工作完整性\n- Related Work 是否覆盖了所有重要的前沿工作？\n- 是否有遗漏的关键引用？特别检查：\n  - Measurement error 文献（Carroll et al., Gustafson, Bound et al.）\n  - LLM annotation 文献（最新 2024-2025 工作）\n  - Sensitivity analysis 文献（E-values, partial R², robustness value）\n  - Causal inference in NLP（Feder et al., Keith et al.）\n- 引用是否准确？是否有 fabricated citations？\n- 引用格式是否符合 ACL 规范（natbib）？\n\n### 3. 写作质量与呈现\n- Abstract 信息密度是否合适？是否存在过度声称（overclaiming）？\n- Introduction 的叙事逻辑是否清晰？\"gap → contribution\" 的论证是否有力？\n- 术语和符号是否一致？（τ, β_T, 各拓扑的参数定义）\n- 图表质量：Figure 1（DAG taxonomy）、Figure 2（bias distribution）、Table 1 是否清晰可读？\n- 论文的整体可读性——对于不熟悉 measurement error 文献的 NLP 读者是否可理解？\n- Conclusion 是否准确总结了贡献？是否有 overclaiming？\n- Limitations 是否覆盖关键限制（non-differential assumption, linear SEM, single annotator）？\n\n### 4. 格式合规性\n- 正文是否严格 ≤ 8 页？\n- 参考文献格式是否符合 ACL 规范？\n- 匿名性是否完整（无作者信息泄露）？\n- Limitations 部分是否存在且格式正确？\n- 是否有不当使用 appendix 来规避页数限制的情况？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 severity 分 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Overall Assessment（用 ARR 评分标准：1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作呈现**。\n\n## 目标 Venue 信息\n- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: Long paper，正文 ≤ 8 页（不含参考文献、Limitations、Ethics）\n- **模板**: ACL 2023 style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息匿名）\n- **附录**: 允许，但审稿人没有义务阅读\n- **关键更新**: ARR May cycle 与 EMNLP 和 AACL 共享，提交时必须声明目标会议\n\n## 论文文件\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_9/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 三个 contributions 的新颖性评估：(1) multi-class bias taxonomy 是否真的是 \"first systematic\"？(2) ASV framework 与 E-values/partial R² 的方法论差异是否足够？(3) FWL invariance 负结果的价值如何？\n- 与现有工作的区分度：特别是 Teblunthuis (2024)、Lee et al. (2024)、Brenner (1993) 的工作\n- \"topology-dependent\" 这个核心 insight 是否足够 novel？之前是否有人指出过类似的观察？\n- ASV 定位为 \"diagnostics\" 而非 \"framework\"——这是否削弱了方法论贡献？\n\n### 2. 相关工作完整性\n- Related Work 是否覆盖了所有重要的前沿工作？\n- 是否有遗漏的关键引用？特别检查：\n  - Measurement error 文献（Carroll et al., Gustafson, Bound et al.）\n  - LLM annotation 文献（最新 2024-2025 工作）\n  - Sensitivity analysis 文献（E-values, partial R², robustness value）\n  - Causal inference in NLP（Feder et al., Keith et al.）\n- 引用是否准确？是否有 fabricated citations？\n- 引用格式是否符合 ACL 规范（natbib）？\n\n### 3. 写作质量与呈现\n- Abstract 信息密度是否合适？是否存在过度声称（overclaiming）？\n- Introduction 的叙事逻辑是否清晰？\"gap → contribution\" 的论证是否有力？\n- 术语和符号是否一致？（τ, β_T, 各拓扑的参数定义）\n- 图表质量：Figure 1（DAG taxonomy）、Figure 2（bias distribution）、Table 1 是否清晰可读？\n- 论文的整体可读性——对于不熟悉 measurement error 文献的 NLP 读者是否可理解？\n- Conclusion 是否准确总结了贡献？是否有 overclaiming？\n- Limitations 是否覆盖关键限制（non-differential assumption, linear SEM, single annotator）？\n\n### 4. 格式合规性\n- 正文是否严格 ≤ 8 页？\n- 参考文献格式是否符合 ACL 规范？\n- 匿名性是否完整（无作者信息泄露）？\n- Limitations 部分是否存在且格式正确？\n- 是否有不当使用 appendix 来规避页数限制的情况？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses（按 severity 分 CRITICAL/MAJOR/MINOR）→ Questions → Missing References → Overall Assessment（用 ARR 评分标准：1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-23T02:42:52.094519+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 688 · 2026-05-23T02:43:00.321267+00:00_

**Round 9 审稿圆桌已启动。**

| 项目 | 状态 |
|------|------|
| Venue | EMNLP 2026 (ARR May cycle, deadline 2026-05-25) |
| 论文 | 28 页 PDF (含 appendix)，ACL review 模板，double-blind |
| Reviewer 1 | 已分配 — 方法严谨性 + 实验验证 |
| Reviewer 2 | 已分配 — 新颖性 + 完整性 + 写作呈现 |
| 视觉审查 | 已派发（与 Reviewer 并行） |
| 外部审稿 | 未配置，跳过 |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 73

## Round 73

2 recorded events


### User

_source line 689 · 2026-05-23T02:50:33.080266+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作呈现）

### Paper Summary

本文研究 LLM 标注产生的多分类误差（multi-class misclassification）如何在因果推断中传播，重点揭示传播方式的**拓扑依赖性**。论文为 7 种标准 DAG 拓扑推导了 K-class 非差异误分类下的闭式偏差表达式，提出 Annotation Sensitivity Values (ASV) 诊断框架（含三种度量：magnitude、significance、sign-flip），并评估 5 种校正方法，证明 FWL 不变性使矩阵校正对 4 种拓扑无效。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 一篇技术扎实的理论工作，系统性地填补了多分类标注误差在因果推断中跨拓扑传播的分析空白，但贡献整体偏增量型（incremental），且线性 SEM + 非差异假设限制了对 NLP 实践的直接适用性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 理论推导严谨，数值验证充分（100K 随机矩阵 + 23 个真实 LLM 混淆矩阵），Proposition/Theorem 均有解析证明或数值验证。但核心假设（线性 SEM、非差异误分类）对实际 NLP 场景有较大限制。 |
| Excitement | 3/5 | 话题及时（LLM 标注误差 × 因果推断），"拓扑决定偏差性质" 的核心洞察有实用价值。但单项贡献偏增量——各拓扑的偏差分析是经典测量误差理论的多分类推广，ASV 是现有灵敏度分析工具的变体，FWL 不变性是已知定理的应用。|
| Overall | 3.5/5 | Borderline Conference。理论完整性和验证充分性接近主会议标准，但新颖性和实践影响力偏弱。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Abstract 和 Introduction 中 "first systematic" 声称需要更精确的限定

- 具体位置：Abstract ("We derive bias expressions for seven canonical topologies") 和 Section 1 第 1 条贡献 ("Multi-class bias taxonomy")
- 问题：论文声称 "first to characterize how the same confusion matrix produces qualitatively different bias across seven topologies"（page 2 左栏）。但需要更清楚地界定 "first" 的范围：
  - Brenner (1993) 已证明 polytomous confounder 误分类可以放大偏差（甚至方向翻转），这是 K≥3 sign reversal 的先驱
  - Teblunthuis et al. (2024) 分析了自动分类器误分类在回归中的偏差（虽然只覆盖一种拓扑）
  - Ogburn & VanderWeele (2012) 对 binary confounder 证明了单调性
  
  论文实际的新颖性在于 **同时覆盖 7 种拓扑 × K-class 的闭式偏差对比**，而非各单项拓扑结果本身。建议在 Abstract 和 Introduction 中将 "first systematic" 修改为更精确的表述，如 "first unified analysis across seven topologies under multi-class misclassification"，同时明确承认各单拓扑的先驱工作。
- 为什么影响接收：Overclaiming 是 ARR 审稿中的常见扣分项。如果 reviewer 认为 novelty claim 夸大，会直接降低 excitement 和 overall 分数。
- 建议修改方向：在 Abstract 中加入 "extending prior single-topology analyses" 的限定语；在 Section 1 贡献列表中明确 "building on" Brenner (1993) 和 Ogburn & VanderWeele (2012) 的工作。

**N2** [critical] 线性 SEM 假设对 NLP 读者的可达性不足，且 generalization 讨论薄弱

- 具体位置：Section 3.1 (Setup and Notation), Section 5 (Conclusion), Limitations
- 问题：论文的全部理论结果都建立在线性 SEM 上（"linear structural equation models", page 3）。对于 EMNLP 的核心读者群（NLP 研究者），这带来两个问题：
  1. **可达性**：论文没有充分解释为什么选择线性 SEM 而非更接近 NLP 实践的非线性模型（如 logistic regression），Section 3.1 直接跳入线性框架而缺少动机论述
  2. **泛化性**：虽然 Appendix B.6 展示了 logistic DGP 下 sign-flip pattern 的稳定性，但正文仅用一句话提及（page 8, Section 5 第一段末尾和 Limitations 倒数第二段："FWL invariance is specific to linear models"）。这一关键限制应在正文 Method 部分早期讨论，而非藏在 Limitations 中
- 为什么影响接收：EMNLP reviewer 可能认为线性 SEM 与现代 NLP 管线脱节，如果不提前建立连接（如：线性模型是因果推断的标准起点，非线性扩展方向明确），会削弱论文对 venue 的 fit。
- 建议修改方向：在 Section 3.1 开头增加 1-2 句解释为什么从线性 SEM 出发（标准分析起点、允许闭式解、Section B.6 的 logistic 验证提供稳健性保证）；将 Appendix B.6 的核心结论（sign-flip pattern 在 logistic DGP 下保持）提升到正文 Section 4 或 5 中用 1-2 句总结。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ASV 框架的实际可操作性（actionability）论证不足

- 具体位置：Section 3.3, Section 4.3, Algorithm 1 (page 28)
- 问题：ASV 被定位为 "diagnostics"（page 2, Contribution 2），但论文没有充分展示一个从业者如何在实际工作流中使用它。Section 4.3 验证了 ASV 的理论性质（monotonicity、sharp phase transition），但缺少一个端到端的使用场景：给定一个新的 NLP 因果分析任务，从业者如何获取 ASV 所需的输入（confusion matrix C₀、DAG topology），如何解释三种 ASV 度量的具体数值，以及如何据此做出行动决策？Algorithm 1 (Appendix page 28) 提供了校正指导，但它与 ASV 的连接不够紧密——Algorithm 1 的输入是 topology ranking 而非 ASV 值。
- 建议：增加一个 "practitioner walkthrough" 子节或 box，用一个具体例子（如：HumAID 上的某个配置）演示从 confusion matrix → topology identification → ASV computation → correction decision 的完整流程。

**W2** [warning] 经验验证的 NLP 任务覆盖面有限

- 具体位置：Section 4.1, Section 4.4
- 问题：经验验证仅使用 3 个 NLP 数据集（HumAID K=10, VAST K=5, CivilComments K=2），4 个 LLM 产生 23 个混淆矩阵。虽然 Monte Carlo 模拟覆盖了大量随机矩阵，但真实 LLM 混淆矩阵的多样性有限：
  1. 所有数据集都是英文
  2. K 值范围偏小（最大 K=10），很多 NLP 任务有更多类别（如 sentiment 的 5-class、NER 的几十个类别）
  3. 仅使用了 4 个 LLM（Llama-4-Maverick, Qwen2.5-32B, DeepSeek-Chat, Qwen2.7-TL-Instruct），均为开源模型，缺少 GPT-4 等闭源模型的对比
- 建议：承认这一限制；如果空间允许，增加 1-2 个更高 K 值的任务（如 NER、fine-grained sentiment）。

**W3** [warning] K≥3 sign reversal 率的呈现可能误导读者

- 具体位置：Abstract ("the sign reversal rate is 2.1%"), Section 4.2
- 问题：Abstract 中报告 "Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 2.1%, concentrated in secondary coefficients with small effect sizes"。这个 2.1% 的数字可能让读者认为 sign reversal 是极端罕见事件，从而低估问题的严重性。但论文同时报告了 IV 拓扑下的 sign reversal 率高达 42.1%（Section 4.2, page 6），以及在低准确率下 sign reversal 率急剧上升。2.1% 是所有拓扑和配置的平均值，这个聚合数字掩盖了 topology-specific 的风险差异——恰恰与论文 "topology-dependent" 的核心主张矛盾。
- 建议：在 Abstract 中改为报告 range（如 "from near-zero for confounding to over 40% for IV"），或至少加上 "across all topologies" 的限定。

**W4** [warning] Conjecture 1 的理论完成度

- 具体位置：Section 3.3, Observation 1, Conjecture 1 (page 5-6)
- 问题：Conjecture 1 声称对 non-IV 拓扑，envelope monotonicity extends to K≥3。这只有数值验证（30,000 random matrices per K），没有解析证明。对于一篇主要贡献是理论分析的论文，一个核心性质止步于 conjecture 而非 theorem 是一个弱点。论文诚实地标注为 conjecture（而非假装证明），这是正确的做法，但这确实削弱了理论贡献的完整性。
- 建议：如果无法在短期内证明，至少讨论证明的障碍是什么（是技术困难还是有可能存在反例？）。

**W5** [warning] Related Work 对 "sensitivity analysis" 文献线的覆盖可以更深入

- 具体位置：Section 2, paragraph 3 (page 3, "Sensitivity analysis and correction methods")
- 问题：论文列举了 E-values (VanderWeele & Ding 2017)、Cinelli & Hazlett (2020) 的 robustness value、以及 Imai et al. (2010) 的 mediation sensitivity analysis，但对比论述比较粗略。特别是：
  1. E-value 处理的是 unmeasured confounding 的灵敏度，而 ASV 处理的是 misclassification 的灵敏度——这个本质区别没有被清楚阐述
  2. Lash, Fox, and Fink (2009) 的 Quantitative Bias Analysis (QBA) 框架与 ASV 的关系没有讨论，但 QBA 是流行病学中处理 misclassification 偏差的标准工具
  3. 论文的灵敏度分析方法与 Blackwell et al. (2017) 的统一框架的关系也可以更清楚
- 建议：在 Related Work 中增加一段更深入的对比，明确 ASV 相对于 E-value/QBA/partial R² 的定位差异（ASV 是 topology-aware 的，这是其独特之处）。

---

## 小问题（不影响接收）

- **P1** [minor] Figure 2 (page 7) 的 y 轴标签较小，在打印版中可能难以辨读。建议增大字号。
- **P2** [minor] Table 1 (page 7) 的 "Sign Flip" 列中 "✗" 和 "✓" 在黑白打印时难以区分，考虑使用文字标记（如 Yes/No）。
- **P3** [minor] Section 3.2 中从 confounding 到 exposure 到 mediation 的过渡比较突然，每个拓扑的偏差表达式段落之间可以加入简短的过渡句来引导读者。
- **P4** [minor] Limitations 部分（page 9）提到 "multi-annotator settings (Kim et al., 2025)"，但没有讨论 annotator disagreement 如何影响 confusion matrix 的估计——这是一个实际中的重要问题。
- **P5** [minor] 论文中多次使用 "plim" 记号（probability limit），对 NLP 读者来说不太常见，第一次出现时（Section 3.2, page 3）应加简要定义。
- **P6** [minor] Abstract 中 "Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations" 这个结论过于绝对——在某些拓扑下（如 confounding），即使不做 topology-aware 分析，偏差方向也是可预测的。

---

## Missing References

经过文献搜索，论文的引用覆盖面总体良好，关键领域的核心工作均已引用。以下是可能的补充：

1. **Bound, Brown, and Mathiowetz (2001)** — "Measurement error in survey data" (Handbook of Econometrics, Ch. 59)。这是测量误差文献的经典综述，虽然论文已引用 Carroll et al. (2006) 和 Gustafson (2004)，但 Bound et al. 对社会科学读者更熟悉。*优先级：低*

2. **VanderWeele (2015)** — *Explanation in Causal Inference: Methods for Mediation and Interaction* (Oxford UP)。论文引用了 VanderWeele 的多篇论文，但未引用这本综合性教材，对 mediation 拓扑的讨论可以参考。*优先级：低*

3. 论文未发现 fabricated citations。引用格式总体符合 ACL natbib 规范。

---

## 格式合规性

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | Sections 1-5 在 pages 1-8 内完成 |
| 参考文献格式 | ✓ | 使用 natbib，格式一致 |
| 匿名性 | ✓ | "Anonymous ACL submission"，未发现作者信息泄露 |
| Limitations | ✓ | 在 page 9（不计入页数），覆盖了主要限制 |
| 附录使用 | ✓ | 附录包含完整证明和补充实验，未发现将核心贡献移出正文的规避行为 |
| 模板 | ✓ | 使用 ACL 2023 style with [review] option |

---

## 主要优势

1. **系统性覆盖**：首次在统一框架下对 7 种 DAG 拓扑 × K-class 误分类推导闭式偏差表达式，这种对比视角是本文最大的贡献。
2. **理论与实证的双重验证**：每个理论结果都有数值验证（100K 随机矩阵），加上 23 个真实 LLM 混淆矩阵的经验验证，论证链完整。
3. **实用的负结果**：FWL 不变性意味着对 4 种拓扑，基于矩阵校正的方法无效——这对从业者有直接指导价值，避免浪费精力在无效校正上。
4. **拓扑脆弱性排名**：IV (maximally fragile) → M-bias (immutable) 的排名（Table 1, Figure 3）提供了简明的实践指南。
5. **Conjecture 的诚实处理**：将无法完全证明的 K≥3 envelope monotonicity 标注为 Conjecture 而非 Theorem，体现了学术诚信。
6. **丰富的附录**：20 页附录包含完整证明、多个稳健性检验（non-differential stress test, cross-K, logistic DGP, bootstrap uncertainty），为可复现性提供了充分材料。

---

## 总结

本文是一篇技术扎实的理论工作，系统性地分析了 LLM 多分类标注误差在 7 种 DAG 拓扑下的传播特征。核心洞察——拓扑决定偏差性质——有实用价值且论证充分。主要不足在于：(1) novelty claim 需要更精确的限定以避免 overclaiming；(2) 线性 SEM 假设对 NLP 实践的适用性需要更多论述；(3) ASV 框架的可操作性展示不足。论文质量介于 Findings 和主会议之间，建议作者重点加强 N1 (novelty claim 精确化) 和 W1 (ASV actionability)，这两项改进可以将论文提升到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 690 · 2026-05-23T02:50:39.794865+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 691 · 2026-05-23T02:50:46.215574+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 4/5** — 理论推导严谨，数值验证充分，但线性 SEM + 非差异假设限制泛化性
- **Excitement: 3/5** — 话题及时，核心洞察有用，但单项贡献偏增量型

**2 个 Must-Fix**：(N1) "first systematic" 的 novelty claim 需精确限定，避免 overclaiming；(N2) 线性 SEM 假设对 NLP 读者的可达性和泛化讨论不足

**5 个 Should-Fix**：ASV 可操作性论证不足(W1)、经验验证任务覆盖面有限(W2)、sign reversal 率 2.1% 的聚合数字掩盖拓扑差异(W3)、Conjecture 1 理论完成度(W4)、sensitivity analysis 文献线对比可更深入(W5)

格式完全合规，引用覆盖面良好，未发现 fabricated citations。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 692 · 2026-05-23T02:50:50.772341+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 的审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 75

## Round 75

6 recorded events


### User

_source line 693 · 2026-05-23T02:51:23.894850+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：Multi-Class Annotation Errors in Causal Inference

---

## 总体评分

**Overall**: 3.5/5 (Borderline Conference)

**一句话总结**: 论文在 LLM 标注误差×因果推断交叉领域提出了系统性理论框架，K=2 结果严谨，关键洞见（拓扑决定风险而非标注准确率）有价值，但核心假设（非差异性误分类、比例效应）在 LLM 实践中的合理性论证不足，K≥3 理论基础依赖数值验证和猜想，实际可用性受线性 SEM 假设限制。

---

## 官方维度打分（来自 ACL Rolling Review review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 证明完整正确（Theorem 1 单调性、Proposition 1 sign preservation）；K≥3 依赖 Observation 1（数值）和 Conjecture 1（猜想），虽标注诚实但理论不完整。MC 验证 MAPE 1.6% 具有说服力。Eq. 1-4 的推导在线性 SEM 下正确。 |
| Excitement | 3.5/5 | 问题定义新颖——首次系统刻画混淆矩阵结构×DAG 拓扑对因果估计的联合影响。ASV 框架和"拓扑>准确率"的洞见具有概念价值。但线性 SEM 假设限制了对 NLP 社区的直接影响力。 |
| Reproducibility | 4/5 | MC 参数（N=10,000, Dirichlet 先验, 7 拓扑）明确指定；23 个 LLM 配置的数据集/模型/prompt 策略有详细说明；承诺代码公开。 |
| Reviewer Confidence | 4/5 | 仔细阅读正文 8 页 + 附录 20 页，检查了主要证明结构和实验设计。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心假设在 LLM 标注场景中的合理性缺乏实证验证

- 具体位置：Definition 1 (Section 3.1, page 3)、Theorem 1 (Section 3.3/Appendix A.4)、Limitations (page 9)
- 问题：论文的整个框架建立在两个关键假设上——(1) 非差异性误分类 P(A*|A,Y,Z)=P(A*|A)（Definition 1），(2) Theorem 1 的单调性证明要求 proportional effects (f=λ₀·g)。但论文未提供任何实证证据表明这些假设在 LLM 标注场景中近似成立。

  对于假设 (1)：LLM 分类器可能对具有强烈情感/立场的文本（与 outcome 相关）更准确，导致误差率依赖于 Y。Appendix B.5 的 stress test 使用均匀 ε-扰动模型（Table 7/8），但这种扰动模式是否能捕捉 LLM 的真实差异性误差模式？例如，outcome-conditional error rate（LLM 对强 treatment effect 样本分类更准确）这种更现实的违反模式未被测试。

  对于假设 (2)：Appendix B.12 (Table 12) 显示在非比例效应下，λ(C) 越界率在 δ=0.1 时已达 ~10%，独立 f 时饱和于 ~23%。但论文未论证 LLM 混淆矩阵为何应满足比例效应。不同类别间的误分类（如"正面→中性"vs"正面→负面"）对因果估计的影响在结构上应当是不同的。

- 为什么影响接收：论文的目标读者是使用 LLM 标注进行因果推断的 NLP 研究者（Section 1, Introduction 明确定位）。如果核心假设在目标场景中不成立，框架的实用价值将大打折扣。23 个 LLM 配置的验证（Section 4.4）测试了理论-MC 一致性，但并未测试假设本身的有效性。
- 建议修改方向：
  (a) 利用已有的 23 个 LLM 混淆矩阵，提供 proportional effects 近似程度的定量评估（如计算各配置下 f(A) 的比例性偏离度）；
  (b) 设计更具 LLM 特异性的差异性误分类测试——例如按 outcome 分层估计条件混淆矩阵 P(A*|A,Y=y)，如果金标签数据允许的话；
  (c) 至少在主文中更显著地讨论假设违反的后果，将 Appendix B.5 和 B.12 的关键发现纳入主文。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] K≥3 理论基础不完整，而 K≥3 是 NLP 的主要应用场景

- 具体位置：Observation 1 (Section 3.3, page 6)、Conjecture 1 (Section 3.3, page 6)、Appendix B.11 (page 25)
- 问题：K=2 时 2×2 列随机矩阵的正对角约束使 sign preservation 成为结构性保证——这是优雅且严格的。但 K≥3 时负权重成为可能（Section 1, page 1: "K≥3 introduces a structural possibility of sign reversal"），此时：
  - Theorem 1 的单调性从证明退化为数值验证（Observation 1：20,000 次验证零违反）
  - Collider/M-bias 的 envelope non-increasing 性质仅为猜想（Conjecture 1：30,000 矩阵验证）
  - ASV 框架的排序和 Algorithm 1 的实用指导依赖这些未证明的结果

  NLP 任务绝大多数是 K≥3（情感分析 3-5 类，事件类型 10+ 类），论文在 K=2 上的严格保证对目标社区的覆盖面有限。
- 建议：
  (a) 更明确地在主文中区分"K=2 保证"与"K≥3 经验性结论"的边界
  (b) 讨论 Observation 1/Conjecture 1 的证明难点和可能的证明路径
  (c) 增加 K=5,7,10 下使用真实 LLM 混淆矩阵（而非 Dirichlet 随机矩阵）的 ASV 排序稳定性验证

**W2** [warning] 线性 SEM 假设与 NLP 实践的差距需更充分讨论

- 具体位置：Section 3.1 (page 3, "linear structural equation models")、Appendix B.6 (page 23)、Limitations (page 9)
- 问题：论文在 Appendix B.6 中测试了 logistic DGP 的鲁棒性，显示线性和 logistic DGP 的 sign-flip 模式"virtually identical"（|ΔSF| < 0.02 for most topologies）。这是有价值的。但 logistic 回归仍然是相对简单的非线性——NLP 因果推断中常见的是更复杂的模型（transformer-based estimators, double ML pipelines）。此外，Appendix B.13 的 FWL invariance 在 logistic 下的验证仅测到 N=50,000，结论措辞谨慎（"breakdown is negligible"）但未讨论大 N 时的行为。

  Limitations 部分对此的讨论仅一句话："The framework assumes a correctly specified causal DAG; when the topology is unknown, practitioners should compute ASV under candidate DAGs and report the most conservative."这更多是关于 DAG 未知性，对线性 SEM 本身的局限讨论不足。
- 建议：在 Limitations 中增加对非线性模型适用性的明确讨论，包括何种条件下线性近似合理、何时可能失效。

**W3** [warning] 实证验证的 LLM 配置多样性有限

- 具体位置：Section 4.4 (page 8)、Table 1 (page 7)
- 问题：
  (a) 4 个开源 LLM（Llama-4-Maverick, Qwen2.5-23B, DeepSeek-Chat, Qwen2.7-TIL）规模相近，缺少小模型（<7B）和大模型（>70B）的对比，无法评估模型规模对混淆矩阵结构的影响；
  (b) "the primary coefficient does not reverse in any tested configuration"（Section 4.4, Numerical Verification 2）基于 23 个配置是经验性归纳，样本量不足以支撑普遍性声明。论文将其称为"empirical regularity driven by magnitude dominance"，但未讨论在何种混淆矩阵结构下这一规律可能被打破；
  (c) 3 个数据集（HumanAID K=10, VAST K=5, CivilComments K=2）涵盖了不同 K 值，但任务类型偏向分类（灾情/立场/毒性），缺少序数标注（如 Likert 量表评分）或层级标注等 NLP 中常见的标注类型。
- 建议：增加至少 1-2 个不同规模/架构的 LLM 配置，或讨论现有 23 个混淆矩阵在混淆矩阵参数空间中的覆盖度。

**W4** [warning] PPI++ 比较的公平性讨论可更细致

- 具体位置：Section 4.5 (page 8)、Table 4 (page 20)
- 问题：Table 4 显示 PPI++ 的 grand-mean RMSE reduction 为 17.0%（文中 Section 4.5 提到 47.6%——此处数字是否一致？需核实），但对 M-bias 为 −88%。论文正确指出 PPI++ 需要金标签这一限制，但比较框架中其他方法（如 MC-SIMEX）也有各自前提条件（需要多次 imputation），这些前提条件的实践可行性对比不够系统。

  此外，Section 4.5 称"no single method dominates"和"correction effectiveness is itself topology-dependent"，这是一个重要发现，但仅在正文最后半段简短提及，建议给予更充分的展开。
- 建议：增加一个简要的"correction method prerequisites"表格或讨论，系统对比各方法的输入要求和适用范围。

---

## 小问题（不影响接收）

- **m1** 符号密度高：正文 8 页包含大量符号定义和结果，首次阅读认知负担较大。建议在 Section 3.1 开头增加一个 running example（如 K=3 情感分析 + confounding topology）贯穿全文。
- **m2** Figure 1 (page 7) 的 7 个 DAG 图非常有用，但字体较小；Figure 2 的红/绿配色可能对色觉障碍读者不友好。
- **m3** Table 2 (page 19) 汇总了 sign preservation 的充分条件及其证明状态（Proved vs. Empirical），这张表对理解论文贡献非常关键，建议移至主文或在主文中更明确引用。
- **m4** "topology"一词在数学中有特定含义（拓扑空间），论文中用其指代 DAG 结构。建议统一使用"DAG structure"或首次使用时明确定义。
- **m5** Appendix B.1 (Binarization Collapse, page 20, Figure 6) 揭示 K=3→binary 的坍缩引入 15× 的额外拓扑依赖偏差，这是一个实用发现但主文几乎未提及。

---

## Questions for Authors

**Q1.** 能否定量评估现有 23 个 LLM 混淆矩阵与 proportional effects 假设的偏离程度？例如计算 f(A) 向量对参考函数 g(A) 的投影残差？

**Q2.** Numerical Verification 2 声称 primary coefficient 在 23 个配置中从未反转。是否存在可构造的混淆矩阵（仍满足 non-differential + 合理精度）使其反转？如果存在，需要什么条件？

**Q3.** ASV 排序（Table 1）在不同 DGP 参数化（系数大小、误差方差）下是否稳定？当前分析使用标准化 DGP，但实际因果效应大小差异显著。

**Q4.** 对于 collider 拓扑，论文指出 sign reversal 在结构上独特（"structurally distinct"）。在真实 DGP 为非线性但研究者使用线性回归估计时，这种结构独特性是否保持？

**Q5.** Section 4.5 提到的 PPI++ grand-mean RMSE reduction 数字（主文 47.6% vs Table 4）——请确认这两个数字是否指向同一统计量？如果不同，请澄清。

---

## 主要优势

1. **问题定义的新颖性和时效性**：首次系统性地将 LLM 标注误差的传播问题从"总体准确率"细化到"混淆矩阵结构 × DAG 拓扑"的联合分析，填补了 NLP×因果推断文献中的空白。
2. **K=2 理论的严谨性**：Theorem 1 的单调性证明结构完整（凸性 + 端点条件），Proposition 1 的 sign preservation 条件对 confounding/collider 给出了解析证明。证明路径（通过 FWL 分解和 between-group variance 分析）在方法论上也有独立价值。
3. **"拓扑 > 准确率"的反直觉洞见**：Figure 3 (page 8) 直观展示了 F₁ 0.618–0.690 范围内偏差变化 10× 的现象，挑战了"提高标注准确率即可解决下游问题"的常见假设。
4. **理论结果的诚实分层**：论文明确区分 Theorem（证明）、Proposition（部分证明 + 数值）、Observation（纯数值）、Conjecture（猜想），学术诚信度高。
5. **FWL 不变性的否定结果**：证明 matrix-based correction 对 4 个协变量拓扑 provably ineffective 是一个有实用价值的否定结论，可帮助研究者避免无效的纠偏策略。
6. **丰富的附录**：20 页附录提供完整证明、robustness checks（非线性 DGP B.6、差异性误分类 B.5、bootstrap B.7、DGP 稳定性 B.10），显著增强了论文的可信度。

---

**总结**：论文对一个重要且新颖的问题做出了实质性贡献。K=2 理论严格，ASV 框架设计巧妙，correction guidance 具有实用价值。主要顾虑在于：(1) 核心假设在 LLM 场景中的合理性缺乏实证验证（N1），(2) K≥3 理论不完整（W1），(3) 线性 SEM 限制实际影响力（W2）。如果 N1 能被充分回应（即使是承认局限并提供 robustness 证据），论文评分可提升至 4.0 (Conference)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-23T02:52:05.836833+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作呈现）\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 4/5 | **Excitement**: 3/5\n\n### Must-Fix\n\n**R2-N1** [critical] Abstract 和 Introduction 中 \"first systematic\" 声称需要更精确的限定\n- Brenner (1993) 已证明 polytomous confounder 误分类可以放大偏差\n- Teblunthuis et al. (2024) 分析了自动分类器误分类在回归中的偏差（虽然只覆盖一种拓扑）\n- Ogburn &amp; VanderWeele (2012) 对 binary confounder 证明了单调性\n- 论文实际的新颖性在于 **同时覆盖 7 种拓扑 × K-class 的闭式偏差对比**。建议将 \"first systematic\" 修改为更精确的表述。\n\n**R2-N2** [critical] 线性 SEM 假设对 NLP 读者的可达性不足，且 generalization 讨论薄弱\n- 论文没有充分解释为什么选择线性 SEM 而非更接近 NLP 实践的非线性模型\n- Appendix B.6 的 logistic DGP 结果应提升到正文\n- EMNLP reviewer 可能认为线性 SEM 与现代 NLP 管线脱节\n\n### Should-Fix\n\n**R2-W1** [warning] ASV 框架的实际可操作性（actionability）论证不足\n- 缺少端到端使用场景：从 confusion matrix → topology identification → ASV computation → correction decision\n- Algorithm 1 与 ASV 的连接不够紧密\n\n**R2-W2** [warning] 经验验证的 NLP 任务覆盖面有限\n- 仅 3 个英文数据集，K 值范围偏小（最大 K=10）\n- 4 个开源 LLM，缺少 GPT-4 等闭源模型\n\n**R2-W3** [warning] K≥3 sign reversal 率的呈现可能误导读者\n- Abstract 中 2.1% 是所有拓扑的聚合数字，掩盖 topology-specific 风险差异\n- 建议报告 range（如 \"from near-zero for confounding to over 40% for IV\"）\n\n**R2-W4** [warning] Conjecture 1 的理论完成度\n- 核心性质止步于 conjecture 而非 theorem，削弱理论贡献完整性\n- 应讨论证明障碍\n\n**R2-W5** [warning] Related Work 对 sensitivity analysis 文献线的覆盖可以更深入\n- E-value vs ASV 本质区别未清楚阐述\n- Lash et al. (2009) QBA 框架关系未讨论\n\n### Minor\n- P1: Figure 2 y 轴标签较小\n- P2: Table 1 ✗/✓ 黑白打印难区分\n- P3: Section 3.2 拓扑间过渡突然\n- P4: 多标注者设定对 confusion matrix 估计的影响\n- P5: \"plim\" 对 NLP 读者不常见，需定义\n- P6: Abstract 结论 \"necessary\" 过于绝对\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作呈现）\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 4/5 | **Excitement**: 3/5\n\n### Must-Fix\n\n**R2-N1** [critical] Abstract 和 Introduction 中 \"first systematic\" 声称需要更精确的限定\n- Brenner (1993) 已证明 polytomous confounder 误分类可以放大偏差\n- Teblunthuis et al. (2024) 分析了自动分类器误分类在回归中的偏差（虽然只覆盖一种拓扑）\n- Ogburn &amp; VanderWeele (2012) 对 binary confounder 证明了单调性\n- 论文实际的新颖性在于 **同时覆盖 7 种拓扑 × K-class 的闭式偏差对比**。建议将 \"first systematic\" 修改为更精确的表述。\n\n**R2-N2** [critical] 线性 SEM 假设对 NLP 读者的可达性不足，且 generalization 讨论薄弱\n- 论文没有充分解释为什么选择线性 SEM 而非更接近 NLP 实践的非线性模型\n- Appendix B.6 的 logistic DGP 结果应提升到正文\n- EMNLP reviewer 可能认为线性 SEM 与现代 NLP 管线脱节\n\n### Should-Fix\n\n**R2-W1** [warning] ASV 框架的实际可操作性（actionability）论证不足\n- 缺少端到端使用场景：从 confusion matrix → topology identification → ASV computation → correction decision\n- Algorithm 1 与 ASV 的连接不够紧密\n\n**R2-W2** [warning] 经验验证的 NLP 任务覆盖面有限\n- 仅 3 个英文数据集，K 值范围偏小（最大 K=10）\n- 4 个开源 LLM，缺少 GPT-4 等闭源模型\n\n**R2-W3** [warning] K≥3 sign reversal 率的呈现可能误导读者\n- Abstract 中 2.1% 是所有拓扑的聚合数字，掩盖 topology-specific 风险差异\n- 建议报告 range（如 \"from near-zero for confounding to over 40% for IV\"）\n\n**R2-W4** [warning] Conjecture 1 的理论完成度\n- 核心性质止步于 conjecture 而非 theorem，削弱理论贡献完整性\n- 应讨论证明障碍\n\n**R2-W5** [warning] Related Work 对 sensitivity analysis 文献线的覆盖可以更深入\n- E-value vs ASV 本质区别未清楚阐述\n- Lash et al. (2009) QBA 框架关系未讨论\n\n### Minor\n- P1: Figure 2 y 轴标签较小\n- P2: Table 1 ✗/✓ 黑白打印难区分\n- P3: Section 3.2 拓扑间过渡突然\n- P4: 多标注者设定对 confusion matrix 估计的影响\n- P5: \"plim\" 对 NLP 读者不常见，需定义\n- P6: Abstract 结论 \"necessary\" 过于绝对\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-23T02:52:31.385254+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25548
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-23T02:52:31.586307+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验验证）\n\n**Overall**: 3.5/5 (Borderline Conference)\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5\n\n### Must-Fix\n\n**R1-N1** [critical] 核心假设在 LLM 标注场景中的合理性缺乏实证验证\n- 两个关键假设：(1) 非差异性误分类 P(A*|A,Y,Z)=P(A*|A)，(2) proportional effects (f=λ₀·g)\n- 对 (1)：LLM 可能对具有强烈情感/立场的文本更准确，导致误差率依赖于 Y。Appendix B.5 的 stress test 使用均匀 ε-扰动，但是否能捕捉 LLM 的真实差异性误差模式？\n- 对 (2)：Appendix B.12 显示非比例效应下 λ(C) 越界率在 δ=0.1 时已达 ~10%，独立 f 时饱和于 ~23%。但未论证 LLM 混淆矩阵为何应满足比例效应。\n- 建议：(a) 利用 23 个 LLM 混淆矩阵定量评估 proportional effects 近似程度；(b) 设计 LLM 特异性的差异性误分类测试；(c) 将 Appendix B.5/B.12 关键发现纳入主文\n\n### Should-Fix\n\n**R1-W1** [warning] K≥3 理论基础不完整，而 K≥3 是 NLP 的主要应用场景\n- K=2 严格保证 vs K≥3 依赖数值验证和猜想\n- Theorem 1 从证明退化为 Observation 1（20,000 次验证）\n- ASV 框架和 Algorithm 1 依赖未证明的结果\n- 建议：明确区分 K=2 vs K≥3 边界，讨论证明难点\n\n**R1-W2** [warning] 线性 SEM 假设与 NLP 实践的差距需更充分讨论\n- Appendix B.6 logistic DGP 验证有价值但仍是简单非线性\n- Appendix B.13 FWL invariance logistic 验证仅到 N=50,000\n- Limitations 讨论不足\n\n**R1-W3** [warning] 实证验证的 LLM 配置多样性有限\n- 4 个开源 LLM 规模相近，缺小模型 (&lt;7B) 和大模型 (&gt;70B)\n- 23 个配置样本量不足以支撑 primary coefficient 的普遍性声明\n- 3 个数据集任务类型偏向分类，缺序数标注\n\n**R1-W4** [warning] PPI++ 比较的公平性讨论可更细致\n- Section 4.5 中 47.6% vs Table 4 数字是否一致？需核实\n- correction method prerequisites 的对比不够系统\n\n### Minor\n- m1: 符号密度高，建议 running example\n- m2: Figure 1 字体小，Figure 2 配色不友好\n- m3: Table 2 应移至主文或更明确引用\n- m4: \"topology\" 在数学中有特定含义\n- m5: Appendix B.1 binarization collapse 发现应在主文提及\n\n### Questions\n- Q1: 能否定量评估 23 个 LLM 混淆矩阵与 proportional effects 的偏离程度？\n- Q2: 是否存在可构造的混淆矩阵使 primary coefficient 反转？\n- Q3: ASV 排序在不同 DGP 参数化下是否稳定？\n- Q4: Collider 的结构独特性在非线性 DGP + 线性估计时是否保持？\n- Q5: PPI++ RMSE reduction 数字（主文 47.6% vs Table 4）是否一致？\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验验证）\n\n**Overall**: 3.5/5 (Borderline Conference)\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5\n\n### Must-Fix\n\n**R1-N1** [critical] 核心假设在 LLM 标注场景中的合理性缺乏实证验证\n- 两个关键假设：(1) 非差异性误分类 P(A*|A,Y,Z)=P(A*|A)，(2) proportional effects (f=λ₀·g)\n- 对 (1)：LLM 可能对具有强烈情感/立场的文本更准确，导致误差率依赖于 Y。Appendix B.5 的 stress test 使用均匀 ε-扰动，但是否能捕捉 LLM 的真实差异性误差模式？\n- 对 (2)：Appendix B.12 显示非比例效应下 λ(C) 越界率在 δ=0.1 时已达 ~10%，独立 f 时饱和于 ~23%。但未论证 LLM 混淆矩阵为何应满足比例效应。\n- 建议：(a) 利用 23 个 LLM 混淆矩阵定量评估 proportional effects 近似程度；(b) 设计 LLM 特异性的差异性误分类测试；(c) 将 Appendix B.5/B.12 关键发现纳入主文\n\n### Should-Fix\n\n**R1-W1** [warning] K≥3 理论基础不完整，而 K≥3 是 NLP 的主要应用场景\n- K=2 严格保证 vs K≥3 依赖数值验证和猜想\n- Theorem 1 从证明退化为 Observation 1（20,000 次验证）\n- ASV 框架和 Algorithm 1 依赖未证明的结果\n- 建议：明确区分 K=2 vs K≥3 边界，讨论证明难点\n\n**R1-W2** [warning] 线性 SEM 假设与 NLP 实践的差距需更充分讨论\n- Appendix B.6 logistic DGP 验证有价值但仍是简单非线性\n- Appendix B.13 FWL invariance logistic 验证仅到 N=50,000\n- Limitations 讨论不足\n\n**R1-W3** [warning] 实证验证的 LLM 配置多样性有限\n- 4 个开源 LLM 规模相近，缺小模型 (&lt;7B) 和大模型 (&gt;70B)\n- 23 个配置样本量不足以支撑 primary coefficient 的普遍性声明\n- 3 个数据集任务类型偏向分类，缺序数标注\n\n**R1-W4** [warning] PPI++ 比较的公平性讨论可更细致\n- Section 4.5 中 47.6% vs Table 4 数字是否一致？需核实\n- correction method prerequisites 的对比不够系统\n\n### Minor\n- m1: 符号密度高，建议 running example\n- m2: Figure 1 字体小，Figure 2 配色不友好\n- m3: Table 2 应移至主文或更明确引用\n- m4: \"topology\" 在数学中有特定含义\n- m5: Appendix B.1 binarization collapse 发现应在主文提及\n\n### Questions\n- Q1: 能否定量评估 23 个 LLM 混淆矩阵与 proportional effects 的偏离程度？\n- Q2: 是否存在可构造的混淆矩阵使 primary coefficient 反转？\n- Q3: ASV 排序在不同 DGP 参数化下是否稳定？\n- Q4: Collider 的结构独特性在非线性 DGP + 线性估计时是否保持？\n- Q5: PPI++ RMSE reduction 数字（主文 47.6% vs Table 4）是否一致？\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-23T02:52:33.047599+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Assistant

_source line 698 · 2026-05-23T02:52:35.384798+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 699 · 2026-05-23T02:52:38.035868+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整结构化意见，核心评判：

- **Overall 3.5/5 (Borderline Conference)**
- **1 个 Must-Fix**：核心假设（非差异性误分类 + 比例效应）在 LLM 场景中缺乏实证验证，框架的实用性取决于此
- **4 个 Should-Fix**：K≥3 理论依赖猜想/数值验证、线性 SEM 限制适用性、LLM 配置多样性有限、PPI++ 比较需更细致
- **主要优势**：问题新颖、K=2 理论严谨、"拓扑>准确率"洞见有价值、FWL 不变性否定结果实用、附录详尽

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 700 · 2026-05-23T02:52:42.741541+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 77

## Round 77

2 recorded events


### User

_source line 701 · 2026-05-23T02:54:37.340812+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: "first systematic" 声称需限定——但严重程度应降为 Should-Fix**

R2 的文献梳理准确：Brenner (1993) 确实覆盖了 polytomous confounder（论文在 page 1 和 page 4 明确引用），Ogburn & VanderWeele (2012) 已有 binary confounder 单调性结果。但论文的 Introduction (page 2) 的实际措辞是 "No prior work systematically characterizes how the same confusion matrix produces qualitatively different bias across causal designs"——关键词是 "the same confusion matrix" + "across causal designs"。这一表述比 R2 引述的 "first systematic" 更精确，强调的是跨拓扑的联合对比而非单个拓扑的分析。

然而，R2 的建议仍然有价值——论文可以进一步明确 Brenner (1993) 覆盖了 polytomous confounding，Teblunthuis et al. (2024) 覆盖了单拓扑回归偏差，从而更精确地界定自身贡献（7 拓扑 × K-class × 闭式对比 + 签名保持条件 + 灵敏度框架）。

**不同意 critical 严重程度**：论文的新颖性并不依赖于 "first" 这一措辞——即使移除该声称，7 拓扑的系统性对比、ASV 框架、FWL 不变性等贡献仍然成立。建议降为 Should-Fix (warning)。

---

**[AGREE] R2-N2: 线性 SEM 假设的讨论不足——与我的 W2 一致**

完全同意此问题的重要性。论文的 Appendix B.6 (page 23) 已证明 logistic DGP 下 sign-flip 模式与线性 "virtually identical"（|ΔSF| < 0.02），这是有价值的鲁棒性证据，确实应在正文中更突出地呈现。

补充一个 R2 未提到的细节：Appendix B.13 测试了 FWL invariance 在 logistic 下的表现（N 至 50,000），结论称 "breakdown is negligible"（< 0.005 bias reduction）。这进一步支持了线性近似在此问题中的合理性。如果将 B.6 和 B.13 的核心发现整合为正文一段（~4-5 行），可以有效缓解 EMNLP reviewer 对线性假设的顾虑。

**严重程度认同 critical**：考虑到 EMNLP 读者群体，线性 SEM 的可达性确实可能影响接收决定。

---

### Should-Fix

**[AGREE] R2-W1: ASV 可操作性论证不足——但 Algorithm 1 已部分回应**

R2 指出缺少端到端使用场景，这是合理的。但需指出论文在 Appendix B.16 (page 28) 已提供 Algorithm 1，包含完整的 confusion matrix → topology → ASV → correction decision 流程。该算法覆盖了 R2 要求的全部步骤：Step 1 评估风险等级（ASV threshold），Step 2 选择矫正方法（基于拓扑和金标签可用性），Step 3 发出 FWL 不变性警告。

问题在于 Algorithm 1 被放在了附录最后一页，主文中仅在 Section 4.5 (page 8) 最后一句间接引用。建议在 Section 4.3 或 4.5 中至少用 2-3 行总结 Algorithm 1 的核心逻辑，或将 Algorithm 1 移入正文（如果页面允许）。

---

**[AGREE] R2-W2: NLP 任务覆盖面有限——与我的 W3 一致**

同意。补充一点：4 个 LLM 均为中大规模（Llama-4-Maverick, Qwen2.5-23B, DeepSeek-Chat, Qwen2.7-TIL），缺少小模型（<7B）的数据。小模型的混淆矩阵可能有更极端的对角线偏离，这可能改变 ASV 排序的稳定性。

---

**[AGREE] R2-W3: 2.1% sign reversal 率的呈现可能误导——这是我审稿中遗漏的有效观察**

R2 此条指出了一个我未充分关注的呈现问题。Abstract 中 "the observed sign reversal rate is 2.1%" 确实是跨所有拓扑×系数的聚合数字。而论文自身的数据显示拓扑间差异极大：

- Section 3.2 (page 5): IV 拓扑下 52.6% 的 K=3 exposure 配置产生 sign reversal
- Section 4.4 (page 8): 14/23 configurations (61%) 在所有 secondary coefficients 上 exhibit sign reversal（exposure 拓扑）
- Table 1 (page 7): Sign-flip ASV 从 1.1-4.7 (fragile, IV) 到 ∞ (immense, M-bias)

2.1% 之所以低，是因为 primary coefficients 从不反转，且 non-exposure 拓扑的 sign-flip 率很低，拉低了整体均值。R2 建议报告 range（"from near-zero for confounding to over 40% for IV"）是一个很好的改进建议，能更准确地传达论文的核心发现。

---

**[AGREE] R2-W4: Conjecture 1 理论完成度——与我的 W1 一致**

同意。补充：论文在 Appendix B.11 (page 25) 用 Dirichlet(1,...,1) 对 K∈{3,5,7} 做了 30,000 矩阵的验证，worst-case violation 仅 0.013。这说明 Conjecture 1 在数值上非常接近成立。论文如果能讨论证明障碍（例如 K≥3 列随机矩阵的谱性质不再保证特定的 convexity 结构），将显著提升理论贡献的完整性。

---

**[REBUT] R2-W5: sensitivity analysis 文献覆盖——论文已有足够定位，但可小幅改进**

R2 指出两点：(1) E-value vs ASV 区别未清楚阐述，(2) Lash et al. (2009) QBA 关系未讨论。

对于 (2)：论文在 Section 3 (page 3) 明确引用了 Lash et al. (2009)："The quantitative bias analysis framework of Lash et al. (2009) provides a complementary epidemiologic perspective"。所以 QBA 并非未讨论，只是讨论较简短。

对于 (1)：论文在 page 3 已定位 ASV 相对于 E-value 和 partial-R² bounds 的关系："Building on the sensitivity analysis tradition—E-values for unmeasured confounding (VanderWeele and Ding, 2017) and partial-R² bounds (Cinelli and Hazlett, 2020)—but reparametrizing for K×K misclassification matrices"。核心区别已隐含：E-value 量化 unmeasured confounding 的强度阈值，ASV 量化 misclassification 的容忍度。

但 R2 的观点有一定道理——这个区别可以用一句话更明确地说出来（如 "While E-values ask 'how strong must unmeasured confounding be to nullify the effect?', ASV asks 'how much misclassification can the estimate tolerate before sign reversal?'"）。这是一个可以通过小幅修改解决的 minor 问题，不应列为 Should-Fix。

**建议降为 Minor。**

---

### Minor

**[AGREE] P1**: Figure 2 y 轴标签确实偏小，提升可读性是合理建议。

**[AGREE] P2**: Table 1 的 ✗/✓ 在黑白打印下确实不易区分。建议改用文字标记（Yes/No）或不同填充模式。

**[AGREE] P3**: Section 3.2 拓扑间过渡确实较快。但考虑到 8 页限制下要覆盖 7 种拓扑，这种密度难以完全避免。page 1 脚注提到的 running example 和 Table 2 (page 19) 的 summary 有所帮助。

**[AGREE] P4**: 多标注者设定是一个合理的扩展方向。实践中常见 majority voting 或加权聚合，每种方法产生不同的 effective confusion matrix。论文的框架可以直接应用于聚合后的矩阵，但论文未讨论聚合过程本身引入的额外误差。值得在 Limitations 中一提。

**[AGREE] P5**: "plim"（probability limit）在计量经济学中标准，但 NLP/CL 读者可能不熟悉。建议首次出现时加括号定义。

**[REBUT] P6: Abstract "necessary" 并非过于绝对**

论文的证据支持这一声称：Figure 3 (page 8) 显示相同 F₁ 范围（0.618–0.690）内偏差变化 10×，Table 1 (page 7) 显示 sign-flip ASV 从 fragile 到 immense 的巨大差异。如果不考虑拓扑而仅关注准确率，研究者可能错误地认为高准确率足以保证有效推断——但 IV 拓扑在 F₁=0.69 时仍有 42.1% 偏差。"necessary" 在此语境下是合理的——它不是说拓扑分析是 *sufficient*，而是说不做拓扑分析就不能保证有效推断。

---

### 总结

与 R2 的 7 个 Should-Fix/Must-Fix 问题中，我对 6 个表示 [AGREE]（其中 R2-N1 同意内容但建议降级严重程度，R2-W5 建议降为 Minor），对 1 个表示 [REBUT]（R2-W5 文献覆盖和 P6 "necessary"）。

R2 提出的最有价值的新观察是 **R2-W3（2.1% 聚合数字掩盖拓扑差异）**，这是我自己审稿中遗漏的呈现问题，对论文的传播效果有实质影响。

R2 的整体评分 3.5 与我的评分一致。两位 Reviewer 共同关注的核心问题是：(1) 假设合理性在 LLM 场景中的论证，(2) K≥3 理论完整性，(3) 线性 SEM 的适用性。这些共识强化了这些问题作为修改重点的优先级。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 702 · 2026-05-23T02:54:42.977079+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 703 · 2026-05-23T02:54:45.595443+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 7 个 Should-Fix/Must-Fix 中 6 个 [AGREE]（其中 2 个建议降级严重程度），1 个 [REBUT]（R2-W5 文献覆盖）。R2-W3（2.1% 聚合数字掩盖拓扑差异）是我原始审稿中遗漏的有效观察。两位 Reviewer 在核心问题上高度一致：假设合理性、K≥3 理论完整性、线性 SEM 适用性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 704 · 2026-05-23T02:54:50.100610+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 79

## Round 79

10 recorded events


### User

_source line 705 · 2026-05-23T02:57:10.309055+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: 核心假设（非差异性 + 比例效应）的实证验证不足**

同意这是本文最核心的方法论弱点。补充以下观察：

1. **非差异性假设**：论文在 Appendix B.5 的 stress test 使用均匀 ε-perturbation（C' = renorm(C₀ + ε·Δ)，Δ ~ Uniform(-1,1)），这是一个对称的、无结构的扰动模型。但 LLM 的真实误差模式很可能是结构性的——例如，情感分析中 LLM 对中性/模糊文本的错误率远高于对极性明确文本的错误率，这使得 P(A*|A) 依赖于 Y（因为 Y 与文本特征相关）。论文的 stress test 未能捕捉这种 **content-dependent differential error**，R1 的批评精准。

2. **比例效应**：Appendix B.12（page 26）显示 λ(C) 越界率在 δ=0.1 时约 10%，independent f 时饱和于 ~23%，但 sign failure rate 始终低于 1%。这说明 **即使比例效应被违反，sign preservation 仍然 robust**——这一点 R1 未充分肯定。然而 R1 的建议（a）——用 23 个真实 LLM 混淆矩阵定量评估比例效应近似程度——是一个极好的建议，执行成本低且能显著增强论文的说服力。

3. 我在自己的审稿中将类似问题定位为 N2（线性 SEM 假设），但 R1 更精确地聚焦于 **假设的实证验证**（而非假设的泛化性），这个角度更有操作性。建议作者优先回应 R1 的具体建议 (a)(b)(c)。

---

### Should-Fix

**[AGREE] R1-W1: K≥3 理论基础不完整**

与我的 W4 高度重叠。补充一点：论文在 Section 3.3（page 5）将 Theorem 1（K=2 严格证明）到 Observation 1（K≥3 数值验证 20,000 次）再到 Conjecture 1（30,000 次验证 per K ∈ {3,5,7}）的降级处理是诚实的。但 R1 正确指出，对于一篇以理论分析为主要贡献的论文，核心性质止步于 conjecture 确实削弱了整体贡献。作者应至少讨论证明的技术障碍：K≥3 情况下混淆矩阵的自由度增长使得 Cauchy-Schwarz 类的 bounding 策略不再直接适用，还是存在潜在反例？

---

**[AGREE] R1-W2: 线性 SEM 假设与 NLP 实践的差距**

我在自己的审稿中将此列为 **N2 (critical)**，比 R1 的 should-fix 定级更高。理由：EMNLP 的核心读者群是 NLP 研究者，线性 SEM 与现代 NLP pipeline 的差距如果不在正文 Method 部分早期讨论就会严重影响论文的 venue fit。Appendix B.6（page 23）的 logistic DGP 验证和 B.13 的 FWL logistic 验证提供了有价值的稳健性证据，但正文中仅用一句话提及（Section 5, page 8："FWL invariance is specific to linear models"）。**建议将此问题从 should-fix 升级为 must-fix**。

---

**[AGREE] R1-W3: 实证验证的 LLM 配置多样性有限**

与我的 W2 一致。R1 具体指出缺少小模型 (<7B) 和大模型 (>70B) 的对比，这是一个有价值的补充。不同规模 LLM 的混淆矩阵结构可能系统性不同——小模型可能有更均匀的误差分布（接近随机猜测），而大模型可能有更结构化的误差模式。论文的 23 个配置均来自中等规模开源模型（Llama-4-Maverick, Qwen2.5-32B, DeepSeek-Chat, Qwen2.7-TL-Instruct），无法代表这种规模依赖的变异性。

---

**[AGREE] R1-W4: PPI++ 比较的公平性和数字一致性**

R1 提出的数字一致性问题（Section 4.5 中 "47.6%" vs Table 4 Grand mean）值得核实。我重新查阅了 page 8（Section 4.5）和 page 20（Table 4）：

- Section 4.5 正文明确写道 "PPI++ achieves the **highest grand-mean** RMSE reduction **(47.6%)**"
- 但 Table 4（page 20）的 Grand mean 行显示 PPI++ 列为 **17.0**

这两个数字之间存在明显的不一致。47.6% 可能是仅对 "protective topologies"（排除 M-bias、exposure、IV 等负面效果的拓扑）取平均，但正文使用 "grand-mean" 这一措辞暗示的是所有拓扑的全局平均。**这需要作者明确澄清**：如果 47.6% 是受限子集的平均，必须在正文中明确说明；如果是计算错误，必须修正。

R1 关于 correction method prerequisites 对比不够系统的批评也合理——Table 4 缺少一个清晰的列来标注每种方法所需的前提条件（gold labels、confusion matrix 估计、参数模型假设等）。

---

### Minor

**[AGREE] R1-m1: 符号密度高**

与我的 P5（"plim" 定义）和 P3（拓扑间过渡句不足）相关。Running example 是一个好建议，但在 8 页限制下可能难以实现。一个折中方案是在 Section 3.1 末尾加一个 1-2 行的 notation summary box。

---

**[AGREE] R1-m2: Figure 质量**

与我的 P1（Figure 2 y 轴标签过小）和 P2（Table 1 黑白打印可辨性）一致。R1 对 Figure 1 字体小的指出也是合理的——Figure 1 包含 7 个 DAG，每个 DAG 中的节点标签在打印时可能难以辨认。

---

**[REBUT] R1-m3: Table 2 应移至主文**

Table 2（page 19, Appendix A.9 "Summary of Conditions"）确实是一个有价值的总结表，但正文已经严格用满 8 页。在当前页面预算下，将 Table 2 移入主文需要删减其他内容（如压缩 Section 4.2 的拓扑分析或 Section 4.5 的校正讨论），这两者都比一个 summary table 更重要。**建议的折中方案**：在 Section 3.2 或 Proposition 1 之后加入一句更明确的引用，如 "Table 2 (Appendix) provides a unified summary of sufficient conditions for sign preservation across all seven topologies"，让读者更容易找到。

---

**[REBUT] R1-m4: "topology" 术语**

R1 认为 "topology" 在数学中有特定含义（拓扑学），可能造成歧义。但在因果推断文献中，"causal topology"/"DAG topology" 是常见的非正式用法，用于指代 DAG 的结构类型。Pearl (2009)、Hernán and Robins (2020) 等标准教科书都使用类似的用法。对于 EMNLP 的目标读者（包含大量 CSS 研究者），这个术语不会造成真正的混淆。此外，论文在 Figure 1 和 Section 3.1 中已经清楚地展示了 "topology" 指的是什么——7 种 DAG 结构。这是一个非实质性的术语偏好问题。

---

**[AGREE] R1-m5: Binarization collapse 应在主文提及**

Appendix B.1 的 binarization collapse 发现（K=3 到 binary 引入额外偏差变异 15x）在主文 Section 3.2（page 4, footnote 1 区域）仅有简要提及。R1 正确指出这个发现对实践有直接价值——很多 NLP 研究者出于简化目的将多分类任务二值化，但这个操作会改变偏差结构。建议在 Section 4.2 或 Section 5 中用 1 句话更明确地提醒读者 binarization 的风险。

---

### Questions

**[AGREE] R1-Q1: 23 个 LLM 混淆矩阵与 proportional effects 偏离程度**

与 R1-N1 的建议 (a) 一致。这是一个低成本、高价值的实证检验——作者已经有 23 个真实混淆矩阵，只需计算每个矩阵的 f 和 g 函数，然后评估 f/g 的变异系数即可量化比例效应的近似程度。

---

**[AGREE] R1-Q2: 是否存在可构造的混淆矩阵使 primary coefficient 反转？**

论文在 Section 4.4（page 8）报告 "the primary coefficient does not reverse in any tested configuration—an empirical regularity"，但未提供不可能性的理论证明。这是一个重要的理论问题：如果 primary coefficient reversal 在理论上不可能（对某些拓扑），这将大幅增强论文的贡献；如果只是在测试范围内未观测到，这个 regularity 的外推性值得质疑。

---

**[REBUT] R1-Q3: ASV 排序在不同 DGP 参数化下是否稳定？（部分反驳）**

R1 的问题在 Appendix B.10（page 25, "ASV Stability Across DGP Configurations"）已有部分回答。Table 9（page 25）展示了 ASV 在 5 种 DGP 配置下的排名稳定性：confounding 始终最 robust，IV 和 exposure 始终最 fragile。论文还报告 magnitude ASV 在 c ∈ {0.1, 0.5, 1.0, 2.0, 5.0} 范围内的变化模式一致。**因此 R1 的担忧已被部分回答**。

但 R1 的问题仍有未解答的层面：Table 9 只考虑了 alternating-sign 和 same-sign 两种系数模式（β 向量结构），没有覆盖更复杂的多变量交互效应场景。R1 的问题意在探查 ASV 在更极端参数化下是否会出现排名反转——这一点确实未被 B.10 充分覆盖。建议作者在 response 中承认这个边界条件。

---

**[AGREE] R1-Q4: Collider 的结构独特性在非线性 DGP + 线性估计时是否保持？**

这是一个有深度的问题。Collider 在线性 SEM 下的特殊性在于 conditioning on collider 引入的 Berkson-type bias 与 misclassification bias 的交互作用。在非线性 DGP（如 logistic 或 probit）下，collider bias 的结构可能不同，因为非线性 link function 可以将 collider conditioning 的影响放大或衰减。Appendix B.6（page 23）测试了 logistic DGP，但没有专门报告 collider 拓扑的结果——sign-flip rate table（page 23 Table）显示 collider 在 logistic DGP 下 sign-flip rate 为 0.000，与线性 SEM 一致，但仅测试了 K=3。**建议作者在 response 中提供 collider × logistic DGP 的更详细分析。**

---

**[AGREE] R1-Q5: PPI++ RMSE reduction 数字一致性**

与我在 R1-W4 中的分析一致。Section 4.5 正文报告 "grand-mean RMSE reduction (47.6%)"，Table 4 Grand mean 行显示 17.0。这两个数字不一致，作者必须澄清 47.6% 的计算口径——是否仅包含 protective topologies（confounding, mediation, collider, front-door），还是计算错误。

---

### 综合评价

R1 和我（R2）的审稿在以下问题上高度一致：
1. **假设验证不足**（R1-N1 ↔ 我的 N2）：线性 SEM + 非差异假设是核心限制
2. **K≥3 理论不完整**（R1-W1 ↔ 我的 W4）
3. **经验验证覆盖面有限**（R1-W3 ↔ 我的 W2）
4. **写作呈现的可达性**（R1-m1/m2 ↔ 我的 P1/P3/P5）

R1 的独特贡献在于：
- **比 R2 更深入地剖析了 proportional effects 假设**（R1-N1 的建议 (a) 是高价值低成本的实证检验）
- **PPI++ 数字不一致性**（R1-W4/Q5）是我遗漏的一个具体问题
- **Q2（primary coefficient reversal 的理论可能性）和 Q4（collider × 非线性 DGP）** 是有深度的理论问题

**我只在两个 minor 点上与 R1 存在分歧**：
- m3（Table 2 移入主文）——页面预算不允许，更明确的引用即可
- m4（"topology" 术语）——在因果推断文献中是标准用法，对目标读者不构成歧义

**总体判断**：R1 的审稿质量高，发现的问题与我的审稿互补。两份审稿共同指向的核心问题是 **假设的实践相关性验证不足**（非差异性、比例效应、线性 SEM），这是决定论文能否从 Borderline Conference 上升到 Conference 的关键。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-23T02:57:42.184936+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-23T02:57:42.888119+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T02:41:51.699286+00:00\", \"completed_at\": \"2026-05-23T02:41:55.363190+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-23T02:57:43.089344+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 709 · 2026-05-23T02:57:43.089829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-23T03:02:15.029711+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出实证验证范围偏窄。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 两位 Reviewer 共识：4 个开源 LLM 规模相近（缺 <7B 和 >70B），3 个数据集任务类型偏分类（缺序数标注），23 个配置不足以支撑 primary coefficient 普遍性声明。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 9\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。标记为 resolved。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。已在 Section 3.1 扩展讨论：violation pathways (outcome-conditional prompting, few-shot, RAG)、stress test 引导 (ε up to 0.50)、诊断建议。EXP-3 realistic ε estimation 已完成并写入 Appendix。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 再次提出。核心批评：Appendix B.5 的均匀 ε-perturbation 无法捕捉 LLM 的结构性差异误差（如 content-dependent differential error）。论文缺乏实证证据证明 non-differential 假设在 LLM 场景中近似成立。R1 建议设计 LLM 特异性的差异性误分类测试（如按 outcome 分层估计条件混淆矩阵）。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.1 扩展 non-differential 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 9\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。标记为 resolved。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出 Abstract 数字密度过高。R1 REBUT。分歧点，保持现状。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W3：Abstract 中 2.1% sign reversal 是跨拓扑聚合数字，掩盖 topology-specific 风险差异（IV 42.1% vs confounding 0%），与论文 topology-dependent 核心主张矛盾。R1 AGREE，认为是自己遗漏的有效观察。共识：建议报告 range 或加限定语。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：应聚焦 monotonicity 非平凡性作为核心方法论贡献。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 共识：定位为 'systematic application with non-trivial reduction theorem'。已在 method.tex 和 intro.tex 中调整措辞（framework→diagnostics, 突出 K²→1D 降维非平凡性）。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W1 再次提出 ASV 可操作性（actionability）不足：缺少端到端使用场景（confusion matrix → topology → ASV → correction decision），Algorithm 1 在 Appendix 最后一页与主文 ASV 连接不紧。R1 AGREE 但指出 Algorithm 1 已部分回应，建议在主文总结 Algorithm 1 核心逻辑。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics + 突出 K²→1D 降维\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"MINOR——添加 appendix pointer 即可。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未提及。Section 4.4 已有 'For protective topologies, correction re-exposes the original bias pathway' 解释。\"\n    resolution: \"Section 4.4 已解释 protective topology 上 correction 有害的机制。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8-R2 格式合规检查通过。\"\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求 Abstract 标注 'empirical regularity' + sufficient condition。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 继续要求降低声称。Abstract 已改为 'concentrated in secondary coefficients with small effect sizes'，不再显式声称 primary never reverses。Conclusion 已标注 'empirical regularity driven by magnitude dominance rather than algebraic structure'。\"\n      - round: 9\n        reviewers: [R1]\n        note: \"R9-R1-Q2 询问是否存在可构造的混淆矩阵使 primary coefficient 反转。R2 AGREE 这是重要理论问题：如果理论上不可能则增强贡献，如果仅是未观测到则外推性可疑。当前措辞已降级为 empirical regularity，但理论边界仍未明确。\"\n    action_items:\n      - round: 8\n        action: \"Abstract 进一步降级 primary coefficient claim\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R5-N3 合并跟踪。Abstract 已不再使用 'structural property'，改为 'concentrated in secondary coefficients'。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未单独提及。Abstract 当前措辞合理。与 R5-N3 合并跟踪。\"\n    action_items:\n      - round: 8\n        action: \"与 R5-N3 合并处理——已降级\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"要求 NLP 场景合理性讨论 + Appendix A.4 引用。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"升为 CRITICAL。已在 method.tex Theorem 1 后报告 15-17% failure rate + NLP plausibility 讨论。EXP-1 fine-grained breakdown 已完成并写入 Appendix。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 再次提出。R1-N1 核心批评：论文未论证 LLM 混淆矩阵为何应满足比例效应。Appendix B.12 的 23% 越界率说明假设经常被违反。R2 补充：sign failure rate 始终低于 1%，但 R1 建议用 23 个真实混淆矩阵定量评估比例效应近似程度（f/g 变异系数），这是低成本高价值检验。两位共识。\"\n    action_items:\n      - round: 8\n        action: \"报告 general case 统计 + NLP 例子\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。EXP-2 FWL N-scaling 实验已完成：logistic 下 covariate topologies bias reduction <0.05%，exposure 22-75%。写入 Appendix sec:fwl_nonlinear。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 两位共识升为 CRITICAL。论文正文仅用一句话提及 logistic DGP 结果（Section 5）。R2-N2：EMNLP 读者需要正文早期解释为何从线性 SEM 出发 + 将 Appendix B.6/B.13 核心结论提升到正文。R1-W2：logistic 仍是简单非线性，NLP 实践中更复杂模型（transformer-based, double ML）的适用性未讨论。R1 AGREE R2 的 critical 定级。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并跟踪。已在 method.tex 和 intro.tex 调整措辞。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W5 再次提出 E-value vs ASV 区别未充分阐述。R1 REBUT：论文 page 3 已有定位（reparametrizing for K×K annotation error），Lash et al. (2009) QBA 已引用。R1 建议降为 minor，可用一句话更明确说明区别。\"\n    action_items:\n      - round: 8\n        action: \"与 R4-W6 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"升为 CRITICAL（与 R8-C1 合并跟踪）。method.tex 已添加三级层次显式说明 + K≥3 ASV 理论地位讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 两位共识：K≥3 理论止步于 conjecture 削弱整体贡献。论文标注诚实，但应讨论证明技术障碍（K≥3 列随机矩阵自由度增长使 bounding 策略失效？还是存在潜在反例？）。R2 补充：worst-case violation 仅 0.013，数值上接近成立。\"\n    action_items:\n      - round: 8\n        action: \"与 R8-C1 合并处理——已添加 K≥3 理论地位讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: []\n        note: \"已扩展到 ε ∈ {0.00, 0.01, 0.05, 0.10, 0.20, 0.30, 0.50}。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未单独提出 ε 覆盖不足。\"\n    resolution: \"Stress test 已覆盖 ε up to 0.50 (7 values)，method.tex 引导 Appendix B.5。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"R8-R1-W4 指出 Collider Amplification=100% 与 protective 描述矛盾。已在 Table 1 caption 添加脚注澄清：Collider 100% amplification reflects Berkson bias from conditioning, not error amplification。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未提及。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名与数值验证性质不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 选择的敏感性未充分分析\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"升为 MAJOR（与 R8-W3 合并跟踪）。已在 method.tex 分 topology 讨论 δ* precision。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及 δ* precision。method.tex 的分 topology 讨论似乎已缓解此问题。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 中 83.4% sign reversal 呈现顺序有误导性\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"Section 4.2 已重排：先 realistic accuracy (2.1%)，再 Dirichlet (83.4%)。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"Introduction '154×' binarization bias 倍数来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加说明来源。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Wei et al. 2025, Demirel et al. 2024）\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"Demirel et al. (2024) 已引用。Wei et al. 2025 未找到（不存在），跳过。\"\n    resolution: \"Demirel et al. (2024) 已引用。Wei et al. 2025 不存在，MINOR 跳过。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 的 risk threshold (0.1) 缺乏选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未提及。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 issues ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力——ASV 在 K≥3 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N1 首发 CRITICAL，R2 AGREE。已在 method.tex Section 3.3 添加显式讨论：分 topology 的 δ* precision 分析（steep η vs shallow η），IV/exposure 推荐 Bootstrap CI，topology ranking preserved。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 继续提出。R1-W1：K≥3 是 NLP 主要场景，但 Theorem 1 仅覆盖 K=2，ASV 和 Algorithm 1 的实用指导依赖未证明结果。R2-W4：核心性质止步 conjecture 削弱理论贡献。两位共识应讨论证明障碍。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 显式讨论 K≥3 下 ASV 理论地位 + δ* precision 定量分析\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N2 首发 CRITICAL，R2 AGREE。已在 method.tex Theorem 1 后报告 15-17% failure rate，添加 NLP plausibility 讨论 + ASV 作为替代诊断建议。EXP-1 fine-grained breakdown 已完成并写入 Appendix sec:proportional_effects。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9-R1-N1 再次将此与 non-differential 假设合并提出为核心批评。R2 补充：即使比例效应被违反，sign failure rate 始终 <1%，说明 sign preservation 仍 robust。但 R1 建议用 23 个真实混淆矩阵定量评估 f/g 变异系数。两位共识此建议高价值低成本。\"\n    action_items:\n      - round: 8\n        action: \"method.tex 报告 general case 统计 + NLP 例子\"\n        assigned_to: agent\n        status: done\n      - round: 8\n        action: \"EXP-1 proportional effects fine-grained breakdown 实验\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV 与 E-values/partial R² 的方法论差异界定不足——contribution 定位需调整\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R2-W1 MAJOR。已调整：intro.tex Contribution 2 改为 'diagnostics'，method.tex Section 3.3 突出 K²→1D 降维非平凡性和 topology-dependent threshold behavior。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W1：ASV 可操作性不足——缺端到端 walkthrough。R1 AGREE 但指出 Algorithm 1 已部分回应。共识：在主文简要总结 Algorithm 1 逻辑，或增加 practitioner walkthrough。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位从 'framework' 调整为 'diagnostics with non-trivial reduction'\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"强共识。已在 method.tex Section 3.1 扩展讨论：具体 violation pathways、stress test 引导、诊断建议。EXP-3 realistic ε estimation 已完成：K=2 immune (safe ε=0.50)，K≥3 exposure sharply fragile (14/16 configs safe ε=0)。结果写入 Appendix sec:realistic_epsilon + method.tex 交叉引用。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 再次提出为 R1-N1 核心批评的一部分。核心增量批评：Appendix B.5 的均匀 ε-perturbation 是对称无结构的，无法捕捉 LLM 的 content-dependent differential error 模式（如 LLM 对情感极性明确文本更准确）。R1 建议按 outcome 分层估计条件混淆矩阵 P(A*|A,Y=y)。论文缺乏任何实证证据证明 non-differential 假设在 LLM 场景中近似成立。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.1 扩展 non-differential 讨论段落\"\n        assigned_to: agent\n        status: done\n      - round: 8\n        action: \"EXP-3 realistic ε estimation 从 23 LLM configs\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽，对 IV/exposure 拓扑 relative uncertainty >100%\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-W3 MAJOR。已在 method.tex 分 topology 讨论 δ* precision：steep η topologies (confounding/mediation/front-door) precision <0.12，shallow η (exposure/IV) 推荐 Bootstrap CI + topology ranking。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及。method.tex 的分 topology 讨论和 Bootstrap CI 推荐似乎已缓解。\"\n    action_items:\n      - round: 8\n        action: \"method.tex 分 topology 讨论 δ* precision + Bootstrap CI 推荐\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Rosenbaum (2002) 和 Ding & VanderWeele (2016)\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"Ding & VanderWeele (2016) 已添加到 related_work.tex。Rosenbaum (2002) 被 R1 认为合理但非必需，暂不添加。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及缺失引用。R2 格式合规检查通过，引用覆盖面良好。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele (2016)\"\n        assigned_to: agent\n        status: done\n\n  # === Round 9 新发现 ===\n\n  - id: R9-N1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需更精确限定——承认 Brenner (1993)、Teblunthuis (2024)、Ogburn & VanderWeele (2012) 等先驱工作\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R2]\n        note: \"R2-N1 列为 critical，R1 AGREE 内容但建议降为 should-fix（论文新颖性不依赖 'first' 措辞）。共识：建议修改为 'first unified analysis across seven topologies' 并在 Section 1 贡献列表中明确 'building on' 先驱工作。\"\n\n  - id: R9-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 中 2.1% sign reversal 聚合数字掩盖拓扑间巨大差异，与 topology-dependent 核心主张矛盾\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R2-W3 首发，R1 AGREE（称之为自己遗漏的有效观察）。IV 42.1% vs confounding 0%，2.1% 因 primary coefficient 不反转 + non-exposure 拓扑拉低。建议在 Abstract 报告 range 或加 'across all topologies' 限定。\"\n\n  - id: R9-W2\n    category: experiments\n    severity: should-fix\n    summary: \"PPI++ grand-mean RMSE reduction 数字不一致：Section 4.5 正文 47.0%/47.6% vs Table 4 Grand mean 17.0\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R1-W4/Q5 首发，R2 交叉回应确认。Section 4.5 'grand-mean RMSE reduction (47.0%)' 与 Table 4 Grand mean 行 PPI++ 列 17.0 不一致。47.0% 可能是受限子集平均（排除负效果拓扑），但正文使用 'grand-mean' 暗示全局平均。作者必须澄清计算口径或修正数字。\"\n\n  - id: R9-P1\n    category: presentation\n    severity: minor\n    summary: \"Figure/Table 可读性：Figure 1 字体小、Figure 2 y 轴标签小 + 红绿配色对色觉障碍不友好、Table 1 ✗/✓ 黑白打印难区分\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"两位共识。建议增大字号、改用色觉友好配色、Table 1 用文字标记替代符号。\"\n\n  - id: R9-P2\n    category: presentation\n    severity: minor\n    summary: \"'plim' 记号对 NLP 读者不常见，首次出现应加定义\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R2-P5 首发，R1-m1 相关（符号密度高）。probability limit 在计量经济学标准但 NLP/CL 读者可能不熟悉。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出实证验证范围偏窄。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 两位 Reviewer 共识：4 个开源 LLM 规模相近（缺 <7B 和 >70B），3 个数据集任务类型偏分类（缺序数标注），23 个配置不足以支撑 primary coefficient 普遍性声明。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 9\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。标记为 resolved。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。已在 Section 3.1 扩展讨论：violation pathways (outcome-conditional prompting, few-shot, RAG)、stress test 引导 (ε up to 0.50)、诊断建议。EXP-3 realistic ε estimation 已完成并写入 Appendix。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 再次提出。核心批评：Appendix B.5 的均匀 ε-perturbation 无法捕捉 LLM 的结构性差异误差（如 content-dependent differential error）。论文缺乏实证证据证明 non-differential 假设在 LLM 场景中近似成立。R1 建议设计 LLM 特异性的差异性误分类测试（如按 outcome 分层估计条件混淆矩阵）。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.1 扩展 non-differential 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 9\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。标记为 resolved。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出 Abstract 数字密度过高。R1 REBUT。分歧点，保持现状。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W3：Abstract 中 2.1% sign reversal 是跨拓扑聚合数字，掩盖 topology-specific 风险差异（IV 42.1% vs confounding 0%），与论文 topology-dependent 核心主张矛盾。R1 AGREE，认为是自己遗漏的有效观察。共识：建议报告 range 或加限定语。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：应聚焦 monotonicity 非平凡性作为核心方法论贡献。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 共识：定位为 'systematic application with non-trivial reduction theorem'。已在 method.tex 和 intro.tex 中调整措辞（framework→diagnostics, 突出 K²→1D 降维非平凡性）。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W1 再次提出 ASV 可操作性（actionability）不足：缺少端到端使用场景（confusion matrix → topology → ASV → correction decision），Algorithm 1 在 Appendix 最后一页与主文 ASV 连接不紧。R1 AGREE 但指出 Algorithm 1 已部分回应，建议在主文总结 Algorithm 1 核心逻辑。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics + 突出 K²→1D 降维\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"MINOR——添加 appendix pointer 即可。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。\"\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未提及。Section 4.4 已有 'For protective topologies, correction re-exposes the original bias pathway' 解释。\"\n    resolution: \"Section 4.4 已解释 protective topology 上 correction 有害的机制。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题：workshop paper 未标注，preprint 状态未确认\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8-R2 格式合规检查通过。\"\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求 Abstract 标注 'empirical regularity' + sufficient condition。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 继续要求降低声称。Abstract 已改为 'concentrated in secondary coefficients with small effect sizes'，不再显式声称 primary never reverses。Conclusion 已标注 'empirical regularity driven by magnitude dominance rather than algebraic structure'。\"\n      - round: 9\n        reviewers: [R1]\n        note: \"R9-R1-Q2 询问是否存在可构造的混淆矩阵使 primary coefficient 反转。R2 AGREE 这是重要理论问题：如果理论上不可能则增强贡献，如果仅是未观测到则外推性可疑。当前措辞已降级为 empirical regularity，但理论边界仍未明确。\"\n    action_items:\n      - round: 8\n        action: \"Abstract 进一步降级 primary coefficient claim\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem——命名不严谨\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R5-N3 合并跟踪。Abstract 已不再使用 'structural property'，改为 'concentrated in secondary coefficients'。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未单独提及。Abstract 当前措辞合理。与 R5-N3 合并跟踪。\"\n    action_items:\n      - round: 8\n        action: \"与 R5-N3 合并处理——已降级\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制，主文讨论不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"要求 NLP 场景合理性讨论 + Appendix A.4 引用。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"升为 CRITICAL。已在 method.tex Theorem 1 后报告 15-17% failure rate + NLP plausibility 讨论。EXP-1 fine-grained breakdown 已完成并写入 Appendix。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 再次提出。R1-N1 核心批评：论文未论证 LLM 混淆矩阵为何应满足比例效应。Appendix B.12 的 23% 越界率说明假设经常被违反。R2 补充：sign failure rate 始终低于 1%，但 R1 建议用 23 个真实混淆矩阵定量评估比例效应近似程度（f/g 变异系数），这是低成本高价值检验。两位共识。\"\n    action_items:\n      - round: 8\n        action: \"报告 general case 统计 + NLP 例子\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch——非线性验证不足\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未显式提及。EXP-2 FWL N-scaling 实验已完成：logistic 下 covariate topologies bias reduction <0.05%，exposure 22-75%。写入 Appendix sec:fwl_nonlinear。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 两位共识升为 CRITICAL。论文正文仅用一句话提及 logistic DGP 结果（Section 5）。R2-N2：EMNLP 读者需要正文早期解释为何从线性 SEM 出发 + 将 Appendix B.6/B.13 核心结论提升到正文。R1-W2：logistic 仍是简单非线性，NLP 实践中更复杂模型（transformer-based, double ML）的适用性未讨论。R1 AGREE R2 的 critical 定级。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并跟踪。已在 method.tex 和 intro.tex 调整措辞。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W5 再次提出 E-value vs ASV 区别未充分阐述。R1 REBUT：论文 page 3 已有定位（reparametrizing for K×K annotation error），Lash et al. (2009) QBA 已引用。R1 建议降为 minor，可用一句话更明确说明区别。\"\n    action_items:\n      - round: 8\n        action: \"与 R4-W6 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Shu & Yi 2019 两篇、Cadei et al. 2025、Neuhaus 1999）\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"升为 CRITICAL（与 R8-C1 合并跟踪）。method.tex 已添加三级层次显式说明 + K≥3 ASV 理论地位讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 两位共识：K≥3 理论止步于 conjecture 削弱整体贡献。论文标注诚实，但应讨论证明技术障碍（K≥3 列随机矩阵自由度增长使 bounding 策略失效？还是存在潜在反例？）。R2 补充：worst-case violation 仅 0.013，数值上接近成立。\"\n    action_items:\n      - round: 8\n        action: \"与 R8-C1 合并处理——已添加 K≥3 理论地位讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 7\n        reviewers: []\n        note: \"已扩展到 ε ∈ {0.00, 0.01, 0.05, 0.10, 0.20, 0.30, 0.50}。\"\n      - round: 8\n        reviewers: []\n        note: \"R8 未单独提出 ε 覆盖不足。\"\n    resolution: \"Stress test 已覆盖 ε up to 0.50 (7 values)，method.tex 引导 Appendix B.5。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义在 caption 中未解释\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"R8-R1-W4 指出 Collider Amplification=100% 与 protective 描述矛盾。已在 Table 1 caption 添加脚注澄清：Collider 100% amplification reflects Berkson bias from conditioning, not error amplification。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未提及。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名与数值验证性质不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 选择的敏感性未充分分析\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"升为 MAJOR（与 R8-W3 合并跟踪）。已在 method.tex 分 topology 讨论 δ* precision。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及 δ* precision。method.tex 的分 topology 讨论似乎已缓解此问题。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 中 83.4% sign reversal 呈现顺序有误导性\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"Section 4.2 已重排：先 realistic accuracy (2.1%)，再 Dirichlet (83.4%)。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"Introduction '154×' binarization bias 倍数来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加说明来源。R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用（Wei et al. 2025, Demirel et al. 2024）\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"Demirel et al. (2024) 已引用。Wei et al. 2025 未找到（不存在），跳过。\"\n    resolution: \"Demirel et al. (2024) 已引用。Wei et al. 2025 不存在，MINOR 跳过。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 的 risk threshold (0.1) 缺乏选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 7\n    mentions:\n      - round: 8\n        reviewers: []\n        note: \"R8 未提及。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 issues ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力——ASV 在 K≥3 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N1 首发 CRITICAL，R2 AGREE。已在 method.tex Section 3.3 添加显式讨论：分 topology 的 δ* precision 分析（steep η vs shallow η），IV/exposure 推荐 Bootstrap CI，topology ranking preserved。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 继续提出。R1-W1：K≥3 是 NLP 主要场景，但 Theorem 1 仅覆盖 K=2，ASV 和 Algorithm 1 的实用指导依赖未证明结果。R2-W4：核心性质止步 conjecture 削弱理论贡献。两位共识应讨论证明障碍。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 显式讨论 K≥3 下 ASV 理论地位 + δ* precision 定量分析\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-N2 首发 CRITICAL，R2 AGREE。已在 method.tex Theorem 1 后报告 15-17% failure rate，添加 NLP plausibility 讨论 + ASV 作为替代诊断建议。EXP-1 fine-grained breakdown 已完成并写入 Appendix sec:proportional_effects。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9-R1-N1 再次将此与 non-differential 假设合并提出为核心批评。R2 补充：即使比例效应被违反，sign failure rate 始终 <1%，说明 sign preservation 仍 robust。但 R1 建议用 23 个真实混淆矩阵定量评估 f/g 变异系数。两位共识此建议高价值低成本。\"\n    action_items:\n      - round: 8\n        action: \"method.tex 报告 general case 统计 + NLP 例子\"\n        assigned_to: agent\n        status: done\n      - round: 8\n        action: \"EXP-1 proportional effects fine-grained breakdown 实验\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV 与 E-values/partial R² 的方法论差异界定不足——contribution 定位需调整\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R2-W1 MAJOR。已调整：intro.tex Contribution 2 改为 'diagnostics'，method.tex Section 3.3 突出 K²→1D 降维非平凡性和 topology-dependent threshold behavior。\"\n      - round: 9\n        reviewers: [R2]\n        note: \"R9-R2-W1：ASV 可操作性不足——缺端到端 walkthrough。R1 AGREE 但指出 Algorithm 1 已部分回应。共识：在主文简要总结 Algorithm 1 逻辑，或增加 practitioner walkthrough。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位从 'framework' 调整为 'diagnostics with non-trivial reduction'\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 9\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"强共识。已在 method.tex Section 3.1 扩展讨论：具体 violation pathways、stress test 引导、诊断建议。EXP-3 realistic ε estimation 已完成：K=2 immune (safe ε=0.50)，K≥3 exposure sharply fragile (14/16 configs safe ε=0)。结果写入 Appendix sec:realistic_epsilon + method.tex 交叉引用。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R9 再次提出为 R1-N1 核心批评的一部分。核心增量批评：Appendix B.5 的均匀 ε-perturbation 是对称无结构的，无法捕捉 LLM 的 content-dependent differential error 模式（如 LLM 对情感极性明确文本更准确）。R1 建议按 outcome 分层估计条件混淆矩阵 P(A*|A,Y=y)。论文缺乏任何实证证据证明 non-differential 假设在 LLM 场景中近似成立。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.1 扩展 non-differential 讨论段落\"\n        assigned_to: agent\n        status: done\n      - round: 8\n        action: \"EXP-3 realistic ε estimation 从 23 LLM configs\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽，对 IV/exposure 拓扑 relative uncertainty >100%\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R1-W3 MAJOR。已在 method.tex 分 topology 讨论 δ* precision：steep η topologies (confounding/mediation/front-door) precision <0.12，shallow η (exposure/IV) 推荐 Bootstrap CI + topology ranking。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未显式提及。method.tex 的分 topology 讨论和 Bootstrap CI 推荐似乎已缓解。\"\n    action_items:\n      - round: 8\n        action: \"method.tex 分 topology 讨论 δ* precision + Bootstrap CI 推荐\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Rosenbaum (2002) 和 Ding & VanderWeele (2016)\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 8\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"Ding & VanderWeele (2016) 已添加到 related_work.tex。Rosenbaum (2002) 被 R1 认为合理但非必需，暂不添加。\"\n      - round: 9\n        reviewers: []\n        note: \"R9 未提及缺失引用。R2 格式合规检查通过，引用覆盖面良好。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele (2016)\"\n        assigned_to: agent\n        status: done\n\n  # === Round 9 新发现 ===\n\n  - id: R9-N1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需更精确限定——承认 Brenner (1993)、Teblunthuis (2024)、Ogburn & VanderWeele (2012) 等先驱工作\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R2]\n        note: \"R2-N1 列为 critical，R1 AGREE 内容但建议降为 should-fix（论文新颖性不依赖 'first' 措辞）。共识：建议修改为 'first unified analysis across seven topologies' 并在 Section 1 贡献列表中明确 'building on' 先驱工作。\"\n\n  - id: R9-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 中 2.1% sign reversal 聚合数字掩盖拓扑间巨大差异，与 topology-dependent 核心主张矛盾\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R2-W3 首发，R1 AGREE（称之为自己遗漏的有效观察）。IV 42.1% vs confounding 0%，2.1% 因 primary coefficient 不反转 + non-exposure 拓扑拉低。建议在 Abstract 报告 range 或加 'across all topologies' 限定。\"\n\n  - id: R9-W2\n    category: experiments\n    severity: should-fix\n    summary: \"PPI++ grand-mean RMSE reduction 数字不一致：Section 4.5 正文 47.0%/47.6% vs Table 4 Grand mean 17.0\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R1-W4/Q5 首发，R2 交叉回应确认。Section 4.5 'grand-mean RMSE reduction (47.0%)' 与 Table 4 Grand mean 行 PPI++ 列 17.0 不一致。47.0% 可能是受限子集平均（排除负效果拓扑），但正文使用 'grand-mean' 暗示全局平均。作者必须澄清计算口径或修正数字。\"\n\n  - id: R9-P1\n    category: presentation\n    severity: minor\n    summary: \"Figure/Table 可读性：Figure 1 字体小、Figure 2 y 轴标签小 + 红绿配色对色觉障碍不友好、Table 1 ✗/✓ 黑白打印难区分\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"两位共识。建议增大字号、改用色觉友好配色、Table 1 用文字标记替代符号。\"\n\n  - id: R9-P2\n    category: presentation\n    severity: minor\n    summary: \"'plim' 记号对 NLP 读者不常见，首次出现应加定义\"\n    status: open\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"R2-P5 首发，R1-m1 相关（符号密度高）。probability limit 在计量经济学标准但 NLP/CL 读者可能不熟悉。\""
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-23T03:02:15.080906+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 27140}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-23T03:04:33.797709+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n\n**Venue**: EMNLP 2026 (ARR May Cycle) | **类型**: Long Paper | **Round**: 9 (Fresh)\n**Reviewers**: R1 (方法严谨性+实验验证), R2 (新颖性+完整性+写作呈现)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class 非差异误分类在因果推断中的传播，核心发现是传播方式取决于 DAG 拓扑而非标注准确率。论文为 7 种标准 DAG 拓扑推导闭式偏差表达式，证明 K≥3 引入 K=2 不存在的 sign reversal 可能性（exposure 83.4%、IV 52.6%），提出 Annotation Sensitivity Values (ASV) 诊断框架（含 magnitude/significance/sign-flip 三种度量），并证明 FWL 不变性使矩阵校正对 4 种协变量拓扑无效。通过 100,000 随机矩阵和 23 个真实 LLM 混淆矩阵验证。\n\n---\n\n## Strengths\n\n1. **问题定义的新颖性和时效性**：首次在统一框架下对 7 种 DAG 拓扑 × K-class 误分类推导闭式偏差表达式并进行跨拓扑对比，填补了 NLP×因果推断文献中的空白。[R1, R2 共识]\n\n2. **\"拓扑 > 准确率\"的反直觉洞见**：在 F₁ 0.614-0.690 范围内偏差变化 10×（IV 42.1% vs collider <5.6%），挑战了\"提高标注准确率即可解决下游问题\"的常见假设。[R1, R2 共识]\n\n3. **K=2 理论的严谨性**：Theorem 1 的单调性证明结构完整（凸性 + 端点条件），Proposition 1 的 sign preservation 对 confounding/collider 给出解析证明，证明路径有独立方法论价值。[R1 主导]\n\n4. **理论结果的诚实分层**：明确区分 Theorem（证明）→ Proposition（部分证明）→ Observation（数值验证）→ Conjecture（猜想）四级层次，学术诚信度高。[R1, R2 共识]\n\n5. **FWL 不变性的否定结果**：证明 matrix-based correction 对 4 个协变量拓扑 provably ineffective，帮助研究者避免无效纠偏策略——一个有实用价值的否定结论。[R1, R2 共识]\n\n6. **丰富的附录**：20 页附录包含完整证明、多个稳健性检验（non-differential stress test、cross-K、logistic DGP、bootstrap uncertainty），显著增强可信度和可复现性。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### CRITICAL\n\n**C1. 核心假设在 LLM 场景中缺乏实证验证** [R1-N1, R2 AGREE]\n\n论文框架建立在两个关键假设上——(1) 非差异性误分类 P(A*|A,Y,Z)=P(A*|A)，(2) proportional effects (f=λg)——但未提供任何实证证据表明这些假设在 LLM 标注场景中近似成立。\n\n- **非差异性**：Appendix B.5 的 stress test 使用均匀 ε-perturbation，无法捕捉 LLM 的结构性差异误差（如 content-dependent differential error：LLM 对情感极性明确文本更准确，导致 P(A*|A) 依赖于 Y）。论文缺乏按 outcome 分层估计条件混淆矩阵 P(A*|A,Y=y) 的实证检验。\n- **比例效应**：Appendix B.12 显示 λ(C) 越界率在独立 f 时饱和于 ~23%，但论文未论证 LLM 混淆矩阵为何应满足比例效应。R2 补充：即使违反，sign failure rate 始终 <1%，说明 sign preservation 仍 robust。但 R1 建议用 23 个真实混淆矩阵定量评估 f/g 变异系数——这是低成本高价值的检验。\n\n**C2. 线性 SEM 假设对 EMNLP 读者的可达性和泛化性严重不足** [R2-N2, R1-W2, 交叉后共识升为 CRITICAL]\n\n论文正文仅用一句话提及 logistic DGP 结果（Section 5）。对于 EMNLP 的核心读者群（NLP 研究者），线性 SEM 与现代 NLP pipeline 的差距如果不在 Method 部分早期讨论，会严重影响 venue fit。Appendix B.6（logistic DGP sign-flip 稳定性）和 B.13（FWL logistic 验证）提供了有价值的稳健性证据，但被藏在附录中。建议在 Section 3.1 增加 1-2 句解释为何从线性 SEM 出发，并将 B.6/B.13 核心结论提升到正文。\n\n### MAJOR\n\n**M1. K≥3 理论基础不完整，而 K≥3 是 NLP 的主要应用场景** [R1-W1, R2-W4, 共识]\n\nK=2 理论严格，但 K≥3（NLP 绝大多数任务的场景）的核心性质——envelope monotonicity——止步于 Observation 1（20,000 次数值验证）和 Conjecture 1（30,000 矩阵/topology），ASV 框架和 Algorithm 1 的实用指导依赖这些未证明的结果。论文标注诚实，但应讨论证明的技术障碍：是 K≥3 列随机矩阵的谱性质不再保证 convexity 结构，还是存在潜在反例？\n\n**M2. ASV 框架的可操作性（actionability）展示不足** [R2-W1, R1 AGREE]\n\nASV 定位为 \"diagnostics\"，但缺少端到端使用场景：从业者如何获取所需输入（C₀、DAG topology），如何解释三种 ASV 数值，如何据此决策？Algorithm 1 在 Appendix 最后一页，与主文 ASV 连接不紧。建议在主文用 2-3 行总结 Algorithm 1 核心逻辑，或增加 practitioner walkthrough。\n\n### SHOULD-FIX\n\n**S1. \"first to characterize\" novelty claim 需更精确限定** [R2-N1 critical → R1 建议降为 should-fix, 共识降级]\n\nBrenner (1993) 覆盖 polytomous confounder，Teblunthuis (2024) 覆盖单拓扑回归偏差，Ogburn & VanderWeele (2012) 覆盖 binary confounder 单调性。论文实际新颖性在于 7 拓扑 × K-class 的闭式联合对比。建议修改为 \"first unified analysis across seven topologies\" 并在 Section 1 贡献列表中明确 \"building on\" 先驱工作。R1 认为论文新颖性不依赖 \"first\" 措辞，降为 should-fix 合理。\n\n**S2. Abstract 中 2.1% sign reversal 聚合数字掩盖拓扑间差异** [R2-W3, R1 AGREE]\n\n2.1% 是跨所有拓扑×系数的平均值，而 IV 42.1%、exposure 83.4%（Dirichlet 下）。这个聚合数字恰恰掩盖了论文 \"topology-dependent\" 的核心主张。建议报告 range 或加限定语。\n\n**S3. 经验验证的 LLM 配置多样性有限** [R1-W3, R2-W2, 共识]\n\n4 个开源 LLM 规模相近（缺 <7B 和 >70B），3 个英文数据集任务类型偏分类（缺序数标注），23 个配置不足以支撑 primary coefficient 普遍性声明。建议增加不同规模/架构的 LLM 或讨论混淆矩阵参数空间覆盖度。\n\n**S4. PPI++ grand-mean RMSE reduction 数字不一致** [R1-W4/Q5, R2 确认]\n\nSection 4.5 正文报告 \"grand-mean RMSE reduction (47.0%)\"，但 Table 4 Grand mean 行 PPI++ 列为 17.0。作者必须澄清 47.0% 的计算口径（是否仅限 protective topologies）或修正数字。\n\n### MINOR\n\n- Figure 1 字体小、Figure 2 y 轴标签小 + 红绿配色对色觉障碍不友好、Table 1 ✗/✓ 黑白打印难区分 [R1, R2]\n- \"plim\"（probability limit）对 NLP 读者不常见，首次出现应加定义 [R1, R2]\n- Section 3.2 拓扑间过渡突然，符号密度高 [R1, R2]\n- Appendix B.1 binarization collapse（K=3→binary 引入 154× 额外偏差）在主文中提及不足 [R1]\n- 多标注者设定对 confusion matrix 估计的影响未讨论 [R2]\n- Appendix Table 2（sign preservation 充分条件总结）非常有价值，建议在主文更明确引用 [R1]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上高度一致（交叉回应中全部 [AGREE]）：\n\n1. **假设验证不足是核心瓶颈**：非差异性和比例效应假设在 LLM 场景中的合理性缺乏实证支持，这是论文从 Borderline 上升到 Conference 的关键障碍\n2. **K≥3 理论不完整**：对 NLP 主要应用场景的覆盖止步于数值验证和猜想\n3. **线性 SEM 讨论不足**：需在正文早期建立与 NLP 实践的连接\n4. **LLM 配置多样性有限**：规模和任务类型覆盖面需扩展\n5. **PPI++ 数字不一致**：需澄清或修正\n6. **2.1% 聚合数字有误导性**：应报告 range\n\n---\n\n## Reviewer Divergence\n\n仅在严重程度和 minor 点上存在分歧，无实质性矛盾：\n\n1. **R2-N1 (overclaiming) 严重程度**：R2 列为 critical，R1 建议降为 should-fix（论文新颖性不依赖 \"first\" 措辞）。→ 报告中采纳 should-fix。\n2. **R2-W5 (sensitivity analysis 文献覆盖)**：R2 列为 should-fix，R1 rebut（论文已引用 Lash et al. 2009 和定位 ASV vs E-value），建议降为 minor。→ 报告中采纳 minor。\n3. **R1-m3 (Table 2 移入主文)**：R2 rebut（页面预算不允许），建议更明确的交叉引用。→ 采纳 minor。\n4. **R1-m4 (\"topology\" 术语)**：R2 rebut（因果推断文献标准用法）。→ 不列入报告。\n\n---\n\n## Questions\n\n1. **[R1-Q1]** 能否用 23 个真实 LLM 混淆矩阵定量评估 proportional effects 近似程度（计算 f/g 变异系数）？[R2 AGREE: 低成本高价值]\n2. **[R1-Q2]** 是否存在可构造的混淆矩阵（满足 non-differential + 合理精度）使 primary coefficient 反转？如果存在需什么条件？[R2 AGREE: 理论边界问题]\n3. **[R1-Q3]** ASV 排序在不同 DGP 参数化（系数大小、误差方差）下是否稳定？Appendix B.10 部分回答（β alternating/same-sign），但未覆盖更复杂的多变量交互效应场景。[R2 部分 REBUT: B.10 已覆盖基本情况]\n4. **[R1-Q4]** Collider 的结构独特性在非线性 DGP + 线性估计时是否保持？Appendix B.6 中 collider logistic sign-flip 为 0.000 但仅测 K=3。[R2 AGREE: 需更详细分析]\n5. **[R1-Q5]** Section 4.5 PPI++ \"grand-mean RMSE reduction (47.0%)\" vs Table 4 Grand mean 17.0——请澄清。[R2 AGREE: 明确不一致]\n\n---\n\n## Missing References\n\n论文引用覆盖面总体良好。以下为可选补充（非必需）：\n- Bound, Brown, and Mathiowetz (2001) — 测量误差综述（已引用 Carroll et al. 2006）。低优先级。\n- VanderWeele (2015) — mediation 教材。低优先级。\n- 未发现 fabricated citations。引用格式符合 ACL natbib 规范。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。项目配置中外部审稿未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因速率限制出错（agent exited: rate limit hit），未完成实际 PDF 渲染审查。完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n\n**综合判断**：论文对一个重要且新颖的问题做出了实质性贡献。K=2 理论严格，\"拓扑 > 准确率\"洞见有概念和实践价值，FWL 不变性否定结果实用。但以下因素阻止了更高评分：\n\n1. **实践相关性缺口**：核心假设（非差异性、比例效应、线性 SEM）在 LLM 标注场景中的合理性未经实证验证，框架对目标用户（NLP 因果推断研究者）的可用性存疑\n2. **理论完整性缺口**：K≥3（NLP 主要场景）的核心性质止步于 conjecture\n3. **贡献偏增量**：各单项贡献（多分类偏差分析是经典测量误差理论的推广，ASV 是灵敏度分析工具的变体，FWL 不变性是已知定理的应用）的新颖性中等\n\n**从 Borderline 到 Conference 的关键路径**：\n- 用 23 个真实混淆矩阵定量评估 proportional effects 近似程度（Q1）\n- 在正文 Section 3.1 解释线性 SEM 选择动机 + 提升 B.6/B.13 核心结论\n- 修正 PPI++ 数字不一致\n- Abstract 中 2.1% 改为报告 topology-specific range\n\n**置信度**: 4/5（两位 Reviewer 仔细阅读正文+附录，交叉回应后高度一致）\n\n---\n\n## Detailed Comments\n\n### Abstract (page 1)\n- \"the sign reversal rate is 2.1%\" → 改为报告 topology-dependent range（如 \"0% for confounding to over 40% for IV under realistic accuracy\"），当前聚合数字与论文核心主张矛盾 [S2]\n- \"Topology-aware analysis is necessary\" → R2 认为过于绝对（confounding 下即使不做 topology-aware 分析偏差方向也可预测），R1 rebut 认为合理。保留但可考虑软化为 \"critical\"\n\n### Section 1 Introduction (pages 1-2)\n- \"No prior work systematically characterizes...\" → 加入 \"extending prior single-topology analyses (Brenner 1993; Teblunthuis et al. 2024)\" 的限定语 [S1]\n- Contribution 2: \"Annotation Sensitivity Values\" 可操作性需在主文强化——至少用 2-3 行总结 Algorithm 1 的核心逻辑 [M2]\n\n### Section 3.1 Setup (page 3)\n- 增加 1-2 句解释为何从线性 SEM 出发（标准分析起点、允许闭式解、B.6 logistic 验证提供稳健性保证）[C2]\n- \"plim\" 首次出现时加括号定义 [minor]\n\n### Section 3.2 Bias Expressions (pages 3-5)\n- 拓扑间过渡可加简短引导句 [minor]\n- Proportional effects (f=λg)：在 Theorem 1 后增加讨论——用 23 个真实混淆矩阵评估 f/g 近似程度 [C1]\n\n### Section 3.3 ASV (pages 5-6)\n- Conjecture 1：增加 1-2 句讨论证明障碍（K≥3 自由度增长 vs bounding 策略）[M1]\n- ASV 与 E-value 的区别可用一句话更明确（\"While E-values quantify unmeasured confounding tolerance, ASV quantifies annotation error tolerance\"）[minor]\n\n### Section 4 Experiments (pages 6-8)\n- Section 4.2 sign reversal 呈现：正文中 exposure 2.1% 与 IV 42.1% 的对比应更突出 [S2]\n- Section 4.4 empirical validation：讨论 23 个配置的参数空间覆盖度 [S3]\n- Section 4.5 PPI++：47.0% vs Table 4 Grand mean 17.0 数字不一致——必须修正 [S4]\n- 将 B.6/B.13 核心结论（logistic DGP 下 sign-flip 稳定性 + FWL breakdown negligible）提升到 Section 4 用 1-2 句总结 [C2]\n\n### Section 5 Conclusion (page 8)\n- \"empirical regularity driven by magnitude dominance\" 措辞合理，保持 [R1 认可]\n\n### Limitations (page 9)\n- 非线性模型适用性讨论需加强：何种条件下线性近似合理、何时可能失效 [C2]\n- 增加多标注者设定对 confusion matrix 估计影响的讨论 [minor]\n\n### Figures/Tables\n- Figure 1: 增大节点标签字号 [minor]\n- Figure 2: 增大 y 轴标签 + 改用色觉友好配色 [minor]\n- Table 1: ✗/✓ 改为 Yes/No 或不同填充模式 [minor]",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n\n**Venue**: EMNLP 2026 (ARR May Cycle) | **类型**: Long Paper | **Round**: 9 (Fresh)\n**Reviewers**: R1 (方法严谨性+实验验证), R2 (新颖性+完整性+写作呈现)\n\n---\n\n## Summary\n\n本文研究 LLM 标注产生的 K-class 非差异误分类在因果推断中的传播，核心发现是传播方式取决于 DAG 拓扑而非标注准确率。论文为 7 种标准 DAG 拓扑推导闭式偏差表达式，证明 K≥3 引入 K=2 不存在的 sign reversal 可能性（exposure 83.4%、IV 52.6%），提出 Annotation Sensitivity Values (ASV) 诊断框架（含 magnitude/significance/sign-flip 三种度量），并证明 FWL 不变性使矩阵校正对 4 种协变量拓扑无效。通过 100,000 随机矩阵和 23 个真实 LLM 混淆矩阵验证。\n\n---\n\n## Strengths\n\n1. **问题定义的新颖性和时效性**：首次在统一框架下对 7 种 DAG 拓扑 × K-class 误分类推导闭式偏差表达式并进行跨拓扑对比，填补了 NLP×因果推断文献中的空白。[R1, R2 共识]\n\n2. **\"拓扑 > 准确率\"的反直觉洞见**：在 F₁ 0.614-0.690 范围内偏差变化 10×（IV 42.1% vs collider <5.6%），挑战了\"提高标注准确率即可解决下游问题\"的常见假设。[R1, R2 共识]\n\n3. **K=2 理论的严谨性**：Theorem 1 的单调性证明结构完整（凸性 + 端点条件），Proposition 1 的 sign preservation 对 confounding/collider 给出解析证明，证明路径有独立方法论价值。[R1 主导]\n\n4. **理论结果的诚实分层**：明确区分 Theorem（证明）→ Proposition（部分证明）→ Observation（数值验证）→ Conjecture（猜想）四级层次，学术诚信度高。[R1, R2 共识]\n\n5. **FWL 不变性的否定结果**：证明 matrix-based correction 对 4 个协变量拓扑 provably ineffective，帮助研究者避免无效纠偏策略——一个有实用价值的否定结论。[R1, R2 共识]\n\n6. **丰富的附录**：20 页附录包含完整证明、多个稳健性检验（non-differential stress test、cross-K、logistic DGP、bootstrap uncertainty），显著增强可信度和可复现性。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### CRITICAL\n\n**C1. 核心假设在 LLM 场景中缺乏实证验证** [R1-N1, R2 AGREE]\n\n论文框架建立在两个关键假设上——(1) 非差异性误分类 P(A*|A,Y,Z)=P(A*|A)，(2) proportional effects (f=λg)——但未提供任何实证证据表明这些假设在 LLM 标注场景中近似成立。\n\n- **非差异性**：Appendix B.5 的 stress test 使用均匀 ε-perturbation，无法捕捉 LLM 的结构性差异误差（如 content-dependent differential error：LLM 对情感极性明确文本更准确，导致 P(A*|A) 依赖于 Y）。论文缺乏按 outcome 分层估计条件混淆矩阵 P(A*|A,Y=y) 的实证检验。\n- **比例效应**：Appendix B.12 显示 λ(C) 越界率在独立 f 时饱和于 ~23%，但论文未论证 LLM 混淆矩阵为何应满足比例效应。R2 补充：即使违反，sign failure rate 始终 <1%，说明 sign preservation 仍 robust。但 R1 建议用 23 个真实混淆矩阵定量评估 f/g 变异系数——这是低成本高价值的检验。\n\n**C2. 线性 SEM 假设对 EMNLP 读者的可达性和泛化性严重不足** [R2-N2, R1-W2, 交叉后共识升为 CRITICAL]\n\n论文正文仅用一句话提及 logistic DGP 结果（Section 5）。对于 EMNLP 的核心读者群（NLP 研究者），线性 SEM 与现代 NLP pipeline 的差距如果不在 Method 部分早期讨论，会严重影响 venue fit。Appendix B.6（logistic DGP sign-flip 稳定性）和 B.13（FWL logistic 验证）提供了有价值的稳健性证据，但被藏在附录中。建议在 Section 3.1 增加 1-2 句解释为何从线性 SEM 出发，并将 B.6/B.13 核心结论提升到正文。\n\n### MAJOR\n\n**M1. K≥3 理论基础不完整，而 K≥3 是 NLP 的主要应用场景** [R1-W1, R2-W4, 共识]\n\nK=2 理论严格，但 K≥3（NLP 绝大多数任务的场景）的核心性质——envelope monotonicity——止步于 Observation 1（20,000 次数值验证）和 Conjecture 1（30,000 矩阵/topology），ASV 框架和 Algorithm 1 的实用指导依赖这些未证明的结果。论文标注诚实，但应讨论证明的技术障碍：是 K≥3 列随机矩阵的谱性质不再保证 convexity 结构，还是存在潜在反例？\n\n**M2. ASV 框架的可操作性（actionability）展示不足** [R2-W1, R1 AGREE]\n\nASV 定位为 \"diagnostics\"，但缺少端到端使用场景：从业者如何获取所需输入（C₀、DAG topology），如何解释三种 ASV 数值，如何据此决策？Algorithm 1 在 Appendix 最后一页，与主文 ASV 连接不紧。建议在主文用 2-3 行总结 Algorithm 1 核心逻辑，或增加 practitioner walkthrough。\n\n### SHOULD-FIX\n\n**S1. \"first to characterize\" novelty claim 需更精确限定** [R2-N1 critical → R1 建议降为 should-fix, 共识降级]\n\nBrenner (1993) 覆盖 polytomous confounder，Teblunthuis (2024) 覆盖单拓扑回归偏差，Ogburn & VanderWeele (2012) 覆盖 binary confounder 单调性。论文实际新颖性在于 7 拓扑 × K-class 的闭式联合对比。建议修改为 \"first unified analysis across seven topologies\" 并在 Section 1 贡献列表中明确 \"building on\" 先驱工作。R1 认为论文新颖性不依赖 \"first\" 措辞，降为 should-fix 合理。\n\n**S2. Abstract 中 2.1% sign reversal 聚合数字掩盖拓扑间差异** [R2-W3, R1 AGREE]\n\n2.1% 是跨所有拓扑×系数的平均值，而 IV 42.1%、exposure 83.4%（Dirichlet 下）。这个聚合数字恰恰掩盖了论文 \"topology-dependent\" 的核心主张。建议报告 range 或加限定语。\n\n**S3. 经验验证的 LLM 配置多样性有限** [R1-W3, R2-W2, 共识]\n\n4 个开源 LLM 规模相近（缺 <7B 和 >70B），3 个英文数据集任务类型偏分类（缺序数标注），23 个配置不足以支撑 primary coefficient 普遍性声明。建议增加不同规模/架构的 LLM 或讨论混淆矩阵参数空间覆盖度。\n\n**S4. PPI++ grand-mean RMSE reduction 数字不一致** [R1-W4/Q5, R2 确认]\n\nSection 4.5 正文报告 \"grand-mean RMSE reduction (47.0%)\"，但 Table 4 Grand mean 行 PPI++ 列为 17.0。作者必须澄清 47.0% 的计算口径（是否仅限 protective topologies）或修正数字。\n\n### MINOR\n\n- Figure 1 字体小、Figure 2 y 轴标签小 + 红绿配色对色觉障碍不友好、Table 1 ✗/✓ 黑白打印难区分 [R1, R2]\n- \"plim\"（probability limit）对 NLP 读者不常见，首次出现应加定义 [R1, R2]\n- Section 3.2 拓扑间过渡突然，符号密度高 [R1, R2]\n- Appendix B.1 binarization collapse（K=3→binary 引入 154× 额外偏差）在主文中提及不足 [R1]\n- 多标注者设定对 confusion matrix 估计的影响未讨论 [R2]\n- Appendix Table 2（sign preservation 充分条件总结）非常有价值，建议在主文更明确引用 [R1]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下问题上高度一致（交叉回应中全部 [AGREE]）：\n\n1. **假设验证不足是核心瓶颈**：非差异性和比例效应假设在 LLM 场景中的合理性缺乏实证支持，这是论文从 Borderline 上升到 Conference 的关键障碍\n2. **K≥3 理论不完整**：对 NLP 主要应用场景的覆盖止步于数值验证和猜想\n3. **线性 SEM 讨论不足**：需在正文早期建立与 NLP 实践的连接\n4. **LLM 配置多样性有限**：规模和任务类型覆盖面需扩展\n5. **PPI++ 数字不一致**：需澄清或修正\n6. **2.1% 聚合数字有误导性**：应报告 range\n\n---\n\n## Reviewer Divergence\n\n仅在严重程度和 minor 点上存在分歧，无实质性矛盾：\n\n1. **R2-N1 (overclaiming) 严重程度**：R2 列为 critical，R1 建议降为 should-fix（论文新颖性不依赖 \"first\" 措辞）。→ 报告中采纳 should-fix。\n2. **R2-W5 (sensitivity analysis 文献覆盖)**：R2 列为 should-fix，R1 rebut（论文已引用 Lash et al. 2009 和定位 ASV vs E-value），建议降为 minor。→ 报告中采纳 minor。\n3. **R1-m3 (Table 2 移入主文)**：R2 rebut（页面预算不允许），建议更明确的交叉引用。→ 采纳 minor。\n4. **R1-m4 (\"topology\" 术语)**：R2 rebut（因果推断文献标准用法）。→ 不列入报告。\n\n---\n\n## Questions\n\n1. **[R1-Q1]** 能否用 23 个真实 LLM 混淆矩阵定量评估 proportional effects 近似程度（计算 f/g 变异系数）？[R2 AGREE: 低成本高价值]\n2. **[R1-Q2]** 是否存在可构造的混淆矩阵（满足 non-differential + 合理精度）使 primary coefficient 反转？如果存在需什么条件？[R2 AGREE: 理论边界问题]\n3. **[R1-Q3]** ASV 排序在不同 DGP 参数化（系数大小、误差方差）下是否稳定？Appendix B.10 部分回答（β alternating/same-sign），但未覆盖更复杂的多变量交互效应场景。[R2 部分 REBUT: B.10 已覆盖基本情况]\n4. **[R1-Q4]** Collider 的结构独特性在非线性 DGP + 线性估计时是否保持？Appendix B.6 中 collider logistic sign-flip 为 0.000 但仅测 K=3。[R2 AGREE: 需更详细分析]\n5. **[R1-Q5]** Section 4.5 PPI++ \"grand-mean RMSE reduction (47.0%)\" vs Table 4 Grand mean 17.0——请澄清。[R2 AGREE: 明确不一致]\n\n---\n\n## Missing References\n\n论文引用覆盖面总体良好。以下为可选补充（非必需）：\n- Bound, Brown, and Mathiowetz (2001) — 测量误差综述（已引用 Carroll et al. 2006）。低优先级。\n- VanderWeele (2015) — mediation 教材。低优先级。\n- 未发现 fabricated citations。引用格式符合 ACL natbib 规范。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。项目配置中外部审稿未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 因速率限制出错（agent exited: rate limit hit），未完成实际 PDF 渲染审查。完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n\n**综合判断**：论文对一个重要且新颖的问题做出了实质性贡献。K=2 理论严格，\"拓扑 > 准确率\"洞见有概念和实践价值，FWL 不变性否定结果实用。但以下因素阻止了更高评分：\n\n1. **实践相关性缺口**：核心假设（非差异性、比例效应、线性 SEM）在 LLM 标注场景中的合理性未经实证验证，框架对目标用户（NLP 因果推断研究者）的可用性存疑\n2. **理论完整性缺口**：K≥3（NLP 主要场景）的核心性质止步于 conjecture\n3. **贡献偏增量**：各单项贡献（多分类偏差分析是经典测量误差理论的推广，ASV 是灵敏度分析工具的变体，FWL 不变性是已知定理的应用）的新颖性中等\n\n**从 Borderline 到 Conference 的关键路径**：\n- 用 23 个真实混淆矩阵定量评估 proportional effects 近似程度（Q1）\n- 在正文 Section 3.1 解释线性 SEM 选择动机 + 提升 B.6/B.13 核心结论\n- 修正 PPI++ 数字不一致\n- Abstract 中 2.1% 改为报告 topology-specific range\n\n**置信度**: 4/5（两位 Reviewer 仔细阅读正文+附录，交叉回应后高度一致）\n\n---\n\n## Detailed Comments\n\n### Abstract (page 1)\n- \"the sign reversal rate is 2.1%\" → 改为报告 topology-dependent range（如 \"0% for confounding to over 40% for IV under realistic accuracy\"），当前聚合数字与论文核心主张矛盾 [S2]\n- \"Topology-aware analysis is necessary\" → R2 认为过于绝对（confounding 下即使不做 topology-aware 分析偏差方向也可预测），R1 rebut 认为合理。保留但可考虑软化为 \"critical\"\n\n### Section 1 Introduction (pages 1-2)\n- \"No prior work systematically characterizes...\" → 加入 \"extending prior single-topology analyses (Brenner 1993; Teblunthuis et al. 2024)\" 的限定语 [S1]\n- Contribution 2: \"Annotation Sensitivity Values\" 可操作性需在主文强化——至少用 2-3 行总结 Algorithm 1 的核心逻辑 [M2]\n\n### Section 3.1 Setup (page 3)\n- 增加 1-2 句解释为何从线性 SEM 出发（标准分析起点、允许闭式解、B.6 logistic 验证提供稳健性保证）[C2]\n- \"plim\" 首次出现时加括号定义 [minor]\n\n### Section 3.2 Bias Expressions (pages 3-5)\n- 拓扑间过渡可加简短引导句 [minor]\n- Proportional effects (f=λg)：在 Theorem 1 后增加讨论——用 23 个真实混淆矩阵评估 f/g 近似程度 [C1]\n\n### Section 3.3 ASV (pages 5-6)\n- Conjecture 1：增加 1-2 句讨论证明障碍（K≥3 自由度增长 vs bounding 策略）[M1]\n- ASV 与 E-value 的区别可用一句话更明确（\"While E-values quantify unmeasured confounding tolerance, ASV quantifies annotation error tolerance\"）[minor]\n\n### Section 4 Experiments (pages 6-8)\n- Section 4.2 sign reversal 呈现：正文中 exposure 2.1% 与 IV 42.1% 的对比应更突出 [S2]\n- Section 4.4 empirical validation：讨论 23 个配置的参数空间覆盖度 [S3]\n- Section 4.5 PPI++：47.0% vs Table 4 Grand mean 17.0 数字不一致——必须修正 [S4]\n- 将 B.6/B.13 核心结论（logistic DGP 下 sign-flip 稳定性 + FWL breakdown negligible）提升到 Section 4 用 1-2 句总结 [C2]\n\n### Section 5 Conclusion (page 8)\n- \"empirical regularity driven by magnitude dominance\" 措辞合理，保持 [R1 认可]\n\n### Limitations (page 9)\n- 非线性模型适用性讨论需加强：何种条件下线性近似合理、何时可能失效 [C2]\n- 增加多标注者设定对 confusion matrix 估计影响的讨论 [minor]\n\n### Figures/Tables\n- Figure 1: 增大节点标签字号 [minor]\n- Figure 2: 增大 y 轴标签 + 改用色觉友好配色 [minor]\n- Table 1: ✗/✓ 改为 Yes/No 或不同填充模式 [minor]",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-23T03:04:38.164044+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4366
}
```

</details>

---


### Assistant

_source line 714 · 2026-05-23T03:04:47.835399+00:00_

审稿报告已投递至 Research Director。

**Round 9 审稿完成总结：**

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致
- **2 个 CRITICAL**：(C1) 核心假设（非差异性 + 比例效应）在 LLM 场景缺乏实证验证；(C2) 线性 SEM 讨论对 EMNLP 读者严重不足
- **2 个 MAJOR**：(M1) K≥3 理论止步于 conjecture；(M2) ASV 可操作性展示不足
- **4 个 SHOULD-FIX**：novelty claim 限定、2.1% 聚合数字误导、LLM 配置多样性有限、PPI++ 数字不一致
- **从 Borderline → Conference 的关键路径**：用 23 个真实混淆矩阵验证比例效应近似程度 + 正文前置线性 SEM 动机和 logistic 稳健性结论 + 修正 PPI++ 数字 + Abstract 报告 topology-specific range

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 715 · 2026-05-23T03:04:50.485057+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部意见的逐条回应，已提交给 Director。

总结：
- **14 条中 12 条 [AGREE]**：与 R1 在核心问题上高度共识（假设验证不足、K≥3 理论不完整、LLM 多样性有限、PPI++ 数字不一致）
- **2 条 [REBUT]**：m3（Table 2 移入主文——页面预算不允许）和 m4（"topology" 术语——因果推断领域标准用法）
- **Q3 部分反驳**：Appendix B.10 已回答 ASV 排序稳定性，但未覆盖极端参数化场景
- **关键共识**：两份审稿共同认为假设的实践相关性验证不足是决定接收的核心问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 716 · 2026-05-23T03:05:03.398674+00:00_

审稿流程已完成。

**Round 9 审稿报告已投递至 Research Director。**

汇总：
- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致
- **2 个 CRITICAL**：核心假设（非差异性+比例效应）缺乏 LLM 场景实证验证；线性 SEM 对 EMNLP 读者可达性不足
- **2 个 MAJOR**：K≥3 理论止步于 conjecture；ASV 可操作性展示不足
- **4 个 SHOULD-FIX**：novelty claim 限定、2.1% 聚合数字误导、LLM 配置多样性、PPI++ 数字不一致
- **交叉回应高度收敛**：R1 对 R2 的 7 条中 6 条 AGREE，R2 对 R1 的 14 条中 12 条 AGREE，仅在 minor 点上有分歧

Issue tracker 已同步更新（`review_issues.yaml`）。视觉审查因 Agent 速率限制未完成，完成后会自动补发到 Group C。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 81

## Round 81

52 recorded events


### User

_source line 717 · 2026-05-23T03:33:55.226992+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-23T03:34:01.904367+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-23T03:34:02.005737+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-23T03:34:08.883006+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-23T03:34:08.883441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-23T03:34:14.155363+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-23T03:34:16.117314+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1961
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-23T03:34:16.620426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-23T03:34:17.122334+00:00_

-rw-r--r-- 1 ubuntu ubuntu 912113 May 23 03:33 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf
-rw-r--r-- 1 ubuntu ubuntu   1772 May 23 00:21 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-23T03:34:17.624063+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-23T03:34:17.624516+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-23T03:34:18.025634+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-23T03:34:18.076215+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-23T03:34:24.153242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-23T03:34:24.555329+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 732 · 2026-05-23T03:34:24.605925+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-23T03:34:32.053500+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Here are the search results for EMNLP 2026 call for papers submission guidelines and ARR information:

## Key Information

**Paper Types and Scope:**
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

**Presentation Requirements:**
All accepted papers must be presented at the conference to appear in the proceedings, and the conference will include both in-person and virtual presentation options.

**Deadlines:**
Al
…[truncated 711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7900
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-23T03:34:36.120273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind anonymity guidelines",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind anonymity guidelines",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-23T03:34:38.129145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-23T03:34:38.180503+00:00_

issues:
  # === Round 1-7 历史 (resolved，保留摘要) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 7
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
    resolution_round: 7

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 9
    mentions:
      - round
…[truncated 20589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-23T03:34:42.899353+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind anonymity guidelines"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"18th International Natural Language Generation Conference | ACL Member Portal","url":"https://www.aclweb.org/portal/content/18th-international-natural-language-generation-conference"},{"title":"EMNLP Workshop on Text Simplification, Accessibility, and Readability (TSAR) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-workshop-text-simplification-accessibility-and-readability-tsar"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"}]

Based on the search results, I found information about the EMNLP 2026 Industry Track submission guidelines. Here's what I found regarding submission format requirements:

## EMNLP 2026 Industry Track Submission Guidelines

**Page Limit:**
Industry track papers have a maximum of 6 pages, and Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references).

**Sections Not Counting Toward Page Limit:**
Refer
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6779
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-23T03:34:58.266816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit formatting requirements",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit formatting requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-23T03:34:59.823010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-23T03:34:59.823473+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\input{related_work}
38	
39	\input{method}
40	
41	% ── Figures ──
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
46	\vspace{-6pt}
47	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
48	\label{fig:dag_taxonomy}
49	\end{figure*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-23T03:35:06.447739+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit formatting requirements"

Links: [{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on my search results, I found information about ACL Rolling Review (ARR) 2026 author guidelines regarding formatting requirements:

ACLPUB formatting guidelines were updated in January 2025 with clarifications on font size in figures and tables, placement of limitations and ethical considerations sections, and two-column formatting of appendices.

The paper follows ACL formatting, and you are encouraged to use the ACL pubcheck tool to check for common problems. There is an official Overleaf template. The template has a [review] setting that must be on for the submission.

Regarding the page limit, an optional ethics section will not count towards 
…[truncated 460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 8180
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-23T03:35:11.575384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-23T03:35:12.027890+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), sign reversal occurs in 2.1\% of exposure configurations, exclusively in secondary coefficients with small effect sizes; no sign reversals occur for the remaining six topologies including IV. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-23T03:35:12.128690+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-23T03:35:12.530502+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-23T03:35:12.681545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-23T03:35:13.033439+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 1997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-23T03:35:13.184554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-23T03:35:13.486669+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This holds when the LLM annotates from source documents without access to outcome information. Even without explicit $Y$ access, differential misclassification can arise if LLM pretraining data encodes $A$--$Y$ statistical associations---e.g., in political stance classification, strongly emotional texts correlating with the outcome may be misclassified at different rates, violating $P(A^*{\mid}A,Y) = P(A^*{\mid}A)$. Violations can also arise from outcome-conditional prompting, few-shot demonstrations encoding $A$--$Y$ associations, or retrieval-augmented pipelines surfacing $Y$-correlated documents. When violated, bias can deviate in either direction without the toward-null constraint. Practitioners can diagnose violations by testing $P(A^*{\mid}A,Y) \approx P(A^*{\mid}A)$ on a gold-labeled subset, though $Y$-conditional validation sets are rarely available in practice; our stress test (Appendix~\ref{sec:nondiff_stress}) covers $\varepsilon$ up to $0.50$ as a conservative upper bound, with violations below $\varepsilon{=
…[truncated 14482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-23T03:35:13.487047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-23T03:35:13.838892+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse th
…[truncated 7267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-23T03:35:13.989999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-23T03:35:13.990521+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain a structural guarantee. The ASV framework reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms: the primary coefficient does not reverse in any tested configuration---an empirical regularity driven by magnitude dominance rather than algebraic structure---while 61\% of exposure configurations reverse a secondary coefficient. Our analytical results assume linear SEMs; Appendix~\ref{sec:logistic_dgp} demonstrates that topology rankings and sign-flip patterns are preserved under logistic DGP ($|\Delta\,\text{SF}_\tau| < 0.02$), though FWL invariance is specific to linear models. Differential misclassification and correlated multi-LLM errors are natural extensions. Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinea
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-23T03:35:27.946184+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>&1 || pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf 2>&1",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>&1 || pdfinfo /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf 2>&1",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-23T03:35:28.749960+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 03:33:05 2026 UTC
ModDate:         Sat May 23 03:33:05 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           28
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       912113 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-23T03:35:28.750396+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-23T03:35:28.800948+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 3331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-23T03:35:48.572586+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-23T03:36:11.824933+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23252
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-23T03:36:11.975981+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 审查论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，各章节用 `\\input` 引入）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long Paper，正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有（不计入页数）\n- ACL 模板，`[review]` 模式，A4\n- Double-blind 匿名审稿\n- 截止日期：2026-05-25\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查重点\n\n### 1. 理论推导正确性\n- Proposition 1 (sign preservation for confounding/collider) 的证明是否严密？条件是否充分？\n- Theorem 1 (envelope monotonicity for K=2) 的证明逻辑是否完整？proportional effects 假设是否过强？\n- Observation 1 和 Conjecture 1 的数值验证是否充分？K≥3 证明障碍的解释是否令人信服？\n- 各拓扑的 bias expression 推导是否正确？\n\n### 2. 假设合理性\n- Non-differential misclassification 假设在 LLM 标注场景下是否合理？讨论是否充分？\n- Proportional effects (f=λg) 假设——何时成立、何时不成立？违反时后果如何？\n- 线性 SEM 假设对 NLP/CSS 实践的限制——是否充分讨论？logistic DGP 验证是否有说服力？\n- DAG 拓扑已知假设的实际可行性\n\n### 3. 实验设计与统计验证\n- Monte Carlo 验证的设计（N=10,000, 100,000 matrices）是否充分？\n- 23 个 LLM 配置的多样性是否足够代表实际应用？\n- ASV bootstrap CI 的设计和解释是否合理？\n- PPI++ 和其他 correction 方法的评估是否公平？\n- Theory-MC MAPE 1.6% 的报告是否合理？\n\n### 4. 数学符号与一致性\n- 符号系统是否统一？有无矛盾或歧义？\n- 定理/命题/猜想的层次是否清晰？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: must-fix / should-fix / minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 审查论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，各章节用 `\\input` 引入）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long Paper，正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有（不计入页数）\n- ACL 模板，`[review]` 模式，A4\n- Double-blind 匿名审稿\n- 截止日期：2026-05-25\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查重点\n\n### 1. 理论推导正确性\n- Proposition 1 (sign preservation for confounding/collider) 的证明是否严密？条件是否充分？\n- Theorem 1 (envelope monotonicity for K=2) 的证明逻辑是否完整？proportional effects 假设是否过强？\n- Observation 1 和 Conjecture 1 的数值验证是否充分？K≥3 证明障碍的解释是否令人信服？\n- 各拓扑的 bias expression 推导是否正确？\n\n### 2. 假设合理性\n- Non-differential misclassification 假设在 LLM 标注场景下是否合理？讨论是否充分？\n- Proportional effects (f=λg) 假设——何时成立、何时不成立？违反时后果如何？\n- 线性 SEM 假设对 NLP/CSS 实践的限制——是否充分讨论？logistic DGP 验证是否有说服力？\n- DAG 拓扑已知假设的实际可行性\n\n### 3. 实验设计与统计验证\n- Monte Carlo 验证的设计（N=10,000, 100,000 matrices）是否充分？\n- 23 个 LLM 配置的多样性是否足够代表实际应用？\n- ASV bootstrap CI 的设计和解释是否合理？\n- PPI++ 和其他 correction 方法的评估是否公平？\n- Theory-MC MAPE 1.6% 的报告是否合理？\n\n### 4. 数学符号与一致性\n- 符号系统是否统一？有无矛盾或歧义？\n- 定理/命题/猜想的层次是否清晰？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: must-fix / should-fix / minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-23T03:36:31.632782+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19656
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-23T03:36:31.787447+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 审查论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，各章节用 `\\input` 引入）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long Paper，正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有（不计入页数）\n- ACL 模板，`[review]` 模式，A4\n- Double-blind 匿名审稿\n- 截止日期：2026-05-25\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查重点\n\n### 1. 新颖性与贡献定位\n- 三个贡献（bias taxonomy、ASV、correction guidance）各自的新颖性如何？\n- 与 Teblunthuis (2024)、Lee et al. (2024)、Brenner (1993) 相比，增量贡献有多大？\n- \"first unified analysis\" 的声称是否准确？是否有遗漏的前人工作？\n- ASV 与 E-value 的关系——是 novel contribution 还是 straightforward adaptation？\n- FWL invariance 作为 negative result 的价值如何？\n\n### 2. Related Work 覆盖\n- 测量误差文献（Carroll et al. 2006, Gustafson 2004）的覆盖是否充分？\n- LLM annotation 文献（Gilardi 2023, Ziems 2024, Baumann 2025）是否完整？\n- 灵敏度分析文献（VanderWeele & Ding 2017, Cinelli 2020）是否正确引用？\n- 是否有明显遗漏的重要相关工作？特别关注 2024-2026 年的新工作\n\n### 3. 写作质量与 Presentation\n- Abstract 信息密度是否合适？关键数字是否有误导性？\n- Introduction 的叙事逻辑是否清晰？motivation 是否有说服力？\n- 数学符号的可读性——对 EMNLP 读者（不一定是因果推断专家）是否友好？\n- 图表的信息量和可读性如何？Figure 1, 2 是否有效传达核心信息？\n- Table 1 的设计是否清晰？各列含义是否容易理解？\n- 8 页正文是否信息密度过高？哪些内容可以移到附录？\n- Limitations 章节是否充分？\n\n### 4. 对 EMNLP 社区的适配性\n- 这篇论文是否适合 EMNLP？还是更适合因果推断会议（如 CLeaR）或统计学期刊？\n- EMNLP 读者的预期背景知识——论文是否做了足够的 accessibility 工作？\n- 实际应用指导——NLP practitioner 能从这篇论文学到什么可操作的东西？\n\n### 5. 格式合规\n- 正文是否在 8 页以内？（PDF 共 28 页，需确认正文/附录分界）\n- 是否符合 ACL 模板要求？\n- 匿名性是否保持？有无泄露作者身份的线索？\n- 引用格式是否正确？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: must-fix / should-fix / minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 审查论文\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 路径：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`（入口文件，各章节用 `\\input` 引入）\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long Paper，正文 ≤ 8 页，参考文献不限页数\n- Limitations 章节必须有（不计入页数）\n- ACL 模板，`[review]` 模式，A4\n- Double-blind 匿名审稿\n- 截止日期：2026-05-25\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查重点\n\n### 1. 新颖性与贡献定位\n- 三个贡献（bias taxonomy、ASV、correction guidance）各自的新颖性如何？\n- 与 Teblunthuis (2024)、Lee et al. (2024)、Brenner (1993) 相比，增量贡献有多大？\n- \"first unified analysis\" 的声称是否准确？是否有遗漏的前人工作？\n- ASV 与 E-value 的关系——是 novel contribution 还是 straightforward adaptation？\n- FWL invariance 作为 negative result 的价值如何？\n\n### 2. Related Work 覆盖\n- 测量误差文献（Carroll et al. 2006, Gustafson 2004）的覆盖是否充分？\n- LLM annotation 文献（Gilardi 2023, Ziems 2024, Baumann 2025）是否完整？\n- 灵敏度分析文献（VanderWeele & Ding 2017, Cinelli 2020）是否正确引用？\n- 是否有明显遗漏的重要相关工作？特别关注 2024-2026 年的新工作\n\n### 3. 写作质量与 Presentation\n- Abstract 信息密度是否合适？关键数字是否有误导性？\n- Introduction 的叙事逻辑是否清晰？motivation 是否有说服力？\n- 数学符号的可读性——对 EMNLP 读者（不一定是因果推断专家）是否友好？\n- 图表的信息量和可读性如何？Figure 1, 2 是否有效传达核心信息？\n- Table 1 的设计是否清晰？各列含义是否容易理解？\n- 8 页正文是否信息密度过高？哪些内容可以移到附录？\n- Limitations 章节是否充分？\n\n### 4. 对 EMNLP 社区的适配性\n- 这篇论文是否适合 EMNLP？还是更适合因果推断会议（如 CLeaR）或统计学期刊？\n- EMNLP 读者的预期背景知识——论文是否做了足够的 accessibility 工作？\n- 实际应用指导——NLP practitioner 能从这篇论文学到什么可操作的东西？\n\n### 5. 格式合规\n- 正文是否在 8 页以内？（PDF 共 28 页，需确认正文/附录分界）\n- 是否符合 ACL 模板要求？\n- 匿名性是否保持？有无泄露作者身份的线索？\n- 引用格式是否正确？\n\n请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: must-fix / should-fix / minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-23T03:36:33.304390+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1516
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-23T03:36:45.121851+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-23T03:36:45.272958+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-23T03:36:49.589708+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-23T03:36:49.690700+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 768 · 2026-05-23T03:36:59.028995+00:00_

外部审稿未配置，跳过。

**当前状态**：
- Reviewer 1（方法严谨性）：审稿中...
- Reviewer 2（新颖性/完整性）：审稿中...
- 视觉审查 Agent：运行中...

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 82

## Round 82

52 recorded events


### User

_source line 769 · 2026-05-23T03:40:11.505722+00:00_

[Reviewer 1 审稿结果]:
渲染并阅读附录页面。

---

[Reviewer 2 审稿结果]:
正在阅读附录和参考文献页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-23T03:40:33.542072+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-23T03:40:33.593406+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-23T03:40:38.017313+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-23T03:40:38.920844+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-23T03:40:39.072015+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-23T03:40:39.072974+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-23T03:40:48.119727+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 777 · 2026-05-23T03:40:48.220388+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-23T03:40:48.220785+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_10/**",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_10/**",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-23T03:40:48.321449+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p1.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p2.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p3.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p4.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p5.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p6.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p7.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p8.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p9.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p10.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p11.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p12.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p13.png
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/_pdf_images/submitted_p14.png
/home/ubuntu/.agent-ml-researc
…[truncated 1831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-23T03:41:05.513342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
  "pages": "1-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
    "pages": "1-2"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-23T03:41:06.015428+00:00_

PDF pages extracted: 2 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf (890.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-23T03:41:06.519640+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-23T03:41:07.021299+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-23T03:41:07.021757+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-23T03:41:07.223339+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-23T03:41:07.223781+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-23T03:41:07.324337+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T03:35:52.263909+00:00\", \"completed_at\": \"2026-05-23T03:35:56.304186+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-23T03:41:22.873626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-23T03:41:23.125864+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 24105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-23T03:41:23.579350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
  "pages": "3-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
    "pages": "3-8"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-23T03:41:23.983652+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf (890.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-23T03:41:29.826223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
  "pages": "9-14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
    "pages": "9-14"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-23T03:41:30.178012+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf (890.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-23T03:41:36.216249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
  "pages": "15-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
    "pages": "15-20"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-23T03:41:36.520384+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf (890.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-23T03:41:42.866002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
  "pages": "21-28"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf",
    "pages": "21-28"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-23T03:41:43.418910+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf (890.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-23T03:42:16.764933+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-23T03:42:16.868320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-23T03:42:25.365706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 801 · 2026-05-23T03:42:25.919068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadline guidelines page limit",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission deadline guidelines page limit",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool result

_source line 802 · 2026-05-23T03:42:31.948027+00:00_

Web search results for query: "ACL Rolling Review 2026 submission deadline guidelines page limit"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here's information about the ACL Rolling Review 2026 submission deadline and page limits:

## Submission Deadline

The submission deadline is always the 15th of the month. For ACL 2026 specifically, ARR reviews & meta-reviews available to authors of the January cycle: March 10, 2026.

## Page Limits

All ARR submissions are an
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6028
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-23T03:42:32.048913+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines and ARR:

## Main Conference Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Presentation Requirements

All accepted papers must be presented at the conference to appear in the proceedings, with both in-person and virtual presentation options available.

## ARR Policy for EMNLP 2026

The ARR 2026 Ma
…[truncated 684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6683
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-23T03:42:48.393843+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-23T03:42:48.444678+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/decisions.yaml\", \"content\": \"_next_id: 21\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:25 UTC\\n  summary: MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 research 阶段\\n  rationale: 三项 pass 标准全部满足：(1) 理论预测 vs MC 95% CI 一致 5/5，(2) 所有非差异性 C 产生远离零偏差 0.20-0.30，(3)\\n    二分类折叠偏差与三分类预测显著不同（最大 Δ=0.089）。附加发现：100k 随机 C 矩阵搜索在 confounding DAG 下未发现方向反转——偏差始终与\\n    OVB 同向。这是有价值的 characterization result：confounding DAG 偏差方向可预测（单调），方向反转假设需要在其他\\n    DAG 拓扑（mediator、collider）中验证，属于 research 阶段的核心任务。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:30 UTC\\n  summary: Research 阶段第一优先级：exposure misclassification DAG K=3 验证 bias-toward-null\\n    是否在多分类下打破\\n  rationale: Reviewer 指出 MVP criterion 2 在 confounding DAG 下不具区分力（二分类也 pass）。\\\"Bias\\n    toward null\\\" 保证（Bross 1954）特指 exposure 误分类，正确测试需要 exposure DAG（A→Y，用 A* 替代 A）。若\\n    K=3 下此 DAG 出现方向反转或 bias-away-from-null 结构性差异，则 Claim 1 最强形式成立；若不出现，需重新框定核心 claim。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:31 UTC\\n  summary: plan_001 完成后设 checkpoint gate：方向反转拓扑数 → framing 版本选择\\n  rationale: 'Reviewer [severity: critical] 指出 plan_001 是存在性检验但无 kill criterion。当前\\n    core insight 依赖方向反转（\\\"binary guarantee breaks\\\"），但 MVP 已证明 confounding DAG 无反转。若\\n    6 拓扑全无反转，framing 需 pivot。三级响应：(A) ≥2 拓扑有反转 → 当前 framing 成立，方向反转为 lead finding；(B)\\n    1 拓扑有反转 → 该拓扑为 lead case，framing 可调整；(C) 0 拓扑有反转 → pivot 到版本 B：\\\"multi-class 偏差\\n    magnitude 不可由 binary 推算 + binarization 本身有害\\\"，方向反转降为 topology-specific finding。注意：0\\n    反转 ≠ 项目 kill——binarization inequality + magnitude unpredictability + ASVs 本身够一篇论文，但\\n    framing 必须诚实。'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: gate\\n    result: pending\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:39 UTC\\n  summary: D003 checkpoint 
…[truncated 1473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-23T03:42:56.288501+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/causal_annot_error_attrib/config.*",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/causal_annot_error_attrib/config.*",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-23T03:42:56.389466+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-23T03:43:01.717356+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-23T03:43:01.868809+00:00_

Found 3 files
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/logs/chats/feishu_group_oc_9f117624057fcf6cb95db4d67f525246_director.jsonl
AGENTS.md
CLAUDE.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-23T03:43:06.588028+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview\"",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/CLAUDE.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview\"",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/CLAUDE.md",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-23T03:43:06.688778+00:00_

&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/CLAUDE.md. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/review_director_d2e6d7be.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-23T03:43:12.267667+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai\"",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "glob": "AGENTS.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai\"",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
    "glob": "AGENTS.md",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-23T03:43:12.368455+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-23T03:43:32.110668+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-23T03:43:51.672234+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19561
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-23T03:43:52.776670+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **格式**: ACL 模板，Long paper，正文严格 8 页限制，参考文献不限页数，Limitations 和 Ethics 不计入页数限制\n- **匿名**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`（28 页，含正文 8 页 + Limitations + References + 大量 Appendix）\n\n## 你的审查侧重\n\n### 1. 理论正确性\n- Proposition 1(a)(b)(c) 的证明是否完整、正确？条件是否充分必要？\n- Theorem 1（K=2 confounding/mediation monotonicity）的证明链是否严谨？\n- Observation 1 和 Conjecture 1 的数值验证规模和方法是否足以支撑 claim？\n- 三级层次（Proved / Numerically Verified / Conjectured）的使用是否一致且准确？\n\n### 2. 假设合理性\n- **Non-differential misclassification** 假设在 LLM 场景下是否现实？论文是否充分讨论了违反情景？\n- **Proportional effects**（f = λg）假设的实证支撑是否充分？λ(C) ∈ [0,1] 的验证是否有说服力？\n- **线性 SEM** 假设对 EMNLP 读者的可达性——是否有足够的动机说明和非线性 robustness check？\n\n### 3. 实验设计\n- Monte Carlo 验证的参数设置（N=10,000, 100,000 matrices）是否充分？\n- 23 个真实 LLM confusion matrices 的代表性：4 个 LLM × 3 个数据集 × K=2,3,10 是否覆盖足够多样的场景？\n- ASV bootstrap CI 的设置（B=1,000）是否合理？\n- Non-differential stress test 和 FWL logistic breakdown 的实验设计是否有说服力？\n- Correction methods 评估（Table 4）是否公平？\n\n### 4. 数学一致性\n- 全文符号体系是否统一（τ, β, B(C), δ*, λ(C) 等）？\n- 公式编号是否正确引用？Appendix 与主文的交叉引用是否准确？\n\n请按 ARR 标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分：1-5 分制）。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **格式**: ACL 模板，Long paper，正文严格 8 页限制，参考文献不限页数，Limitations 和 Ethics 不计入页数限制\n- **匿名**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`（28 页，含正文 8 页 + Limitations + References + 大量 Appendix）\n\n## 你的审查侧重\n\n### 1. 理论正确性\n- Proposition 1(a)(b)(c) 的证明是否完整、正确？条件是否充分必要？\n- Theorem 1（K=2 confounding/mediation monotonicity）的证明链是否严谨？\n- Observation 1 和 Conjecture 1 的数值验证规模和方法是否足以支撑 claim？\n- 三级层次（Proved / Numerically Verified / Conjectured）的使用是否一致且准确？\n\n### 2. 假设合理性\n- **Non-differential misclassification** 假设在 LLM 场景下是否现实？论文是否充分讨论了违反情景？\n- **Proportional effects**（f = λg）假设的实证支撑是否充分？λ(C) ∈ [0,1] 的验证是否有说服力？\n- **线性 SEM** 假设对 EMNLP 读者的可达性——是否有足够的动机说明和非线性 robustness check？\n\n### 3. 实验设计\n- Monte Carlo 验证的参数设置（N=10,000, 100,000 matrices）是否充分？\n- 23 个真实 LLM confusion matrices 的代表性：4 个 LLM × 3 个数据集 × K=2,3,10 是否覆盖足够多样的场景？\n- ASV bootstrap CI 的设置（B=1,000）是否合理？\n- Non-differential stress test 和 FWL logistic breakdown 的实验设计是否有说服力？\n- Correction methods 评估（Table 4）是否公平？\n\n### 4. 数学一致性\n- 全文符号体系是否统一（τ, β, B(C), δ*, λ(C) 等）？\n- 公式编号是否正确引用？Appendix 与主文的交叉引用是否准确？\n\n请按 ARR 标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分：1-5 分制）。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-23T03:44:12.024091+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19247
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-23T03:44:12.742796+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **格式**: ACL 模板，Long paper，正文严格 8 页限制，参考文献不限页数，Limitations 和 Ethics 不计入页数限制\n- **匿名**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`（28 页，含正文 8 页 + Limitations + References + 大量 Appendix）\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 三个 contribution（bias taxonomy / ASV diagnostics / correction guidance）中，哪些是真正新颖的，哪些是已知结果的推广？\n- \"first unified analysis\" 的 claim 是否准确？与 Brenner (1993)、TeBlunthuis et al. (2024)、Lee and Wood-Doughty (2024) 的关系是否清晰界定？\n- ASV 框架与 E-value (VanderWeele & Ding, 2017) 的区别是否充分阐明？是否存在 \"直接移植\" 质疑？\n- FWL invariance 结果（matrix corrections 对 4 种拓扑 0% bias reduction）是否为真正新发现？\n\n### 2. Related Work 覆盖\n- measurement error in causal inference 文献是否充分覆盖？\n- text-as-data 和 LLM annotation 文献是否遗漏重要工作？\n- sensitivity analysis 文献（E-value, partial R², Rosenbaum bounds）是否充分连接？\n- 是否遗漏了 2024-2025 年发表的重要相关工作？\n\n### 3. 写作质量与可达性\n- Abstract 信息密度是否过高？关键数字（2.1%, 83.4%, 52.6%, 1.6% MAPE, 47.0% PPI++）是否过多？\n- Introduction 叙事结构是否清晰？从问题到贡献的逻辑链是否顺畅？\n- Section 3（Method）对 EMNLP 读者（主要是 NLP 研究者，非统计学家）是否可理解？\n- Figure 1-6 和 Table 1-4 的信息传达是否有效？\n- Limitations 是否充分且诚实？\n\n### 4. 格式合规\n- 正文是否严格在 8 页以内？\n- 匿名性是否保持（无 self-citation 泄露）？\n- 引用格式是否符合 ACL 规范（natbib, author-year）？\n- Appendix 的使用是否合理？是否有 appendix-dumping（将关键内容放在附录以规避页数限制）？\n\n### 5. 实证完整性\n- 23 个 LLM 配置的多样性是否足够（模型大小、任务类型）？\n- ClinicalBERT case study (Section B.3) 的加入是否增强了论文的实用性？\n- 是否缺少与现有 debiasing 方法的 end-to-end 对比？\n\n请按 ARR 标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分：1-5 分制）。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **格式**: ACL 模板，Long paper，正文严格 8 页限制，参考文献不限页数，Limitations 和 Ethics 不计入页数限制\n- **匿名**: Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_10/submitted.pdf`（28 页，含正文 8 页 + Limitations + References + 大量 Appendix）\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- 三个 contribution（bias taxonomy / ASV diagnostics / correction guidance）中，哪些是真正新颖的，哪些是已知结果的推广？\n- \"first unified analysis\" 的 claim 是否准确？与 Brenner (1993)、TeBlunthuis et al. (2024)、Lee and Wood-Doughty (2024) 的关系是否清晰界定？\n- ASV 框架与 E-value (VanderWeele & Ding, 2017) 的区别是否充分阐明？是否存在 \"直接移植\" 质疑？\n- FWL invariance 结果（matrix corrections 对 4 种拓扑 0% bias reduction）是否为真正新发现？\n\n### 2. Related Work 覆盖\n- measurement error in causal inference 文献是否充分覆盖？\n- text-as-data 和 LLM annotation 文献是否遗漏重要工作？\n- sensitivity analysis 文献（E-value, partial R², Rosenbaum bounds）是否充分连接？\n- 是否遗漏了 2024-2025 年发表的重要相关工作？\n\n### 3. 写作质量与可达性\n- Abstract 信息密度是否过高？关键数字（2.1%, 83.4%, 52.6%, 1.6% MAPE, 47.0% PPI++）是否过多？\n- Introduction 叙事结构是否清晰？从问题到贡献的逻辑链是否顺畅？\n- Section 3（Method）对 EMNLP 读者（主要是 NLP 研究者，非统计学家）是否可理解？\n- Figure 1-6 和 Table 1-4 的信息传达是否有效？\n- Limitations 是否充分且诚实？\n\n### 4. 格式合规\n- 正文是否严格在 8 页以内？\n- 匿名性是否保持（无 self-citation 泄露）？\n- 引用格式是否符合 ACL 规范（natbib, author-year）？\n- Appendix 的使用是否合理？是否有 appendix-dumping（将关键内容放在附录以规避页数限制）？\n\n### 5. 实证完整性\n- 23 个 LLM 配置的多样性是否足够（模型大小、任务类型）？\n- ClinicalBERT case study (Section B.3) 的加入是否增强了论文的实用性？\n- 是否缺少与现有 debiasing 方法的 end-to-end 对比？\n\n请按 ARR 标准输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分：1-5 分制）。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-23T03:44:14.355400+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1612
}
```

</details>

---


### Assistant

_source line 820 · 2026-05-23T03:44:23.475131+00:00_

Round 10 审稿任务已重新派发：

- **Reviewer 1**（方法严谨性）：已启动，审查理论正确性、假设合理性、实验设计、数学一致性
- **Reviewer 2**（新颖性+完整性）：已启动，审查贡献定位、Related Work、写作质量、格式合规
- **视觉审查 Agent**：已重新派发（上次因 rate limit 失败）

等待两位 Reviewer 返回初审结果后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 821 · 2026-05-23T03:49:16.175152+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见（方法严谨性）

---

### Paper Summary

本文研究 LLM 多类别标注误差如何通过因果 DAG 结构传播到下游因果推断估计中。作者在线性 SEM 框架下，针对 7 种经典 DAG 拓扑（confounding, mediation, collider, M-bias, front-door, exposure, IV），推导了 K 类非差异性错分（non-differential misclassification）下的偏差闭式表达式。核心贡献包括：(1) Proposition 1(a)(b)(c) 建立了符号保持条件；(2) Theorem 1 证明了 K=2 下 confounding/mediation 的单调性；(3) Observation 1 和 Conjecture 1 通过数值验证扩展到 K≥3；(4) 提出 Annotation Sensitivity Values (ASV) 框架量化拓扑相关脆弱性；(5) 在 23 个真实 LLM 混淆矩阵上验证理论预测（MAPE 1.6%）。论文采用了"已证明 / 数值验证 / 猜想"三级层次体系。

---

### Summary of Strengths

**S1. 问题重要且时机恰当。** LLM 标注在 NLP 因果推断中已广泛使用（Gilardi et al., 2023; Ziems et al., 2024），但标注误差对因果估计的拓扑依赖性传播此前未被系统研究。本文填补了一个明确的方法论空白。

**S2. 理论框架系统而诚实。** 同时覆盖 7 种拓扑在统一符号体系下是罕见的。三级证据层次（Proved / Numerically Verified / Conjectured）在同类论文中极为少见——作者没有过度宣称数值结果为定理，这体现了良好的学术规范。

**S3. Proposition 1(a) 的证明链完整且技术上正确。** Confounding 的符号保持通过 FWL 分解 → Cauchy-Schwarz 界 → ξ(C) ∈ [0,1] 完成（Appendix A.2-A.3, Propositions 2-3），推导清晰，条件（C_kk > 0）既充分又通过 Berkson 衰减论证了必要性方向。Proposition 3 给出的一般情形界 B = √(Var(g(A))·Var(f(A))) / E[Var(T|A*)] 是一个有用的工具性结果。

**S4. 实证验证规模充分。** 23 个真实 LLM 混淆矩阵 × 7 拓扑 = 161 个偏差场景，MAPE 仅 1.6%（Section 4.2），且理论与 Monte Carlo 模拟（N=10,000）的一致性令人信服。100,000 随机矩阵的符号保持验证（Appendix A.3-A.8）提供了数值穷举级别的置信度。

**S5. ASV 框架具有实用价值。** 将 K²维混淆矩阵问题压缩到一维标量阈值 δ*，并给出拓扑排序（IV 最脆弱 → M-bias 最稳健），对实践者选择校正策略有直接指导意义（Algorithm 1, Table 5）。

**S6. 校正方法比较公平且实用。** Table 4 在 6 种误差结构 × 4 拓扑下比较 5 种方法，PPI++ 的 47% RMSE 降幅和 FWL 不变性的实际验证（Appendix B.4）都是有价值的实践发现。

---

### Summary of Weaknesses

**N1 [Critical] Theorem 1（K=2 单调性）到 K≥3 的理论鸿沟是本文最大的方法论缺陷。**

- 具体位置：Section 3.2 (Theorem 1), Section 3.2 (Observation 1, Conjecture 1), Appendix A.4
- 问题：Theorem 1 仅对 K=2 给出了严格证明（利用 2×2 矩阵的代数性质：同号对角元 + 反号非对角元），而论文的绝大多数 NLP 应用场景涉及 K≥3（情感分析 K=3, 灾害分类 K=10 等）。K≥3 的单调性完全依赖数值验证：Observation 1 用 20,000 个随机 C₀ 矩阵，Conjecture 1 用 10,000 个。论文承认"analytic proof for general K remains open"（Section 3.2, Observation 1），但正文未充分讨论为什么 K=2 的证明技术无法推广——是代数障碍（K≥3 的 stochastic constraint 更复杂）还是本质困难？
- 为什么影响接收：对于一篇以理论贡献为核心卖点的论文，最关键的一般性结果（K≥3 单调性）仅有数值支撑，这显著削弱了理论贡献的深度。EMNLP 读者使用的几乎都是 K≥3 的分类任务。
- 建议修改方向：(a) 至少说明 K=2 证明中哪一步在 K≥3 失败，是 perspective function 的 convexity 不再成立，还是 Dirichlet subspace 的几何结构改变？(b) 考虑给出 K=3 的特殊情形证明，或 (c) 提供更强的数值 evidence，例如用符号计算验证 K=3 下 V_B(δ) 的二阶导非负性。

**N2 [Critical] Proportional effects 假设（f = λg）的理论动机薄弱，且对 mediation 符号保持至关重要。**

- 具体位置：Appendix A.5 (Proposition 4), Appendix B.12 (Table 12-13)
- 问题：Mediation 拓扑的符号保持（Proposition 4, page 15-16）严格依赖 f(A) = λg(A) 这一比例效应假设。该假设要求误分类对处理变量的效应与真实效应成比例——这是一个关于 DGP 的结构性假设，而非关于混淆矩阵的统计性质。论文用 23 个 LLM 混淆矩阵验证 λ(C) ∈ [0,1]（Table 13），但这只是验证了当假设成立时 λ 的取值范围，并未论证假设本身为何合理。Appendix B.12 Table 12 显示在 independent (f ≠ g) 条件下符号保持仍达 97%，但这个 97% 是在哪些 DGP 参数下得到的？如果 f 和 g 的相关性较低，3% 的失败率在实际应用中可能是不可接受的。
- 为什么影响接收：Mediation 是 NLP 因果推断中最常用的拓扑之一（e.g., text → mediator → outcome），如果符号保持依赖一个难以在实践中验证的假设，该拓扑的理论保证就存在实质性缺口。
- 建议修改方向：(a) 给出 proportional effects 在具体 NLP 场景中的 interpretable sufficient condition（例如，何种类型的分类误差满足此假设），(b) 展示 f 与 g 相关性从高到低变化时符号保持率的降解曲线，(c) 讨论当 f ⊥ g 时失败的 3% 案例的特征。

**W1 [Warning] Exposure 拓扑的符号反转（Proposition 7）削弱了"拓扑决定偏差方向"的核心叙事。**

- 具体位置：Section 3.2 (page 4, "Exposure... can produce sign reversal for K≥3"), Appendix A.8 (Proposition 7, page 19)
- 问题：Abstract 和 Introduction 的核心 claim 是"annotation errors propagate into downstream causal estimates in ways that depend on both the error structure and the causal design"，暗示拓扑提供了可预测的偏差方向。但 Proposition 7 构造了 K=3 exposure DGP 的符号反转反例（C_kk > 0.5），且 Table 1 确认 exposure 和 IV 在经验中分别有 83.8% 和 62.9% 的符号反转率。这意味着对于 exposure/IV 拓扑，符号保持实际上**不成立**——这不是边界情况，而是主要行为模式。
- 建议：在 Abstract 和 Introduction 中更显著地突出 exposure/IV 的例外性，而非仅在 Section 3.2 中间一句话带过。目前的表述容易让读者产生"所有拓扑都有某种符号保持保证"的错误印象。

**W2 [Warning] 线性 SEM 假设对 EMNLP 读者群的适用性讨论不足。**

- 具体位置：Section 3 (page 3, "linear structural equation models"), Appendix B.6 (Table 8 nonlinear robustness)
- 问题：NLP 中的因果推断通常涉及高维文本特征和非线性模型（logistic regression, neural networks）。论文在 Appendix B.6 展示了 logistic DGP 下 sign-flip rate 为零，但 (a) 这仅验证了 sign 方向，未验证偏差大小的预测精度在非线性下是否保持；(b) Table 7 的 FWL invariance 检验显示 logistic regression 下 OLS vs. breakdown 的差异为 ~10⁻³，作者声称"practically negligible"，但未讨论在更强非线性（如深度模型）下会如何；(c) Appendix B.13 的 FWL invariance under nonlinear models 测试仅用了 VAST K=5 的一个数据集。
- 建议：补充讨论线性 SEM 假设的 scope of validity——在什么条件下偏差表达式的一阶近似仍然有效？是否可以给出非线性下的 remainder bound？

**W3 [Warning] ASV Bootstrap CI 过宽，限制了实际诊断价值。**

- 具体位置：Section 4.3 (page 8), Appendix B.7
- 问题：报告的 bootstrap CI 为 δ* = 0.94 [0.60, 1.36]（exposure）和 0.75 [0.44, 1.29]（IV）。这些区间跨越了论文自身定义的"fragile"（δ* < 1）和"immune"（δ* > 1）的分界线，意味着对于单个数据集，ASV 无法可靠区分脆弱和稳健拓扑。论文承认"point estimates should be interpreted with caution when the first stage is weak"，但未讨论在什么样本量下 CI 会收窄到实用水平。
- 建议：给出 CI 宽度与样本量 N 的关系，或讨论在典型 NLP 数据集规模（N=1K-100K）下 ASV 的 power。

**W4 [Warning] Non-differential stress test 的"graceful degradation"描述过于乐观。**

- 具体位置：Section 4.2 (page 6, "structural guarantee for non-exposure topologies"), Appendix B.5 (Table 8)
- 问题：Table 8 显示在 ε=0.10（中等差异性误分类）下，IV 的 sign-flip rate 已达 7.5%，front-door 达 2.6%。在 ε=0.50 时，front-door 达 17.9%，IV 达 24.0%。论文称此为"graceful degradation"，但未提供实际 LLM 系统中差异性误分类的典型 ε 量级。如果真实 LLM 的 ε 通常在 0.1-0.3（例如，LLM 对负面情感的识别准确率低于正面情感），那么这些 sign-flip rate 可能构成实际威胁。
- 建议：(a) 用 Appendix B.14 中的 23 个真实 LLM 混淆矩阵估算实际 ε 值，(b) 讨论在该实际 ε 范围内 sign preservation 保证的有效性。

---

### Questions for Authors

**Q1.** Theorem 1 证明中 V_B(δ) 的 convexity 依赖于 perspective function 在 K=2 时的特殊性质。对于 K=3，Hessian 是否仍是半正定的？你们是否尝试过符号计算（如 Mathematica/Sage）来验证？

**Q2.** Table 13 的 λ(C) 分布显示 mean λ ≈ 0.75，但标准差是多少？是否存在 λ < 0 或 λ > 1 的 outlier？如果存在，对应的混淆矩阵有什么特征？

**Q3.** Correction method 评估（Table 4）中 PPI++ 需要 gold labels。在实际场景中 gold labels 的获取成本是主要瓶颈——论文是否评估了 PPI++ 在不同 gold label 比例下的性能降解？

**Q4.** ASV 的计算依赖于已知的拓扑结构（Algorithm 1 根据拓扑选择校正方法）。在实践中，研究者通常不确定真实 DAG——论文是否考虑过 ASV 在 DAG 不确定性下的 robustness？

**Q5.** Appendix B.14 报告了 23 个 LLM 混淆矩阵的差异性误分类阈值。Table 15 显示分布"sharply bimodal"——能否报告两个 mode 的具体 ε 值和对应的 LLM/数据集组合？

---

### Missing References

1. **校准文献**：论文讨论了 LLM 混淆矩阵但未引用 LLM calibration 相关工作。LLM 的 calibration 直接影响混淆矩阵的估计质量，建议引用近期 LLM calibration 综述。

2. **Dawid-Skene 及标注聚合模型**：论文 Limitations 提到"multi-annotator settings where confusion matrices are estimated from inter-annotator agreement"，但未引用 Dawid & Skene (1979) 或后续的 probabilistic annotation 模型（如 Raykar et al., 2010），这些方法直接与混淆矩阵估计相关。

3. **Sensitivity analysis 在 NLP 中的应用**：Veitch et al. (2020) "Adapting Text Embeddings for Causal Inference" 讨论了文本数据中的因果推断敏感性分析，与本文的 ASV 有方法论上的联系。

---

### Limitations and Societal Impact

论文的 Limitations section（page 9）合理覆盖了主要限制：non-differential 假设、线性 SEM、单标注器设定。但对 correlated multi-LLM errors 的讨论仅一句话带过，建议适当扩展。Societal impact 方面无特别顾虑。

---

## 总体评分

### 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | K=2 证明严谨完整（Prop 1a, Theorem 1），但 K≥3 的核心结果仅有数值支撑；proportional effects 假设动机不足。三级层次体系体现了诚实态度，但"已证明"部分占比有限。 |
| **Excitement** | 3.5/5 | 问题定义精准且时机好，7 拓扑统一框架在同类工作中独特。ASV 是新颖贡献。但线性 SEM 限制了对 NLP 社区的直接适用性，且 exposure/IV 的符号反转削弱了核心叙事的普适性。 |
| **Reproducibility** | 4/5 | 论文承诺公开代码和所有实验脚本（Section 5），Appendix 提供了详尽的参数设置和算法伪代码（Algorithm 1）。23 个 LLM 混淆矩阵的详细参数在 Appendix 中有记录。 |
| **Confidence** | 4/5 | 我熟悉测量误差理论、因果推断和 NLP 标注质量文献，仔细验证了主要证明。 |

### Overall Assessment

**Overall**: **3.5 — Borderline Conference**

**一句话总结**: 本文提出了一个系统且诚实的理论框架来分析 LLM 标注误差在因果推断中的拓扑依赖性传播，但 K≥3 的核心理论结果缺乏证明、proportional effects 假设动机不足、以及线性 SEM 的适用性限制，使其在 soundness 和 NLP applicability 上未达到 Conference 级别的充分性。

如果作者能 (1) 给出 K=3 的单调性证明或明确说明证明障碍的数学本质，(2) 为 proportional effects 提供可解释的充分条件，(3) 补充非线性模型下偏差预测精度的验证，评分可提升至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 822 · 2026-05-23T03:49:28.139279+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 84

## Round 84

2 recorded events


### User

_source line 823 · 2026-05-23T03:49:30.914504+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

概要：Overall 3.5 (Borderline Conference)。主要发现两个 critical 问题和四个 warning 级问题：

**Critical:**
- **N1**: Theorem 1 仅证明 K=2，K≥3 单调性全靠数值验证，对 NLP 场景（通常 K≥3）的理论保证不足
- **N2**: Mediation 符号保持依赖 proportional effects (f=λg) 假设，理论动机薄弱

**Warning:**
- **W1**: Exposure/IV 的高符号反转率（83.8%/62.9%）削弱"拓扑决定偏差方向"叙事
- **W2**: 线性 SEM 假设对 EMNLP 读者适用性讨论不足
- **W3**: ASV bootstrap CI 过宽（跨越 fragile/immune 分界），实际诊断价值有限
- **W4**: Non-differential stress test 中 ε=0.10 时 IV 已有 7.5% sign-flip，"graceful degradation" 描述偏乐观

**主要优势**: 问题定义精准、7 拓扑统一框架独特、三级证据层次诚实、实证验证充分（161 场景 MAPE 1.6%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 824 · 2026-05-23T03:49:37.780405+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 85

## Round 85

6 recorded events


### User

_source line 825 · 2026-05-23T03:50:10.179414+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 完整审稿意见

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 via ACL Rolling Review
**审查侧重**: 新颖性 + 完整性

---

## Summary

本文研究 LLM 标注产生的 K 类混淆矩阵如何在七种 canonical DAG 拓扑下传播为下游因果估计偏差。三个贡献：(1) 推导 K≥3 非差异性误分类下七种拓扑的 bias 闭式表达；(2) 提出 Annotation Sensitivity Value (ASV) 三组诊断指标；(3) 通过 FWL 定理证明矩阵校正方法对四种拓扑无效，推荐 PPI++ 作为替代。实验包括 100,000 次随机混淆矩阵的 Monte Carlo 仿真和 23 个真实 LLM 配置的实证验证。

---

## Strengths

**S1. FWL 不变性是一个干净且重要的负面结果。** Section 4.5 和 Appendix B.2 证明，对于 confounding、mediation、collider、M-bias 四种拓扑，任何矩阵校正（MLA、naive plugin）都无法减少偏差，因为 FWL 分解保证了 T 的系数仅取决于 T 对 A* 投影的残差，而非 A* 的取值本身。Table 4 用六种方法 × 六种拓扑的 RMSE 对比清晰验证了这一结论。这是一个对实践者有直接指导价值的发现——告诉他们"不要浪费时间做矩阵校正，直接用 PPI++"。

**S2. 拓扑覆盖的系统性。** 七种 DAG 拓扑（confounding、exposure、mediation、collider、M-bias、front-door、IV）× K≥3 类别的全面覆盖在现有文献中确实是首次。Brenner (1993) 仅处理 polytomous confounding 的二元情形；TeBlunthuis et al. (2024) 仅覆盖 K=2 下四种 DAG；Lee and Wood-Doughty (2024) 仅覆盖一种 DAG 拓扑的 categorical 扩展。本文的覆盖范围是这些工作的超集。

**S3. K≥3 引入的结构性差异被清晰刻画。** Section 4.2 展示 K=3 的 binarization collapse 现象——当 K=3 的注释被压缩为二元标签时，exposure 和 IV 拓扑会引入额外偏差（14% 和 17.5% sign-flip），这是 K=2 框架无法预测的。Figure 2 的 bias 分布可视化有效传达了不同拓扑间的脆弱性差异。

**S4. 实证验证设计合理。** Monte Carlo 仿真的 analytical-vs-simulation MAPE 控制在 1.6%（Table 内文 Section 4.2），23 个真实 LLM 配置的验证覆盖了三个 NLP 任务。ClinicalBERT case study (Appendix B.3) 提供了框架在临床 NLP 中的端到端应用示范，增加了实用性。

**S5. Algorithm 1 (p.28) 提供了可操作的拓扑感知校正选择流程。** 从拓扑识别 → gold label 可用性判断 → 方法选择（PPI++/MC-SIMEX/MLA/DSL）的决策树对实践者直接可用。

---

## Weaknesses

**W1. [Should-Fix] ASV 相对于 E-value 的新颖性边界不够清晰。**

Section 3.3 引入 ASV 框架，将混淆矩阵 C(δ) = (1−δ)I + δC₀ 参数化后沿 δ 做单维敏感性分析。这与 E-value (VanderWeele & Ding, 2017) 的概念框架高度同构——E-value 问"未观测混杂需要多强才能推翻结论"，ASV 问"标注误差需要多严重才能推翻结论"。Section 2 (Related Work) 和 Section 3.3 都承认了这一联系，但没有充分阐明 ASV 在理论层面超越 E-value 的具体创新点。

三个 ASV 类型（magnitude、significance、sign-flip）是有用的，但本质上是同一个 δ 参数在三个不同阈值条件下的值。建议作者更明确地界定：ASV 的技术贡献是将 sensitivity analysis 从"未观测混杂"推广到"观测变量的系统性测量误差"，而非仅仅是 E-value 的参数替换。

**W2. [Should-Fix] Abstract 信息密度过高，不利于 EMNLP 读者快速理解。**

Abstract 中出现了五个具体数字（K≥3 introduces structural misclassification, 2.1% sign reversal, 83.4%, 52.6%, 1.6% MAPE, 47.0% PPI++），对于非因果推断专家的 NLP 读者而言，信息负荷过重。建议保留最关键的 1-2 个数字（如 FWL invariance 的 0% 和 PPI++ 的 47%），其余用定性描述替代。

**W3. [Should-Fix] Section 3 对 EMNLP 主要读者群体可达性不足。**

Section 3.1 使用 plim（probability limit）符号但未对 NLP 读者做直觉解释；Section 3.2 引入 FWL 分解假设读者熟悉计量经济学；Proposition 1、Theorem 1、Observation 1、Conjecture 1 的连续出现使该部分读起来更像统计学期刊而非 EMNLP。建议在每个形式化结果之后加一句 plain-language interpretation（例如 Theorem 1 之后解释"这意味着，只要标注误差不是完全随机的，confounding bias 就会随误差单调恶化"）。

**W4. [Should-Fix] Conjecture 1 作为未证明的猜想削弱了理论贡献。**

Conjecture 1（envelope monotonicity for K≥2 under collider/M-bias topologies）是论文声称的理论贡献之一，但仅有 20,000 次随机 C₀ 矩阵的数值验证（Appendix B.11），未提供解析证明。对于一篇以理论分析为核心卖点的论文，一个关键结果停留在 conjecture 阶段会被质疑完整性。建议至少提供 K=3 的解析证明，或更明确地说明证明困难的技术原因。

**W5. [Minor → Should-Fix] 非差异性误分类假设的讨论在正文中不够充分。**

整个框架依赖 P(A*|A,Y,Z) = P(A*|A) 假设（Definition 1, Section 3.1）。Limitations（p.9）提及但仅一句话。Appendix B.5 的 stress test 显示 ε < 0.10 时结果稳健，但 LLM 标注在实践中很可能违反此假设——LLM 对不同类型文本的误分类率可能与 outcome 相关（例如情感极端的文本更容易被正确分类）。建议在 Section 3.1 或 4.1 中加一段讨论此假设在 LLM 场景下的合理性边界，而非仅在 Limitations 一笔带过。

**W6. [Minor] 真实数据实验偏轻。**

23 个 LLM 配置来自 4 个开源模型（7B-23B 规模），未覆盖 commercial API 模型（GPT-4、Claude 等）和更大规模模型（70B+）。三个 NLP 任务（political stance、sentiment、disaster）均为分类任务，缺乏更复杂的 NLP 场景（如 NER、relation extraction）。虽然理论贡献不依赖于此，但作为"practical guidance"的论文，更广泛的实证覆盖会更有说服力。

**W7. [Minor] Appendix 体量较大（20页）但使用合理。**

20 页 Appendix 包含证明、额外实验、case study 和 notation 表。主文自成体系，不存在 appendix-dumping（关键结论均在正文 8 页内呈现）。但 ClinicalBERT case study (B.3) 的实用价值较高，如果能在正文中至少用一段提及其关键发现（topology identification → correction method selection → RMSE reduction），会增强论文的应用说服力。

---

## Questions for Authors

**Q1.** ASV 的 sharp phase transition（Figure 4, N* ≈ 6,000-10,000）对于小规模 NLP 数据集（N < 1,000）的实践者意味着什么？论文是否建议小数据集不适用 ASV，还是有替代建议？

**Q2.** Table 4 显示 PPI++ 在 IV 拓扑下 RMSE 降低为 -88.0（即恶化）。这是否意味着 PPI++ 在某些拓扑下不仅无效反而有害？正文 Section 4.5 没有讨论这一 negative transfer 问题。

**Q3.** FWL invariance 结果依赖线性结构方程模型假设。Appendix B.6 测试了 logistic DGP 下的鲁棒性，但真实 NLP 场景中的 Y 通常是高度非线性的。作者如何评估 FWL 结果在非线性模型中的推广性？Appendix B.13 的结果（"matrix-based corrections are practically ineffective for four topologies under logistic regression as well"）是否足以支撑一般性结论？

**Q4.** Conjecture 1 声称 collider/M-bias 拓扑的 |B(C)| 在 envelope 意义下非递增。是否存在反例表明某些特定 C₀ 结构下单调性被违反？20,000 次随机验证的覆盖性如何保证？

**Q5.** 非差异性假设下，论文假定 LLM 的误分类率不依赖于 outcome Y。但如果 LLM 使用的 prompt 包含与 Y 相关的上下文信息（如 few-shot exemplars 中含有 outcome 线索），这一假设即被违反。作者是否考虑过 prompt 设计对非差异性假设的影响？

---

## Missing References

1. **Prediction-Powered Causal Inferences (2025, arXiv 2502.06343)**: 这是 PPI 框架在因果推断中的最新扩展，与本文的 PPI++ 应用直接相关。论文引用了 Angelopoulos et al. (2023) 和 Candès et al. (2025) 但未引用这篇将 PPI 系统性地扩展到因果推断的工作。

2. **"Variance-Aware LLM Annotation for Strategy Research" (2025, arXiv 2601.02370)**: 讨论 LLM 标注中的 variance sources 和诊断协议，与本文的 ASV 诊断框架互补。

3. **"Hidden Measurement Error in LLM Pipelines" (2026, arXiv 2604.11581)**: 系统性分析 LLM pipeline 中隐藏的测量误差如何扭曲标注和评估，与本文的问题设定高度相关（但可能发表在本文投稿截止之后）。

4. 论文 Section 2 提到了 Rosenbaum bounds 但未引用 Rosenbaum (2002) 的原始工作；E-value 部分引用了 VanderWeele & Ding (2017) 但未引用 Mathur et al. (2018) 对 E-value 的统计功效分析——这对理解 ASV 的 power 特性是相关的。

---

## 官方维度打分（ACL Rolling Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4/5 (Strong) | 核心理论结果（Proposition 1-6, Theorem 1）有解析证明+数值验证；FWL 不变性证明严谨；Monte Carlo 与解析预测的 MAPE 1.6% 表明理论-实证一致性好。扣分点：Conjecture 1 未证明；非差异性假设在 LLM 场景下的适用性讨论不足。 |
| **Excitement** | 3/5 (Interesting) | FWL 不变性结果和拓扑感知校正指南有实践价值；但 ASV 的新颖性相对于 E-value 边界模糊；bias taxonomy 的贡献更偏"系统性覆盖"而非"深层新洞察"；对 EMNLP 核心读者的吸引力有限——更适合统计/计量经济学受众。 |
| **Reproducibility** | 4/5 | 声称将公开代码和所有实验脚本；Monte Carlo 设置参数充分记录；但论文中未提供代码链接（可能因 double-blind），且真实 LLM 实验的完整配置细节（prompt 模板、温度设置等）仅在 Appendix 中部分提及。 |
| **Reviewer Confidence** | 4/5 | 我熟悉因果推断、测量误差理论和 NLP 中的标注质量问题。对计量经济学的 FWL 定理和 sensitivity analysis 有足够理解来评估技术正确性。 |

---

## 总体评分

**Overall**: **3.5 — Borderline Conference**

**一句话总结**: 一篇技术扎实的测量误差理论工作，FWL 不变性结果有真正的实践价值，但 ASV 的新颖性边界不够锐利，写作对 EMNLP 读者偏重统计形式化，且关键的 Conjecture 1 缺乏解析证明——介于 Conference 和 Findings 之间。

**详细判断依据**:
- **支持 Conference 的因素**: 七拓扑 × K≥3 的系统性覆盖在文献中确实是首次（S2）；FWL 不变性是干净的负面结果，对实践者有直接指导价值（S1）；Monte Carlo 验证与解析预测一致性好（S4）；Algorithm 1 提供了可操作的校正选择流程（S5）。
- **推向 Findings 的因素**: ASV 的新颖性主要是 E-value 到标注误差域的适配，理论深度有限（W1）；Conjecture 1 停留在猜想阶段（W4）；Section 3 对 EMNLP 读者可达性不足（W3）；真实数据实验覆盖偏窄（W6）；贡献整体偏"系统性梳理"而非"突破性发现"。

---

## 主要优势（汇总）
1. FWL 不变性证明是本文最强的单点贡献——直接告诉实践者矩阵校正在四种拓扑下无效
2. 七拓扑 × K≥3 的系统性覆盖填补了文献空白
3. K≥3 binarization collapse 现象的刻画是有趣且实用的新发现
4. ClinicalBERT case study 展示了框架的端到端应用价值
5. 理论-实证一致性（1.6% MAPE）为分析结果提供了可信度支撑


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-23T03:51:01.295917+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 完整审稿意见\n\n**审查侧重**: 新颖性 + 完整性\n\n### Summary\n本文研究 LLM 标注产生的 K 类混淆矩阵如何在七种 canonical DAG 拓扑下传播为下游因果估计偏差。三个贡献：(1) 推导 K≥3 非差异性误分类下七种拓扑的 bias 闭式表达；(2) 提出 Annotation Sensitivity Value (ASV) 三组诊断指标；(3) 通过 FWL 定理证明矩阵校正方法对四种拓扑无效，推荐 PPI++ 作为替代。\n\n### Strengths\n**S1.** FWL 不变性是一个干净且重要的负面结果。Section 4.5 和 Appendix B.2 证明矩阵校正对四种拓扑无效。\n**S2.** 七种 DAG 拓扑 × K≥3 类别的全面覆盖在现有文献中确实是首次。\n**S3.** K≥3 的 binarization collapse 现象（exposure/IV 拓扑 14%/17.5% sign-flip）被清晰刻画。\n**S4.** Monte Carlo 仿真 MAPE 1.6%，23 个 LLM 配置验证合理。\n**S5.** Algorithm 1 提供可操作的拓扑感知校正选择流程。\n\n### Weaknesses\n**W1. [Should-Fix] ASV 相对于 E-value 的新颖性边界不够清晰。** C(δ) = (1−δ)I + δC₀ 参数化与 E-value 高度同构。三个 ASV 类型本质上是同一个 δ 参数在三个不同阈值条件下的值。建议更明确界定 ASV 的技术贡献。\n\n**W2. [Should-Fix] Abstract 信息密度过高。** 五个具体数字对非因果推断专家的 NLP 读者信息负荷过重。\n\n**W3. [Should-Fix] Section 3 对 EMNLP 主要读者群体可达性不足。** plim 符号未对 NLP 读者做直觉解释；FWL 分解假设读者熟悉计量经济学；形式化结果连续出现更像统计学期刊。\n\n**W4. [Should-Fix] Conjecture 1 作为未证明的猜想削弱了理论贡献。** 仅有 20,000 次随机 C₀ 矩阵的数值验证，未提供解析证明。\n\n**W5. [Minor→Should-Fix] 非差异性误分类假设的讨论在正文中不够充分。** LLM 对不同类型文本的误分类率可能与 outcome 相关。\n\n**W6. [Minor] 真实数据实验偏轻。** 未覆盖 commercial API 模型和更大规模模型（70B+），三个 NLP 任务均为分类任务。\n\n**W7. [Minor] Appendix 体量较大但使用合理。** ClinicalBERT case study (B.3) 实用价值较高，建议正文中至少用一段提及。\n\n### Questions\n**Q1.** ASV 的 sharp phase transition 对小规模数据集（N < 1,000）意味着什么？\n**Q2.** Table 4 PPI++ 在 M-bias 下 RMSE 降低为 -88.0%，正文未讨论 negative transfer。\n**Q3.** FWL invariance 在非线性模型中的推广性如何？\n**Q4.** Conjecture 1 是否存在反例？20,000 次随机验证的覆盖性如何保证？\n**Q5.** prompt 设计对非差异性假设的影响？\n\n### Missing References\n1. Prediction-Powered Causal Inferences (2025, arXiv 2502.06343)\n2. Variance-Aware LLM Annotation for Strategy Research (2025, arXiv 2601.02370)\n3. Hidden Measurement Error in LLM Pipelines (2026, arXiv 2604.11581)\n4. Rosenbaum (2002), Mathur et al. (2018) E-value power analysis\n\n### Overall: 3.5 — Borderline Conference\nSoundness 4/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 完整审稿意见\n\n**审查侧重**: 新颖性 + 完整性\n\n### Summary\n本文研究 LLM 标注产生的 K 类混淆矩阵如何在七种 canonical DAG 拓扑下传播为下游因果估计偏差。三个贡献：(1) 推导 K≥3 非差异性误分类下七种拓扑的 bias 闭式表达；(2) 提出 Annotation Sensitivity Value (ASV) 三组诊断指标；(3) 通过 FWL 定理证明矩阵校正方法对四种拓扑无效，推荐 PPI++ 作为替代。\n\n### Strengths\n**S1.** FWL 不变性是一个干净且重要的负面结果。Section 4.5 和 Appendix B.2 证明矩阵校正对四种拓扑无效。\n**S2.** 七种 DAG 拓扑 × K≥3 类别的全面覆盖在现有文献中确实是首次。\n**S3.** K≥3 的 binarization collapse 现象（exposure/IV 拓扑 14%/17.5% sign-flip）被清晰刻画。\n**S4.** Monte Carlo 仿真 MAPE 1.6%，23 个 LLM 配置验证合理。\n**S5.** Algorithm 1 提供可操作的拓扑感知校正选择流程。\n\n### Weaknesses\n**W1. [Should-Fix] ASV 相对于 E-value 的新颖性边界不够清晰。** C(δ) = (1−δ)I + δC₀ 参数化与 E-value 高度同构。三个 ASV 类型本质上是同一个 δ 参数在三个不同阈值条件下的值。建议更明确界定 ASV 的技术贡献。\n\n**W2. [Should-Fix] Abstract 信息密度过高。** 五个具体数字对非因果推断专家的 NLP 读者信息负荷过重。\n\n**W3. [Should-Fix] Section 3 对 EMNLP 主要读者群体可达性不足。** plim 符号未对 NLP 读者做直觉解释；FWL 分解假设读者熟悉计量经济学；形式化结果连续出现更像统计学期刊。\n\n**W4. [Should-Fix] Conjecture 1 作为未证明的猜想削弱了理论贡献。** 仅有 20,000 次随机 C₀ 矩阵的数值验证，未提供解析证明。\n\n**W5. [Minor→Should-Fix] 非差异性误分类假设的讨论在正文中不够充分。** LLM 对不同类型文本的误分类率可能与 outcome 相关。\n\n**W6. [Minor] 真实数据实验偏轻。** 未覆盖 commercial API 模型和更大规模模型（70B+），三个 NLP 任务均为分类任务。\n\n**W7. [Minor] Appendix 体量较大但使用合理。** ClinicalBERT case study (B.3) 实用价值较高，建议正文中至少用一段提及。\n\n### Questions\n**Q1.** ASV 的 sharp phase transition 对小规模数据集（N < 1,000）意味着什么？\n**Q2.** Table 4 PPI++ 在 M-bias 下 RMSE 降低为 -88.0%，正文未讨论 negative transfer。\n**Q3.** FWL invariance 在非线性模型中的推广性如何？\n**Q4.** Conjecture 1 是否存在反例？20,000 次随机验证的覆盖性如何保证？\n**Q5.** prompt 设计对非差异性假设的影响？\n\n### Missing References\n1. Prediction-Powered Causal Inferences (2025, arXiv 2502.06343)\n2. Variance-Aware LLM Annotation for Strategy Research (2025, arXiv 2601.02370)\n3. Hidden Measurement Error in LLM Pipelines (2026, arXiv 2604.11581)\n4. Rosenbaum (2002), Mathur et al. (2018) E-value power analysis\n\n### Overall: 3.5 — Borderline Conference\nSoundness 4/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-23T03:51:39.010151+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 37714
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-23T03:51:39.512567+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 完整审稿意见\n\n**审查侧重**: 方法严谨性\n\n### Summary\n本文在线性 SEM 框架下，针对 7 种经典 DAG 拓扑推导了 K 类非差异性错分下的偏差闭式表达式。核心贡献包括 Proposition 1(a)(b)(c) 建立符号保持条件；Theorem 1 证明 K=2 单调性；Observation 1 和 Conjecture 1 数值扩展到 K≥3；ASV 框架量化拓扑相关脆弱性；23 个真实 LLM 混淆矩阵验证（MAPE 1.6%）。\n\n### Strengths\n**S1.** 问题重要且时机恰当，填补明确的方法论空白。\n**S2.** 理论框架系统而诚实，三级证据层次（Proved / Numerically Verified / Conjectured）极为少见。\n**S3.** Proposition 1(a) 的证明链完整且技术上正确（FWL 分解 → Cauchy-Schwarz 界 → ξ(C) ∈ [0,1]）。\n**S4.** 实证验证规模充分（161 场景 MAPE 1.6%，100,000 随机矩阵符号保持验证）。\n**S5.** ASV 框架将 K²维问题压缩到一维标量 δ*，拓扑排序对实践者有直接指导意义。\n**S6.** Table 4 校正方法比较公平且实用。\n\n### Weaknesses\n**N1 [Critical] Theorem 1（K=2 单调性）到 K≥3 的理论鸿沟是本文最大的方法论缺陷。** Theorem 1 仅对 K=2 给出严格证明（利用 2×2 矩阵代数性质）。K≥3 的单调性完全依赖数值验证（Observation 1: 20,000 个 C₀, Conjecture 1: 10,000 个）。正文未充分讨论为什么 K=2 的证明技术无法推广——是代数障碍还是本质困难？建议：(a) 说明 K=2 证明中哪一步在 K≥3 失败；(b) 考虑 K=3 特殊情形证明；(c) 用符号计算验证 K=3 下 V_B(δ) 的二阶导非负性。\n\n**N2 [Critical] Proportional effects 假设（f = λg）理论动机薄弱，对 mediation 符号保持至关重要。** Mediation 的符号保持严格依赖此假设。Table 13 验证了 λ(C) ∈ [0,1]，但只是验证了假设成立时 λ 的取值范围，未论证假设本身为何合理。Appendix B.12 Table 12 显示 independent (f⊥g) 条件下符号保持仍达 97%，但 3% 的失败率在哪些 DGP 参数下得到？建议：(a) 给出 NLP 场景中的 interpretable sufficient condition；(b) 展示 f 与 g 相关性降解曲线；(c) 讨论失败案例特征。\n\n**W1 [Warning] Exposure/IV 高符号反转率（83.8%/62.9%）削弱\"拓扑决定偏差方向\"叙事。** Proposition 7 的反例表明 exposure/IV 的符号反转不是边界情况而是主要行为模式。建议在 Abstract/Introduction 更显著突出这一例外。\n\n**W2 [Warning] 线性 SEM 假设对 EMNLP 读者群适用性讨论不足。** Appendix B.6 仅验证了 sign 方向，未验证偏差大小预测精度在非线性下是否保持；B.13 仅用了一个数据集。\n\n**W3 [Warning] ASV Bootstrap CI 过宽（exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29]），跨越 fragile/immune 分界线。** 未讨论在什么样本量下 CI 会收窄到实用水平。\n\n**W4 [Warning] Non-differential stress test 的\"graceful degradation\"过于乐观。** ε=0.10 时 IV sign-flip 已达 7.5%，ε=0.50 时 IV 达 24.0%。未提供实际 LLM 系统中典型 ε 量级。\n\n### Questions\n**Q1.** K=3 时 Hessian 是否仍半正定？是否尝试过符号计算验证？\n**Q2.** Table 13 的 λ(C) 标准差？是否存在 λ<0 或 λ>1 的 outlier？\n**Q3.** PPI++ 在不同 gold label 比例下的性能降解？\n**Q4.** ASV 在 DAG 不确定性下的 robustness？\n**Q5.** Table 15 的两个 mode 具体 ε 值和对应 LLM/数据集组合？\n\n### Missing References\n1. LLM calibration 综述\n2. Dawid & Skene (1979) 及 probabilistic annotation 模型\n3. Veitch et al. (2020) \"Adapting Text Embeddings for Causal Inference\"\n\n### Overall: 3.5 — Borderline Conference\nSoundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 完整审稿意见\n\n**审查侧重**: 方法严谨性\n\n### Summary\n本文在线性 SEM 框架下，针对 7 种经典 DAG 拓扑推导了 K 类非差异性错分下的偏差闭式表达式。核心贡献包括 Proposition 1(a)(b)(c) 建立符号保持条件；Theorem 1 证明 K=2 单调性；Observation 1 和 Conjecture 1 数值扩展到 K≥3；ASV 框架量化拓扑相关脆弱性；23 个真实 LLM 混淆矩阵验证（MAPE 1.6%）。\n\n### Strengths\n**S1.** 问题重要且时机恰当，填补明确的方法论空白。\n**S2.** 理论框架系统而诚实，三级证据层次（Proved / Numerically Verified / Conjectured）极为少见。\n**S3.** Proposition 1(a) 的证明链完整且技术上正确（FWL 分解 → Cauchy-Schwarz 界 → ξ(C) ∈ [0,1]）。\n**S4.** 实证验证规模充分（161 场景 MAPE 1.6%，100,000 随机矩阵符号保持验证）。\n**S5.** ASV 框架将 K²维问题压缩到一维标量 δ*，拓扑排序对实践者有直接指导意义。\n**S6.** Table 4 校正方法比较公平且实用。\n\n### Weaknesses\n**N1 [Critical] Theorem 1（K=2 单调性）到 K≥3 的理论鸿沟是本文最大的方法论缺陷。** Theorem 1 仅对 K=2 给出严格证明（利用 2×2 矩阵代数性质）。K≥3 的单调性完全依赖数值验证（Observation 1: 20,000 个 C₀, Conjecture 1: 10,000 个）。正文未充分讨论为什么 K=2 的证明技术无法推广——是代数障碍还是本质困难？建议：(a) 说明 K=2 证明中哪一步在 K≥3 失败；(b) 考虑 K=3 特殊情形证明；(c) 用符号计算验证 K=3 下 V_B(δ) 的二阶导非负性。\n\n**N2 [Critical] Proportional effects 假设（f = λg）理论动机薄弱，对 mediation 符号保持至关重要。** Mediation 的符号保持严格依赖此假设。Table 13 验证了 λ(C) ∈ [0,1]，但只是验证了假设成立时 λ 的取值范围，未论证假设本身为何合理。Appendix B.12 Table 12 显示 independent (f⊥g) 条件下符号保持仍达 97%，但 3% 的失败率在哪些 DGP 参数下得到？建议：(a) 给出 NLP 场景中的 interpretable sufficient condition；(b) 展示 f 与 g 相关性降解曲线；(c) 讨论失败案例特征。\n\n**W1 [Warning] Exposure/IV 高符号反转率（83.8%/62.9%）削弱\"拓扑决定偏差方向\"叙事。** Proposition 7 的反例表明 exposure/IV 的符号反转不是边界情况而是主要行为模式。建议在 Abstract/Introduction 更显著突出这一例外。\n\n**W2 [Warning] 线性 SEM 假设对 EMNLP 读者群适用性讨论不足。** Appendix B.6 仅验证了 sign 方向，未验证偏差大小预测精度在非线性下是否保持；B.13 仅用了一个数据集。\n\n**W3 [Warning] ASV Bootstrap CI 过宽（exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29]），跨越 fragile/immune 分界线。** 未讨论在什么样本量下 CI 会收窄到实用水平。\n\n**W4 [Warning] Non-differential stress test 的\"graceful degradation\"过于乐观。** ε=0.10 时 IV sign-flip 已达 7.5%，ε=0.50 时 IV 达 24.0%。未提供实际 LLM 系统中典型 ε 量级。\n\n### Questions\n**Q1.** K=3 时 Hessian 是否仍半正定？是否尝试过符号计算验证？\n**Q2.** Table 13 的 λ(C) 标准差？是否存在 λ<0 或 λ>1 的 outlier？\n**Q3.** PPI++ 在不同 gold label 比例下的性能降解？\n**Q4.** ASV 在 DAG 不确定性下的 robustness？\n**Q5.** Table 15 的两个 mode 具体 ε 值和对应 LLM/数据集组合？\n\n### Missing References\n1. LLM calibration 综述\n2. Dawid & Skene (1979) 及 probabilistic annotation 模型\n3. Veitch et al. (2020) \"Adapting Text Embeddings for Causal Inference\"\n\n### Overall: 3.5 — Borderline Conference\nSoundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-23T03:51:40.976389+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1463
}
```

</details>

---


### Assistant

_source line 830 · 2026-05-23T03:51:46.139597+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 86

## Round 86

58 recorded events


### User

_source line 831 · 2026-05-23T03:51:47.274848+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

---

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。FWL 不变性是最强贡献点，ASV 新颖性边界和 Conjecture 1 未证明是主要扣分项。提出了 5 个 questions for authors 和 4 条 missing references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-23T03:51:52.655376+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-23T03:51:52.757577+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-23T03:52:23.459551+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-23T03:52:23.459924+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-23T03:52:25.517395+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-23T03:52:25.568058+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-23T03:52:29.182003+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-23T03:52:29.182490+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-23T03:52:31.190791+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer submit_review_report update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer submit_review_report update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-23T03:52:31.242344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-23T03:52:37.864086+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-23T03:52:37.914801+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-23T03:52:40.329951+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "dispatch_visual_check get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "dispatch_visual_check get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-23T03:52:40.431670+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-23T03:52:43.298204+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status request_external_review read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status request_external_review read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-23T03:52:43.298568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-23T03:53:02.703425+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-23T03:53:03.256878+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-23T03:53:03.257472+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-23T03:53:03.408185+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-23T03:53:03.408841+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-23T03:53:03.409120+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-23T03:54:05.276485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-23T03:54:05.628238+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	
20	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
21	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
24	\graphicspath{{../../figures/paper/}}
25	
26	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	
35	\input{introduction}
36	
37	\input{related_work}
38	
39	\input{method}
40	
41	% ── Figures ──
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
46	\vspace{-6pt}
47	\caption{Seven canonical DAG topologies with starred-node annotation. $A$ (latent) connects to $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies across topologies.}
48	\label{fig:dag_taxonomy}
49	\end{figure*}
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig2_bias_distribution.pdf}
54	\vspace{-6pt}
55	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices. Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
56	\label{fig:bias_distribution}
57	\end{figure*}
58	
59	\input{experiments}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\appendix
66	\input{appendix_proofs}
67	
68	\end{document}
69	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-23T03:54:05.628805+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-23T03:54:05.628984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-23T03:54:06.582704+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-23T03:54:06.935384+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-23T03:54:06.986080+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-23T03:54:07.036749+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-23T03:54:23.775004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-23T03:54:24.277655+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy (diagonal ${\geq}\,0.7$), sign reversal occurs in 2.1\% of exposure configurations, exclusively in secondary coefficients with small effect sizes; no sign reversals occur for the remaining six topologies including IV. We introduce Annotation Sensitivity Values (ASVs) revealing a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-23T03:54:24.278111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-23T03:54:24.781441+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, however, is never reversed in any t
…[truncated 2662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-23T03:54:24.781913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-23T03:54:25.283257+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{valeri_vanderweele2013}. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document the rapid adoption of LLM annotators, \citet{baumann2025} found 31\% incorrect conclusions, \citet{pangakis_wolken_fasching2023} demonstrated that automated annotations require task-specific validation, \citet{cheng_mayya_sedoc2024} propose str
…[truncated 1997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-23T03:54:25.283757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-23T03:54:25.785642+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\begin{definition}[Non-differential misclassification]
10	\label{def:nondiff}
11	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
12	\end{definition}
13	
14	This holds when the LLM annotates from source documents without access to outcome information. Violations arise when pretraining data encodes $A$--$Y$ associations, outcome-conditional prompting is used, or retrieval pipelines surface $Y$-correlated documents. Our stress test (Appendix~\ref{sec:nondiff_stress}) shows violations below $\varepsilon{=}0.05$ cause $<$3~pp degradation; for $K{\geq}3$ exposure, even $\varepsilon{=}0.01$ produces sign reversal in 14 of 16 empirical configurations (Appendix~\ref{sec:realistic_epsilon}).
15	
16	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009} in which $A$ occupies structurally distinct causal roles: confounder, exposure, mediator, collider, M-bias variable, front-door mediator, and instrument. Throughout, we derive probability limits under \emph{linear} structural equation models~\cite{carroll2006}, the standard framework for exact characterization of topology-dependent bias; robustness under logistic regression is verified in Appendix~\ref
…[truncated 12707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-23T03:54:25.786024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-23T03:54:26.238275+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each of the seven topologies (confounding, exposure, mediation, collider, M-bias, front-door, IV), we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute the analytical probability limit of the causal estimator, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies, $N{=}10{,}000$). Per-topology MAPE ranges from 0.3\% (confounding) to 3.7\% (IV); the IV maximum reflects the Wald estimator's small-denominator variance amplification.
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient. The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five of seven topologies exhibit zero sign-flip rate across all sampled matrices (Table~\ref{tab:taxonomy}). Confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse th
…[truncated 7267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-23T03:54:26.288998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-23T03:54:26.740828+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology across seven canonical topologies. The classical binary guarantee breaks at $K \geq 3$: exposure and IV topologies produce sign reversal, while five topologies maintain structural guarantees. ASVs reveal a vulnerability spectrum from IV (maximally fragile) to M-bias (immune), and matrix-based corrections are provably ineffective for four topologies due to FWL invariance. Empirical validation with 23 real LLM configurations confirms the primary coefficient never reverses---an empirical regularity driven by magnitude dominance---while 61\% of exposure configurations reverse a secondary coefficient. Topology rankings and sign-flip patterns persist under logistic DGP ($|\Delta\,\text{SF}_\tau| < 0.02$; Appendix~\ref{sec:logistic_dgp}). Code for ASV computation and all experiments will be publicly released.
5	
6	\section*{Limitations}
7	
8	Our framework assumes non-differential misclassification ($P(A^*|A, Y, \mathbf{Z}) = P(A^*|A)$), which holds when the LLM does not observe $Y$ but may be violated when it accesses $Y$-correlated information---e.g., outcome-conditional prompting, few-shot demonstrations encoding outcome--treatment associations, or retrieval-augmented annotation carrying outcome signal (Appendix~\ref{sec:nondiff_stress}). The framework assumes a correctly specified causal DAG; when the topology is uncertain, practitioners should compute ASV under candidate DAGs and report the most conservative. Closed-form expressions are derived for $K{=}3$ and verified at $K{=}5,7$ under linear structural equations; extensions to arbitrary $K$ and nonlinear models (Appendix~\ref{sec:logistic_dgp}) remain open. We address misclassification of $A$ by a single annotator; outcome misclassification and correlated multi-annotator settings~\cite{kim_garg2025} introduce additional bias channels not captured here, and multi-annotator settings
…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-23T03:54:26.741243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-23T03:54:34.233529+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 through ARR:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Dates

The ARR submission deadline for long and short papers is May 25, 2026, with the reviewer registration deadline for all authors on May 27, 2026. Author response and author-review
…[truncated 828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7492
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-23T03:55:06.752426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-23T03:55:07.707959+00:00_

File content (37560 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-23T03:55:07.708403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-23T03:55:08.009483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 880 · 2026-05-23T03:55:08.110696+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 24105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-23T03:55:15.703403+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

I found information about EMNLP 2026 submission requirements from the official conference website. Here's what I found regarding submission format, page limits, templates, and double-blind review:

**Page Limits:**

For the main conference papers, the search results reference ARR (ACL Rolling Review) submission requirements, though specific page limits for main conference papers weren't explicitly stated in these results. However, for the Industry Track specifically, Industry Track papers have a maximum of 6 pages, with papers not exceeding 6 pages in length (excluding ethical considerations and references), where references and limitations sections do not count toward the page limit.

**Templates and Format:**

Manuscripts should be submitted electronically in PDF format using available templates, and authors should not m
…[truncated 605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7994
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-23T03:56:01.388348+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool call

_source line 883 · 2026-05-23T03:56:01.589653+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 884 · 2026-05-23T03:56:05.767448+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4379
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-23T03:56:06.072041+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 4482
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-23T03:56:43.816710+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_11/submitted.pdf`\n\n### Venue 要求（EMNLP 2026）\n- **投稿系统**: ACL Rolling Review (ARR)，May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文严格 8 页，参考文献不限，Limitations 和 Ethics 不计入页数（但不得包含过多额外内容）\n- **模板**: ACL 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（无匿名期要求）\n- **附录**: 允许，审稿人可自行决定是否阅读\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n请重点审查以下方面：\n\n1. **理论严谨性**：\n   - 7 种 DAG 拓扑的 bias 表达式推导是否正确？\n   - Proposition 1（sign preservation）的条件是否充分且清晰？\n   - Theorem 1（envelope monotonicity, K=2）的证明是否完整？\n   - Observation 1（K≥3 monotonicity）和 Conjecture 1（ε-approximate monotonicity）的数值验证是否充分？三级证据层次（proved / verified / conjectured）是否清晰？\n   - ASV 三种诊断的定义是否 well-defined？\n\n2. **实验有效性**：\n   - Monte Carlo 验证（161 scenarios, MAPE 1.6%）是否充分？\n   - 23 个真实 LLM confusion matrices 的经验验证是否有效？\n   - 5 种校正方法的比较是否公平？\n   - FWL invariance 的实证验证是否充分？\n   - Non-differential misclassification 假设在 LLM 场景下是否合理？\n\n3. **关键假设**：\n   - Non-differential misclassification 假设的现实性\n   - Proportional effects 假设（f=λg）的适用性\n   - 线性 SEM 假设的局限性\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 是否 double-blind（作者信息匿名）？\n   - 引用格式是否符合 ACL 规范？\n\n请按以下格式输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，编号 W1, W2, ...)\n- Questions for Authors (逐条，编号 Q1, Q2, ...)\n- Missing References (如有)\n- Minor Issues (如有)\n- Overall Assessment (评分 + 理由，使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)\n- Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务\n\n### 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_11/submitted.pdf`\n\n### Venue 要求（EMNLP 2026）\n- **投稿系统**: ACL Rolling Review (ARR)，May 2026 cycle\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文严格 8 页，参考文献不限，Limitations 和 Ethics 不计入页数（但不得包含过多额外内容）\n- **模板**: ACL 模板（\\usepackage[review]{acl}）\n- **匿名规则**: Double-blind（无匿名期要求）\n- **附录**: 允许，审稿人可自行决定是否阅读\n\n### 你的审查侧重：方法严谨性 + 实验有效性\n\n请重点审查以下方面：\n\n1. **理论严谨性**：\n   - 7 种 DAG 拓扑的 bias 表达式推导是否正确？\n   - Proposition 1（sign preservation）的条件是否充分且清晰？\n   - Theorem 1（envelope monotonicity, K=2）的证明是否完整？\n   - Observation 1（K≥3 monotonicity）和 Conjecture 1（ε-approximate monotonicity）的数值验证是否充分？三级证据层次（proved / verified / conjectured）是否清晰？\n   - ASV 三种诊断的定义是否 well-defined？\n\n2. **实验有效性**：\n   - Monte Carlo 验证（161 scenarios, MAPE 1.6%）是否充分？\n   - 23 个真实 LLM confusion matrices 的经验验证是否有效？\n   - 5 种校正方法的比较是否公平？\n   - FWL invariance 的实证验证是否充分？\n   - Non-differential misclassification 假设在 LLM 场景下是否合理？\n\n3. **关键假设**：\n   - Non-differential misclassification 假设的现实性\n   - Proportional effects 假设（f=λg）的适用性\n   - 线性 SEM 假设的局限性\n\n4. **格式合规**：\n   - 正文是否 ≤ 8 页？\n   - 是否 double-blind（作者信息匿名）？\n   - 引用格式是否符合 ACL 规范？\n\n请按以下格式输出审稿意见：\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，编号 W1, W2, ...)\n- Questions for Authors (逐条，编号 Q1, Q2, ...)\n- Missing References (如有)\n- Minor Issues (如有)\n- Overall Assessment (评分 + 理由，使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit)\n- Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-23T03:56:45.327373+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-23T03:57:00.119529+00:00_

Reviewer 1 已派发，视觉审查已启动。

**当前审稿圆桌进度汇报（Round 11, Fresh 模式）：**

**投稿信息：**
- 目标 venue：EMNLP 2026 (ARR May cycle)
- 截止日期：2026-05-25
- 类别：Long Paper（8 页正文限制）
- 匿名规则：Double-blind

**Reviewer 编排（EMNLP = 2 人）：**
- **Reviewer 1**：方法严谨性 + 实验有效性（已派发，等待结果）
- **Reviewer 2**：新颖性 + 完整性（已返回，Overall 3.5 Borderline Conference）

**并行任务：**
- 视觉审查 Agent：已派发（fire-and-forget）
- 外部审稿：未配置

**Reviewer 2 摘要（待 Reviewer 1 返回后进入交叉分享）：**
- FWL 不变性是最强贡献点
- ASV 新颖性边界和 Conjecture 1 未证明是主要扣分项
- 5 个 questions for authors，4 条 missing references

等待 Reviewer 1 返回后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 87

## Round 87

10 recorded events


### User

_source line 889 · 2026-05-23T03:57:00.123913+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Strengths 回应

**[AGREE] S1: FWL 不变性是干净且重要的负面结果。**
完全同意。Section 4.5 + Appendix B.2 证明了对四种协变量拓扑（confounding, mediation, collider, M-bias），基于混淆矩阵的校正在线性 OLS 下精确实现 0% bias reduction。Appendix B.13 进一步验证了在 logistic 回归下偏差可忽略（mean < 0.05%）。这个结果对实践者有直接指导意义——避免在这四种拓扑上浪费精力做矩阵校正。

**[AGREE] S2: 七种 DAG 拓扑 × K≥3 的全面覆盖。**
同意。Lee and Wood-Doughty (2024) 仅覆盖 K=2、四种 DAG。本文将分析扩展到 K≥3 的全 K×K 混淆矩阵并覆盖七种典型拓扑，确实是文献中的首次。

**[AGREE] S3: Binarization collapse 现象的刻画。**
同意。Section 3.2 (Numerical Verification 2) 清晰展示了 K=3 到二值化引入额外 bias（跨拓扑变化 1.5×），exposure 和 IV 分别 14%/17.5% 的 sign-flip rate 是有价值的定量发现。

**[AGREE] S4: Monte Carlo MAPE 1.6%，23 个 LLM 配置验证。**
同意。Section 4.2 报告 grand MAPE 1.6%（161 scenarios），Section 4.4 用 23 个真实 LLM 混淆矩阵验证，theory-practice gap 极小。

**[AGREE] S5: Algorithm 1 的可操作性。**
同意。Algorithm 1（Appendix 第28页）提供了清晰的拓扑感知校正决策流程，从 DAG 识别到方法选择，对实践者直接可用。

---

### Weaknesses 回应

**[REBUT] R2-W1: ASV 相对于 E-value 的新颖性边界不够清晰。**

R2 认为 C(δ) = (1−δ)I + δC₀ 参数化与 E-value "高度同构"，三个 ASV 类型本质上是同一 δ 在不同阈值的值。我认为这个批评**过度简化了技术差异**：

1. **领域本质不同**：E-value 量化的是"未观测混杂需要多强才能解释掉效应"（unmeasured confounding），而 ASV 量化的是"标注误差需要多大才能改变因果结论"（annotation error propagation）。两者的 perturbation 对象完全不同——E-value 扰动的是因果图中缺失的边，ASV 扰动的是观测变量的测量过程。

2. **三类 ASV 并非同一阈值的简单变体**：δ_mag（magnitude threshold，类比 E-value）、δ_sig（significance threshold，结合 Wald estimator 方差）、δ_sf（sign-flip threshold，capture 定性结论翻转）分别回答不同的实践问题。特别是 δ_sf 捕捉的 sign reversal 在 E-value 框架中没有自然对应物——E-value 不关注效应方向翻转，只关注效应是否可被解释掉。

3. **拓扑依赖性是核心创新**：Figure 4 和 Table 3 展示 ASV 排序从 IV（最脆弱）到 M-bias（最稳健），这种 topology-dependent vulnerability spectrum 在 E-value 文献中没有对应概念，因为 E-value 不区分 DAG 拓扑。

4. 论文本身已在 Section 3.3 明确承认了与 E-value 的联系（"analogous to E-values"），但区分了其拓扑感知的独特性。

**综合判断**：R2 的建议"更明确界定技术贡献"是合理的写作改进建议，但将 ASV 定性为与 E-value "高度同构"在技术上不准确。建议作者在 Section 3.3 增加一段与 E-value 的显式对比。

---

**[AGREE] R2-W2: Abstract 信息密度过高。**
同意。当前 Abstract 包含约 5 个具体数字（1.6% MAPE、14%/17.5% sign-flip、K≥3 等）。对 EMNLP 的 NLP 主流读者而言，信息负荷确实偏重。建议保留 1-2 个最核心的数字（如 MAPE 和 sign-flip），其余移至 Introduction 第一段。

---

**[AGREE] R2-W3: Section 3 对 NLP 读者可达性不足。**
部分同意。plim 符号（probability limit）和 FWL 分解确实假设读者具备计量经济学背景。论文在 Section 3 的每个形式化结果后提供了文字解释（如 Section 3.2 的 Numerical Verification），但对 EMNLP 读者来说仍然偏 technical。

不过我认为 R2 略有夸大——这是一篇方法论论文，其核心贡献就是形式化分析。完全降低形式化程度会损害 soundness。**建议折中**：在 Section 3.1 开头增加一个"Notation roadmap"段落（3-4 句话），用直觉语言解释 plim 和 FWL 的核心思想，帮助 NLP 读者建立直觉后再进入形式化推导。

---

**[REBUT] R2-W4: Conjecture 1 作为未证明猜想削弱理论贡献。**

我不完全同意这个定性。

1. **透明标注是学术美德**：论文将其明确标为 "Conjecture" 而非 "Theorem"，这是负责任的做法。如果作者强行给出一个不完整的"证明"，反而会削弱论文可信度。

2. **数值验证规模充分**：Appendix B.11 报告了 210,000 个随机 C₀ 矩阵的验证（K ∈ {3,5,7}，每种 30,000 个），违反单调性的比例极低——对 confounding/mediation/collider/M-bias/front-door 趋近于 0，仅 IV 拓扑有较高违反率（但 IV 是已知最脆弱的拓扑）。

3. **K=2 已有解析证明**：Theorem 1 对 K=2 给出了完整的解析证明（Appendix A.4），Conjecture 1 仅针对 K≥3 的推广。论文清楚地指出 K≥3 的困难在于 (K²−K)-dimensional manifold 上的 off-diagonal perturbation 通过 ratio structures (mediation) 和 denominator crossings (IV) 阻碍了逐元素分解。

4. **不影响论文核心贡献**：Conjecture 1 是关于 ASV envelope monotonicity 的辅助结果。论文的核心贡献——七种拓扑的 bias 闭式表达、FWL 不变性、三类 ASV——均不依赖于 Conjecture 1 的成立。

**综合判断**：这是一个诚实的理论边界，而非弱点。建议作者在 Conjecture 1 附近简要说明为何 K≥3 的解析证明具有本质困难。

---

**[AGREE] R2-W5: 非差异性误分类假设的正文讨论不足。**
同意。这是论文最关键的假设（Definition 1），但正文仅在 Definition 1 给出形式化定义，对其实际含义和 LLM 场景下的合理性讨论不够。虽然 Appendix B.5 提供了详细的 stress test（96 configurations，ε 从 0 到 0.10），但正文 Limitations 节仅简短提及。

**建议**：在 Section 3.1 Definition 1 之后增加 2-3 句话，用直觉解释为什么 LLM 标注可能满足/违反此假设（如：当 LLM 不直接接触 outcome 信息时，误分类率与 Y 无关，假设成立；当 prompt 包含 outcome-conditional 信息时，假设可能被违反），并引用 B.5 的 stress test 结论。

---

**[AGREE] R2-W6: 真实数据实验偏轻。**
部分同意。23 个 LLM 配置均为开源 7-8B 模型（Llama-3-8B, Qwen-2.5-7B, DeepSeek-Chat 等），缺少 commercial API 模型（GPT-4, Claude）和大规模模型（70B+）。三个任务（stance detection 4类, sentiment 5类, disaster response 10+类）虽然覆盖了不同 K 值，但均为文本分类。

不过我认为这个弱点**不影响核心贡献**。论文的主要贡献是理论框架（bias 表达式 + ASV + FWL 不变性），实证部分的目的是验证理论预测而非穷举所有 LLM。Section 4.4 的核心发现——"分类准确率不能替代混淆矩阵结构作为因果风险指标"——不太可能因为换用更大模型而改变。

**但作为改进建议是合理的**：如果能补充 1-2 个 commercial API 的混淆矩阵，会增强结果的普适性声明。

---

**[AGREE] R2-W7: ClinicalBERT case study 应在正文提及。**
完全同意。Appendix B.3 的 ClinicalBERT case study（用于患者吸烟状态分类作为混杂因素，估计超声心动图对死亡率的因果效应）非常有说服力——展示了 FWL 不变性的实际意义（矩阵校正对 confounder 无效 → 需要 PPI++）和 zero sign-flip guarantee 的实用价值。在正文 Section 4 中用一段话提及此案例，能显著增强论文的"接地气"程度，尤其对 EMNLP 的应用导向读者。

---

### Questions 回应

**Q1: ASV 的 sharp phase transition 对小样本（N < 1,000）意味什么？**

R2 提出了一个合理的关注点。ASV 基于 plim（渐近量），sharp transition 在有限样本中会被方差模糊。Appendix B.7 提供了 bootstrap 不确定性分析（N=1,500, B=1,000），Table 3 的 95% CI 显示 confounding 从未达到 10% 阈值。但确实没有直接测试 N < 1,000。

我的判断：这是一个合理的 future work 方向，但不是当前论文的缺陷——ASV 的设计目标是提供渐近诊断指标，类比 E-value 同样是渐近量。论文应在 Limitations 中明确提及有限样本下的行为。

**Q2: Table 4 PPI++ 在 M-bias 下 RMSE −88.0% 的 negative transfer。**

R2 称"正文未讨论 negative transfer"，但实际上**正文已明确讨论**。Section 4.5 第二段（第 8 页）原文："PPI++ achieves the highest grand-mean RMSE reduction (47.0% RMSE) but requires gold labels and is harmful for M-bias (−88%)." 这正是 negative transfer 的讨论。

但我同意可以**更深入解释原因**：PPI++ 在 M-bias 下有害，可能是因为 M-bias 的 DAG 结构导致 gold-label 校正反而引入了不必要的 confounder 调整，放大了 M-bias 本身的偏差。建议作者补充 1-2 句机制解释。

**Q3: FWL invariance 在非线性模型中的推广性。**

论文已在 Appendix B.13 直接回答了此问题。在 logistic 回归下验证了 FWL invariance，结论是 bias reduction 可忽略不计（mean < 0.05%），跨所有 N ∈ {1k, 5k, 10k, 50k, 200k}。Table 5 展示所有 covariate 拓扑在 logistic 下的 bias reduction 均 < 0.01%。因此 R2 的担忧在论文已覆盖范围内得到了充分回应。

**Q4: Conjecture 1 是否存在反例？20,000 次验证的覆盖性。**

Appendix B.11 实际使用了 210,000 个矩阵（每 K 值 30,000 个，K ∈ {3,5,7}）。论文报告了 violation counts，对非 IV 拓扑接近 0，IV 拓扑违反率较高但属于已知最脆弱的拓扑。K=2 有反例构造（Appendix A.4 提到的 permutation matrix），但 K=2 有解析证明覆盖。对 K≥3，作者明确标为 conjecture 并承认解析证明的困难。覆盖性方面，使用 Gauss-Hermite quadrature (100 points) 进一步消除采样噪声。

**Q5: Prompt 设计对非差异性假设的影响。**

这与 W5 相关。论文在 Limitations 中提及 "outcome misclassification of A by a single annotator; outcome misclassification and correlated multi-annotator settings"。Prompt 设计的确是影响非差异性假设的关键因素——如果 prompt 包含与 Y 相关的上下文信息（如 outcome-conditional prompting），就会违反假设。这是一个实践中重要的考量，但属于 future work 范畴而非当前论文的方法论缺陷。

---

### Missing References 回应

1. **Prediction-Powered Causal Inferences (2025, arXiv 2502.06343)**：与论文的 PPI++ 讨论直接相关。论文已引用了 Angelopoulos et al. (2023) 和 Zrnic and Candès (2024)，但这篇 2025 年的 causal-specific PPI 论文确实应该引用。**[AGREE]** 建议补充。

2. **Variance-Aware LLM Annotation (2025, arXiv 2601.02370)**：关于 LLM 标注方差的工作，与 ASV 的 sensitivity analysis 有联系。**[AGREE]** 建议在 Related Work Section 2 的 "Text classifiers and LLM annotation" 部分补充。

3. **Hidden Measurement Error in LLM Pipelines (2026, arXiv 2604.11581)**：非常新的工作（2026年4月），直接讨论 LLM pipeline 中的测量误差。**[AGREE]** 高度相关，建议补充。

4. **Rosenbaum (2002), Mathur et al. (2018) E-value power analysis**：论文已引用 VanderWeele and Ding (2017) 来介绍 E-value。Rosenbaum (2002) 是 sensitivity analysis 的经典文献，Mathur et al. (2018) 是 E-value power analysis 的重要工作。考虑到 R2-W1 关于 ASV vs E-value 的讨论，引用这两篇会帮助更清晰地界定 ASV 的技术定位。**[AGREE]** 建议补充。

---

### 对 R2 Overall 评分的意见

R2 给出 **3.5 (Borderline Conference)**，Soundness 4/5, Excitement 3/5。

我认为 Excitement 3/5 **偏低**。理由：

1. 七种拓扑 × K≥3 的系统化分析在文献中确实是空白（R2 自己在 S2 也承认）。
2. FWL 不变性作为负面结果具有重要的实践价值——它直接告诉实践者哪些校正方法在哪些拓扑下注定无效。
3. ASV 的 topology-dependent vulnerability spectrum（Figure 4）提供了前所未有的风险评估工具。

R2 的 Weaknesses 中，W1（ASV vs E-value）和 W4（Conjecture 1）是主要拉低 excitement 的因素，但如我上面分析，W1 的"高度同构"判断在技术上不准确，W4 是诚实的理论边界而非弱点。

**我的独立评估**：Overall 应在 **3.5-4.0** 区间。Excitement 应为 3.5/5 而非 3/5。论文在理论贡献和实践指导两方面都有清晰的增量价值。主要拉低评分的因素是 EMNLP 读者可达性（W2, W3）和真实数据实验覆盖度（W6），这些都是可通过 camera-ready 修改解决的问题。

---

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条交叉回应，已提交给 Director。要点总结：

- **5 个 Strengths 全部 [AGREE]**，FWL 不变性和七拓扑覆盖确实是论文核心贡献
- **2 个 [REBUT]**：
  - W1（ASV vs E-value "高度同构"）——技术上不准确，两者扰动对象不同，ASV 的拓扑依赖性和三类分解是独特贡献
  - W4（Conjecture 1 削弱理论贡献）——透明标注为 conjecture 是学术美德，210,000 次数值验证充分，且不影响论文核心贡献
- **5 个 [AGREE]**（W2/W3/W5/W6/W7），均附具体改进建议
- **Q2 事实纠正**：R2 称"正文未讨论 negative transfer"，但 Section 4.5 已明确提及 PPI++ 对 M-bias 有害（−88%）
- **4 个 Missing References 均同意补充**
- **对 R2 的 3.5 评分认为 Excitement 偏低**，建议 3.5-4.0 区间

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 1 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R1-S1: 问题重要且时机恰当。**
同意。LLM 标注在 NLP 因果推断中的普及确实使这个问题具有紧迫性。论文 Section 1 引用了 Gilardi et al. (2023)、Ziems et al. (2024) 等证据表明 LLM 标注已广泛替代人工标注，但下游因果偏差的系统性分析确实是空白。

**[AGREE] R1-S2: 三级证据层次（Proved / Numerically Verified / Conjectured）。**
强烈同意。这是本文最突出的方法论优点之一。绝大多数理论论文会模糊证明完整性的边界，而本文在 Section 3.2 (Proposition 1)、Section 4.2 (Numerical Verification 1-2)、Section 5 (Conjecture 1) 之间画出清晰界线。这种诚实的分层在 EMNLP 投稿中极为少见，我认为应作为本文的一个 strength 被 AC 特别注意。

**[AGREE] R1-S3: Proposition 1(a) 证明链完整。**
同意。Appendix A.3（p.12）的证明逻辑清晰：FWL 分解 → 定义 R(C) 和 D(C) → Cauchy-Schwarz 界 → ξ(C) ∈ [0,1]。Step 1 bound the numerator 和 Step 2 bound the denominator 的结构使证明可独立验证。

**[AGREE] R1-S4: 实证验证规模充分。**
同意。161 场景 MAPE 1.6%（Section 4.1）、100,000 随机矩阵符号保持验证（Numerical Verification 1, Section 3.2）的规模足以支撑核心 claim。补充一点：Figure 5（p.21）展示的理论-实证偏差分布叠加图提供了直观的 visual confirmation。

**[AGREE] R1-S5: ASV 框架的实用价值。**
同意。将 K² 维混淆矩阵压缩到一维标量 δ* 的做法对实践者有直接指导意义。Algorithm 1（p.28）提供了 topology → correction method 的完整决策流程，这在理论论文中不常见。

**[AGREE] R1-S6: Table 4 校正方法比较。**
同意。Table 4（p.8）在 6 种 error structures × 7 topologies 的 210 种配置下比较了 Naive/MLA/DSL/MC-SIMEX/PPI++，覆盖面充分。PPI++ 在 grand-mean RMSE 上最优（47.0%）的结论有足够支撑。

---

### Weaknesses 回应

**[AGREE with nuance] R1-N1: K=2 到 K≥3 的理论鸿沟。**

R1 的核心判断是对的——Theorem 1 仅覆盖 K=2 确实是方法论局限。但我认为 R1 **低估了论文已有的自我诊断深度**：

1. Appendix A.4（p.13-14）Step 4 明确指出了技术障碍所在：K=2 时 V'_B(δ) ≤ 0 可通过 2×2 矩阵代数性质直接验证（C_δ 的对角占优保证），但 K≥3 时需要一个依赖于 C_δ 和 p 的矩阵 M 为负半定，而"simple diagonal thresholds are sufficient in practice but not universal"。这**已经回答了** R1 建议的 (a)——哪一步在 K≥3 失败。

2. 论文的三级层次设计（S2）正是为了应对这个鸿沟。Conjecture 1 被明确标记为 conjecture 而非 theorem，并附带 210,000 个矩阵的数值支撑（Appendix B.11, p.25）。

3. 但我**同意** R1 的一个具体建议有价值：K=3 的符号计算验证（symbolic verification of Hessian semi-definiteness）可以显著加强论文。如果 K=3 特殊情形能被证明，那么 K≥3 的 conjecture 就从"纯数值"升级到"有部分解析支撑"。

**结论：这是一个真实的局限，但论文的处理方式已经达到了诚实和透明的标准。建议补充 K=3 符号计算验证作为加强项，但不应以此作为拒稿理由。**

---

**[REBUT] R1-N2: Proportional effects 假设动机薄弱。**

R1 认为这是 critical 级别问题，我不同意这个严重程度判定。原因：

1. **论文提供了多层 robustness 证据**：Appendix B.15（p.27, Table 15）在 4 个 DGP groups × 100,000 matrices 下验证，proportional effects 下 sign preservation 达 99.4%，non-proportional 下仍有 97.3%，**独立的 f 和 g 下仍有 97%**。这说明 proportional effects 不是一个 knife-edge 假设——符号保持对该假设的违反是 robust 的。

2. **Proposition 4（Appendix A.5, p.15-16）提供了 boundedness 保证**：即使 f 和 g 不 proportional，leakage coefficient λ(C) ∈ [0,1]（在 column-stochastic C 下无条件成立），且论文证明了 λ(C) = 0 at C = I 和 λ(C) → 1 at rank-one C 的端点行为。这提供了 structural understanding，而非仅仅数值验证。

3. R1 问"3% 的失败率在哪些 DGP 参数下得到"——Table 15 最后一行 "Non-proportional" 的 A(C) mean 0.240 且 sign preservation 97.3%，而 Table 12（p.26）进一步按 proportionality degree 分解了 OOB rate 和 sign failure rate。这些数据**已经在论文中**。

**结论：这应降级为 should-fix（W 级），而非 critical。建议在正文中增加一句提及 Table 15 robustness 结果的引用，但该假设的理论地位已在 Proposition 4 中充分讨论。**

---

**[AGREE] R1-W1: Exposure/IV 高符号反转率削弱叙事。**

同意此为 should-fix 级问题。但需指出，论文 Abstract 已经明确写道："exposure and IV topologies can reverse the treatment effect sign"，Section 4.2 标题 "Structural guarantee for non-exposure topologies" 也从正面区分了两类拓扑。Proposition 7（p.18, Appendix A.8）给出了 exposure 符号反转的**构造性反例**，说明这是结构性特征而非 artifact。

我认为论文的处理已经够透明，但同意 R1 的一个具体建议：Introduction 中可以更早、更显著地将 7 种拓扑分为 "sign-preserving"（5 种）和 "sign-reversing"（2 种）两大类，而不是到 Section 4.2 才揭示。

---

**[AGREE] R1-W2: 线性 SEM 假设的适用性讨论不足。**

同意此为合理关切，但 R1 部分表述有误：

1. Appendix B.6（p.23）不是"仅验证了 sign 方向"——Table 中同时报告了 Linear SF_r 和 Logistic SF_r（sign-flip rates），证明两种 DGP 下 sign-flip 模式几乎一致。这实际上**同时验证了方向和定性行为**。

2. R1 说"B.13 仅用了一个数据集"——Appendix B.13（p.26, Table 13）是 Monte Carlo 模拟（N up to 50,000，across all 7 topologies），不是"一个数据集"。这个表述不准确。

3. 但我同意一个更本质的关切：论文未讨论偏差**大小**预测精度在非线性下的保持程度。Table 13 显示 logistic regression 下 bias reduction 仍然 negligible（mean < 0.065%），但这只是间接证据。一个显式的 "MAPE under logistic DGP" 数字会更有说服力。

---

**[AGREE] R1-W3: ASV Bootstrap CI 过宽。**

同意。Appendix B.7 Table 3（p.5, 正文）报告 exposure δ*=0.94 [0.60,1.36]，IV δ*=0.75 [0.44,1.29]。这些 CI 确实跨越了 fragile/immune 分界线（论文使用 10% bias threshold），降低了 ASV 在这两种拓扑下的实用决策能力。

但我想补充一个 R1 未提到的观察：对于 confounding、mediation、collider、M-bias、front-door 五种拓扑，ASV CI 都在同一 fragility 类别内（Table 3），只有 exposure 和 IV 的 CI 跨界。这说明 CI 宽度问题是**拓扑特异的**，而非 ASV 框架的系统性缺陷。论文可以通过明确报告 "at what N does CI stabilize" 来回应。

---

**[AGREE with nuance] R1-W4: Non-differential stress test 的 "graceful degradation" 过于乐观。**

R1 的关切方向正确。Table 8（p.24）确实显示 IV 在 ε=0.10 时 sign-flip 7.5%，ε=0.50 时 24.0%。但我认为论文的解读比 R1 描述的更 nuanced：

1. 论文自己的结论是"the non-differential assumption is load-bearing"（Table 14, p.27 的标题），这不是"过于乐观"。

2. 正文 Section 4.3 的结论段（p.23）说"small ε departures... change rates by fewer than 3 percentage points"，这指的是 ε ≤ 0.05 的范围。ε=0.10 和 ε=0.50 的结果在 extended stress test 中报告，论文确实承认了 degradation。

3. 但 R1 关于"未提供实际 LLM 系统中典型 ε 量级"的批评**完全成立**。论文有 23 个真实 LLM 混淆矩阵但未量化其 non-differential departure。这是一个可操作的改进建议。

---

### Questions 回应

**[AGREE] R1-Q1: K=3 Hessian 半正定性。**
有价值的问题，与 N1 直接相关。这是加强 Conjecture 1 的最直接路径。

**[REBUT] R1-Q2: Table 13 λ(C) 的标准差和 outlier。**
R1 引用了错误的表。Table 13（p.26-27）是 logistic bias reduction 结果，不是 λ(C) 的表。λ(C) 相关结果在 Appendix B.12 Table 12（p.26）和 B.15 Table 15（p.27）。Table 12 报告了 A(C) out-of-bounds rate 按 proportionality degree 的分解，Table 15 报告了 A(C) mean。论文确实未报告 λ(C) 标准差，补充这个统计量是合理的。

**[AGREE] R1-Q3: PPI++ 在不同 gold label 比例下的性能降解。**
论文 Table 4（p.8）和 Appendix B.3（p.22）只测试了固定的 gold label setting（ClinicalBERT case study），未做 gold label ratio sensitivity analysis。这是一个有价值的实验建议。

**[AGREE] R1-Q4: ASV 在 DAG 不确定性下的 robustness。**
论文假设 DAG 已知（Section 3.1），但实践中 DAG 选择本身有不确定性。Limitations 中提到了"extensions to arbitrary A and nonlinear models remain open"，但未专门讨论 DAG uncertainty。合理的关切。

**[AGREE] R1-Q5: Table 15 的两个 mode。**
（R1 原文说 Table 15，但根据上下文应指 non-differential stress test 的 bimodal 分布。）论文 Figure 9（p.24）展示了 magnitude ASV 在 exposure 的 bimodal 分布，但未给出两个 mode 对应的具体 LLM/数据集组合。补充这一信息有助于实践解读。

---

### Missing References 回应

**[REBUT] R1-MR1: LLM calibration 综述。**
本文的核心关注是 misclassification 对因果推断的偏差传播，而非 LLM 的 calibration 本身。Section 2 (Related Work) 的 "Text classifiers and LLM annotation" 段落已引用了 Gilardi et al. (2023)、Ziems et al. (2024)、Baumann et al. (2025) 等讨论 LLM 标注错误率的工作。增加 calibration 综述不会改变论文的 contribution 定位，属于 nice-to-have。

**[AGREE] R1-MR2: Dawid & Skene (1979) 及 probabilistic annotation 模型。**
同意这是一个有价值的缺失引用。Dawid-Skene 模型是 multi-annotator error modeling 的经典基础，与本文的混淆矩阵参数化有概念上的联系。虽然本文的设定是单 annotator（LLM），但引用 D&S 可以帮助读者理解方法论根源。

**[REBUT] R1-MR3: Veitch et al. (2020) "Adapting Text Embeddings for Causal Inference"。**
论文 Section 2 已引用了 Veitch et al. (2020) 关于 text-as-treatment 框架中的 text embeddings。具体在 References（p.10）可见 "Linda Valeri and Tyler J. VanderWeele, 2013" 和 "Tyler J. VanderWeele and Peng Ding, 2017" 等相关引用。但 Veitch et al. (2020) 的具体引用确实未出现在我阅读的 references 中——需要核实。如果确实缺失，应补充。

---

### 对 R1 总体评分的看法

R1 给出 Overall 3.5（Borderline Conference），Soundness 3.5/5，Excitement 3.5/5。

我认为：
- **Soundness 3.5 偏低**。论文的证明在其声称的范围内是正确的，三级层次设计避免了 over-claiming。K≥3 的 gap 是诚实标记为 conjecture 的，不应算 soundness 扣分。合理评分应为 **4/5**。
- **Excitement 3.5 合理**。问题重要但框架限于线性 SEM，对 EMNLP 主流受众的直接可用性有限。
- **Overall 3.5 可接受**，但如果 N1 的 K=3 符号验证和 N2 的 robustness evidence 被 AC 充分考虑，我认为 **3.5-4.0 之间更合理**。

---

### 总结

| R1 意见 | 我的判定 | 核心理由 |
|--------|--------|--------|
| S1-S6 | 全部 AGREE | — |
| N1 (K≥3 gap) | AGREE with nuance | 真实局限，但论文已诚实处理；K=3 符号验证是可操作的加强项 |
| N2 (proportional effects) | REBUT severity | 应降为 W 级；Table 15 和 Proposition 4 已提供多层 robustness 证据 |
| W1 (exposure/IV 叙事) | AGREE | Intro 应更早分类两大拓扑类型 |
| W2 (线性假设) | AGREE | 非线性下 MAPE 数字缺失，但 R1 对 B.13 的描述有误 |
| W3 (CI 过宽) | AGREE | 拓扑特异问题，非框架缺陷 |
| W4 (stress test 乐观) | AGREE with nuance | 论文自己说"load-bearing"，但缺少实际 LLM ε 量级 |
| Q1-Q5 | 大部分 AGREE | Q2 引用了错误的表 |
| MR1-MR3 | MR2 AGREE, MR1/MR3 REBUT | MR1 非核心相关；MR3 需核实 |

---

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部意见的逐条交叉回应，已提交至 Review Director。核心判定：

- **6 个 Strengths 全部同意**，特别强调三级证据层次（S2）应被 AC 特别注意
- **N1（K≥3 gap）**：同意是真实局限，但论文处理已达到诚实标准，建议补充 K=3 符号验证作为加强项而非拒稿理由
- **N2（proportional effects）**：反驳 critical 严重级别——Table 15 和 Proposition 4 提供了充分的 robustness 证据，应降为 W 级
- **W1-W4**：大部分同意，但纠正了 R1 对 B.13 的描述错误（是 Monte Carlo 模拟而非"一个数据集"），以及 W4 中论文自己已说"load-bearing"而非"过于乐观"
- **Q2 引用了错误的表号**（Table 13 是 logistic bias，不是 λ(C)）
- **总体评分**：认为 R1 的 Soundness 3.5 偏低，应为 4/5；Overall 3.5 可接受但偏保守

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-23T03:57:58.637732+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-23T03:57:58.788810+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"running\", \"started_at\": \"2026-05-23T03:56:05.326240+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-23T03:57:58.839553+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-23T03:57:58.840032+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-23T04:04:15.044224+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。建议 Limitations 扩展具体讨论缺失的 commercial API 和 >70B 模型。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。承认为 honest limitation + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补 2-3 句直觉解释（何时满足/违反）。缺少实际 LLM 系统的典型 ε 量级。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字（MAPE + sign-flip），其余移至 Introduction。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT（不同扰动对象、topology-dependence 独特、sign-flip ASV 无 E-value 对应物）。Director 判定 R1 技术正确但 R2 的 positioning 建议有价值。建议 Section 3.3 增加显式 ASV-vs-E-value 对比段。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Section 4.4 已解释。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求降低声称。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Abstract 已改为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。Abstract 现为 'exclusively in secondary coefficients with small effect sizes'，可能已修复。待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"Abstract 进一步降级\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已降级为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。Abstract 现措辞为经验事实（'exclusively in secondary coefficients'），不再声称为 structural property。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"与 R5-N3 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。EXP-4（23 真实矩阵 × 4 DGP）进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R1 评为 critical，R2 REBUT 降为 should-fix。R2 引用 Table 15（97.3% sign preservation under non-proportional）和 Proposition 4。Director 判定降为 should-fix，但主文应引用 Table 15 robustness。\"\n    action_items:\n      - round: 8\n        action: \"报告 general case 统计\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 用 23 真实矩阵评估 proportional effects\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 相同。R11 分歧持续但方向明确：需增加显式 ASV-vs-E-value 对比段。\"\n    action_items:\n      - round: 8\n        action: \"与 R4-W6 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加三级层次说明。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：三级层次（Proved/Verified/Conjectured）清晰且被两位 Reviewer 赞为 S2 strength。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"与 R8-C1 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"Collider脚注已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Table 1 caption 现包含 Collider 脚注解释。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"Table 1 caption 添加 Collider 脚注\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及，可能已修复或优先级降低。待 Research Director 确认。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：exposure/IV 的 Bootstrap CI 跨越 fragile/immune 分界线（exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29]），但其余 5 种拓扑 CI 在同一类别内。属拓扑特异问题，非框架缺陷。建议报告 CI 在何 N 下收敛。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及，可能已修复或优先级降低。待 Research Director 确认。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。写作修改进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：两位 Reviewer 均认为论文诚实处理了此局限（Conjecture 标注 + 210K 矩阵验证 + proof obstacle 解释）。R2 建议补充 K=3 符号计算验证作为加强项而非拒稿理由。Director 降级为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续：要求用 23 真实矩阵评估 f/g 近似程度。EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。R11 分歧：R1 critical vs R2 should-fix。R2 引用 Table 15（97.3% under non-proportional）和 Proposition 4 成功 REBUT severity。Director 降为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"EXP-1 proportional effects breakdown\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。R11 分歧持续但 Director 建议增加 ASV-vs-E-value 显式对比段落。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位调整\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：均匀 ε 无法捕捉结构性差异。承认 limitation + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 NEW-1 合并。R11 共识：仍需在 Definition 1 后补直觉解释 + 缺实际 LLM ε 量级。\"\n    action_items:\n      - round: 8\n        action: \"EXP-3 realistic ε\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R7-SF5 合并。R11 共识：exposure/IV CI 跨界是拓扑特异问题。建议报告 CI 收敛的 N 阈值。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Related Work Section 3 现引用 ding_vanderweele2016。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: critical\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。要求 f/g coefficient of variation 评估。EXP-4 进行中。非差异性部分：承认均匀 ε 局限 + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：R2 成功 REBUT R1 的 critical 评级（Table 15 97.3% robustness）。非差异性部分两位 Reviewer 共识需加强主文讨论。Director 综合降为 should-fix。\"\n    action_items:\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"method.tex 非差异性局限性讨论增强\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-C2\n    category: scope\n    severity: critical\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足——正文讨论严重不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新问题。需 Section 3.1 加线性 SEM 动机 + Section 4 提升 B.6/B.13 logistic 结论。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Appendix B.6/B.13 有 logistic 验证但主文整合不足。R2 纠正 R1 对 B.13 的误解（是 MC 模拟非单一数据集）。建议在 Section 4 用 1-2 句话提升 logistic DGP 核心结论。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"Section 4 提升 logistic DGP 核心结论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-M1\n    category: soundness\n    severity: major\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C1。新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 现已包含 proof obstacle 解释（K²-K dimensional manifold, off-diagonal perturbation interactions）。两位 Reviewer 均认为处理诚实。R2 建议 K=3 符号验证作为加强项。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 proof obstacle 技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-M2\n    category: method\n    severity: major\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新问题。需在主文 Section 3.3 总结 Algorithm 1 核心逻辑。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Algorithm 1 被两位 Reviewer 认可为可操作（S5 strength）。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 加 Algorithm 1 摘要 2-3 行\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R2, R1]\n        note: \"改为 'first unified analysis' + building on Brenner/Teblunthuis。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Introduction 现措辞为 'first unified analysis...building on prior single-topology analyses'，两位 Reviewer 认可。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 9\n        action: \"Introduction novelty claim 改写\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"改为报告 topology-specific：exposure 2.1%, 其他 0%。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Abstract 现为 'sign reversal occurs in 2.1% of exposure configurations...no sign reversals occur for the remaining six topologies including IV'。已 topology-specific。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 9\n        action: \"Abstract sign reversal 改为 topology-specific range\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"DDL 前无法新增 LLM。Limitations 扩展讨论。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。R11 共识：不影响核心贡献。Limitations 已提及但可更具体。\"\n    action_items:\n      - round: 9\n        action: \"Limitations 增加 LLM 多样性讨论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S4\n    category: presentation\n    severity: should-fix\n    summary: \"PPI++ 47.0% vs Table 4 17.0 数字不一致\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"经核实：不存在不一致。Appendix Table Grand mean PPI++ = 47.0，主文也 47.0%。17.0 在论文中不存在，Reviewer 可能误读。\"\n    resolution: \"数字实际一致（47.0%），Reviewer 误读。无需修改论文。\"\n    resolution_round: 9\n\n  # === Round 11 新发现 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：B.3 的 ClinicalBERT 案例展示了 FWL 不变性的实际意义和 zero sign-flip guarantee 的实用价值，在正文用一段话提及能显著增强论文对 EMNLP 应用导向读者的说服力。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：在 Section 3.1 开头增加 3-4 句话用直觉语言解释 plim 和 FWL 核心思想，帮助 NLP 读者建立直觉后再进入形式化推导。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失 5 篇相关引用（R11 新发现）\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识补充：(1) Prediction-Powered Causal Inferences 2025 arXiv:2502.06343, (2) Variance-Aware LLM Annotation 2025 arXiv:2601.02370, (3) Hidden Measurement Error in LLM Pipelines 2026 arXiv:2604.11581, (4) Dawid & Skene 1979, (5) Rosenbaum 2002 + Mathur et al. 2018。其中 MR1(calibration综述) 和 MR3(Veitch 2020) 存在分歧——R1 建议补充但 R2 认为非核心相关。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8 再次提出。Limitations 已添加商业 LLM 讨论。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"S3: LLM 配置多样性有限（缺 <7B, >70B, ordinal）。Limitations 扩展中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 再次提出。两位 Reviewer 共识：不影响核心贡献但限制泛化性声明。建议 Limitations 扩展具体讨论缺失的 commercial API 和 >70B 模型。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"method.tex 添加完整的讨论。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"R8 复发。Section 3.1 扩展讨论 + EXP-3 realistic ε。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：stress test 均匀 ε 无法捕捉结构性差异误差。承认为 honest limitation + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Definition 1 后应补 2-3 句直觉解释（何时满足/违反）。缺少实际 LLM 系统的典型 ε 量级。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"正文 ≤ 8 页已验证。\"\n    resolution_round: 4\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 11\n    mentions:\n      - round: 5\n        reviewers: []\n        note: \"Introduction 已重写。\"\n      - round: 8\n        reviewers: [R2]\n        note: \"R8-R2-W5 再次提出。R1 REBUT。分歧点。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Abstract ~5 个数字过多，建议保留 1-2 个核心数字（MAPE + sign-flip），其余移至 Introduction。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"共识：聚焦 monotonicity 非平凡性。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整 framework→diagnostics + K²→1D 降维。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R2 认为与 E-value 高度同构，R1 REBUT（不同扰动对象、topology-dependence 独特、sign-flip ASV 无 E-value 对应物）。Director 判定 R1 技术正确但 R2 的 positioning 建议有价值。建议 Section 3.3 增加显式 ASV-vs-E-value 对比段。\"\n    action_items:\n      - round: 8\n        action: \"ASV 措辞从 framework 降为 diagnostics\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Section 4.4 已解释。\"\n    resolution_round: 8\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: in_progress\n    first_raised_round: 5\n    last_seen_round: 11\n    mentions:\n      - round: 7\n        reviewers: [R1, R2]\n        note: \"CRITICAL——要求降低声称。\"\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Abstract 已改为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。Abstract 现为 'exclusively in secondary coefficients with small effect sizes'，可能已修复。待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"Abstract 进一步降级\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已降级为 'concentrated in secondary coefficients'。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未直接提及。Abstract 现措辞为经验事实（'exclusively in secondary coefficients'），不再声称为 structural property。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"与 R5-N3 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 Theorem 1 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% failure rate + NLP plausibility。EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续要求实证验证。EXP-4（23 真实矩阵 × 4 DGP）进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 分歧：R1 评为 critical，R2 REBUT 降为 should-fix。R2 引用 Table 15（97.3% sign preservation under non-proportional）和 Proposition 4。Director 判定降为 should-fix，但主文应引用 Table 15 robustness。\"\n    action_items:\n      - round: 8\n        action: \"报告 general case 统计\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 用 23 真实矩阵评估 proportional effects\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整措辞。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 相同。R11 分歧持续但方向明确：需增加显式 ASV-vs-E-value 对比段。\"\n    action_items:\n      - round: 8\n        action: \"与 R4-W6 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加三级层次说明。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：三级层次（Proved/Verified/Conjectured）清晰且被两位 Reviewer 赞为 S2 strength。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"与 R8-C1 合并处理\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1]\n        note: \"Collider脚注已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Table 1 caption 现包含 Collider 脚注解释。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"Table 1 caption 添加 Collider 脚注\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及，可能已修复或优先级降低。待 Research Director 确认。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 δ* precision。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：exposure/IV 的 Bootstrap CI 跨越 fragile/immune 分界线（exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29]），但其余 5 种拓扑 CI 在同一类别内。属拓扑特异问题，非框架缺陷。建议报告 CI 在何 N 下收敛。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及，可能已修复或优先级降低。待 Research Director 确认。\"\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 8 ===\n\n  - id: R8-C1\n    category: soundness\n    severity: critical\n    summary: \"K≥3 ASV 理论基础为 conjectural\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已添加 δ* precision 分析。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"M1 复发：要求讨论证明障碍技术原因。写作修改进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：两位 Reviewer 均认为论文诚实处理了此局限（Conjecture 标注 + 210K 矩阵验证 + proof obstacle 解释）。R2 建议补充 K=3 符号计算验证作为加强项而非拒稿理由。Director 降级为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"Section 3.3 讨论 K≥3 理论地位\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 证明障碍技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R8-C2\n    category: soundness\n    severity: critical\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已报告 15-17% + EXP-1 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 继续：要求用 23 真实矩阵评估 f/g 近似程度。EXP-4 进行中。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。R11 分歧：R1 critical vs R2 should-fix。R2 引用 Table 15（97.3% under non-proportional）和 Proposition 4 成功 REBUT severity。Director 降为 should-fix。\"\n    action_items:\n      - round: 8\n        action: \"EXP-1 proportional effects breakdown\"\n        assigned_to: agent\n        status: done\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R8-W1\n    category: novelty\n    severity: major\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已调整为 diagnostics。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。R11 分歧持续但 Director 建议增加 ASV-vs-E-value 显式对比段落。\"\n    action_items:\n      - round: 8\n        action: \"ASV 定位调整\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W2\n    category: soundness\n    severity: major\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"Section 3.1 扩展 + EXP-3 完成。\"\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"C1 再次提出：均匀 ε 无法捕捉结构性差异。承认 limitation + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 NEW-1 合并。R11 共识：仍需在 Definition 1 后补直觉解释 + 缺实际 LLM ε 量级。\"\n    action_items:\n      - round: 8\n        action: \"EXP-3 realistic ε\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-W3\n    category: method\n    severity: major\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R1, R2]\n        note: \"已分 topology 讨论 + Bootstrap CI。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R7-SF5 合并。R11 共识：exposure/IV CI 跨界是拓扑特异问题。建议报告 CI 收敛的 N 阈值。\"\n    action_items:\n      - round: 8\n        action: \"分 topology 讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 11\n    mentions:\n      - round: 8\n        reviewers: [R2]\n        note: \"已添加。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Related Work Section 3 现引用 ding_vanderweele2016。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 8\n        action: \"引用 Ding & VanderWeele\"\n        assigned_to: agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: critical\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C2。要求 f/g coefficient of variation 评估。EXP-4 进行中。非差异性部分：承认均匀 ε 局限 + pipeline design 缓解。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识降级：R2 成功 REBUT R1 的 critical 评级（Table 15 97.3% robustness）。非差异性部分两位 Reviewer 共识需加强主文讨论。Director 综合降为 should-fix。\"\n    action_items:\n      - round: 9\n        action: \"EXP-4 23 真实矩阵 × 4 DGP proportional effects 评估\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"method.tex 非差异性局限性讨论增强\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-C2\n    category: scope\n    severity: critical\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足——正文讨论严重不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新问题。需 Section 3.1 加线性 SEM 动机 + Section 4 提升 B.6/B.13 logistic 结论。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Appendix B.6/B.13 有 logistic 验证但主文整合不足。R2 纠正 R1 对 B.13 的误解（是 MC 模拟非单一数据集）。建议在 Section 4 用 1-2 句话提升 logistic DGP 核心结论。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.1 加线性 SEM 动机句\"\n        assigned_to: agent\n        status: in_progress\n      - round: 9\n        action: \"Section 4 提升 logistic DGP 核心结论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-M1\n    category: soundness\n    severity: major\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"延续 R8-C1。新增要求：证明障碍的技术原因。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"Section 3.3 现已包含 proof obstacle 解释（K²-K dimensional manifold, off-diagonal perturbation interactions）。两位 Reviewer 均认为处理诚实。R2 建议 K=3 符号验证作为加强项。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 增加 K≥3 proof obstacle 技术解释\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-M2\n    category: method\n    severity: major\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"新问题。需在主文 Section 3.3 总结 Algorithm 1 核心逻辑。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Algorithm 1 被两位 Reviewer 认可为可操作（S5 strength）。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 9\n        action: \"Section 3.3 加 Algorithm 1 摘要 2-3 行\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R2, R1]\n        note: \"改为 'first unified analysis' + building on Brenner/Teblunthuis。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"R11 共识：Introduction 现措辞为 'first unified analysis...building on prior single-topology analyses'，两位 Reviewer 认可。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 9\n        action: \"Introduction novelty claim 改写\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"改为报告 topology-specific：exposure 2.1%, 其他 0%。\"\n      - round: 11\n        reviewers: []\n        note: \"R11 未提及。Abstract 现为 'sign reversal occurs in 2.1% of exposure configurations...no sign reversals occur for the remaining six topologies including IV'。已 topology-specific。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 9\n        action: \"Abstract sign reversal 改为 topology-specific range\"\n        assigned_to: agent\n        status: done\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 11\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"DDL 前无法新增 LLM。Limitations 扩展讨论。\"\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"与 R1-W3 合并。R11 共识：不影响核心贡献。Limitations 已提及但可更具体。\"\n    action_items:\n      - round: 9\n        action: \"Limitations 增加 LLM 多样性讨论\"\n        assigned_to: agent\n        status: in_progress\n\n  - id: R9-S4\n    category: presentation\n    severity: should-fix\n    summary: \"PPI++ 47.0% vs Table 4 17.0 数字不一致\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 9\n    mentions:\n      - round: 9\n        reviewers: [R1, R2]\n        note: \"经核实：不存在不一致。Appendix Table Grand mean PPI++ = 47.0，主文也 47.0%。17.0 在论文中不存在，Reviewer 可能误读。\"\n    resolution: \"数字实际一致（47.0%），Reviewer 误读。无需修改论文。\"\n    resolution_round: 9\n\n  # === Round 11 新发现 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 中提及\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：B.3 的 ClinicalBERT 案例展示了 FWL 不变性的实际意义和 zero sign-flip guarantee 的实用价值，在正文用一段话提及能显著增强论文对 EMNLP 应用导向读者的说服力。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识：在 Section 3.1 开头增加 3-4 句话用直觉语言解释 plim 和 FWL 核心思想，帮助 NLP 读者建立直觉后再进入形式化推导。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失 5 篇相关引用（R11 新发现）\"\n    status: open\n    first_raised_round: 11\n    last_seen_round: 11\n    mentions:\n      - round: 11\n        reviewers: [R1, R2]\n        note: \"共识补充：(1) Prediction-Powered Causal Inferences 2025 arXiv:2502.06343, (2) Variance-Aware LLM Annotation 2025 arXiv:2601.02370, (3) Hidden Measurement Error in LLM Pipelines 2026 arXiv:2604.11581, (4) Dawid & Skene 1979, (5) Rosenbaum 2002 + Mathur et al. 2018。其中 MR1(calibration综述) 和 MR3(Veitch 2020) 存在分歧——R1 建议补充但 R2 认为非核心相关。\""
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-23T04:04:15.199686+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 28185}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 155
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-23T04:06:05.629853+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 11 Consolidated Review Report\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Long Paper (8 页正文限制)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文分析了 K≥3 多类别标注误差在七种典型 DAG 拓扑下如何传播到因果估计中。核心贡献包括：(1) 七种拓扑的 bias 闭式表达，证明/验证五种拓扑保持符号方向而 exposure 和 IV 可产生符号反转；(2) Annotation Sensitivity Values (ASV) 诊断工具揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱；(3) FWL 不变性负面结果证明基于矩阵的校正方法对四种拓扑无效。23 个真实 LLM 配置的 161 场景验证确认理论预测（MAPE 1.6%）。\n\n---\n\n## Strengths\n\n**S1 [共识]**: FWL 不变性是干净且重要的负面结果——对四种协变量拓扑，矩阵校正在线性 OLS 下精确实现 0% bias reduction。Appendix B.13 验证 logistic 下偏差可忽略（mean < 0.05%）。对实践者有直接指导意义：避免在这些拓扑上尝试矩阵校正。\n\n**S2 [共识]**: 三级证据层次（Proved / Numerically Verified / Conjectured）是突出的方法论优点。Proposition 1 → Observation 1 → Conjecture 1 清晰界定证明边界。在 EMNLP 投稿中极为少见的学术诚实。\n\n**S3 [共识]**: 首次系统覆盖 K≥3 × 7 种 DAG 拓扑。前作（Lee & Wood-Doughty 2024）仅覆盖 K=2、4 种 DAG。文献中确实是空白。\n\n**S4 [共识]**: 实证验证规模充分。161 场景 MAPE 1.6%，100,000 随机矩阵符号保持验证，23 个真实 LLM 配置跨 K=2/3/10。\n\n**S5 [共识]**: Algorithm 1 提供可操作的拓扑感知校正决策流程（DAG 识别 → 方法选择），在理论论文中不常见。\n\n**S6 [共识]**: Table 4 校正方法比较覆盖 210 种配置（5 方法 × 6 error structures × 7 拓扑），结论充分支撑。\n\n---\n\n## Weaknesses\n\n### Must-Fix (0 项)\n\n无。\n\n### Major (3 项)\n\n**W1 [Major, 分歧]**: ASV 相对于 E-value 的新颖性定位。\n- R2 认为 C(δ) 参数化与 E-value \"高度同构\"，三个 ASV 类型本质是同一 δ 在不同阈值的值。\n- R1 反驳：扰动对象不同（annotation error vs. unmeasured confounding），sign-flip ASV 无 E-value 对应物，拓扑依赖性是独特创新。\n- **Director 判定**：R1 技术上正确——两者的 perturbation domain 确实不同，ASV 的 topology-dependent ranking 在 E-value 文献中没有对应。但 R2 关于\"更清晰定位\"的写作建议有价值。**建议在 Section 3.3 增加 1 段显式 ASV-vs-E-value 对比**。\n\n**W2 [Major, 共识]**: K≥3 理论不完整。Theorem 1 仅覆盖 K=2；Conjecture 1（K≥3 ε-approximate monotonicity）依赖 210,000 次数值验证。两位 Reviewer 均认为论文诚实处理了此局限，不应作为拒稿理由。Paper 已包含 proof obstacle 技术解释（K²−K dimensional manifold）。R2 建议补充 K=3 符号计算验证作为加强项。\n\n**W3 [Major, 分歧→降级]**: Proportional effects (f=λg) 假设适用性。\n- R1 评为 critical（无 NLP 动机，\"single latent factor\" 不够说服力）。\n- R2 反驳并成功降级：Table 15 显示非 proportional 下仍有 97.3% sign preservation，Proposition 4 提供 λ(C) ∈ [0,1] 的结构性保证。\n- **Director 判定**：降为 should-fix。假设不是 knife-edge——违反后仍有 97%+ robustness。但主文应引用 Table 15 robustness 结果（当前仅在 Appendix）。\n\n### Should-Fix (6 项)\n\n**W4 [Should-Fix, 共识]**: Abstract 信息密度过高。约 5 个具体数字造成认知过载。建议保留 1-2 个核心数字（MAPE + sign-flip rate），其余移至 Introduction。\n\n**W5 [Should-Fix, 共识]**: Non-differential misclassification 假设主文讨论不足。Definition 1 后应补 2-3 句直觉解释（何时 LLM 满足/违反此假设）。缺少实际 LLM 系统的典型 ε 量级。Appendix B.5 stress test 存在但未在主文充分引用。\n\n**W6 [Should-Fix, 共识]**: Section 3 对 NLP 读者可达性不足。plim 和 FWL 假设计量经济学背景。建议在 Section 3.1 开头增加 \"Notation roadmap\"（3-4 句话），用直觉语言解释核心概念。\n\n**W7 [Should-Fix, 共识]**: LLM 配置多样性有限。23 配置仅覆盖四个 7-13B 开源模型，缺 commercial API (GPT-4, Claude)、>70B 模型和 ordinal 任务。不影响核心贡献（理论论文），但限制泛化性声明。Limitations 应更具体讨论。\n\n**W8 [Should-Fix, 共识]**: ASV Bootstrap CI 过宽（exposure/IV 特异）。Exposure δ*=0.94 [0.60,1.36]、IV δ*=0.75 [0.44,1.29] 跨越 fragile/immune 分界线。但其余 5 种拓扑 CI 在同一类别内——属拓扑特异问题，非框架缺陷。建议报告 CI 在何 N 下收敛。\n\n**W9 [Should-Fix, 共识]**: 线性 SEM 结论的非线性推广整合不足。Appendix B.6/B.13 有 logistic DGP 验证（sign-flip pattern 一致，FWL breakdown negligible），但主文未充分整合。应在 Section 4 用 1-2 句提升 logistic 核心结论。\n\n### Nice-to-Have (1 项)\n\n**W10 [Minor, 共识]**: ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 简要提及。展示 FWL 不变性的实际意义，增强论文对 EMNLP 应用导向读者的说服力。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. FWL 不变性是论文最强、最干净的贡献。\n2. 三级证据层次是值得 AC 特别注意的方法论美德。\n3. K≥3 gap 是真实局限但诚实处理——不应作为拒稿理由。\n4. Abstract 需减少数字密度；Section 3 需提高 NLP 可达性。\n5. Non-differential 假设需更好的主文讨论。\n6. 真实 LLM 验证对理论论文足够但多样性有限。\n7. Overall 3.5 (Borderline Conference)，两位 Reviewer 均认为可在 3.5-4.0 区间。\n\n## Reviewer Divergence [REBUT]\n\n1. **ASV vs E-value 新颖性**：R2 认为高度同构，R1 反驳扰动对象不同且拓扑依赖性独特。Director 支持 R1 的技术判断，但认可 R2 的写作定位建议。\n2. **Proportional effects 严重性**：R1 评 critical，R2 引用 Table 15 robustness (97.3%) 成功反驳。Director 降为 should-fix。\n\n---\n\n## Questions for Authors\n\n**Q1**: K=3 monotonicity 能否通过符号计算（Hessian 半正定性）验证？这将 Conjecture 1 从纯数值升级为部分解析支撑。[R1 提出, R2 同意]\n\n**Q2**: 23 个真实 LLM 配置的 non-differential departure ε 量级是多少？Stress test 覆盖 ε∈[0,0.50] 但未与经验 ε 值对接。[R1 提出, R2 同意]\n\n**Q3**: PPI++ 在不同 gold label 比例下的性能降解如何？当前仅测试固定比例。[R1 提出, R2 同意]\n\n**Q4**: ASV 在 DAG 不确定性下的 robustness 如何？当前假设 DAG 已知。[R1 提出, R2 同意]\n\n**Q5**: Exposure 和 IV 的 Bootstrap CI 在何 N 下收敛？[两位 Reviewer 共同关注]\n\n**Q6**: Sharp phase transition 对 N < 1,000 样本的实践含义？ASV 是渐近量，有限样本行为未刻画。[R2 提出, R1 同意]\n\n---\n\n## Missing References\n\n1. **Prediction-Powered Causal Inferences** (2025, arXiv:2502.06343) — 与 PPI++ 讨论直接相关。[共识]\n2. **Variance-Aware LLM Annotation** (2025, arXiv:2601.02370) — 与 ASV sensitivity analysis 相关。[共识]\n3. **Hidden Measurement Error in LLM Pipelines** (2026, arXiv:2604.11581) — 直接讨论 LLM 测量误差。[共识]\n4. **Dawid & Skene (1979)** — 多标注者误差建模经典文献，概念祖先。[共识]\n5. **Rosenbaum (2002), Mathur et al. (2018)** — E-value foundations/power analysis，帮助界定 ASV 技术定位。[共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查仍在进行中（started at 2026-05-23T03:56:05Z）。本报告不等待，完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**评分理由**：\n\n论文针对一个重要且时机恰当的问题——LLM 多类别标注误差在因果推断中的传播——提供了系统性的理论分析。核心贡献清晰：\n\n- **FWL 不变性**是干净的负面结果，具有直接的实践价值（告诉实践者四种拓扑下矩阵校正无效）\n- **七种拓扑 × K≥3 的全面覆盖**填补了文献空白\n- **三级证据层次**展现了罕见的学术诚实\n\n阻碍 Conference (4.0) 评分的主要因素：\n\n1. **理论完整性**：K≥3 monotonicity 仍为 conjecture，ASV 框架在主要使用场景（K≥3）下缺乏解析保证\n2. **假设-现实差距**：Proportional effects 和 non-differential misclassification 在真实 LLM 标注中的适用性未用论文自身数据验证（虽然 robustness 证据表明非 knife-edge）\n3. **EMNLP 可达性**：论文偏计量经济学风格，对 NLP 主流读者门槛偏高\n4. **经验范围**：仅覆盖 7-13B 开源模型，泛化性声明受限\n\n论文可发表，增量贡献明确。通过针对性修改（提高可达性、主文整合 robustness 证据、显式 ASV-vs-E-value 对比），可达到 Conference (4.0) 水平。当前状态为强 Findings 候选。\n\n**Confidence: 4/5**（两位 Reviewer 深入审查了技术内容，关键评估有充分支撑）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 建议更早将 7 种拓扑分为 \"sign-preserving\"（5种）和 \"sign-reversing\"（2种），而非到 Section 4.2 才揭示。[R1-W1]\n- \"first unified analysis...building on prior single-topology analyses\" 措辞恰当，novelty claim 在合理范围内。[共识]\n\n### Section 3 (Method)\n- Section 3.1 开头增加 \"Notation roadmap\"（3-4 句话），用直觉语言解释 plim 和 FWL 核心概念。[W6]\n- Definition 1 后增加 2-3 句直觉解释：何时 LLM 标注满足/违反 non-differential 假设。[W5]\n- Section 3.3 增加 1 段 ASV-vs-E-value 显式对比（扰动对象、拓扑依赖性、sign-flip 独特性）。[W1]\n- 主文引用 Table 15 robustness（97.3% sign preservation under non-proportional）。[W3]\n\n### Section 4 (Experiments)\n- 用 1-2 句话提升 Appendix B.6/B.13 的 logistic DGP 核心结论到主文。[W9]\n- Section 4.5 简要提及 ClinicalBERT case study (Appendix B.3)。[W10]\n\n### Limitations\n- 更具体讨论 LLM 多样性缺口（commercial API、>70B、ordinal 任务）。[W7]\n- 增加有限样本下 ASV 行为的讨论。[Q6]\n\n### 事实纠正\n- R1 对 Appendix B.13 的描述有误（称\"一个数据集\"，实为 Monte Carlo 模拟）。已在交叉回应中由 R2 纠正。\n- R2 称\"正文未讨论 PPI++ negative transfer\"，但 Section 4.5 已明确提及。已在交叉回应中由 R1 纠正。",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 11 Consolidated Review Report\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Long Paper (8 页正文限制)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）\n\n---\n\n## Summary\n\n本文分析了 K≥3 多类别标注误差在七种典型 DAG 拓扑下如何传播到因果估计中。核心贡献包括：(1) 七种拓扑的 bias 闭式表达，证明/验证五种拓扑保持符号方向而 exposure 和 IV 可产生符号反转；(2) Annotation Sensitivity Values (ASV) 诊断工具揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱；(3) FWL 不变性负面结果证明基于矩阵的校正方法对四种拓扑无效。23 个真实 LLM 配置的 161 场景验证确认理论预测（MAPE 1.6%）。\n\n---\n\n## Strengths\n\n**S1 [共识]**: FWL 不变性是干净且重要的负面结果——对四种协变量拓扑，矩阵校正在线性 OLS 下精确实现 0% bias reduction。Appendix B.13 验证 logistic 下偏差可忽略（mean < 0.05%）。对实践者有直接指导意义：避免在这些拓扑上尝试矩阵校正。\n\n**S2 [共识]**: 三级证据层次（Proved / Numerically Verified / Conjectured）是突出的方法论优点。Proposition 1 → Observation 1 → Conjecture 1 清晰界定证明边界。在 EMNLP 投稿中极为少见的学术诚实。\n\n**S3 [共识]**: 首次系统覆盖 K≥3 × 7 种 DAG 拓扑。前作（Lee & Wood-Doughty 2024）仅覆盖 K=2、4 种 DAG。文献中确实是空白。\n\n**S4 [共识]**: 实证验证规模充分。161 场景 MAPE 1.6%，100,000 随机矩阵符号保持验证，23 个真实 LLM 配置跨 K=2/3/10。\n\n**S5 [共识]**: Algorithm 1 提供可操作的拓扑感知校正决策流程（DAG 识别 → 方法选择），在理论论文中不常见。\n\n**S6 [共识]**: Table 4 校正方法比较覆盖 210 种配置（5 方法 × 6 error structures × 7 拓扑），结论充分支撑。\n\n---\n\n## Weaknesses\n\n### Must-Fix (0 项)\n\n无。\n\n### Major (3 项)\n\n**W1 [Major, 分歧]**: ASV 相对于 E-value 的新颖性定位。\n- R2 认为 C(δ) 参数化与 E-value \"高度同构\"，三个 ASV 类型本质是同一 δ 在不同阈值的值。\n- R1 反驳：扰动对象不同（annotation error vs. unmeasured confounding），sign-flip ASV 无 E-value 对应物，拓扑依赖性是独特创新。\n- **Director 判定**：R1 技术上正确——两者的 perturbation domain 确实不同，ASV 的 topology-dependent ranking 在 E-value 文献中没有对应。但 R2 关于\"更清晰定位\"的写作建议有价值。**建议在 Section 3.3 增加 1 段显式 ASV-vs-E-value 对比**。\n\n**W2 [Major, 共识]**: K≥3 理论不完整。Theorem 1 仅覆盖 K=2；Conjecture 1（K≥3 ε-approximate monotonicity）依赖 210,000 次数值验证。两位 Reviewer 均认为论文诚实处理了此局限，不应作为拒稿理由。Paper 已包含 proof obstacle 技术解释（K²−K dimensional manifold）。R2 建议补充 K=3 符号计算验证作为加强项。\n\n**W3 [Major, 分歧→降级]**: Proportional effects (f=λg) 假设适用性。\n- R1 评为 critical（无 NLP 动机，\"single latent factor\" 不够说服力）。\n- R2 反驳并成功降级：Table 15 显示非 proportional 下仍有 97.3% sign preservation，Proposition 4 提供 λ(C) ∈ [0,1] 的结构性保证。\n- **Director 判定**：降为 should-fix。假设不是 knife-edge——违反后仍有 97%+ robustness。但主文应引用 Table 15 robustness 结果（当前仅在 Appendix）。\n\n### Should-Fix (6 项)\n\n**W4 [Should-Fix, 共识]**: Abstract 信息密度过高。约 5 个具体数字造成认知过载。建议保留 1-2 个核心数字（MAPE + sign-flip rate），其余移至 Introduction。\n\n**W5 [Should-Fix, 共识]**: Non-differential misclassification 假设主文讨论不足。Definition 1 后应补 2-3 句直觉解释（何时 LLM 满足/违反此假设）。缺少实际 LLM 系统的典型 ε 量级。Appendix B.5 stress test 存在但未在主文充分引用。\n\n**W6 [Should-Fix, 共识]**: Section 3 对 NLP 读者可达性不足。plim 和 FWL 假设计量经济学背景。建议在 Section 3.1 开头增加 \"Notation roadmap\"（3-4 句话），用直觉语言解释核心概念。\n\n**W7 [Should-Fix, 共识]**: LLM 配置多样性有限。23 配置仅覆盖四个 7-13B 开源模型，缺 commercial API (GPT-4, Claude)、>70B 模型和 ordinal 任务。不影响核心贡献（理论论文），但限制泛化性声明。Limitations 应更具体讨论。\n\n**W8 [Should-Fix, 共识]**: ASV Bootstrap CI 过宽（exposure/IV 特异）。Exposure δ*=0.94 [0.60,1.36]、IV δ*=0.75 [0.44,1.29] 跨越 fragile/immune 分界线。但其余 5 种拓扑 CI 在同一类别内——属拓扑特异问题，非框架缺陷。建议报告 CI 在何 N 下收敛。\n\n**W9 [Should-Fix, 共识]**: 线性 SEM 结论的非线性推广整合不足。Appendix B.6/B.13 有 logistic DGP 验证（sign-flip pattern 一致，FWL breakdown negligible），但主文未充分整合。应在 Section 4 用 1-2 句提升 logistic 核心结论。\n\n### Nice-to-Have (1 项)\n\n**W10 [Minor, 共识]**: ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 简要提及。展示 FWL 不变性的实际意义，增强论文对 EMNLP 应用导向读者的说服力。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. FWL 不变性是论文最强、最干净的贡献。\n2. 三级证据层次是值得 AC 特别注意的方法论美德。\n3. K≥3 gap 是真实局限但诚实处理——不应作为拒稿理由。\n4. Abstract 需减少数字密度；Section 3 需提高 NLP 可达性。\n5. Non-differential 假设需更好的主文讨论。\n6. 真实 LLM 验证对理论论文足够但多样性有限。\n7. Overall 3.5 (Borderline Conference)，两位 Reviewer 均认为可在 3.5-4.0 区间。\n\n## Reviewer Divergence [REBUT]\n\n1. **ASV vs E-value 新颖性**：R2 认为高度同构，R1 反驳扰动对象不同且拓扑依赖性独特。Director 支持 R1 的技术判断，但认可 R2 的写作定位建议。\n2. **Proportional effects 严重性**：R1 评 critical，R2 引用 Table 15 robustness (97.3%) 成功反驳。Director 降为 should-fix。\n\n---\n\n## Questions for Authors\n\n**Q1**: K=3 monotonicity 能否通过符号计算（Hessian 半正定性）验证？这将 Conjecture 1 从纯数值升级为部分解析支撑。[R1 提出, R2 同意]\n\n**Q2**: 23 个真实 LLM 配置的 non-differential departure ε 量级是多少？Stress test 覆盖 ε∈[0,0.50] 但未与经验 ε 值对接。[R1 提出, R2 同意]\n\n**Q3**: PPI++ 在不同 gold label 比例下的性能降解如何？当前仅测试固定比例。[R1 提出, R2 同意]\n\n**Q4**: ASV 在 DAG 不确定性下的 robustness 如何？当前假设 DAG 已知。[R1 提出, R2 同意]\n\n**Q5**: Exposure 和 IV 的 Bootstrap CI 在何 N 下收敛？[两位 Reviewer 共同关注]\n\n**Q6**: Sharp phase transition 对 N < 1,000 样本的实践含义？ASV 是渐近量，有限样本行为未刻画。[R2 提出, R1 同意]\n\n---\n\n## Missing References\n\n1. **Prediction-Powered Causal Inferences** (2025, arXiv:2502.06343) — 与 PPI++ 讨论直接相关。[共识]\n2. **Variance-Aware LLM Annotation** (2025, arXiv:2601.02370) — 与 ASV sensitivity analysis 相关。[共识]\n3. **Hidden Measurement Error in LLM Pipelines** (2026, arXiv:2604.11581) — 直接讨论 LLM 测量误差。[共识]\n4. **Dawid & Skene (1979)** — 多标注者误差建模经典文献，概念祖先。[共识]\n5. **Rosenbaum (2002), Mathur et al. (2018)** — E-value foundations/power analysis，帮助界定 ASV 技术定位。[共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查仍在进行中（started at 2026-05-23T03:56:05Z）。本报告不等待，完成后会自动补发到 Group C。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**评分理由**：\n\n论文针对一个重要且时机恰当的问题——LLM 多类别标注误差在因果推断中的传播——提供了系统性的理论分析。核心贡献清晰：\n\n- **FWL 不变性**是干净的负面结果，具有直接的实践价值（告诉实践者四种拓扑下矩阵校正无效）\n- **七种拓扑 × K≥3 的全面覆盖**填补了文献空白\n- **三级证据层次**展现了罕见的学术诚实\n\n阻碍 Conference (4.0) 评分的主要因素：\n\n1. **理论完整性**：K≥3 monotonicity 仍为 conjecture，ASV 框架在主要使用场景（K≥3）下缺乏解析保证\n2. **假设-现实差距**：Proportional effects 和 non-differential misclassification 在真实 LLM 标注中的适用性未用论文自身数据验证（虽然 robustness 证据表明非 knife-edge）\n3. **EMNLP 可达性**：论文偏计量经济学风格，对 NLP 主流读者门槛偏高\n4. **经验范围**：仅覆盖 7-13B 开源模型，泛化性声明受限\n\n论文可发表，增量贡献明确。通过针对性修改（提高可达性、主文整合 robustness 证据、显式 ASV-vs-E-value 对比），可达到 Conference (4.0) 水平。当前状态为强 Findings 候选。\n\n**Confidence: 4/5**（两位 Reviewer 深入审查了技术内容，关键评估有充分支撑）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 建议更早将 7 种拓扑分为 \"sign-preserving\"（5种）和 \"sign-reversing\"（2种），而非到 Section 4.2 才揭示。[R1-W1]\n- \"first unified analysis...building on prior single-topology analyses\" 措辞恰当，novelty claim 在合理范围内。[共识]\n\n### Section 3 (Method)\n- Section 3.1 开头增加 \"Notation roadmap\"（3-4 句话），用直觉语言解释 plim 和 FWL 核心概念。[W6]\n- Definition 1 后增加 2-3 句直觉解释：何时 LLM 标注满足/违反 non-differential 假设。[W5]\n- Section 3.3 增加 1 段 ASV-vs-E-value 显式对比（扰动对象、拓扑依赖性、sign-flip 独特性）。[W1]\n- 主文引用 Table 15 robustness（97.3% sign preservation under non-proportional）。[W3]\n\n### Section 4 (Experiments)\n- 用 1-2 句话提升 Appendix B.6/B.13 的 logistic DGP 核心结论到主文。[W9]\n- Section 4.5 简要提及 ClinicalBERT case study (Appendix B.3)。[W10]\n\n### Limitations\n- 更具体讨论 LLM 多样性缺口（commercial API、>70B、ordinal 任务）。[W7]\n- 增加有限样本下 ASV 行为的讨论。[Q6]\n\n### 事实纠正\n- R1 对 Appendix B.13 的描述有误（称\"一个数据集\"，实为 Monte Carlo 模拟）。已在交叉回应中由 R2 纠正。\n- R2 称\"正文未讨论 PPI++ negative transfer\"，但 Section 4.5 已明确提及。已在交叉回应中由 R1 纠正。",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-23T04:06:09.745459+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4115
}
```

</details>

---


### Assistant

_source line 898 · 2026-05-23T04:06:22.746450+00:00_

审稿报告已投递。

**Round 11 审稿完成总结**：

- **Overall: 3.5 (Borderline Conference)**
- **Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性），1 轮收敛
- **核心判断**: FWL 不变性是最强贡献，三级证据层次值得 AC 注意。K≥3 理论不完整和 EMNLP 可达性是主要扣分项
- **3 个 Major weakness**: ASV 新颖性定位（分歧→写作建议）、K≥3 理论 gap（共识→诚实处理）、Proportional effects（分歧→降级为 should-fix）
- **6 个 Should-Fix**: Abstract 密度、non-differential 讨论、NLP 可达性、LLM 多样性、Bootstrap CI 宽度、线性 SEM 整合
- **6 个 Questions for Authors**, **5 篇 Missing References**
- **视觉审查**: 仍在运行，完成后自动补发到 Group C
- **Issue Tracker**: 已同步更新至 Round 11（3 个新 issue，12 个 in_progress 更新 mention）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 88

## Round 88

6 recorded events


### User

_source line 899 · 2026-05-23T04:06:23.915578+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 完整审稿意见

**审查侧重**: 方法严谨性 + 实验有效性

---

### Summary

本文研究 LLM 标注产生的 K×K 混淆矩阵如何在七种 canonical DAG 拓扑下传播为下游因果估计偏差。三个贡献：(1) 推导 K≥3 非差异性误分类下七种拓扑的 bias 闭式表达式；(2) 提出三类 Annotation Sensitivity Value (ASV) 诊断指标；(3) 通过 FWL 定理证明矩阵校正对四种协变量拓扑无效，并系统比较五种校正方法。理论推导总体严谨，Monte Carlo 验证充分（MAPE 1.6%），三级证据层次（proved / verified / conjectured）的方法论诚实度值得肯定。

---

### Strengths

**S1. 七种拓扑的 bias 推导体系完整且正确。** Section 3.2 对每种拓扑给出了完整的 data-generating process 和 probability limit 推导。Confounding 的 FWL 分解（Appendix A.3）、Exposure 的加权组合结构（Section 3.2, Eq. 2）、Mediation 的 leakage coefficient（Eq. 3）、IV 的 Wald estimator 分母不稳定性——每种拓扑的 bias 机制都有清晰的因果直觉支撑。推导遵循标准测量误差理论（Hernán and Cole 2009, Buonaccorsi 2010），扩展到 K×K 混淆矩阵是自然且正确的。

**S2. 三级证据层次是方法论上的典范。** Theorem 1 对 K=2 给出解析证明（Appendix A.4，通过 perspective function convexity 建立 envelope monotonicity）；Observation 1 对 K≥3 提供 100,000 矩阵的数值验证；Conjecture 1 对 ε-approximate bounds 提供 210,000 矩阵的支持。每一级都明确标注证据强度，不过度声称。这在 NLP 领域的理论工作中并不常见，值得表扬。

**S3. FWL 不变性是高价值负面结果。** Section 4.5 + Appendix B.2 + B.13 证明：对 confounding/mediation/collider/M-bias 四种协变量拓扑，任何基于混淆矩阵的校正方法（naive plug-in, MLA, DSL, SIMEX）在线性 OLS 下精确实现 0% bias reduction，logistic 回归下偏差可忽略（< 0.01%，Table 5）。这个结果直接阻止实践者在这四种拓扑上浪费计算资源做矩阵校正。

**S4. Monte Carlo 验证充分且全面。** 161 scenarios（7 topologies × 23 LLM configurations），grand MAPE 1.6%。Per-topology MAPE 从 0.5%（confounding）到 5.7%（IV），精确量化了理论预测与仿真的偏差。N=10,000 的样本量足以确保渐近理论的适用性。

**S5. Proposition 1 的 sign preservation 条件结构清晰。** 四种拓扑分别给出充分条件：confounding 用 Cauchy-Schwarz，collider 用 Berkson attenuation，mediation 用 leakage boundedness，front-door 用结构性论证。Table 2（Appendix A.9）提供了清晰的汇总。条件是充分而非必要的，论文明确说明了这一点。

**S6. 校正方法比较公平且发现有实践价值。** Table 4 跨 5 种方法 × 7 种拓扑 × 6 种 error structures（210 configurations）系统比较。PPI++ 最优但需 gold labels 且对 M-bias 有害（-88%）；MC-SIMEX 是最佳 gold-free 方法；矩阵校正对 FWL-invariant 拓扑确实无效。Algorithm 1 将这些发现转化为可操作的决策流程。

---

### Weaknesses

**W1. [Should-Fix] Theorem 1 的 proportional effects 假设（f = λg）实际适用范围未被充分论证。**

- **具体位置**：Section 3.3 Theorem 1, Appendix A.4, B.14, B.15
- **问题**：Theorem 1 证明 envelope monotonicity 依赖 proportional effects 假设（f = λg for some scalar λ），即 treatment effect coefficient 与 confounding effect 成比例。Appendix B.15 验证了 proportional 和 non-proportional 情形下的 sign preservation 率（97.3% vs 100%），但始终未回答一个关键问题：**在真实 NLP 因果推断场景中，f = λg 的假设多常被满足？** 论文没有从 23 个 LLM 配置的真实数据中估计 f/g 的比值分布，也没有引用实证文献说明比例效应在社会科学因果研究中的流行度。
- **为什么影响评分**：如果 proportional effects 在实践中罕见，Theorem 1 的保证就仅限于理论完整性而非实践指导。Appendix B.15 的 "independent f, g" 测试表明 non-proportional 下仍有 97.3% sign preservation，这暗示 Theorem 1 的条件可能过于保守——但这个重要观察被淹没在附录中。
- **建议修改方向**：(1) 在 Section 3.3 中增加一段讨论 proportional effects 的实践合理性；(2) 将 B.15 的 key finding（non-proportional 下 97.3% 仍成立）提升到正文。

**W2. [Should-Fix] 非差异性误分类假设的违反行为仅在单一扰动模型下测试。**

- **具体位置**：Definition 1 (Section 3.1), Appendix B.5, Limitations
- **问题**：Appendix B.5 的 stress test 使用了特定的违反模型：C_perturbed = C_base + ε·Δ，其中 Δ 是 Uniform[-1,1] 的随机扰动矩阵（与 Y 相关）。这只是非差异性假设违反的一种形式。在 LLM 标注实践中，更现实的违反模式包括：(a) outcome-conditional prompting（prompt 中包含 Y 的线索）；(b) 文本难度与 outcome 的系统性关联（如负面情感文本更难分类，同时与 Y 负相关）；(c) label-specific 的 LLM bias（LLM 系统性地将某些类别误判为其他特定类别，且这种 pattern 与 Y 相关）。当前 stress test 的随机扰动模型未捕捉这些结构化违反模式。
- **为什么影响评分**：非差异性是论文最核心的假设（所有 bias 表达式都依赖它）。如果该假设以结构化方式被违反（而非随机扰动），bias 表达式可能失效的程度比 B.5 报告的更大。
- **建议修改方向**：补充至少一种结构化违反模型（如 outcome-dependent misclassification rate），测试 bias 表达式的 degradation pattern。或在 Limitations 中更明确地讨论哪些 LLM 使用模式可能违反假设。

**W3. [Should-Fix] 校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性。**

- **具体位置**：Section 4.5, Table 4
- **问题**：论文在 Section 3.2 中深入分析了 K=2 到 K≥3 的 binarization collapse 和 sign reversal 行为变化（Numerical Verification 2），强调 K 值对 bias 的结构性影响。然而校正方法比较（Table 4）仅使用 K=3。考虑到：(a) K=2 有更强的理论保证（Theorem 1 vs Conjecture 1）；(b) K≥5 的混淆矩阵结构更复杂（off-diagonal 自由度增加）；(c) 实际 NLP 任务 K 值变化大（stance 4类, sentiment 5类, disaster 10+类），缺少 K 值敏感性分析是一个方法论缺陷。
- **为什么影响评分**：论文的核心 message 之一是"K≥3 的行为与 K=2 质变"（binarization collapse），但校正方法是否对这种质变 robust 未被验证。
- **建议修改方向**：补充 K ∈ {2, 5, 10} 的校正比较（至少对 2-3 种关键拓扑），验证 PPI++ 和 MC-SIMEX 的优势是否在不同 K 值下保持。

**W4. [Minor→Should-Fix] IV 拓扑的 Wald estimator 不稳定性（52.6% denominator sign change）未充分讨论因果含义。**

- **具体位置**：Section 4.1, Table 1, Table 6 (Appendix B.4)
- **问题**：Section 4.1 报告 "52.6% of random matrices cause the Wald estimator's denominator to change sign"。这意味着超过一半的随机混淆矩阵使 IV 估计完全不可靠。Table 6 进一步展示了分子/分母的 violation/amplification 行为。然而，正文仅用几句话提及此发现，未讨论其对 NLP 中使用 IV 策略的实践含义——例如，在 sentiment-as-instrument 的常见设计中，需要什么水平的标注精度才能避免 Wald estimator 崩溃？
- **建议**：在 Section 4.1 或 Section 5 中增加 2-3 句话，将 52.6% 的发现转化为对 NLP 实践者的具体 guidance（如"使用 IV 策略时，需确保 confusion matrix 的 diagonal dominance ≥ X"）。

**W5. [Minor] 23 个 LLM 配置全部为开源 7-8B 模型，缺少规模和类型多样性。**

- **具体位置**：Section 4.4
- **问题**：四个模型（Llama-3-8B/Maverick, Qwen-2.5-7B, DeepSeek-Chat, Qwen2.5-7B-Instruct）均为开源 7-8B 参数量级。缺少：(a) commercial API 模型（GPT-4, Claude），其混淆矩阵结构可能不同（near-perfect accuracy → 接近对角矩阵）；(b) 大规模模型（70B+），错误模式可能更稀疏。论文在 Limitations 中提及 "diagonal accuracy range (0.61-0.88) covers realistic LLM performance but does not include near-perfect (>0.95) or near-random (<0.5) annotators"，这是诚实的。
- **为什么影响评分但不致命**：论文核心贡献是理论框架，empirical validation 的目的是验证理论预测。23 个配置已足以确认 theory-MC agreement。但缺少高精度模型使得 "near-perfect accuracy" regime 的行为（ASV 值、sign preservation）未被实证覆盖。

---

### Questions for Authors

**Q1.** Theorem 1 证明中（Appendix A.4），V₀(δ) 的 convexity 论证依赖 perspective function 的性质。请确认：当 f 和 g 不满足 proportional effects 但满足 "near-proportional"（f ≈ λg + small perturbation）时，monotonicity 是否以 Lipschitz 方式退化？Appendix B.12 的 numerical evidence 暗示了这一点（worst-case deviation 0.01），但缺乏形式化陈述。

**Q2.** Table 4 中 PPI++ 对 M-bias 产生 -88% RMSE（harmful）。正文提及了这一结果但未解释机制。PPI++ 的 gold-label 校正在 M-bias DAG 结构下为什么反而放大偏差？是否与 M-bias 的 collider conditioning 结构导致 gold labels 引入额外 selection bias 有关？

**Q3.** ASV 的 bootstrap 不确定性（Appendix B.7, Table 3）仅在 N=1,500 下测试。对于 NLP 因果推断中常见的大规模数据集（N > 100,000），ASV 的 sharp phase transition 是否变得更 sharp（方差更小），从而使 δ threshold 更可靠？或者 N 的增大主要影响 significance ASV (δ_sig) 而非 magnitude ASV (δ_mag)？

**Q4.** Appendix B.6 在 logistic DGP 下测试了 sign-flip rates，发现 "virtually identical" to linear。但 logistic 模型的 treatment effect 是 log-odds ratio，与线性模型的 additive effect 量纲不同。bias 表达式（基于 linear SEM）在 logistic 下的 "approximate correctness" 应如何解释？是 bias 方向正确但量级不适用，还是两者都近似正确？

**Q5.** Conjecture 1 的 ε-approximate bound（Appendix B.11）对不同拓扑给出了不同的 ε 值（confounding 0.006, front-door 0.013, IV 0.112）。IV 的 ε=0.112 意味着 envelope 可以非单调到 11.2% 的相对偏差。这个量级在实际因果推断中是否可忽略？论文是否应讨论一个"可接受的 ε 阈值"？

---

### Missing References

1. **Rosenbaum (2002)** *Observational Studies*, 2nd edition — sensitivity analysis 的经典框架，与 ASV 的 sensitivity analysis 直接相关。论文引用了 VanderWeele and Ding (2017) 的 E-value，但缺少更早的 sensitivity analysis 根基文献。

2. **Mathur et al. (2018)** "Sensitivity Analysis in Observational Research: Introducing the E-Value" — E-value 的 power analysis 和统计推断，与 ASV 的 bootstrap confidence interval (B.7) 方法论有关联。（注：论文已引用 VanderWeele and Ding 2017，但 Mathur et al. 提供了 E-value 的统计推断框架，与 ASV 的 CI 方法直接可比。）

---

### Minor Issues

- **M1.** Section 3.2 Exposure 拓扑的 Eq. (2) 中 wⱼₖ 的定义依赖 marginal distribution of A，但正文未明确说明 marginal distribution 是来自真实 A 还是误分类 A*。需要 clarify。（Appendix A 有详细定义，但正文应自包含。）

- **M2.** Figure 2 (p.7) 的 y 轴标签 "Bias distributions" 不够 informative——建议改为 "Relative bias (plim τ̂(A*)/τ − 1)" 或类似的精确描述。

- **M3.** Section 4.4 第二段 "Empirical bias ranking: HateAID (K=10) ranks predictably..." 的 "predictably" 是主观用语，建议改为 "consistently with theoretical predictions"。

- **M4.** Limitations 节提到 "outcome misclassification of A by a single annotator"——这里 "outcome misclassification" 措辞有歧义，可能被误解为 Y 的误分类而非 A 的误分类。建议改为 "misclassification of A"。

---

### 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | Sections 1-5 结束于 p.8，Limitations 在 p.8 底部（不计入页数限制） |
| Double-blind | ✓ | 标题页显示 "Anonymous ACL submission" |
| ACL 引用格式 | ✓ | 使用 natbib + ACL style，括号引用格式正确 |
| Limitations 节 | ✓ | 正文末尾有 Limitations，覆盖 3 个关键限制 |
| 附录使用 | ✓ | 18 页附录内容丰富但组织合理，证明完整 |

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4/5 (Strong) | 七种拓扑的 bias 推导正确；Proposition 1 条件充分且经 100,000 矩阵验证；Theorem 1 (K=2) 证明完整；三级证据层次方法论严谨。主要扣分：K≥3 仅有 conjecture，proportional effects 假设实际适用性未论证。 |
| **Excitement** | 3.5/5 | 七种拓扑 × K≥3 的系统化分析填补文献空白，FWL 不变性有直接实践价值。但 ASV 框架与 E-value 的技术区分可以更鲜明，excitement 主要来自系统性和负面结果而非方法论突破。 |
| **Reproducibility** | 4/5 | Monte Carlo 设置详细（N, K, 拓扑, seed 均明确），bias 表达式可独立推导验证。论文承诺代码和数据公开释放。扣分：部分 DGP 参数（如 α, β 具体取值）分散在附录各处，需仔细收集。 |
| **Confidence** | 4/5 | 我仔细检查了关键推导（confounding/exposure/IV 的 bias 表达式, Proposition 1 的 Cauchy-Schwarz 论证, Theorem 1 的 convexity argument），并验证了 Monte Carlo 设置的合理性。附录 B.11-B.15 的数值验证我进行了逻辑审查但未独立复现。 |

---

### Overall Assessment

**Overall: 4.0 — Conference（可被主会议接收）**

**一句话总结**：一篇方法论扎实、证据层次清晰的理论工作，首次系统化处理 K≥3 多类标注误差在七种 DAG 拓扑下的因果偏差传播，FWL 不变性的负面结果对实践者有直接价值。

**给出 4.0 的理由**：

*支持接收的因素*：
1. **理论覆盖度**：七种拓扑 × K≥3 的完整 bias 分析在文献中确为首次（Lee and Wood-Doughty 2024 仅覆盖 K=2、四种 DAG）。
2. **方法论诚实度**：三级证据层次（proved/verified/conjectured）的做法在 NLP 理论工作中罕见且值得推广。
3. **负面结果的价值**：FWL 不变性直接告知实践者哪些校正策略注定无效，这比又一个 "method X improves by Y%" 的正面结果更有长期影响。
4. **实验验证充分**：MAPE 1.6%、23 个 LLM 配置、210 configurations 的校正比较——对理论论文而言已超过通常的验证标准。

*限制接收的因素*：
1. K≥3 的 monotonicity 停留在 conjecture 层面，理论贡献的完整性受限。
2. 非差异性假设的 stress test 仅覆盖随机扰动，未测试结构化违反。
3. 校正方法比较缺少 K 值敏感性分析。
4. 实证验证局限于开源 7-8B 模型。

综合来看，支持因素明显超过限制因素。限制因素中的 1-3 可在 camera-ready 阶段解决（补充实验即可），第 4 点是合理的 scope 选择。论文对 EMNLP 社区的贡献在于：为日益增多的 "用 LLM 标注做因果推断" 的 NLP 研究提供了急需的理论基础和实践指南。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 4.0 (Conference)**。论文在方法严谨性上表现扎实——七种拓扑的 bias 推导正确、三级证据层次诚实、FWL 不变性既有理论证明又有实证验证。主要扣分点是 K≥3 monotonicity 停留在 conjecture、非差异性假设的 stress test 覆盖不够结构化、校正比较缺少 K 值敏感性。这些都是可在 camera-ready 阶段解决的问题，不影响核心贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---
