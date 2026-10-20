#!/usr/bin/env python3
"""D012 Phase 1: Claim-level entailment rescoring.

For each chain's formalized claims, checks whether each claim is
logically entailed by (problem premises + prior claims in the chain).

ic_entail = entailed_count / total_claims
ic_consist = consistent_count / total_claims  (fallback: not contradicted by premises)

Compares discrimination power (Cohen's d) of ic_entail vs the old ic_score.

Usage:
    cd /root && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
    HF_DATASETS_OFFLINE=1 python /root/autodl-tmp/svs_formal_verification/entailment_rescorer.py
"""

import json
import logging
import random
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, "/root")

import yaml
from svs_pipeline.config import PipelineConfig
from svs_pipeline.types import Problem, AtomicClaim
from svs_pipeline.data import load_proofwriter
from svs_pipeline.generation import ChainSampler
from svs_pipeline.formalization import ClaimDecomposer, AutoFormalizer, VocabNormalizer
from svs_pipeline.z3_sandbox import get_sandbox

logger = logging.getLogger(__name__)

OUTPUT_PATH = Path("/root/outputs/entailment_rescore_results.json")


def load_config() -> PipelineConfig:
    cfg = PipelineConfig()
    with open("/root/config_local.yaml") as f:
        raw = yaml.safe_load(f)
    for section_name in ("api", "sampling", "verification", "mvp"):
        section_obj = getattr(cfg, section_name)
        for k, v in raw.get(section_name, {}).items():
            if hasattr(section_obj, k):
                setattr(section_obj, k, v)
    if "output_dir" in raw:
        cfg.output_dir = raw["output_dir"]
    return cfg


def get_target_problem_ids() -> set[str]:
    with open("/root/outputs/results_partial.json") as f:
        data = json.load(f)
    return {item["problem_id"] for item in data}


def formalize_premises(
    premises: list[str], vocab: dict, formalizer: AutoFormalizer, problem_id: str
) -> list[dict]:
    fake_claims = [
        AtomicClaim(chain_id=-1, problem_id=problem_id, claim_index=i, text=p)
        for i, p in enumerate(premises)
    ]
    formalized = formalizer.formalize_batch(fake_claims, vocab)
    results = []
    for c in formalized:
        results.append({
            "text": c.text,
            "fol": c.fol,
            "z3_parseable": c.z3_parseable,
            "error": c.fol_error,
        })
    return results


def entailment_rescore_chain(
    claims: list[AtomicClaim],
    premise_fols: list[str],
    vocab: dict,
    z3_timeout_ms: int = 30000,
) -> dict:
    sandbox = get_sandbox()
    formalized = [(i, c) for i, c in enumerate(claims) if c.z3_parseable and c.fol]

    if not formalized:
        return {
            "entailed_count": 0,
            "consistent_count": 0,
            "formalized_count": 0,
            "total_claims": len(claims),
            "ic_entail": 0.0,
            "ic_consist": 0.0,
            "claim_results": [],
        }

    claim_results = []
    entailed_count = 0
    consistent_count = 0
    prior_fols = []

    for orig_idx, claim in formalized:
        entails, status = sandbox.check_entailment(
            prior_fols, vocab, premise_fols, claim.fol, z3_timeout_ms
        )

        is_consistent = sandbox.check_sat_set(
            [claim.fol], vocab, premise_fols, z3_timeout_ms
        )

        if entails:
            entailed_count += 1
        if is_consistent:
            consistent_count += 1

        claim_results.append({
            "claim_index": orig_idx,
            "text": claim.text[:120],
            "fol": claim.fol,
            "entailed": entails,
            "entail_status": status,
            "consistent": is_consistent,
        })

        prior_fols.append(claim.fol)

    total = len(claims)
    n_form = len(formalized)

    return {
        "entailed_count": entailed_count,
        "consistent_count": consistent_count,
        "formalized_count": n_form,
        "total_claims": total,
        "ic_entail": entailed_count / total if total > 0 else 0.0,
        "ic_consist": consistent_count / total if total > 0 else 0.0,
        "claim_results": claim_results,
    }


