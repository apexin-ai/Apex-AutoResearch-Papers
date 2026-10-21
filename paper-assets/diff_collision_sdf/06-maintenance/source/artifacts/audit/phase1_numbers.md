# Phase 1 Number Extraction — Data Authenticity Audit

Generated: 2026-05-29
Base directory: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/

---

## abstract.tex

L2 | 99 | "over 99\% of safe episodes in Pi0-family models are action-collapse artifacts" | result
L2 | 99% | "over 99\% of safe episodes" | result

---

## introduction.tex

L6 | 91.5 | "Pi0+A1 reports 91.5\% CAR" (figure caption) | result
L6 | 99.6 | "99.6\% of safe episodes have displacement ${<}\,0.1$\,mm" (figure caption) | result
L6 | 0.1 | "displacement ${<}\,0.1$\,mm" (figure caption) | hyperparam
L6 | 0 | "dfCAR drops to ${\approx}\,0$\%" (figure caption) | result
L6 | 73 | "all oracle variants underperform unrefined baselines (73--77\% vs.\ 82--83\%)" (figure caption) | result
L6 | 77 | "all oracle variants underperform unrefined baselines (73--77\% vs.\ 82--83\%)" (figure caption) | result
L6 | 82 | "unrefined baselines (73--77\% vs.\ 82--83\%)" (figure caption) | result
L6 | 83 | "unrefined baselines (73--77\% vs.\ 82--83\%)" (figure caption) | result
L6 | 26 | "collision-free demonstrations account for $+$26\,pp CAR" (figure caption) | result
L6 | 2.2 | "SDF supervision adds only $+$2.2\,pp" (figure caption) | result
L6 | 0.155 | "$p = 0.155$, n.s." (figure caption) | stat
L10 | 91.5 | "Our SDF-augmented Pi0 reaches 91.5\% CAR across 800 episodes" | result
L10 | 800 | "91.5\% CAR across 800 episodes" | dataset
L11 | 732 | "Of the 732 collision-free episodes" | dataset
L11 | 99.6 | "99.6\% exhibit displacement below 0.1\,mm" | result
L11 | 0.1 | "displacement below 0.1\,mm" | hyperparam
L11 | 0 | "TSR is 0\% across all 800 episodes" | result
L11 | 800 | "TSR is 0\% across all 800 episodes" | dataset
L14 | 100 | "spanning 100+ experiments" | dataset
L14 | 6000 | "6000+ evaluation episodes" | dataset
L16 | 91.5 | "dfCAR collapses Pi0+A1 from 91.5\% to ${\approx}$\,0\%" | result
L16 | 0 | "Pi0+A1 from 91.5\% to ${\approx}$\,0\%" | result
L16 | 3 | "3/732 safe episodes survive" | result
L16 | 732 | "3/732 safe episodes survive" | dataset
L16 | 71.5 | "Pi0.5 validates the metric: TSR\,=\,71.5\%" | result
L16 | 28.5 | "CAR\,=\,28.5\%" | result
L16 | 288 | "every safe episode above 288\,mm displacement" | result
L18 | 73.1 | "Three ground-truth oracle variants all achieve lower CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%)" | result
L18 | 76.9 | "73.1--76.9\% vs.\ 82--83\%" | result
L18 | 82 | "vs.\ 82--83\%" | result
L18 | 83 | "vs.\ 82--83\%" | result
L20 | 26 | "LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\sim}$26 points" | result
L20 | 0.155 | "$p \geq 0.155$ for $\lambda \in \{0.01, 0.1\}$" | stat
L20 | 0.01 | "$\lambda \in \{0.01, 0.1\}$" | hyperparam
L20 | 0.1 | "$\lambda \in \{0.01, 0.1\}$" | hyperparam
L22 | 100 | "diagnose action collapse across 100+ experiments" | dataset
L22 | 99 | "revealing that $>$99\% of Pi0 safe episodes are inaction artifacts" | result
L22 | 26 | "collision-free demonstration data accounts for nearly all CAR gains (${\sim}$26\,pp)" | result
L22 | 0.155 | "no statistically significant SDF benefit ($p \geq 0.155$)" | stat
L27 | 91.5 | "Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\%" (figure caption) | result
L27 | 0 | "drops to ${\approx}$\,0\%" (figure caption) | result
L27 | 288 | "Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes" (figure caption) | result

---

## method.tex

L5 | 2.5 | "Pi0 (${\sim}$2.5B)" | other
L5 | 50 | "Each uses 50 episodes per task (200 total)" | dataset
L5 | 200 | "50 episodes per task (200 total)" | dataset
L5 | 3 | "Pi0.5 multi-seed runs use 3 seeds (600 episodes)" | dataset
L5 | 600 | "3 seeds (600 episodes)" | dataset
L5 | 7 | "fixed evaluation seed (seed\,=\,7)" | hyperparam
L15 | 2.5 | "Pi0 Full-FT ... ${\sim}$2.5B" (table) | other
L18 | 33.5 | "Pi0 LoRA ... ${\sim}$33.5M" (table) | other
L19 | 658 | "Pi0+A1 (SDF aux) ... ${\sim}$658K" (table) | other
L20 | 34.2 | "Pi0+A3 (learned SDF) ... ${\sim}$34.2M" (table) | other
L21 | 0 | "Pi0.5 (pre-trained) ... 0" (table, trainable params) | other
L22 | 33.5 | "Pi0.5 LoRA ... ${\sim}$33.5M" (table) | other
L23 | 0.005 | "Pi0.5+A1 ... $\lambda \in \{0.005, 0.01, 0.1\}$" (table) | hyperparam
L23 | 0.01 | "$\lambda \in \{0.005, 0.01, 0.1\}$" (table) | hyperparam
L23 | 0.1 | "$\lambda \in \{0.005, 0.01, 0.1\}$" (table) | hyperparam
L23 | 34.2 | "Pi0.5+A1 ... ${\sim}$34.2M" (table) | other
L30 | 0.1 | "$\tau_d = 0.1$\,mm" | hyperparam
L34 | 1 | "collapsed episodes below 1\,$\mu$m" | result
L34 | 200 | "active episodes above 200\,mm" | result
L34 | 2 | "any $\tau_d \in [2, 200]$\,mm yields identical results" | result
L34 | 200 | "any $\tau_d \in [2, 200]$\,mm yields identical results" | result
L38 | 0.005 | "$\lambda \in \{0.005, 0.01, 0.1\}$" | hyperparam
L38 | 0.01 | "$\lambda \in \{0.005, 0.01, 0.1\}$" | hyperparam
L38 | 0.1 | "$\lambda \in \{0.005, 0.01, 0.1\}$" | hyperparam
L42 | 0.05 | "clamped to $[-\delta, \delta]$ ($\delta = 0.05$\,m)" | hyperparam
L42 | 0.1 | "Eikonal regularization (weight 0.1)" | hyperparam
L42 | 64 | "64 query points per step" | hyperparam
L42 | 64 | "precomputed $64^3$ voxel grid" | hyperparam
L42 | 1024 | "2-layer MLP (1024 $\to$ 256 $\to$ 3)" | hyperparam
L42 | 256 | "2-layer MLP (1024 $\to$ 256 $\to$ 3)" | hyperparam
L42 | 3 | "2-layer MLP (1024 $\to$ 256 $\to$ 3)" | hyperparam
L44 | 0 | "Phase~1 (steps 0--5K)" | hyperparam
L44 | 5000 | "Phase~1 (steps 0--5K)" | hyperparam
L44 | 5000 | "Phase~2 (steps 5K--30K)" | hyperparam
L44 | 30000 | "Phase~2 (steps 5K--30K)" | hyperparam
L44 | 100 | "100-step gradient warmup ramp" | hyperparam
L46 | 0 | "TSR\,=\,0\%" (Pi0+A1 action collapse) | result

---

## related_work.tex

*(No quantitative result numbers, dataset sizes, or statistical values appear in this section — only citations and qualitative descriptions.)*

---

## claim1.tex

