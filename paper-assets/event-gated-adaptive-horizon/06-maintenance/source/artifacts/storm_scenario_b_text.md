# STORM Scenario B — Pre-written Paper Text

> Scenario B: STORM baseline healthy + CIVO does NOT trigger with dt-conditioning.
> This narrows CIVO from "any imagination-based AC" to "RSSM-specific".

---

## 1. analysis.tex ¶4 "Implications beyond DreamerV3" — Scenario B Replacement

**Current text (line 15):**
> The structural vulnerability---shared imagined rollouts defeat diversity-based remedies---is not architecture-specific. Any imagination-based actor-critic that (1)~trains its critic entirely on model-generated rollouts and (2)~bootstraps value targets within the same learned model faces the same closed-loop constraint...

**Scenario B replacement:**

```latex
\paragraph{Implications beyond DreamerV3.}
\looseness=-1 Cross-architecture validation on STORM \citep{zhang2023storm}, a transformer-based world model with identical imagination-based actor-critic training, reveals that CIVO is RSSM-specific: under the same $\dt$-conditioning configuration that reliably induces CIVO in DreamerV3 (trained embedding, subsample ON, $H{=}8$), STORM produces NVE $[TBD]\times$ on Walker Walk---below the $2.0\times$ threshold---with eval return $[TBD]$ ($[TBD]\%$ of its own baseline). This identifies RSSM-specific properties as additional necessary conditions beyond learned temporal embeddings and multi-rate exposure. We hypothesize two architectural factors that may confer immunity. First, the transformer's parallel attention mechanism processes all time steps simultaneously rather than through sequential recurrent updates, potentially reducing the gradient pathway through which $\dt$-embeddings co-adapt with dynamics predictions. Second, the absence of a recurrent bottleneck (DreamerV3's GRU deterministic state) distributes the temporal embedding's influence across multiple attention heads, diluting the concentrated co-adaptation that drives CIVO in the RSSM. These hypotheses are consistent with the negative result but remain untested; targeted ablations (e.g., adding a recurrent bottleneck to STORM) would be needed to confirm the causal mechanism. The shared-rollout constraint---critics trained on model-generated data bootstrap from the same model---remains a structural risk factor for any imagination-based system, but recurrent dynamics appear to be a necessary amplifier for CIVO onset.
```

---

## 2. analysis.tex ¶5 末句 — Scenario B Replacement

**Current text (end of line 18):**
> For transformer-based world models \citep{micheli2023iris}, whether this boundary shifts remains open.

**Scenario B replacement:**

```latex
STORM (transformer world model) does not trigger CIVO at 6~DoF Walker Walk under the same conditions that induce onset in DreamerV3 (NVE $[TBD]\times$ vs.\ $3.32\times$), suggesting the DoF boundary interacts with architecture-specific dynamics processing.
```

---

## 3. Abstract — Scenario B Version

**Current text contains:**
> cross-environment analysis across seven additional environments confirms specificity to moderate-complexity locomotion.

**Scenario B — insert after the above sentence:**

```latex
Cross-architecture validation on a transformer world model (STORM) shows no CIVO onset under identical conditions, identifying recurrent dynamics as an additional necessary factor.
```

**Full sentence in context:**

```latex
...cross-environment analysis across seven additional environments confirms specificity to moderate-complexity locomotion. Cross-architecture validation on a transformer world model (STORM) shows no CIVO onset under identical conditions, identifying recurrent dynamics as an additional necessary factor. The recurrent state-space model develops...
```

---

## 4. Intro — Contribution List Update

If the intro has a numbered contribution list, update the cross-environment bullet to:

```latex
Cross-environment analysis across seven additional environments confirms specificity to moderate-complexity locomotion, and cross-architecture validation on STORM (transformer world model) identifies recurrent dynamics as a necessary architectural condition.
```

---

## 5. Limitations (conclusion.tex) — Scenario B Replacement

**Current text:**
> All experiments use DreamerV3 as the sole world-model architecture; whether CIVO manifests in transformer-based world models remains untested...

**Scenario B replacement:**

```latex
Cross-architecture validation on STORM (transformer world model) shows no CIVO onset, narrowing the vulnerability to RSSM-based dynamics. However, only two architectures have been tested; whether other recurrent world models (e.g., S4-based, Mamba-based) share this vulnerability, and whether the transformer's immunity holds across environments and hyperparameter ranges, remains open. Observations are proprioceptive in simulation; pixel inputs and sim-to-real transfer have not been evaluated.
```

---

## 6. Discussion — New Analysis Paragraph (insert after ¶4)

**New paragraph for Scenario B only:**

```latex
\paragraph{Why transformers may resist CIVO.}
\looseness=-1 STORM's immunity under conditions that reliably trigger CIVO in DreamerV3 suggests that recurrent state processing is a necessary architectural amplifier. We identify two candidate mechanisms, both untested. (1)~\emph{Parallel vs.\ sequential temporal processing}: the RSSM's GRU processes each imagination step sequentially, creating a gradient pathway where the $\dt$-embedding's influence compounds across the recurrent chain; the transformer's self-attention computes all steps in parallel, potentially distributing the embedding's effect across heads and reducing compounding. (2)~\emph{Bottleneck concentration}: the RSSM channels all temporal information through a single deterministic state vector, concentrating co-adaptation pressure; the transformer's multi-head attention distributes information across $h$ independent subspaces. These hypotheses predict that adding a recurrent bottleneck to STORM would restore CIVO susceptibility---a testable prediction for future work.
```

---

## 7. Related Work — Minor Update

Add to the end of the paragraph on value overestimation:

```latex
Our cross-architecture validation on STORM \citep{zhang2023storm} narrows CIVO to RSSM-based dynamics, suggesting that transformer attention mechanisms resist the co-adaptation pathway.
```

---

## Checklist Before Slot-In

- [ ] STORM baseline eval return ≥ 600 (healthy baseline confirmed)
- [ ] STORM + trained dt_emb NVE < 2.0× (CIVO NOT triggered — Scenario B confirmed)
- [ ] STORM frozen control NVE also < 2.0× (both conditions negative)
- [ ] Verify STORM trained dt_emb eval return is NOT catastrophically low (if eval is low but NVE is also low, it's a different failure mode, not CIVO)
- [ ] Replace all `[TBD]` with actual numbers
- [ ] Add `\citep{zhang2023storm}` to references.bib
- [ ] Search-and-replace "architecture-specific" claims in all .tex files
- [ ] Recompile, verify ≤ 10 main pages
