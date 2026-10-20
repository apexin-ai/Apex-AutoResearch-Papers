"""
D003 Experiment 2: EMA vs Recency eviction on WikiText-2 32K prefill.

Load WikiText-2 text concatenated to 32768 tokens, 80/20 split,
evaluate continuation PPL under 6 eviction strategies:
full, ema_0.9, ema_0.7, ema_0.5, random, recency.

Input: WikiText-2 (wikitext-2-raw-v1)
Output: JSON with per-strategy PPL, eviction stats
Dependencies: torch, transformers, datasets, tqdm, carc_utils, carc_kv_eviction
"""

import argparse
import gc
import json
import sys
import time
from typing import Any, Dict, List, Optional

import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

from carc_utils import EMAAnchorManager
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


def load_wikitext_tokens(tokenizer, seq_len: int = 32768) -> torch.Tensor:
    """Load WikiText-2 validation and concatenate to seq_len tokens."""
    from datasets import load_dataset

    ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="test", trust_remote_code=True)

    texts = []
    for item in ds:
        text = item.get("text", "")
        if text and len(text.strip()) >= 20:
            texts.append(text)

    full_text = "\n".join(texts)
    all_ids = tokenizer(full_text, return_tensors="pt", add_special_tokens=False).input_ids[0]

    if len(all_ids) < seq_len:
        print(f"WARNING: WikiText-2 only has {len(all_ids)} tokens, requested {seq_len}")
        seq_len = len(all_ids)

    return all_ids[:seq_len].unsqueeze(0)  # (1, seq_len)


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
            pass
        elif strategy == "recency":
            pass

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
    parser = argparse.ArgumentParser(description="D003 Exp2: WikiText-2 32K EMA vs Recency")
    parser.add_argument("--model", default="/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-14B")
    parser.add_argument("--output", default="/root/carc/d003_wikitext32k_results.json")
    parser.add_argument("--budget-ratio", type=float, default=0.5)
    parser.add_argument("--grace-window", type=int, default=175)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seq-len", type=int, default=32768)
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

    # --- Load WikiText-2 ---
    print(f"\nLoading WikiText-2 ({args.seq_len} tokens)...")
    input_ids = load_wikitext_tokens(tokenizer, seq_len=args.seq_len).to(device)
    total_len = input_ids.shape[1]
    print(f"Loaded {total_len} tokens")

    # 80/20 split
    prefill_len = int(total_len * 0.8)
    eval_len = total_len - prefill_len
    budget = int(prefill_len * args.budget_ratio)
    print(f"Split: prefill={prefill_len}, eval={eval_len}, budget={budget}")

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
    recency_ppl = next(r["ppl"] for r in results if r["strategy"] == "recency")
    ema_ppls = {r["strategy"]: r["ppl"] for r in results if r["strategy"].startswith("ema")}
    best_ema = min(ema_ppls.values())

    ema_vs_random_gap = (random_ppl - best_ema) / random_ppl * 100 if random_ppl > 0 else 0
    ema_beats_recency = best_ema < recency_ppl

    print(f"\nFull baseline PPL: {full_ppl:.4f}")
    print(f"Best EMA PPL: {best_ema:.4f}")
    print(f"Random PPL: {random_ppl:.4f}")
    print(f"Recency PPL: {recency_ppl:.4f}")
    print(f"EMA vs Random gap: {ema_vs_random_gap:.2f}%")
    print(f"EMA < Recency? {'YES' if ema_beats_recency else 'NO'}")
    print(f"PASS (EMA < Recency)? {'YES' if ema_beats_recency else 'NO'}")

    # --- Save ---
    output = {
        "experiment": "d003_wikitext_32k",
        "config": {
            "model": args.model,
            "budget_ratio": args.budget_ratio,
            "budget": budget,
            "grace_window": args.grace_window,
            "seq_len": args.seq_len,
            "total_tokens": total_len,
            "prefill_len": prefill_len,
            "eval_len": eval_len,
        },
        "results": results,
        "summary": {
            "full_ppl": full_ppl,
            "best_ema_ppl": best_ema,
            "random_ppl": random_ppl,
            "recency_ppl": recency_ppl,
            "ema_vs_random_gap_pct": round(ema_vs_random_gap, 2),
            "ema_beats_recency": ema_beats_recency,
            "pass": ema_beats_recency,
        },
    }
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
