"""Compute pairwise cosine similarity matrix and BCS scores.

Input: Type embeddings .pt file
Output: Similarity matrix .pt, heatmap PDF
Dependencies: torch, matplotlib, seaborn
"""
import argparse
import logging
from pathlib import Path

import torch
import torch.nn.functional as F

logger = logging.getLogger(__name__)


def load_embeddings(path: str) -> dict:
    """Load {type_name: tensor} from .pt file."""
    return torch.load(path, map_location="cpu", weights_only=True)


def compute_similarity_matrix(embeddings: dict) -> tuple:
    """Compute pairwise cosine similarity matrix.

    Returns:
        (sim_matrix, type_names, type_to_idx) where sim_matrix is N×N tensor.
    """
    type_names = sorted(embeddings.keys())
    type_to_idx = {name: i for i, name in enumerate(type_names)}

    vecs = torch.stack([embeddings[name] for name in type_names]).float()
    vecs = F.normalize(vecs, dim=1)
    sim_matrix = vecs @ vecs.T  # N×N cosine similarity

    return sim_matrix, type_names, type_to_idx


def compute_bcs(type_subset: list, sim_matrix: torch.Tensor, type_to_idx: dict) -> float:
    """Compute Batch Confusability Score for a subset of types.

    BCS = mean pairwise cosine similarity among batch types.

    Args:
        type_subset: List of type names in the batch.
        sim_matrix: Full N×N similarity matrix.
        type_to_idx: Mapping from type name to matrix index.

    Returns:
        BCS value (float).
    """
    if len(type_subset) < 2:
        return 0.0

    indices = [type_to_idx[t] for t in type_subset]
    total = 0.0
    count = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count


def compute_bcs_max(type_subset: list, sim_matrix: torch.Tensor, type_to_idx: dict) -> float:
    """DEPRECATED: Compute BCS using max pairwise similarity.

    Kept for backward compatibility. Use compute_bcs() (mean) instead.
    """
    if len(type_subset) < 2:
        return 0.0

    indices = [type_to_idx[t] for t in type_subset]
    max_sim = float("-inf")
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            val = sim_matrix[indices[i], indices[j]].item()
            if val > max_sim:
                max_sim = val
    return max_sim


def plot_similarity_heatmap(sim_matrix: torch.Tensor, type_names: list, output_path: str):
    """Plot and save cosine similarity heatmap."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, ax = plt.subplots(figsize=(20, 18))
    sns.heatmap(
        sim_matrix.numpy(),
        xticklabels=type_names,
        yticklabels=type_names,
        cmap="RdYlBu_r",
        vmin=-0.2,
        vmax=1.0,
        square=True,
        ax=ax,
    )
    ax.set_title("Type Embedding Cosine Similarity", fontsize=14)
    plt.xticks(fontsize=5, rotation=90)
    plt.yticks(fontsize=5, rotation=0)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info("Saved heatmap to %s", output_path)


def main():
    parser = argparse.ArgumentParser(description="Compute BCS similarity matrix")
    parser.add_argument("--embeddings_path", required=True, help="Type embeddings .pt file")
    parser.add_argument("--output_dir", required=True, help="Output directory for sim_matrix.pt + heatmap")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    embeddings = load_embeddings(args.embeddings_path)
    logger.info("Loaded embeddings for %d types", len(embeddings))

    sim_matrix, type_names, type_to_idx = compute_similarity_matrix(embeddings)
    logger.info("Similarity matrix shape: %s", sim_matrix.shape)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    torch.save({"sim_matrix": sim_matrix, "type_names": type_names, "type_to_idx": type_to_idx},
               output_dir / "sim_matrix.pt")
    logger.info("Saved sim_matrix.pt")

    plot_similarity_heatmap(sim_matrix, type_names, str(output_dir / "heatmap.pdf"))


if __name__ == "__main__":
    main()
