# Dual Narrative Templates: Claim 3 λ=0.1 Results

> **Purpose**: Pre-written text for two scenarios based on λ=0.1 s2 30K result.  
> **Decision rule**: Scenario C if 3-seed permutation p < 0.05; Scenario B if p ≥ 0.05.  
> **Placeholders**: `{s0_car}`, `{s1_car}`, `{s2_car}`, `{mean_car}`, `{std_car}`, `{p_value}`, `{z_value}`, `{delta_pp}` (= mean_car − 54.5), `{tsr_mean}`, `{tsr_std}`  
> **Null distribution**: mean=54.5%, σ=2.15 (LoRA×2 + λ=0.005×3, 5 measurements)  
> **Current 2-seed 30K**: s0≈58.6%, s1≈57.9%, mean=58.25%

---

## File: abstract.tex, Line 7

### Current text:
> Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.83\%$\,\pm\,$2.25, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61); at $\lambda{=}0.1$, two of three seeds show a marginal signal (58.25\%$\,\pm\,$0.35, $p{\approx}0.032$) whose per-task avoidance pattern still mirrors the demonstration distribution, requiring further investigation.

### Version A (Scenario C, p < 0.05):
> Its contribution during training is dose-dependent: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.83\%$\,\pm\,$2.25, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61); at $\lambda{=}0.1$, a modest but statistically significant increase emerges ({mean_car}\%$\,\pm\,${std_car}, permutation $p{=}${p_value}, 3 seeds), though the effect size ({delta_pp}\,pp) is small relative to the $+$28\,pp gain from fine-tuning alone, and per-task avoidance patterns still mirror the demonstration distribution.

### Version B (Scenario B, p ≥ 0.05):
> SDF supervision during training adds no measurable benefit: LoRA-only fine-tuning raises dfCAR from 26.8\% to 54.83\%$\,\pm\,$2.25, matching SDF-augmented training across the full tested range $\lambda \in \{0.005, 0.01, 0.1\}$ ($p{>}0.05$ for all; $\lambda{=}0.1$: {mean_car}\%$\,\pm\,${std_car}, 3 seeds).

---

## File: abstract.tex, Line 9

### Current text:
> Displacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision can be neither credited with nor expected to deliver collision avoidance.

### Version A (Scenario C, p < 0.05):
> Displacement filtering is necessary for meaningful VLA safety evaluation; even at the highest tested loss weight, the modest SDF effect is dwarfed by demonstration-driven avoidance and cannot overcome the structural limitation of EE-only supervision.

### Version B (Scenario B, p ≥ 0.05):
> Displacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision is fully redundant across a 20$\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.

---

## File: claim3.tex, Line 3

### Current text:
> Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.

### Version A (Scenario C, p < 0.05):
> Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF at three loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.

### Version B (Scenario B, p ≥ 0.05):
> Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.

---

## File: claim3.tex, Line 7 (Table caption)

### Current text:
> \caption{Avoidance source attribution on SafeLIBERO. SDF at $\lambda \leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$); $\lambda = 0.1$ shows a marginal signal ($z = 1.85$, $p \approx 0.032$, $n{=}2$) that requires additional seeds. All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}

### Version A (Scenario C, p < 0.05):
> \caption{Avoidance source attribution on SafeLIBERO. SDF at $\lambda \leq 0.01$ adds no measurable CAR beyond LoRA-only ($p > 0.1$). At $\lambda = 0.1$, a modest increase reaches statistical significance ($z = {z_value}$, permutation $p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\,pp) is small relative to the $+$28\,pp LoRA gain. All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}

### Version B (Scenario B, p ≥ 0.05):
> \caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}

---

## File: claim3.tex, Line 20 (Table λ=0.1 row)

### Current text:
> LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 48.0\,$\pm$\,1.4 & 58.25\,$\pm$\,0.35 & 0.394 \\

### Version A (Scenario C, p < 0.05):
> LoRA+SDF $\lambda{=}0.1$ & 3 & {tsr_mean}\,$\pm$\,{tsr_std} & {mean_car}\,$\pm$\,{std_car} & 0.394 \\

