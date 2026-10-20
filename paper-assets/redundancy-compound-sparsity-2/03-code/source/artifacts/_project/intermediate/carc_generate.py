"""
CARC KV Eviction generation pipeline.

Custom autoregressive generation loop with per-step KV eviction.
Replaces model.generate() to enable fine-grained cache control.

Input: model, tokenizer, prompt, budget_ratio, grace_window
Output: generated text + eviction stats
Dependencies: torch, transformers, carc_utils, carc_kv_eviction
"""

import argparse
import json
import time
from typing import Any, Dict, List, Optional

import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

from carc_utils import EMAAnchorManager
from carc_kv_eviction import CARCKVEviction


class KVCapture:
    """Captures raw K/V projection outputs (pre-RoPE) for EMA scoring."""

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


def _get_cache_length(past_key_values: Any) -> int:
    if hasattr(past_key_values, 'get_seq_length'):
        return past_key_values.get_seq_length()
    if hasattr(past_key_values, 'key_cache') and len(past_key_values.key_cache) > 0:
        return past_key_values.key_cache[0].shape[2]
    if isinstance(past_key_values, tuple) and len(past_key_values) > 0:
        return past_key_values[0][0].shape[-2]
    return 0


def _sample(logits: torch.Tensor, temperature: float, top_p: float,
            top_k: int) -> torch.Tensor:
    if temperature <= 0:
        return logits.argmax(dim=-1, keepdim=True)

    logits = logits / temperature

    if top_k > 0:
        k = min(top_k, logits.size(-1))
        topk_vals, _ = torch.topk(logits, k)
        logits[logits < topk_vals[:, -1:]] = float('-inf')

    if top_p < 1.0:
        sorted_logits, sorted_idx = torch.sort(logits, descending=True)
        cumprobs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
        sorted_mask = (cumprobs - F.softmax(sorted_logits, dim=-1)) >= top_p
        sorted_logits[sorted_mask] = float('-inf')
        logits = logits.scatter(1, sorted_idx, sorted_logits)

    probs = F.softmax(logits, dim=-1)
    return torch.multinomial(probs, 1)


class CARCGenerator:
    def __init__(self, model, tokenizer, budget_ratio=0.5, grace_window=175,
                 ema_gamma=0.9, enable_windowed_reset=True,
                 window_size=16, tau_reset=0.3, n_reset=5):
        self.model = model
        self.tokenizer = tokenizer
        self.num_layers = len(model.model.layers)

        num_kv_heads = getattr(model.config, "num_key_value_heads", None)
        max_pos = getattr(model.config, "max_position_embeddings", 4096)
        budget = int(max_pos * budget_ratio)

        self.ema_manager = EMAAnchorManager(
            gamma=ema_gamma,
            num_kv_heads=num_kv_heads,
            per_head=num_kv_heads is not None,
            enable_reset=enable_windowed_reset,
            window_size=window_size,
            tau_reset=tau_reset,
            n_reset=n_reset,
        )
        self.eviction_manager = CARCKVEviction(
            budget=budget,
            grace_window=grace_window,
        )
        self.kv_capture = KVCapture(model, self.num_layers)
        self._budget = budget

    def _compute_step_ema(self) -> Optional[torch.Tensor]:
        """Average EMA scores across all layers for the current step's captured K/V."""
        layer_scores = []
        for layer_idx in range(self.num_layers):
            if layer_idx not in self.kv_capture.kv:
                continue
            pair = self.kv_capture.kv[layer_idx]
            if pair[0] is None or pair[1] is None:
                continue
            scores = self.ema_manager.compute_scores(layer_idx, pair[0], pair[1])
            layer_scores.append(scores.cpu())
        if not layer_scores:
            return None
        return torch.stack(layer_scores).mean(dim=0)

    def generate(self, prompt: str, max_new_tokens: int = 2048,
                 temperature: float = 0.6, top_p: float = 0.95,
                 top_k: int = 50) -> dict:
        self.ema_manager.reset()
        self.eviction_manager.reset()

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.model.device)
        generated_ids: List[int] = []
        cache_size_history: List[int] = []
        ema_scores_history: List[float] = []
        eos_id = self.tokenizer.eos_token_id

        # --- Prefill ---
        self.kv_capture.active = True
        self.kv_capture.clear()
        with torch.no_grad():
            outputs = self.model(input_ids, use_cache=True)
        past_key_values = outputs.past_key_values
        position_counter = input_ids.shape[1]

        avg_scores = self._compute_step_ema()
        self.kv_capture.clear()
        if avg_scores is not None:
            self.eviction_manager.update_scores(avg_scores)

        cache_size_history.append(_get_cache_length(past_key_values))

        # First token
        logits = outputs.logits[:, -1, :]
        next_token = _sample(logits, temperature, top_p, top_k)
        generated_ids.append(next_token.item())

        if next_token.item() == eos_id:
            return self._build_result(generated_ids, cache_size_history, ema_scores_history)

        # --- Autoregressive loop ---
        for step in range(1, max_new_tokens):
            self.kv_capture.clear()
            pos_ids = torch.tensor([[position_counter]], device=input_ids.device)
            with torch.no_grad():
                outputs = self.model(
                    input_ids=next_token.view(1, 1),
                    past_key_values=past_key_values,
                    position_ids=pos_ids,
                    use_cache=True,
                )
            past_key_values = outputs.past_key_values
            position_counter += 1

            avg_score = self._compute_step_ema()
            self.kv_capture.clear()
            if avg_score is not None:
                self.eviction_manager.update_scores(avg_score)
                ema_scores_history.append(avg_score.mean().item())

            cache_length = _get_cache_length(past_key_values)

            if self.eviction_manager.should_evict(cache_length):
                mask = self.eviction_manager.compute_eviction_mask(cache_length)
                past_key_values = self.eviction_manager.apply_eviction(past_key_values, mask)
                cache_length = _get_cache_length(past_key_values)

            cache_size_history.append(cache_length)

            logits = outputs.logits[:, -1, :]
            next_token = _sample(logits, temperature, top_p, top_k)
            generated_ids.append(next_token.item())

            if next_token.item() == eos_id:
                break

        self.kv_capture.active = False
        return self._build_result(generated_ids, cache_size_history, ema_scores_history)

    def _build_result(self, generated_ids, cache_size_history, ema_scores_history):
        self.kv_capture.active = False
        text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        return {
            "text": text,
            "num_tokens": len(generated_ids),
            "eviction_stats": self.eviction_manager.eviction_stats(),
            "cache_size_history": cache_size_history,
            "ema_scores": ema_scores_history,
        }

    def cleanup(self):
        self.kv_capture.remove()


