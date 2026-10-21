# Excluded Tasks Anti-Cherry-Picking Analysis (C2 Rebuttal)

> **Revision 2026-05-18**: Added C2-focused death dominance analysis with aggregate statistics and paper-ready text. All excluded task data verified against prescreening `summary.json` and MVP runs.

## 0. C2 Anti-Cherry-Picking: Death Dominance in Excluded Tasks

### Core Finding

**18 of 19 excluded task types (95%) exhibit death-asymmetric patterns.** The one exception, grow-plant, shows zero deaths under both strategies (an intrinsically safe task). Death dominance is an environment-level phenomenon across ScienceWorld, not a task-selection artifact.

### Combined Death Rate Table (All 19 Excluded Tasks)

| Task | Group | n | Int DR% | Det DR% | ΔDR (pp) | Int Mean | Det Mean |
|------|-------|---|---------|---------|----------|----------|----------|
| boil | A | 20 | 50.0 | 20.0 | +30.0 | -49.75 | -19.70 |
| change-state-of-matter | A | 20 | 55.0 | 15.0 | +40.0 | -54.70 | -14.50 |
| chem-mix-paint-secondary | A | 20 | 45.0 | 10.0 | +35.0 | -41.00 | -5.50 |
| grow-plant | A | 20 | 0.0 | 0.0 | 0.0 | +0.50 | +0.50 |
| melt | A | 20 | 55.0 | 15.0 | +40.0 | -54.70 | -14.55 |
| chem-mix-paint-tertiary | B | 5 | 40.0 | 20.0 | +20.0 | -37.40 | -17.40 |
| find-living-thing | B | 5 | 60.0 | 20.0 | +40.0 | -58.40 | -16.60 |
| find-plant | B | 5 | 60.0 | 0.0 | +60.0 | -58.40 | +3.20 |
| inclined-friction-named | B | 5 | 60.0 | 20.0 | +40.0 | -60.00 | -20.00 |
| inclined-friction-unnamed | B | 5 | 60.0 | 0.0 | +60.0 | -60.00 | 0.00 |
| lifespan-shortest | B | 5 | 60.0 | 40.0 | +20.0 | -60.00 | -40.00 |
| measure-melt-known | B | 5 | 60.0 | 0.0 | +60.0 | -58.80 | +1.20 |
| mendelian-known | C | 5 | 60.0 | 20.0 | +40.0 | -60.00 | -20.00 |
| mendelian-unknown | C | 5 | 60.0 | 40.0 | +20.0 | -60.00 | -40.00 |
| power-component | C | 5 | 60.0 | 20.0 | +40.0 | -60.00 | -20.00 |
| power-renewable | C | 5 | 60.0 | 0.0 | +60.0 | -60.00 | 0.00 |
| test-conductivity | C | 5 | 60.0 | 20.0 | +40.0 | -60.00 | -20.00 |
| test-conductivity-unknown | C | 5 | 60.0 | 20.0 | +40.0 | -60.00 | -20.00 |
| use-thermometer | C | 5 | 60.0 | 20.0 | +40.0 | -59.40 | -19.40 |

Groups: A = MVP development (20 episodes), B = redundant family variant (5 episodes prescreening), C = agent-incompetent (5 episodes prescreening).

### Aggregate Comparison

| Metric | Excluded (19 tasks) | Included (11 tasks) |
|--------|--------------------|--------------------|
| Tasks with ΔDR > 0 | 18/19 (95%) | 10/11 (91%) |
| Tasks with ΔDR ≥ 20 pp | 18/19 (95%) | 10/11 (91%) |
| Mean int death rate | 53.9% | 46.5%* |
| Mean det death rate | 15.8% | 17.8%* |
| Mean ΔDR | +38.2 pp | +28.7 pp* |
| Tasks with zero deaths both | 1/19 (grow-plant) | 1/11 (find-non-living-thing) |

*Included task stats from plan_c 20-episode evaluation. Excluded Group A from 20-episode MVP data; Groups B-C from 5-episode prescreening.

