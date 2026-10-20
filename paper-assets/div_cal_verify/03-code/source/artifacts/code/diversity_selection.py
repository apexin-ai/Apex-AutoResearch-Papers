# Diversity-based data selection: PCA projection + greedy submodular selection + quality filter.
# Implements DiSF-style selection: greedily pick samples that maximize embedding covariance uniformity.

import torch
import numpy as np
from sklearn.decomposition import PCA


def fit_pca(reference_embeddings, n_components=32):
    """Fit PCA on reference set embeddings.

    Args:
        reference_embeddings: (N, D) tensor or array from the reference set.
        n_components: Target dimensionality.

    Returns:
        Fitted sklearn PCA object.
    """
    X = reference_embeddings.numpy() if isinstance(reference_embeddings, torch.Tensor) else reference_embeddings
    pca = PCA(n_components=n_components)
    pca.fit(X)
    return pca


def project(embeddings, pca):
    """Project embeddings to PCA space.

    Returns:
        (N, n_components) numpy array.
    """
    X = embeddings.numpy() if isinstance(embeddings, torch.Tensor) else embeddings
    return pca.transform(X)


def compute_normalized_eigenvalue_variance(X):
    """Normalized eigenvalue variance: ||C||_F / trace(C)².

    Lower = more uniform eigenvalues = more diverse coverage.
    Returns inf for degenerate cases.
    """
    if len(X) < 2:
        return float('inf')
    cov = np.cov(X.T)
    if cov.ndim == 0:
        return 0.0
    trace = np.trace(cov)
    if trace < 1e-10:
        return float('inf')
    frob = np.linalg.norm(cov, "fro")
    return frob / (trace ** 2)


def quality_filter(candidates, model, tokenizer, reference_set, device,
                   percentile=90, batch_size=32):
    """Filter out candidates with perplexity above the threshold.

    Threshold = percentile-th percentile of reference set perplexity under the current model.

    Args:
        candidates: List of token id lists.
        model: Current student model.
        tokenizer: Tokenizer.
        reference_set: List of token id lists (reference R).
        device: torch device.
        percentile: Cutoff percentile.
        batch_size: Batch size.

    Returns:
        (filtered_indices, threshold): indices of candidates that pass, and the ppl threshold.
    """
    ref_ppls = _compute_perplexities(model, reference_set, device, batch_size)
    threshold = np.percentile(ref_ppls, percentile)

    cand_ppls = _compute_perplexities(model, candidates, device, batch_size)
    filtered = [i for i, ppl in enumerate(cand_ppls) if ppl <= threshold]
    return filtered, threshold


@torch.no_grad()
def _compute_perplexities(model, input_ids_list, device, batch_size=32):
    """Compute per-sequence perplexity."""
    model.eval()
    ppls = []
    for i in range(0, len(input_ids_list), batch_size):
        batch = input_ids_list[i:i + batch_size]
        max_len = max(len(ids) for ids in batch)
        padded = torch.zeros(len(batch), max_len, dtype=torch.long, device=device)
        mask = torch.zeros(len(batch), max_len, dtype=torch.long, device=device)
        for j, ids in enumerate(batch):
            padded[j, :len(ids)] = torch.tensor(ids, dtype=torch.long)
            mask[j, :len(ids)] = 1

        outputs = model(input_ids=padded, attention_mask=mask, labels=padded)
        logits = outputs.logits

        # per-token cross-entropy
        shift_logits = logits[:, :-1, :].contiguous()
        shift_labels = padded[:, 1:].contiguous()
        shift_mask = mask[:, 1:].contiguous()

        loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
        losses = loss_fct(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1)
        ).view(shift_labels.shape)

        # per-sequence mean loss → perplexity
        seq_losses = (losses * shift_mask).sum(dim=1) / shift_mask.sum(dim=1).clamp(min=1)
        seq_ppls = torch.exp(seq_losses).cpu().tolist()
        ppls.extend(seq_ppls)

    return np.array(ppls)


