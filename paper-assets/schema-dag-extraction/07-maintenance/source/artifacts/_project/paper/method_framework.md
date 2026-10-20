# Section 3: Method

## 3.1 Problem Formulation

### Schema Complexity in Training-Free LLM IE

We consider training-free information extraction where an LLM $\mathcal{M}$ extracts typed mentions from input text $x$ given a schema $\mathcal{S} = \{(t_i, d_i)\}_{i=1}^{N}$, where $t_i$ is a type name and $d_i$ its natural language description. The LLM receives $\mathcal{S}$ (or a subset) in its prompt and produces structured predictions $\hat{Y} = \{(m_j, t_j)\}$, each a mention span $m_j$ paired with a type $t_j \in \mathcal{S}$.

**Type count** $N = |\mathcal{S}|$ is the number of types presented simultaneously. Prior work implicitly treats $N$ as the sole driver of schema complexity.

**Pairwise type confusability.** We define the *Schema Confusability Score* (SCS) between types $t_i$ and $t_j$ as:

$$\text{SCS}(t_i, t_j) = \text{cosine}(\mathbf{e}_i, \mathbf{e}_j)$$

where $\mathbf{e}_i \in \mathbb{R}^D$ is the mean-pooled hidden state of $\mathcal{M}$ when encoding type $t_i$'s definition. SCS captures the degree to which two types occupy overlapping regions in the model's representation space.

**Batch Confusability Score (BCS).** For a batch $B \subseteq \mathcal{S}$, we define:

$$\text{BCS}(B) = \max_{t_i, t_j \in B, \, i \neq j} \text{SCS}(t_i, t_j)$$

BCS measures the worst-case confusability within a batch --- the pair of types most likely to be confused by the model when co-presented.

**Schema complexity** is thus characterized by two independent factors: the *count* $N$ and the *confusability structure* of $\mathcal{S}$, as captured by the pairwise SCS matrix $\mathbf{C} \in [0,1]^{N \times N}$.


## 3.2 Controlled Experiment Design

To disentangle the effects of type count and type confusability on extraction quality, we design a controlled experimental protocol with two complementary analyses.

### Count Curve Analysis

We construct type subsets of increasing size $n \in \{5, 10, 15, \ldots, N\}$ by sampling from $\mathcal{S}$, extract on fixed evaluation samples, and measure micro-F1, precision, and recall as functions of $n$. Multiple random draws per count level reduce sampling variance. This establishes the *marginal* effect of count on extraction performance.

### Within-Count BCS Correlation

At each count level $n$, multiple batches with the same number of types but *different* confusability profiles are constructed. We compute:

$$r = \text{Pearson}(\text{BCS}(B_1), \ldots, \text{BCS}(B_m); \; F_1(B_1), \ldots, F_1(B_m)) \quad \text{at fixed } n$$

A significant negative correlation at fixed $n$ demonstrates that confusability predicts quality degradation *beyond* what count alone explains. We further compute partial correlations $r(\text{F1}, \text{BCS} \mid n)$ pooled across all count levels to quantify confusability's independent contribution.

### Multi-Channel Degradation Model

The controlled analysis reveals two orthogonal degradation channels:

- **Channel 1 (Count $\to$ Recall decline):** Increasing $N$ causes the model to *omit* entities. Manifests as monotonic recall degradation, consistent with attention capacity limits.
- **Channel 2 (Confusability $\to$ Precision decline):** Co-presenting confusable types causes *type confusion* --- entities are detected but assigned the wrong type. Manifests as precision degradation correlated with BCS.

Error taxonomy analysis confirms the two channels produce distinct error types: *omission errors* (false negatives from capacity limits) vs. *type confusion errors* (correct span, wrong type).


## 3.3 SDGD Framework

Based on the multi-channel degradation model, we propose **Schema-Decomposed Graph-Driven (SDGD) extraction**, a framework that partitions the schema into low-confusability batches to neutralize Channel 2 degradation.

### Algorithm Overview

