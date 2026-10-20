#!/usr/bin/env python3
"""Data volume control: randomly remove 9813 windows from 46708 non-test windows.

Disentangles data volume reduction from OB signal loss in the -7.7pp drop.
If random-removal F1 >> 0.770 (OB removal), then OB has independent value.
If random-removal F1 ~ 0.770, then the drop is just from losing data.
"""
import json, random, sys
from pathlib import Path
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn
from sklearn.metrics import accuracy_score, f1_score


def set_seed(s):
    random.seed(s)
    torch.manual_seed(s)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(s)


def calc_metrics(y, p):
    return {
        "macro_f1": f1_score(y, p, average="macro", zero_division=0),
        "accuracy": accuracy_score(y, p),
        "f1_stag": f1_score(y, p, pos_label=0, zero_division=0),
        "f1_prog": f1_score(y, p, pos_label=1, zero_division=0),
    }


def main():
    BASE = Path("/root/autodl-tmp/agent_progress_probe")
    SEEDS = [42, 123, 456]
    N_REMOVE = 9813
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print("Loading full data...")
    data = torch.load(BASE / "data/embeddings.pt", weights_only=False)
    embs, labs, iids = data["embeddings"], data["labels"], data["instance_ids"]
    edim = data["embed_dim"]
    total = len(labs)
    print(f"Total: {total} windows, embed_dim={edim}")

    with open(BASE / "checkpoints_full/split_info.json") as f:
        si = json.load(f)
    test_idx_set = set(si["test_indices"])
    non_test = [i for i in range(total) if i not in test_idx_set]
    print(f"Test: {len(test_idx_set)} | Non-test: {len(non_test)}")
    assert len(non_test) + len(test_idx_set) == total

    test_sorted = sorted(test_idx_set)
    test_embs = [embs[i] for i in test_sorted]
    test_labs = [labs[i] for i in test_sorted]
    test_loader = DataLoader(
        WindowDataset(test_embs, test_labs), batch_size=64, collate_fn=collate_fn
    )

    results = {}
    for seed in SEEDS:
        print(f"\n{'='*50}")
        print(f"Seed {seed}: removing {N_REMOVE} random from {len(non_test)}")
        print(f"{'='*50}")

        rng = random.Random(seed)
        remove = set(rng.sample(non_test, N_REMOVE))
        keep = [i for i in non_test if i not in remove]
        print(f"Kept: {len(keep)} windows (expected {len(non_test) - N_REMOVE})")

        keep_iids = [iids[i] for i in keep]
        uniq = sorted(set(keep_iids))
        rng2 = random.Random(seed + 1000)
        rng2.shuffle(uniq)
        n_train_inst = int(len(uniq) * 0.82)
        train_inst = set(uniq[:n_train_inst])

        tr_idx = [keep[j] for j, iid in enumerate(keep_iids) if iid in train_inst]
        va_idx = [keep[j] for j, iid in enumerate(keep_iids) if iid not in train_inst]
        print(f"Train: {len(tr_idx)} | Val: {len(va_idx)}")

        set_seed(seed)
        tr_labs_list = [labs[i] for i in tr_idx]
        npos = sum(tr_labs_list)
        nneg = len(tr_labs_list) - npos
        pw = torch.tensor([nneg / max(npos, 1)]).to(device)

        tr_ds = WindowDataset([embs[i] for i in tr_idx], tr_labs_list)
        va_ds = WindowDataset([embs[i] for i in va_idx], [labs[i] for i in va_idx])
        tr_loader = DataLoader(tr_ds, batch_size=32, shuffle=True, collate_fn=collate_fn)
        va_loader = DataLoader(va_ds, batch_size=64, collate_fn=collate_fn)

        model = ProgressProbe(
            embed_dim=edim, hidden_size=256, num_layers=2, dropout=0.1
        ).to(device)
        opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
        crit = nn.BCEWithLogitsLoss(pos_weight=pw)

        outdir = BASE / f"checkpoints_vol_ctrl_seed{seed}"
        outdir.mkdir(parents=True, exist_ok=True)

        best_vf1, best_ep, noimprove = 0.0, 0, 0
        for ep in range(1, 21):
            model.train()
            tloss, n = 0.0, 0
            for pad, bl, lens in tr_loader:
                logits = model(pad.to(device), lens)
                loss = crit(logits, bl.to(device))
                opt.zero_grad()
                loss.backward()
                opt.step()
                tloss += loss.item() * len(bl)
                n += len(bl)

            model.eval()
            yl, yp = [], []
            with torch.no_grad():
                for pad, bl, lens in va_loader:
                    logits = model(pad.to(device), lens)
                    preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
                    yl.extend(bl.long().tolist())
                    yp.extend(preds.tolist())
            vm = calc_metrics(yl, yp)

            improved = vm["macro_f1"] > best_vf1
            if improved:
                best_vf1 = vm["macro_f1"]
                best_ep = ep
                noimprove = 0
                torch.save(
                    {
                        "model_state_dict": model.state_dict(),
                        "embed_dim": edim,
                        "hidden_size": 256,
                        "num_layers": 2,
                        "dropout": 0.1,
                    },
                    outdir / "best_model.pt",
                )
            else:
                noimprove += 1
            mk = " *" if improved else ""
            print(f"  Ep {ep:2d} loss={tloss/n:.4f} val_F1={vm['macro_f1']:.4f}{mk}")
            if noimprove >= 5:
                print(f"  Early stop ep {ep}")
                break

        ckpt = torch.load(outdir / "best_model.pt", weights_only=False, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])
        model.eval()
        yl, yp = [], []
        with torch.no_grad():
            for pad, bl, lens in test_loader:
                logits = model(pad.to(device), lens)
                preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
                yl.extend(bl.long().tolist())
                yp.extend(preds.tolist())
        tm = calc_metrics(yl, yp)
        tm["best_epoch"] = best_ep
        tm["best_val_f1"] = round(best_vf1, 4)
        results[seed] = tm
        print(f"\n  Test: macro_f1={tm['macro_f1']:.4f} acc={tm['accuracy']:.4f} "
              f"f1_stag={tm['f1_stag']:.4f} f1_prog={tm['f1_prog']:.4f}")

    print(f"\n{'='*50}\nSUMMARY\n{'='*50}")
    f1s = [results[s]["macro_f1"] for s in SEEDS]
    mean_f1, std_f1 = float(np.mean(f1s)), float(np.std(f1s))
    delta = (mean_f1 - 0.770) * 100
    print(f"Random removal ({N_REMOVE}w): {mean_f1:.4f} +/- {std_f1:.4f}")
    print(f"OB removal ({N_REMOVE}w):     0.770 +/- 0.022")
    print(f"Original baseline:            0.847")
    print(f"Delta random vs OB: {delta:+.1f}pp")

    summary = {
        "per_seed": {str(s): results[s] for s in SEEDS},
        "mean_macro_f1": round(mean_f1, 4),
        "std_macro_f1": round(std_f1, 4),
        "ob_mean_f1": 0.770,
        "ob_std_f1": 0.022,
        "baseline_f1": 0.847,
        "delta_random_vs_ob_pp": round(delta, 1),
    }
    print(f"METRICS_JSON={json.dumps(summary)}")


if __name__ == "__main__":
    main()
