"""exp17 evaluation: all 9 checkpoints on DD OOD, AA OOD, ToxicChat + comparison with 500-sample results."""
import sys
import json
import argparse
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from collections import defaultdict
from sklearn.metrics import f1_score, precision_score, recall_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.gru_classifier import GRUClassifier
from src.models.deberta_multitask import DeBERTaMultiTask
from transformers import AutoTokenizer, AutoModel

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
MODEL_NAME = "microsoft/deberta-v3-base"
MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def load_encoder(mode, deberta_checkpoint, device):
    if mode == "treatment" and deberta_checkpoint:
        ckpt_path = Path(deberta_checkpoint)
        model_pt = ckpt_path / "model.pt"
        if model_pt.exists():
            model = DeBERTaMultiTask(model_name=MODEL_NAME)
            state_dict = torch.load(model_pt, map_location="cpu")
            model.load_state_dict(state_dict)
            encoder = model.deberta
        else:
            encoder = AutoModel.from_pretrained(str(ckpt_path))
    else:
        encoder = AutoModel.from_pretrained(MODEL_NAME)
    encoder.eval()
    for p in encoder.parameters():
        p.requires_grad = False
    return encoder.to(device)


def embed_turns(encoder, tokenizer, turns, device):
    if len(turns) == 0:
        turns = [""]
    enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        return out.last_hidden_state[:, 0, :]


def eval_set(encoder, gru, tokenizer, convs, device):
    gru.eval()
    all_preds, all_labels = [], []
    for c in convs:
        turns = extract_user_turns(c)
        embs = embed_turns(encoder, tokenizer, turns, device)
        embs_padded = embs.unsqueeze(0)
        lengths = torch.tensor([embs.size(0)], dtype=torch.long).to(device)
        with torch.no_grad():
            logits = gru(embs_padded, lengths)
            pred = logits.argmax(dim=1).item()
        all_preds.append(pred)
        all_labels.append(get_label(c))

    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)
    return {
        "f1_macro": float(f1_score(all_labels, all_preds, average="macro")),
        "precision": float(precision_score(all_labels, all_preds, average="macro", zero_division=0)),
        "recall": float(recall_score(all_labels, all_preds, average="macro", zero_division=0)),
        "n": len(all_labels),
        "n_jailbreak": int(all_labels.sum()),
        "n_benign": int((all_labels == 0).sum()),
    }


VARIANT_CONFIGS = {
    "vanilla": {
        "mode": "baseline",
        "gru_subpath": "baseline/best.pt",
        "deberta_subpath": None,
    },
    "mlm": {
        "mode": "treatment",
        "gru_subpath": "treatment/best.pt",
        "deberta_subpath": "deberta_mlm/best",
    },
    "9class": {
        "mode": "treatment",
        "gru_subpath": "treatment/best.pt",
        "deberta_subpath": "deberta_multitask/best",
    },
}


def resolve_checkpoint_paths(ckpt_dir, variant, seed):
    cfg = VARIANT_CONFIGS[variant]
    base = Path(ckpt_dir) / f"{variant}_seed{seed}"
    gru_path = base / cfg["gru_subpath"]
    deberta_path = base / cfg["deberta_subpath"] if cfg["deberta_subpath"] else None
    return cfg["mode"], str(gru_path), str(deberta_path) if deberta_path else None


