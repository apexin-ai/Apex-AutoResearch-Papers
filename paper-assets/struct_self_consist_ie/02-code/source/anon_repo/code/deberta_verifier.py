#!/usr/bin/env python3
"""DeBERTa Representation Verifier for structured output quality prediction."""
import json
import argparse
import random
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModel, get_linear_schedule_with_warmup

SEED = 42


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def entity_set(ext):
    return {(e["start"], e["end"], e["type"]) for e in ext.get("entities", [])}


def compute_entity_f1(pred, gold):
    pred_set = entity_set(pred)
    gold_set = entity_set(gold)
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / (tp + len(pred_set - gold_set))
    r = tp / (tp + len(gold_set - pred_set))
    return 2 * p * r / (p + r)


def serialize_entities(ext):
    ents = ext.get("entities", [])
    if not ents:
        return "No entities found."
    parts = [f"{e['text']} ({e['type']})" for e in ents]
    return "; ".join(parts)


def load_data(path, max_instances=None):
    data = []
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            gold = d["gold"]
            if isinstance(gold, dict) and not gold.get("entities"):
                continue
            if isinstance(gold, list) and not gold:
                continue
            data.append(d)
    if max_instances and len(data) > max_instances:
        random.seed(SEED)
        random.shuffle(data)
        data = data[:max_instances]
    return data


def prepare_examples(instances):
    examples = []
    for inst in instances:
        text = inst["text"]
        gold = inst["gold"]
        for sample in inst["samples"]:
            f1 = compute_entity_f1(sample, gold)
            output_text = serialize_entities(sample)
            examples.append({
                "input_text": text,
                "output_text": output_text,
                "f1": f1,
            })
    return examples


def split_instances(instances, train_ratio=0.8, seed=SEED):
    rng = random.Random(seed)
    idxs = list(range(len(instances)))
    rng.shuffle(idxs)
    n_train = int(len(instances) * train_ratio)
    train = [instances[i] for i in idxs[:n_train]]
    test = [instances[i] for i in idxs[n_train:]]
    return train, test


class VerifierDataset(Dataset):
    def __init__(self, examples, tokenizer, max_length=512):
        self.examples = examples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        ex = self.examples[idx]
        encoding = self.tokenizer(
            ex["input_text"],
            ex["output_text"],
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "token_type_ids": encoding.get("token_type_ids", torch.zeros_like(encoding["input_ids"])).squeeze(0),
            "label": torch.tensor(ex["f1"], dtype=torch.float32),
        }


class DeBERTaVerifier(nn.Module):
    def __init__(self, model_name="microsoft/deberta-v3-base"):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden_size = self.encoder.config.hidden_size
        self.regressor = nn.Sequential(
            nn.Dropout(0.1),
            nn.Linear(hidden_size, 1),
        )

    def forward(self, input_ids, attention_mask, token_type_ids=None):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        cls_repr = outputs.last_hidden_state[:, 0, :]
        return self.regressor(cls_repr).squeeze(-1)


def train_model(model, train_loader, val_loader, device, epochs=3, lr=2e-5, warmup_ratio=0.1):
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    total_steps = len(train_loader) * epochs
    warmup_steps = int(total_steps * warmup_ratio)
    scheduler = get_linear_schedule_with_warmup(optimizer, warmup_steps, total_steps)
    criterion = nn.MSELoss()

    best_val_loss = float("inf")
    best_state = None

    for epoch in range(epochs):
        model.train()
        train_loss = 0.0
        for batch in train_loader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            token_type_ids = batch["token_type_ids"].to(device)
            labels = batch["label"].to(device)

            preds = model(input_ids, attention_mask, token_type_ids)
            loss = criterion(preds, labels)

            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()

            train_loss += loss.item()

        avg_train_loss = train_loss / len(train_loader)

        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for batch in val_loader:
                input_ids = batch["input_ids"].to(device)
                attention_mask = batch["attention_mask"].to(device)
                token_type_ids = batch["token_type_ids"].to(device)
                labels = batch["label"].to(device)
                preds = model(input_ids, attention_mask, token_type_ids)
                loss = criterion(preds, labels)
                val_loss += loss.item()

        avg_val_loss = val_loss / len(val_loader)
        print(f"  Epoch {epoch+1}/{epochs}: train_loss={avg_train_loss:.4f}, val_loss={avg_val_loss:.4f}")

        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    if best_state:
        model.load_state_dict(best_state)
    return model


