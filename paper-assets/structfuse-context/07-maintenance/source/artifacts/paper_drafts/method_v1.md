# 3. Method

## 3.1 Problem Formulation

We formulate file-level code retrieval as a contrastive learning problem. Given a repository $\mathcal{R}$ containing source files, a query $q$ consists of a buggy function or file paired with its issue description. A positive file $p \in \mathcal{R}$ is the gold patch target---a file modified to resolve the issue. All remaining non-query, non-gold files constitute the negative candidate pool.

We train an encoder $E: \mathcal{F} \to \mathbb{R}^d$ such that $\text{sim}(E(q), E(p)) \gg \text{sim}(E(q), E(n))$ for any negative $n$. Training minimizes the InfoNCE loss \cite{oord2018representation}, also known as NT-Xent \cite{chen2020simclr}:

$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E(q), E(p)) / \tau)}{\exp(\text{sim}(E(q), E(p)) / \tau) + \sum_{i=1}^{K} \exp(\text{sim}(E(q), E(n_i)) / \tau)}$$

where $\tau$ is a learnable temperature parameter and $\{n_1, \ldots, n_K\}$ are $K$ negatives selected by a mining strategy. The central question is how the choice of mining strategy affects retrieval quality, and whether structural code information provides signal beyond embedding similarity.

## 3.2 Structural Extraction Pipeline

To enable structure-aware negative mining, we extract inter-procedural data-flow graphs from repository snapshots using CodeQL \cite{avgustinov2016ql}. For each query function $q$, we construct a CodeQL database from the repository at the relevant commit, then perform 2-hop bounded taint-tracking analysis to identify all files reachable from $q$ through inter-procedural data-flow paths. This captures cross-function semantic relationships---for instance, a utility function that transforms data passed from a source through multiple call boundaries.

A file $f$ is \emph{connected} to query $q$ if $f$ is reachable from $q$ via inter-procedural data-flow paths in the structural graph $G$; otherwise $f$ is \emph{disconnected}. Connected files include both gold targets and non-gold files that participate in the query's data-flow neighborhood (e.g., shared utility modules, intermediate processing functions).

When CodeQL analysis fails due to missing build configurations, we fall back to beniget \cite{guelton2019beniget}, a Python AST-based def-use analyzer providing intra-module data-flow coverage. In practice, beniget fallback triggered for 764 instances (4.8\% of successfully extracted), of which 20 yielded non-empty structural data; CodeQL accounts for the remaining 99.9\% of structural extractions. At full scale, the pipeline successfully extracts for 15,897 out of 44,173 instances across 123 repositories, with 0\% CodeQL analysis timeout. Structural connectivity is available for 34.3\% of instances (15,153 with non-empty structural data out of 44,173); among those, 78\% contain connected files beyond the gold target, confirming that connectivity captures functional relevance beyond gold-file identity. We frame this pipeline as a practical enabling tool (\S5), not a standalone contribution.

## 3.3 Negative Mining Strategies

We compare three strategies spanning different dimensions of negative difficulty. All strategies share a common two-stage protocol: first, a pool of up to 50 candidate negatives is constructed according to the strategy (in practice, pool sizes range from 2 to 50 with a mean of 31--34 depending on strategy, as small repositories may contain fewer eligible candidates); then $K{=}7$ negatives are randomly sampled from this pool per training instance. This decouples strategy-specific selection from stochastic sampling effects.

**Random.** Negatives are drawn uniformly at random from all non-positive files within the same repository. This serves as the no-signal baseline, reflecting the standard approach in dense retrieval \cite{karpukhin2020dpr}.

**Embedding-distance.** For each encoder, we use its own pretrained weights (frozen; not updated during training) to compute cosine similarity between the query and all non-positive repository files. The 50 most similar non-positive files form the candidate pool. These are semantic near-misses: files that \emph{appear} relevant to the pretrained encoder but are not gold targets. This strategy incurs zero additional cost beyond the one-time offline embedding computation, as the pretrained encoder is already available.

