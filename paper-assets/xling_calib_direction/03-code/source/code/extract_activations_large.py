"""
Extract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).

Differences from extract_activations.py:
  - Uses register_forward_hook instead of output_hidden_states=True.
    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,
    which is prohibitive for 94-layer models. Hooks capture only the target layers.
  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).
  - Incremental saving via --save_interval to survive OOM or interruption.
  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).

Output format is identical to extract_activations.py:
  layer{i}_{lang}.pt  ->  {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}

Dependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm

Usage:
  python extract_activations_large.py \
    --model Qwen/Qwen3-235B-A22B \
    --languages en zh ar hi sw ko \
    --layers 0,8,16,24,32,48,64,80,93 \
    --output_dir ./activations \
    --quantization int4 \
    --save_interval 200
"""

import argparse
import os

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm


LETTERS = ["A", "B", "C", "D"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, help="HuggingFace model name or path")
    p.add_argument("--languages", nargs="+",
                   default=["en", "zh", "ar", "hi", "sw", "ko", "es", "fr", "de", "ru",
                            "tr", "bn", "ja", "pt", "vi", "te", "id", "pl", "nl", "uk"])
    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
                   help="Comma-separated transformer layer indices (0-indexed)")
    p.add_argument("--output_dir", default="./activations")
    p.add_argument("--n_shot", type=int, default=5)
    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
    p.add_argument("--subjects", nargs="*", default=None,
                   help="Restrict to these MMLU subjects (default: all)")
    p.add_argument("--quantization", default="none", choices=["none", "int4", "int8"],
                   help="Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)")
    p.add_argument("--save_interval", type=int, default=500,
                   help="Incrementally save every N samples (0 = only save at end)")
    p.add_argument("--split_ratio", type=float, default=0.0,
                   help="If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval")
    p.add_argument("--split_seed", type=int, default=42,
                   help="Random seed for train/eval split (ensures reproducibility across languages)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data loading (identical to extract_activations.py)
# ---------------------------------------------------------------------------

def load_mmlu(language, split="test"):
    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
    if language == "en":
        return load_dataset("cais/mmlu", "all", split=split)
    return load_dataset("CohereForAI/Global-MMLU", language, split=split)


def load_mmlu_dev(language):
    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
    for split_name in ["dev", "validation"]:
        try:
            return load_mmlu(language, split_name)
        except (ValueError, KeyError):
            continue
    raise RuntimeError(f"No dev/validation split found for '{language}'")


def normalize_row(row):
    """Normalize a dataset row to {question, choices, answer(int), subject}."""
    question = row.get("question", row.get("input", ""))

    if "choices" in row and isinstance(row["choices"], list):
        choices = list(row["choices"])
    else:
        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]

    answer = row.get("answer", row.get("target", 0))
    if isinstance(answer, str):
        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)

    return {
        "question": question,
        "choices": choices,
        "answer": int(answer),
        "subject": row.get("subject", "unknown"),
    }


# ---------------------------------------------------------------------------
# Prompt formatting (identical to extract_activations.py)
# ---------------------------------------------------------------------------

def _format_question(question, choices):
    parts = [f"{question}\n"]
    for i, c in enumerate(choices):
        parts.append(f"{LETTERS[i]}. {c}\n")
    return "".join(parts)


def build_prompt(row, few_shot_rows, n_shot):
    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
    subject_pretty = row["subject"].replace("_", " ")
    lines = [
        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
    ]
    for fs in few_shot_rows[:n_shot]:
        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
        lines.append(_format_question(fs["question"], fs["choices"]))
        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
    lines.append(_format_question(row["question"], row["choices"]))
    lines.append("Answer:")
    return "".join(lines)


# ---------------------------------------------------------------------------
# Model loading with quantization support
# ---------------------------------------------------------------------------

def load_model(model_name, dtype, quantization):
    """Load model with optional INT4/INT8 quantization via bitsandbytes."""
    kwargs = dict(device_map="auto", trust_remote_code=True)

    if quantization == "int4":
        from transformers import BitsAndBytesConfig
        kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
    elif quantization == "int8":
        from transformers import BitsAndBytesConfig
        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
    else:
        kwargs["torch_dtype"] = dtype

    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
    model.eval()
    return model


