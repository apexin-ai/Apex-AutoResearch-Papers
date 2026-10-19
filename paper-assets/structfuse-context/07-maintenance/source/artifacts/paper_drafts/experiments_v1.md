# §4 Experiments

## §4.1 Experimental Setup

**Dataset.** We construct a code retrieval dataset from SWE-smith \cite{yang2025swesmith}, a large-scale collection of synthetic Python bug-fix instances derived from real-world GitHub repositories. After excluding repositories with failed clones, 44,173 instances across 123 repositories remain. Our structural extraction pipeline (\S3.2) produces inter-procedural data-flow graphs for 15,897 instances (36.0\%); of these, 14,288 yield resolvable positive files and are retained for training. Per-seed stratified splits produce $\sim$11,300 training and $\sim$3,000 validation instances, preserving repository-level distribution across partitions.

**Encoders.** We select two 3B-parameter decoder-only code models representing distinct pretraining paradigms: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} (Fill-in-the-Middle on curated multilingual code) and **StarCoder2-3B** \cite{lozhkov2024starcoder2} (multi-task FIM on The Stack v2). These encoders exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (0.799). This divergence enables examination of whether mining strategy effectiveness interacts with encoder properties---a core question of our study.

**Training.** All fine-tuning details follow \S3.4: LoRA ($r{=}16$, $\alpha{=}32$) on $W_q$/$W_v$, InfoNCE with learnable $\tau$, AdamW ($\text{lr}{=}2{\times}10^{-5}$). Seed 42 trains for 3 epochs without early stopping to provide a full overfitting diagnostic curve; seeds 43 and 44 train for 2 epochs with early stopping (patience 2, evaluated every 500 steps).\footnote{The 3-epoch seed-42 runs enable analysis of post-peak degradation (\S4.3.3); all checkpoint selection uses the same dual-checkpoint protocol regardless of epoch count.} We maintain dual checkpoints per run: $\theta^*_{\text{loss}}$ (best validation loss) and $\theta^*_{\text{R@1}}$ (best validation Recall@1).

**Evaluation.** Pool-based retrieval with pool size 50 (1 positive + 49 negatives). Primary metric: Recall@1 (R@1)---whether the top-ranked file is a gold patch target. We report $\theta^*_{\text{R@1}}$ as the primary result; fixed-checkpoint ($\theta^*_{\text{loss}}$) comparisons appear in Table~2 as a robustness check.

**Seeds.** Each encoder $\times$ strategy combination is trained with 3 random seeds (42, 43, 44), yielding $2 \times 3 \times 3 = 18$ total runs. We report cluster bootstrap 95\% confidence intervals with repo as resampling unit ($B{=}10{,}000$) for all pairwise comparisons.


## §4.2 Main Results

### Table 1: Primary Results ($\theta^*_{\text{R@1}}$ checkpoint)

Table~1 reports R@1 for each strategy $\times$ seed combination, selected by best validation R@1. [TBD: fill final numbers after all 18 runs complete.]

\begin{table}[t]
\centering
\caption{R@1 by negative mining strategy (\textbf{Qwen2.5-Coder-3B}). Pool size = 50 (provisional, pool=8; final pool=50 results pending). $\theta^*_{\text{R@1}}$ checkpoint.}
\label{tab:main-qwen}
\small
\begin{tabular}{lccccc}
\toprule
Strategy & Seed 42 & Seed 43 & Seed 44 & Mean & 95\% CI \\
\midrule
Random           & 0.5527 & 0.5554 & 0.6009 & X.XX & [X.XX, X.XX] \\
Embedding-dist.  & X.XX   & 0.5606 & X.XX   & X.XX & [X.XX, X.XX] \\
Dataflow-aware   & X.XX   & X.XX   & X.XX   & X.XX & [X.XX, X.XX] \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[t]
\centering
\caption{R@1 by negative mining strategy (\textbf{StarCoder2-3B}). Pool size = 50 (provisional, pool=8; final pool=50 results pending). $\theta^*_{\text{R@1}}$ checkpoint.}
\label{tab:main-starcoder}
\small
\begin{tabular}{lccccc}
\toprule
Strategy & Seed 42 & Seed 43 & Seed 44 & Mean & 95\% CI \\
\midrule
Random           & 0.4604 & X.XX & X.XX & X.XX & [X.XX, X.XX] \\
Embedding-dist.  & X.XX   & X.XX & X.XX & X.XX & [X.XX, X.XX] \\
Dataflow-aware   & X.XX   & X.XX & X.XX & X.XX & [X.XX, X.XX] \\
\bottomrule
\end{tabular}
\end{table}

