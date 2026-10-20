"""CED-as-reranker: inference-time reranking of N SFT candidates using CED scoring.

No fine-tuning. SFT model generates N candidates per document, CED selects the best one.
Compares: Greedy baseline, CED reranker, Oracle (F1-best), Random.

Usage:
  python -m freige.eval.ced_reranker \
      --base_model ./outputs \
      --sft_adapter ./outputs \
      --data_dir ./data/docred \
      --nli_model_path ./outputs \
      --output_dir ./outputs/eval_results
      --num_generations 8 --temperature 0.7 --max_docs 50
"""

import argparse
import json
import logging
import random
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from tqdm import tqdm

from freige.data.docred_processor import DOCRED_REL_INFO
from freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output
from freige.rewards.ced_reward import (
    CEDRewardModel,
    VERBALIZATION_TEMPLATES,
    verbalize_triple,
)
from freige.training.rsft_generate import (
    generate_batch,
    load_model_and_tokenizer,
    prepare_generation_data,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

_REL_NAME_TO_CODE = {v.lower().strip(): k for k, v in DOCRED_REL_INFO.items()}

def verbalize_by_name(head: str, relation: str, tail: str) -> str:
    """Verbalize a triple using relation name instead of Pxxx code."""
    pcode = _REL_NAME_TO_CODE.get(relation.lower().strip())
    if pcode:
        return verbalize_triple(head, pcode, tail)
    return f"{head} {relation} {tail}."

def score_candidate_ced(
    parsed_triples: list[dict],
    sents: list[str],
    ced_model: CEDRewardModel,
    tau: float = 0.5,
) -> float:
    """CED score for one candidate — uses only predicted evidence, no gold info.

    For each predicted triple:
      claim   = verbalized triple
      pos     = concat of model-cited evidence sentences
      neg     = all other sentences in the document
      CED(t)  = max(0, p_pos - max_j p_neg_j) * I(p_pos > tau)
    Returns mean CED across triples.
    """
    if not parsed_triples:
        return 0.0

    n_sents = len(sents)
    all_ids = set(range(n_sents))
    scores = []

    for t in parsed_triples:
        if not isinstance(t, dict):
            continue
        head = t.get("head", "")
        relation = t.get("relation", "")
        tail = t.get("tail", "")
        evidence = t.get("evidence", [])
        if not (head and relation and tail):
            continue

        claim = verbalize_by_name(head, relation, tail)

        evi_ids = {int(e) for e in evidence if isinstance(e, int) and 0 <= int(e) < n_sents}
        if not evi_ids:
            scores.append(0.0)
            continue

        cited = [sents[i] for i in sorted(evi_ids)]
        neg_ids = all_ids - evi_ids
        negs = [sents[i] for i in sorted(neg_ids)]

        if negs:
            r = ced_model.compute_ced_reward(claim, cited, negs, tau=tau)
        else:
            r = ced_model.compute_flat_nli_reward(claim, cited, tau=tau)
        scores.append(r["reward"])

    return float(np.mean(scores)) if scores else 0.0

def candidate_rel_f1(parsed_triples: list[dict], gold_triples: list[dict]) -> float:
    """Per-candidate relation F1 against gold (for Oracle selection)."""
    gold_set = {
        (str(g["head"]).lower().strip(),
         str(g["relation"]).lower().strip(),
         str(g["tail"]).lower().strip())
        for g in gold_triples
    }
    pred_set = set()
    for p in parsed_triples:
        if isinstance(p, dict):
            pred_set.add((
                str(p.get("head", "")).lower().strip(),
                str(p.get("relation", "")).lower().strip(),
                str(p.get("tail", "")).lower().strip(),
            ))
    if not gold_set:
        return 1.0 if not pred_set else 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0.0
    rec = tp / len(gold_set) if gold_set else 0.0
    return 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0

def evaluate_strategy(
    selections: dict,
    gold: list[dict],
    train_file: str,
) -> dict:
    """Run DocREDEvaluator on the selected candidates."""
    all_preds = []
    for doc_id, cand in selections.items():
        for t in cand["parsed_triples"]:
            all_preds.append({
                "doc_id": doc_id,
                "head": t["head"],
                "tail": t["tail"],
                "relation": t["relation"],
                "evidence": t.get("evidence", []),
            })

    evaluator = DocREDEvaluator.from_train_file(train_file)
    metrics = evaluator.evaluate(all_preds, gold)

    n = len(selections)
    n_ok = sum(1 for c in selections.values() if c.get("format_ok", False))
    metrics["n_docs"] = n
    metrics["n_predictions"] = len(all_preds)
    metrics["format_ok_rate"] = n_ok / n if n else 0.0
    return metrics

# ---------------------------------------------------------------------------
# Generation helpers
# ---------------------------------------------------------------------------

def load_generation_checkpoint(gen_file: Path) -> dict:
    """Load previously generated candidates from JSONL (for resume)."""
    docs = defaultdict(list)
    if not gen_file.exists():
        return {}
    with open(gen_file) as f:
        for line in f:
            rec = json.loads(line)
            docs[rec["doc_id"]].append(rec)
    logger.info("Resumed %d docs from %s", len(docs), gen_file)
    return dict(docs)

@torch.no_grad()
def generate_greedy_single(model, tokenizer, prompt, max_new_tokens):
    """Generate one output with greedy decoding."""
    inputs = tokenizer(
        prompt, return_tensors="pt", truncation=True, max_length=4096,
    ).to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,

        pad_token_id=tokenizer.pad_token_id,
    )
    input_len = inputs["input_ids"].shape[1]
    gen_ids = outputs[0, input_len:]
    text = tokenizer.decode(gen_ids, skip_special_tokens=True)
    truncated = len(gen_ids) >= max_new_tokens
    return text, truncated

