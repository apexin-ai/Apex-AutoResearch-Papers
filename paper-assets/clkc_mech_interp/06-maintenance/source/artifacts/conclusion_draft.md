\section{Conclusion}
\label{sec:conclusion}

We presented a mechanistic analysis of cross-lingual knowledge conflicts in multilingual LLMs, combining residual stream probing with representation steering across Llama-3.1-8B-Instruct and Qwen3-8B.
Our results establish three findings: conflict signals are linearly detectable in residual stream representations and transfer across languages via the model's general cross-lingual representational space, not through a conflict-specific encoding mechanism; the transfer asymmetry (ZH$\to$EN $>$ EN$\to$ZH by ${\sim}$7~pp) mirrors a baseline asymmetry observed in non-conflict tasks, attributing it to structural properties of English-dominant models; and a detection--decision layer dissociation places the causal node at mid-layers (${\sim}$41\% depth), upstream of the late-layer probing peak where the conflict outcome becomes linearly readable but is no longer causally relevant.
The confound exclusion pipeline---COMET translation quality stratification, token overlap analysis, and non-conflict baseline comparison---provides a reusable methodological template for cross-lingual probing studies.
Future work should extend these analyses to typologically diverse language pairs and additional model families to test whether the detection--decision dissociation holds more broadly.
