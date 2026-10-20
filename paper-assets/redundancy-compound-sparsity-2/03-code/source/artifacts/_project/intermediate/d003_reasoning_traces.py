"""
D003 Experiment 1: EMA vs Random eviction on reasoning traces.

Generate MATH-500 reasoning traces with DeepSeek-R1-Distill-Qwen-14B,
concatenate into ~30-40K token sequence, then evaluate continuation PPL
under 6 eviction strategies: full, ema_0.9, ema_0.7, ema_0.5, random, recency.

Input: MATH-500 problems (hendrycks/competition_math)
Output: JSON with per-strategy PPL, eviction stats
Dependencies: torch, transformers, datasets, tqdm, carc_utils, carc_kv_eviction
"""

import argparse
import gc
import json
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

from carc_utils import EMAAnchorManager, load_math_data
from carc_kv_eviction import CARCKVEviction


class KVCapture:
    def __init__(self, model, num_layers: int):
        self._hooks: list = []
        self.kv: Dict[int, List[Optional[torch.Tensor]]] = {}
        self.active = True
        for i in range(num_layers):
            attn = model.model.layers[i].self_attn
            self._hooks.append(attn.k_proj.register_forward_hook(self._hook(i, 0)))
            self._hooks.append(attn.v_proj.register_forward_hook(self._hook(i, 1)))

    def _hook(self, layer_idx: int, slot: int):
        def fn(_module, _inp, out):
            if not self.active:
                return
            self.kv.setdefault(layer_idx, [None, None])[slot] = out.detach()
        return fn

    def clear(self):
        self.kv.clear()

    def remove(self):
        for h in self._hooks:
            h.remove()
        self._hooks.clear()


def get_cache_length(past_kv: Any) -> int:
    if hasattr(past_kv, "get_seq_length"):
        return past_kv.get_seq_length()
    if hasattr(past_kv, "key_cache") and len(past_kv.key_cache) > 0:
        return past_kv.key_cache[0].shape[2]
    if isinstance(past_kv, tuple) and len(past_kv) > 0:
        return past_kv[0][0].shape[-2]
    return 0


def generate_reasoning_traces(
    model, tokenizer, prompts: List[str], max_new_tokens: int = 2048,
    device: torch.device = torch.device("cuda:0"),
) -> List[int]:
    """Greedy-generate reasoning traces and return concatenated token ids."""
    all_ids: List[int] = []
    eos_id = tokenizer.eos_token_id

    for i, prompt in enumerate(tqdm(prompts, desc="Generating traces")):
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
        generated = []

        with torch.no_grad():
            outputs = model(input_ids, use_cache=True)
            past_kv = outputs.past_key_values
            next_token = outputs.logits[:, -1, :].argmax(dim=-1, keepdim=True)
            generated.append(next_token.item())

            for _ in range(max_new_tokens - 1):
                if next_token.item() == eos_id:
                    break
                outputs = model(
                    input_ids=next_token.view(1, 1),
                    past_key_values=past_kv,
                    use_cache=True,
                )
                past_kv = outputs.past_key_values
                next_token = outputs.logits[:, -1, :].argmax(dim=-1, keepdim=True)
                generated.append(next_token.item())

        trace_ids = input_ids[0].tolist() + generated
        all_ids.extend(trace_ids)
        print(f"  Trace {i+1}: {len(trace_ids)} tokens (total: {len(all_ids)})")

        del past_kv, outputs
        torch.cuda.empty_cache()

        if len(all_ids) >= 40000:
            break

    return all_ids