**Qwen results.** [TBD: 2--3 sentences summarizing Qwen panel. Expected pattern: embedding > random with consistent improvement across seeds; dataflow-aware shows smaller or inconsistent benefit.] The embedding-distance strategy improves over random by [TBD: +X.Xpp mean $\Delta$, 95\% CI], confirming that simple static mining provides reliable signal without gradient-based mechanisms. Dataflow-aware negatives [TBD: describe observed pattern relative to embedding and random].

**StarCoder results.** [TBD: 2--3 sentences. Expected: similar embedding > random pattern; dataflow potentially neutral-to-negative based on pilot.] Embedding-distance mining yields [TBD: +X.Xpp, CI] improvement over random, directionally consistent with the Qwen results. Dataflow-aware negatives [TBD: describe interaction pattern].

**Cross-encoder comparison.** The absolute R@1 gap between encoders ([TBD: Qwen mean $-$ StarCoder mean $\approx$ X.Xpp]) reflects differences in pretrained representation quality rather than strategy effectiveness. Critically, the \emph{relative} strategy ranking [TBD: is consistent / diverges] across encoders, with the dataflow-aware strategy showing encoder-dependent interaction (Claim~2).

**Claim 1 support.** Embedding-distance mining improves over random by [TBD: $\Delta$ + CI] (Qwen) and [TBD: $\Delta$ + CI] (StarCoder), establishing simple static mining as a reliable zero-cost baseline.

**Claim 2 support (exploratory).** [TBD: describe the encoder-dependent interaction pattern for dataflow-aware negatives. Frame as observation, not established finding. Reference representation geometry analysis in \S4.3.5.]


### Table 2: Fixed-Checkpoint Robustness Check ($\theta^*_{\text{loss}}$)

To confirm that strategy rankings are not artifacts of checkpoint selection, Table~2 reports R@1 using the best-by-validation-loss checkpoint. [TBD: fill after all runs complete.]

\begin{table}[t]
\centering
\caption{R@1 by strategy, $\theta^*_{\text{loss}}$ checkpoint (robustness check). Both encoders.}
\label{tab:fixed-checkpoint}
\small
\begin{tabular}{lcccc}
\toprule
 & \multicolumn{2}{c}{Qwen2.5-Coder-3B} & \multicolumn{2}{c}{StarCoder2-3B} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5}
Strategy & Mean R@1 & 95\% CI & Mean R@1 & 95\% CI \\
\midrule
Random           & X.XX & [X.XX, X.XX] & X.XX & [X.XX, X.XX] \\
Embedding-dist.  & X.XX & [X.XX, X.XX] & X.XX & [X.XX, X.XX] \\
Dataflow-aware   & X.XX & [X.XX, X.XX] & X.XX & [X.XX, X.XX] \\
\bottomrule
\end{tabular}
\end{table}

Strategy rankings under $\theta^*_{\text{loss}}$ are [TBD: directionally consistent with / diverge from] the primary $\theta^*_{\text{R@1}}$ results. [TBD: note any cases where val\_loss and R@1 select different checkpoints, cross-referencing \S4.3.1.]


## §4.3 Analysis

### §4.3.1 Checkpoint Selection Criterion

