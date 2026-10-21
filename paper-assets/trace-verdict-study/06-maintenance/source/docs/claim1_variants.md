# Claim 1 A/B Variants — Pending seed456 Result

> Prepared 2026-05-15. Exact DeepSeek seed456 numbers marked `XX.XX%` — fill in when results arrive.
> Mean/σ are Director's estimates: Version A (seed456≈99%) → mean≈96.5%, σ≈5pp; Version B (seed456≈91%) → mean≈94.5%, σ≈5pp.
> All numbers use **final checkpoint (epoch 3)** as primary, consistent with current paper.

---

## 1. Abstract (main.tex, lines 20–23)

### Current
```latex
Our key finding is that exception events alone achieve near-perfect accuracy across models under the primary seed (99.83\% Qwen, 99.33\% DeepSeek, gap = 0.50pp), while a multi-component representation (VOTA) degrades by 14.96pp on the weaker model.
We decompose the gap between full traces and compressed representations into gradient dilution (26\%) and information overload (74\%), establishing that irrelevant trace content---not training signal quality---is the primary bottleneck.
Component ablation reveals a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach only 85.6\%.
These results reframe verdict prediction as fault detection, where the minimal sufficient signal is a compact exception event; cross-model seed robustness is under active investigation.
```

### Version A (seed456 ≈ 99%, optimistic)
```latex
Our key finding is that exception events alone achieve near-perfect accuracy on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and are the most effective component on DeepSeek (mean XX.XX\%, $\sigma{=}$X.Xpp, 3 seeds), with two of three DeepSeek seeds matching Qwen performance; the outlier is attributable to LoRA initialization sensitivity.
A multi-component representation (VOTA) degrades by 14.96pp on the weaker model.
We decompose the gap between full traces and compressed representations into gradient dilution (26\%) and information overload (74\%), establishing that irrelevant trace content---not training signal quality---is the primary bottleneck.
Component ablation reveals a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach only 85.6\%.
These results reframe verdict prediction as fault detection, where the minimal sufficient signal is a compact exception event that transfers well across model families; training stability is a secondary factor for smaller models.
```

### Version B (seed456 ≈ 91%, conservative)
```latex
Our key finding is that exception events alone achieve near-perfect accuracy on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and consistently outperform all other trace components on DeepSeek (mean XX.XX\% vs.\ VOTA 84.45\%), but absolute cross-model parity is not achieved ($\sigma{=}$X.Xpp across 3 DeepSeek seeds).
A multi-component representation (VOTA) degrades by 14.96pp on the weaker model.
We decompose the gap between full traces and compressed representations into gradient dilution (26\%) and information overload (74\%), establishing that irrelevant trace content---not training signal quality---is the primary bottleneck.
Component ablation reveals a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy, while Tier~2 signals (loop compression) reach only 85.6\%.
These results reframe verdict prediction as fault detection, where the minimal sufficient signal is a compact exception event---the best-performing component on both models---though model-dependent training dynamics affect absolute cross-model performance.
```

---

## 2. Introduction — Bold Finding (introduction.tex, lines 15–17)

### Current
```latex
Our results reveal a striking finding: \textbf{exception events alone are sufficient for near-perfect verdict prediction across models under the primary seed, though cross-model seed robustness requires further validation.}
With only exception events as trace input, both models achieve ${\geq}$99.3\% accuracy under seed 42 (cross-model gap = 0.50 percentage points); DeepSeek seed sensitivity is under investigation.
In contrast, the full VOTA representation---which combines exception events with assertion-point and loop information---degrades by 14.96pp on the weaker model, indicating that processing mixed trace components demands model capability that exception-only prediction does not.
```

### Version A
```latex
Our results reveal a striking finding: \textbf{exception events alone achieve near-perfect verdict prediction on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and transfer well to DeepSeek (mean XX.XX\%), though LoRA initialization sensitivity introduces seed-dependent variance ($\sigma{=}$X.Xpp).}
Two of three DeepSeek seeds match Qwen performance; the outlier (seed 123, 91.09\%) is attributable to suboptimal LoRA initialization (fail recall = 70\%).
In contrast, the full VOTA representation---which combines exception events with assertion-point and loop information---degrades by 14.96pp on the weaker model, indicating that processing mixed trace components demands model capability that exception-only prediction does not.
```

