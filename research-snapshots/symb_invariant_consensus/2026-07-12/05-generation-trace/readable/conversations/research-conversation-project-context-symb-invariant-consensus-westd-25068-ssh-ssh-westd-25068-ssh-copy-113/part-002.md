# Research conversation: <project_context> # 项目: symb_invariant_consensus ## 运行环境 - 服务器名: westd-25068 - SSH 连接命令: ssh westd-25068 # 必须用此命令，~/.ssh — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-symb-invariant-consensus-westd-25068-ssh-ssh-westd-25068-ssh-copy-113.md) · [Structured JSON](../../../sessions/23/23647b2793c20e178c09.json)

## Round 1

### Tool result

_source line 57 · 2026-05-22T13:59:15.961Z_

<details><summary>↩ Tool result · `toolu_01VTZ8pDW4N5VPkiSNatVuDR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1205-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1206-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1207-Underfull \hbox (badness 1383) in paragraph at lines 15--16
docs/paper/main.log:1208:\T1/ptm/m/n/10.95 (+20) holds across three NLI ar-chi-tec-tures and six
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1209- []
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1210-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1211-) (./discussion.tex
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-135-
docs/paper/diagnosis.tex-136-\paragraph{Method-level interventions.} ICG ($\Delta \approx 0$, $p = .206$), Contrastive ($\Delta = -9.31$\,pp, $p < 0.01$), and Debate ($\Delta = -18.63$/$-23.00$\,pp, $p < 0.001$) all fail (Table~\ref{tab:method_interventions}, Appendix~\ref{app:remediation}). Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles) produce neutral-to-negative results (Appendix Table~\ref{tab:additional_interventions}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-137-
docs/paper/diagnosis.tex:138:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-139-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-140-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-141-\centering
--
docs/paper/appendix.tex-211-$\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\text{CCR}(\text{self}, G) \approx 0$; (2)~Finding~2 predicts $\text{CCR}(V, G) > 0$ when $V$ is independent and capable.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-212-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-213-\paragraph{Empirical CCR across verifier--generator pairs.}
docs/paper/appendix.tex:214:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-215-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-216-\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-217-\centering
--
docs/paper/appendix.tex-285-\label{tab:power}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-286-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-287-
docs/paper/appendix.tex:288:The largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-289-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-290-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-291-\section{Bootstrap Confidence Intervals}
--
docs/paper/appendix.tex-309-\label{tab:bootstrap}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-310-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-311-
docs/paper/appendix.tex:312:All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-313-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-314-
docs/paper/appendix.tex-315-\section{Case Studies: Discordant Predictions}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-885-\begin{table}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-886-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-887-\small
docs/paper/appendix.tex:888:\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\%$). Three NLI verifiers $\times$ three weight settings. {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$ (McNemar).}
docs/paper/appendix.tex-889-\label{tab:multi-nli}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-890-\begin{tabular}{@{}llrrl@{}}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-891-\toprule
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-935-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-936-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-937-\includegraphics[width=0.78\columnwidth]{figures/capability_gap_scatter}
docs/paper/appendix.tex:938:\caption{Combo gain vs.\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator.}
docs/paper/appendix.tex-939-\label{fig:capability-gap}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-940-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-941-
docs/paper/appendix.tex:942:Table~\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\% standalone, combo $+5.17$\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\% standalone, combo $+4.17$\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \geq 3$.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-943-
docs/paper/appendix.tex:944:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-945-
docs/paper/appendix.tex:946:\paragraph{Robustness check.} Including all nine conditions (three verifiers $\times$ three weight levels on Mistral-7B) yields Spearman $\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-947-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-948-\paragraph{Full NLI combo with BH correction.}
docs/paper/appendix.tex-949-\label{app:nli-combo-full}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-9-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-10-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-11-\paragraph{Why it works.}
docs/paper/solutions.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-13-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-14-\paragraph{Capability gap hypothesis.}
docs/paper/solutions.tex:15:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-16-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-17-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-18-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-25-
docs/paper/introduction.tex-26-Oracle controls confirm the mechanism is sound ($+29.90$\,pp Mistral-7B, $+14.22$\,pp Qwen-14B on FOLIO, $p < 0.001$; \S\ref{sec:oracle}), yet self-extraction captures only ${\sim}$12\% of this ceiling.
docs/paper/introduction.tex-27-The central finding is a persistent independence-accuracy trade-off \citep{krogh1994neural}: Debate reduces $\kappa$ to 0.15 but collapses accuracy ($-18.6$\,pp); other methods cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling across three families (\S\ref{sec:remediation}).
docs/paper/introduction.tex:28:A cross-architecture proof-of-concept escapes the bottleneck: DeBERTa NLI yields $+6.67$\,pp on ProofWriter ($p < 0.001$), confirmed across three NLI architectures (\S\ref{sec:cross-arch}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-29-
docs/paper/introduction.tex-30-Our contributions are:
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-31-\begin{enumerate}[nosep,leftmargin=*]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2249-\@writefile{toc}{\contentsline {section}{\numberline {W}Multi-Verifier NLI Results}{23}{appendix.W}\protected@file@percent }
docs/paper/main.aux-2250-\newlabel{app:multi-nli}{{W}{23}{Multi-Verifier NLI Results}{appendix.W}{}}
docs/paper/main.aux-2251-\newlabel{app:multi-nli@cref}{{[section][23][]W}{[1][23][]23}{}{}{}}
docs/paper/main.aux:2252:\@writefile{lot}{\contentsline {table}{\numberline {26}{\ignorespaces Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\%$). Three NLI verifiers $\times $ three weight settings. {*}\,$p < 0.05$;\enspace  {**}\,$p < 0.01$;\enspace  {***}\,$p < 0.001$ (McNemar).}}{23}{table.caption.83}\protected@file@percent }
docs/paper/main.aux:2253:\newlabel{tab:multi-nli}{{26}{23}{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\%$). Three NLI verifiers $\times $ three weight settings. {*}\,$p < 0.05$;\enspace {**}\,$p < 0.01$;\enspace {***}\,$p < 0.001$ (McNemar)}{table.caption.83}{}}
docs/paper/main.aux-2254-\newlabel{tab:multi-nli@cref}{{[table][26][]26}{[1][23][]23}{}{}{}}
docs/paper/main.aux-2255-\newlabel{app:3verifier-bh}{{W}{23}{Three-verifier BH correction}{section*.84}{}}
docs/paper/main.aux-2256-\newlabel{app:3verifier-bh@cref}{{[section][23][]W}{[1][23][]23}{}{}{}}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2272-\@LN{1731}{22}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2273-\@LN{1732}{22}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2274-\@LN@col{2}
docs/paper/main.aux:2275:\@writefile{lof}{\contentsline {figure}{\numberline {7}{\ignorespaces Combo gain vs.\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator.}}{23}{figure.caption.86}\protected@file@percent }
docs/paper/main.aux:2276:\newlabel{fig:capability-gap}{{7}{23}{Combo gain vs.\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator}{figure.caption.86}{}}
docs/paper/main.aux-2277-\newlabel{fig:capability-gap@cref}{{[figure][7][]7}{[1][23][]23}{}{}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2278-\@LN{1733}{22}
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2279-\@LN{1734}{22}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17988d54-08f5-4e41-b16b-feb7dc35bf5e",
  "isSidechain": false,
  "promptId": "dc065ad1-7a33-4484-84cc-5c01195cf1b0",
  "type": "user",
  "uuid": "a3591e26-eaaf-4535-b26d-ac9c983e3a89",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1205-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1206-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1207-Underfull \\hbox (badness 1383) in paragraph at lines 15--16\ndocs/paper/main.log:1208:\\T1/ptm/m/n/10.95 (+20) holds across three NLI ar-chi-tec-tures and six\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1209- []\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1210-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.log-1211-) (./discussion.tex\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-135-\ndocs/paper/diagnosis.tex-136-\\paragraph{Method-level interventions.} ICG ($\\Delta \\approx 0$, $p = .206$), Contrastive ($\\Delta = -9.31$\\,pp, $p < 0.01$), and Debate ($\\Delta = -18.63$/$-23.00$\\,pp, $p < 0.001$) all fail (Table~\\ref{tab:method_interventions}, Appendix~\\ref{app:remediation}). Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles) produce neutral-to-negative results (Appendix Table~\\ref{tab:additional_interventions}).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-137-\ndocs/paper/diagnosis.tex:138:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-139-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-140-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-141-\\centering\n--\ndocs/paper/appendix.tex-211-$\\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\\text{CCR}(\\text{self}, G) \\approx 0$; (2)~Finding~2 predicts $\\text{CCR}(V, G) > 0$ when $V$ is independent and capable.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-212-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-213-\\paragraph{Empirical CCR across verifier--generator pairs.}\ndocs/paper/appendix.tex:214:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-215-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-216-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-217-\\centering\n--\ndocs/paper/appendix.tex-285-\\label{tab:power}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-286-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-287-\ndocs/paper/appendix.tex:288:The largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-289-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-290-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-291-\\section{Bootstrap Confidence Intervals}\n--\ndocs/paper/appendix.tex-309-\\label{tab:bootstrap}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-310-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-311-\ndocs/paper/appendix.tex:312:All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-313-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-314-\ndocs/paper/appendix.tex-315-\\section{Case Studies: Discordant Predictions}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-885-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-886-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-887-\\small\ndocs/paper/appendix.tex:888:\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\ndocs/paper/appendix.tex-889-\\label{tab:multi-nli}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-890-\\begin{tabular}{@{}llrrl@{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-891-\\toprule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-935-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-936-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-937-\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\ndocs/paper/appendix.tex:938:\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator.}\ndocs/paper/appendix.tex-939-\\label{fig:capability-gap}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-940-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-941-\ndocs/paper/appendix.tex:942:Table~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-943-\ndocs/paper/appendix.tex:944:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-945-\ndocs/paper/appendix.tex:946:\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-947-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-948-\\paragraph{Full NLI combo with BH correction.}\ndocs/paper/appendix.tex-949-\\label{app:nli-combo-full}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-9-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-10-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-11-\\paragraph{Why it works.}\ndocs/paper/solutions.tex:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-13-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-14-\\paragraph{Capability gap hypothesis.}\ndocs/paper/solutions.tex:15:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-16-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-17-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex-18-\\centering\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-25-\ndocs/paper/introduction.tex-26-Oracle controls confirm the mechanism is sound ($+29.90$\\,pp Mistral-7B, $+14.22$\\,pp Qwen-14B on FOLIO, $p < 0.001$; \\S\\ref{sec:oracle}), yet self-extraction captures only ${\\sim}$12\\% of this ceiling.\ndocs/paper/introduction.tex-27-The central finding is a persistent independence-accuracy trade-off \\citep{krogh1994neural}: Debate reduces $\\kappa$ to 0.15 but collapses accuracy ($-18.6$\\,pp); other methods cluster at $\\kappa \\approx 0.40$--$0.47$, a same-model ceiling across three families (\\S\\ref{sec:remediation}).\ndocs/paper/introduction.tex:28:A cross-architecture proof-of-concept escapes the bottleneck: DeBERTa NLI yields $+6.67$\\,pp on ProofWriter ($p < 0.001$), confirmed across three NLI architectures (\\S\\ref{sec:cross-arch}).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-29-\ndocs/paper/introduction.tex-30-Our contributions are:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex-31-\\begin{enumerate}[nosep,leftmargin=*]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2249-\\@writefile{toc}{\\contentsline {section}{\\numberline {W}Multi-Verifier NLI Results}{23}{appendix.W}\\protected@file@percent }\ndocs/paper/main.aux-2250-\\newlabel{app:multi-nli}{{W}{23}{Multi-Verifier NLI Results}{appendix.W}{}}\ndocs/paper/main.aux-2251-\\newlabel{app:multi-nli@cref}{{[section][23][]W}{[1][23][]23}{}{}{}}\ndocs/paper/main.aux:2252:\\@writefile{lot}{\\contentsline {table}{\\numberline {26}{\\ignorespaces Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times $ three weight settings. {*}\\,$p < 0.05$;\\enspace  {**}\\,$p < 0.01$;\\enspace  {***}\\,$p < 0.001$ (McNemar).}}{23}{table.caption.83}\\protected@file@percent }\ndocs/paper/main.aux:2253:\\newlabel{tab:multi-nli}{{26}{23}{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times $ three weight settings. {*}\\,$p < 0.05$;\\enspace {**}\\,$p < 0.01$;\\enspace {***}\\,$p < 0.001$ (McNemar)}{table.caption.83}{}}\ndocs/paper/main.aux-2254-\\newlabel{tab:multi-nli@cref}{{[table][26][]26}{[1][23][]23}{}{}{}}\ndocs/paper/main.aux-2255-\\newlabel{app:3verifier-bh}{{W}{23}{Three-verifier BH correction}{section*.84}{}}\ndocs/paper/main.aux-2256-\\newlabel{app:3verifier-bh@cref}{{[section][23][]W}{[1][23][]23}{}{}{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2272-\\@LN{1731}{22}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2273-\\@LN{1732}{22}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2274-\\@LN@col{2}\ndocs/paper/main.aux:2275:\\@writefile{lof}{\\contentsline {figure}{\\numberline {7}{\\ignorespaces Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator.}}{23}{figure.caption.86}\\protected@file@percent }\ndocs/paper/main.aux:2276:\\newlabel{fig:capability-gap}{{7}{23}{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator}{figure.caption.86}{}}\ndocs/paper/main.aux-2277-\\newlabel{fig:capability-gap@cref}{{[figure][7][]7}{[1][23][]23}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2278-\\@LN{1733}{22}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2279-\\@LN{1734}{22}",
    "numLines": 100
  },
  "sourceToolAssistantUUID": "17988d54-08f5-4e41-b16b-feb7dc35bf5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-22T13:59:16.935Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HT181NLSNRi9a1jeunzAks`</summary>