def run_generation(model, tokenizer, items, args, output_dir):
    """Generate greedy baseline + N sampled candidates per doc. Supports resume."""
    gen_file = output_dir / "generations.jsonl"
    greedy_file = output_dir / "greedy_outputs.jsonl"

    # --- Sampled candidates (resume-aware) ---
    existing = load_generation_checkpoint(gen_file)
    remaining = [it for it in items if it["doc_id"] not in existing]
    logger.info("Sampled generation: %d total, %d done, %d remaining",
                len(items), len(existing), len(remaining))

    if remaining:
        with open(gen_file, "a") as fout:
            for idx in tqdm(range(len(remaining)), desc="Generating (sampled)"):
                item = remaining[idx]
                outputs, trunc_flags = generate_batch(
                    model, tokenizer, [item["prompt"]],
                    args.num_generations, args.temperature, args.max_new_tokens,
                )
                gens = outputs[0]
                truncs = trunc_flags[0]

                candidates = []
                for gi, raw_text in enumerate(gens):
                    parsed, fmt_ok = parse_model_output(raw_text)
                    trunc = truncs[gi] if gi < len(truncs) else False
                    rec = {
                        "doc_id": item["doc_id"],
                        "generation_idx": gi,
                        "raw_text": raw_text,
                        "parsed_triples": parsed,
                        "format_ok": fmt_ok,
                        "truncated": trunc,
                    }
                    candidates.append(rec)
                    fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                existing[item["doc_id"]] = candidates
                fout.flush()

    # --- Greedy baseline (resume-aware) ---
    greedy_existing = {}
    if greedy_file.exists():
        with open(greedy_file) as f:
            for line in f:
                rec = json.loads(line)
                greedy_existing[rec["doc_id"]] = rec
        logger.info("Greedy resume: %d docs already done", len(greedy_existing))

    greedy_remaining = [it for it in items if it["doc_id"] not in greedy_existing]
    if greedy_remaining:
        # Override generation_config for greedy
        orig_temp = model.generation_config.temperature
        orig_do_sample = model.generation_config.do_sample
        model.generation_config.temperature = 1.0
        model.generation_config.do_sample = False

        with open(greedy_file, "a") as fout:
            for item in tqdm(greedy_remaining, desc="Generating (greedy)"):
                raw_text, truncated = generate_greedy_single(
                    model, tokenizer, item["prompt"], args.max_new_tokens,
                )
                parsed, fmt_ok = parse_model_output(raw_text)
                rec = {
                    "doc_id": item["doc_id"],
                    "raw_text": raw_text,
                    "parsed_triples": parsed,
                    "format_ok": fmt_ok,
                    "truncated": truncated,
                }
                greedy_existing[rec["doc_id"]] = rec
                fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()

        # Restore for any further sampling
        model.generation_config.temperature = orig_temp
        model.generation_config.do_sample = orig_do_sample

    # Assemble per-doc dict
    item_map = {it["doc_id"]: it for it in items}
    all_docs = {}
    for doc_id, cands in existing.items():
        if doc_id not in item_map:
            continue
        all_docs[doc_id] = {
            "candidates": cands,
            "greedy": greedy_existing.get(doc_id),
            "gold_triples": item_map[doc_id]["gold_triples"],
            "sents": item_map[doc_id]["sents"],
        }
    return all_docs

