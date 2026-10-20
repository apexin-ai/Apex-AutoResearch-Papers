import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch_geometric.loader import DataLoader

from src.models.gin_encoder import GINEncoder
from src.models.supcon_loss import SupConLoss
from src.augmentations import dual_augment


def parse_args():
    parser = argparse.ArgumentParser(description="MVP training: SupCon + Linear Probe for graph jailbreak detection")
    parser.add_argument("--data_dir", type=str, default="./data")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--hidden_dim", type=int, default=64)
    parser.add_argument("--feat_dim", type=int, default=128)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--holdout_mode", type=str, default=None, help="Failure mode to hold out for testing")
    parser.add_argument("--n_folds", type=int, default=5)
    parser.add_argument("--patience", type=int, default=20)
    parser.add_argument("--weight_decay", type=float, default=1e-4)
    parser.add_argument("--output_dir", type=str, default="./results")
    parser.add_argument("--aug1", type=str, default="dropout_edge")
    parser.add_argument("--aug2", type=str, default="drop_feature")
    return parser.parse_args()


def set_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_dataset(data_dir, holdout_mode=None, holdout_benign_ratio=0.15, seed=42):
    """
    Load dataset with proper cross-mode holdout that includes benign samples in test.

    When holdout_mode is set:
    - Test set = all attack graphs of that mode + a proportion of benign graphs
    - Train set = remaining graphs
    This prevents the test set from being 100% attack (which would make AUROC undefined).
    """
    data_path = Path(data_dir)
    graphs = torch.load(data_path / "graphs.pt", weights_only=False)

    if holdout_mode is not None:
        attack_test = [g for g in graphs if getattr(g, 'failure_mode', None) == holdout_mode]
        benign_all = [g for g in graphs if getattr(g, 'failure_mode', None) == "benign"]
        other_attack = [g for g in graphs
                        if getattr(g, 'failure_mode', None) != holdout_mode
                        and getattr(g, 'failure_mode', None) != "benign"]

        # Hold out a proportion of benign for test set
        rng = np.random.RandomState(seed)
        n_benign_test = max(1, int(len(benign_all) * holdout_benign_ratio))
        benign_indices = rng.permutation(len(benign_all))
        benign_test = [benign_all[i] for i in benign_indices[:n_benign_test]]
        benign_train = [benign_all[i] for i in benign_indices[n_benign_test:]]

        train_graphs = other_attack + benign_train
        test_graphs = attack_test + benign_test
        return train_graphs, test_graphs

    return graphs, None