# ---------------------------------------------------------------------------
# Architecture-adaptive layer access
# ---------------------------------------------------------------------------

def get_layer_modules(model):
    """Return the nn.ModuleList of transformer layers, adapting to model architecture.

    Tries common attribute paths used by different model families:
      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)
      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)
      - model.gpt_neox.layers   (GPT-NeoX variants)
    """
    candidates = [
        ("model.model.layers", lambda m: m.model.layers),
        ("model.transformer.h", lambda m: m.transformer.h),
        ("model.gpt_neox.layers", lambda m: m.gpt_neox.layers),
    ]
    for path_name, accessor in candidates:
        try:
            layers = accessor(model)
            if hasattr(layers, "__len__") and len(layers) > 0:
                print(f"  Layer access path: {path_name}  ({len(layers)} layers)")
                return layers
        except AttributeError:
            continue
    raise RuntimeError(
        "Cannot locate transformer layers. "
        "Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers"
    )


# ---------------------------------------------------------------------------
# Forward hook machinery
# ---------------------------------------------------------------------------

def get_final_norm(model):
    """Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).

    Used to apply post-norm on the last layer's hook output, matching the behavior of
    output_hidden_states=True which returns post-norm activations for the final layer.
    """
    candidates = [
        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma
        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J
        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX
    ]
    for accessor in candidates:
        try:
            norm = accessor(model)
            if norm is not None:
                return norm
        except AttributeError:
            continue
    return None


def register_activation_hooks(model, layer_indices, captured):
    """Register forward hooks on target layers to capture last-token hidden states.

    Why hooks instead of output_hidden_states=True:
      output_hidden_states materializes ALL layers' hidden states in memory at once.
      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)
      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific
      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.

    Post-norm on last layer:
      output_hidden_states returns post-norm activations for the final layer (i.e., after
      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency
      with MVP experiments that used output_hidden_states, we apply the final norm to the
      last layer's hook output. All other layers return pre-norm (direct layer output).
    """
    layers = get_layer_modules(model)
    n_layers = len(layers)
    final_norm = get_final_norm(model)
    max_target_layer = max(layer_indices)
    handles = []

    def make_hook(layer_idx):
        def hook_fn(module, input, output):
            h = output[0] if isinstance(output, tuple) else output
            h = h[0, -1]
            # Apply final norm on the last transformer layer to match output_hidden_states behavior
            if layer_idx == n_layers - 1 and final_norm is not None:
                with torch.no_grad():
                    h = final_norm(h.unsqueeze(0)).squeeze(0)
            captured[layer_idx] = h.detach().cpu().float()
        return hook_fn

    for li in layer_indices:
        if li < 0 or li >= n_layers:
            raise ValueError(f"Layer index {li} out of range [0, {n_layers})")
        handles.append(layers[li].register_forward_hook(make_hook(li)))

    return handles


def remove_hooks(handles):
    for h in handles:
        h.remove()


# ---------------------------------------------------------------------------
# Incremental save / load
# ---------------------------------------------------------------------------

def save_layer_data(storage, layer_indices, lang, output_dir,
                    train_indices=None, eval_indices=None):
    """Save accumulated activations for all target layers.

    If train_indices/eval_indices are provided, saves separate train/eval files
    instead of a single file.
    """
    for li in layer_indices:
        if not storage[li]["acts"]:
            continue
        acts = torch.stack(storage[li]["acts"])
        labels = torch.tensor(storage[li]["labels"], dtype=torch.long)

        if train_indices is not None and eval_indices is not None:
            for suffix, indices in [("train", train_indices), ("eval", eval_indices)]:
                idx = [i for i in indices if i < len(acts)]
                if not idx:
                    continue
                idx_t = torch.tensor(idx, dtype=torch.long)
                path = os.path.join(output_dir, f"layer{li}_{lang}_{suffix}.pt")
                torch.save({"activations": acts[idx_t], "labels": labels[idx_t]}, path)
        else:
            path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
            torch.save({"activations": acts, "labels": labels}, path)