L3 | 99 | "over 99\% of collision-free episodes are action-collapse artifacts" | result
L3 | 0 | "Applying dfCAR collapses all three to ${\approx}$\,0\%" | result
L3 | 91.5 | "Pi0+A1 achieves the highest raw CAR (91.5\%)" | result
L3 | 200 | "every safe episode exceeds 200\,mm displacement" | result
L3 | 28.5 | "dfCAR equals raw CAR (28.5\%)" | result
L7 | 0.1 | "displacement $< \tau_d = 0.1$\,mm" (table caption) | hyperparam
L7 | 3 | "only 3/732 safe episodes exceed the threshold" (table caption) | result
L7 | 732 | "only 3/732 safe episodes exceed the threshold" (table caption) | dataset
L15 | 200 | "Pi0 Full-FT  & 200" (table, episodes) | dataset
L15 | 83.0 | "Pi0 Full-FT ... CAR = 83.0" (table) | result
L15 | 0.5 | "Pi0 Full-FT ... TSR = 0.5" (table) | result
L15 | 99.4 | "Pi0 Full-FT ... Collapsed = 99.4" (table) | result
L15 | 0 | "Pi0 Full-FT ... dfCAR = $\approx$\,0" (table) | result
L16 | 200 | "Pi0 LoRA     & 200" (table, episodes) | dataset
L16 | 82.0 | "Pi0 LoRA ... CAR = 82.0" (table) | result
L16 | 0.0 | "Pi0 LoRA ... TSR = 0.0" (table) | result
L16 | 99 | "Pi0 LoRA ... Collapsed = ${\sim}$99" (table) | result
L16 | 0 | "Pi0 LoRA ... dfCAR = $\approx$\,0" (table) | result
L17 | 800 | "Pi0+A1 (SDF) & 800" (table, episodes) | dataset
L17 | 91.5 | "Pi0+A1 ... CAR = 91.5" (table) | result
L17 | 0.0 | "Pi0+A1 ... TSR = 0.0" (table) | result
L17 | 99.6 | "Pi0+A1 ... Collapsed = 99.6" (table) | result
L17 | 0 | "Pi0+A1 ... dfCAR = $\approx$\,0" (table) | result
L19 | 200 | "Pi0.5  & 200" (table, episodes) | dataset
L19 | 28.5 | "Pi0.5 ... CAR = 28.5" (table) | result
L19 | 71.5 | "Pi0.5 ... TSR = 71.5" (table) | result
L19 | 0.0 | "Pi0.5 ... Collapsed = 0.0" (table) | result
L19 | 28.5 | "Pi0.5 ... dfCAR = 28.5" (table) | result
L27 | 82 | "Pi0-family models show 82--91\,pp gaps" (figure caption) | result
L27 | 91 | "Pi0-family models show 82--91\,pp gaps" (figure caption) | result
L30 | 82 | "Pi0-family models show 82--91\,pp gaps between reported CAR and dfCAR" | result
L30 | 91 | "82--91\,pp gaps" | result
L32 | 0.1 | "The 0.1\,mm threshold is physically motivated" | hyperparam
L32 | 1 | "typical manipulation actions produce 1--10\,mm of EE displacement per step" | other
L32 | 10 | "1--10\,mm of EE displacement per step" | other
L32 | 300 | "sub-0.1\,mm cumulative displacement over an entire episode (up to 300 steps)" | dataset
L32 | 1 | "collapsed episodes cluster below 1\,$\mu$m" | result
L32 | 200 | "active episodes exceed 200\,mm" | result
L32 | 2 | "any threshold in the range $\tau_d \in [2, 200]$\,mm yields identical dfCAR values" | result
L32 | 200 | "any threshold in the range $\tau_d \in [2, 200]$\,mm yields identical dfCAR values" | result

---

## claim2.tex

L3 | 76.9 | "the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%)" | result
L3 | 5.1 | "falls 5.1 points below LoRA" | result
L3 | 82.0 | "below LoRA (82.0\%)" | result
L15 | 82.0 | "LoRA baseline (no refine) & 82.0" (table) | result
L15 | 99.4 | "LoRA baseline ... Collapsed = 99.4" (table) | result
L16 | 83.0 | "Full-FT baseline (no refine) & 83.0" (table) | result
L18 | 75.0 | "Oracle-adaptive ... CAR = 75.0" (table) | result
L18 | 98.3 | "Oracle-adaptive ... Collapsed = 98.3" (table) | result
L18 | 14.2 | "Oracle-adaptive ... Refines/ep = 14.2" (table) | result
L19 | 73.1 | "Oracle-fixed ... CAR = 73.1" (table) | result
L19 | 98.3 | "Oracle-fixed ... Collapsed = 98.3" (table) | result
L19 | 14.8 | "Oracle-fixed ... Refines/ep = 14.8" (table) | result
L19 | 0.005 | "Oracle-fixed (GT, $\alpha{=}0.005$)" (table) | hyperparam
L20 | 76.9 | "Oracle-feature ... CAR = 76.9" (table) | result
L20 | 96.7 | "Oracle-feature ... Collapsed = 96.7" (table) | result
L20 | 241.7 | "Oracle-feature ... Refines/ep = 241.7" (table) | result
L22 | 77.1 | "A3 learned SDF & 77.1" (table) | result
L22 | 0.0 | "A3 learned SDF ... Refines/ep = 0.0" (table) | result
L25 | 57.0 | "Pi0.5 LoRA (no refine) & 57.0" (table) | result
L25 | 0.0 | "Pi0.5 LoRA ... Collapsed = 0.0" (table) | result
L26 | 51.9 | "Pi0.5 Oracle-adaptive & 51.9" (table) | result
L26 | 0.0 | "Pi0.5 Oracle-adaptive ... Collapsed = 0.0" (table) | result
L26 | 14.2 | "Pi0.5 Oracle-adaptive ... Refines/ep = 14.2" (table) | result
L31 | 9 | "On the one task where the EE is the primary collision body, oracle refinement helps (+9 points)" | result
L31 | 0 | "The A3 learned SDF never triggers refinement (0 steps per episode)" | result
L37 | 96 | "On \texttt{orange\_juice} (LoRA CAR\,=\,96\%)" | result
L37 | 82.5 | "Oracle-adaptive reduces CAR to 82.5\%" | result
L37 | 57.0 | "we apply Oracle-adaptive to Pi0.5 LoRA (0\% action-collapse, CAR\,=\,57.0\%)" | result
L37 | 0 | "0\% action-collapse" | result
L37 | 51.9 | "CAR drops to 51.9\% ($-$5.1\,pp)" | result
L37 | 5.1 | "$-$5.1\,pp, confirming that the counterproductive effect is structural" | result

---

## claim3.tex

L3 | 26 | "LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points" | result
L3 | 20 | "20$\times$ range of loss weights" | other
L3 | 0.005 | "$\lambda \in \{0.005, 0.01, 0.1\}$" | hyperparam
L3 | 0.01 | "$\lambda \in \{0.005, 0.01, 0.1\}$" | hyperparam
L3 | 0.1 | "$\lambda \in \{0.005, 0.01, 0.1\}$" | hyperparam
L3 | 30000 | "all evaluated at the 30K-step checkpoint" | hyperparam
L7 | 0.05 | "all fine-tuned models exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m" (table caption note) | result
L7 | 0.37 | "displacement $>$\,0.37\,m" (table caption note) | result
L7 | 0.05 | "p > 0.05 for $\lambda \in \{0.01, 0.1\}$" (table caption) | stat
L7 | 0.01 | "$\lambda \in \{0.01, 0.1\}$" (table caption) | hyperparam
L7 | 0.1 | "$\lambda \in \{0.01, 0.1\}$" (table caption) | hyperparam
L15 | 1 | "Pi0.5 baseline & 1" (table, seeds) | dataset
L15 | 71.5 | "Pi0.5 baseline ... TSR = 71.5" (table) | result
L15 | 28.5 | "Pi0.5 baseline ... CAR = 28.5" (table) | result
L15 | 0.367 | "Pi0.5 baseline ... EE Disp = 0.367" (table) | result
L17 | 3 | "LoRA-only (no SDF) & 3" (table, seeds) | dataset
L17 | 49.7 | "LoRA-only ... TSR = 49.7\,$\pm$\,3.2" (table) | result
L17 | 3.2 | "TSR = 49.7\,$\pm$\,3.2" (table) | stat
L17 | 54.83 | "LoRA-only ... CAR = 54.83\,$\pm$\,2.25" (table) | result
L17 | 2.25 | "CAR = 54.83\,$\pm$\,2.25" (table) | stat
L17 | 0.391 | "LoRA-only ... EE Disp = 0.391" (table) | result
L18 | 3 | "LoRA+SDF $\lambda{=}0.005$ & 3" (table, seeds) | dataset
L18 | 0.005 | "$\lambda{=}0.005$" (table) | hyperparam
L18 | 54.0 | "LoRA+SDF λ=0.005 ... TSR = 54.0\,$\pm$\,3.0" (table) | result
L18 | 3.0 | "TSR = 54.0\,$\pm$\,3.0" (table) | stat
L18 | 54.5 | "λ=0.005 ... CAR = 54.5\,$\pm$\,2.29" (table) | result
L18 | 2.29 | "CAR = 54.5\,$\pm$\,2.29" (table) | stat
L18 | 0.387 | "λ=0.005 ... EE Disp = 0.387" (table) | result
L19 | 3 | "LoRA+SDF $\lambda{=}0.01$ & 3" (table, seeds) | dataset
L19 | 0.01 | "$\lambda{=}0.01$" (table) | hyperparam
L19 | 53.8 | "λ=0.01 ... TSR = 53.8\,$\pm$\,1.5" (table) | result
L19 | 1.5 | "TSR = 53.8\,$\pm$\,1.5" (table) | stat
L19 | 56.33 | "λ=0.01 ... CAR = 56.33\,$\pm$\,1.61" (table) | result
L19 | 1.61 | "CAR = 56.33\,$\pm$\,1.61" (table) | stat
L19 | 0.389 | "λ=0.01 ... EE Disp = 0.389" (table) | result
L20 | 3 | "LoRA+SDF $\lambda{=}0.1$ & 3" (table, seeds) | dataset
L20 | 0.1 | "$\lambda{=}0.1$" (table) | hyperparam
L20 | 50.2 | "λ=0.1 ... TSR = 50.2\,$\pm$\,3.9" (table) | result
L20 | 3.9 | "TSR = 50.2\,$\pm$\,3.9" (table) | stat
L20 | 57.00 | "λ=0.1 ... CAR = 57.00\,$\pm$\,2.18" (table) | result
L20 | 2.18 | "CAR = 57.00\,$\pm$\,2.18" (table) | stat
L20 | 0.394 | "λ=0.1 ... EE Disp = 0.394" (table) | result
L26 | 26 | "collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points" | result
L26 | 28.5 | "28.5\% $\to$ 54.83\%" | result
L26 | 54.83 | "28.5\% $\to$ 54.83\%" | result
L26 | 0.37 | "displacement above 0.37\,m" | result
L26 | 54.83 | "LoRA-only CAR (54.83\%) is statistically indistinguishable from all SDF conditions" | result
L26 | 0.1 | "including $\lambda = 0.1$" | hyperparam
L26 | 57.00 | "57.00\%, $p = 0.155$" | result
L26 | 0.155 | "$p = 0.155$" | stat
L26 | 0 | "A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%" | hyperparam
L26 | 5000 | "($\lambda = 0$ after step 5K)" | hyperparam
L26 | 57.5 | "yields CAR\,=\,57.5\%" | result
L26 | 18000 | "At the 18K checkpoint (13K steps of Phase~2 training, single seed s2)" | hyperparam
L26 | 13000 | "13K steps of Phase~2 training" | hyperparam
L29 | 18 | "Fine-tuning degrades TSR by ${\sim}$18--22\,pp" | result
L29 | 22 | "TSR by ${\sim}$18--22\,pp" | result
L29 | 71.5 | "71.5\% $\to$ 49.7--54.0\%" | result
L29 | 49.7 | "71.5\% $\to$ 49.7--54.0\%" | result
L29 | 54.0 | "71.5\% $\to$ 49.7--54.0\%" | result
L29 | 0.37 | "all models retain $>$\,0.37\,m displacement" | result
L29 | 0.39 | "The SSR/TSR ratio increases from 0.39 (baseline)" | result
L29 | 0.51 | "to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr})" | result
L29 | 0.60 | "0.51--0.60 (Appendix~\ref{sec:appendix_ssr})" | result
L32 | 20 | "Increasing $\lambda$ by 20$\times$ to 0.1" | other
L32 | 0.1 | "20$\times$ to 0.1" | hyperparam
L32 | 57.00 | "CAR\,=\,57.00\%\,$\pm$\,2.18 (3 seeds: 58.0\%, 58.5\%, 54.5\%)" | result
L32 | 2.18 | "$\pm$\,2.18" | stat
L32 | 58.0 | "3 seeds: 58.0\%, 58.5\%, 54.5\%" | result
L32 | 58.5 | "3 seeds: 58.0\%, 58.5\%, 54.5\%" | result
L32 | 54.5 | "3 seeds: 58.0\%, 58.5\%, 54.5\%" | result
L32 | 0.155 | "within the null distribution ($p = 0.155$" | stat
L32 | 0.071 | "One-tailed $p = 0.071$" (footnote) | stat
L35 | 0.005 | "Pooling LoRA-only and $\lambda = 0.005$ seeds as null (Null~B)" | hyperparam
L35 | 84 | "$\binom{9}{3} = 84$ permutations" | stat
L35 | 0.155 | "$p = 0.155$" | stat
L35 | 6 | "$\binom{6}{3} = 20$ permutations" | stat
L35 | 20 | "$\binom{6}{3} = 20$ permutations" | stat
L35 | 0.250 | "$p = 0.250$" | stat
L35 | 0.05 | "both yield non-significance at $\alpha = 0.05$" | stat
L38 | 3 | "With $n = 3$ seeds per group" | dataset
L38 | 2.3 | "$\sigma \approx 2.3$\,pp (LoRA cross-seed standard deviation)" | stat
L38 | 0.05 | "a two-sample $t$-test at $\alpha = 0.05$ (one-tailed)" | stat
L38 | 80 | "achieves 80\% power only for effects $\geq 5.6$\,pp" | stat
L38 | 5.6 | "effects $\geq 5.6$\,pp" | stat
L38 | 2.2 | "The observed effect of ${\sim}$2.2\,pp falls well below this minimum detectable effect (MDE)" | result
L41 | 1.0 | "SDF $\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.0, $+$2.5, $+$5.5\,pp)" | result
L41 | 2.5 | "$+$1.0, $+$2.5, $+$5.5\,pp" | result
L41 | 5.5 | "$+$1.0, $+$2.5, $+$5.5\,pp" | result
L41 | 0.9 | "lower cross-seed variance ($\sigma = 0.9$\,pp vs.\ 2.2\,pp for LoRA)" | stat
L41 | 2.2 | "$\sigma = 0.9$\,pp vs.\ 2.2\,pp for LoRA" | stat
L41 | 2.2 | "The observed effect (${\sim}$2.2\,pp) falls below the MDE (${\sim}$5.6\,pp)" | result
L41 | 5.6 | "MDE (${\sim}$5.6\,pp)" | stat
L41 | 3 | "cannot be resolved at $n = 3$" | dataset