def run_strategy(
    strategy: str,
    model,
    num_layers: int,
    input_ids: torch.Tensor,
    prefill_len: int,
    budget: int,
    grace_window: int,
    device: torch.device,
    chunk_size: int = 512,
) -> Dict:
    """Run one eviction strategy and return PPL + stats."""

    use_eviction = strategy != "full"
    gamma_map = {"ema_0.9": 0.9, "ema_0.7": 0.7, "ema_0.5": 0.5}

    num_kv_heads = getattr(model.config, "num_key_value_heads", None)

    kv_capture = None
    ema_manager = None
    eviction_mgr = None

    if use_eviction:
        eviction_mgr = CARCKVEviction(budget=budget, grace_window=grace_window)
        if strategy in gamma_map:
            gamma = gamma_map[strategy]
            ema_manager = EMAAnchorManager(
                gamma=gamma, num_kv_heads=num_kv_heads,
                per_head=num_kv_heads is not None,
            )
            kv_capture = KVCapture(model, num_layers)
        elif strategy == "random":
            pass  # random scores, no EMA needed
        elif strategy == "recency":
            pass  # recency scores, no EMA needed

    position_counter = 0
    past_kv = None

    # --- Chunked prefill ---
    num_chunks = (prefill_len + chunk_size - 1) // chunk_size
    for ci in tqdm(range(num_chunks), desc=f"  [{strategy}] prefill", leave=False):
        start = ci * chunk_size
        end = min(start + chunk_size, prefill_len)
        chunk_ids = input_ids[:, start:end]
        chunk_len = chunk_ids.shape[1]

        position_ids = torch.arange(
            position_counter, position_counter + chunk_len, device=device
        ).unsqueeze(0)

        if kv_capture is not None:
            kv_capture.active = True
            kv_capture.clear()

        with torch.no_grad():
            outputs = model(
                input_ids=chunk_ids,
                position_ids=position_ids,
                past_key_values=past_kv,
                use_cache=True,
            )
        past_kv = outputs.past_key_values
        position_counter += chunk_len

        if use_eviction:
            # Pad scores to (current_tracked + chunk_len) so update_scores
            # appends new positions instead of overwriting old ones.
            cur_tracked = eviction_mgr._length
            if strategy in gamma_map and kv_capture is not None:
                layer_scores = []
                for li in range(num_layers):
                    if li in kv_capture.kv and kv_capture.kv[li][0] is not None:
                        scores = ema_manager.compute_scores(
                            li, kv_capture.kv[li][0], kv_capture.kv[li][1]
                        )
                        layer_scores.append(scores)
                if layer_scores:
                    avg_score = torch.stack(layer_scores).mean(dim=0)
                    chunk_scores = avg_score.mean(dim=0)
                    padded = torch.zeros(cur_tracked + chunk_len)
                    padded[cur_tracked:] = chunk_scores
                    eviction_mgr.update_scores(padded)
                kv_capture.clear()
            elif strategy == "random":
                padded = torch.zeros(cur_tracked + chunk_len)
                padded[cur_tracked:] = torch.rand(chunk_len)
                eviction_mgr.update_scores(padded)
            elif strategy == "recency":
                # Globally decreasing: older positions get higher scores → evicted first
                padded = torch.zeros(cur_tracked + chunk_len)
                padded[cur_tracked:] = torch.arange(
                    prefill_len - start, prefill_len - start - chunk_len, -1,
                    dtype=torch.float32,
                )
                eviction_mgr.update_scores(padded)

            cache_len = get_cache_length(past_kv)
            if eviction_mgr.should_evict(cache_len):
                mask = eviction_mgr.compute_eviction_mask(cache_len)
                past_kv = eviction_mgr.apply_eviction(past_kv, mask)

        del outputs
        torch.cuda.empty_cache()

    # --- Eval: continuation PPL ---
    eval_len = input_ids.shape[1] - prefill_len
    total_nll = 0.0
    n_tokens = 0

    for ti in tqdm(range(eval_len), desc=f"  [{strategy}] eval", leave=False):
        idx = prefill_len + ti
        token = input_ids[:, idx:idx+1]
        position_ids = torch.tensor([[position_counter]], device=device)

        if kv_capture is not None:
            kv_capture.active = True
            kv_capture.clear()

        with torch.no_grad():
            outputs = model(
                input_ids=token,
                position_ids=position_ids,
                past_key_values=past_kv,
                use_cache=True,
            )
        past_kv = outputs.past_key_values
        position_counter += 1

        if use_eviction:
            if strategy in gamma_map and kv_capture is not None:
                layer_scores = []
                for li in range(num_layers):
                    if li in kv_capture.kv and kv_capture.kv[li][0] is not None:
                        scores = ema_manager.compute_scores(
                            li, kv_capture.kv[li][0], kv_capture.kv[li][1]
                        )
                        layer_scores.append(scores)
                if layer_scores:
                    avg_score = torch.stack(layer_scores).mean(dim=0)
                    eviction_mgr.update_scores(avg_score.mean(dim=0))
                kv_capture.clear()
            elif strategy == "random":
                eviction_mgr.update_scores(torch.rand(1))
            elif strategy == "recency":
                eviction_mgr.update_scores(torch.tensor([1.0]))

            cache_len = get_cache_length(past_kv)
            if eviction_mgr.should_evict(cache_len):
                mask = eviction_mgr.compute_eviction_mask(cache_len)
                past_kv = eviction_mgr.apply_eviction(past_kv, mask)

        # Compute NLL for the *next* token
        if ti < eval_len - 1:
            next_token_id = input_ids[0, idx + 1].item()
            log_probs = F.log_softmax(outputs.logits[:, -1, :], dim=-1)
            nll = -log_probs[0, next_token_id].item()
            total_nll += nll
            n_tokens += 1

        del outputs
        if ti % 200 == 0:
            torch.cuda.empty_cache()

    if kv_capture is not None:
        kv_capture.remove()

    ppl = float("inf")
    if n_tokens > 0:
        ppl = float(torch.exp(torch.tensor(total_nll / n_tokens)).item())

    eviction_stats = eviction_mgr.eviction_stats() if eviction_mgr else {}

    del past_kv
    torch.cuda.empty_cache()
    gc.collect()

    return {
        "strategy": strategy,
        "ppl": round(ppl, 4),
        "eval_tokens": n_tokens,
        "prefill_tokens": prefill_len,
        **eviction_stats,
    }


