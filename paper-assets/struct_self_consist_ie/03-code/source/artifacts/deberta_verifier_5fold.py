#!/usr/bin/env python3
"""DeBERTa Verifier: 5-fold CV x 3 seeds evaluation for SciERC."""

import argparse
import json
import os
import subprocess
import sys
import time

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

PROJECT_DIR = "/root/autodl-tmp/struct_self_consist_ie"
DATA_PATH = os.path.join(PROJECT_DIR, "output/exp_012_rerun_1024/samples.jsonl")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "output/deberta_verifier_5fold")
CHECKPOINT_DIR = os.path.join(OUTPUT_DIR, "checkpoints")
MODEL_NAME = "microsoft/deberta-v3-base"
SEEDS = [42, 123, 456]
N_FOLDS = 5
EPOCHS = 10
PATIENCE = 3
BATCH_SIZE = 16
LR = 2e-5
WEIGHT_DECAY = 0.01
MAX_LENGTH = 512
GPUS = [1, 2]


def compute_entity_f1(pred_entities, gold_entities):
    pred_set = set((e["text"], e["type"]) for e in pred_entities)
    gold_set = set((e["text"], e["type"]) for e in gold_entities)
    if len(pred_set) == 0 and len(gold_set) == 0:
        return 1.0
    if len(pred_set) == 0 or len(gold_set) == 0:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)


def serialize_entities(entities):
    return "; ".join(f"{e['text']} ({e['type']})" for e in entities)


def load_data():
    instances = []
    with open(DATA_PATH) as f:
        for line in f:
            inst = json.loads(line)
            gold_ents = inst["gold"]["entities"]
            samples = []
            for i, s in enumerate(inst["samples"]):
                f1 = compute_entity_f1(s["entities"], gold_ents)
                text_b = serialize_entities(s["entities"])
                samples.append({
                    "text_a": inst["text"],
                    "text_b": text_b,
                    "f1": f1,
                    "logprob": inst["logprobs"][i],
                })
            greedy_f1 = compute_entity_f1(inst["greedy"]["entities"], gold_ents)
            oracle_f1 = max(s["f1"] for s in samples)
            lp_idx = max(range(len(samples)), key=lambda j: samples[j]["logprob"])
            lp_f1 = samples[lp_idx]["f1"]
            instances.append({
                "id": inst["id"],
                "samples": samples,
                "greedy_f1": greedy_f1,
                "oracle_f1": oracle_f1,
                "lp_f1": lp_f1,
            })
    return instances