def train_supcon_epoch(encoder, loader, optimizer, loss_fn, aug1, aug2, device):
    encoder.train()
    total_loss = 0.0
    for batch in loader:
        batch = batch.to(device)
        view1, view2 = dual_augment(batch, aug1, aug2)
        view1 = view1.to(device)
        view2 = view2.to(device)

        z1 = encoder(view1)
        z2 = encoder(view2)

        features = torch.stack([z1, z2], dim=1)  # [bsz, 2, feat_dim]
        loss = loss_fn(features, batch.y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * z1.size(0)

    return total_loss / len(loader.dataset)


def train_linear_probe(encoder, train_loader, val_loader, feat_dim, device, epochs=50, lr=0.01):
    encoder.eval()
    classifier = nn.Linear(feat_dim, 2).to(device)
    optimizer = torch.optim.Adam(classifier.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    best_auroc = 0.0
    best_state = None

    for epoch in range(epochs):
        classifier.train()
        for batch in train_loader:
            batch = batch.to(device)
            with torch.no_grad():
                feats = encoder(batch)
            logits = classifier(feats)
            loss = criterion(logits, batch.y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        auroc = evaluate(encoder, classifier, val_loader, device)["auroc"]
        if auroc > best_auroc:
            best_auroc = auroc
            best_state = classifier.state_dict().copy()

    classifier.load_state_dict(best_state)
    return classifier


def evaluate(encoder, classifier, loader, device):
    encoder.eval()
    classifier.eval()
    all_probs = []
    all_labels = []

    with torch.no_grad():
        for batch in loader:
            batch = batch.to(device)
            feats = encoder(batch)
            logits = classifier(feats)
            probs = torch.softmax(logits, dim=1)[:, 1]
            all_probs.append(probs.cpu())
            all_labels.append(batch.y.cpu())

    all_probs = torch.cat(all_probs).numpy()
    all_labels = torch.cat(all_labels).numpy()
    preds = (all_probs >= 0.5).astype(int)

    return {
        "auroc": roc_auc_score(all_labels, all_probs),
        "f1": f1_score(all_labels, preds),
        "precision": precision_score(all_labels, preds, zero_division=0),
        "recall": recall_score(all_labels, preds, zero_division=0),
    }


def run_fold(train_graphs, val_graphs, args, device, fold_idx):
    train_loader = DataLoader(train_graphs, batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(val_graphs, batch_size=args.batch_size, shuffle=False)

    input_dim = train_graphs[0].x.size(1)
    encoder = GINEncoder(
        input_dim=input_dim,
        hidden_dim=args.hidden_dim,
        feat_dim=args.feat_dim,
    ).to(device)

    optimizer = torch.optim.Adam(encoder.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs)
    loss_fn = SupConLoss(temperature=0.07)

    best_val_auroc = 0.0
    patience_counter = 0
    best_encoder_state = None

    # Phase 1: SupCon pre-training
    for epoch in range(args.epochs):
        train_loss = train_supcon_epoch(encoder, train_loader, optimizer, loss_fn, args.aug1, args.aug2, device)
        scheduler.step()

        # Quick linear eval for early stopping
        tmp_classifier = nn.Linear(args.feat_dim, 2).to(device)
        tmp_opt = torch.optim.Adam(tmp_classifier.parameters(), lr=0.01)
        criterion = nn.CrossEntropyLoss()
        encoder.eval()
        for _ in range(10):
            tmp_classifier.train()
            for batch in train_loader:
                batch = batch.to(device)
                with torch.no_grad():
                    feats = encoder(batch)
                logits = tmp_classifier(feats)
                loss = criterion(logits, batch.y)
                tmp_opt.zero_grad()
                loss.backward()
                tmp_opt.step()

        metrics = evaluate(encoder, tmp_classifier, val_loader, device)
        val_auroc = metrics["auroc"]

        if val_auroc > best_val_auroc:
            best_val_auroc = val_auroc
            best_encoder_state = {k: v.clone() for k, v in encoder.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1

        if patience_counter >= args.patience:
            break

    encoder.load_state_dict(best_encoder_state)

    # Phase 2: Linear probe
    classifier = train_linear_probe(encoder, train_loader, val_loader, args.feat_dim, device)

    val_metrics = evaluate(encoder, classifier, val_loader, device)

    # Save checkpoint
    os.makedirs(args.output_dir, exist_ok=True)
    torch.save(encoder.state_dict(), os.path.join(args.output_dir, f"encoder_fold{fold_idx}.pt"))

    return val_metrics


def main():
    args = parse_args()
    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    graphs, test_graphs = load_dataset(args.data_dir, args.holdout_mode, seed=args.seed)

    if test_graphs is not None:
        # Cross-failure-mode holdout
        labels = np.array([g.y.item() for g in graphs])
        skf = StratifiedKFold(n_splits=args.n_folds, shuffle=True, random_state=args.seed)
        fold_results = []

        for fold_idx, (train_idx, val_idx) in enumerate(skf.split(np.zeros(len(graphs)), labels)):
            train_graphs_fold = [graphs[i] for i in train_idx]
            val_graphs_fold = [graphs[i] for i in val_idx]
            metrics = run_fold(train_graphs_fold, val_graphs_fold, args, device, fold_idx)
            fold_results.append(metrics)
            print(f"Fold {fold_idx}: AUROC={metrics['auroc']:.4f} F1={metrics['f1']:.4f}")

        # Train encoder on ALL non-holdout data (not just one fold's 80%)
        input_dim = graphs[0].x.size(1)
        encoder = GINEncoder(input_dim=input_dim, hidden_dim=args.hidden_dim, feat_dim=args.feat_dim).to(device)

        # Split non-holdout into encoder_train (85%) / encoder_val (15%) for early stopping
        enc_labels = np.array([g.y.item() for g in graphs])
        enc_rng = np.random.RandomState(args.seed + 1)
        enc_val_size = max(1, int(len(graphs) * 0.15))
        enc_perm = enc_rng.permutation(len(graphs))
        enc_val_idx = enc_perm[:enc_val_size]
        enc_train_idx = enc_perm[enc_val_size:]
        enc_train_graphs = [graphs[i] for i in enc_train_idx]
        enc_val_graphs = [graphs[i] for i in enc_val_idx]

        enc_train_loader = DataLoader(enc_train_graphs, batch_size=args.batch_size, shuffle=True)
        enc_val_loader = DataLoader(enc_val_graphs, batch_size=args.batch_size, shuffle=False)

        optimizer = torch.optim.Adam(encoder.parameters(), lr=args.lr, weight_decay=args.weight_decay)
        scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs)
        loss_fn = SupConLoss(temperature=0.07)

        best_val_auroc = 0.0
        patience_counter = 0
        best_encoder_state = None

        for epoch in range(args.epochs):
            train_supcon_epoch(encoder, enc_train_loader, optimizer, loss_fn, args.aug1, args.aug2, device)
            scheduler.step()

            tmp_clf = nn.Linear(args.feat_dim, 2).to(device)
            tmp_opt = torch.optim.Adam(tmp_clf.parameters(), lr=0.01)
            criterion = nn.CrossEntropyLoss()
            encoder.eval()
            for _ in range(10):
                tmp_clf.train()
                for batch in enc_train_loader:
                    batch = batch.to(device)
                    with torch.no_grad():
                        feats = encoder(batch)
                    logits = tmp_clf(feats)
                    loss = criterion(logits, batch.y)
                    tmp_opt.zero_grad()
                    loss.backward()
                    tmp_opt.step()

            val_metrics_enc = evaluate(encoder, tmp_clf, enc_val_loader, device)
            if val_metrics_enc["auroc"] > best_val_auroc:
                best_val_auroc = val_metrics_enc["auroc"]
                best_encoder_state = {k: v.clone() for k, v in encoder.state_dict().items()}
                patience_counter = 0
            else:
                patience_counter += 1
            if patience_counter >= args.patience:
                break

        encoder.load_state_dict(best_encoder_state)
        torch.save(encoder.state_dict(), os.path.join(args.output_dir, "encoder_holdout.pt"))

        # Linear probe: train on enc_train, validate on enc_val (test set never seen)
        probe_train_loader = DataLoader(enc_train_graphs, batch_size=args.batch_size, shuffle=True)
        probe_val_loader = DataLoader(enc_val_graphs, batch_size=args.batch_size, shuffle=False)
        classifier = train_linear_probe(encoder, probe_train_loader, probe_val_loader, args.feat_dim, device)

        # Final evaluation on holdout test set
        test_loader = DataLoader(test_graphs, batch_size=args.batch_size, shuffle=False)
        test_metrics = evaluate(encoder, classifier, test_loader, device)
        print(f"Holdout test ({args.holdout_mode}): AUROC={test_metrics['auroc']:.4f} F1={test_metrics['f1']:.4f}")

    else:
        # Standard 5-fold CV
        labels = np.array([g.y.item() for g in graphs])
        skf = StratifiedKFold(n_splits=args.n_folds, shuffle=True, random_state=args.seed)
        fold_results = []

        for fold_idx, (train_idx, val_idx) in enumerate(skf.split(np.zeros(len(graphs)), labels)):
            train_graphs_fold = [graphs[i] for i in train_idx]
            val_graphs_fold = [graphs[i] for i in val_idx]
            metrics = run_fold(train_graphs_fold, val_graphs_fold, args, device, fold_idx)
            fold_results.append(metrics)
            print(f"Fold {fold_idx}: AUROC={metrics['auroc']:.4f} F1={metrics['f1']:.4f}")

        test_metrics = None

    # Aggregate results
    avg_metrics = {}
    for key in fold_results[0]:
        values = [r[key] for r in fold_results]
        avg_metrics[key] = {"mean": float(np.mean(values)), "std": float(np.std(values))}

    results = {
        "args": vars(args),
        "fold_results": fold_results,
        "avg_metrics": avg_metrics,
    }
    if test_metrics is not None:
        results["holdout_test"] = test_metrics

    os.makedirs(args.output_dir, exist_ok=True)
    with open(os.path.join(args.output_dir, "results.json"), "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nAverage: AUROC={avg_metrics['auroc']['mean']:.4f}±{avg_metrics['auroc']['std']:.4f} "
          f"F1={avg_metrics['f1']['mean']:.4f}±{avg_metrics['f1']['std']:.4f}")


if __name__ == "__main__":
    main()