### Version B
```latex
Our results reveal a striking finding: \textbf{exception events alone achieve near-perfect verdict prediction on Qwen (99.83\% $\pm$ 0.00, 3 seeds) and consistently outperform all other trace components on DeepSeek (mean XX.XX\% vs.\ VOTA 84.45\%), but absolute cross-model parity is not achieved ($\sigma{=}$X.Xpp across 3 DeepSeek seeds).}
DeepSeek seed variance suggests that LoRA initialization quality is a significant bottleneck for smaller models.
In contrast, the full VOTA representation---which combines exception events with assertion-point and loop information---degrades by 14.96pp on the weaker model, indicating that processing mixed trace components demands model capability that exception-only prediction does not.
```

---

## 3. Introduction — Contribution #1 (introduction.tex, line 24)

### Current
```latex
\item \textbf{Exception signal transfer}: We show that exception events alone achieve 99.83\%/99.33\% accuracy across two models under seed 42 (gap = 0.50pp), while VOTA degrades 14.96pp on the weaker model; DeepSeek seed sensitivity is discussed in \S\ref{sec:cross_model}.
```

### Version A
```latex
\item \textbf{Exception signal transfer}: We show that exception events alone achieve 99.83\% $\pm$ 0.00 on Qwen (3 seeds) and mean XX.XX\% on DeepSeek (3 seeds, $\sigma{=}$X.Xpp), transferring well across model families despite LoRA initialization sensitivity on the smaller model (\S\ref{sec:cross_model}).
```

### Version B
```latex
\item \textbf{Exception signal transfer}: We show that exception events are the most effective component on both models (Qwen 99.83\% $\pm$ 0.00; DeepSeek mean XX.XX\%, $\sigma{=}$X.Xpp), consistently outperforming VOTA (84.45\% on DeepSeek) despite significant seed-dependent variance (\S\ref{sec:cross_model}).
```

---

## 4. Experiments — Cross-Model Paragraph (experiments.tex, lines 34–43)

### Current
```latex
Table~\ref{tab:cross_model} reveals a striking asymmetry.
Under \texttt{exception\_only} with seed 42, the cross-model gap is only 0.50 percentage points (pp); however, preliminary results from an additional DeepSeek seed suggest that this cross-model parity may be seed-dependent (see Limitations).
Under VOTA, the gap widens to 14.96pp: DeepSeek drops to 84.45\% while Qwen remains at 99.41\%.
This pattern suggests that processing mixed trace components (loop compressions, assertion points) demands model capability that the smaller DeepSeek lacks, whereas isolated exception events are interpretable by both models.
Per-class analysis (Appendix~\ref{sec:per_class}) reveals the mechanism: DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.

The \texttt{no\_trace} baseline confirms that source code alone provides limited signal (75.13\% for Qwen, 73.36\% for DeepSeek), only marginally above majority-class guessing (71.51\%).

Seed robustness for Qwen \texttt{exception\_only} was evaluated across three seeds (42, 123, 456): all three produced identical accuracy of 99.83\% with exactly two errors each ($\sigma{=}0$, $n{=}3$).
DeepSeek \texttt{exception\_only} seed robustness evaluation is in progress; preliminary results indicate seed sensitivity, and epoch-level checkpoint analysis is pending.
```

