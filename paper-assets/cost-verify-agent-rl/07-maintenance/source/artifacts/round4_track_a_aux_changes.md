# Round 4 Track A-Aux Changes

## Item 5: Method Selection Framework (discussion.tex)

### Before
```
\paragraph{Practitioner guidance.}
Use episode-level credit when the full episode fits in context; otherwise use the largest feasible $h$ ($h{\geq}20$; $h{\leq}10$ collapses). Finer-grained methods (Turn-PPO, GAGPO) should be applied only after establishing an episode-level baseline, as they assume correct gradient direction.
```

### After
```
\paragraph{Practitioner guidance.}
Use episode-level credit when the full episode fits in context; otherwise use the largest feasible $h$ ($h{\geq}20$; $h{\leq}10$ collapses). Finer-grained methods (Turn-PPO, GAGPO) should be applied only after establishing an episode-level baseline, as they assume correct gradient direction.

\paragraph{Method selection.}
The M1/M2 diagnostic framework guides practitioners toward the appropriate fix without exhaustive ablation. If only M2 is active (sign misattribution with sufficient observation context, e.g., $h$ large enough to preserve task-relevant information), methods that correct per-step credit---Turn-PPO~\cite{turnppo2025}, HCAPO~\cite{hcapo2026}, GiGPO~\cite{feng2025gigpo}---directly address the failure mode by replacing outcome-based advantage with finer-grained credit signals. If only M1 is active (information loss from truncated context without sign corruption), increasing the observation window $h$ or switching to full-context encoding resolves the bottleneck. When both M1 and M2 co-occur (the typical default configuration), episode-level methods eliminate M2 entirely and M1 simultaneously, as demonstrated by our Cell~D results. The practical value of this framework is diagnostic, not algorithmic: it helps practitioners identify \textit{which} existing method to apply rather than proposing a new one.
```

## Item 6: REINFORCE++ and Dense Baselines Table (appendix.tex)

### Before
(No table between REINFORCE++ paragraph and Discount factor sweep)

### After
```
\begin{table}[h]
\centering
\caption{Additional baselines on ALFWorld (1.7B). Neither method improves over the SFT baseline on in-distribution tasks.}
\label{tab:additional_baselines}
\small
\begin{tabular}{@{}lccc@{}}
\toprule
\textbf{Method} & \textbf{Best Step} & \textbf{In-Dist (\%)} & \textbf{OOD (\%)} \\
\midrule
SFT baseline & --- & 12.50 & 6.72 \\
Dense reward ($h{=}2$) & 5 & 0 & 0 \\
REINFORCE++ & 5 & 12.50 & --- \\
\bottomrule
\end{tabular}
\end{table}
```

## Item 8: Discussion Scope Limitation (discussion.tex)

### Before
```
Sign misattribution arises whenever three structural properties co-occur: (a) step-level windowing, (b) sparse binary reward, and (c) group-relative normalization. Under these conditions, ...
```

### After
```
Sign misattribution arises whenever three structural properties co-occur: (a) step-level windowing, (b) sparse binary reward, and (c) group-relative normalization. These three conditions are theoretically sufficient within any group-relative normalization framework (Section~\ref{sec:theory}), though our experimental verification is limited to GRPO on ALFWorld and ScienceWorld. Under these conditions, ...
```

## Item 9: Missing References (references.bib + related_work.tex)

### references.bib — Added entries
- `dapo2025`: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale" (Yu et al., arXiv:2503.14476)
- `vapo2025`: "VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks" (Yue et al., arXiv:2504.05118)
- `prime2025`: "Process Reinforcement through Implicit Rewards" (Cui et al., arXiv:2502.01456)
- `ahmadian2024back`: "Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs" (Ahmadian et al., ACL 2024)

### related_work.tex — RL for multi-turn LLM agents paragraph
#### Before
```
PPO~\cite{schulman2017ppo}, GRPO~\cite{shao2024deepseekmath}, and DPO~\cite{rafailov2023dpo} underpin RLHF~\cite{ouyang2022instructgpt} and have been extended to multi-turn agents~\cite{yao2023react} through step-independent windowing~\cite{ragen2025}. Subsequent work improves algorithms (GiGPO~\cite{feng2025gigpo}), reward design ...
```
#### After
```
PPO~\cite{schulman2017ppo}, GRPO~\cite{shao2024deepseekmath}, and DPO~\cite{rafailov2023dpo} underpin RLHF~\cite{ouyang2022instructgpt} and have been extended to multi-turn agents~\cite{yao2023react} through step-independent windowing~\cite{ragen2025}. Ahmadian et al.~\cite{ahmadian2024back} show that simpler REINFORCE-style methods can match PPO for single-turn RLHF, but the multi-turn credit assignment problem remains unaddressed. Subsequent work improves algorithms (GiGPO~\cite{feng2025gigpo}, DAPO~\cite{dapo2025}), reward design ...
```