**Dataflow-aware.** This strategy combines structural filtering with lexical ranking. First, all structurally connected files are excluded from the candidate pool---specifically, all files in $R_G(q)$ (reachable via inter-procedural data-flow paths and call-graph edges). This ensures negatives are structurally disconnected from the query. Second, the remaining disconnected files are ranked by BM25 score \cite{robertson2009bm25} ($k_1{=}1.2$, $b{=}0.75$) in descending order, and the top-50 form the candidate pool. Formally:

$$\text{pool}_{\text{df}}(q) = \underset{x \in \mathcal{D} :\ x \notin R_G(q) \,\wedge\, x \notin \text{gold}(q)}{\text{top-}50}\ \text{BM25}(q, x)$$

where $R_G(q)$ denotes files reachable from $q$ in structural graph $G$. Structural information serves exclusively as a \emph{filter} (determining which files to exclude), while BM25 provides the \emph{ranking} signal among remaining candidates. The rationale is that high-BM25, structurally-disconnected files are lexically similar but functionally unrelated---a hypothesized difficulty dimension distinct from embedding distance.

## 3.4 Training Setup

**Encoders.** We use two decoder-only code language models with distinct pretraining: Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{lozhkov2024starcoder2}. These encoders differ in pretraining corpora and representation geometry, enabling examination of whether mining strategy effectiveness interacts with encoder properties.

**Fine-tuning.** We apply LoRA \cite{hu2022lora} adaptation with rank $r{=}16$, scaling factor $\alpha{=}32$, and dropout 0.05, targeting query and value projection matrices ($W_q$, $W_v$) in every attention layer. Input sequences are truncated to 2,048 tokens. Following prior work showing mean pooling outperforms [CLS] and last-token alternatives for code representations \cite{reimers2019sentencebert, zhang2024codesage}, we apply mean pooling over non-padding positions followed by L2 normalization, then project through a two-layer MLP ($2048 \to \text{GELU} \to 256$) to a 256-dimensional embedding space.

**Optimization.** We use AdamW (lr=$2 \times 10^{-5}$, cosine annealing, warmup ratio 0.1, weight decay 0.01) with gradient checkpointing and gradient clipping (max norm 1.0). The InfoNCE temperature is initialized to $\tau{=}0.07$ and learned during training. Each training instance consists of 1 positive and $K{=}7$ negatives sampled from the candidate pool, with a per-device batch size of 8. One seed per configuration (seed 42) trains for 3 epochs without early stopping to provide overfitting diagnostics; the remaining seeds (43, 44) train for 2 epochs with early stopping (patience 2, evaluated every 500 steps). We save two checkpoints per run: best by validation loss and best by validation R@1.

## 3.5 Evaluation Protocol

**Retrieval metric.** We evaluate on a pool-based retrieval task: given a query, the model ranks a candidate pool of 50 files by cosine similarity. The primary metric is Recall@1 (R@1)---whether the top-ranked file is a gold patch target.

**Checkpoint selection.** We report the best-by-R@1 checkpoint as the primary result, selected by validation R@1. Fixed-checkpoint comparisons are reported as a robustness check to confirm that strategy rankings are not artifacts of checkpoint selection.

**Data splits.** For each seed, we perform per-repository stratified splitting to produce $\sim$11,300 training and $\sim$3,000 validation instances, ensuring repository-level distribution is preserved across partitions. All strategies share the same splits per seed.

**Statistical rigor.** Each encoder $\times$ strategy combination is trained with 3 random seeds (42, 43, 44), yielding 18 total runs (2 encoders $\times$ 3 strategies $\times$ 3 seeds). We report bootstrap 95\% confidence intervals for all comparisons.

**Downstream evaluation.** To validate that retrieval improvements transfer to end-to-end performance, we evaluate on SWE-bench Lite \cite{jimenez2024swebench} (300 instances) with an LLM-based repair agent. The retriever provides file-level context, measuring whether improved retrieval translates to higher issue resolution rates.
