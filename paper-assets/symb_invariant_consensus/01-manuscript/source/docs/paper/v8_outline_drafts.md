# V8 Outline Drafts — Working Document

Status: DRAFT, not committed to .tex. Awaiting Director approval + Dir-J data.

---

## Abstract Core Sentence (Draft)

We hypothesized that aggregating First-Order Logic constraints from $K$ reasoning traces would beat majority voting. Across 12+ orthogonal interventions, 6 ensemble configurations, and the full LLM capability range (Mistral-7B at 54\% to Qwen3-14B thinking mode at 86\%), no constraint-space or ensemble-space method significantly improves over Self-Consistency. We formalize this as the \emph{Symbolic Mirage}---self-extracted constraints project the generating model's distributional biases rather than providing independent verification---and prove a structural bound (Bias Ratio $4.97\times$, Effective-$K < 2$) that explains why. Cross-architecture verification is the only direction that escapes the bound: a 406M DeBERTa NLI verifier achieves $+3.50$\,pp ($p = 0.013$, BH-adjusted $p = 0.038$) on ProofWriter, where same-model SICA \emph{degrades} by $-2.83$\,pp.

---

## §4.x Cross-Capability Universality (Draft)

### Key Finding Sentence

Even the strongest LLM we tested---Qwen3-14B in thinking mode, which reaches 86.27\% SC accuracy---does not benefit from SICA: $\Delta = +0.49$\,pp, McNemar $p = 1.0$, with only 3 discordant pairs out of 204 problems.

### Supporting Paragraph

The Symbolic Mirage operates across the full capability spectrum. Table~\ref{tab:cross-capability} shows SICA's effect spanning a 32\,pp SC range: Mistral-7B (54.41\%) through Qwen3-14B thinking mode (86.27\%). At the low end, SICA produces its only positive trends but none reach significance; at the high end, trace homogeneity ($\kappa = 0.91$, $K_{\text{eff}} = 1.09$) collapses SICA to SC. The cross-capability pattern confirms the mirage is not a capability-dependent artifact but a structural property of self-extraction: stronger models produce more homogeneous traces (Proposition~2), stronger confirmation bias compresses the accuracy ceiling (Proposition~4), and late-step contamination intensifies with reasoning depth (Proposition~5). No capability level escapes.

---

## §5.1 CAV Formal Statement (Draft)

### Cross-Architecture Verification (CAV)

Let $M_1$ (generator) and $M_2$ (verifier) be models with architecturally independent inductive biases, i.e., their error sets satisfy $\text{Corr}(e_{M_1}, e_{M_2}) \approx 0$. Define the CAV ensemble prediction:

$$a^*_{\text{CAV}} = \arg\max_a \; \text{votes}_{M_1}(a) + w \cdot \mathbb{1}[v_{M_2} = a]$$

where $v_{M_2}$ is $M_2$'s independent verdict and $w$ controls verifier influence. Unlike same-model symbolic aggregation where $\text{BR}(M_1, M_1) > 1$ causes systematic bias amplification (Proposition 1), the cross-architecture condition ensures $\text{BR}(M_1, M_2) \to 1$: the verifier's errors are uncorrelated with the generator's, providing genuine corrective signal on the generator's error subset. CAV improves over SC when:

$$P(v_{M_2} = a^* \mid a_{M_1} \neq a^*) > P(v_{M_2} \neq a^* \mid a_{M_1} = a^*)$$

i.e., the verifier corrects the generator more often than it corrupts it---satisfied when $M_2$'s per-label accuracy exceeds chance on $M_1$'s error distribution.

**Empirical validation**: DeBERTa-large (406M, encoder-only, NLI-trained) and Mistral-7B (decoder-only, instruction-tuned) share no architecture, training data, or inference mechanism. On Mistral's weakest category (False: 43% of errors), DeBERTa achieves 71.43% vs SC's 38.10% via contradiction detection. ProofWriter w=3: +3.50pp, p=0.013, BH-adjusted p=0.038.

---

## §6.x HGE Negative + Discussion (Draft)

### HGE Key Finding

Six ensemble configurations (Heterogeneous Generator Ensemble) all underperform the best single model by 1.81--2.84\,pp. Generator-side mixing cannot escape the mirage: combining models with different biases incurs an anti-diversity penalty where cross-model constraints are rejected by Z3 rather than providing complementary signal.

### Qwen3-14B Thinking Mode Sentence

Thinking-mode reasoning intensifies rather than alleviates the mirage: Qwen3-14B ($\kappa = 0.91$, $C_0 = 2.6\%$) produces near-identical traces across samples, compressing $K_{\text{eff}}$ to 1.09. The 32\,pp capability advantage over Mistral-7B translates to zero SICA benefit ($\Delta = +0.49$\,pp, $p = 1.0$).

---

## §5.3 Generalization [PENDING DATA]

Awaiting Dir-J1 (LogiQA cross-arch), Dir-J2 (Qwen3-14B base), Dir-J3 (multi-verifier ensemble).

---

## Data Registry

| Exp ID | Data | Source |
|--------|------|--------|
| exp028b | Qwen3-14B thinking SICA: 86.76%, SC: 86.27%, Δ=+0.49pp, p=1.0, 3 discordant | Dir-I-3 |
| (pending) | HGE 6 configs, all -1.81 to -2.84pp vs best single | Dir-I-3 |
| (pending) | Dir-J1/J2/J3 cross-arch generalization | Dir-J |