---

## discussion.tex

L6 | 0 | "LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within the null band ($p > 0.05$)" (figure caption) | stat
L6 | 0.01 | "$\lambda \in \{0.01, 0.1\}$" (figure caption) | hyperparam
L6 | 0.1 | "$\lambda \in \{0.01, 0.1\}$" (figure caption) | hyperparam
L6 | 0.05 | "$p > 0.05$" (figure caption) | stat
L6 | 20 | "20$\times$ loss-weight range" (figure caption) | other
L10 | 5 | "reducing CAR by 5--10\,pp as the end-effector push rotates unmonitored links through obstacles" | result
L10 | 10 | "reducing CAR by 5--10\,pp" | result
L10 | 0.1 | "Even at $\lambda = 0.1$, CAR remains within the null distribution ($p = 0.155$)" | hyperparam
L10 | 0.155 | "$p = 0.155$" | stat
L14 | 3 | "Statistical power is limited by $n{=}3$ seeds per condition" | dataset
L14 | 5.6 | "MDE ${\approx}$ 5.6\,pp at 80\% power" | stat
L14 | 80 | "MDE ${\approx}$ 5.6\,pp at 80\% power" | stat
L14 | 2 | "a genuine 2--5\,pp effect remains consistent with our data" | result
L14 | 5 | "2--5\,pp effect remains consistent with our data" | result

---

## appendix.tex

### Appendix A: Complete Multi-Seed Results (sec:appendix_multiseed)

L4 | 30000 | "all fine-tuned conditions at the 30K checkpoint" | hyperparam
L4 | 7 | "evaluation seed\,=\,7" | hyperparam
L4 | 200 | "200 episodes each" | dataset
L8 | 30000 | "30K steps, evaluation seed\,=\,7 (200 episodes)" (table caption) | hyperparam
L8 | 7 | "evaluation seed\,=\,7" (table caption) | hyperparam
L8 | 200 | "(200 episodes)" (table caption) | dataset
L8 | 0.37 | "All episodes exhibit displacement $>$\,0.37\,m" (table caption) | result
L17 | 57.0 | "LoRA-only s0 CAR = 57.0" (table) | result
L17 | 46.0 | "LoRA-only s0 TSR = 46.0" (table) | result
L17 | 54.83 | "Mean CAR = 54.83$\pm$2.25" (table) | result
L17 | 2.25 | "$\pm$2.25" (table) | stat
L17 | 49.7 | "Mean TSR = 49.7$\pm$3.2" (table) | result
L17 | 3.2 | "$\pm$3.2" (table) | stat
L18 | 52.5 | "LoRA-only s1 CAR = 52.5" (table) | result
L18 | 51.5 | "LoRA-only s1 TSR = 51.5" (table) | result
L19 | 55.0 | "LoRA-only s2 CAR = 55.0" (table) | result
L19 | 51.5 | "LoRA-only s2 TSR = 51.5" (table) | result
L22 | 57.0 | "SDF λ=0.005 s0 CAR = 57.0" (table) | result
L22 | 55.5 | "SDF λ=0.005 s0 TSR = 55.5" (table) | result
L22 | 54.5 | "Mean CAR = 54.5$\pm$2.29" (table) | result
L22 | 2.29 | "$\pm$2.29" (table) | stat
L22 | 54.0 | "Mean TSR = 54.0$\pm$3.0" (table) | result
L22 | 3.0 | "$\pm$3.0" (table) | stat
L23 | 54.0 | "SDF λ=0.005 s1 CAR = 54.0" (table) | result
L23 | 50.5 | "SDF λ=0.005 s1 TSR = 50.5" (table) | result
L24 | 52.5 | "SDF λ=0.005 s2 CAR = 52.5" (table) | result
L24 | 56.0 | "SDF λ=0.005 s2 TSR = 56.0" (table) | result
L27 | 57.0 | "SDF λ=0.01 s0 CAR = 57.0" (table) | result
L27 | 52.5 | "SDF λ=0.01 s0 TSR = 52.5" (table) | result
L27 | 56.33 | "Mean CAR = 56.33$\pm$1.61" (table) | result
L27 | 1.61 | "$\pm$1.61" (table) | stat
L27 | 53.8 | "Mean TSR = 53.8$\pm$1.5" (table) | result
L27 | 1.5 | "$\pm$1.5" (table) | stat
L28 | 57.5 | "SDF λ=0.01 s1 CAR = 57.5" (table) | result
L28 | 55.5 | "SDF λ=0.01 s1 TSR = 55.5" (table) | result
L29 | 54.5 | "SDF λ=0.01 s2 CAR = 54.5" (table) | result
L29 | 53.5 | "SDF λ=0.01 s2 TSR = 53.5" (table) | result
L32 | 58.0 | "SDF λ=0.1 s0 CAR = 58.0" (table) | result
L32 | 47.0 | "SDF λ=0.1 s0 TSR = 47.0" (table) | result
L32 | 57.00 | "Mean CAR = 57.00$\pm$2.18" (table) | result
L32 | 2.18 | "$\pm$2.18" (table) | stat
L32 | 50.2 | "Mean TSR = 50.2$\pm$3.9" (table) | result
L32 | 3.9 | "$\pm$3.9" (table) | stat
L33 | 58.5 | "SDF λ=0.1 s1 CAR = 58.5" (table) | result
L33 | 49.0 | "SDF λ=0.1 s1 TSR = 49.0" (table) | result
L34 | 54.5 | "SDF λ=0.1 s2 CAR = 54.5" (table) | result
L34 | 54.5 | "SDF λ=0.1 s2 TSR = 54.5" (table) | result