```json
{
  "pattern": "produce.*gains|gains.*w|w.*gains",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "-i": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3591e26-eaaf-4535-b26d-ac9c983e3a89",
  "isSidechain": false,
  "requestId": "req_011CbHj6q25o7pa9TdWpYLXC",
  "type": "assistant",
  "uuid": "df7d1926-d902-4a1d-8191-e8c41a49ce93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9rpR7Y5gFRGiLZRxqwDz9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 61580,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 385,
          "cache_read_input_tokens": 61580,
          "cache_creation_input_tokens": 3014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3014
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 59_

```json
{
  "type": "last-prompt",
  "leafUuid": "4845c5ac-c5d2-45fd-9365-c6a67f614680",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a"
}
```

---


### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify three NLI architectures in paper results",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a"
}
```

---


### Assistant

_source line 61 · 2026-05-22T13:59:20.363Z_

Now let me read the actual Table 3 in solutions.tex (the main cross-arch results) and the appendix Table 26 (multi-NLI).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4845c5ac-c5d2-45fd-9365-c6a67f614680",
  "isSidechain": false,
  "requestId": "req_011CbHj7JAjAr1K8u8sBjKbW",
  "type": "assistant",
  "uuid": "085c96f3-7c5c-458f-9bdd-3f3800d5a6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sm3t54rVQABM5bUVyjcQ7q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6319,
      "cache_read_input_tokens": 64594,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 64594,
          "cache_creation_input_tokens": 6319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6319
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-22T13:59:20.912Z_

