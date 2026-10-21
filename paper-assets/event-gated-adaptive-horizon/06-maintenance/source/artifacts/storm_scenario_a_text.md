# STORM Scenario A — Pre-written Paper Text

> Scenario A: STORM baseline healthy + CIVO triggered with dt-conditioning.
> These texts are ready to slot in once STORM experiment data confirms Scenario A.
> Replace `[TBD]` placeholders with actual numbers.

---

## 1. Table 1 (tab:main_results) — New STORM Section

Insert before `\bottomrule` in `experiments_results.tex`:

```latex
\midrule
\multicolumn{8}{l}{\textit{Transformer world model (cross-architecture)}} \\
--- & STORM Baseline ($\dt{=}1$) & --- & --- & 15 & \textcolor{gray}{TBD} & \textcolor{gray}{TBD} & \textcolor{gray}{TBD}$^h$ \\
\rowcolor{gray!15}
--- & STORM + dt\_emb & trn & ON & 8 & \textcolor{gray}{TBD} & \textcolor{gray}{TBD} & \textcolor{gray}{TBD}$^h$ \\
--- & STORM Frozen emb & frz$^b$ & ON & 8 & \textcolor{gray}{TBD} & \textcolor{gray}{TBD} & \textcolor{gray}{TBD}$^h$ \\
```

Add footnote to caption: `$^h$~STORM (transformer world model); results pending experiment completion.`

---

## 2. analysis.tex ¶4 "Implications beyond DreamerV3" — Scenario A Replacement

**Current text (line 15):**
> The structural vulnerability---shared imagined rollouts defeat diversity-based remedies---is not architecture-specific. Any imagination-based actor-critic that (1)~trains its critic entirely on model-generated rollouts and (2)~bootstraps value targets within the same learned model faces the same closed-loop constraint: remedies that assume diverse or independent training sources (Double Q pessimism, ensemble disagreement, noise injection) lose corrective power when both sides of the training signal originate from the same model. This applies to TD-MPC2 with imagination-only critic training, IRIS with transformer-based world models, and any future architecture that combines temporal conditioning with pure-imagination value estimation. Whether the specific onset boundary (6 DoF locomotion) generalizes remains open; the structural constraint does.

**Scenario A replacement:**

```latex
\paragraph{Implications beyond DreamerV3.}
\looseness=-1 The structural vulnerability is not architecture-specific: CIVO emerges in both the RSSM-based DreamerV3 and the transformer-based STORM \citep{zhang2023storm}, confirming that the phenomenon manifests across RSSM and transformer dynamics architectures, suggesting the vulnerability lies in the imagination-based actor-critic training paradigm rather than any single dynamics model. STORM replaces the GRU-based RSSM with a causal transformer and uses discrete categorical latents (vs.\ DreamerV3's continuous--discrete hybrid), yet trained $\dt$-embeddings produce NVE $[TBD]\times$ on Walker Walk (vs.\ $3.32\times$ in DreamerV3), while frozen controls remain below the $2.0\times$ threshold (NVE $[TBD]\times$). The shared structural factor---critics trained entirely on model-generated rollouts---is the common denominator: any system that (1)~trains its critic on imagined data and (2)~bootstraps value targets within the same learned model faces the same closed-loop constraint. Two architectures do not establish universal generality; whether CIVO manifests in diffusion-based planners \citep{janner2022diffuser} or hybrid real-imagined training regimes remains open.
```

---

## 3. analysis.tex ¶5 末句 — Scenario A Replacement

**Current text (end of line 18):**
> For transformer-based world models \citep{micheli2023iris}, whether this boundary shifts remains open.

**Scenario A replacement:**

```latex
STORM (transformer world model) exhibits CIVO onset at 6~DoF Walker Walk with NVE $[TBD]\times$, consistent with the DreamerV3 boundary; whether the threshold shifts for higher-DoF tasks under transformer dynamics remains open.
```

---

## 4. Abstract — Scenario A Cross-Architecture Insertion

**Current text contains:**
> cross-environment analysis across seven additional environments confirms specificity to moderate-complexity locomotion.

**Scenario A version — insert after the above sentence:**

```latex
Cross-architecture validation on STORM (transformer world model) confirms that CIVO is not specific to RSSM-based dynamics.
```

**Full sentence in context:**

```latex
...cross-environment analysis across seven additional environments confirms specificity to moderate-complexity locomotion. Cross-architecture validation on STORM (transformer world model) confirms that CIVO is not specific to RSSM-based dynamics. The recurrent state-space model develops...
```

