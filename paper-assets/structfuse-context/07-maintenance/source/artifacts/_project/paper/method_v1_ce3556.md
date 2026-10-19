# §3 Method

## §3.1 Problem Formulation

We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.

We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files. Concretely, we optimize $\theta$ such that for all $f^+ \in \mathcal{F}^+_q$ and $f^- \in \mathcal{F} \setminus \mathcal{F}^+_q$:

$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$

where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.

The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. Random negatives are often too easy, providing weak gradient signal \cite{chen2020simclr}. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.

## §3.2 StructFuse Pipeline

Our pipeline consists of three stages: (1) structural graph extraction via static analysis, (2) training data construction with strategy-specific negative mining, and (3) contrastive fine-tuning of a pretrained code encoder.

**CodeQL Extraction.** We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. Specifically, we define taint-tracking queries that trace data flow from designated sources to sinks, crossing function call boundaries. This yields a set of data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file.

We set a scope bound on the analysis depth to ensure tractability: queries that exceed a predefined step limit are terminated. In practice, this achieves 0\% timeout rate across 123 out of 131 repositories in our dataset.

**Structural Connectivity Graph.** From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. This graph captures inter-procedural structural relationships between files—two files are connected if data flows between them across function call boundaries.

A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.

**Structural Coverage.** At full scale, 78\% of files connected in $G$ are non-gold files (i.e., structurally related but not in the patch), providing a rich pool for structure-grounded negative mining. The remaining files either lack data-flow connections or belong to isolated modules.

## §3.3 Training Objective

**Contrastive Loss.** We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$, the loss is:

$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$

where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query. Our framework supports distance-weighted positive scores via per-sample weights $w_i = \exp(-\alpha \cdot d_i)$, where $d_i$ is the data-flow path distance from query to positive and $\alpha = 1.0$. In practice, the training data assigns a uniform distance of $d = 1$ to all positives, yielding a constant weight $w = e^{-1}$ across all samples. Since this scales all per-sample losses equally, the optimization is equivalent to standard unweighted InfoNCE.

**Encoder Architecture.** We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—which differ in pretraining objectives (Fill-in-the-Middle vs. multi-task including Fill-in-the-Middle) and exhibit distinct representation geometries (§5). We apply mean pooling over non-padding positions of the last hidden layer to obtain fixed-dimensional representations, followed by L2 normalization. Each encoder is augmented with a two-layer MLP projection head (Linear→GELU→Linear) that maps the pooled hidden state to a 256-dimensional embedding space.

**Parameter-Efficient Fine-Tuning.** We apply LoRA \cite{hu2022lora} to the query and value projection matrices ($W_q$, $W_v$) of each attention layer with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated. We use AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10\% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2048 tokens. We train for 2 epochs with early stopping (patience=2). An initial exploratory seed ($s_{42}$) uses 3 epochs to provide a complete overfitting curve; subsequent seeds use 2 epochs based on observed overfitting after epoch 1 (see §4). Evaluation is performed every 500 steps.

**Dual Checkpoint Selection.** We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement.

## §3.4 Negative Mining Strategies

We compare three negative mining strategies that span a spectrum from uninformed to structure-grounded selection.

**Random Mining.** For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$. This serves as the baseline: negatives are unbiased but typically easy, as randomly chosen files are unlikely to share topical or structural similarity with the query.

**Embedding-Distance Mining.** We compute embeddings for all files and queries using the frozen pretrained encoder $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we retrieve the $K$ non-gold files with highest cosine similarity to $q$ in the pretrained embedding space:

$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$

This selects files that the pretrained encoder already considers similar to the query—hard negatives that force the fine-tuned encoder to learn finer distinctions. Critically, this mining is **static**: embeddings are computed once from $E_{\theta_0}$ and not refreshed during training, avoiding the computational overhead and instability of online re-mining \cite{xiong2021ance}.

**Dataflow-Aware Mining.** This strategy leverages the structural connectivity graph $G$ from §3.2 to select negatives that are textually similar but structurally disconnected from the query context. Formally, for query $q$ with associated gold files $\mathcal{F}^+_q$, we define the reachability set $\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$, where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:

$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$

That is, we select the most similar non-gold files that are also **structurally unreachable** from the gold files in the data-flow graph. The intuition is that these files represent a category of particularly informative negatives: they appear relevant based on surface-level textual features (variable names, API patterns, shared imports) yet lack the inter-procedural data-flow connections that characterize true functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.

**Difficulty Gradient.** The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are harder (high pretrained similarity, no structural constraint). Dataflow-aware negatives add a structural filter on top of embedding distance, selecting a subset that is simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives (§5).

For repositories where the structural graph $G$ has insufficient coverage (fewer than $K$ structurally disconnected candidates above a similarity threshold), the dataflow-aware strategy falls back to embedding-distance mining. This fallback applies to approximately 66\% of training instances, which lack structural connectivity data and therefore cannot supply structurally disconnected candidates. We analyze the fallback stratum separately in stratified evaluation (§5).