**Input:** Type schema $\mathcal{S} = \{(t_i, d_i)\}_{i=1}^N$; type embeddings $\mathbf{E} \in \mathbb{R}^{N \times D}$; confusability threshold $\tau$; LLM $\mathcal{M}$; evaluation samples $\mathcal{X}$. Optionally: empirical confusion matrix $\mathbf{C}_{\text{emp}}$ (for SDGD-cal).

**Output:** Merged predictions $\hat{Y}$ over all types.

**Step 1 --- Confusability matrix computation.** Compute pairwise confusability $\mathbf{C} \in [0,1]^{N \times N}$. In the zero-shot variant (SDGD-zero), $\mathbf{C}_{ij} = \text{cosine}(\mathbf{e}_i, \mathbf{e}_j)$. In the calibrated variant (SDGD-cal), $\mathbf{C}$ is derived from an empirical confusion matrix obtained on a small calibration set (\S3.4).

**Step 2 --- Thresholded confusability graph.** Construct undirected graph $G = (V, E)$ where $V = \mathcal{S}$ and edge $(t_i, t_j) \in E$ iff $\mathbf{C}_{ij} > \tau$ and $i \neq j$. Two types are adjacent iff they are "too confusable" to co-exist in a single batch.

**Step 3 --- Greedy graph coloring.** Compute a proper vertex coloring of $G$ using greedy coloring with the \texttt{largest\_first} strategy. The coloring assigns each type to a color (batch) such that no two adjacent (highly confusable) types share a batch. The number of colors $k$ equals the chromatic number approximation.

**Step 4 --- Per-batch extraction.** For each color group $B_c$ ($c = 1, \ldots, k$), construct a prompt containing only the type definitions in $B_c$, and extract mentions from all samples $\mathcal{X}$ using $\mathcal{M}$ with constrained decoding (JSON schema restricting outputs to types in $B_c$).

**Step 5 --- Cross-batch merge.** Since graph coloring guarantees non-overlapping type sets across batches, predictions are merged by simple union. For each sample, the final prediction set is the concatenation of predictions from all $k$ batches.

### LaTeX Pseudocode

```latex
\begin{algorithm}[t]
\caption{SDGD: Schema-Decomposed Graph-Driven Extraction}
\label{alg:sdgd}
\begin{algorithmic}[1]
\REQUIRE Schema $\mathcal{S} = \{(t_i, d_i)\}_{i=1}^N$, embeddings $\mathbf{E} \in \mathbb{R}^{N \times D}$, threshold $\tau$, LLM $\mathcal{M}$, samples $\mathcal{X}$
\ENSURE Predictions $\hat{Y}$

\STATE \textbf{// Step 1: Confusability matrix}
\STATE $\mathbf{C}_{ij} \leftarrow \text{cosine}(\mathbf{e}_i, \mathbf{e}_j)$ for all $i, j \in [N]$
\COMMENT{SDGD-zero; SDGD-cal uses empirical confusion}

\STATE \textbf{// Step 2: Thresholded confusability graph}
\STATE $V \leftarrow \mathcal{S}$
\STATE $E \leftarrow \{(t_i, t_j) \mid \mathbf{C}_{ij} > \tau,\ i \neq j\}$
\STATE $G \leftarrow (V, E)$

\STATE \textbf{// Step 3: Graph coloring}
\STATE $\phi \leftarrow \textsc{GreedyColor}(G, \text{largest\_first})$
\COMMENT{$\phi: V \to \{1, \ldots, k\}$}
\STATE $\{B_1, \ldots, B_k\} \leftarrow \textsc{GroupByColor}(\phi)$

\STATE \textbf{// Step 4: Per-batch extraction}
\STATE $\hat{Y} \leftarrow \emptyset$
\FOR{$c = 1$ \TO $k$}
    \STATE $\hat{Y}_c \leftarrow \mathcal{M}.\text{extract}(\mathcal{X}, B_c)$
    \COMMENT{Constrained to types in $B_c$}
    \STATE $\hat{Y} \leftarrow \hat{Y} \cup \hat{Y}_c$
    \COMMENT{Union merge}
\ENDFOR

\RETURN $\hat{Y}$
\end{algorithmic}
\end{algorithm}
```