### Version B (Scenario B, p ≥ 0.05):
> LoRA+SDF $\lambda{=}0.1$ & 3 & {tsr_mean}\,$\pm$\,{tsr_std} & {mean_car}\,$\pm$\,{std_car} & 0.394 \\

---

## File: claim3.tex, Line 24 (Table footnote)

### Current text:
> {\footnotesize \textsuperscript{$\dagger$}30K checkpoint, two of three seeds; third seed in progress.}

### Version A (Scenario C, p < 0.05):
> *(Delete footnote and remove $\dagger$ from table row.)*

### Version B (Scenario B, p ≥ 0.05):
> *(Delete footnote and remove $\dagger$ from table row.)*

---

## File: claim3.tex, Lines 27 (Main body paragraph)

### Current text:
> Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.83\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\%) is within 0.25\,pp of $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.33\%, $p > 0.1$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.

### Version A (Scenario C, p < 0.05):
> Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.83\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. At $\lambda \leq 0.01$, SDF supervision produces no measurable benefit: LoRA-only CAR (54.83\%) is within 0.25\,pp of $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.33\%, $p > 0.1$; Appendix~\ref{sec:appendix_null}). At $\lambda = 0.1$, a modest increase emerges (Section~\ref{sec:lambda_high}), but per-task CAR ordering remains identical across all conditions (chocolate\_pudding highest, bbq\_sauce lowest), indicating that avoidance patterns reflect the demonstration distribution regardless of SDF loss weight. A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect.

### Version B (Scenario B, p ≥ 0.05):
> Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.83\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.83\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ ({mean_car}\%, $p = {p_value}$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.

---

## File: claim3.tex, Lines 32–33 (Dose-response paragraph)

### Current text:
> \paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
> Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,58.25\%\,$\pm$\,0.35 at the 30K checkpoint (two of three seeds), above the null distribution (mean 54.67\%, $\sigma = 1.94$, $z = 1.85$, $p \approx 0.032$). This departure is suggestive but inconclusive at $n = 2$. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend (mean 55.3\%, within 0.3$\sigma$ of the null; Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K remains identical to all other conditions (Figure~\ref{fig:lambda_car}). The response is thus dose-dependent: SDF is fully redundant at $\lambda \leq 0.01$ ($p > 0.1$), with a marginal signal at $\lambda = 0.1$ whose modest effect size (${\sim}$3.6\,pp) and limited sample preclude strong conclusions. Even at elevated $\lambda$, avoidance patterns remain driven by demonstration distribution rather than geometric supervision.

### Version A (Scenario C, p < 0.05):
> \paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
> Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint (3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), a modest but statistically significant departure from the null distribution (mean 54.5\%, $\sigma = 2.15$; permutation $p = {p_value}$). The effect size of {delta_pp}\,pp is small relative to the $+$28\,pp gain from LoRA fine-tuning alone, indicating that EE-only SDF supervision can incrementally augment demonstration-driven avoidance at sufficiently high loss weights but cannot substitute for it. A stepwise ablation across six checkpoints (16K--28K) shows no sustained trend prior to 30K (mean 55.3\%, within 0.3$\sigma$ of the null; Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K remains identical to all other conditions (Figure~\ref{fig:lambda_car}), confirming that the dominant avoidance signal remains the demonstration distribution. The response is thus dose-dependent: SDF is fully redundant at $\lambda \leq 0.01$ ($p > 0.1$), with a small but detectable effect at $\lambda = 0.1$ that preserves the same demonstration-driven avoidance fingerprint.

### Version B (Scenario B, p ≥ 0.05):
> \paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
> Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint (3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$; permutation $p = {p_value}$). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.

---

## File: claim3.tex, Lines 38–39 (Figure caption)

### Current text:
> \caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ (58.25\%, 2 seeds) shows a marginal departure ($p \approx 0.032$) whose per-task pattern still matches the demonstration distribution.}

### Version A (Scenario C, p < 0.05):
> \caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within the null band; $\lambda = 0.1$ ({mean_car}\%, 3 seeds) shows a modest but significant departure (permutation $p = {p_value}$, {delta_pp}\,pp effect size) whose per-task avoidance pattern still matches the demonstration distribution.}

### Version B (Scenario B, p ≥ 0.05):
> \caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. All tested $\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\times$ loss-weight range.}