**Key observations:**
1. Excluded tasks have **higher** internal death rates (53.9% vs 46.5%) and **higher** death-rate differential (+38.2 pp vs +28.7 pp) than included tasks. The included subset is, if anything, LESS death-prone.
2. Both populations have exactly one zero-death task each (grow-plant excluded, find-non-living-thing included), showing the selection retains non-death-dominated tasks.
3. Deterministic death rates are comparable (15.8% excluded vs 17.8% included), confirming the asymmetry is specific to internal reasoning.

### LaTeX Table (Paper-Ready)

```latex
\begin{table}[t]
\centering
\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{tabular}{@{}llrcccl@{}}
\toprule
Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
\midrule
boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
\midrule
chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
\midrule
mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
\midrule
\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
\bottomrule
\end{tabular}
\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks.}
\label{tab:excluded-death}
\end{table}
```

### Appendix C Paragraph (Ready to Insert)

> Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp. This exceeds the $+28.7$\,pp mean among included tasks. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Rather, the excluded tasks either lack a viable routing alternative (deterministic also fails) or provide no non-death routing variation. This confirms that death dominance is an environment-level phenomenon spanning all ScienceWorld task families, not an artifact of task selection.

---

## 1. Complete 30-Task Classification

### Data Sources

| Source | Description | Episodes per task |
|--------|-------------|-------------------|
| **plan_c** | Plan-001b full evaluation | 20-40 |
| **mvp** | MVP development runs | 20 |
| **prescreening** | 5-episode screening runs | 5 |

### Included (11 tasks, 245 episodes)

| Task | n | source | det_death% | int_death% | det_mean | int_mean | det_nd | int_nd | Δnd |
|------|---|--------|-----------|-----------|----------|----------|--------|--------|-----|
| chemistry-mix | 20 | plan_c | 25.0 | 45.0 | -21.75 | -43.55 | 4.33 | 2.64 | +1.69 |
| find-animal | 20 | plan_c | 25.0 | 50.0 | -22.55 | -49.20 | 3.27 | 1.60 | +1.67 |
| find-non-living-thing | 40 | plan_c | 0.0 | 0.0 | +28.48 | +18.90 | 28.48 | 18.90 | +9.58 |
| freeze | 20 | plan_c | 25.0 | 55.0 | -24.25 | -54.75 | 1.00 | 0.56 | +0.44 |
| grow-fruit | 20 | plan_c | 20.0 | 45.0 | -18.55 | -43.65 | 1.81 | 2.45 | -0.64 |
| identify-life-stages-1 | 20 | plan_c | 10.0 | 55.0 | -7.50 | -55.00 | 2.78 | 0.00 | +2.78 |
| identify-life-stages-2 | 20 | plan_c | 20.0 | 50.0 | -18.40 | -48.40 | 2.00 | 3.20 | -1.20 |
| inclined-plane-determine-angle | 20 | plan_c | 20.0 | 55.0 | -19.00 | -55.00 | 1.25 | 0.00 | +1.25 |
| lifespan-longest-lived | 25 | plan_c | 16.0 | 56.0 | -10.00 | -54.00 | 7.14 | 4.55 | +2.59 |
| lifespan-longest-lived-then-shortest-lived | 20 | plan_c | 10.0 | 45.0 | -4.20 | -45.00 | 6.44 | 0.00 | +6.44 |
| measure-melting-point-unknown-substance | 20 | plan_c | 25.0 | 55.0 | -24.25 | -54.30 | 1.00 | 1.56 | -0.56 |

### Excluded (19 tasks)

#### Group A: MVP Development Tasks (5 tasks, 100 episodes)

| Task | n | source | det_death% | int_death% | det_mean | int_mean | det_nd | int_nd | Δnd |
|------|---|--------|-----------|-----------|----------|----------|--------|--------|-----|
| boil | 20 | mvp | 20.0 | 50.0 | -19.70 | -49.75 | 0.38 | 0.50 | -0.12 |
| change-the-state-of-matter-of | 20 | mvp | 15.0 | 55.0 | -14.50 | -54.70 | 0.59 | 0.67 | -0.08 |
| chemistry-mix-paint-secondary-color | 20 | mvp | 10.0 | 45.0 | -5.50 | -41.00 | 5.00 | 7.27 | -2.27 |
| grow-plant | 20 | mvp | 0.0 | 0.0 | +0.50 | +0.50 | 0.50 | 0.50 | 0.00 |
| melt | 20 | mvp | 15.0 | 55.0 | -14.55 | -54.70 | 0.53 | 0.67 | -0.14 |