def main():
    parser = argparse.ArgumentParser(description="D003 Exp1: Reasoning Traces EMA vs Random")
    parser.add_argument("--model", default="/root/carc/models/DeepSeek-R1-Distill-Qwen-14B")
    parser.add_argument("--output", default="/root/carc/d003_reasoning_results.json")
    parser.add_argument("--budget-ratio", type=float, default=0.5)
    parser.add_argument("--grace-window", type=int, default=175)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--num-traces", type=int, default=20)
    parser.add_argument("--max-trace-tokens", type=int, default=2048)
    parser.add_argument("--chunk-size", type=int, default=512)
    parser.add_argument("--dtype", default="bf16", choices=["fp16", "bf16"])
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}")
    dtype = torch.float16 if args.dtype == "fp16" else torch.bfloat16

    print(f"Loading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype, device_map={"": device}, trust_remote_code=True,
    )
    model.eval()
    num_layers = len(model.model.layers)
    print(f"Model loaded: {num_layers} layers, kv_heads={getattr(model.config, 'num_key_value_heads', None)}")

    # --- Generate reasoning traces ---
    print(f"\nGenerating {args.num_traces} reasoning traces...")
    prompts = load_math_data(num_problems=args.num_traces, seed=42)
    all_ids = generate_reasoning_traces(
        model, tokenizer, prompts,
        max_new_tokens=args.max_trace_tokens, device=device,
    )
    total_len = len(all_ids)
    print(f"Total trace tokens: {total_len}")

    if total_len < 1000:
        print("ERROR: Too few tokens generated. Aborting.")
        sys.exit(1)

    # 80/20 split
    prefill_len = int(total_len * 0.8)
    eval_len = total_len - prefill_len
    budget = int(prefill_len * args.budget_ratio)
    print(f"Split: prefill={prefill_len}, eval={eval_len}, budget={budget}")

    input_ids = torch.tensor([all_ids], dtype=torch.long, device=device)

    # --- Run strategies ---
    strategies = ["full", "ema_0.9", "ema_0.7", "ema_0.5", "random", "recency"]
    results = []

    for strat in strategies:
        print(f"\n{'='*60}")
        print(f"Running strategy: {strat}")
        print(f"{'='*60}")
        t0 = time.time()
        result = run_strategy(
            strategy=strat,
            model=model,
            num_layers=num_layers,
            input_ids=input_ids,
            prefill_len=prefill_len,
            budget=budget,
            grace_window=args.grace_window,
            device=device,
            chunk_size=args.chunk_size,
        )
        elapsed = time.time() - t0
        result["elapsed_seconds"] = round(elapsed, 1)
        results.append(result)
        print(f"  PPL={result['ppl']:.4f}  ({elapsed:.1f}s)")

    # --- Summary ---
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"{'Strategy':<12} {'PPL':>10} {'Evicted':>10} {'Triggers':>10}")
    print("-" * 44)
    for r in results:
        print(f"{r['strategy']:<12} {r['ppl']:>10.4f} {r.get('total_evicted', 0):>10} {r.get('eviction_triggers', 0):>10}")

    # PASS criteria check
    full_ppl = next(r["ppl"] for r in results if r["strategy"] == "full")
    random_ppl = next(r["ppl"] for r in results if r["strategy"] == "random")
    ema_ppls = {r["strategy"]: r["ppl"] for r in results if r["strategy"].startswith("ema")}
    best_ema = min(ema_ppls.values())
    gap = (random_ppl - best_ema) / random_ppl * 100 if random_ppl > 0 else 0

    print(f"\nFull baseline PPL: {full_ppl:.4f}")
    print(f"Best EMA PPL: {best_ema:.4f}")
    print(f"Random PPL: {random_ppl:.4f}")
    print(f"EMA vs Random gap: {gap:.2f}%")
    print(f"PASS (≥5% gap)? {'YES' if gap >= 5.0 else 'NO'}")

    # --- Save ---
    output = {
        "experiment": "d003_reasoning_traces",
        "config": {
            "model": args.model,
            "budget_ratio": args.budget_ratio,
            "budget": budget,
            "grace_window": args.grace_window,
            "num_traces": args.num_traces,
            "total_tokens": total_len,
            "prefill_len": prefill_len,
            "eval_len": eval_len,
        },
        "results": results,
        "summary": {
            "full_ppl": full_ppl,
            "best_ema_ppl": best_ema,
            "random_ppl": random_ppl,
            "ema_vs_random_gap_pct": round(gap, 2),
            "pass": gap >= 5.0,
        },
    }
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