---

## File: discussion.tex, Line 6

### Current text:
> \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$28\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). At low $\lambda$, SDF is redundant; at $\lambda = 0.1$, the marginal signal preserves the same demonstration-driven pattern.

### Version A (Scenario C, p < 0.05):
> \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$28\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). At $\lambda \leq 0.01$, SDF is fully redundant; at $\lambda = 0.1$, a modest {delta_pp}\,pp effect emerges ($p = {p_value}$) but preserves the same demonstration-driven avoidance pattern, suggesting that EE-only SDF can weakly augment—but not redirect—the implicit signal at sufficiently high loss weights.

### Version B (Scenario B, p ≥ 0.05):
> \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$28\,pp CAR gain arises entirely from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = {p_value}$), confirming that Level~A signal masking is not the binding constraint—the failure is architectural.

---

## File: discussion.tex, Line 12 (Limitations)

### Current text:
> The $\lambda = 0.1$ condition has $n = 2$ seeds; the marginal departure ($p \approx 0.032$) is inconclusive.

### Version A (Scenario C, p < 0.05):
> The $\lambda = 0.1$ effect ({delta_pp}\,pp, $p = {p_value}$, $n = 3$) is statistically significant but small; whether this modest gain justifies the computational cost of SDF supervision requires task-specific cost-benefit analysis.

### Version B (Scenario B, p ≥ 0.05):
> *(Delete this sentence entirely — the λ=0.1 limitation is resolved.)*

---

## File: discussion.tex, Line 3 (Opening summary)

### Current text:
> Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for all measured avoidance gains (\S\ref{sec:avoidance_source}).

### Version A (Scenario C, p < 0.05):
> Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing at most a modest increment at high loss weights (\S\ref{sec:avoidance_source}).

### Version B (Scenario B, p ≥ 0.05):
> *(No change needed — current text already states "all measured avoidance gains," which is correct for Scenario B.)*

---

## Summary: Switch Checklist

When s2 30K result arrives, compute 3-seed mean, run permutation test, then:

| Step | Version A (p < 0.05) | Version B (p ≥ 0.05) |
|------|----------------------|----------------------|
| 1. abstract.tex L7 | Replace with dose-dependent + modest significance | Replace with full-range redundancy |
| 2. abstract.tex L9 | Weaken to "dwarfed by demo-driven avoidance" | Strengthen to "fully redundant" |
| 3. claim3.tex L3 | Add λ=0.1 to scope list | Add λ=0.1 + "20× range" framing |
| 4. claim3.tex L7 caption | Add significance stats, note small effect | Remove λ-specific stats, state full redundancy |
| 5. claim3.tex L20 table | Update to 3-seed numbers | Update to 3-seed numbers |
| 6. claim3.tex L24 footnote | Delete | Delete |
| 7. claim3.tex L27 body | Split low/high λ narrative | Extend redundancy to full range |
| 8. claim3.tex L32–33 dose-response ¶ | Rewrite as modest-but-significant | Replace with full-redundancy confirmation |
| 9. claim3.tex L38–39 fig caption | Update numbers + "modest" | Full redundancy framing |
| 10. discussion.tex L3 | "nearly all" instead of "all" | No change |
| 11. discussion.tex L6 | Acknowledge weak augmentation | Confirm architectural failure |
| 12. discussion.tex L12 | Replace with cost-benefit framing | Delete sentence |

### Permutation Test Command (run when s2 data arrives)
```python
# Null pool: LoRA s0, s1, s2 + λ=0.005 s0, s1, s2 (6 values after LoRA s2 completes)
# Or: LoRA s0, s1 + λ=0.005 s0, s1, s2 (5 values, current null)
# Test pool: λ=0.1 s0, s1, s2 (3 values)
# One-sided test: does λ=0.1 mean exceed null mean?
```