#### Group B: Redundant Family Variants (7 tasks)

| Task | n | source | Family rep (included) | det_death% | int_death% | det_mean | det_nd | int_nd | Δnd |
|------|---|--------|-----------------------|-----------|-----------|----------|--------|--------|-----|
| chemistry-mix-paint-tertiary-color | 5 | prescreening | chemistry-mix | 20.0 | 40.0 | -17.40 | 3.25 | 4.33 | -1.08 |
| find-living-thing | 5 | prescreening | find-animal | 20.0 | 60.0 | -16.60 | 4.25 | 4.00 | +0.25 |
| find-plant | 5 | prescreening | find-animal | 0.0 | 60.0 | +3.20 | 3.20 | 4.00 | -0.80 |
| inclined-plane-friction-named-surfaces | 5 | prescreening | inclined-plane-determine-angle | 20.0 | 60.0 | -20.00 | 0.00 | 0.00 | 0.00 |
| inclined-plane-friction-unnamed-surfaces | 5 | prescreening | inclined-plane-determine-angle | 0.0 | 60.0 | 0.00 | 0.00 | 0.00 | 0.00 |
| lifespan-shortest-lived | 5 | prescreening | lifespan-longest-lived | 40.0 | 60.0 | -40.00 | 0.00 | 0.00 | 0.00 |
| measure-melting-point-known-substance | 5 | prescreening | measure-melting-point-unknown | 0.0 | 60.0 | +1.20 | 1.20 | 3.00 | -1.80 |

#### Group C: Agent-Incompetent Task Families (7 tasks)

| Task | n | source | det_death% | int_death% | det_mean | det_nd | int_nd | Δnd |
|------|---|--------|-----------|-----------|----------|--------|--------|-----|
| mendelian-genetics-known-plant | 5 | prescreening | 20.0 | 60.0 | -20.00 | 0.00 | 0.00 | 0.00 |
| mendelian-genetics-unknown-plant | 5 | prescreening | 40.0 | 60.0 | -40.00 | 0.00 | 0.00 | 0.00 |
| power-component | 5 | prescreening | 20.0 | 60.0 | -20.00 | 0.00 | 0.00 | 0.00 |
| power-component-renewable-vs-nonrenewable-energy | 5 | prescreening | 0.0 | 60.0 | 0.00 | 0.00 | 0.00 | 0.00 |
| test-conductivity | 5 | prescreening | 20.0 | 60.0 | -20.00 | 0.00 | 0.00 | 0.00 |
| test-conductivity-of-unknown-substances | 5 | prescreening | 20.0 | 60.0 | -20.00 | 0.00 | 0.00 | 0.00 |
| use-thermometer | 5 | prescreening | 20.0 | 60.0 | -19.40 | 0.75 | 1.50 | -0.75 |

## 2. Statistical Comparison

### Best-available data (plan_c / mvp 20-ep + prescreening 5-ep)

| Metric | Included (11) | Excluded (19) |
|--------|--------------|---------------|
| n_episodes per task | 20-40 | 5-20 |
| Mean int_death_rate | 46.5% | 53.9% |
| Mean det_death_rate | 17.8% | 15.8% |
| Mean ΔDR (int - det) | +28.7 pp | +38.2 pp |
| Tasks with ΔDR > 0 | 10/11 (91%) | 18/19 (95%) |
| Tasks with ΔDR ≥ 20 pp | 10/11 (91%) | 18/19 (95%) |
| Zero-death tasks | 1 (find-non-living) | 1 (grow-plant) |
| Tasks with Δnd = 0 | 0/11 (0%) | 10/19 (53%) |
| Non-death routing signal (Δnd != 0) | 11/11 | 9/19 |

**Caveat**: Sample sizes differ. The 5-episode prescreening estimates are noisy (e.g., chemistry-mix: det_death = 0% at n=5 but 25% at n=20). The death-rate comparison should be interpreted with this variance in mind.

## 3. Key Distinctions Between Included and Excluded Tasks