def greedy_disf_selection(embeddings_pca, budget, quality_mask=None):
    """Greedy selection minimizing normalized eigenvalue variance of covariance.

    Each step picks the candidate that minimizes ||C(S∪{x})||_F / trace(C(S∪{x}))²,
    which selects for uniform eigenvalue spread (= diverse spatial coverage).

    Args:
        embeddings_pca: (N, d) numpy array of PCA-projected embeddings.
        budget: Number of samples to select.
        quality_mask: Optional boolean array (True = eligible). None = all eligible.

    Returns:
        List of selected indices.
    """
    N = len(embeddings_pca)
    if quality_mask is None:
        quality_mask = np.ones(N, dtype=bool)

    eligible = set(np.where(quality_mask)[0])
    if len(eligible) == 0:
        return []

    budget = min(budget, len(eligible))
    selected = []

    # pick first sample: the one FARTHEST from the overall mean (most outlier = most diverse seed)
    mean = embeddings_pca[list(eligible)].mean(axis=0)
    dists = np.linalg.norm(embeddings_pca - mean, axis=1)
    dists[~quality_mask] = -np.inf
    first = int(np.argmax(dists))
    selected.append(first)
    eligible.discard(first)

    for _ in range(1, budget):
        if not eligible:
            break

        best_idx = -1
        best_score = float('inf')

        current_data = embeddings_pca[selected]

        for candidate in eligible:
            trial = np.vstack([current_data, embeddings_pca[candidate:candidate + 1]])
            score = compute_normalized_eigenvalue_variance(trial)
            if score < best_score:
                best_score = score
                best_idx = candidate

        selected.append(best_idx)
        eligible.discard(best_idx)

        if len(selected) % 100 == 0:
            print(f"  Selected {len(selected)}/{budget}")

    return selected


def select_data(student_model, tokenizer, candidates, reference_set, reference_embeddings,
                device, method="internal", contriever_model=None,
                pca_dim=32, budget=None, quality_percentile=90, batch_size=32):
    """Full RGDS selection pipeline: quality filter → embed → PCA → greedy select.

    Args:
        student_model: Current student model.
        tokenizer: Tokenizer.
        candidates: List of token id lists (synthetic data pool).
        reference_set: List of token id lists (fixed reference R).
        reference_embeddings: Precomputed reference embeddings (N_ref, D).
        device: torch device.
        method: "internal" or "contriever".
        contriever_model: Required if method="contriever".
        pca_dim: PCA target dimensionality.
        budget: How many samples to select. Default = len(candidates) // 2.
        quality_percentile: Perplexity cutoff percentile.
        batch_size: Batch size.

    Returns:
        selected_indices: List of indices into the original candidates list.
    """
    from representation_monitor import compute_diversity_scores

    if budget is None:
        budget = len(candidates) // 2

    # Step 1: quality filter
    print("Quality filtering...")
    quality_indices, ppl_threshold = quality_filter(
        candidates, student_model, tokenizer, reference_set, device,
        percentile=quality_percentile, batch_size=batch_size
    )
    print(f"  {len(quality_indices)}/{len(candidates)} passed (ppl threshold: {ppl_threshold:.1f})")

    if len(quality_indices) == 0:
        print("  WARNING: No candidates passed quality filter, returning empty selection")
        return []

    # Step 2: compute embeddings for all candidates
    print(f"Computing embeddings (method={method})...")
    all_embeddings = compute_diversity_scores(
        student_model, candidates, device, method=method,
        tokenizer=tokenizer, contriever_model=contriever_model, batch_size=batch_size
    )

    # Step 3: fit PCA — must use same embedding space for fit and transform
    if method == "contriever":
        print(f"Computing Contriever reference embeddings for PCA fit...")
        ref_embeddings_for_pca = compute_diversity_scores(
            student_model, reference_set, device, method="contriever",
            tokenizer=tokenizer, contriever_model=contriever_model, batch_size=batch_size
        )
        ref_emb = ref_embeddings_for_pca.numpy() if isinstance(ref_embeddings_for_pca, torch.Tensor) else ref_embeddings_for_pca
    else:
        ref_emb = reference_embeddings.numpy() if isinstance(reference_embeddings, torch.Tensor) else reference_embeddings

    print(f"PCA projection to d={pca_dim}...")
    pca = fit_pca(ref_emb, n_components=pca_dim)
    candidates_pca = project(all_embeddings, pca)

    # Step 4: greedy selection with quality mask
    quality_mask = np.zeros(len(candidates), dtype=bool)
    quality_mask[quality_indices] = True

    budget = min(budget, len(quality_indices))
    print(f"Greedy submodular selection (budget={budget})...")
    selected = greedy_disf_selection(candidates_pca, budget, quality_mask=quality_mask)

    return selected
