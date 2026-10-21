"""
generate_chain_decoding.py — Chain generation with greedy + top-k strategies.
Loads model once, runs both strategies sequentially.
Output: data/{model}-{strategy}/generations_shard0.jsonl
"""
import argparse, json, os, time, signal
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

signal.signal(signal.SIGHUP, signal.SIG_IGN)

MODEL_PATHS = {
    "pythia-2.8b": "/root/autodl-tmp/models/pythia-2.8b/models--EleutherAI--pythia-2.8b/snapshots/2a259cdd96a4beb1cdf467512e3904197345f6a9",
    "olmo-2-1b": "/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B",
    "qwen3-1.7b": "/root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base",
    "llama-3.2-3b": "/root/autodl-tmp/models/Llama-3.2-3B",
    "mistral-7b-v0.3": "/root/autodl-tmp/models/mistral-7b-v0.3",
    "pythia-1b": "/root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b",
    "qwen3-0.6b": "/root/autodl-tmp/models/qwen3-0.6b/Qwen/Qwen3-0___6B-Base",
    "qwen3-8b": "/root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base",
}

MAX_DEPTH = 4
NUM_DEPTHS = MAX_DEPTH + 1
STRATEGIES = {
    "greedy": {"do_sample": False},
    "topk": {"do_sample": True, "temperature": 0.7, "top_k": 50, "top_p": 1.0},
}


def load_seeds(path, tokenizer, max_tokens=256):
    seeds = []
    with open(path) as f:
        for line_num, line in enumerate(f):
            item = json.loads(line)
            text = item.get("text", "")
            if len(text.strip()) < 100:
                continue
            token_ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
            if len(token_ids) < 64:
                continue
            seeds.append({"seed_id": line_num, "text": tokenizer.decode(token_ids)})
    print(f"Loaded {len(seeds)} seeds")
    return seeds


def generate_continuation(model, tokenizer, text, device, strategy_kwargs,
                          max_new_tokens=256, prompt_tokens=128, repetition_penalty=1.0):
    input_ids = tokenizer.encode(text, add_special_tokens=False)
    if len(input_ids) == 0:
        return ""
    input_ids = input_ids[-prompt_tokens:]
    input_tensor = torch.tensor([input_ids], device=device)

    gen_kwargs = {
        "max_new_tokens": max_new_tokens,
        "pad_token_id": tokenizer.pad_token_id or tokenizer.eos_token_id,
        "repetition_penalty": repetition_penalty,
        **strategy_kwargs,
    }

    with torch.no_grad():
        output = model.generate(input_tensor, **gen_kwargs)

    new_tokens = output[0][len(input_ids):]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)


def load_done_seeds(path):
    done = set()
    if not os.path.exists(path):
        return done
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                done.add(json.loads(line)['seed_id'])
            except (json.JSONDecodeError, KeyError):
                pass
    return done


def run_generation(model, tokenizer, seeds, device, strategy_name, strategy_kwargs,
                   output_dir, model_name, repetition_penalty=1.0):
    dir_name = f"{model_name}-{strategy_name}"
    out_dir = os.path.join(output_dir, dir_name)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "generations_shard0.jsonl")

    done_seeds = load_done_seeds(out_path)
    if done_seeds:
        print(f"[{strategy_name}] Resuming: {len(done_seeds)} seeds done")

    t0 = time.time()
    count = 0
    skipped = 0

    with open(out_path, "a") as f:
        for i, seed_info in enumerate(tqdm(seeds, desc=f"{model_name}-{strategy_name}")):
            seed_id = seed_info["seed_id"]
            if seed_id in done_seeds:
                continue

            base_id = i * NUM_DEPTHS
            seed_text = seed_info["text"]

            gen0_tokens = tokenizer.encode(seed_text, add_special_tokens=False)
            f.write(json.dumps({
                "id": base_id, "depth": 0, "text": seed_text,
                "seed_id": seed_id, "token_count": len(gen0_tokens),
                "model": model_name, "strategy": strategy_name,
            }, ensure_ascii=False) + "\n")
            f.flush()
            count += 1

            prev_text = seed_text
            for depth in range(1, NUM_DEPTHS):
                check_ids = tokenizer.encode(prev_text, add_special_tokens=False)
                if len(check_ids) == 0 or len(prev_text.strip()) < 10:
                    skipped += 1
                    break

                continuation = generate_continuation(
                    model, tokenizer, prev_text, device, strategy_kwargs,
                    repetition_penalty=repetition_penalty
                )
                if not continuation or len(continuation.strip()) == 0:
                    skipped += 1
                    break

                cont_tokens = tokenizer.encode(continuation, add_special_tokens=False)
                f.write(json.dumps({
                    "id": base_id + depth, "depth": depth, "text": continuation,
                    "seed_id": seed_id, "token_count": len(cont_tokens),
                    "model": model_name, "strategy": strategy_name,
                }, ensure_ascii=False) + "\n")
                f.flush()
                count += 1
                prev_text = continuation

            if (i + 1) % 100 == 0:
                elapsed = time.time() - t0
                print(f"[{strategy_name}] {i+1}/{len(seeds)} done, {elapsed:.0f}s")

    elapsed = time.time() - t0
    print(f"[{strategy_name}] Done: {count} records in {elapsed:.1f}s (skipped {skipped})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", required=True, choices=list(MODEL_PATHS.keys()))
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--input", default="data/wiki_seed_1000.jsonl")
    parser.add_argument("--output-dir", default="data/")
    parser.add_argument("--repetition-penalty", type=float, default=1.0)
    parser.add_argument("--strategies", nargs="+", default=["greedy", "topk"],
                        choices=["greedy", "topk"])
    args = parser.parse_args()

    model_path = MODEL_PATHS[args.model_name]
    print(f"Loading {args.model_name} from {model_path} on {args.device}")

    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float16, trust_remote_code=True,
    ).to(args.device)
    model.eval()
    print(f"Model loaded, dtype={model.dtype}, vocab={model.config.vocab_size}")

    project_root = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(project_root, args.input) if not os.path.isabs(args.input) else args.input
    seeds = load_seeds(input_path, tokenizer)

    output_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir

    for strategy in args.strategies:
        torch.manual_seed(42)
        torch.cuda.manual_seed(42)
        run_generation(model, tokenizer, seeds, args.device, strategy, STRATEGIES[strategy],
                       output_dir, args.model_name, args.repetition_penalty)

    print("All strategies complete.")


if __name__ == "__main__":
    main()