### Appendix B: Displacement Distribution (sec:appendix_displacement)

L45 | 1 | "Pi0-family models (blue) cluster below 1\,$\mu$m" (figure caption) | result
L45 | 200 | "Pi0.5 episodes (orange) exceed 200\,mm" (figure caption) | result
L45 | 2 | "any value in $[2, 200]$\,mm" (figure caption) | result
L45 | 200 | "$[2, 200]$\,mm" (figure caption) | result

### Appendix C: Displacement Threshold Sensitivity Analysis (sec:appendix_threshold)

L52 | 4 | "we evaluate the action-collapse rate across four orders of magnitude" | other
L62 | 0.001 | "$\tau_d$ = 0.001 mm (1\,$\mu$m)" (table) | hyperparam
L62 | 73.9 | "A1-LoRA collapse rate at τ=0.001mm = 73.9" (table) | result
L62 | 0.0 | "Pi0.5 Baseline collapse rate = 0.0" (table) | result
L62 | 0.0 | "Pi0.5+A1 collapse rate = 0.0" (table) | result
L63 | 0.1 | "$\tau_d$ = 0.1 mm" (table) | hyperparam
L63 | 99.6 | "A1-LoRA collapse rate at τ=0.1mm = 99.6" (table) | result
L63 | 0.0 | "Pi0.5 Baseline collapse rate = 0.0" (table) | result
L63 | 0.0 | "Pi0.5+A1 collapse rate = 0.0" (table) | result
L64 | 1.0 | "$\tau_d$ = 1.0 mm" (table) | hyperparam
L64 | 100.0 | "A1-LoRA collapse rate at τ=1.0mm = 100.0" (table) | result
L64 | 0.0 | "Pi0.5 Baseline collapse rate = 0.0" (table) | result
L64 | 0.0 | "Pi0.5+A1 collapse rate = 0.0" (table) | result
L65 | 10 | "$\tau_d$ = 10 mm" (table) | hyperparam
L65 | 100.0 | "A1-LoRA collapse rate at τ=10mm = 100.0" (table) | result
L65 | 0.0 | "Pi0.5 Baseline collapse rate = 0.0" (table) | result
L65 | 0.0 | "Pi0.5+A1 collapse rate = 0.0" (table) | result
L70 | 0.1 | "$\tau_d = 0.1$\,mm represents a conservative threshold" | hyperparam
L70 | 1 | "displacement below this value is physically negligible...typical action magnitudes are 1--10\,mm" | other
L70 | 10 | "1--10\,mm per step" | other
L70 | 1 | "Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as action-collapsed" | hyperparam
L70 | 73.9 | "73.9\% of A1-LoRA safe episodes are classified as action-collapsed" | result
L72 | 2 | "All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm" | result
L72 | 200 | "$\tau_d \in [2, 200]$\,mm" | result
L72 | 300 | "At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold" | result
L72 | 0 | "0--2 episodes per seed" | result
L72 | 2 | "0--2 episodes per seed fall below threshold" | result
L72 | 200 | "displacement 200--300\,mm" | result
L72 | 300 | "displacement 200--300\,mm" | result
L72 | 0.5 | "causing $\leq$0.5\,pp deviation" | result

### Appendix C continued: Table tab:dfcar_threshold

L86 | 57.0 | "LoRA s0 @ τ=2mm dfCAR = 57.0" (table) | result
L86 | 57.0 | "LoRA s0 @ τ=5,10,20,50,100,200mm dfCAR = 57.0" (table, repeated) | result
L87 | 52.5 | "LoRA s1 dfCAR = 52.5 across τ=[2..200]mm" (table) | result
L88 | 57.0 | "SDF λ=0.005 s0 dfCAR = 57.0 across τ=[2..200]mm" (table) | result
L88 | 57.1 | "SDF λ=0.005 s0 @ τ=300mm dfCAR = 57.1" (table) | result
L89 | 54.0 | "SDF λ=0.005 s1 dfCAR = 54.0 across all τ" (table) | result
L90 | 52.5 | "SDF λ=0.005 s2 dfCAR = 52.5 across τ=[2..200]mm" (table) | result
L90 | 52.3 | "SDF λ=0.005 s2 @ τ=300mm dfCAR = 52.3" (table) | result
L91 | 57.0 | "SDF λ=0.01 s0 dfCAR = 57.0 across all τ" (table) | result
L92 | 57.5 | "SDF λ=0.01 s1 dfCAR = 57.5 across τ=[2..200]mm" (table) | result
L92 | 57.1 | "SDF λ=0.01 s1 @ τ=300mm dfCAR = 57.1" (table) | result
L93 | 54.5 | "SDF λ=0.01 s2 dfCAR = 54.5 across τ=[2..200]mm" (table) | result
L93 | 54.0 | "SDF λ=0.01 s2 @ τ=300mm dfCAR = 54.0" (table) | result

### Appendix D: Per-Task TSR Breakdown (sec:appendix_tsr_pertask)

L105 | 71.5 | "Baseline reports... aggregate TSR\,=\,71.5\%" (table caption) | result
L114 | 74.0 | "Orange Juice: Pi0.5 Base = 74.0" (table) | result
L114 | 30.0 | "Orange Juice: LoRA-only = 30.0" (table) | result
L114 | 33.3 | "Orange Juice: SDF λ=0.005 = 33.3" (table) | result
L114 | 24.7 | "Orange Juice: SDF λ=0.01 = 24.7" (table) | result
L115 | 80.0 | "Choco. Pudding: Pi0.5 Base = 80.0" (table) | result
L115 | 70.7 | "Choco. Pudding: LoRA-only = 70.7" (table) | result
L115 | 78.0 | "Choco. Pudding: SDF λ=0.005 = 78.0" (table) | result
L115 | 76.7 | "Choco. Pudding: SDF λ=0.01 = 76.7" (table) | result
L116 | 66.0 | "Milk: Pi0.5 Base = 66.0" (table) | result
L116 | 44.7 | "Milk: LoRA-only = 44.7" (table) | result
L116 | 35.3 | "Milk: SDF λ=0.005 = 35.3" (table) | result
L116 | 48.7 | "Milk: SDF λ=0.01 = 48.7" (table) | result
L117 | 66.0 | "BBQ Sauce: Pi0.5 Base = 66.0" (table) | result
L117 | 60.7 | "BBQ Sauce: LoRA-only = 60.7" (table) | result
L117 | 69.3 | "BBQ Sauce: SDF λ=0.005 = 69.3" (table) | result
L117 | 65.3 | "BBQ Sauce: SDF λ=0.01 = 65.3" (table) | result
L119 | 71.5 | "Mean: Pi0.5 Base = 71.5" (table) | result
L119 | 51.5 | "Mean: LoRA-only = 51.5" (table) | result
L119 | 54.0 | "Mean: SDF λ=0.005 = 54.0" (table) | result
L119 | 53.8 | "Mean: SDF λ=0.01 = 53.8" (table) | result

### Appendix E: Per-Task CAR Breakdown (sec:appendix_pertask_car)

L138 | 68 | "LoRA s0 OJ CAR = 68" (table) | result
L138 | 74 | "LoRA s0 CP CAR = 74" (table) | result
L138 | 66 | "LoRA s0 Milk CAR = 66" (table) | result
L138 | 20 | "LoRA s0 BBQ CAR = 20" (table) | result
L138 | 57.0 | "LoRA s0 Agg. = 57.0" (table) | result
L139 | 54 | "LoRA s1 OJ CAR = 54" (table) | result
L139 | 68 | "LoRA s1 CP CAR = 68" (table) | result
L139 | 72 | "LoRA s1 Milk CAR = 72" (table) | result
L139 | 16 | "LoRA s1 BBQ CAR = 16" (table) | result
L139 | 52.5 | "LoRA s1 Agg. = 52.5" (table) | result
L140 | 56 | "LoRA s2 OJ CAR = 56" (table) | result
L140 | 76 | "LoRA s2 CP CAR = 76" (table) | result
L140 | 62 | "LoRA s2 Milk CAR = 62" (table) | result
L140 | 26 | "LoRA s2 BBQ CAR = 26" (table) | result
L140 | 55.0 | "LoRA s2 Agg. = 55.0" (table) | result
L141 | 54.0 | "SDF λ=0.005 (3-seed) OJ = 54.0" (table) | result
L141 | 72.7 | "SDF λ=0.005 (3-seed) CP = 72.7" (table) | result
L141 | 71.3 | "SDF λ=0.005 (3-seed) Milk = 71.3" (table) | result
L141 | 20.0 | "SDF λ=0.005 (3-seed) BBQ = 20.0" (table) | result
L141 | 54.5 | "SDF λ=0.005 (3-seed) Agg. = 54.5" (table) | result
L142 | 57.3 | "SDF λ=0.01 (3-seed) OJ = 57.3" (table) | result
L142 | 72.7 | "SDF λ=0.01 (3-seed) CP = 72.7" (table) | result
L142 | 72.0 | "SDF λ=0.01 (3-seed) Milk = 72.0" (table) | result
L142 | 23.3 | "SDF λ=0.01 (3-seed) BBQ = 23.3" (table) | result
L142 | 56.3 | "SDF λ=0.01 (3-seed) Agg. = 56.3" (table) | result
L143 | 60 | "SDF λ=0.1 s0 OJ = 60" (table) | result
L143 | 74 | "SDF λ=0.1 s0 CP = 74" (table) | result
L143 | 68 | "SDF λ=0.1 s0 Milk = 68" (table) | result
L143 | 30 | "SDF λ=0.1 s0 BBQ = 30" (table) | result
L143 | 58.0 | "SDF λ=0.1 s0 Agg. = 58.0" (table) | result
L144 | 66 | "SDF λ=0.1 s1 OJ = 66" (table) | result
L144 | 72 | "SDF λ=0.1 s1 CP = 72" (table) | result
L144 | 70 | "SDF λ=0.1 s1 Milk = 70" (table) | result
L144 | 26 | "SDF λ=0.1 s1 BBQ = 26" (table) | result
L144 | 58.5 | "SDF λ=0.1 s1 Agg. = 58.5" (table) | result
L145 | 56 | "SDF λ=0.1 s2 OJ = 56" (table) | result
L145 | 76 | "SDF λ=0.1 s2 CP = 76" (table) | result
L145 | 70 | "SDF λ=0.1 s2 Milk = 70" (table) | result
L145 | 16 | "SDF λ=0.1 s2 BBQ = 16" (table) | result
L145 | 54.5 | "SDF λ=0.1 s2 Agg. = 54.5" (table) | result
L146 | 60.7 | "SDF λ=0.1 (3-seed) OJ = 60.7" (table) | result
L146 | 74.0 | "SDF λ=0.1 (3-seed) CP = 74.0" (table) | result
L146 | 69.3 | "SDF λ=0.1 (3-seed) Milk = 69.3" (table) | result
L146 | 24.0 | "SDF λ=0.1 (3-seed) BBQ = 24.0" (table) | result
L146 | 57.0 | "SDF λ=0.1 (3-seed) Agg. = 57.0" (table) | result
L151 | 0.0553 | "avg\_max\_obstacle\_displacement of 0.0553\,m (per-task: OJ\,=\,0.033, CP\,=\,0.055, Milk\,=\,0.041, BBQ\,=\,0.093)" | result
L151 | 0.033 | "OJ\,=\,0.033" | result
L151 | 0.055 | "CP\,=\,0.055" | result
L151 | 0.041 | "Milk\,=\,0.041" | result
L151 | 0.093 | "BBQ\,=\,0.093" | result