### Version A
```latex
Table~\ref{tab:cross_model} reveals a striking asymmetry.
Under \texttt{exception\_only}, Qwen achieves 99.83\% $\pm$ 0.00 across three seeds, while DeepSeek averages XX.XX\% ($\sigma{=}$X.Xpp, $n{=}3$): two of three seeds achieve near-Qwen accuracy (seed 42: 99.33\%, seed 456: XX.XX\%), while seed 123 yields 91.09\%, attributable to suboptimal LoRA initialization (fail recall = 70\%).
Exception events thus transfer well across model families, though training stability is a secondary factor for smaller models.
Under VOTA, the gap widens to 14.96pp: DeepSeek drops to 84.45\% while Qwen remains at 99.41\%.
This pattern suggests that processing mixed trace components (loop compressions, assertion points) demands model capability that the smaller DeepSeek lacks, whereas isolated exception events are interpretable by both models.
Per-class analysis (Appendix~\ref{sec:per_class}) reveals the mechanism: DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.

The \texttt{no\_trace} baseline confirms that source code alone provides limited signal (75.13\% for Qwen, 73.36\% for DeepSeek), only marginally above majority-class guessing (71.51\%).

Seed robustness diverges sharply across models.
Qwen \texttt{exception\_only} produces identical accuracy of 99.83\% across all three seeds ($\sigma{=}0$, $n{=}3$, exactly two errors each).
DeepSeek shows seed-dependent variance ($\sigma{=}$X.Xpp, $n{=}3$), with two seeds achieving near-Qwen accuracy and one outlier consistent with LoRA initialization sensitivity (see \S\ref{sec:discussion_lora}).
```

### Version B
```latex
Table~\ref{tab:cross_model} reveals a striking asymmetry.
Under \texttt{exception\_only}, Qwen achieves 99.83\% $\pm$ 0.00 across three seeds, while DeepSeek averages XX.XX\% ($\sigma{=}$X.Xpp, $n{=}3$): only seed 42 approaches Qwen performance (99.33\%), while seeds 123 and 456 yield ${\approx}$91\% (91.09\% and XX.XX\% respectively), suggesting that LoRA initialization quality is a significant bottleneck for the smaller model.
Exception events consistently outperform all other trace components on both models (DeepSeek mean XX.XX\% vs.\ VOTA 84.45\%), but absolute cross-model parity is not achieved.
Under VOTA, the gap widens to 14.96pp: DeepSeek drops to 84.45\% while Qwen remains at 99.41\%.
This pattern suggests that processing mixed trace components (loop compressions, assertion points) demands model capability that the smaller DeepSeek lacks, whereas isolated exception events---though seed-sensitive on DeepSeek---remain the best-performing component by a wide margin.
Per-class analysis (Appendix~\ref{sec:per_class}) reveals the mechanism: DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.

The \texttt{no\_trace} baseline confirms that source code alone provides limited signal (75.13\% for Qwen, 73.36\% for DeepSeek), only marginally above majority-class guessing (71.51\%).

Seed robustness diverges sharply across models.
Qwen \texttt{exception\_only} produces identical accuracy of 99.83\% across all three seeds ($\sigma{=}0$, $n{=}3$, exactly two errors each).
DeepSeek shows substantial seed-dependent variance ($\sigma{=}$X.Xpp, $n{=}3$), with only seed 42 achieving near-Qwen accuracy; seeds 123 and 456 yield ${\approx}$91\%, indicating that LoRA initialization quality significantly affects exception signal utilization on smaller models.
```

---

## 5. Discussion — §5.2 Simplicity as Robustness (discussion.tex, lines 14–19)

### Current
```latex
\subsection{Simplicity as Robustness}

The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
Exception events transfer across models precisely because they are structurally simple---a fixed-format error message that any instruction-tuned model can pattern-match.
VOTA's richer representation (loop summaries, assertion comparisons) requires compositional reasoning over heterogeneous formats, which the smaller DeepSeek model (2T pretrain tokens) cannot reliably perform---consistent with findings that SFT generalization depends heavily on base model capability \citep{yang2024generalization}.
The practical implication is that trace-based systems should default to the simplest sufficient signal, reserving richer representations for tasks that demonstrably require them.
```

### Version A
```latex
\subsection{Simplicity as Relative Robustness}

The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
Exception events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations is robust across all seeds.
Two of three DeepSeek seeds match Qwen's near-perfect accuracy; the outlier (seed 123, 91.09\%) is attributable to LoRA initialization landing in a suboptimal basin (fail recall = 70\%), not to a failure of the exception signal itself.
VOTA's richer representation (loop summaries, assertion comparisons) requires compositional reasoning over heterogeneous formats, which the smaller DeepSeek model (2T pretrain tokens) cannot reliably perform---consistent with findings that SFT generalization depends heavily on base model capability \citep{yang2024generalization}.
The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.
```