def evaluate_selection(model, instances, tokenizer, device, max_length=512):
    model.eval()
    greedy_f1s = []
    oracle_f1s = []
    verifier_sel_f1s = []
    lp_sel_f1s = []

    with torch.no_grad():
        for inst in instances:
            text = inst["text"]
            gold = inst["gold"]
            samples = inst["samples"]
            logprobs = inst.get("logprobs", [s.get("mean_logprob", 0) for s in samples])

            sample_f1s = [compute_entity_f1(s, gold) for s in samples]
            greedy_f1 = compute_entity_f1(inst["greedy"], gold)

            oracle_f1 = max(sample_f1s)
            lp_best_idx = int(np.argmax(logprobs))
            lp_sel_f1 = sample_f1s[lp_best_idx]

            pred_scores = []
            for sample in samples:
                output_text = serialize_entities(sample)
                encoding = tokenizer(
                    text, output_text,
                    max_length=max_length, padding="max_length",
                    truncation=True, return_tensors="pt",
                )
                input_ids = encoding["input_ids"].to(device)
                attention_mask = encoding["attention_mask"].to(device)
                token_type_ids = encoding.get("token_type_ids", torch.zeros_like(input_ids)).to(device)
                score = model(input_ids, attention_mask, token_type_ids).item()
                pred_scores.append(score)

            verifier_best_idx = int(np.argmax(pred_scores))
            verifier_sel_f1 = sample_f1s[verifier_best_idx]

            greedy_f1s.append(greedy_f1)
            oracle_f1s.append(oracle_f1)
            verifier_sel_f1s.append(verifier_sel_f1)
            lp_sel_f1s.append(lp_sel_f1)

    greedy_avg = np.mean(greedy_f1s)
    oracle_avg = np.mean(oracle_f1s)
    verifier_avg = np.mean(verifier_sel_f1s)
    lp_avg = np.mean(lp_sel_f1s)
    gap = oracle_avg - greedy_avg
    verifier_closure = (verifier_avg - greedy_avg) / gap * 100 if gap > 0 else 0
    lp_closure = (lp_avg - greedy_avg) / gap * 100 if gap > 0 else 0

    return {
        "greedy_f1": float(greedy_avg),
        "lp_sel_f1": float(lp_avg),
        "verifier_sel_f1": float(verifier_avg),
        "oracle_f1": float(oracle_avg),
        "lp_gap_closure": float(lp_closure),
        "verifier_gap_closure": float(verifier_closure),
        "n_instances": len(instances),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=["scierc", "fewnerd"], required=True)
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--model_name", default="microsoft/deberta-v3-base")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--max_instances", type=int, default=None)
    parser.add_argument("--save_path", default=None)
    parser.add_argument("--eval_only", default=None)
    parser.add_argument("--cross_eval_path", default=None)
    args = parser.parse_args()

    set_seed(SEED)
    device = torch.device(args.device)

    print(f"Loading data from {args.data_path}...")
    instances = load_data(args.data_path, max_instances=args.max_instances)
    print(f"  Gold-filtered instances: {len(instances)}")

    train_insts, test_insts = split_instances(instances)
    print(f"  Train: {len(train_insts)} instances, Test: {len(test_insts)} instances")

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)

    if args.eval_only:
        print(f"Loading model from {args.eval_only}...")
        model = DeBERTaVerifier(args.model_name).to(device)
        model.load_state_dict(torch.load(args.eval_only, map_location=device, weights_only=True))
    else:
        train_examples = prepare_examples(train_insts)
        test_examples = prepare_examples(test_insts)
        print(f"  Train examples: {len(train_examples)}, Test examples: {len(test_examples)}")

        train_dataset = VerifierDataset(train_examples, tokenizer, args.max_length)
        test_dataset = VerifierDataset(test_examples, tokenizer, args.max_length)

        train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=2)
        val_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, num_workers=2)

        print(f"Training DeBERTa verifier on {args.dataset} ({args.device})...")
        model = DeBERTaVerifier(args.model_name).to(device)
        model = train_model(model, train_loader, val_loader, device, epochs=args.epochs, lr=args.lr)

        if args.save_path:
            torch.save(model.state_dict(), args.save_path)
            print(f"  Model saved to {args.save_path}")

    print(f"\nEvaluating selection on {args.dataset} test set...")
    results = evaluate_selection(model, test_insts, tokenizer, device, args.max_length)

    print(f"\n{'='*60}")
    print(f"Results: {args.dataset}")
    print(f"{'='*60}")
    print(f"  Greedy F1:          {results['greedy_f1']:.4f}")
    print(f"  LP Selection F1:    {results['lp_sel_f1']:.4f}  (gap closure: {results['lp_gap_closure']:.1f}%)")
    print(f"  Verifier Sel F1:    {results['verifier_sel_f1']:.4f}  (gap closure: {results['verifier_gap_closure']:.1f}%)")
    print(f"  Oracle F1:          {results['oracle_f1']:.4f}")
    print(f"  N test instances:   {results['n_instances']}")

    result_out = {args.dataset: results}

    if args.cross_eval_path:
        print(f"\nCross-dataset evaluation on {args.cross_eval_path}...")
        cross_instances = load_data(args.cross_eval_path)
        _, cross_test = split_instances(cross_instances)
        cross_results = evaluate_selection(model, cross_test, tokenizer, device, args.max_length)
        cross_name = "fewnerd" if args.dataset == "scierc" else "scierc"
        print(f"\n{'='*60}")
        print(f"Cross-dataset: {args.dataset} -> {cross_name}")
        print(f"{'='*60}")
        print(f"  Greedy F1:          {cross_results['greedy_f1']:.4f}")
        print(f"  LP Selection F1:    {cross_results['lp_sel_f1']:.4f}  (gap closure: {cross_results['lp_gap_closure']:.1f}%)")
        print(f"  Verifier Sel F1:    {cross_results['verifier_sel_f1']:.4f}  (gap closure: {cross_results['verifier_gap_closure']:.1f}%)")
        print(f"  Oracle F1:          {cross_results['oracle_f1']:.4f}")
        result_out[f"{args.dataset}_to_{cross_name}"] = cross_results

    out_path = args.save_path.replace(".pt", "_results.json") if args.save_path else f"/root/autodl-tmp/struct_self_consist_ie/output/deberta_verifier_{args.dataset}_results.json"
    with open(out_path, "w") as f:
        json.dump(result_out, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