### Appendix F: Safe Success Rate Analysis (sec:appendix_ssr)

L174 | 71.5 | "Pi0.5 baseline TSR = 71.5" (table) | result
L174 | 28.5 | "Pi0.5 baseline CAR = 28.5" (table) | result
L174 | 28.0 | "Pi0.5 baseline SSR = 28.0" (table) | result
L174 | 0.39 | "Pi0.5 baseline SSR/TSR = 0.39" (table) | result
L175 | 49.7 | "LoRA-only (3 seeds) TSR = 49.7" (table) | result
L175 | 54.83 | "LoRA-only (3 seeds) CAR = 54.83" (table) | result
L175 | 27.7 | "LoRA-only (3 seeds) SSR = 27.7" (table) | result
L175 | 0.56 | "LoRA-only (3 seeds) SSR/TSR = 0.56" (table) | result
L176 | 54.0 | "SDF λ=0.005 (3 seeds) TSR = 54.0" (table) | result
L176 | 54.5 | "SDF λ=0.005 (3 seeds) CAR = 54.5" (table) | result
L176 | 27.8 | "SDF λ=0.005 (3 seeds) SSR = 27.8" (table) | result
L176 | 0.51 | "SDF λ=0.005 (3 seeds) SSR/TSR = 0.51" (table) | result
L177 | 53.8 | "SDF λ=0.01 (3 seeds) TSR = 53.8" (table) | result
L177 | 56.33 | "SDF λ=0.01 (3 seeds) CAR = 56.33" (table) | result
L177 | 30.2 | "SDF λ=0.01 (3 seeds) SSR = 30.2" (table) | result
L177 | 0.56 | "SDF λ=0.01 (3 seeds) SSR/TSR = 0.56" (table) | result
L178 | 50.2 | "SDF λ=0.1 (3 seeds) TSR = 50.2" (table) | result
L178 | 57.00 | "SDF λ=0.1 (3 seeds) CAR = 57.00" (table) | result
L178 | 30.2 | "SDF λ=0.1 (3 seeds) SSR = 30.2" (table) | result
L178 | 0.60 | "SDF λ=0.1 (3 seeds) SSR/TSR = 0.60" (table) | result

### Appendix G: Per-Task Oracle Analysis (sec:appendix_pertask_oracle)

L187 | 46.0 | "LoRA baseline achieves only 46.0\% CAR" (on task chocolate_pudding) | result
L187 | 55.0 | "Oracle-adaptive improves to 55.0\%" | result
L187 | 47.5 | "Oracle-feature to 47.5\%" | result
L187 | 96.0 | "Oracle-adaptive reduces task~0 (orange_juice) from 96.0\%" | result
L187 | 82.5 | "to 82.5\%" | result
L187 | 98.0 | "task~2 (milk) from 98.0\%" | result
L187 | 77.5 | "to 77.5\%" | result
L189 | 241.7 | "feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants)" | result
L189 | 14.2 | "14.2 for Cartesian variants" | result
L189 | 0.004 | "gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49)" | result
L189 | 0.006 | "0.004--0.006" | result
L189 | 0.18 | "0.18--0.49" | result
L189 | 0.49 | "0.18--0.49" | result
L189 | 76.9 | "CAR (76.9\%) shows no advantage despite 17$\times$ more steps" | result
L189 | 17 | "despite 17$\times$ more steps" | other
L189 | 0 | "The A3 learned SDF never triggers refinement (0 steps/episode)" | result
L201 | 96.0 | "LoRA baseline Task 0 = 96.0" (table) | result
L201 | 46.0 | "LoRA baseline Task 1 = 46.0" (table) | result
L201 | 98.0 | "LoRA baseline Task 2 = 98.0" (table) | result
L201 | 88.0 | "LoRA baseline Task 3 = 88.0" (table) | result
L201 | 82.0 | "LoRA baseline Agg. = 82.0" (table) | result
L203 | 82.5 | "Oracle-adaptive Task 0 = 82.5" (table) | result
L203 | 55.0 | "Oracle-adaptive Task 1 = 55.0" (table) | result
L203 | 77.5 | "Oracle-adaptive Task 2 = 77.5" (table) | result
L203 | 85.0 | "Oracle-adaptive Task 3 = 85.0" (table) | result
L203 | 75.0 | "Oracle-adaptive Agg. = 75.0" (table) | result
L204 | 85.0 | "Oracle-fixed Task 0 = 85.0" (table) | result
L204 | 50.0 | "Oracle-fixed Task 1 = 50.0" (table) | result
L204 | 77.5 | "Oracle-fixed Task 2 = 77.5" (table) | result
L204 | 80.0 | "Oracle-fixed Task 3 = 80.0" (table) | result
L204 | 73.1 | "Oracle-fixed Agg. = 73.1" (table) | result
L205 | 90.0 | "Oracle-feature Task 0 = 90.0" (table) | result
L205 | 47.5 | "Oracle-feature Task 1 = 47.5" (table) | result
L205 | 82.5 | "Oracle-feature Task 2 = 82.5" (table) | result
L205 | 87.5 | "Oracle-feature Task 3 = 87.5" (table) | result
L205 | 76.9 | "Oracle-feature Agg. = 76.9" (table) | result
L212 | 5.1 | "The aggregate CAR drop ($-$5.1\,pp)" | result
L224 | 68.0 | "Pi0.5 LoRA s0 (no refine) OJ = 68.0" (table) | result
L224 | 74.0 | "Pi0.5 LoRA s0 (no refine) CP = 74.0" (table) | result
L224 | 66.0 | "Pi0.5 LoRA s0 (no refine) Milk = 66.0" (table) | result
L224 | 20.0 | "Pi0.5 LoRA s0 (no refine) BBQ = 20.0" (table) | result
L224 | 57.0 | "Pi0.5 LoRA s0 (no refine) Agg. = 57.0" (table) | result
L225 | 50.0 | "Pi0.5 Oracle-adaptive OJ = 50.0" (table) | result
L225 | 75.0 | "Pi0.5 Oracle-adaptive CP = 75.0" (table) | result
L225 | 70.0 | "Pi0.5 Oracle-adaptive Milk = 70.0" (table) | result
L225 | 12.5 | "Pi0.5 Oracle-adaptive BBQ = 12.5" (table) | result
L225 | 51.9 | "Pi0.5 Oracle-adaptive Agg. = 51.9" (table) | result
L227 | -18.0 | "Δ OJ = $-$18.0" (table) | result
L227 | 1.0 | "Δ CP = $+$1.0" (table) | result
L227 | 4.0 | "Δ Milk = $+$4.0" (table) | result
L227 | -7.5 | "Δ BBQ = $-$7.5" (table) | result
L227 | -5.1 | "Δ Agg. = $-$5.1" (table) | result

### Appendix H: Null Distribution (sec:appendix_null)

