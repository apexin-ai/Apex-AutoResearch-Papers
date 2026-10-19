# §3 Method

## §3.1 Problem Formulation

We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.

We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:

$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$

where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.

The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.

## §3.2 Structural Information Extraction

### CodeQL Bounded Data-Flow Analysis

We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:

- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.
- **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.

### File-Level Reachability

From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.

A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.

At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].

### Beniget Fallback

For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].

### Coverage Statistics

The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:

| Metric | Value |
|--------|-------|
| Timeout rate | 0% (all repository tiers) |
| Repository coverage | 123/131 (93.9%) |
| Structural data rate | 34% of instances |
| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |

The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.

## §3.3 Structure-Aware Negative Mining

We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.

### Random Negatives

For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$:

$$f^-_{\text{rand}} \sim \text{Uniform}(\mathcal{F} \setminus \mathcal{F}^+_q), \quad |\{f^-_{\text{rand}}\}| = K$$

This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.

### Embedding-Distance Negatives

We compute embeddings for all files and queries using $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:

$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$

These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\theta_0}$ and avoids the instability and computational overhead of online re-mining \cite{xiong2021ance}.

### Dataflow-Aware Negatives

This strategy combines embedding distance with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:

$$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$

where $E^*$ denotes the transitive closure of $G$. The dataflow-aware negatives are:

$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$

These files are simultaneously similar in the embedding space (hard) and structurally disconnected in the data-flow graph (informative). They represent a category of false positives of textual similarity: files that appear relevant based on surface features (shared imports, API patterns, variable names) but lack the inter-procedural data-flow connections that characterize functional relatedness. By training the encoder to distinguish these cases, we aim to push the embedding space toward capturing structural semantics beyond lexical overlap.

For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).

### Difficulty Gradient

The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives select a subset of hard negatives that are additionally structurally disconnected—simultaneously similar in text and disconnected in structure. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).

### Relationship to BM25 Baselines

In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].

## §3.4 Contrastive Fine-tuning

### InfoNCE Loss

We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$:

$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$

where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].

### LoRA Fine-tuning Setup

We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—using LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.

Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].

Training uses AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.

### Dual Checkpoint Strategy

We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].

### Early Stopping

The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].