### Threshold Selection

The threshold $\tau$ controls graph density and hence the number of batches $k$. We adopt an **adaptive threshold** strategy that is schema-agnostic:

$$\tau = \mu(\mathbf{C}_{\text{upper}}) + k_\sigma \cdot \sigma(\mathbf{C}_{\text{upper}})$$

where $\mathbf{C}_{\text{upper}}$ denotes the upper-triangular entries of $\mathbf{C}$ (excluding the diagonal), $\mu$ and $\sigma$ are the mean and standard deviation, and $k_\sigma$ is the sole hyperparameter. The adaptive threshold adjusts to the embedding distribution of each schema, avoiding reliance on dataset-specific tuning. We set $k_\sigma = 1.0$ by default and conduct ablations over $k_\sigma \in \{0.5, 1.0, 1.5, 2.0\}$.

For analysis purposes, we also report an **oracle threshold** derived from the BCS--quality degradation curve on the development set. The oracle serves as an upper bound and is clearly distinguished from the adaptive method in all results.

### Complexity

Graph coloring on $N$ types is $O(N^2)$ with greedy heuristics. For the schemas in our experiments ($N \leq 168$), decomposition completes in milliseconds. The dominant cost is LLM inference: SDGD requires $k \times |\mathcal{X}|$ generation calls, compared to $1 \times |\mathcal{X}|$ for single-pass and $N \times |\mathcal{X}|$ for per-type splitting. With $k \approx 8\text{--}12$, SDGD achieves $5\text{--}8\times$ fewer calls than per-type splitting.


## 3.4 SDGD-zero and SDGD-cal Variants

We instantiate two variants of the SDGD framework, differing in how the confusability matrix $\mathbf{C}$ is obtained:

### SDGD-zero (Zero-Shot)

The confusability matrix is computed from type embeddings alone, with no labeled data. We encode each type definition $d_i$ through $\mathcal{M}$ and extract the mean-pooled last hidden state $\mathbf{e}_i \in \mathbb{R}^D$. Pairwise cosine similarity serves as the confusability proxy:

$$\mathbf{C}_{ij}^{\text{zero}} = \text{cosine}(\mathbf{e}_i, \mathbf{e}_j)$$

**Advantages:** Fully zero-shot; no labeled data required; embeddings are precomputed once per schema. Suitable for rapid deployment on new schemas.

**Limitation:** Embedding similarity is a *proxy* for confusability. Two types may be semantically similar yet easily distinguished in context (e.g., \textit{person-artist} and \textit{person-actor} share embedding space but have distinct contextual cues).

### SDGD-cal (Calibrated)

The confusability matrix is derived from empirical extraction errors on a small calibration set of $m$ labeled examples per type:

1. Run single-pass extraction with all $N$ types on the calibration set.
2. Construct a raw confusion matrix $\mathbf{C}_{\text{raw}} \in \mathbb{R}^{N \times N}$, where $\mathbf{C}_{\text{raw}}[i,j]$ counts gold type-$i$ entities predicted as type-$j$.
3. Symmetrize: $\mathbf{C}_{\text{sym}} = (\mathbf{C}_{\text{raw}} + \mathbf{C}_{\text{raw}}^\top) / 2$.
4. Normalize: $\mathbf{C}_{ij}^{\text{cal}} = \mathbf{C}_{\text{sym}}[i,j] / \sum_j \mathbf{C}_{\text{sym}}[i,j]$.

**Advantages:** Measures *actual* model confusion rather than semantic proximity. Captures model-specific and context-dependent confusability patterns.

**Cost:** Requires $m$ labeled examples per type for calibration ($m = 5\text{--}10$ in our experiments). Total calibration cost: one extraction pass over the calibration set.

### Comparison

| | SDGD-zero | SDGD-cal |
|---|---|---|
| Data requirement | None | $m$ labeled examples/type |
| Confusability signal | Semantic proximity | Empirical model errors |
| Schema adaptability | Instant | Requires calibration pass |
| Expected quality | Good (proxy) | Best (ground-truth confusion) |
