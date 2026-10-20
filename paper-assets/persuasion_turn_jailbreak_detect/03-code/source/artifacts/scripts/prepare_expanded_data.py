"""Merge original 500 (plan_002_splits) + expanded 500 conversations into 1000-sample dataset.

Reads already-processed plan_002_splits data and raw expanded data,
normalizes expanded data to match the plan_002 format, then performs
stratified split (700/150/150) with balanced jailbreak/benign per split.
"""
import json
import argparse
import random
from pathlib import Path
from collections import Counter


PROJ = Path("/root/persuasion_turn_jailbreak_detect")


def _resolve_path(path):
    """If path doesn't exist but .progress version does, use that."""
    p = Path(path)
    if p.exists():
        return str(p)
    progress = Path(str(p) + ".progress")
    if progress.exists():
        print(f"  NOTE: {p.name} not found, using {progress.name} (in-progress)")
        return str(progress)
    raise FileNotFoundError(f"Neither {p} nor {progress} found. Is generation still running?")


def load_processed(directory):
    """Load already-processed data from plan_002_splits (train+val+test)."""
    convs = []
    for split in ["train.jsonl", "val.jsonl", "test.jsonl"]:
        path = Path(directory) / split
        if not path.exists():
            print(f"  WARNING: {path} not found, skipping")
            continue
        with open(path) as f:
            for line in f:
                if line.strip():
                    c = json.loads(line.strip())
                    c["_origin"] = "original"
                    convs.append(c)
    return convs


def load_expanded_jailbreak(path):
    """Load raw expanded jailbreak data and normalize to plan_002 format."""
    convs = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            c = json.loads(line.strip())
            new_turns = []
            for t in c["turns"]:
                nt = dict(t)
                if t["role"] == "user" and "intended_strategy" in t:
                    nt["persuasion_strategy"] = t["intended_strategy"] + 1
                elif t["role"] == "user":
                    nt["persuasion_strategy"] = 0
                new_turns.append(nt)
            raw_id = c.get("conv_id", c.get("conversation_id"))
            cid = f"exp_jb_{raw_id}" if not raw_id.startswith("exp_jb_") else raw_id
            convs.append({
                "conversation_id": cid,
                "turns": new_turns,
                "label": "jailbreak",
                "source": c.get("source", "qwen3-8b-crescendo-expanded"),
                "attack_type": c.get("attack_type", c.get("playbook_name", "crescendo")),
                "_origin": "expanded",
            })
    return convs


def load_expanded_benign(path):
    """Load raw expanded benign data and normalize to plan_002 format."""
    convs = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            c = json.loads(line.strip())
            new_turns = []
            for t in c["turns"]:
                nt = dict(t)
                if t["role"] == "user":
                    nt["persuasion_strategy"] = 0
                new_turns.append(nt)
            raw_id = c.get("conversation_id", "")
            cid = f"exp_bn_{raw_id}" if not raw_id.startswith("exp_bn_") else raw_id
            convs.append({
                "conversation_id": cid,
                "turns": new_turns,
                "label": "benign",
                "source": c.get("source", "qwen3-8b-crescendo-expanded"),
                "_origin": "expanded",
            })
    return convs


def stratified_split(convs, train_ratio=0.7, val_ratio=0.15, seed=42):
    random.seed(seed)
    jailbreak = [c for c in convs if c["label"] == "jailbreak"]
    benign = [c for c in convs if c["label"] == "benign"]
    random.shuffle(jailbreak)
    random.shuffle(benign)

    def split_list(lst, tr, vr):
        n = len(lst)
        n_train = int(n * tr)
        n_val = int(n * vr)
        return lst[:n_train], lst[n_train:n_train + n_val], lst[n_train + n_val:]

    j_train, j_val, j_test = split_list(jailbreak, train_ratio, val_ratio)
    b_train, b_val, b_test = split_list(benign, train_ratio, val_ratio)

    train = j_train + b_train
    val = j_val + b_val
    test = j_test + b_test
    random.shuffle(train)
    random.shuffle(val)
    random.shuffle(test)
    return train, val, test


def save_jsonl(data, path):
    with open(path, "w") as f:
        for item in data:
            out = {k: v for k, v in item.items() if not k.startswith("_")}
            f.write(json.dumps(out, ensure_ascii=False) + "\n")


def print_stats(name, data):
    labels = Counter(c["label"] for c in data)
    origins = Counter(c.get("_origin", "unknown") for c in data)
    origin_label = Counter((c.get("_origin", "unknown"), c["label"]) for c in data)

    print(f"\n{name}: {len(data)} total")
    print(f"  Labels: {dict(labels)}")
    print(f"  Origin: {dict(origins)}")
    print(f"  Origin x Label:")
    for (origin, label), cnt in sorted(origin_label.items()):
        print(f"    {origin}/{label}: {cnt}")


def main():
    parser = argparse.ArgumentParser(description="Merge original + expanded data for exp17")
    parser.add_argument("--original_dir", type=str,
                        default=str(PROJ / "data/plan_002_splits"),
                        help="Directory with original processed splits")
    parser.add_argument("--expanded_jailbreak", type=str,
                        default=str(PROJ / "data/expanded_conversations/crescendo_jailbreak_expanded.jsonl"))
    parser.add_argument("--expanded_benign", type=str,
                        default=str(PROJ / "data/expanded_conversations/crescendo_benign_expanded.jsonl"))
    parser.add_argument("--output_dir", type=str,
                        default=str(PROJ / "data/expanded_1000"))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry_run", action="store_true")
    args = parser.parse_args()

    print("=== Loading Original Data ===")
    original = load_processed(args.original_dir)
    print(f"  Loaded {len(original)} conversations from {args.original_dir}")

    print("\n=== Loading Expanded Data ===")
    jb_path = _resolve_path(args.expanded_jailbreak)
    bn_path = _resolve_path(args.expanded_benign)
    exp_jb = load_expanded_jailbreak(jb_path)
    print(f"  Jailbreak: {len(exp_jb)} from {jb_path}")
    exp_bn = load_expanded_benign(bn_path)
    print(f"  Benign: {len(exp_bn)} from {bn_path}")

    all_convs = original + exp_jb + exp_bn
    print(f"\nTotal: {len(all_convs)} conversations")

    # Check for duplicate IDs
    ids = [c["conversation_id"] for c in all_convs]
    dupes = [id for id, cnt in Counter(ids).items() if cnt > 1]
    if dupes:
        print(f"  WARNING: {len(dupes)} duplicate conversation IDs, deduplicating by first occurrence")
        seen = set()
        deduped = []
        for c in all_convs:
            if c["conversation_id"] not in seen:
                seen.add(c["conversation_id"])
                deduped.append(c)
        all_convs = deduped
        print(f"  After dedup: {len(all_convs)}")

    print_stats("All Data", all_convs)

    train, val, test = stratified_split(all_convs, seed=args.seed)

    print_stats("Train", train)
    print_stats("Val", val)
    print_stats("Test", test)

    if not args.dry_run:
        out = Path(args.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        save_jsonl(train, out / "train.jsonl")
        save_jsonl(val, out / "val.jsonl")
        save_jsonl(test, out / "test.jsonl")
        print(f"\nSaved to {out}/")
        print(f"  train.jsonl: {len(train)}")
        print(f"  val.jsonl: {len(val)}")
        print(f"  test.jsonl: {len(test)}")
    else:
        print("\n[DRY RUN] No files written.")


if __name__ == "__main__":
    main()
