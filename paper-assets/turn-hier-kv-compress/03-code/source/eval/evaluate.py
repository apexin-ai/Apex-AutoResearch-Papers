"""TurnKV evaluation harness — KIRR and continuation perplexity across methods and compression ratios."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from contextlib import nullcontext
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    import torch

# ---------------------------------------------------------------------------
# Path setup — support both `python eval/evaluate.py` and `python -m eval.evaluate`
# ---------------------------------------------------------------------------
_here = os.path.dirname(os.path.abspath(__file__))
_root = os.path.dirname(_here)
if _root not in sys.path:
    sys.path.insert(0, _root)
if os.path.join(_root, "src") not in sys.path:
    sys.path.insert(0, os.path.join(_root, "src"))

from eval.config import EvalConfig
from eval.metrics import check_info_retained, compute_perplexity, compute_summary


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

CSV_FIELDS = [
    "trace_id",
    "case_type",
    "method",
    "compression_ratio",
    "kirr",
    "ppl_full",
    "ppl_compressed",
    "ppl_ratio",
    "num_planted",
    "num_retained",
]


def parse_args() -> argparse.Namespace:
    cfg = EvalConfig()
    p = argparse.ArgumentParser(
        description="Evaluate TurnKV vs uniform EA and full baseline"
    )
    p.add_argument("--traces", default=cfg.traces_path)
    p.add_argument("--model", default=cfg.model_name)
    p.add_argument(
        "--compression_ratios", nargs="+", type=float, default=cfg.compression_ratios
    )
    p.add_argument("--beta", type=float, default=cfg.beta)
    p.add_argument("--output_csv", default=cfg.output_csv)
    p.add_argument("--output_summary", default=cfg.output_summary)
    p.add_argument("--max_traces", type=int, default=None)
    p.add_argument("--device", default=cfg.device)
    p.add_argument("--max_new_tokens", type=int, default=cfg.max_new_tokens)
    return p.parse_args()


def load_traces(path: str, max_traces: Optional[int] = None) -> List[dict]:
    with open(path) as f:
        traces = json.load(f)
    if max_traces is not None:
        traces = traces[:max_traces]
    return traces


def make_press(method: str, compression_ratio: float, beta: float):
    """Create a kvpress press object for the given method."""
    from kvpress import ExpectedAttentionPress

    if method == "uniform_ea":
        return ExpectedAttentionPress(compression_ratio=compression_ratio)

    if method == "turnkv":
        from turnkv.press import TurnKVPress

        return TurnKVPress(compression_ratio=compression_ratio, beta=beta)

    raise ValueError(f"Unknown method: {method}")


def apply_press(press, model):
    """Context manager that optionally applies a press to a model."""
    if press is None:
        return nullcontext(model)
    return press(model)


# ---------------------------------------------------------------------------
# Per-trace evaluation
# ---------------------------------------------------------------------------


def evaluate_trace(
    trace: dict,
    model,
    tokenizer,
    role_extractor,
    compression_ratios: List[float],
    beta: float,
    max_new_tokens: int,
    ppl_target_tokens: int,
    device: str,
) -> List[dict]:
    """Run all methods on a single trace, return one result row per method x CR."""
    import torch

    messages = trace["messages"]
    case_type = trace.get("metadata", {}).get("case_type", "standard")
    planted = trace["planted_info"]
    num_planted = len(planted)
    trace_id = trace["trace_id"]

    # Tokenize for perplexity (no generation prompt)
    input_ids = tokenizer.apply_chat_template(
        messages, return_tensors="pt", add_generation_prompt=False
    ).to(device)
    seq_len = input_ids.shape[1]
    target_start = max(1, seq_len - ppl_target_tokens)

    # Segments for TurnKV
    segments = role_extractor.extract(input_ids[0])

    results: List[dict] = []

    # ---- Full baseline (no compression) ----
    ppl_full = compute_perplexity(model, tokenizer, input_ids, target_start)

    full_retained = 0
    for info in planted:
        q_msgs = messages + [{"role": "user", "content": info["retrieval_question"]}]
        q_ids = tokenizer.apply_chat_template(
            q_msgs, return_tensors="pt", add_generation_prompt=True
        ).to(device)
        with torch.no_grad():
            gen = model.generate(q_ids, max_new_tokens=max_new_tokens, do_sample=False)
        text = tokenizer.decode(gen[0][q_ids.shape[1] :], skip_special_tokens=True)
        if check_info_retained(text, info["expected_answer"]):
            full_retained += 1

    full_kirr = full_retained / num_planted if num_planted else 1.0
    results.append(
        {
            "trace_id": trace_id,
            "case_type": case_type,
            "method": "full",
            "compression_ratio": 0.0,
            "kirr": round(full_kirr, 4),
            "ppl_full": round(ppl_full, 4),
            "ppl_compressed": round(ppl_full, 4),
            "ppl_ratio": 1.0,
            "num_planted": num_planted,
            "num_retained": full_retained,
        }
    )

    # ---- Compressed methods ----
    for method in ["uniform_ea", "turnkv"]:
        for cr in compression_ratios:
            press = make_press(method, cr, beta)

            # PPL with compression
            if method == "turnkv":
                press.set_segments(segments)
            with apply_press(press, model):
                ppl_comp = compute_perplexity(model, tokenizer, input_ids, target_start)

            # KIRR with compression
            retained = 0
            for info in planted:
                q_msgs = messages + [
                    {"role": "user", "content": info["retrieval_question"]}
                ]
                q_ids = tokenizer.apply_chat_template(
                    q_msgs, return_tensors="pt", add_generation_prompt=True
                ).to(device)

                if method == "turnkv":
                    q_segments = role_extractor.extract(q_ids[0])
                    press.set_segments(q_segments)

                with apply_press(press, model):
                    with torch.no_grad():
                        gen = model.generate(
                            q_ids, max_new_tokens=max_new_tokens, do_sample=False
                        )

                text = tokenizer.decode(
                    gen[0][q_ids.shape[1] :], skip_special_tokens=True
                )
                if check_info_retained(text, info["expected_answer"]):
                    retained += 1

            kirr = retained / num_planted if num_planted else 1.0
            ppl_ratio = ppl_comp / ppl_full if ppl_full > 0 else float("inf")

            results.append(
                {
                    "trace_id": trace_id,
                    "case_type": case_type,
                    "method": method,
                    "compression_ratio": cr,
                    "kirr": round(kirr, 4),
                    "ppl_full": round(ppl_full, 4),
                    "ppl_compressed": round(ppl_comp, 4),
                    "ppl_ratio": round(ppl_ratio, 4),
                    "num_planted": num_planted,
                    "num_retained": retained,
                }
            )

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    args = parse_args()

    import torch
    from tqdm import tqdm
    from transformers import AutoModelForCausalLM, AutoTokenizer

    from turnkv.role_extractor import RoleExtractor

    print(f"Loading model {args.model} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16, device_map=args.device
    )
    model.eval()

    role_extractor = RoleExtractor(tokenizer, template_name="llama3")

    traces = load_traces(args.traces, args.max_traces)
    print(f"Loaded {len(traces)} traces")

    all_results: List[dict] = []

    for trace in tqdm(traces, desc="Evaluating"):
        try:
            rows = evaluate_trace(
                trace,
                model,
                tokenizer,
                role_extractor,
                args.compression_ratios,
                args.beta,
                args.max_new_tokens,
                EvalConfig.ppl_target_tokens,
                args.device,
            )
            all_results.extend(rows)
        except Exception as e:
            print(f"ERROR on {trace['trace_id']}: {e}", file=sys.stderr)

    # ---- Save CSV ----
    os.makedirs(os.path.dirname(args.output_csv) or ".", exist_ok=True)
    with open(args.output_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        w.writerows(all_results)
    print(f"Results saved to {args.output_csv}")

    # ---- Save summary ----
    summary = compute_summary(all_results, args.compression_ratios)
    os.makedirs(os.path.dirname(args.output_summary) or ".", exist_ok=True)
    with open(args.output_summary, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {args.output_summary}")

    verdict = summary["mvp_verdict"]["overall"]
    print(f"\n{'=' * 40}")
    print(f"MVP Verdict: {verdict}")
    print(f"{'=' * 40}")


if __name__ == "__main__":
    main()