### related_work.tex — Credit assignment paragraph
#### Before
```
... Hindsight credit assignment~\cite{harutyunyan2019hindsight} and return decomposition~\cite{arjona2019rudder} address delayed reward through temporal decomposition, complementary to our sign-level diagnosis. Several studies corroborate ...
```
#### After
```
... Hindsight credit assignment~\cite{harutyunyan2019hindsight} and return decomposition~\cite{arjona2019rudder} address delayed reward through temporal decomposition, complementary to our sign-level diagnosis. PRIME~\cite{prime2025} enables implicit process reward models that provide step-level supervision using only outcome labels, while VAPO~\cite{vapo2025} augments policy optimization with a value model for finer-grained credit in reasoning tasks. Several studies corroborate ...
```

## M3: Seed Classification Threshold Sensitivity (appendix.tex)

### Before
```
The small standard deviation (1.29pp) confirms that the large inter-seed differences observed in Table~\ref{tab:seed_variability}---ranging from 0\% (collapsed) to 30.6\% (generalized)---reflect genuine training dynamics rather than evaluation noise.
```

### After
```
The small standard deviation (1.29pp) confirms that the large inter-seed differences observed in Table~\ref{tab:seed_variability}---ranging from 0\% (collapsed) to 30.6\% (generalized)---reflect genuine training dynamics rather than evaluation noise. We note that this variance estimate is based on a stagnant seed (seed200); generalized seeds with higher success rates may exhibit different variance profiles due to the non-linear relationship between success rate and binomial variance.

The classification threshold between stagnant and generalized seeds is based on Fisher's exact test at $p < 0.05$ vs.\ the SFT baseline; shifting to $p < 0.01$ would reclassify seed2 (the marginal case at $p = 0.03$) as stagnant, changing the generalization rate from 36\% to 27\%.
```

## M4: AI Disclosure Wording (appendix.tex)

### Before
```
\item \textbf{Literature:} summarizing related papers to inform
    related-work section.
```

### After
```
\item \textbf{Literature:} identifying potentially relevant papers to inform
    our literature review.
```

## Q1: Cell C Hyperparameter Details (appendix.tex)

**Skipped** — already present in existing text: "KL penalty $\beta \in \{0.001, 0.01, 0.04\}$, learning rate $\in \{5{\times}10^{-7}, 10^{-6}\}$). All runs terminated due to training instability: KL divergence spiked above 10.0 within 2--3 steps"

## Q3: HCAPO h=2 Discussion (discussion.tex)

### Before
```
Recent concurrent methods validate our diagnosis. HCAPO~\cite{hcapo2026} achieves 91.4\% on ALFWorld (7B) by directly addressing M2 through hindsight credit assignment, while retaining $h{=}2$ windowed context (M1). GiGPO~\cite{feng2025gigpo} similarly achieves 90.2\% ... confirming that sign misattribution (M2) is the primary destructive mechanism. Note that these results use 7B models; direct numerical comparison with our 1.7B results is not meaningful.
```

### After
```
Recent concurrent methods validate our diagnosis. HCAPO~\cite{hcapo2026} retains the $h{=}2$ windowed context (preserving M1) but replaces step-level advantage with hindsight credit assignment, directly eliminating M2. Its success (91.4\% at 7B) confirms that M2 is the primary destructive mechanism even when M1 imposes a performance ceiling. GiGPO~\cite{feng2025gigpo} similarly achieves 90.2\% with step-level credit refinement. Both methods avoid the collapse we diagnose while using the same $h{=}2$ configuration that causes catastrophic failure under standard GRPO (Cell~A). Note that these results use 7B models; direct numerical comparison with our 1.7B results is not meaningful.
```

## Q5: Episode vs Step Wall-Clock Comparison (appendix.tex)

### Before
(Not present)

### After
```
\paragraph{Training efficiency.} Episode-level training processes the same total tokens as step-independent training but in fewer, longer sequences. On our hardware (2$\times$ RTX PRO 6000, 1.7B model), step-independent training ($h{=}2$) completes 15 steps in approximately 10--12 hours; episode-level training takes comparable wall-clock time as the increased sequence length is offset by fewer padding tokens.
```

## Q6: Eval Variance Stagnant-Only Caveat (appendix.tex)

### Before
```
The small standard deviation (1.29pp) confirms that the large inter-seed differences observed in Table~\ref{tab:seed_variability}---ranging from 0\% (collapsed) to 30.6\% (generalized)---reflect genuine training dynamics rather than evaluation noise.
```

### After
```
The small standard deviation (1.29pp) confirms that the large inter-seed differences observed in Table~\ref{tab:seed_variability}---ranging from 0\% (collapsed) to 30.6\% (generalized)---reflect genuine training dynamics rather than evaluation noise. We note that this variance estimate is based on a stagnant seed (seed200); generalized seeds with higher success rates may exhibit different variance profiles due to the non-linear relationship between success rate and binomial variance.
```