def load_existing_progress(layer_indices, lang, output_dir):
    """Load previously saved data to support resumption after interruption."""
    storage = {li: {"acts": [], "labels": []} for li in layer_indices}
    n_existing = 0
    for li in layer_indices:
        path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
        if os.path.exists(path):
            data = torch.load(path, weights_only=True)
            storage[li]["acts"] = list(data["activations"].unbind(0))
            storage[li]["labels"] = data["labels"].tolist()
            n_existing = max(n_existing, len(storage[li]["labels"]))
    return storage, n_existing


# ---------------------------------------------------------------------------
# Main extraction loop
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    layer_indices = sorted(int(x) for x in args.layers.split(","))
    os.makedirs(args.output_dir, exist_ok=True)

    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
    print(f"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}")

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = load_model(args.model, dtype, args.quantization)

    n_model_layers = model.config.num_hidden_layers
    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
    for li in layer_indices:
        if li < 0 or li >= n_model_layers:
            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")

    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")

    # Split indices: computed once on the first language, reused for all
    split_train_indices = None
    split_eval_indices = None

    # Register hooks once — they persist across forward calls
    captured = {}
    handles = register_activation_hooks(model, layer_indices, captured)

    try:
        for lang_idx, lang in enumerate(args.languages):
            print(f"\n{'='*50}")
            print(f"  Language: {lang}")
            print(f"{'='*50}")

            test_ds = load_mmlu(lang, "test")
            dev_ds = load_mmlu_dev(lang)

            if args.subjects:
                test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
                dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)

            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))

            # Compute split on first language, reuse for all subsequent languages
            if args.split_ratio > 0 and split_train_indices is None:
                from sklearn.model_selection import train_test_split
                subjects = [normalize_row(test_ds[i])["subject"] for i in range(n)]
                split_train_indices, split_eval_indices = train_test_split(
                    list(range(n)), train_size=args.split_ratio,
                    stratify=subjects, random_state=args.split_seed,
                )
                split_path = os.path.join(args.output_dir, "split_indices.pt")
                torch.save({
                    "train": split_train_indices, "eval": split_eval_indices,
                    "split_ratio": args.split_ratio, "seed": args.split_seed,
                    "n_total": n, "first_lang": lang,
                }, split_path)
                print(f"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})")

            dev_by_subject: dict[str, list] = {}
            for r in dev_ds:
                dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
            dev_fallback = list(dev_ds)[:args.n_shot]

            # Try to resume from existing partial results
            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)
            if n_existing > 0:
                print(f"  Resuming from sample {n_existing} (found existing data)")

            for i in tqdm(range(n_existing, n), desc=f"[{lang}]", initial=n_existing, total=n):
                row = normalize_row(test_ds[i])
                few_shots = dev_by_subject.get(row["subject"], dev_fallback)
                prompt = build_prompt(row, few_shots, args.n_shot)

                inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
                                   max_length=4096).to(model.device)

                with torch.no_grad():
                    # No output_hidden_states — hooks capture what we need
                    out = model(**inputs)

                logits_last = out.logits[0, -1]
                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
                pred = choice_logits.argmax().item()
                correct = int(pred == row["answer"])

                for li in layer_indices:
                    storage[li]["acts"].append(captured[li])
                    storage[li]["labels"].append(correct)

                captured.clear()
                del out, inputs

                if (i + 1) % 100 == 0:
                    torch.cuda.empty_cache()

                # Incremental save
                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:
                    save_layer_data(storage, layer_indices, lang, args.output_dir,
                                    split_train_indices, split_eval_indices)
                    print(f"  [checkpoint] saved at sample {i + 1}")

            # Final save for this language
            save_layer_data(storage, layer_indices, lang, args.output_dir,
                            split_train_indices, split_eval_indices)
            for li in layer_indices:
                n_samples = len(storage[li]["labels"])
                if n_samples > 0:
                    acc = sum(storage[li]["labels"]) / n_samples
                    if split_train_indices is not None:
                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt")
                    else:
                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt")

    finally:
        # Always clean up hooks, even if an exception occurs
        remove_hooks(handles)

    print("\nExtraction complete.")


if __name__ == "__main__":
    main()
