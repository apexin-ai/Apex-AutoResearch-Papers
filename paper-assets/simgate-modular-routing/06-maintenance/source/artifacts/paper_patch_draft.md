# Paper Patch Drafts

Pre-drafted LaTeX patches for pending experimental results. [TBD] placeholders mark data from Gemma-2-9B ScienceWorld and Llama-3.1-8B ALFWorld experiments.

---

## Section 2a: ALFWorld Subsection Expansion

Current ALFWorld coverage is a single paragraph in Section 4.4 (Cross-Environment Boundary Probes). This draft expands it to incorporate cross-model replication and formal DAF=0% explanation.

```latex
\paragraph{Cross-environment validation: ALFWorld.}
ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides a complementary test environment where the deterministic strategy receives admissible-action enumeration---an information asymmetry rather than a computation mode switch.
Unlike ScienceWorld, ALFWorld has no death mechanism: $\delta = 0$ and DAF $= 0\%$ by construction.
The entire routing signal arises from information asymmetry: the admissible-action oracle eliminates exploration errors that the internal strategy must resolve through trial-and-error interaction.

With Qwen2.5-7B-Instruct, 35 of 37 non-tie labels (94.6\%) favor the information-advantaged strategy, with 25.9\% det-preferred, 1.5\% int-preferred, and 72.6\% no-preference across 135 episodes.
The per-task-type breakdown (Appendix~\ref{app:cross-env-details}, Table~\ref{tab:alfworld-pertask}) reveals that \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$), while multi-object tasks requiring sequential reasoning show weaker effects, consistent with admissible actions providing less advantage when planning depth matters.

Cross-model replication with Llama-3.1-8B-Instruct ([TBD] games) yields [TBD]\% det-preferred, [TBD]\% int-preferred, and [TBD]\% no-preference, with [TBD] of [TBD] non-tie labels favoring the information-advantaged strategy ([TBD]\%).
The information-asymmetry mechanism replicates across model families: both models show zero death labels and one-directional dominance driven by admissible-action access rather than catastrophic failure.

This cross-environment contrast is diagnostic: the framework correctly identifies qualitatively different mechanisms---death avoidance in ScienceWorld (DAF $= 90.4\%$) versus information asymmetry in ALFWorld (DAF $= 0\%$)---without modification.
The DAF $= 0\%$ result is not a failure of the framework but a correct diagnosis: when no death mechanism exists, all routing signal must originate from non-death performance differences, and the framework quantifies this distinction.
```

---

## Section 2b: Cross-Model and Cross-Environment Table Expansion

Current cross-model data is spread across Section 4.2 (Llama ScienceWorld) and Section 4.3 (72B scaling). This draft consolidates into a unified table spanning models and environments.

```latex
\begin{table}[t]
\centering
\small
\begin{tabular}{llccccc}
\toprule
Model & Environment & $n$ & Int DR & Det DR & $\Delta$DR & DAF \\
\midrule
Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% \\
Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% \\
Gemma-2-9B & ScienceWorld & [TBD] & [TBD] & [TBD] & [TBD] & [TBD] \\
Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% \\
\midrule
Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% \\
Llama-3.1-8B & ALFWorld & [TBD] & [TBD] & [TBD] & [TBD] & [TBD] \\
\midrule
Qwen2.5-7B & MATH & 300 & N/A & N/A & N/A & N/A \\
\bottomrule
\end{tabular}
\caption{Cross-model and cross-environment replication of the counterfactual routing analysis. \textbf{ScienceWorld}: death dominance replicates across three model families (7--9B range) and persists under $10{\times}$ scaling (72B); internal vulnerability is structurally similar (${\sim}$41--43\% at 7--9B), while the differential magnitude varies with deterministic strategy safety. \textbf{ALFWorld}: DAF $= 0\%$ by construction (no death mechanism); routing signal arises from information asymmetry via admissible-action access. \textbf{MATH}: near-identical accuracy between strategies; no routing signal emerges without catastrophic failure. DR = death rate; $\Delta$DR = internal DR $-$ deterministic DR; DAF = Death Avoidance Factor at $P{=}100$.}
\label{tab:cross-model-env}
\end{table}
```

### Notes on table placement

- **If Gemma confirms death dominance (DAF > 80%)**: promote this table to main text (replace or supplement current Table 3 in Section 4.3), adding a row count of "3 model families" in the caption.
- **If Gemma is weaker (DAF 50-80%)**: keep the table in the appendix (Appendix M), reference from main text with a sentence like "A third model family (Gemma-2-9B) shows directionally consistent but attenuated death dominance (Appendix~\ref{app:cross-model})."
- **If Gemma reverses**: table still goes in appendix, but caption and surrounding text must discuss the model-dependency finding honestly.

### Integration with existing text

The current Section 4.2 (Multi-Model Validation) text about Llama remains valid. The expanded table consolidates data that is currently scattered across:
- Section 4.2: Llama-3.1-8B ScienceWorld data
- Section 4.3: Qwen2.5-72B data (currently in Table 2, agent improvement context)
- Section 4.4: ALFWorld Qwen data
- Appendix L: ALFWorld per-task breakdown
- Appendix M: Llama per-task breakdown

The MATH row uses N/A for death-related metrics because MATH episodes use a code interpreter with no death mechanism; the 795-episode dataset is referenced in Section 4.4 but death rates are not applicable.