L236 | 0.005 | "three LoRA-only seeds and three $\lambda = 0.005$ seeds" | hyperparam
L236 | 57.0 | "57.0\% (LoRA s0, re-evaluated)" | result
L236 | 52.5 | "52.5\% (LoRA s1)" | result
L236 | 55.0 | "55.0\% (LoRA s2)" | result
L236 | 57.0 | "57.0\% ($\lambda{=}0.005$ s0)" | result
L236 | 54.0 | "54.0\% ($\lambda{=}0.005$ s1)" | result
L236 | 52.5 | "52.5\% ($\lambda{=}0.005$ s2)" | result
L236 | 54.67 | "yielding mean 54.67\% and standard deviation 2.07\%" | stat
L236 | 2.07 | "standard deviation 2.07\%" | stat
L236 | 5 | "Bessel-corrected, $n{-}1 = 5$" | stat
L236 | 0.01 | "The $\lambda = 0.01$ mean of 56.33\%" | hyperparam
L236 | 56.33 | "$\lambda = 0.01$ mean of 56.33\%" | result
L236 | 0.8 | "falls within $0.8\sigma$ of this null ($p > 0.1$)" | stat
L236 | 0.1 | "$p > 0.1$" | stat
L236 | 0.1 | "$\lambda = 0.1$ 30K mean of 57.00\%" | hyperparam
L236 | 57.00 | "$\lambda = 0.1$ 30K mean of 57.00\%" | result
L236 | 58.0 | "3 seeds: 58.0\%, 58.5\%, 54.5\%" | result
L236 | 58.5 | "3 seeds: 58.0\%, 58.5\%, 54.5\%" | result
L236 | 54.5 | "3 seeds: 58.0\%, 58.5\%, 54.5\%" | result
L236 | 0.155 | "two-tailed permutation $p = 0.155$" | stat
L236 | 0.071 | "one-tailed $p = 0.071$" | stat
L236 | 0.05 | "non-significant at conventional thresholds ($\alpha = 0.05$)" | stat
L238 | 57 | "Pooling the six null values $\{57, 52.5, 55, 57, 54, 52.5\}$" | result
L238 | 52.5 | "$\{57, 52.5, 55, 57, 54, 52.5\}$" | result
L238 | 55 | "$\{57, 52.5, 55, 57, 54, 52.5\}$" | result
L238 | 54 | "$\{57, 52.5, 55, 57, 54, 52.5\}$" | result
L238 | 58 | "three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$" | result
L238 | 58.5 | "$\{58, 58.5, 54.5\}$" | result
L238 | 54.5 | "$\{58, 58.5, 54.5\}$" | result
L238 | 9 | "nine measurements" | stat
L238 | 84 | "$\binom{9}{3} = 84$ three-element combinations" | stat
L238 | 57.00 | "whose mean $\geq 57.00$" | result
L238 | 6 | "Six combinations meet this threshold" | stat
L238 | 6 | "exact one-tailed permutation $p = 6/84 \approx 0.071$" | stat
L238 | 84 | "$p = 6/84$" | stat
L238 | 0.071 | "$\approx 0.071$" | stat
L238 | 13 | "additionally count combinations...yielding $p = 13/84 \approx 0.155$" | stat
L238 | 84 | "$p = 13/84$" | stat
L238 | 0.155 | "$\approx 0.155$" | stat
L238 | 54.5 | "With the third seed ($s_2 = 54.5\%$)" | result
L238 | 58.25 | "2 seeds) down to 57.00\%" — the 2-seed mean is implicitly 58.25 | result
L238 | 57.00 | "the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%" | result
L241 | 57.0 | "three LoRA-only seeds are used as the null pool ($\{57.0, 52.5, 55.0\}$)" | result
L241 | 52.5 | "$\{57.0, 52.5, 55.0\}$" | result
L241 | 55.0 | "$\{57.0, 52.5, 55.0\}$" | result
L241 | 6 | "$\binom{6}{3} = 20$ permutations" | stat
L241 | 20 | "$\binom{6}{3} = 20$ permutations" | stat
L241 | 0.1 | "For $\lambda = 0.1$ (treatment mean 57.00\%)" | hyperparam
L241 | 57.00 | "treatment mean 57.00\%" | result
L241 | 3 | "one-tailed $p = 3/20 = 0.150$" | stat
L241 | 20 | "$p = 3/20$" | stat
L241 | 0.150 | "one-tailed $p = 3/20 = 0.150$" | stat
L241 | 5 | "two-tailed $p = 5/20 = 0.250$" | stat
L241 | 20 | "$p = 5/20$" | stat
L241 | 0.250 | "two-tailed $p = 5/20 = 0.250$" | stat
L241 | 0.01 | "For $\lambda = 0.01$ (treatment mean 56.33\%)" | hyperparam
L241 | 56.33 | "treatment mean 56.33\%" | result
L241 | 6 | "one-tailed $p = 6/20 = 0.300$" | stat
L241 | 20 | "$p = 6/20$" | stat
L241 | 0.300 | "one-tailed $p = 6/20 = 0.300$" | stat
L241 | 12 | "two-tailed $p = 12/20 = 0.600$" | stat
L241 | 20 | "$p = 12/20$" | stat
L241 | 0.600 | "two-tailed $p = 12/20 = 0.600$" | stat
L241 | 0.01 | "Under the broader Null~B pool, $\lambda = 0.01$" | hyperparam
L241 | 13 | "one-tailed $p = 13/84 \approx 0.155$" | stat
L241 | 84 | "$p = 13/84$" | stat
L241 | 0.155 | "$\approx 0.155$" | stat
L241 | 25 | "two-tailed $p = 25/84 \approx 0.298$" | stat
L241 | 84 | "$p = 25/84$" | stat
L241 | 0.298 | "$\approx 0.298$" | stat
L241 | 0.05 | "All tests are non-significant at $\alpha = 0.05$" | stat
L241 | 57.0 | "the LoRA-only pool already contains a high seed (57.0\%)" | result
L243 | 0 | "Setting $\lambda = 0$ during Phase~2 (steps 5K--18K)" | hyperparam
L243 | 5000 | "steps 5K--18K" | hyperparam
L243 | 18000 | "steps 5K--18K" | hyperparam
L243 | 5000 | "SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K)" | hyperparam
L243 | 57.5 | "yields CAR of 57.5\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2)" | result
L243 | 18000 | "at the 18K checkpoint" | hyperparam
L243 | 13000 | "13K steps of Phase~2 training" | hyperparam

### Appendix I: Step-wise Checkpoint Analysis (sec:appendix_stepwise)

L248 | 0.1 | "per-seed CAR at seven checkpoints for $\lambda = 0.1$" | hyperparam
L248 | 0 | "Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K" | dataset
L248 | 16000 | "available at 16K" | hyperparam
L248 | 20000 | "20K" | hyperparam
L248 | 22000 | "22K" | hyperparam
L248 | 30000 | "30K" | hyperparam
L248 | 24000 | "24K--28K report seed-0 only" | hyperparam
L248 | 28000 | "24K--28K" | hyperparam
L248 | 30000 | "seed~2 is available at 30K only" | hyperparam
L260 | 16000 | "16K steps Seed 0 = 55.5, Seed 1 = 56.0, Mean = 55.75" (table) | hyperparam
L260 | 55.5 | "16K steps Seed 0 = 55.5" (table) | result
L260 | 56.0 | "16K steps Seed 1 = 56.0" (table) | result
L260 | 55.75 | "16K steps Mean = 55.75" (table) | result
L261 | 20000 | "20K steps" (table) | hyperparam
L261 | 55.0 | "20K steps Seed 0 = 55.0" (table) | result
L261 | 56.0 | "20K steps Seed 1 = 56.0" (table) | result
L261 | 55.5 | "20K steps Mean = 55.5" (table) | result
L262 | 22000 | "22K steps" (table) | hyperparam
L262 | 60.5 | "22K steps Seed 0 = 60.5" (table) | result
L262 | 56.5 | "22K steps Seed 1 = 56.5" (table) | result
L262 | 58.5 | "22K steps Mean = 58.5" (table) | result
L263 | 24000 | "24K steps" (table) | hyperparam
L263 | 52.5 | "24K steps Seed 0 = 52.5" (table) | result
L264 | 26000 | "26K steps" (table) | hyperparam
L264 | 53.5 | "26K steps Seed 0 = 53.5" (table) | result
L265 | 28000 | "28K steps" (table) | hyperparam
L265 | 54.5 | "28K steps Seed 0 = 54.5" (table) | result
L266 | 30000 | "30K steps" (table) | hyperparam
L266 | 58.0 | "30K steps Seed 0 = 58.0" (table) | result
L266 | 58.5 | "30K steps Seed 1 = 58.5" (table) | result
L266 | 54.5 | "30K steps Seed 2 = 54.5" (table) | result
L266 | 57.00 | "30K steps Mean = 57.00" (table) | result
L271 | 8 | "checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%)" | result
L271 | 52.5 | "seed~0: 52.5--60.5\%" | result
L271 | 60.5 | "52.5--60.5\%" | result
L271 | 3 | "cross-seed standard deviation at any fixed checkpoint ($\leq$3\,pp)" | stat
L271 | 50 | "consistent with binomial sampling noise at $n = 50$ episodes per task" | dataset
L271 | 7 | "$\sigma \approx 7$\,pp per task for $p \approx 0.5$" | stat
L271 | 0.5 | "for $p \approx 0.5$" | stat
L271 | 30000 | "At 30K" | hyperparam
L271 | 54.5 | "the third seed ($s_2 = 54.5\%$) falls well within the null range" | result
L271 | 57.00 | "pulling the three-seed mean to 57.00\%" | result
L271 | 0.155 | "rendering the earlier two-seed departure non-significant ($p = 0.155$)" | stat

### Appendix J: Oracle SDF Refinement Details (sec:appendix_oracle)