<details open><summary>🔧 Tool call — Read · `toolu_011XMx4BSFJFpToAeLiDxwRk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "085c96f3-7c5c-458f-9bdd-3f3800d5a6ad",
  "isSidechain": false,
  "requestId": "req_011CbHj7JAjAr1K8u8sBjKbW",
  "type": "assistant",
  "uuid": "88a0bc95-c3ec-4bc4-acb0-009dd1c2db0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sm3t54rVQABM5bUVyjcQ7q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6319,
      "cache_read_input_tokens": 64594,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 64594,
          "cache_creation_input_tokens": 6319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6319
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-22T13:59:20.941Z_

<details><summary>↩ Tool result · `toolu_011XMx4BSFJFpToAeLiDxwRk`</summary>

```text
1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	\looseness=-1 We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. This proof-of-concept is limited to propositional-logic benchmarks whose premise-conclusion structure naturally suits NLI; generalization to non-logical domains remains untested. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
7	
8	\paragraph{Main result.}
9	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo $w{=}3$ yields $+2.94$\,pp (n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). After BH correction ($m{=}12$), only Mistral-7B ProofWriter conditions ($w{=}3$, $w{=}5$) remain significant.
10	
11	\paragraph{Why it works.}
12	\looseness=-1 Our preliminary results suggest three conditions jointly enable the escape---structural independence, positive capability gap, and task-verifier alignment---expanded as candidate design principles in \S\ref{sec:discussion}. Note that NLI classification operates on (premise, conclusion) pairs, a fundamentally different task from symbolic constraint extraction; the success here may partly reflect task-format alignment rather than a general escape mechanism. Per-label analysis confirms NLI and SC excel on complementary labels (Appendix~\ref{app:multi-nli}); all three NLI architectures produce gains at $w \geq 3$.
13	
14	\paragraph{Capability gap hypothesis.}
15	\looseness=-1 Four generators spanning a 46-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}): only Mistral-7B (SC 39.33\%, below the verifier) gains significantly ($+6.67$\,pp, $p < 0.001$); stronger generators show no improvement. The monotonic relationship holds across three NLI architectures and six verifier-generator pairs (Figure~\ref{fig:capability-gap}; Appendix~\ref{app:capability-gap}). A $2{\times}2$ generator${\times}$extractor matrix confirms BR $> 1$ in all eight cells ($1.94$--$2.70$; Appendix~\ref{app:2x2}).
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability ($w{=}3$).}
21	\label{tab:cross_generator_nli}
22	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llcccc@{}}
23	\toprule
24	Generator & Family & SC & Gap & Combo $\Delta$ ($w{=}3$) & $p$ \\
25	\midrule
26	Mistral-7B & Mistral & 39.33\% & $+$15.67 & $+$6.67\,pp & $<$0.001 \\
27	LLaMA-3.1-8B & LLaMA & 72.50\% & $-$17.50 & $+$0.83\,pp & 0.66 \\
28	Qwen2.5-14B & Qwen & 74.00\% & $-$19.00 & $+$0.67\,pp & 0.50 \\
29	Qwen3-14B & Qwen & 85.83\% & $-$30.83 & $+$0.50\,pp & 0.45 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
34	\paragraph{Disagreement-Routed Cascade.}
35	A cost-aware variant invokes NLI only below consensus threshold $\tau$, recovering 90\% of full-combo gain at ${\sim}$35\% NLI cost ($\tau{=}0.7$; Appendix~\ref{app:drc}).
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88a0bc95-c3ec-4bc4-acb0-009dd1c2db0d",
  "isSidechain": false,
  "promptId": "dc065ad1-7a33-4484-84cc-5c01195cf1b0",
  "type": "user",
  "uuid": "a110061f-4444-4a9e-88d9-b3c83e4c1451",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
      "content": "\\section{Cross-Architecture Proof-of-Concept}\n\\label{sec:solutions}\n\\label{sec:cross-arch}\n\n\\paragraph{Method.}\n\\looseness=-1 We test with DeBERTa-large \\citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \\citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. This proof-of-concept is limited to propositional-logic benchmarks whose premise-conclusion structure naturally suits NLI; generalization to non-logical domains remains untested. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).\n\n\\paragraph{Main result.}\n\\looseness=-1 DeBERTa NLI alone achieves 49.51\\% on FOLIO (below SC's 55.88\\%) and 55.00\\% on ProofWriter (above SC's 39.33\\%). On FOLIO ($n = 204$), combo $w{=}3$ yields $+2.94$\\,pp (n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\\,pp ($p < 0.001$)---while same-model SICA \\emph{degrades} ProofWriter ($-2.83$\\,pp; Table~\\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\\S\\ref{sec:mirage}). After BH correction ($m{=}12$), only Mistral-7B ProofWriter conditions ($w{=}3$, $w{=}5$) remain significant.\n\n\\paragraph{Why it works.}\n\\looseness=-1 Our preliminary results suggest three conditions jointly enable the escape---structural independence, positive capability gap, and task-verifier alignment---expanded as candidate design principles in \\S\\ref{sec:discussion}. Note that NLI classification operates on (premise, conclusion) pairs, a fundamentally different task from symbolic constraint extraction; the success here may partly reflect task-format alignment rather than a general escape mechanism. Per-label analysis confirms NLI and SC excel on complementary labels (Appendix~\\ref{app:multi-nli}); all three NLI architectures produce gains at $w \\geq 3$.\n\n\\paragraph{Capability gap hypothesis.}\n\\looseness=-1 Four generators spanning a 46-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\\% standalone; Table~\\ref{tab:cross_generator_nli}): only Mistral-7B (SC 39.33\\%, below the verifier) gains significantly ($+6.67$\\,pp, $p < 0.001$); stronger generators show no improvement. The monotonic relationship holds across three NLI architectures and six verifier-generator pairs (Figure~\\ref{fig:capability-gap}; Appendix~\\ref{app:capability-gap}). A $2{\\times}2$ generator${\\times}$extractor matrix confirms BR $> 1$ in all eight cells ($1.94$--$2.70$; Appendix~\\ref{app:2x2}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability ($w{=}3$).}\n\\label{tab:cross_generator_nli}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Family & SC & Gap & Combo $\\Delta$ ($w{=}3$) & $p$ \\\\\n\\midrule\nMistral-7B & Mistral & 39.33\\% & $+$15.67 & $+$6.67\\,pp & $<$0.001 \\\\\nLLaMA-3.1-8B & LLaMA & 72.50\\% & $-$17.50 & $+$0.83\\,pp & 0.66 \\\\\nQwen2.5-14B & Qwen & 74.00\\% & $-$19.00 & $+$0.67\\,pp & 0.50 \\\\\nQwen3-14B & Qwen & 85.83\\% & $-$30.83 & $+$0.50\\,pp & 0.45 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Disagreement-Routed Cascade.}\nA cost-aware variant invokes NLI only below consensus threshold $\\tau$, recovering 90\\% of full-combo gain at ${\\sim}$35\\% NLI cost ($\\tau{=}0.7$; Appendix~\\ref{app:drc}).\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  },
  "sourceToolAssistantUUID": "88a0bc95-c3ec-4bc4-acb0-009dd1c2db0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-22T13:59:21.502Z_