def compute_summary(chains: list[dict]) -> dict:
    correct = [c for c in chains if c["is_correct"]]
    wrong = [c for c in chains if not c["is_correct"]]

    def desc(values):
        if not values:
            return {"count": 0}
        a = np.array(values)
        return {
            "count": len(a),
            "mean": float(np.mean(a)),
            "std": float(np.std(a)),
            "median": float(np.median(a)),
            "min": float(np.min(a)),
            "max": float(np.max(a)),
        }

    def cohens_d(a, b):
        if not a or not b:
            return None
        na, nb = np.array(a, dtype=float), np.array(b, dtype=float)
        pooled = np.sqrt((np.var(na) + np.var(nb)) / 2)
        if pooled < 1e-10:
            return 0.0
        return float((np.mean(na) - np.mean(nb)) / pooled)

    def ci_95_bootstrap(a, b, n_boot=5000):
        if not a or not b:
            return None
        na, nb = np.array(a), np.array(b)
        rng = np.random.RandomState(42)
        ds = []
        for _ in range(n_boot):
            sa = rng.choice(na, size=len(na), replace=True)
            sb = rng.choice(nb, size=len(nb), replace=True)
            p = np.sqrt((np.var(sa) + np.var(sb)) / 2)
            ds.append((np.mean(sa) - np.mean(sb)) / p if p > 1e-10 else 0.0)
        ds.sort()
        return [float(ds[int(0.025 * n_boot)]), float(ds[int(0.975 * n_boot)])]

    metrics = {}
    for name in ("ic_score_old", "ic_entail", "ic_consist"):
        c_vals = [c[name] for c in correct]
        w_vals = [c[name] for c in wrong]
        d = cohens_d(c_vals, w_vals)
        ci = ci_95_bootstrap(c_vals, w_vals)
        t_stat, p_val = (None, None)
        if len(c_vals) >= 2 and len(w_vals) >= 2:
            t_stat, p_val = stats.ttest_ind(c_vals, w_vals)
            t_stat, p_val = float(t_stat), float(p_val)
        metrics[name] = {
            "correct": desc(c_vals),
            "wrong": desc(w_vals),
            "cohens_d": d,
            "ci_95": ci,
            "ttest_t": t_stat,
            "ttest_p": p_val,
        }

    entail_rates = [
        c["entailed_count"] / c["formalized_claims"]
        if c["formalized_claims"] > 0 else 0
        for c in chains
    ]
    consist_rates = [
        c["consistent_count"] / c["formalized_claims"]
        if c["formalized_claims"] > 0 else 0
        for c in chains
    ]

    return {
        "n_problems": len(set(c["problem_id"] for c in chains)),
        "n_chains": len(chains),
        "n_correct": len(correct),
        "n_wrong": len(wrong),
        "metrics": metrics,
        "entailment_rate": desc(entail_rates),
        "consistency_rate": desc(consist_rates),
    }