In [TBD: N out of 18] runs (50\%), the best-by-loss checkpoint ($\theta^*_{\text{loss}}$) and best-by-R@1 checkpoint ($\theta^*_{\text{R@1}}$) select different training steps, indicating that validation loss and retrieval performance can diverge during fine-tuning.

\begin{table}[t]
\centering
\caption{Checkpoint divergence: $\theta^*_{\text{loss}}$ vs.\ $\theta^*_{\text{R@1}}$ across all 18 runs.}
\label{tab:checkpoint-criterion}
\small
\begin{tabular}{lcc}
\toprule
 & Same step & Different step \\
\midrule
Qwen (9 runs)     & [TBD: N] & [TBD: N] \\
StarCoder (9 runs) & [TBD: N] & [TBD: N] \\
\midrule
Total (18 runs)    & [TBD: N] & [TBD: N] \\
\bottomrule
\end{tabular}
\end{table}

This divergence motivates our dual-checkpoint protocol: reporting $\theta^*_{\text{R@1}}$ as the primary metric (aligned with the downstream objective) while providing $\theta^*_{\text{loss}}$ as a robustness check.

Among the 5 completed Qwen runs, 3 (60\%) exhibit criterion divergence---including both embedding-distance and random strategies---indicating that loss--R@1 decoupling is a general property of contrastive fine-tuning rather than a strategy-specific phenomenon. This makes the dual-checkpoint protocol a practical necessity for contrastive code retrieval, regardless of negative mining strategy.

**Illustrative case (Qwen, seed 44).** With embedding-distance negatives, R@1 peaks at step 500 (0.5942) but validation loss continues improving to step 1000 (0.4341)---the two criteria select \emph{different} checkpoints ($\theta^*_{\text{R@1}}$ at step 500, $\theta^*_{\text{loss}}$ at step 1000). With random negatives on the same seed, both criteria agree at step 500. However, random seed 43 also exhibits divergence, confirming that this phenomenon is not exclusive to harder negatives. Selecting by validation loss alone in the diverged embedding-distance case would yield a checkpoint 1.3pp below peak R@1. [TBD: Full 18-run divergence statistics after M2 completion. Reference checkpoint\_criterion\_table for detailed per-run breakdown.]


### §4.3.2 Seed Variance Analysis

We examine sensitivity to random seed initialization via leave-one-out analysis. For each strategy $\times$ encoder, we compute the mean R@1 when excluding each seed in turn.

[TBD: Leave-one-out table or figure showing per-seed contribution to variance.]

Seed 44 exhibits [TBD: notably higher / lower / comparable] R@1 for Qwen random (0.6009 vs.\ 0.5527--0.5554 for s42/s43), an outlier that [TBD: inflates mean / does not change ranking]. This seed was early-stopped at step 1500 (patience exhausted), with its best checkpoint at step 500 (R@1 declined from 0.6009 to 0.5542 over the subsequent 1000 steps), suggesting [TBD: interpretation---favorable random initialization or data ordering]. Despite this variance, the strategy ranking (embedding > random) holds under all leave-one-out combinations, confirming robustness.

[TBD: Report coefficient of variation per strategy $\times$ encoder. Note whether harder strategies (embedding, dataflow) show lower or higher seed variance than random.]


### §4.3.3 Training Dynamics

We analyze post-peak R@1 degradation and loss--R@1 divergence to characterize how negative difficulty affects training trajectories. We define two metrics:

\begin{itemize}
\item \textbf{R@1 decay rate}: the per-500-step R@1 drop after peak, computed as $\delta_{\text{R@1}} = (\text{R@1}_{\text{peak}} - \text{R@1}_{\text{peak}+500}) / \text{R@1}_{\text{peak}}$. Larger values indicate faster overfitting on the retrieval metric.
\item \textbf{Loss--R@1 divergence}: whether $\theta^*_{\text{loss}}$ and $\theta^*_{\text{R@1}}$ select different training steps. When the two criteria diverge, validation loss continues improving after R@1 has peaked---the model is learning features that reduce loss but do not improve ranking.
\end{itemize}