Note: This insertion adds ~15 words to the abstract. If space is tight, condense to: "cross-architecture validation on a transformer world model confirms architecture independence."

---

## 5. Limitations Section — Update

**Current text (conclusion.tex line 11):**
> All experiments use DreamerV3 as the sole world-model architecture; whether CIVO manifests in transformer-based world models remains untested...

**Scenario A replacement:**

```latex
Primary experiments use DreamerV3; cross-architecture validation on STORM (transformer world model) confirms CIVO generalizes beyond RSSM, but only two architectures have been tested. Whether CIVO manifests in diffusion-based planners or pixel-input settings remains untested.
```

---

## 6. Related Work — Minor Update

**Current text (related_work.tex) contains a sentence ending with:**
> ...revealing that shared imagined rollouts create a structural constraint...

No change needed for Scenario A — the claim is already architecture-general. Optionally add STORM citation:

```latex
This paper fills the gap at the intersection of temporal conditioning and imagination-based value estimation, with cross-architecture validation on STORM \citep{zhang2023storm} confirming the structural constraint beyond RSSM dynamics.
```

---

## 7. Intro Contribution List — Scenario A Update

**Current text (introduction.tex line 18, end of Contribution 1):**
> ...cross-environment validation confirms specificity to moderate-complexity locomotion (\S\ref{sec:discussion}).

**Scenario A — append before the closing period:**

```latex
    \item \textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning. Factorial analysis isolates trained $\dt$-embedding $+$ multi-rate exposure as jointly necessary for CIVO susceptibility; frozen and removed controls never trigger CIVO. The NVE diagnostic achieves perfect binary classification (AUROC${=}1.000$, $n{=}36$); cross-environment validation confirms specificity to moderate-complexity locomotion, and cross-architecture validation on a transformer world model confirms the phenomenon is not RSSM-specific (\S\ref{sec:discussion}).
```

---

## 8. Appendix — STORM DMC Experiment Details

**New subsection in appendix.tex:**

```latex
\subsection{STORM DMC Adaptation and Experiment Details}
\label{sec:storm_details}

\looseness=-1 To test cross-architecture generalization, we adapted STORM \citep{zhang2023storm}---a transformer world model with discrete categorical latents ($32{\times}32$) and imagination-based actor-critic training---to DMC Walker Walk with proprioceptive observations. The open-source STORM codebase supports only Atari (discrete actions, image observations); our adaptation replaces the CNN encoder/decoder with MLP networks ($24 \to 256 \to 256$, three layers), converts discrete action embeddings to continuous projections ($\text{nn.Linear}(6, 512)$), and implements a TanhGaussian policy for 6-dim continuous control. The transformer dynamics model (2-layer, 8-head, 512-dim) and imagination-based actor-critic training loop are unchanged from the original STORM.

\paragraph{Hyperparameters.}
Batch size $16$, batch length $64$, imagination horizon $15$, world model learning rate $3{\times}10^{-4}$, agent learning rate $3{\times}10^{-5}$, $\gamma{=}0.997$, $\lambda{=}0.95$, entropy coefficient $10^{-4}$, replay buffer $10^6$ transitions, warmup $5000$ steps. Training runs 500K environment steps on a single GPU.

\paragraph{Baseline ($\dt{=}1$).}
[TBD: eval return, learning curve description, comparison to DreamerV3 baseline 787.7±230.8]

\paragraph{$\dt$-conditioning (trained embedding).}
[TBD: eval return, NVE trajectory, CIVO onset description]

\paragraph{Frozen control.}
[TBD: eval return, NVE, confirmation of no CIVO]

\begin{figure}[h]
\centering
% \includegraphics[width=\columnwidth]{figures/storm_learning_curves.pdf}
\caption{STORM Walker Walk: learning curves and NVE trajectories for baseline, trained $\dt$-embedding, and frozen control configurations. [TBD]}
\label{fig:storm_curves}
\end{figure}
```

---

## Checklist Before Slot-In

- [ ] STORM baseline eval return ≥ 600 (healthy baseline threshold)
- [ ] STORM + trained dt_emb NVE ≥ 2.0× (CIVO confirmed)
- [ ] STORM frozen control NVE < 2.0× (control matches)
- [ ] Replace all `[TBD]` with actual numbers
- [ ] Add `\citep{zhang2023storm}` to references.bib
- [ ] Recompile, verify ≤ 10 main pages
- [ ] Update Table 3 (intervention hierarchy) if STORM interventions tested
