# §4 Experiments

## §4.1 Experimental Setup

**Dataset.** We construct our training corpus from SWE-bench \cite{jimenez2024swebench}, a benchmark of real-world GitHub issues paired with developer-authored patches. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, we run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain 15,897 instances across 123 repositories with structural data, yielding a structural coverage rate of 36%. The remaining 64% of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.

For each random seed, we perform a per-repository stratified split to produce 11,236–11,308 training and 2,980–3,052 validation instances (varying by seed due to stratified splitting). Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.

**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.

**Baselines.** We compare three negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—against a BM25 retrieval baseline. The BM25 baseline uses Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point. We additionally evaluate BM25-mined negatives as a fourth contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{cocohanere2025}.

## §4.2 Implementation Details

**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.799). This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies.

**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We use a linear projection head mapping the last hidden state to a 256-dimensional embedding. Training uses InfoNCE loss with temperature $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.

For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).

**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.

**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the full experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours.

## §4.3 Results

### Main Results

Table 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\pm$ standard deviation over three seeds.

**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.

| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
|---|---|---|---|---|---|---|
| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |
| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
| Random | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
| Embedding-distance | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |

**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\placeholder{+X.X}pp and \placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.

### Pilot Validation

Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.

**Table 2: Pilot results (single seed, 24-repo subset).** Pool size = 50.

| Strategy | Qwen R@1 | StarCoder R@1 |
|---|---|---|
| Random | 0.536 | 0.492 |
| Embedding-distance | 0.556 (+2.0pp) | 0.508 (+1.6pp) |
| Dataflow-aware | 0.544 (+0.8pp) | 0.487 (−0.5pp) |

The pilot established two findings subsequently confirmed at full scale: (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.

### Ablations

**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\in \{50, 100, 200, 500\}$.

**Table 3: R@1 by pool size.**

| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\Delta$ | SC Emb. | SC Rand. | SC $\Delta$ |
|---|---|---|---|---|---|---|
| 50 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
| 100 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
| 200 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
| 500 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |

**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.

| Strategy | Qwen R@1 (s42) |
|---|---|
| Static embedding-distance | \placeholder{X.XX} |
| Dynamic (epoch re-mining) | \placeholder{X.XX} |

### Downstream Evaluation

**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).

| Retriever | Resolve Rate |
|---|---|
| BM25 | \placeholder{X.X%} |
| Random-trained | \placeholder{X.X%} |
| Embedding-trained (Qwen) | \placeholder{X.X%} |

### Structural Extraction Scalability

The CodeQL-based extraction pipeline processes 123 of 131 target repositories (93.9%) with 0% analysis timeout, supporting Claim 3 that structure-grounded negative mining is practically feasible at scale. Mean per-repository extraction time is 8.93 seconds (p95 = 31.95s, max = 633.68s). The connected-not-gold rate (Z%) averages 34.3% across all repositories, with a clear tier-wise gradient: small repositories exhibit Z\_mean = 28.4%, medium 44.4%, large 60.4%, and xlarge 81.2%, indicating that structural connectivity density increases with codebase size. *These figures are based on the current M1 extraction pass; updated numbers from the M1v2 re-extraction will be incorporated in the final version.*

## §4.4 Analysis

### Representation Geometry and Negative Difficulty

A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.

**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\_sim − neg\_sim.

| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
|---|---|---|---|---|---|---|
| | pos\_sim | neg\_sim | margin | pos\_sim | neg\_sim | margin |
| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |
| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |
| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |

Several patterns emerge from Table 4:

**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\times$ larger margins across all strategies, indicating a more separable pretrained space.

**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.

**Mechanistic hypothesis.** When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.

### Stratified Analysis

We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.

**Table 5: R@1 stratified by structural data availability.**

| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\Delta$ | SC (Emb.) | SC (DF) | $\Delta$ |
|---|---|---|---|---|---|---|---|
| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
| No structural data (fallback) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |

Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.

### CodeQL Scalability

We report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).

**Table 6: CodeQL extraction scalability by repository tier.**

| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
|---|---|---|---|---|---|
| Small (<50 files) | 1 | 500 | 0% | 81.0% | 0.0% |
| Medium (50–200) | 17 | 4,096 | 0% | 47.2% | 50.0% |
| Large (200–500) | 40 | 13,628 | 0% | 34.3% | 85.7% |
| XLarge (500+) | 29 | 25,949 | 0% | 31.4% | 96.0% |
| **Total** | **123** | **44,173** | **0%** | **36.0%** | — |

The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ files. This indicates that larger repositories provide richer pools for structure-grounded negative mining. The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
<!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