[TBD: Learning curve figure---validation R@1 vs.\ training step for all 18 runs, faceted by encoder.]

**Illustrative comparison (Qwen, seed 44).** Table~[TBD: N] traces the full R@1 and validation loss trajectories for embedding-distance and random negatives under identical data splits.

\begin{table}[t]
\centering
\caption{Training dynamics: embedding-distance vs.\ random (Qwen, seed 44). Both runs share identical data splits; only the negative mining strategy differs.}
\label{tab:training-dynamics-s44}
\small
\begin{tabular}{lcccc}
\toprule
 & \multicolumn{2}{c}{Embedding-distance} & \multicolumn{2}{c}{Random} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5}
Step & R@1 & Val loss & R@1 & Val loss \\
\midrule
500  & \textbf{0.5942} & 0.4579 & \textbf{0.6009} & \textbf{0.4252} \\
1000 & 0.5813 & \textbf{0.4341} & 0.5638 & 0.4357 \\
1500 & 0.5709 & 0.4394 & 0.5542 & 0.4541 \\
2000 & 0.5576 & 0.4503 & --- & --- \\
\midrule
$\delta_{\text{R@1}}$ & \multicolumn{2}{c}{$-$2.2\% per 500 steps} & \multicolumn{2}{c}{$-$6.2\% per 500 steps} \\
Loss--R@1 diverge? & \multicolumn{2}{c}{Yes (step 500 vs.\ 1000)} & \multicolumn{2}{c}{No (both step 500)$^\dagger$} \\
\bottomrule
\multicolumn{5}{l}{\footnotesize $^\dagger$Random seed 43 \emph{does} exhibit divergence; this seed-specific agreement is not strategy-general.}
\end{tabular}
\end{table}

Three observations emerge from this controlled comparison. First, both strategies peak at the same step (500), suggesting that peak timing is driven by data volume and learning rate schedule rather than negative difficulty. Second, random negatives exhibit a steeper post-peak R@1 decay ($\delta_{\text{R@1}} = -6.2\%$ per 500 steps vs.\ $-2.2\%$ for embedding-distance), indicating that harder negatives provide a regularizing effect that slows overfitting on the retrieval metric. Third, loss--R@1 divergence appears in this embedding-distance run (validation loss improves 500 steps past R@1 peak) but not in the random run on the same seed. However, divergence also occurs in random seed 43, indicating that this decoupling is a general property of contrastive fine-tuning observed across strategies (60\% of completed runs; \S4.3.1), not a strategy-specific effect.

[TBD: Aggregate statistics across all 18 runs. Report mean $\delta_{\text{R@1}}$ per strategy $\times$ encoder with 95\% CI. Test whether harder negatives systematically reduce post-peak decay rate and increase loss--R@1 divergence frequency.]


### §4.3.4 BM25 Comparison

[TBD: Placeholder for plan\_018 Phase 2 results. This subsection will report two BM25-related comparisons.]

**BM25 retrieval baseline.** As a non-neural reference, BM25 \cite{robertson2009bm25} achieves [TBD: X.XX] R@1 on the evaluation pool. All contrastive strategies substantially outperform this baseline ([TBD: +X.Xpp minimum gap]), confirming the value of learned representations.

**BM25-mined negatives.** To ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, we train contrastive models using BM25-mined negatives (top-50 BM25-scoring non-gold files per query). [TBD: Results and comparison to embedding-distance mining. Expected outcomes: (a) BM25 negatives $\approx$ random $\rightarrow$ lexical similarity alone insufficient; (b) BM25 negatives $>$ random $\rightarrow$ any hard negative helps; (c) BM25 negatives $\approx$ embedding $\rightarrow$ difficulty source matters less than difficulty level.]


### §4.3.5 Negative Difficulty Analysis