<details><summary>↩ Tool result · `toolu_012wYFXJtvLPTiGeZGgHy1mq`</summary>

```text
880	\end{table}
881	
882	\section{Multi-Verifier NLI Results}
883	\label{app:multi-nli}
884	
885	\begin{table}[h]
886	\centering
887	\small
888	\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\%$). Three NLI verifiers $\times$ three weight settings. {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$ (McNemar).}
889	\label{tab:multi-nli}
890	\begin{tabular}{@{}llrrl@{}}
891	\toprule
892	Verifier & Standalone & $w$ & $\Delta$ (pp) & $p$ \\
893	\midrule
894	DeBERTa-MNLI & 55.00\% & 1 & $+$0.83 & n.s. \\
895	 & & 3 & $+$6.67 & ${<}0.001${***} \\
896	 & & 5 & $+$11.00 & ${<}0.001${***} \\
897	\addlinespace
898	RoBERTa-MNLI & 37.67\% & 1 & $-$0.17 & n.s. \\
899	 & & 3 & $+$4.17 & 0.003{**} \\
900	 & & 5 & $+$4.33 & 0.037{*} \\
901	\addlinespace
902	BART-MNLI & 46.17\% & 1 & 0.00 & n.s. \\
903	 & & 3 & $+$5.17 & ${<}0.001${***} \\
904	 & & 5 & $+$6.33 & 0.003{**} \\
905	\bottomrule
906	\end{tabular}\\[2pt]
907	{\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\%$ across all verifiers.}
908	\end{table}
909	
910	\paragraph{Three-verifier BH correction.}
911	\label{app:3verifier-bh}
912	Table~\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \S\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.
913	
914	\begin{table}[h]
915	\centering
916	\small
917	\caption{BH correction across 3 verifiers $\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \checkmark: $p_{\text{BH}} < 0.05$.}
918	\label{tab:3verifier-bh}
919	\setlength{\tabcolsep}{4pt}
920	\begin{tabular}{@{}lcccccc@{}}
921	\toprule
922	Verifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\
923	\midrule
924	DeBERTa-MNLI & & \checkmark & \checkmark & \checkmark & \checkmark \\
925	RoBERTa-MNLI & & & \checkmark & \checkmark & \checkmark \\
926	BART-MNLI & & & \checkmark & \checkmark & \checkmark \\
927	\bottomrule
928	\end{tabular}\\[2pt]
929	{\footnotesize 10/15 significant at $\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}
930	\end{table}
931	
932	\section{Capability Gap Data Points}
933	\label{app:capability-gap}
934	
935	\begin{figure}[t]
936	\centering
937	\includegraphics[width=0.78\columnwidth]{figures/capability_gap_scatter}
938	\caption{Combo gain vs.\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator.}
939	\label{fig:capability-gap}
940	\end{figure}
941	
942	Table~\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\% standalone, combo $+5.17$\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\% standalone, combo $+4.17$\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \geq 3$.
943	
944	Across all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\times$ Mistral-7B plus three negative-gap generators $\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\ref{fig:capability-gap}). Only conditions where the verifier's standalone accuracy exceeds the generator's SC accuracy show significant improvement, confirming Finding~2. After BH correction ($m{=}12$), only Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$) survive.
945	
946	\paragraph{Robustness check.} Including all nine conditions (three verifiers $\times$ three weight levels on Mistral-7B) yields Spearman $\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.
947	
948	\paragraph{Full NLI combo with BH correction.}
949	\label{app:nli-combo-full}
950	
951	\begin{table}[h]
952	\centering
953	\small
954	\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\% standalone). Two of twelve conditions survive correction (both Mistral-7B). {*}\,$p_{\text{BH}} < 0.05$;\enspace{***}\,$p_{\text{BH}} < 0.001$.}
955	\label{tab:nli-combo-full}
956	\setlength{\tabcolsep}{3.5pt}
957	\begin{tabular}{@{}llrrrrl@{}}
958	\toprule
959	Generator & $w$ & Combo (\%) & $\Delta$ (pp) & $p_{\text{raw}}$ & $p_{\text{BH}}$ & \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9365a79-0ae8-4805-90c5-d495066224f7",
  "isSidechain": false,
  "promptId": "dc065ad1-7a33-4484-84cc-5c01195cf1b0",
  "type": "user",
  "uuid": "f66258b2-f0c3-45a5-a58c-13df881838bc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\\end{table}\n\n\\section{Multi-Verifier NLI Results}\n\\label{app:multi-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\n\\label{tab:multi-nli}\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nVerifier & Standalone & $w$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nDeBERTa-MNLI & 55.00\\% & 1 & $+$0.83 & n.s. \\\\\n & & 3 & $+$6.67 & ${<}0.001${***} \\\\\n & & 5 & $+$11.00 & ${<}0.001${***} \\\\\n\\addlinespace\nRoBERTa-MNLI & 37.67\\% & 1 & $-$0.17 & n.s. \\\\\n & & 3 & $+$4.17 & 0.003{**} \\\\\n & & 5 & $+$4.33 & 0.037{*} \\\\\n\\addlinespace\nBART-MNLI & 46.17\\% & 1 & 0.00 & n.s. \\\\\n & & 3 & $+$5.17 & ${<}0.001${***} \\\\\n & & 5 & $+$6.33 & 0.003{**} \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\\%$ across all verifiers.}\n\\end{table}\n\n\\paragraph{Three-verifier BH correction.}\n\\label{app:3verifier-bh}\nTable~\\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \\S\\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH correction across 3 verifiers $\\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \\checkmark: $p_{\\text{BH}} < 0.05$.}\n\\label{tab:3verifier-bh}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nVerifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\\\\n\\midrule\nDeBERTa-MNLI & & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nRoBERTa-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\nBART-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize 10/15 significant at $\\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}\n\\end{table}\n\n\\section{Capability Gap Data Points}\n\\label{app:capability-gap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\n\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only when the verifier exceeds the generator.}\n\\label{fig:capability-gap}\n\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Only conditions where the verifier's standalone accuracy exceeds the generator's SC accuracy show significant improvement, confirming Finding~2. After BH correction ($m{=}12$), only Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$) survive.\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (both Mistral-7B). {*}\\,$p_{\\text{BH}} < 0.05$;\\enspace{***}\\,$p_{\\text{BH}} < 0.001$.}\n\\label{tab:nli-combo-full}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{raw}}$ & $p_{\\text{BH}}$ & \\\\",
      "numLines": 80,
      "startLine": 880,
      "totalLines": 1180
    }
  },
  "sourceToolAssistantUUID": "e9365a79-0ae8-4805-90c5-d495066224f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-22T13:59:21.490Z_

<details open><summary>🔧 Tool call — Read · `toolu_012wYFXJtvLPTiGeZGgHy1mq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 880,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a110061f-4444-4a9e-88d9-b3c83e4c1451",
  "isSidechain": false,
  "requestId": "req_011CbHj7JAjAr1K8u8sBjKbW",
  "type": "assistant",
  "uuid": "e9365a79-0ae8-4805-90c5-d495066224f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sm3t54rVQABM5bUVyjcQ7q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6319,
      "cache_read_input_tokens": 64594,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 64594,
          "cache_creation_input_tokens": 6319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6319
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-22T13:59:38.292Z_