def print_stats(chains: list[dict]):
    s = compute_summary(chains)

    print("\n" + "=" * 70)
    print("ENTAILMENT RESCORING RESULTS")
    print("=" * 70)
    print(f"Problems: {s['n_problems']}, Chains: {s['n_chains']}")
    print(f"Correct: {s['n_correct']}, Wrong: {s['n_wrong']}")

    for name in ("ic_score_old", "ic_entail", "ic_consist"):
        m = s["metrics"][name]
        print(f"\n--- {name} ---")
        c, w = m["correct"], m["wrong"]
        if c["count"] and w["count"]:
            print(f"  Correct: {c['mean']:.4f} +/- {c['std']:.4f} (n={c['count']})")
            print(f"  Wrong:   {w['mean']:.4f} +/- {w['std']:.4f} (n={w['count']})")
        d = m["cohens_d"]
        print(f"  Cohen's d: {d:.4f}" if d is not None else "  Cohen's d: N/A")
        ci = m["ci_95"]
        if ci:
            print(f"  95% CI:  [{ci[0]:.4f}, {ci[1]:.4f}]")
        if m["ttest_p"] is not None:
            print(f"  t={m['ttest_t']:.4f}, p={m['ttest_p']:.6f}")

    er = s["entailment_rate"]
    cr = s["consistency_rate"]
    print(f"\nEntailment rate (per chain): mean={er.get('mean',0):.4f}, "
          f"median={er.get('median',0):.4f}, std={er.get('std',0):.4f}")
    print(f"Consistency rate (per chain): mean={cr.get('mean',0):.4f}, "
          f"median={cr.get('median',0):.4f}, std={cr.get('std',0):.4f}")

    # Sample claims
    entailed_ex, non_entailed_ex = [], []
    for c in chains:
        for d in c.get("claim_details", []):
            if d["entailed"] and len(entailed_ex) < 3:
                entailed_ex.append(d)
            elif (not d["entailed"] and d.get("entail_status") != "subprocess_error"
                  and len(non_entailed_ex) < 3):
                non_entailed_ex.append(d)

    if entailed_ex:
        print("\nSample ENTAILED claims:")
        for ex in entailed_ex:
            print(f"  + {ex['text']}")
            print(f"    FOL: {ex['fol']}")

    if non_entailed_ex:
        print("\nSample NON-ENTAILED claims:")
        for ex in non_entailed_ex:
            print(f"  - {ex['text']}")
            print(f"    FOL: {ex['fol']}")
            print(f"    status: {ex['entail_status']}")

    print("=" * 70)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    cfg = load_config()
    random.seed(cfg.mvp.seed)
    np.random.seed(cfg.mvp.seed)

    target_ids = get_target_problem_ids()
    logger.info("Target: %d problem IDs from results_partial.json", len(target_ids))

    problems = load_proofwriter(
        subset=cfg.mvp.subset,
        num_problems=cfg.mvp.num_problems,
        seed=cfg.mvp.seed,
    )
    problems = [p for p in problems if p.id in target_ids]
    logger.info("Matched %d problems", len(problems))

    # Load gold labels from original results
    with open("/root/outputs/results_partial.json") as f:
        orig = {item["problem_id"]: item for item in json.load(f)}

    sampler = ChainSampler(cfg.api, cfg.sampling)
    decomposer = ClaimDecomposer(cfg.api)
    vocab_norm = VocabNormalizer(cfg.api)
    formalizer = AutoFormalizer(cfg.api)
    sandbox = get_sandbox()

    all_chains = []
    t_global = time.time()

    for i, problem in enumerate(problems):
        t0 = time.time()
        gold_label = orig.get(problem.id, {}).get("gold_label", problem.label)
        logger.info("=== Problem %d/%d: %s (gold=%s) ===",
                     i + 1, len(problems), problem.id, gold_label)

        # 1. Sample chains
        chains = sampler.sample(problem, cfg.sampling.num_chains)
        logger.info("Sampled %d chains", len(chains))

        # 2. Vocab
        vocab = vocab_norm.extract_vocab(problem)

        # 3. Formalize premises
        prem_results = formalize_premises(
            problem.premises, vocab, formalizer, problem.id
        )
        premise_fols = [p["fol"] for p in prem_results if p["z3_parseable"]]
        logger.info("Premises formalized: %d/%d",
                     len(premise_fols), len(problem.premises))

        # 4. Process each chain
        for chain in chains:
            claims = decomposer.decompose(chain, problem)
            claims = formalizer.formalize_batch(claims, vocab)

            fol_strs = [c.fol for c in claims if c.z3_parseable and c.fol]
            n_formalized = len(fol_strs)

            # Old IC (SAT-based)
            is_sat, ic_old, mcs_size = sandbox.check_ic(
                fol_strs, vocab, len(claims),
                premise_fols=premise_fols,
                z3_timeout_ms=cfg.verification.z3_timeout_ms,
            )

            # New entailment-based IC
            entail = entailment_rescore_chain(
                claims, premise_fols, vocab, cfg.verification.z3_timeout_ms
            )

            is_correct = chain.answer == gold_label

            all_chains.append({
                "problem_id": problem.id,
                "chain_id": chain.chain_id,
                "answer": chain.answer,
                "gold_label": gold_label,
                "is_correct": is_correct,
                "total_claims": len(claims),
                "formalized_claims": n_formalized,
                "ic_score_old": ic_old,
                "ic_sat": is_sat,
                "mcs_size": mcs_size,
                "ic_entail": entail["ic_entail"],
                "ic_consist": entail["ic_consist"],
                "entailed_count": entail["entailed_count"],
                "consistent_count": entail["consistent_count"],
                "n_premises_fol": len(premise_fols),
                "claim_details": entail["claim_results"],
                "premise_fols": premise_fols,
            })

        elapsed = time.time() - t0
        logger.info("Problem %s done in %.1fs (%d chains)",
                     problem.id, elapsed, len(chains))

        # Checkpoint every 4 problems
        if (i + 1) % 4 == 0:
            OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(OUTPUT_PATH, "w") as f:
                json.dump({"chains": all_chains,
                           "summary": compute_summary(all_chains),
                           "status": "partial",
                           "problems_done": i + 1},
                          f, indent=2, default=str)
            logger.info("Checkpoint saved (%d problems)", i + 1)

    total_time = time.time() - t_global
    logger.info("Total time: %.1fs (%.1fs/problem)", total_time,
                total_time / len(problems) if problems else 0)

    print_stats(all_chains)

    summary = compute_summary(all_chains)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump({
            "chains": all_chains,
            "summary": summary,
            "status": "complete",
            "total_time_s": total_time,
        }, f, indent=2, default=str)
    logger.info("Final results saved to %s", OUTPUT_PATH)

    sandbox.shutdown()


if __name__ == "__main__":
    main()