def worker_main(fold, seed, gpu_id):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)

    import numpy as np
    import torch
    import torch.nn as nn
    from torch.utils.data import Dataset, DataLoader
    from transformers import AutoTokenizer, AutoModel
    from scipy.stats import spearmanr
    from sklearn.model_selection import KFold

    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    device = torch.device("cuda:0")
    tag = f"fold{fold}_seed{seed}"

    print(f"[{tag}] Loading data, GPU phys={gpu_id}...", flush=True)
    instances = load_data()
    n = len(instances)

    kf = KFold(n_splits=N_FOLDS, shuffle=True, random_state=seed)
    splits = list(kf.split(range(n)))
    train_idx, val_idx = splits[fold]
    train_instances = [instances[i] for i in train_idx]
    val_instances = [instances[i] for i in val_idx]

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    def tokenize_instances(insts):
        examples = []
        for inst in insts:
            for s in inst["samples"]:
                enc = tokenizer(
                    s["text_a"], s["text_b"],
                    max_length=MAX_LENGTH, truncation=True,
                )
                examples.append({
                    "input_ids": enc["input_ids"],
                    "attention_mask": enc["attention_mask"],
                    "f1": s["f1"],
                })
        return examples

    train_examples = tokenize_instances(train_instances)
    val_examples = tokenize_instances(val_instances)

    class SimpleDataset(Dataset):
        def __init__(self, exs):
            self.exs = exs
        def __len__(self):
            return len(self.exs)
        def __getitem__(self, idx):
            return self.exs[idx]

    def collate_fn(batch):
        max_len = max(len(b["input_ids"]) for b in batch)
        bsz = len(batch)
        input_ids = torch.zeros(bsz, max_len, dtype=torch.long)
        attn_mask = torch.zeros(bsz, max_len, dtype=torch.long)
        targets = torch.zeros(bsz, dtype=torch.float)
        for i, b in enumerate(batch):
            length = len(b["input_ids"])
            input_ids[i, :length] = torch.tensor(b["input_ids"])
            attn_mask[i, :length] = torch.tensor(b["attention_mask"])
            targets[i] = b["f1"]
        return {"input_ids": input_ids, "attention_mask": attn_mask, "target": targets}

    train_loader = DataLoader(
        SimpleDataset(train_examples), batch_size=BATCH_SIZE,
        shuffle=True, collate_fn=collate_fn, num_workers=0, pin_memory=True,
    )
    val_loader = DataLoader(
        SimpleDataset(val_examples), batch_size=BATCH_SIZE,
        shuffle=False, collate_fn=collate_fn, num_workers=0, pin_memory=True,
    )

    class Verifier(nn.Module):
        def __init__(self):
            super().__init__()
            self.encoder = AutoModel.from_pretrained(MODEL_NAME)
            self.head = nn.Sequential(
                nn.Linear(768, 256),
                nn.ReLU(),
                nn.Dropout(0.1),
                nn.Linear(256, 1),
                nn.Sigmoid(),
            )
        def forward(self, input_ids, attention_mask):
            out = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
            cls = out.last_hidden_state[:, 0]
            return self.head(cls).squeeze(-1)

    model = Verifier().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    criterion = nn.MSELoss()

    print(f"[{tag}] train={len(train_examples)} val={len(val_examples)} samples", flush=True)

    best_val_loss = float("inf")
    patience_cnt = 0
    best_state = None

    for epoch in range(EPOCHS):
        t_ep = time.time()
        model.train()
        train_loss_sum = 0.0
        n_train = 0
        for batch in train_loader:
            ids = batch["input_ids"].to(device)
            mask = batch["attention_mask"].to(device)
            tgt = batch["target"].to(device)
            pred = model(ids, mask)
            loss = criterion(pred, tgt)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            train_loss_sum += loss.item() * len(tgt)
            n_train += len(tgt)
        train_loss = train_loss_sum / n_train

        model.eval()
        val_loss_sum = 0.0
        n_val = 0
        preds_list = []
        tgts_list = []
        with torch.no_grad():
            for batch in val_loader:
                ids = batch["input_ids"].to(device)
                mask = batch["attention_mask"].to(device)
                tgt = batch["target"].to(device)
                pred = model(ids, mask)
                loss = criterion(pred, tgt)
                val_loss_sum += loss.item() * len(tgt)
                n_val += len(tgt)
                preds_list.extend(pred.cpu().numpy().tolist())
                tgts_list.extend(tgt.cpu().numpy().tolist())
        val_loss = val_loss_sum / n_val
        rho, _ = spearmanr(preds_list, tgts_list)

        elapsed_ep = time.time() - t_ep
        print(
            f"  [{tag}] Epoch {epoch+1}/{EPOCHS} "
            f"train={train_loss:.4f} val={val_loss:.4f} rho={rho:.4f} "
            f"({elapsed_ep:.0f}s)",
            flush=True,
        )

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_cnt = 0
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
        else:
            patience_cnt += 1
            if patience_cnt >= PATIENCE:
                print(f"  [{tag}] Early stopping at epoch {epoch+1}", flush=True)
                break

    model.load_state_dict(best_state)
    model.to(device)
    model.eval()

    ckpt_path = os.path.join(CHECKPOINT_DIR, f"{tag}.pt")
    torch.save(best_state, ckpt_path)

    all_preds = []
    all_tgts = []
    with torch.no_grad():
        for batch in val_loader:
            ids = batch["input_ids"].to(device)
            mask = batch["attention_mask"].to(device)
            pred = model(ids, mask)
            all_preds.extend(pred.cpu().numpy().tolist())
            all_tgts.extend(batch["target"].numpy().tolist())

    all_preds = np.array(all_preds)
    all_tgts = np.array(all_tgts)
    rho_final, _ = spearmanr(all_preds, all_tgts)

    n_val_inst = len(val_instances)
    n_samples = 8
    pred_matrix = all_preds.reshape(n_val_inst, n_samples)
    tgt_matrix = all_tgts.reshape(n_val_inst, n_samples)

    sel_idx = np.argmax(pred_matrix, axis=1)
    deberta_sel_f1 = float(np.mean([tgt_matrix[i, sel_idx[i]] for i in range(n_val_inst)]))

    lp_sel_vals = []
    for inst in val_instances:
        logprobs = [s["logprob"] for s in inst["samples"]]
        best_lp_idx = int(np.argmax(logprobs))
        lp_sel_vals.append(inst["samples"][best_lp_idx]["f1"])
    lp_sel_f1 = float(np.mean(lp_sel_vals))

    greedy_f1 = float(np.mean([inst["greedy_f1"] for inst in val_instances]))
    oracle_f1 = float(np.mean([inst["oracle_f1"] for inst in val_instances]))

    gap = oracle_f1 - greedy_f1
    deberta_gc = (deberta_sel_f1 - greedy_f1) / gap * 100 if gap > 1e-9 else 0.0
    lp_gc = (lp_sel_f1 - greedy_f1) / gap * 100 if gap > 1e-9 else 0.0

    result = {
        "fold": fold,
        "seed": seed,
        "gpu": gpu_id,
        "spearman_rho": float(rho_final),
        "deberta_sel_f1": deberta_sel_f1,
        "deberta_gap_closure_pct": float(deberta_gc),
        "greedy_f1": greedy_f1,
        "lp_sel_f1": lp_sel_f1,
        "lp_gap_closure_pct": float(lp_gc),
        "oracle_f1": oracle_f1,
        "best_val_loss": float(best_val_loss),
    }

    result_path = os.path.join(OUTPUT_DIR, f"result_{tag}.json")
    with open(result_path, "w") as f:
        json.dump(result, f, indent=2)

    print(
        f"[{tag}] DONE rho={rho_final:.4f} sel_f1={deberta_sel_f1:.4f} gc={deberta_gc:.1f}%",
        flush=True,
    )