L277 | 160 | "Each is evaluated for 160 episodes (4 tasks $\times$ 40)" | dataset
L277 | 4 | "4 tasks $\times$ 40" | dataset
L277 | 40 | "4 tasks $\times$ 40" | dataset
L281 | 0.005 | "the step size is fixed at $\alpha = 0.005$ regardless of distance" | hyperparam
L283 | 241.7 | "feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants)" | result
L283 | 14.2 | "vs.\ 14.2 for Cartesian variants" | result
L283 | 0.004 | "gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space)" | result
L283 | 0.006 | "0.004--0.006" | result
L283 | 0.18 | "0.18--0.49" | result
L283 | 0.49 | "0.18--0.49 in action space" | result

### Appendix K: Cross-Scene Validation (sec:appendix_spatial_bowl)

L291 | 0.005 | "SDF condition ($\lambda = 0.005$) yields CAR of 11.5\% versus 12.0\% for LoRA-only" | hyperparam
L291 | 11.5 | "yields CAR of 11.5\%" | result
L291 | 12.0 | "versus 12.0\% for LoRA-only" | result
L291 | 0.5 | "a $-$0.5\,pp difference" | result
L291 | 49.0 | "TSR is comparable across conditions (49.0\% vs.\ 51.5\%)" | result
L291 | 51.5 | "49.0\% vs.\ 51.5\%" | result
L291 | 0 | "single training seed (seed~0)" | hyperparam
L291 | 7 | "a single evaluation seed (seed~7, 200 episodes)" | hyperparam
L291 | 200 | "200 episodes" | dataset
L303 | 12.0 | "LoRA-only CAR = 12.0" (table) | result
L303 | 49.0 | "LoRA-only TSR = 49.0" (table) | result
L304 | 0.005 | "SDF λ=0.005" (table) | hyperparam
L304 | 11.5 | "SDF λ=0.005 CAR = 11.5" (table) | result
L304 | 51.5 | "SDF λ=0.005 TSR = 51.5" (table) | result
L309 | 11 | "The substantially lower CAR on spatial_bowl relative to object_pudding (11--12\% vs.\ 54--57\%)" | result
L309 | 12 | "11--12\%" | result
L309 | 54 | "vs.\ 54--57\%" | result
L309 | 57 | "54--57\%" | result
L309 | 0.5 | "the SDF condition performs comparably ($\Delta$CAR\,=\,$-$0.5\,pp, well within noise)" | result

### Appendix L: Evaluation Seed Robustness (sec:appendix_eval_seed)

L330 | 53.0 | "LoRA s0 CAR @ eval seed 0 = 53.0" (table) | result
L330 | 57.0 | "LoRA s0 CAR @ eval seed 7 = 57.0" (table) | result
L330 | 56.5 | "LoRA s0 CAR @ eval seed 42 = 56.5" (table) | result
L330 | 57.5 | "LoRA s0 CAR @ eval seed 99 = 57.5" (table) | result
L330 | 53.0 | "LoRA s0 CAR @ eval seed 123 = 53.0" (table) | result
L330 | 55.4 | "LoRA s0 Mean CAR = 55.4$\pm$2.2" (table) | result
L330 | 2.2 | "$\pm$2.2" (table) | stat
L331 | 55.5 | "LoRA s0 TSR @ eval seed 0 = 55.5" (table) | result
L331 | 46.0 | "LoRA s0 TSR @ eval seed 7 = 46.0" (table) | result
L331 | 46.0 | "LoRA s0 TSR @ eval seed 42 = 46.0" (table) | result
L331 | 52.0 | "LoRA s0 TSR @ eval seed 99 = 52.0" (table) | result
L331 | 50.5 | "LoRA s0 TSR @ eval seed 123 = 50.5" (table) | result
L331 | 50.0 | "LoRA s0 Mean TSR = 50.0$\pm$4.1" (table) | result
L331 | 4.1 | "$\pm$4.1" (table) | stat
L334 | 52.5 | "SDF λ=0.01 s0 CAR @ eval seed 0 = 52.5" (table) | result
L334 | 57.0 | "SDF λ=0.01 s0 CAR @ eval seed 7 = 57.0" (table) | result
L334 | 57.0 | "SDF λ=0.01 s0 CAR @ eval seed 99 = 57.0" (table) | result
L334 | 57.0 | "SDF λ=0.01 s0 CAR @ eval seed 256 = 57.0" (table) | result
L334 | 55.9 | "SDF λ=0.01 s0 Mean CAR = 55.9$\pm$2.3" (table) | result
L334 | 2.3 | "$\pm$2.3" (table) | stat
L335 | 48.5 | "SDF λ=0.01 s0 TSR @ eval seed 0 = 48.5" (table) | result
L335 | 52.5 | "SDF λ=0.01 s0 TSR @ eval seed 7 = 52.5" (table) | result
L335 | 46.5 | "SDF λ=0.01 s0 TSR @ eval seed 99 = 46.5" (table) | result
L335 | 48.0 | "SDF λ=0.01 s0 TSR @ eval seed 256 = 48.0" (table) | result
L335 | 48.9 | "SDF λ=0.01 s0 Mean TSR = 48.9$\pm$2.6" (table) | result
L335 | 2.6 | "$\pm$2.6" (table) | stat
L338 | 58.0 | "SDF λ=0.1 s0 CAR @ eval seed 7 = 58.0" (table) | result
L338 | 59.0 | "SDF λ=0.1 s0 CAR @ eval seed 42 = 59.0" (table) | result
L338 | 58.5 | "SDF λ=0.1 s0 CAR @ eval seed 123 = 58.5" (table) | result
L338 | 57.0 | "SDF λ=0.1 s0 CAR @ eval seed 256 = 57.0" (table) | result
L338 | 58.1 | "SDF λ=0.1 s0 Mean CAR = 58.1$\pm$0.9" (table) | result
L338 | 0.9 | "$\pm$0.9" (table) | stat
L339 | 47.0 | "SDF λ=0.1 s0 TSR @ eval seed 7 = 47.0" (table) | result
L339 | 52.5 | "SDF λ=0.1 s0 TSR @ eval seed 42 = 52.5" (table) | result
L339 | 53.5 | "SDF λ=0.1 s0 TSR @ eval seed 123 = 53.5" (table) | result
L339 | 48.0 | "SDF λ=0.1 s0 TSR @ eval seed 256 = 48.0" (table) | result
L339 | 50.3 | "SDF λ=0.1 s0 Mean TSR = 50.3$\pm$3.2" (table) | result
L339 | 3.2 | "$\pm$3.2" (table) | stat
L344 | 53.0 | "LoRA s0 CAR ranges from 53.0\% to 57.5\% across five evaluation seeds" | result
L344 | 57.5 | "to 57.5\%" | result
L344 | 5 | "across five evaluation seeds" | dataset
L344 | 2.2 | "(std\,=\,2.2\,pp)" | stat
L344 | 55.9 | "SDF λ=0.01 s0 produces near-identical mean CAR (55.9\% across four eval seeds vs.\ 55.4\% for LoRA)" | result
L344 | 4 | "across four eval seeds" | dataset
L344 | 55.4 | "vs.\ 55.4\% for LoRA" | result
L344 | 58.1 | "SDF λ=0.1 s0 shows a slightly higher mean (58.1\%)" | result
L344 | 2.8 | "the difference (2.8\,pp, ${<}$1.3$\sigma$)" | result
L344 | 1.3 | "${<}$1.3$\sigma$" | stat

### Appendix L continued: Per-task eval seed detail (tab:eval_seed_car_detail)

L358 | 46 | "LoRA s0 eval 0: OJ = 46" (table) | result
L358 | 70 | "LoRA s0 eval 0: CP = 70" (table) | result
L358 | 74 | "LoRA s0 eval 0: Milk = 74" (table) | result
L358 | 22 | "LoRA s0 eval 0: BBQ = 22" (table) | result
L358 | 53.0 | "LoRA s0 eval 0: Agg. = 53.0" (table) | result
L359 | 68 | "LoRA s0 eval 7: OJ = 68" (table) | result
L359 | 74 | "LoRA s0 eval 7: CP = 74" (table) | result
L359 | 66 | "LoRA s0 eval 7: Milk = 66" (table) | result
L359 | 20 | "LoRA s0 eval 7: BBQ = 20" (table) | result
L359 | 57.0 | "LoRA s0 eval 7: Agg. = 57.0" (table) | result
L360 | 60 | "LoRA s0 eval 42: OJ = 60" (table) | result
L360 | 70 | "LoRA s0 eval 42: CP = 70" (table) | result
L360 | 68 | "LoRA s0 eval 42: Milk = 68" (table) | result
L360 | 28 | "LoRA s0 eval 42: BBQ = 28" (table) | result
L360 | 56.5 | "LoRA s0 eval 42: Agg. = 56.5" (table) | result
L361 | 58 | "LoRA s0 eval 99: OJ = 58" (table) | result
L361 | 76 | "LoRA s0 eval 99: CP = 76" (table) | result
L361 | 66 | "LoRA s0 eval 99: Milk = 66" (table) | result
L361 | 30 | "LoRA s0 eval 99: BBQ = 30" (table) | result
L361 | 57.5 | "LoRA s0 eval 99: Agg. = 57.5" (table) | result
L362 | 52 | "LoRA s0 eval 123: OJ = 52" (table) | result
L362 | 74 | "LoRA s0 eval 123: CP = 74" (table) | result
L362 | 66 | "LoRA s0 eval 123: Milk = 66" (table) | result
L362 | 20 | "LoRA s0 eval 123: BBQ = 20" (table) | result
L362 | 53.0 | "LoRA s0 eval 123: Agg. = 53.0" (table) | result
L364 | 56.8 | "Mean$\pm$Std OJ = 56.8$\pm$8.3" (table) | result
L364 | 8.3 | "$\pm$8.3" (table) | stat
L364 | 72.8 | "Mean$\pm$Std CP = 72.8$\pm$2.7" (table) | result
L364 | 2.7 | "$\pm$2.7" (table) | stat
L364 | 68.0 | "Mean$\pm$Std Milk = 68.0$\pm$3.5" (table) | result
L364 | 3.5 | "$\pm$3.5" (table) | stat
L364 | 24.0 | "Mean$\pm$Std BBQ = 24.0$\pm$4.7" (table) | result
L364 | 4.7 | "$\pm$4.7" (table) | stat
L364 | 55.4 | "Mean$\pm$Std Agg. = 55.4$\pm$2.2" (table) | result
L364 | 2.2 | "$\pm$2.2" (table) | stat