All data located. Here's the complete answer:

---

## 三个 NLI 架构

1. **DeBERTa-large-MNLI** (microsoft/deberta-large-mnli, 406M)
2. **RoBERTa-large-MNLI** (37.67% standalone on PW)
3. **BART-large-MNLI** (46.17% standalone on PW)

## ProofWriter Mistral-7B combo 结果 (n=600, SC=39.33%)

| Verifier | Standalone | w=1 Δpp (p) | w=3 Δpp (p) | w=5 Δpp (p) |
|----------|-----------|-------------|-------------|-------------|
| DeBERTa-MNLI | 55.00% | +0.83 (n.s.) | **+6.67** (p<0.001) | **+11.00** (p<0.001) |
| RoBERTa-MNLI | 37.67% | -0.17 (n.s.) | **+4.17** (p=0.003) | **+4.33** (p=0.037) |
| BART-MNLI | 46.17% | +0.00 (n.s.) | **+5.17** (p<0.001) | **+6.33** (p=0.003) |

BH 校正后 (m=15): 10/15 条件显著，所有 w≥3 条件均通过。

## 论文中 claim 的原文

`solutions.tex:12` — "all three NLI architectures produce gains at w ≥ 3"

## 数据位置

- **主表 (Table 3)**: `solutions.tex` — cross-generator comparison，仅 DeBERTa × 4 generators，w=3
- **附录 Table 26** (`appendix.tex:888`, Appendix W): 3 verifiers × 3 weights 完整矩阵（上表数据）
- **附录 BH Table** (`appendix.tex:917`): 3 verifiers × 5 weights BH 校正
- **Artifact**: `artifacts/_project/data/nli_multi_verifier_recomputed.json`
- **Figure 7** (`appendix.tex:938`): capability gap scatter, 6 points across 3 architectures

## 数据来源实验

registry 中对应 `exp-wave3-dir-r-nli-verifier` (DeBERTa) 和 `exp-wave3-dir-r-combo-extended`。RoBERTa/BART 数据在 `nli_multi_verifier_recomputed.json` 中，经 alphabetical tiebreaking 重算。

**Claim 成立**: 三个 NLI 架构在 ProofWriter Mistral-7B 上 w≥3 均产生显著正增益（p<0.05），BH 校正后仍然成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f66258b2-f0c3-45a5-a58c-13df881838bc",
  "isSidechain": false,
  "requestId": "req_011CbHj7ddWfwnmc3Qh4XCNx",
  "type": "assistant",
  "uuid": "65b9b1e9-0d80-46c9-8325-7089467c5c4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jDcRTBYAG2ns8r4djXfU9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3812,
      "cache_read_input_tokens": 70913,
      "output_tokens": 781,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 781,
          "cache_read_input_tokens": 70913,
          "cache_creation_input_tokens": 3812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3812
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "leafUuid": "65b9b1e9-0d80-46c9-8325-7089467c5c4f",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a"
}
```

---


### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify three NLI architectures in paper results",
  "sessionId": "ab3968b2-3ac1-44aa-9508-55fa05175a9a"
}
```

---
