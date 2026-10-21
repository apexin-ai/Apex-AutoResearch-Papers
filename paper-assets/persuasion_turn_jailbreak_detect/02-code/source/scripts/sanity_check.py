#!/usr/bin/env python3
"""Sanity check: DeBERTa embeddings + LogisticRegression to verify distributional distance."""

import json
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from transformers import AutoTokenizer, AutoModel
import torch

CRESCENDO_FILE = Path("/root/persuasion_turn_jailbreak_detect/data/generated/crescendo_conversations.jsonl")
WILDCHAT_FILE = Path("/root/persuasion_turn_jailbreak_detect/data/wildchat_benign_226.jsonl")
STATS_FILE = Path("/root/persuasion_turn_jailbreak_detect/data/generated/generation_stats.json")
MODEL_NAME = "microsoft/deberta-v3-base"
CACHE_DIR = "/root/autodl-tmp/hf_cache"


def extract_user_turns(conversation):
    turns = conversation.get("turns", conversation.get("messages", []))
    return [t["content"] for t in turns if t["role"] == "user"]


def embed_conversations(conversations, tokenizer, model, device, max_len=512):
    embeddings = []
    for conv in conversations:
        user_texts = extract_user_turns(conv)
        if not user_texts:
            embeddings.append(np.zeros(768))
            continue
        combined = " [SEP] ".join(user_texts)[:2000]
        inputs = tokenizer(combined, return_tensors="pt", truncation=True, max_length=max_len, padding=True).to(device)
        with torch.no_grad():
            outputs = model(**inputs)
        emb = outputs.last_hidden_state.mean(dim=1).cpu().numpy()[0]
        embeddings.append(emb)
    return np.array(embeddings)


def main():
    device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
    model = AutoModel.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR).to(device).eval()

    crescendo = []
    with open(CRESCENDO_FILE) as f:
        for line in f:
            crescendo.append(json.loads(line))
    print(f"Loaded {len(crescendo)} crescendo conversations")

    wildchat = []
    with open(WILDCHAT_FILE) as f:
        for line in f:
            wildchat.append(json.loads(line))
    print(f"Loaded {len(wildchat)} wildchat conversations")

    print("Embedding crescendo conversations...")
    X_crescendo = embed_conversations(crescendo, tokenizer, model, device)
    print("Embedding wildchat conversations...")
    X_wildchat = embed_conversations(wildchat, tokenizer, model, device)

    X = np.vstack([X_crescendo, X_wildchat])
    y = np.array([1] * len(X_crescendo) + [0] * len(X_wildchat))

    clf = LogisticRegression(max_iter=1000, random_state=42)
    scores = cross_val_score(clf, X, y, cv=5, scoring="f1")

    mean_f1 = scores.mean()
    std_f1 = scores.std()
    print(f"\nSanity Check Results:")
    print(f"  5-fold CV F1: {mean_f1:.4f} +/- {std_f1:.4f}")

    if mean_f1 > 0.90:
        print("  WARNING: F1 > 0.90 -- distributional shortcut detected!")
    elif mean_f1 < 0.70:
        print("  NOTE: F1 < 0.70 -- conversations may be too similar to benign")
    else:
        print("  OK: F1 in target range [0.70, 0.90]")

    if STATS_FILE.exists():
        with open(STATS_FILE) as f:
            stats = json.load(f)
    else:
        stats = {}

    stats["sanity_check_f1"] = {
        "mean": round(mean_f1, 4),
        "std": round(std_f1, 4),
        "per_fold": [round(s, 4) for s in scores.tolist()],
    }

    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print(f"Stats saved to {STATS_FILE}")


if __name__ == "__main__":
    main()
