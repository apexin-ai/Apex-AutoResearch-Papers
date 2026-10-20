# Representation quality monitor: RankMe, k-NN probe, diversity scoring, failsafe detection.
# Core component of RGDS — tracks whether student model's internal representations are still
# reliable for diversity measurement, and triggers fallback to Contriever when they degrade.

import torch
import torch.nn.functional as F
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sentence_transformers import SentenceTransformer


@torch.no_grad()
def extract_hidden_states(model, input_ids_list, device, batch_size=32, layer=-1):
    """Extract last-hidden-layer representations for a list of token sequences.

    Args:
        model: HuggingFace causal LM.
        input_ids_list: List of token id lists.
        device: torch device.
        batch_size: Inference batch size.
        layer: Which hidden layer to use (-1 = last).

    Returns:
        Tensor of shape (N, hidden_dim), mean-pooled over sequence length.
    """
    model.eval()
    all_reprs = []
    for i in range(0, len(input_ids_list), batch_size):
        batch = input_ids_list[i:i + batch_size]
        max_len = max(len(ids) for ids in batch)
        padded = torch.zeros(len(batch), max_len, dtype=torch.long, device=device)
        mask = torch.zeros(len(batch), max_len, dtype=torch.long, device=device)
        for j, ids in enumerate(batch):
            padded[j, :len(ids)] = torch.tensor(ids, dtype=torch.long)
            mask[j, :len(ids)] = 1

        outputs = model(input_ids=padded, attention_mask=mask, output_hidden_states=True)
        hidden = outputs.hidden_states[layer]  # (B, T, D)

        # mean pooling over non-padding positions
        mask_expanded = mask.unsqueeze(-1).float()
        pooled = (hidden * mask_expanded).sum(dim=1) / mask_expanded.sum(dim=1).clamp(min=1)
        all_reprs.append(pooled.cpu())

    return torch.cat(all_reprs, dim=0)


def compute_rankme(model, reference_set, device, batch_size=32):
    """RankMe effective rank: exp(Shannon entropy of normalized singular values).

    Higher = more diverse/spread representations. Drop indicates collapse.
    """
    reprs = extract_hidden_states(model, reference_set, device, batch_size)
    reprs = reprs.float()

    # center
    reprs = reprs - reprs.mean(dim=0, keepdim=True)

    # SVD
    U, S, Vh = torch.linalg.svd(reprs, full_matrices=False)

    # normalized singular values → probability distribution
    S_norm = S / S.sum()
    S_norm = S_norm[S_norm > 1e-10]

    entropy = -(S_norm * torch.log(S_norm)).sum().item()
    effective_rank = np.exp(entropy)

    return effective_rank


def compute_knn_probe(model, reference_set, rare_labels, device,
                      k=5, batch_size=32, test_fraction=0.2):
    """5-NN probe accuracy: can the representation space still distinguish rare vs common?

    Args:
        rare_labels: List of bool/int labels (1 = contains rare n-grams).
        k: Number of neighbors.
        test_fraction: Fraction held out for evaluation.

    Returns:
        Accuracy score (0-1).
    """
    reprs = extract_hidden_states(model, reference_set, device, batch_size)
    reprs = reprs.numpy()
    labels = np.array(rare_labels, dtype=int)

    # train/test split (deterministic)
    n = len(reprs)
    n_test = max(1, int(n * test_fraction))
    X_train, X_test = reprs[:-n_test], reprs[-n_test:]
    y_train, y_test = labels[:-n_test], labels[-n_test:]

    if len(np.unique(y_train)) < 2:
        return 0.5  # degenerate case

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return accuracy_score(y_test, y_pred)


def compute_diversity_scores(model, candidates, device, method="internal",
                             tokenizer=None, contriever_model=None, batch_size=32):
    """Compute per-sample diversity scores using internal or Contriever embeddings.

    Args:
        model: Student model (used when method="internal").
        candidates: List of token id lists.
        device: torch device.
        method: "internal" (student model) or "contriever" (external).
        tokenizer: Required for Contriever to decode tokens to text.
        contriever_model: Preloaded SentenceTransformer for Contriever.
        batch_size: Batch size for embedding.

    Returns:
        embeddings: Tensor of shape (N, D).
    """
    if method == "internal":
        embeddings = extract_hidden_states(model, candidates, device, batch_size)
    elif method == "contriever":
        if tokenizer is None or contriever_model is None:
            raise ValueError("Contriever mode requires tokenizer and contriever_model")
        texts = [tokenizer.decode(ids, skip_special_tokens=True) for ids in candidates]
        embeddings = contriever_model.encode(texts, batch_size=batch_size,
                                             show_progress_bar=False, convert_to_tensor=True)
        embeddings = embeddings.cpu()
    else:
        raise ValueError(f"Unknown method: {method}")

    return embeddings


def failsafe_check(rankme_current, rankme_gen0, knn_accuracy,
                   tau_rank=0.5, tau_knn=0.6):
    """Determine whether to switch from internal to external (Contriever) embeddings.

    Triggers fallback when EITHER:
      - RankMe dropped below tau_rank fraction of gen-0 value, OR
      - k-NN probe accuracy dropped below tau_knn

    Returns:
        (should_fallback: bool, reason: str)
    """
    rank_ratio = rankme_current / max(rankme_gen0, 1e-6)
    reasons = []

    if rank_ratio < tau_rank:
        reasons.append(f"RankMe ratio {rank_ratio:.3f} < {tau_rank}")
    if knn_accuracy < tau_knn:
        reasons.append(f"k-NN accuracy {knn_accuracy:.3f} < {tau_knn}")

    if reasons:
        return True, "; ".join(reasons)
    return False, "representations healthy"


def load_contriever(device="cpu"):
    """Load the Contriever model for external diversity scoring."""
    model = SentenceTransformer("facebook/contriever", device=device)
    return model