def coordinator_main():
    import numpy as np

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    print("Pre-downloading model...", flush=True)
    subprocess.run(
        [
            sys.executable, "-c",
            "from transformers import AutoTokenizer, AutoModel; "
            f"AutoTokenizer.from_pretrained('{MODEL_NAME}'); "
            f"AutoModel.from_pretrained('{MODEL_NAME}'); "
            "print('Model cached.')",
        ],
        check=True,
    )

    tasks = [(fold, seed) for seed in SEEDS for fold in range(N_FOLDS)]
    print(f"Total: {len(tasks)} tasks (5 folds x 3 seeds)", flush=True)

    script = os.path.abspath(__file__)
    t0 = time.time()

    for i in range(0, len(tasks), 2):
        batch = tasks[i : i + 2]
        procs = []
        for j, (fold, seed) in enumerate(batch):
            gpu = GPUS[j % len(GPUS)]
            cmd = [
                sys.executable, script, "--worker",
                "--fold", str(fold), "--seed", str(seed), "--gpu", str(gpu),
            ]
            p = subprocess.Popen(cmd)
            procs.append((p, fold, seed))
            print(f"Launched fold={fold} seed={seed} on GPU {gpu} (pid={p.pid})", flush=True)
        for p, fold, seed in procs:
            rc = p.wait()
            if rc != 0:
                print(f"WARNING: fold={fold} seed={seed} exited with code {rc}", flush=True)

    elapsed = time.time() - t0
    print(f"\nAll tasks done in {elapsed / 60:.1f} minutes", flush=True)

    all_results = []
    for seed in SEEDS:
        for fold in range(N_FOLDS):
            rpath = os.path.join(OUTPUT_DIR, f"result_fold{fold}_seed{seed}.json")
            if os.path.exists(rpath):
                with open(rpath) as f:
                    all_results.append(json.load(f))
            else:
                print(f"WARNING: missing {rpath}")

    if not all_results:
        print("No results collected!")
        return

    rhos = [r["spearman_rho"] for r in all_results]
    sel_f1s = [r["deberta_sel_f1"] for r in all_results]
    gcs = [r["deberta_gap_closure_pct"] for r in all_results]
    lp_gcs = [r["lp_gap_closure_pct"] for r in all_results]

    instances = load_data()

    output = {
        "protocol": "5-fold CV, 3 seeds",
        "model": MODEL_NAME,
        "dataset": "SciERC",
        "n_instances": len(instances),
        "n_samples_per_instance": 8,
        "per_fold_results": all_results,
        "aggregate": {
            "spearman_rho": {"mean": float(np.mean(rhos)), "std": float(np.std(rhos))},
            "selection_f1": {"mean": float(np.mean(sel_f1s)), "std": float(np.std(sel_f1s))},
            "gap_closure_pct": {"mean": float(np.mean(gcs)), "std": float(np.std(gcs))},
            "greedy_f1": float(np.mean([r["greedy_f1"] for r in all_results])),
            "lp_sel_f1": float(np.mean([r["lp_sel_f1"] for r in all_results])),
            "lp_gap_closure_pct": {
                "mean": float(np.mean(lp_gcs)),
                "std": float(np.std(lp_gcs)),
            },
            "oracle_f1": float(np.mean([r["oracle_f1"] for r in all_results])),
        },
    }

    results_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(results_path, "w") as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 60, flush=True)
    print("AGGREGATE RESULTS (15 runs)", flush=True)
    print("=" * 60, flush=True)
    print(f"Spearman rho:      {np.mean(rhos):.4f} +/- {np.std(rhos):.4f}")
    print(f"DeBERTa sel F1:    {np.mean(sel_f1s):.4f} +/- {np.std(sel_f1s):.4f}")
    print(f"DeBERTa gap close: {np.mean(gcs):.1f}% +/- {np.std(gcs):.1f}%")
    print(f"LP sel F1:         {np.mean([r['lp_sel_f1'] for r in all_results]):.4f}")
    print(f"LP gap close:      {np.mean(lp_gcs):.1f}% +/- {np.std(lp_gcs):.1f}%")
    print(f"Greedy F1:         {np.mean([r['greedy_f1'] for r in all_results]):.4f}")
    print(f"Oracle F1:         {np.mean([r['oracle_f1'] for r in all_results]):.4f}")
    print(f"\nSaved to {results_path}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--fold", type=int)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--gpu", type=int)
    args = parser.parse_args()

    if args.worker:
        worker_main(args.fold, args.seed, args.gpu)
    else:
        coordinator_main()