def main():
    parser = argparse.ArgumentParser(description="exp17 evaluation across OOD benchmarks")
    parser.add_argument("--ckpt_dir", type=str, default=str(PROJ / "checkpoints/exp17"))
    parser.add_argument("--data_dir", type=str, default=str(PROJ / "data/expanded_1000"))
    parser.add_argument("--dd_ood", type=str, default=str(PROJ / "data/generated/deceptive_delight_all.jsonl"))
    parser.add_argument("--aa_ood", type=str, default=str(PROJ / "data/actorattack_ood/actorattack_all.jsonl"))
    parser.add_argument("--toxicchat", type=str, default=str(PROJ / "data/mhj/toxicchat_plan002_eval.jsonl"))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_file", type=str, default=str(PROJ / "results/exp17_eval.json"))
    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 123, 456])
    parser.add_argument("--variants", type=str, nargs="+", default=["vanilla", "mlm", "9class"])
    parser.add_argument("--ref_500_file", type=str, default=None,
                        help="JSON file with 500-sample results for comparison")
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    # Load test data
    test_data = load_jsonl(Path(args.data_dir) / "test.jsonl")
    test_benign = [c for c in test_data if c["label"] == "benign"]

    dd_jb = load_jsonl(args.dd_ood)
    dd_test = dd_jb + test_benign
    print(f"DD OOD: {len(dd_jb)} jailbreak + {len(test_benign)} benign = {len(dd_test)}")

    aa_jb = load_jsonl(args.aa_ood)
    aa_test = aa_jb + test_benign
    print(f"AA OOD: {len(aa_jb)} jailbreak + {len(test_benign)} benign = {len(aa_test)}")

    tc_test = load_jsonl(args.toxicchat)
    tc_jb = sum(1 for c in tc_test if c["label"] == "jailbreak")
    print(f"ToxicChat: {tc_jb} jailbreak + {len(tc_test) - tc_jb} benign = {len(tc_test)}")

    benchmarks = {
        "dd_ood": dd_test,
        "aa_ood": aa_test,
        "toxicchat": tc_test,
        "iid": test_data,
    }

    results = {}
    rows = []

    for variant in args.variants:
        for seed in args.seeds:
            key = f"{variant}_seed{seed}"
            print(f"\n{'='*60}")
            print(f"Evaluating: {key}")

            mode, gru_path, deberta_path = resolve_checkpoint_paths(args.ckpt_dir, variant, seed)

            if not Path(gru_path).exists():
                print(f"  SKIP: GRU checkpoint not found at {gru_path}")
                continue

            encoder = load_encoder(mode, deberta_path, device)
            gru = GRUClassifier(
                input_dim=encoder.config.hidden_size,
                hidden_dim=GRU_HIDDEN,
                num_layers=GRU_LAYERS,
                dropout=GRU_DROPOUT,
            )
            gru.load_state_dict(torch.load(gru_path, map_location="cpu"))
            gru.to(device)

            results[key] = {}
            row = {"variant": variant, "seed": seed}

            for bench_name, bench_data in benchmarks.items():
                r = eval_set(encoder, gru, tokenizer, bench_data, device)
                results[key][bench_name] = r
                row[f"{bench_name}_f1"] = r["f1_macro"]
                print(f"  {bench_name}: F1={r['f1_macro']:.4f} P={r['precision']:.4f} R={r['recall']:.4f}")

            rows.append(row)

            del encoder, gru
            torch.cuda.empty_cache()

    # Summary table
    print(f"\n{'='*80}")
    print("SUMMARY TABLE")
    print(f"{'='*80}")
    header = f"{'Variant':<10} {'Seed':<6} {'DD F1':>8} {'AA F1':>8} {'TC F1':>8} {'IID F1':>8}"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(f"{row['variant']:<10} {row['seed']:<6} "
              f"{row.get('dd_ood_f1', 0):.4f}   "
              f"{row.get('aa_ood_f1', 0):.4f}   "
              f"{row.get('toxicchat_f1', 0):.4f}   "
              f"{row.get('iid_f1', 0):.4f}")

    # Per-variant averages
    print(f"\n{'='*80}")
    print("PER-VARIANT AVERAGES (mean +/- std across seeds)")
    print(f"{'='*80}")
    for variant in args.variants:
        variant_rows = [r for r in rows if r["variant"] == variant]
        if not variant_rows:
            continue
        print(f"\n{variant}:")
        for bench in ["dd_ood", "aa_ood", "toxicchat", "iid"]:
            vals = [r.get(f"{bench}_f1", 0) for r in variant_rows]
            if vals:
                print(f"  {bench:<12}: {np.mean(vals):.4f} +/- {np.std(vals):.4f}")

    # Save
    output = {
        "experiment": "exp17_dataset_scale",
        "description": "3 variants x 3 seeds on expanded 1000-sample dataset",
        "data_dir": args.data_dir,
        "results": results,
        "summary_rows": rows,
    }

    if args.ref_500_file and Path(args.ref_500_file).exists():
        ref = json.loads(Path(args.ref_500_file).read_text())
        output["reference_500"] = ref

    Path(args.output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {args.output_file}")


if __name__ == "__main__":
    main()