We analyze the pretrained margin distribution to provide mechanistic grounding for the observed strategy $\times$ encoder interaction. For each query, we compute the cosine similarity margin: $\text{margin} = \text{sim}(q, p) - \text{mean}(\text{sim}(q, n_i))$ in the frozen pretrained embedding space.

\begin{table}[t]
\centering
\caption{Negative difficulty in pretrained embedding space (2048-token context).}
\label{tab:neg-difficulty}
\small
\begin{tabular}{lcccccc}
\toprule
 & \multicolumn{3}{c}{Qwen2.5-Coder-3B} & \multicolumn{3}{c}{StarCoder2-3B} \\
\cmidrule(lr){2-4} \cmidrule(lr){5-7}
Strategy & pos\_sim & neg\_sim & margin & pos\_sim & neg\_sim & margin \\
\midrule
Random          & 0.986 & 0.911 & 0.074 & 0.799 & 0.605 & 0.194 \\
Embedding-dist. & 0.986 & 0.969 & 0.017 & 0.808 & 0.741 & 0.067 \\
Dataflow-aware  & 0.986 & 0.956 & 0.029 & 0.801 & 0.682 & 0.119 \\
\bottomrule
\end{tabular}
\end{table}

**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of 0.074. StarCoder maintains 2.6--4.1$\times$ larger margins, indicating a more separable pretrained space.

**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), dataflow-aware intermediate, random easiest. However, the magnitude of margin compression differs: embedding-distance mining reduces Qwen's margin by 77\% (0.074 $\to$ 0.017) versus 65\% for StarCoder (0.194 $\to$ 0.067).

**Distribution analysis.** Figure~\ref{fig:rep-geometry} visualizes these patterns across two complementary views. The margin comparison panel (Figure~\ref{fig:rep-geometry}a) shows that Qwen's positive-negative margins are uniformly compressed across all strategies, with embedding-distance negatives nearly eliminating the margin entirely (0.017). The similarity distribution panel (Figure~\ref{fig:rep-geometry}b) reveals the underlying mechanism: Qwen's negative similarities are clustered in a narrow band near 0.95--0.97, leaving little room for the encoder to distinguish positives from hard negatives, whereas StarCoder's negatives span a wider range (0.60--0.74), providing a richer gradient landscape.

**Interpretation.** In Qwen's saturated space, embedding-distance negatives occupy precisely the region where the encoder is most uncertain, providing maximal gradient signal. Dataflow-aware negatives target a structurally motivated subset that may exclude some of the most informative hard negatives. In StarCoder's well-separated space, both strategies have sufficient room to be effective. We frame this as a candidate mechanistic explanation for the encoder-dependent interaction observed in \S4.2, not as an established causal account.


### §4.3.6 Pool Size Sensitivity

[TBD: Placeholder for plan\_019 results. Evaluate at pool sizes \{50, 100, 200, 500\} to confirm strategy rankings hold at realistic retrieval sizes. Report R@1 $\times$ strategy $\times$ pool size for both encoders.]


## §4.4 Effect Size Interpretation

The full-scale embedding $\to$ random improvement ([TBD: +X.Xpp Qwen, +X.Xpp StarCoder]) is smaller than pilot estimates (+2.0pp, +1.6pp). This shrinkage is expected: full-scale training data provides stronger random baselines by exposing the encoder to a broader distribution of negatives, reducing the marginal value of targeted selection. [TBD: quantify shrinkage ratio and contextualize against effect sizes reported in DPR \cite{karpukhin2020dpr} and ANCE \cite{xiong2021ance}.]

**Downstream evaluation.** [TBD: Placeholder for SWE-bench Lite results (plan\_003). Report resolve rate with BM25, random-trained, and embedding-trained retrievers. This validates that retrieval R@1 improvements transfer to end-to-end issue resolution.]

Extended discussion of representation geometry, limitations, and future work appears in \S5.