def main():
    parser = argparse.ArgumentParser(description="CARC KV Eviction Generation")
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt", default="What is 1+1?")
    parser.add_argument("--budget-ratio", type=float, default=0.5)
    parser.add_argument("--grace-window", type=int, default=175)
    parser.add_argument("--max-new-tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.6)
    parser.add_argument("--top-p", type=float, default=0.95)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--ema-gamma", type=float, default=0.9)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--dtype", default="bf16", choices=["fp16", "bf16"])
    args = parser.parse_args()

    dtype = torch.float16 if args.dtype == "fp16" else torch.bfloat16
    print(f"Loading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True,
    )
    model.eval()

    max_pos = getattr(model.config, "max_position_embeddings", 4096)
    budget = int(max_pos * args.budget_ratio)
    num_kv_heads = getattr(model.config, "num_key_value_heads", None)
    print(f"Config: budget={budget} (ratio={args.budget_ratio}, max_pos={max_pos}), "
          f"grace={args.grace_window}, kv_heads={num_kv_heads}")

    gen = CARCGenerator(
        model, tokenizer,
        budget_ratio=args.budget_ratio,
        grace_window=args.grace_window,
        ema_gamma=args.ema_gamma,
    )

    t0 = time.time()
    result = gen.generate(
        prompt=args.prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        top_k=args.top_k,
    )
    elapsed = time.time() - t0
    gen.cleanup()

    tps = result['num_tokens'] / max(elapsed, 0.001)
    print(f"\nGenerated {result['num_tokens']} tokens in {elapsed:.1f}s ({tps:.1f} tok/s)")
    stats = result['eviction_stats']
    print(f"Evictions: {stats['eviction_triggers']} triggers, "
          f"{stats['total_evicted']} tokens evicted, "
          f"cache util={stats['cache_utilization']:.2f}")
    if result['cache_size_history']:
        h = result['cache_size_history']
        print(f"Cache size: min={min(h)}, max={max(h)}, final={h[-1]}")
    print(f"\n{'='*60}")
    print(result['text'])
    print(f"{'='*60}")

    if args.output:
        out = {
            "prompt": args.prompt,
            "text": result["text"],
            "num_tokens": result["num_tokens"],
            "elapsed_seconds": round(elapsed, 2),
            "tokens_per_second": round(tps, 1),
            "eviction_stats": result["eviction_stats"],
            "config": {
                "model": args.model,
                "budget_ratio": args.budget_ratio,
                "grace_window": args.grace_window,
                "max_new_tokens": args.max_new_tokens,
                "temperature": args.temperature,
                "top_p": args.top_p,
                "top_k": args.top_k,
            },
        }
        with open(args.output, 'w') as f:
            json.dump(out, f, indent=2)
        print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
