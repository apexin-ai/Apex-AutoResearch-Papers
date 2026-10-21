"""OOD perplexity evaluation: OpenWebText + Wikipedia."""
import argparse
import json
import math
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_ood_texts(dataset_name, max_docs=5000, cache_dir="/root/autodl-tmp/.hf_cache"):
    from datasets import load_dataset
    cache_jsonl = os.path.join(cache_dir, f"ood_{dataset_name}_{max_docs}.jsonl")
    if os.path.exists(cache_jsonl):
        print(f"  Loading cached {cache_jsonl}")
        texts = []
        with open(cache_jsonl) as f:
            for line in f:
                texts.append(json.loads(line)["text"])
        return texts

    print(f"  Downloading {dataset_name} from HuggingFace...")
    if dataset_name == "openwebtext":
        ds = load_dataset("openwebtext", split="train", streaming=True,
                          cache_dir=cache_dir, trust_remote_code=True)
        text_key = "text"
    elif dataset_name == "wikipedia":
        ds = load_dataset("wikipedia", "20220301.en", split="train",
                          streaming=True, cache_dir=cache_dir, trust_remote_code=True)
        text_key = "text"
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    texts = []
    os.makedirs(os.path.dirname(cache_jsonl), exist_ok=True)
    with open(cache_jsonl, "w") as f:
        for i, example in enumerate(ds):
            if i >= max_docs:
                break
            t = example[text_key]
            if len(t.strip()) < 50:
                max_docs += 1
                continue
            texts.append(t)
            f.write(json.dumps({"text": t}) + "\n")
    print(f"  Cached {len(texts)} docs to {cache_jsonl}")
    return texts


def eval_perplexity(model, tokenizer, texts, max_length=2048):
    stride = max_length // 2
    device = next(model.parameters()).device
    total_nll = 0.0
    total_tokens = 0

    for doc_idx, text in enumerate(texts):
        encodings = tokenizer(text, return_tensors="pt", truncation=False)
        input_ids = encodings.input_ids[0]
        seq_len = input_ids.size(0)
        if seq_len < 2:
            continue

        for begin in range(0, seq_len, stride):
            end = min(begin + max_length, seq_len)
            target_begin = max(begin, stride) if begin > 0 else 1

            ids = input_ids[begin:end].unsqueeze(0).to(device)
            target_ids = ids.clone()
            target_ids[0, :target_begin - begin] = -100

            with torch.no_grad(), torch.amp.autocast("cuda"):
                outputs = model(ids, labels=target_ids)

            n_tokens = (target_ids[0] != -100).sum().item()
            if n_tokens > 0:
                total_nll += outputs.loss.float().item() * n_tokens
                total_tokens += n_tokens

            if end == seq_len:
                break

        if (doc_idx + 1) % 500 == 0:
            interim_loss = total_nll / total_tokens if total_tokens else 0
            print(f"  [{doc_idx+1}/{len(texts)}] tokens={total_tokens}, loss={interim_loss:.4f}")

    avg_loss = total_nll / total_tokens if total_tokens > 0 else float("inf")
    avg_ppl = math.exp(avg_loss) if avg_loss < 30 else float("inf")
    return {"loss": round(avg_loss, 4), "perplexity": round(avg_ppl, 2), "num_tokens": total_tokens}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoints", nargs="+", required=True)
    parser.add_argument("--datasets", nargs="+", default=["openwebtext", "wikipedia"])
    parser.add_argument("--max_docs", type=int, default=5000)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--output_path", type=str, default=None)
    parser.add_argument("--fp16", action="store_true")
    args = parser.parse_args()

    ood_data = {}
    for ds_name in args.datasets:
        print(f"\nLoading OOD dataset: {ds_name}")
        ood_data[ds_name] = load_ood_texts(ds_name, max_docs=args.max_docs)
        print(f"  {ds_name}: {len(ood_data[ds_name])} documents")

    results = {}
    for ckpt_path in args.checkpoints:
        ckpt_path = ckpt_path.rstrip("/")
        if not os.path.exists(ckpt_path):
            print(f"\nSKIPPING (not found): {ckpt_path}")
            results[ckpt_path] = {"error": "checkpoint not found"}
            continue

        short_name = ckpt_path.split("/models/")[-1].replace("/final", "")
        print(f"\n{'='*60}")
        print(f"Evaluating: {short_name} ({ckpt_path})")
        print(f"{'='*60}")

        tokenizer = AutoTokenizer.from_pretrained(ckpt_path, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        dtype = torch.float16 if args.fp16 else torch.float32
        model = AutoModelForCausalLM.from_pretrained(
            ckpt_path, torch_dtype=dtype, trust_remote_code=True
        ).cuda().eval()

        ckpt_results = {}
        for ds_name, texts in ood_data.items():
            print(f"\n  --- {ds_name} ---")
            t0 = time.time()
            r = eval_perplexity(model, tokenizer, texts, max_length=args.max_length)
            elapsed = time.time() - t0
            r["elapsed_seconds"] = round(elapsed, 1)
            ckpt_results[ds_name] = r
            print(f"  {ds_name}: PPL={r['perplexity']:.2f} Loss={r['loss']:.4f} "
                  f"Tokens={r['num_tokens']} Time={elapsed:.0f}s")

        results[short_name] = ckpt_results
        del model
        torch.cuda.empty_cache()

    out_path = args.output_path
    if out_path is None:
        gpu_id = os.environ.get("CUDA_VISIBLE_DEVICES", "x")
        out_path = f"ood_eval_results_gpu{gpu_id}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    print("\n" + "="*80)
    print(f"{'Checkpoint':<35} {'OWT PPL':>10} {'Wiki PPL':>10}")
    print("-"*80)
    for name, ds_results in results.items():
        if "error" in ds_results:
            print(f"{name:<35} {'MISSING':>10} {'MISSING':>10}")
            continue
        owt = ds_results.get("openwebtext", {}).get("perplexity", "N/A")
        wiki = ds_results.get("wikipedia", {}).get("perplexity", "N/A")
        print(f"{name:<35} {owt:>10} {wiki:>10}")
    print("="*80)


if __name__ == "__main__":
    main()