1. **Non-death routing signal**: The primary discriminator. All 11 included tasks have Δnd != 0 in the 20-episode evaluation. 10/19 excluded tasks have Δnd = 0, offering no routing-relevant information beyond death avoidance.

2. **Agent incompetence (Group C)**: 6/7 Group C tasks score exactly 0.0 in non-death episodes under both strategies. use-thermometer is the exception (det_nd = 0.75, int_nd = 1.50), but scores remain near zero.

3. **Taxonomic redundancy (Group B)**: 7 tasks are variants of included family representatives. Including them would inflate sample size with correlated observations.

4. **Development contamination (Group A)**: 5 tasks used for pipeline development. Standard ML practice to exclude.

5. **Death rates are NOT the primary discriminator**: Included tasks have comparable or even lower death asymmetry (+28.7 pp ΔDR) compared to excluded tasks (+38.2 pp). The exclusion is driven by information content for routing research, not task difficulty.

## 4. Exclusion Criteria Assessment

Three criteria, independently justified:

**Criterion 1: MVP development data (5 tasks)** -- boil, melt, change-the-state-of-matter-of, chemistry-mix-paint-secondary-color, grow-plant were used to build and debug the experimental pipeline. Excluding them prevents circular evaluation.

**Criterion 2: Taxonomic deduplication (7 tasks)** -- One representative per ScienceWorld family prevents within-family correlation from inflating the effective sample size.

**Criterion 3: Agent-floor tasks (7 tasks)** -- Four families (mendelian-genetics, power-component, test-conductivity, use-thermometer) where Qwen2.5-7B achieves near-zero task progress in non-death episodes under both strategies. 6/7 have det_nd = int_nd = 0.0. These reflect backbone capability limitations, not routing methodology.

**Selection bias check**: The included set retains tasks that work against a pure death-dominance narrative:
- find-non-living-thing: zero deaths under both strategies, det_nd = 28.48 (genuine non-death routing signal)
- grow-fruit (Δnd = -0.64), identify-life-stages-2 (Δnd = -1.20), measure-melting-point-unknown (Δnd = -0.56): internal outperforms deterministic in non-death episodes

## 5. Paper Revision Suggestions

### Current wording (experiments.tex, line 3):
> "the 19 excluded types show no routing signal (both strategies time out)"

**Problem**: Many excluded tasks do NOT have "both strategies time out." find-plant has det scores [0, 8, 8, 0, 0]; identify-life-stages-1 has det score 25 in one episode. The parenthetical is inaccurate.

**Suggested revision**:
> "the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7); an anti-cherry-picking analysis confirms death dominance in 18 of these 19 types (Appendix~\ref{app:excluded-tasks})"

### Current wording (main.tex, line 71):
> "types where both strategies time out on all seed variations are excluded"

**Suggested revision**:
> "types are excluded when they were used for pipeline development, are taxonomically redundant with a retained family representative, or exhibit near-zero task progress under both strategies (agent capability floor)"

### Current wording (main.tex, line 102, anti-cherry-picking paragraph):
> "The deterministic-strategy death rate is comparable between included (17.8%) and excluded (14.9%) task types; prescreening does not select for death-prone tasks."

**Suggested revision** (stronger, using death asymmetry not just det death rate):
> "All 19 excluded task types except grow-plant (an intrinsically death-free task) exhibit death-asymmetric patterns, with a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. Exclusion is driven by absence of non-death routing signal ($\Delta_\text{nd} = 0$ for 53\% of excluded tasks) and standard deduplication practices, not by the presence or absence of death dominance."

### New appendix subsection:
Add a dedicated "Excluded Tasks Death Dominance" subsection within Appendix B (Per-Task Decomposition) or as a new Appendix C, containing Table~\ref{tab:excluded-death} and the analysis paragraph from Section 0.

## 6. Raw Data Sources

- Included tasks: `results/prescreening/{task}/summary.json` (5 episodes) and plan_c evaluation (20 episodes)
- Group A (MVP): MVP development runs (20 episodes each)
- Groups B-C: `results/prescreening/{task}/summary.json` (5 episodes each)
- Prescreening log confirms 2 tasks skipped as "MVP-tested": boil, change-the-state-of-matter-of
- Death defined as score <= -100