### Appendix M: Training Details (sec:appendix_training)

L374 | 16 | "LoRA adapters injected into the PaliGemma vision encoder (rank 16, α=16)" | hyperparam
L374 | 16 | "α=16" | hyperparam
L374 | 32 | "action expert (rank 32, α=32)" | hyperparam
L374 | 32 | "α=32" | hyperparam
L374 | 4 | "The SDF decoder is a 4-layer MLP (hidden dimension 256)" | hyperparam
L374 | 256 | "hidden dimension 256" | hyperparam
L374 | 1024 | "taking pooled suffix features (1024-d)" | hyperparam
L374 | 3 | "query points (3-d) as input" | hyperparam
L374 | 1024 | "end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3)" | hyperparam
L374 | 256 | "1024 $\to$ 256 $\to$ 3" | hyperparam
L374 | 3 | "1024 $\to$ 256 $\to$ 3" | hyperparam
L379 | 0 | "Phase 1 (steps 0--5000)" | hyperparam
L379 | 5000 | "steps 0--5000" | hyperparam
L381 | 5000 | "Phase 2 (steps 5000--30000)" | hyperparam
L381 | 30000 | "steps 5000--30000" | hyperparam
L381 | 100 | "100-step gradient warmup ramp" | hyperparam
L393 | 3.5 | "Pi0.5 (OpenPi, $\sim$3.5B parameters)" (hyperparams table) | other
L394 | 2.5e-5 | "Learning rate & $2.5 \times 10^{-5}$" (hyperparams table) | hyperparam
L395 | 1000 | "Warmup steps & 1000" (hyperparams table) | hyperparam
L396 | 32 | "Batch size & 32" (hyperparams table) | hyperparam
L397 | 30000 | "Total steps & 30000" (hyperparams table) | hyperparam
L398 | 0.005 | "$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\}" (hyperparams table) | hyperparam
L398 | 0.01 | "0.01" (hyperparams table) | hyperparam
L398 | 0.1 | "0.1" (hyperparams table) | hyperparam
L399 | 0.01 | "$\lambda_\mathrm{ee}$ & 0.01" (hyperparams table) | hyperparam
L400 | 64 | "SDF query points per step & 64" (hyperparams table) | hyperparam
L401 | 0.05 | "SDF clamp $\delta$ & 0.05 m" (hyperparams table) | hyperparam
L402 | 0.1 | "Eikonal weight & 0.1" (hyperparams table) | hyperparam
L403 | 16 | "LoRA rank (vision) & 16" (hyperparams table) | hyperparam
L404 | 32 | "LoRA rank (action) & 32" (hyperparams table) | hyperparam
L405 | 5000 | "Phase 1 duration & 5000 steps" (hyperparams table) | hyperparam
L411 | 300 | "Each episode runs for at most 300 timesteps" | hyperparam
L411 | 50 | "The policy generates a 50-step action trajectory" | hyperparam
L411 | 5 | "executes the first 5 steps before replanning" | hyperparam
L411 | 180 | "camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention" | hyperparam
L411 | 5 | "verified to restore TSR from ${\sim}$5\% to ${\sim}$52\%" | result
L411 | 52 | "to ${\sim}$52\%" | result
L411 | 40 | "Oracle variants use 40 episodes per task (160 total)" | dataset
L411 | 160 | "40 episodes per task (160 total)" | dataset
L411 | 50 | "all other configurations use 50 episodes per task (200 total)" | dataset
L411 | 200 | "50 episodes per task (200 total)" | dataset
L414 | 64 | "SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid" | hyperparam
L414 | 64 | "64 query points are randomly sampled per step from this grid" | hyperparam
L417 | 96 | "NVIDIA RTX PRO 6000 GPUs (96\,GB)" | other
L417 | 6 | "Phase~1 (5K steps) takes approximately 6 hours on a single GPU" | other
L417 | 5000 | "Phase~1 (5K steps)" | hyperparam
L417 | 25000 | "Phase~2 (25K steps) takes approximately 32 hours" | hyperparam
L417 | 32 | "approximately 32 hours" | other
L417 | 200 | "Evaluation of 200 episodes requires approximately 4 hours" | dataset
L417 | 4 | "approximately 4 hours" | other
L417 | 100 | "Across 100+ experiments" | dataset
L417 | 700 | "total computational budget is approximately 700 GPU-hours" | other

### Appendix N: TSR Collapse Mechanism (sec:appendix_tsr_collapse)

L423 | 71.5 | "Fine-tuning Pi0.5 with LoRA alone reduces TSR from 71.5\%" | result
L423 | 49.7 | "to 49.7\,$\pm$\,3.2\%" | result
L423 | 3.2 | "$\pm$\,3.2\%" | stat
L423 | 21.8 | "a drop of 21.8\,pp" | result
L423 | 0.005 | "TSR under $\lambda = 0.005$ is 54.0\,$\pm$\,3.0\%" | hyperparam
L423 | 54.0 | "54.0\,$\pm$\,3.0\%" | result
L423 | 3.0 | "$\pm$\,3.0\%" | stat
L423 | 17.5 | "($-$17.5\,pp)" | result
L423 | 0.01 | "under $\lambda = 0.01$ is 53.8\,$\pm$\,1.5\%" | hyperparam
L423 | 53.8 | "53.8\,$\pm$\,1.5\%" | result
L423 | 1.5 | "$\pm$\,1.5\%" | stat
L423 | 17.7 | "($-$17.7\,pp)" | result
L423 | 0.1 | "under $\lambda = 0.1$ is 50.2\,$\pm$\,3.9\%" | hyperparam
L423 | 50.2 | "50.2\,$\pm$\,3.9\%" | result
L423 | 3.9 | "$\pm$\,3.9\%" | stat
L423 | 21.3 | "($-$21.3\,pp)" | result
L423 | 21.8 | "The largest SDF drop ($\lambda = 0.1$, $-$21.3\,pp) matches the LoRA-only drop ($-$21.8\,pp) to within 0.5\,pp" | result
L423 | 0.5 | "to within 0.5\,pp" | result
L425 | 0.37 | "end-effector displacement $>$\,0.37\,m" | result
L425 | 0.05 | "mean obstacle displacement ${\sim}$0.05\,m" | result
L425 | 0.5 | "baseline safe failure rate 0.5\%" | result
L425 | 50 | "${\sim}$50\% of episodes" | result
L425 | 100 | "representing a 100$\times$ increase in safe failures" | result

---

## main.tex

*(No quantitative numbers — only document structure, package declarations, and \input commands.)*

---

## contingency_claim3.tex

*(This file is NOT included in main.tex — it contains placeholder templates with {MEAN}, {S0}, {S1}, {DELTA} tokens, not actual numbers. The scenario thresholds are qualitative decision rules, not paper data. No real numbers to extract.)*

Placeholder values noted for audit completeness:
- 54.5 | "null distribution (mean 54.5\%, $\sigma = 2.15$)" — referenced scenario threshold
- 2.15 | "$\sigma = 2.15$" — referenced scenario threshold

---

## experimental_framework.tex

L5 | 50 | "Each method is evaluated for 50 episodes per task (200 episodes total)" | dataset
L5 | 200 | "200 episodes total" | dataset
L5 | 3 | "multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration" | dataset
L5 | 600 | "600 episodes per configuration" | dataset
L19 | 0.1 | "$\tau_d = 0.1$\,mm" | hyperparam
L23 | 1 | "collapsed episodes cluster below 1\,$\mu$m and active episodes exceed 200\,mm" | result
L23 | 200 | "active episodes exceed 200\,mm" | result
L23 | 2 | "any $\tau_d \in [2, 200]$\,mm produces identical filtering" | result
L23 | 200 | "$\tau_d \in [2, 200]$\,mm" | result
L29 | 3 | "Pi0 (${\sim}$3B parameters)" | other
L29 | 3.5 | "Pi0.5 extends this architecture to ${\sim}$3.5B parameters" | other
L36 | 0.005 | "We evaluate $\lambda_\text{SDF} \in \{0.005, 0.01\}$" | hyperparam
L36 | 0.01 | "0.01\}" | hyperparam
L36 | 0 | "Phase~1 (steps 0--5K)" | hyperparam
L36 | 5000 | "steps 0--5K" | hyperparam
L36 | 5000 | "Phase~2 (steps 5K--30K)" | hyperparam
L36 | 30000 | "steps 5K--30K" | hyperparam
L46 | 0.005 | "a constant step size $\alpha = 0.005$" | hyperparam
L49 | 160 | "Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes)" | dataset
L49 | 4 | "4 tasks $\times$ 40 episodes" | dataset
L49 | 40 | "4 tasks $\times$ 40 episodes" | dataset

---

*End of Phase 1 extraction. Total files processed: 12 (10 active, 1 structure-only [main.tex], 1 template-only [contingency_claim3.tex]).*