def main():
    parser = argparse.ArgumentParser(description="CED-as-reranker PoC")
    parser.add_argument("--base_model", default="./outputs")
    parser.add_argument("--sft_adapter", default="./outputs")
    parser.add_argument("--data_dir", default="./data/docred")
    parser.add_argument("--output_dir", default="./outputs/eval_results")
    parser.add_argument("--nli_model_path", default="cross-encoder/nli-deberta-v3-base")
    parser.add_argument("--num_generations", type=int, default=8)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max_new_tokens", type=int, default=2048)
    parser.add_argument("--tau", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_docs", type=int, default=None)
    parser.add_argument("--wandb_run_name", type=str, default=None,
                        help="W&B run name. None = no logging.")
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # W&B init
    wandb_run = None
    if args.wandb_run_name:
        import wandb
        wandb_run = wandb.init(
            project="your-project",
            name=args.wandb_run_name,
            config=vars(args),
            tags=["ced-reranker", "inference-time"],
        )

    # --- Step 1: Load model & generate ---
    logger.info("Loading SFT model (merged, bf16, no quantize)...")
    model, tokenizer = load_model_and_tokenizer(
        args.base_model, sft_adapter=args.sft_adapter, quantize=False,
    )
    # Qwen3 generation_config override — must be explicit to avoid config defaults
    model.generation_config.temperature = args.temperature
    model.generation_config.top_k = 0
    model.generation_config.do_sample = True

    logger.info("Preparing dev data...")
    items = prepare_generation_data(args.data_dir, "dev", tokenizer)
    if args.max_docs:
        items = items[:args.max_docs]
    logger.info("Dev docs to process: %d", len(items))

    t0 = time.time()
    all_docs = run_generation(model, tokenizer, items, args, output_dir)
    gen_time = time.time() - t0
    logger.info("Generation done: %.1fs (%.2f s/doc)", gen_time, gen_time / max(len(items), 1))

    del model, tokenizer
    torch.cuda.empty_cache()

    # --- Step 2: CED scoring ---
    logger.info("Loading NLI model for CED scoring: %s", args.nli_model_path)
    ced_model = CEDRewardModel(model_name=args.nli_model_path, device="cuda")

    ced_list, f1_list = [], []
    ced_sel, oracle_sel, rand_sel, greedy_sel = {}, {}, {}, {}

    scores_file = output_dir / "per_doc_scores.jsonl"
    with open(scores_file, "w") as fout:
        for doc_id, doc in tqdm(all_docs.items(), desc="CED scoring"):
            cands = doc["candidates"]
            gold_t = doc["gold_triples"]
            sents = doc["sents"]

            ced_scores = [
                score_candidate_ced(c["parsed_triples"], sents, ced_model, tau=args.tau)
                for c in cands
            ]
            f1_scores = [
                candidate_rel_f1(c["parsed_triples"], gold_t)
                for c in cands
            ]

            fout.write(json.dumps({
                "doc_id": doc_id,
                "ced_scores": [round(s, 4) for s in ced_scores],
                "oracle_f1_scores": [round(s, 4) for s in f1_scores],
            }, ensure_ascii=False) + "\n")

            ced_list.extend(ced_scores)
            f1_list.extend(f1_scores)

            ced_sel[doc_id] = cands[int(np.argmax(ced_scores))]
            oracle_sel[doc_id] = cands[int(np.argmax(f1_scores))]
            rand_sel[doc_id] = cands[random.randint(0, len(cands) - 1)]

            if doc.get("greedy"):
                greedy_sel[doc_id] = doc["greedy"]

    del ced_model
    torch.cuda.empty_cache()

    # --- Step 3: Evaluate ---
    logger.info("Evaluating strategies...")

    with open(Path(args.data_dir) / "dev.json") as f:
        dev_data = json.load(f)
    if args.max_docs:
        keep = set(all_docs.keys())
        dev_data = [d for d in dev_data if d.get("title", "") in keep]
    gold = gold_from_docred(dev_data)

    train_file = str(Path(args.data_dir) / "train_annotated.json")
    results = {}
    for name, sel in [
        ("greedy_baseline", greedy_sel),
        ("ced_reranker", ced_sel),
        ("oracle_reranker", oracle_sel),
        ("random_baseline", rand_sel),
    ]:
        if not sel:
            continue
        m = evaluate_strategy(sel, gold, train_file)
        results[name] = m
        logger.info("%s: f1=%.4f evi_f1=%.4f edcr=%.4f prec=%.4f rec=%.4f preds=%d",
                     name, m["f1"], m["evi_f1"], m.get("edcr", 0),
                     m["precision"], m["recall"], m["n_predictions"])

    # CED-F1 correlation (Spearman)
    from scipy.stats import spearmanr
    corr, pval = spearmanr(ced_list, f1_list)
    results["ced_f1_correlation"] = {
        "spearman_r": round(corr, 4),
        "p_value": float(f"{pval:.2e}"),
        "n_samples": len(ced_list),
    }
    logger.info("CED-F1 Spearman r=%.4f (p=%s, n=%d)", corr, f"{pval:.2e}", len(ced_list))

    results["config"] = vars(args)
    results["generation_time_seconds"] = round(gen_time, 1)

    results_path = output_dir / "results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    logger.info("Results → %s", results_path)

    # W&B log
    if wandb_run:
        import wandb
        log_data = {}
        for strategy in ["greedy_baseline", "ced_reranker", "oracle_reranker", "random_baseline"]:
            if strategy in results:
                m = results[strategy]
                for metric in ["f1", "evi_f1", "edcr", "precision", "recall", "ign_f1"]:
                    if metric in m:
                        log_data[f"{strategy}/{metric}"] = m[metric]
        log_data["ced_f1_spearman_r"] = results["ced_f1_correlation"]["spearman_r"]
        log_data["generation_time_seconds"] = gen_time
        wandb.log(log_data)
        wandb.finish()

    # Console summary
    print("\n" + "=" * 80)
    print(f"  CED-as-Reranker  (N={args.num_generations}, T={args.temperature}, tau={args.tau}, "
          f"docs={len(all_docs)})")
    print("=" * 80)
    print(f"  {'Strategy':<20s} {'rel_f1':>8s} {'evi_f1':>8s} {'EDCR':>8s} "
          f"{'prec':>8s} {'recall':>8s} {'ign_f1':>8s} {'preds':>6s}")
    print("-" * 80)
    for tag, label in [
        ("greedy_baseline", "Greedy baseline"),
        ("random_baseline", "Random (N=8)"),
        ("ced_reranker", "CED reranker"),
        ("oracle_reranker", "Oracle (upper)"),
    ]:
        if tag not in results:
            continue
        m = results[tag]
        print(f"  {label:<20s} {m['f1']:>8.4f} {m['evi_f1']:>8.4f} "
              f"{m.get('edcr',0):>8.4f} {m['precision']:>8.4f} "
              f"{m['recall']:>8.4f} {m['ign_f1']:>8.4f} {m['n_predictions']:>6d}")
    print("-" * 80)
    c = results["ced_f1_correlation"]
    print(f"  CED-F1 Spearman r = {c['spearman_r']:.4f}  (p = {c['p_value']})")

    # Delta vs greedy
    if "greedy_baseline" in results and "ced_reranker" in results:
        g = results["greedy_baseline"]
        r = results["ced_reranker"]
        delta_f1 = r["f1"] - g["f1"]
        delta_evi = r["evi_f1"] - g["evi_f1"]
        print(f"  CED vs Greedy: Δrel_f1={delta_f1:+.4f}, Δevi_f1={delta_evi:+.4f}")
    if "greedy_baseline" in results and "oracle_reranker" in results:
        g = results["greedy_baseline"]
        o = results["oracle_reranker"]
        headroom = o["f1"] - g["f1"]
        print(f"  Oracle headroom:  Δrel_f1={headroom:+.4f}")
    print("=" * 80)

if __name__ == "__main__":
    main()