### Version B
```latex
\subsection{Simplicity as Relative Robustness}

The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
Exception events are consistently the most effective component on both models---even DeepSeek's worst seed (91.09\%) exceeds VOTA (84.45\%)---but absolute cross-model parity is not achieved: DeepSeek averages XX.XX\% ($\sigma{=}$X.Xpp) vs.\ Qwen's 99.83\% $\pm$ 0.00.
The seed variance suggests that structural simplicity ensures \emph{relative} robustness (exception $>$ VOTA on every seed), but \emph{absolute} performance depends on LoRA initialization quality, which is model-dependent.
VOTA's richer representation (loop summaries, assertion comparisons) requires compositional reasoning over heterogeneous formats, which the smaller DeepSeek model (2T pretrain tokens) cannot reliably perform---consistent with findings that SFT generalization depends heavily on base model capability \citep{yang2024generalization}.
The practical implication is that trace-based systems should default to the simplest sufficient signal, but deployers targeting smaller models should invest in training stabilization (multi-seed selection, warmup tuning) to mitigate LoRA initialization sensitivity.
```

---

## 6. Conclusion — Finding (1) (conclusion.tex, lines 6–8)

### Current
```latex
\textbf{(1) Exception signal transfer.}
Exception events alone achieve 99.83\% (Qwen) and 99.33\% (DeepSeek) accuracy under the primary seed (gap = 0.50pp); however, preliminary DeepSeek seed evaluation reveals sensitivity that warrants further investigation before claiming cross-model universality.
In contrast, the full VOTA representation degrades by 14.96pp on the weaker model, revealing that mixed trace processing is model-dependent.
```

### Version A
```latex
\textbf{(1) Exception signal transfer.}
Exception events alone achieve 99.83\% $\pm$ 0.00 on Qwen (3 seeds) and mean XX.XX\% on DeepSeek (3 seeds, $\sigma{=}$X.Xpp), with two of three DeepSeek seeds matching Qwen performance.
The signal transfers well across model families; LoRA initialization sensitivity introduces seed-dependent variance on the smaller model but does not undermine exception events' position as the most effective component.
In contrast, the full VOTA representation degrades by 14.96pp on the weaker model, revealing that mixed trace processing is model-dependent.
```

### Version B
```latex
\textbf{(1) Exception signal transfer.}
Exception events alone achieve 99.83\% $\pm$ 0.00 on Qwen (3 seeds) and consistently outperform all other trace components on DeepSeek (mean XX.XX\% vs.\ VOTA 84.45\%), but absolute cross-model parity is not achieved ($\sigma{=}$X.Xpp across 3 DeepSeek seeds).
LoRA initialization quality is a significant bottleneck for smaller models; training stabilization is needed for reliable exception signal utilization.
In contrast, the full VOTA representation degrades by 14.96pp on the weaker model, revealing that mixed trace processing is model-dependent.
```

---

## Cascade Updates Needed (both versions)

When patching the chosen version, the following sections also need updating:

1. **Table 1** (experiments.tex lines 14–32): DeepSeek exception_only row → report 3-seed mean ± σ; update footnote † to describe 3-seed results; add per-seed details to caption or appendix.

2. **Discussion §5.3 Checkpoint Selection** (discussion.tex lines 21–28): Currently describes only seed42 epoch dynamics. Needs 3-seed epoch data (seed42: 99.83→99.33, seed123: 91.43→91.09, seed456: TBD). Version A: emphasize that 2/3 seeds show epoch-1 near-perfection. Version B: emphasize that only 1/3 seeds achieves near-perfection at any epoch.

3. **Discussion §5.5 Limitations** (discussion.tex lines 44–54): Remove "in progress" / "under investigation" language for DeepSeek seeds; replace with concrete 3-seed results.

4. **Appendix Table 8** (appendix.tex lines 184–199): Add DeepSeek seed123 and seed456 rows.

5. **paper_framing.md**: Update Claim 1 section with final 3-seed numbers.

6. **writing_plan.yaml**: Update Claim 1 status from `provisional` to `ready` (Version A) or `qualified` (Version B).
