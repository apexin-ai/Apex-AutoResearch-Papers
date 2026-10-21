"""DCOL evaluation: load checkpoint, extract embeddings, kNN + AUC + t-SNE.

Usage:
    python eval_dcol.py --checkpoint best.pt --data_dir /path/to/test_jsonls \
        --output_dir ./eval_results

Dependencies: torch, transformers, sklearn, matplotlib
"""

import argparse
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
from sklearn.manifold import TSNE
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from torch.utils.data import DataLoader
from transformers import AutoTokenizer

from dcol_dataset import DepthCollator, DepthDataset
from dcol_model import DColModel


@torch.no_grad()
def extract_embeddings(model, loader, device):
    model.eval()
    all_emb, all_labels = [], []
    for batch in loader:
        ids = batch["input_ids"].to(device)
        mask = batch["attention_mask"].to(device)
        with torch.amp.autocast("cuda", enabled=device.type == "cuda"):
            emb = model(ids, mask)
        all_emb.append(emb.float().cpu())
        all_labels.append(batch["labels"])
    return torch.cat(all_emb).numpy(), torch.cat(all_labels).numpy()


def pairwise_auc(embeddings: np.ndarray, labels: np.ndarray) -> dict:
    """OvO pairwise AUC between all depth pairs."""
    classes = sorted(set(labels))
    results = {}
    for i, c1 in enumerate(classes):
        for c2 in classes[i + 1:]:
            mask = (labels == c1) | (labels == c2)
            sub_emb = embeddings[mask]
            sub_lab = (labels[mask] == c2).astype(int)
            # Use distance to class centroids as score
            c1_center = embeddings[labels == c1].mean(axis=0)
            c2_center = embeddings[labels == c2].mean(axis=0)
            scores = np.linalg.norm(sub_emb - c1_center, axis=1) - \
                     np.linalg.norm(sub_emb - c2_center, axis=1)
            auc = roc_auc_score(sub_lab, scores)
            results[f"AUC_{c1}_vs_{c2}"] = auc
    return results


def plot_tsne(embeddings: np.ndarray, labels: np.ndarray, save_path: str):
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    coords = tsne.fit_transform(embeddings)
    plt.figure(figsize=(8, 6))
    cmap = plt.cm.get_cmap("tab10", 4)
    for d in range(4):
        mask = labels == d
        if mask.any():
            plt.scatter(coords[mask, 0], coords[mask, 1],
                        c=[cmap(d)], label=f"depth {d}", alpha=0.6, s=15)
    plt.legend()
    plt.title("t-SNE of DCOL Embeddings")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"t-SNE plot saved to {save_path}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate DCOL model")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default="./eval_results")
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--knn_k", type=int, default=5)
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    os.makedirs(args.output_dir, exist_ok=True)

    # Load checkpoint
    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)
    train_args = ckpt["args"]
    model = DColModel(train_args["model_name"], train_args["embed_dim"]).to(device)
    model.load_state_dict(ckpt["model"])
    print(f"Loaded checkpoint: epoch {ckpt.get('epoch', '?')}, "
          f"val_knn_acc={ckpt.get('val_knn_acc', '?')}")

    # Data
    tokenizer = AutoTokenizer.from_pretrained(train_args["model_name"])
    dataset = DepthDataset(args.data_dir)
    collator = DepthCollator(tokenizer, max_length=train_args.get("max_length", 512))
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False,
                        collate_fn=collator, num_workers=2, pin_memory=True)

    # Extract embeddings
    embeddings, labels = extract_embeddings(model, loader, device)
    print(f"Extracted {len(embeddings)} embeddings, classes: {np.bincount(labels)}")

    # kNN classification
    knn = KNeighborsClassifier(n_neighbors=args.knn_k, metric="euclidean")
    knn.fit(embeddings, labels)
    preds = knn.predict(embeddings)  # leave-one-out would be better; this is resubstitution
    acc = (preds == labels).mean()
    print(f"kNN (k={args.knn_k}) resubstitution accuracy: {acc:.4f}")

    # Confusion matrix
    cm = confusion_matrix(labels, preds)
    print(f"Confusion matrix:\n{cm}")

    # Pairwise AUC
    auc_results = pairwise_auc(embeddings, labels)
    for k, v in sorted(auc_results.items()):
        print(f"  {k}: {v:.4f}")
    mean_auc = np.mean(list(auc_results.values()))
    print(f"  Mean pairwise AUC: {mean_auc:.4f}")

    # t-SNE visualization
    plot_tsne(embeddings, labels, os.path.join(args.output_dir, "tsne.png"))

    # Save embeddings
    np.savez(os.path.join(args.output_dir, "embeddings.npz"),
             embeddings=embeddings, labels=labels)
    print(f"Embeddings saved to {args.output_dir}/embeddings.npz")


if __name__ == "__main__":
    main()
