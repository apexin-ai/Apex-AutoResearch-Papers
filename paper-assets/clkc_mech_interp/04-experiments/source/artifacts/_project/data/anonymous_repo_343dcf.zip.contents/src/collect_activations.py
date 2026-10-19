"""Collect residual stream activations from all transformer layers.

Loads a causal LM, feeds each sample's (question + context) prompt through
the model, hooks every layer's output, and saves the last-token hidden state
per layer.

Input:  JSONL files in --data_dir  (e.g. en_conflict_train.jsonl)
Output: {lang}_activations.pt  containing:
        - "activations": Tensor (N, num_layers, hidden_dim)
        - "labels":      Tensor (N,)  (0 = no_conflict, 1 = conflict)
        - "split_sizes": dict {"train": int, "test": int}
"""

import argparse
import json
import os
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


LABEL_MAP = {"no_conflict": 0, "conflict": 1}


def load_jsonl(path: str) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f]


def build_prompt(sample: dict) -> str:
    return (
        f"Context: {sample['context']}\n"
        f"Question: {sample['question']}\n"
        f"Answer:"
    )


def collect(
    model,
    tokenizer,
    samples: list[dict],
    batch_size: int,
    device: str,
) -> tuple[torch.Tensor, torch.Tensor]:
    num_layers = model.config.num_hidden_layers
    all_activations = []
    all_labels = []

    for start in range(0, len(samples), batch_size):
        batch = samples[start : start + batch_size]
        prompts = [build_prompt(s) for s in batch]
        labels = [LABEL_MAP[s["label"]] for s in batch]

        inputs = tokenizer(
            prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(device)

        layer_outputs: dict[int, torch.Tensor] = {}
        hooks = []

        def make_hook(layer_idx):
            def hook_fn(module, input, output):
                hidden = output[0] if isinstance(output, tuple) else output
                layer_outputs[layer_idx] = hidden.detach()
            return hook_fn

        for idx, layer in enumerate(model.model.layers):
            hooks.append(layer.register_forward_hook(make_hook(idx)))

        with torch.no_grad():
            model(**inputs)

        for h in hooks:
            h.remove()

        seq_lengths = inputs["attention_mask"].sum(dim=1)
        batch_acts = []
        for i in range(len(batch)):
            last_pos = inputs["input_ids"].shape[1] - 1
            sample_layers = []
            for l in range(num_layers):
                sample_layers.append(layer_outputs[l][i, last_pos, :].cpu())
            batch_acts.append(torch.stack(sample_layers))

        all_activations.extend(batch_acts)
        all_labels.extend(labels)

        print(f"  Processed {min(start + batch_size, len(samples))}/{len(samples)} samples")

    activations = torch.stack(all_activations)
    labels = torch.tensor(all_labels, dtype=torch.long)
    return activations, labels


def main():
    parser = argparse.ArgumentParser(description="Collect residual stream activations")
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--lang", type=str, default="en", choices=["en", "zh", "de"])
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--train_file", type=str, default=None,
                        help="Override train JSONL path")
    parser.add_argument("--test_file", type=str, default=None,
                        help="Override test JSONL path")
    args = parser.parse_args()

    output_dir = args.output_dir or args.data_dir

    if args.train_file and args.test_file:
        train_path = Path(args.train_file)
        test_path = Path(args.test_file)
    else:
        suffix = "_verified" if args.lang == "en" else ("_validated" if args.lang == "zh" else "")
        train_path = Path(args.data_dir) / f"{args.lang}_conflict_train{suffix}.jsonl"
        test_path = Path(args.data_dir) / f"{args.lang}_conflict_test{suffix}.jsonl"

    if not train_path.exists():
        raise FileNotFoundError(f"Train file not found: {train_path}")
    if not test_path.exists():
        raise FileNotFoundError(f"Test file not found: {test_path}")

    train_data = load_jsonl(str(train_path))
    test_data = load_jsonl(str(test_path))
    print(f"[{args.lang}] Loaded {len(train_data)} train + {len(test_data)} test samples")

    print(f"Loading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    device = next(model.parameters()).device
    print(f"Model loaded on {device}, layers={model.config.num_hidden_layers}, "
          f"hidden_dim={model.config.hidden_size}")

    all_samples = train_data + test_data

    print(f"Collecting activations for {len(all_samples)} samples...")
    activations, labels = collect(model, tokenizer, all_samples, args.batch_size, device)

    os.makedirs(output_dir, exist_ok=True)
    out_path = Path(output_dir) / f"{args.lang}_activations.pt"
    torch.save(
        {
            "activations": activations,
            "labels": labels,
            "split_sizes": {"train": len(train_data), "test": len(test_data)},
        },
        out_path,
    )
    print(f"Saved activations to {out_path}  shape={activations.shape}")


if __name__ == "__main__":
    main()
