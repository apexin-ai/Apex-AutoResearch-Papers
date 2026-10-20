#!/usr/bin/env python3
"""Systematic Nocuity Deep Dive: convergence analysis, linguistic comparison, mechanism convergence."""

import json
import csv
import re
from collections import defaultdict, Counter
from pathlib import Path
from scipy import stats
import numpy as np

BASE = Path(__file__).resolve().parent
DATA = BASE / "_project" / "data"
ANALYSIS = BASE / "full_study" / "analysis"

MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
VIOLATION_BINARY = {"moderate", "critical"}


def load_per_clause_summary():
    rows = []
    with open(ANALYSIS / "per_clause_summary.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["violation_rate"] = float(row["violation_rate"])
            row["n_violations"] = int(row["n_violations"])
            rows.append(row)
    return rows


def load_clause_templates():
    result = {}
    # Primary templates (no coreferential)
    with open(DATA / "clause_templates_full.json") as f:
        for t in json.load(f):
            result[t["clause_id"]] = t
    # Backup file has coreferential templates
    backup = DATA / "clause_templates_full_28b249.json"
    if backup.exists():
        with open(backup) as f:
            for t in json.load(f):
                if t["clause_id"] not in result:
                    result[t["clause_id"]] = t
    return result


def load_failure_modes():
    """Load all per-model failure mode files (primary only)."""
    fm_files = {
        "gpt-5.4": DATA / "failure_modes.jsonl",
        "gpt-4.1": DATA / "failure_modes_gpt41.jsonl",
        "claude-sonnet-4-6": DATA / "failure_modes_claude.jsonl",
        "deepseek-v3": DATA / "failure_modes_deepseek.jsonl",
        "qwen3-235b": DATA / "failure_modes_qwen3.jsonl",
    }
    all_fms = []
    for model, path in fm_files.items():
        if path.exists():
            with open(path) as f:
                for line in f:
                    rec = json.loads(line)
                    all_fms.append(rec)
    return all_fms


def compute_convergence(rows):
    """For each clause, count how many models triggered a violation (ambiguous only)."""
    clause_models = defaultdict(dict)
    clause_types = {}
    for row in rows:
        if row["condition"] != "ambiguous":
            continue
        cid = row["clause_id"]
        model = row["model"]
        clause_models[cid][model] = row["violation_rate"] > 0
        clause_types[cid] = row["ambiguity_type"]

    convergence = {}
    for cid, model_results in clause_models.items():
        n_violating = sum(1 for v in model_results.values() if v)
        convergence[cid] = {
            "n_violating": n_violating,
            "ambiguity_type": clause_types[cid],
            "models_violated": [m for m, v in model_results.items() if v],
        }
    return convergence


def classify(n_violating):
    if n_violating == 5:
        return "universal"
    elif n_violating >= 3:
        return "majority"
    elif n_violating >= 1:
        return "model_specific"
    else:
        return "safe"


def convergence_distribution(convergence):
    dist = Counter()
    for cid, info in convergence.items():
        cat = classify(info["n_violating"])
        dist[cat] += 1
    total = sum(dist.values())
    return {
        cat: {"count": dist[cat], "pct": round(100 * dist[cat] / total, 1)}
        for cat in ["universal", "majority", "model_specific", "safe"]
    }, total


def per_type_breakdown(convergence):
    type_cats = defaultdict(lambda: Counter())
    for cid, info in convergence.items():
        cat = classify(info["n_violating"])
        type_cats[info["ambiguity_type"]][cat] += 1

    result = {}
    for atype in sorted(type_cats.keys()):
        cats = type_cats[atype]
        total = sum(cats.values())
        result[atype] = {
            "n_clauses": total,
            "universal": cats["universal"],
            "majority": cats["majority"],
            "model_specific": cats["model_specific"],
            "safe": cats["safe"],
            "universal_rate": round(cats["universal"] / total, 4) if total else 0,
            "majority_plus_rate": round((cats["universal"] + cats["majority"]) / total, 4) if total else 0,
        }
    return result


def fisher_incompleteness_universal(per_type):
    inc = per_type["incompleteness"]
    inc_universal = inc["universal"]
    inc_other = inc["n_clauses"] - inc_universal

    other_universal = sum(v["universal"] for k, v in per_type.items() if k != "incompleteness")
    other_other = sum(v["n_clauses"] - v["universal"] for k, v in per_type.items() if k != "incompleteness")

    table = [[inc_universal, inc_other], [other_universal, other_other]]
    odds_ratio, p_value = stats.fisher_exact(table)
    return {
        "contingency_table": {
            "incompleteness": {"universal": inc_universal, "non_universal": inc_other},
            "other_types": {"universal": other_universal, "non_universal": other_other},
        },
        "odds_ratio": round(float(odds_ratio), 3),
        "p_value": float(p_value),
        "significant": p_value < 0.05,
    }


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


def count_conditionals(tokens):
    conditionals = {"if", "when", "unless", "provided", "except", "however",
                    "otherwise", "whether", "until", "should", "may", "might",
                    "could", "would"}
    return sum(1 for t in tokens if t in conditionals)


def count_negations(tokens):
    negations = {"not", "no", "never", "neither", "nor", "cannot", "without",
                 "none", "nothing", "nowhere", "don't", "doesn't", "didn't",
                 "won't", "wouldn't", "shouldn't", "couldn't", "isn't", "aren't",
                 "wasn't", "weren't", "hasn't", "haven't", "hadn't"}
    return sum(1 for t in tokens if t in negations)


def linguistic_comparison(convergence, templates):
    universal_ids = [cid for cid, info in convergence.items() if info["n_violating"] == 5]
    safe_ids = [cid for cid, info in convergence.items() if info["n_violating"] == 0]

    def extract_features(clause_ids):
        features = {"token_len_amb": [], "token_len_unamb": [], "token_delta": [],
                     "conditional_count": [], "negation_count": []}
        for cid in clause_ids:
            if cid not in templates:
                continue
            t = templates[cid]
            amb_tokens = tokenize(t["ambiguous_clause"])
            unamb_tokens = tokenize(t["unambiguous_clause"])
            features["token_len_amb"].append(len(amb_tokens))
            features["token_len_unamb"].append(len(unamb_tokens))
            features["token_delta"].append(len(unamb_tokens) - len(amb_tokens))
            features["conditional_count"].append(count_conditionals(amb_tokens))
            features["negation_count"].append(count_negations(amb_tokens))
        return features

    uni_feats = extract_features(universal_ids)
    safe_feats = extract_features(safe_ids)

    comparison = {}
    for feat_name in ["token_len_amb", "token_delta", "conditional_count", "negation_count"]:
        u_vals = np.array(uni_feats[feat_name])
        s_vals = np.array(safe_feats[feat_name])
        t_stat, t_p = stats.ttest_ind(u_vals, s_vals, equal_var=False)
        mw_stat, mw_p = stats.mannwhitneyu(u_vals, s_vals, alternative="two-sided")
        comparison[feat_name] = {
            "universal_mean": round(float(u_vals.mean()), 2),
            "universal_std": round(float(u_vals.std()), 2),
            "safe_mean": round(float(s_vals.mean()), 2),
            "safe_std": round(float(s_vals.std()), 2),
            "welch_t": round(float(t_stat), 3),
            "welch_p": float(t_p),
            "mann_whitney_U": float(mw_stat),
            "mann_whitney_p": float(mw_p),
            "significant_005": t_p < 0.05 or mw_p < 0.05,
        }

    # Also compute compression ratio: ambiguous / unambiguous token length
    u_ratios = np.array(uni_feats["token_len_amb"]) / np.array(uni_feats["token_len_unamb"])
    s_ratios = np.array(safe_feats["token_len_amb"]) / np.array(safe_feats["token_len_unamb"])
    t_stat, t_p = stats.ttest_ind(u_ratios, s_ratios, equal_var=False)
    mw_stat, mw_p = stats.mannwhitneyu(u_ratios, s_ratios, alternative="two-sided")
    comparison["compression_ratio"] = {
        "description": "ambiguous_len / unambiguous_len (lower = more compressed = more info lost)",
        "universal_mean": round(float(u_ratios.mean()), 3),
        "universal_std": round(float(u_ratios.std()), 3),
        "safe_mean": round(float(s_ratios.mean()), 3),
        "safe_std": round(float(s_ratios.std()), 3),
        "welch_t": round(float(t_stat), 3),
        "welch_p": float(t_p),
        "mann_whitney_U": float(mw_stat),
        "mann_whitney_p": float(mw_p),
        "significant_005": t_p < 0.05 or mw_p < 0.05,
    }

    return comparison, len(universal_ids), len(safe_ids)


def list_universal_clauses(convergence, templates):
    universal = []
    for cid, info in convergence.items():
        if info["n_violating"] != 5:
            continue
        t = templates.get(cid, {})
        universal.append({
            "clause_id": cid,
            "ambiguity_type": info["ambiguity_type"],
            "domain": t.get("domain", "unknown"),
            "ambiguous_clause": t.get("ambiguous_clause", ""),
            "models_violated": sorted(info["models_violated"]),
        })
    universal.sort(key=lambda x: (x["ambiguity_type"], x["clause_id"]))
    return universal


def mechanism_convergence(convergence, failure_modes):
    """For majority-convergent clauses (>=3 models violated), check if failure mode is also convergent."""
    # Build lookup: (clause_id, model) -> failure_mode
    fm_lookup = {}
    for rec in failure_modes:
        fm_lookup[(rec["clause_id"], rec["model"])] = rec["failure_mode"]

    majority_clauses = [
        (cid, info) for cid, info in convergence.items()
        if info["n_violating"] >= 3
    ]

    results = {
        "n_majority_clauses": len(majority_clauses),
        "n_with_fm_data": 0,
        "n_fm_convergent": 0,
        "n_fm_partial": 0,
        "n_fm_divergent": 0,
        "examples": [],
    }

    for cid, info in majority_clauses:
        violated_models = info["models_violated"]
        fms_for_clause = {}
        for model in violated_models:
            fm = fm_lookup.get((cid, model))
            if fm:
                fms_for_clause[model] = fm

        if len(fms_for_clause) < 2:
            continue

        results["n_with_fm_data"] += 1
        fm_values = list(fms_for_clause.values())
        fm_counter = Counter(fm_values)
        most_common_fm, most_common_count = fm_counter.most_common(1)[0]
        agreement_rate = most_common_count / len(fm_values)

        if agreement_rate >= 1.0:
            results["n_fm_convergent"] += 1
            label = "fully_convergent"
        elif agreement_rate >= 0.6:
            results["n_fm_partial"] += 1
            label = "partial"
        else:
            results["n_fm_divergent"] += 1
            label = "divergent"

        if len(results["examples"]) < 10:
            results["examples"].append({
                "clause_id": cid,
                "ambiguity_type": info["ambiguity_type"],
                "n_violating": info["n_violating"],
                "failure_modes": fms_for_clause,
                "dominant_fm": most_common_fm,
                "agreement_rate": round(agreement_rate, 2),
                "convergence_label": label,
            })

    if results["n_with_fm_data"] > 0:
        results["fm_convergence_rate"] = round(
            results["n_fm_convergent"] / results["n_with_fm_data"], 3
        )
        results["fm_partial_plus_rate"] = round(
            (results["n_fm_convergent"] + results["n_fm_partial"]) / results["n_with_fm_data"], 3
        )
    else:
        results["fm_convergence_rate"] = None
        results["fm_partial_plus_rate"] = None

    return results


def per_model_profile(convergence):
    """Which models are most/least likely to violate on universal vs safe clauses."""
    model_violation_by_category = defaultdict(lambda: defaultdict(int))
    model_total_by_category = defaultdict(lambda: defaultdict(int))

    for cid, info in convergence.items():
        cat = classify(info["n_violating"])
        for model in MODELS:
            model_total_by_category[model][cat] += 1
            if model in info["models_violated"]:
                model_violation_by_category[model][cat] += 1

    result = {}
    for model in MODELS:
        result[model] = {}
        for cat in ["universal", "majority", "model_specific", "safe"]:
            total = model_total_by_category[model][cat]
            violated = model_violation_by_category[model][cat]
            result[model][cat] = {
                "violated": violated,
                "total": total,
                "rate": round(violated / total, 3) if total else 0,
            }
    return result


def fine_grained_distribution(convergence):
    """Distribution by exact number of models violating (0-5)."""
    dist = Counter()
    for cid, info in convergence.items():
        dist[info["n_violating"]] += 1
    total = sum(dist.values())
    return {
        str(k): {"count": dist[k], "pct": round(100 * dist[k] / total, 1)}
        for k in range(6)
    }


def main():
    print("Loading data...")
    rows = load_per_clause_summary()
    templates = load_clause_templates()
    failure_modes = load_failure_modes()

    print("Computing convergence scores...")
    convergence = compute_convergence(rows)
    print(f"  Total ambiguous clauses: {len(convergence)}")

    # 1. Distribution
    dist, total = convergence_distribution(convergence)
    fine_dist = fine_grained_distribution(convergence)
    print(f"  Distribution: {dist}")

    # 2. Per-type breakdown
    per_type = per_type_breakdown(convergence)
    fisher = fisher_incompleteness_universal(per_type)
    print(f"  Incompleteness universal rate: {per_type['incompleteness']['universal_rate']}")
    print(f"  Fisher test p={fisher['p_value']:.4f}, OR={fisher['odds_ratio']}")

    # Ranking
    type_ranking_universal = sorted(per_type.keys(), key=lambda t: per_type[t]["universal_rate"], reverse=True)
    type_ranking_majority = sorted(per_type.keys(), key=lambda t: per_type[t]["majority_plus_rate"], reverse=True)

    # 3. Linguistic comparison
    ling_comp, n_uni, n_safe = linguistic_comparison(convergence, templates)
    print(f"  Linguistic comparison: {n_uni} universal vs {n_safe} safe clauses")
    for feat, vals in ling_comp.items():
        sig = "*" if vals.get("significant_005") else ""
        print(f"    {feat}: uni={vals['universal_mean']:.2f}±{vals['universal_std']:.2f}, "
              f"safe={vals['safe_mean']:.2f}±{vals['safe_std']:.2f} {sig}")

    # 4. Universal clause list
    universal_list = list_universal_clauses(convergence, templates)
    print(f"  Universal clauses: {len(universal_list)}")

    # 5. Mechanism convergence
    mech = mechanism_convergence(convergence, failure_modes)
    print(f"  Mechanism convergence: {mech['n_fm_convergent']}/{mech['n_with_fm_data']} "
          f"fully convergent (rate={mech['fm_convergence_rate']})")

    # 6. Per-model profile
    model_profile = per_model_profile(convergence)

    # Assemble output
    output = {
        "convergence_distribution": {
            "four_category": dist,
            "fine_grained_0_to_5": fine_dist,
            "total_clauses": total,
        },
        "per_type_convergence_breakdown": {
            "per_type": per_type,
            "ranking_by_universal_rate": type_ranking_universal,
            "ranking_by_majority_plus_rate": type_ranking_majority,
            "fisher_incompleteness_vs_others": fisher,
        },
        "universal_clauses_list": {
            "count": len(universal_list),
            "clauses": universal_list,
        },
        "linguistic_comparison": {
            "n_universal": n_uni,
            "n_safe": n_safe,
            "features": ling_comp,
        },
        "mechanism_convergence": mech,
        "per_model_profile": model_profile,
    }

    out_path = BASE / "analysis_systematic_nocuity.json"

    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, (np.bool_,)):
                return bool(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return super().default(obj)

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, cls=NpEncoder)
    print(f"\nSaved: {out_path}")

    # Generate summary markdown
    md = generate_summary(output)
    md_path = BASE / "analysis_systematic_nocuity_summary.md"
    with open(md_path, "w") as f:
        f.write(md)
    print(f"Saved: {md_path}")


def generate_summary(data):
    lines = []
    lines.append("# Systematic Nocuity Deep Dive\n")

    # 1. Convergence distribution
    lines.append("## 1. Convergence Distribution\n")
    d = data["convergence_distribution"]
    lines.append(f"Total ambiguous clauses: {d['total_clauses']}\n")
    lines.append("| Category | Count | % |")
    lines.append("|----------|-------|---|")
    for cat in ["universal", "majority", "model_specific", "safe"]:
        info = d["four_category"][cat]
        label = {"universal": "Universal (5/5)", "majority": "Majority (3-4/5)",
                 "model_specific": "Model-specific (1-2/5)", "safe": "Safe (0/5)"}[cat]
        lines.append(f"| {label} | {info['count']} | {info['pct']}% |")
    lines.append("")
    lines.append("Fine-grained (by exact model count):\n")
    lines.append("| Models violated | Count | % |")
    lines.append("|----------------|-------|---|")
    for k in range(6):
        info = d["fine_grained_0_to_5"][str(k)]
        lines.append(f"| {k}/5 | {info['count']} | {info['pct']}% |")
    lines.append("")

    # 2. Per-type breakdown
    lines.append("## 2. Per-Type Convergence\n")
    pt = data["per_type_convergence_breakdown"]
    lines.append("| Type | Universal | Majority(3-4) | Model-specific | Safe | Universal% | Majority+% |")
    lines.append("|------|-----------|---------------|----------------|------|------------|------------|")
    for atype in pt["ranking_by_universal_rate"]:
        info = pt["per_type"][atype]
        lines.append(f"| {atype} | {info['universal']} | {info['majority']} | "
                     f"{info['model_specific']} | {info['safe']} | "
                     f"{info['universal_rate']*100:.0f}% | {info['majority_plus_rate']*100:.0f}% |")
    lines.append("")

    fisher = pt["fisher_incompleteness_vs_others"]
    lines.append(f"**Fisher exact test** (incompleteness universal rate vs others): "
                 f"OR={fisher['odds_ratio']}, p={fisher['p_value']:.4f}, "
                 f"{'significant' if fisher['significant'] else 'not significant'}\n")

    lines.append(f"Ranking by universal rate: {' > '.join(pt['ranking_by_universal_rate'])}\n")
    lines.append(f"Ranking by majority+ rate: {' > '.join(pt['ranking_by_majority_plus_rate'])}\n")

    # 3. Linguistic comparison
    lines.append("## 3. Universal vs Safe: Linguistic Features\n")
    lc = data["linguistic_comparison"]
    lines.append(f"Comparing {lc['n_universal']} universal clauses vs {lc['n_safe']} safe clauses:\n")
    lines.append("| Feature | Universal (mean±std) | Safe (mean±std) | Welch p | MW p | Sig? |")
    lines.append("|---------|---------------------|-----------------|---------|------|------|")
    for feat, vals in lc["features"].items():
        sig = "Yes" if vals.get("significant_005") else "No"
        lines.append(f"| {feat} | {vals['universal_mean']:.2f}±{vals['universal_std']:.2f} | "
                     f"{vals['safe_mean']:.2f}±{vals['safe_std']:.2f} | "
                     f"{vals['welch_p']:.4f} | {vals['mann_whitney_p']:.4f} | {sig} |")
    lines.append("")

    # 4. Universal clauses list
    lines.append("## 4. All Universal Violation Clauses\n")
    ucl = data["universal_clauses_list"]
    lines.append(f"Total: {ucl['count']} clauses\n")
    for c in ucl["clauses"]:
        text = c["ambiguous_clause"][:120] + ("..." if len(c["ambiguous_clause"]) > 120 else "")
        lines.append(f"- **{c['clause_id']}** [{c['ambiguity_type']}, {c['domain']}]: {text}")
    lines.append("")

    # 5. Mechanism convergence
    lines.append("## 5. Mechanism Convergence\n")
    mc = data["mechanism_convergence"]
    lines.append(f"- Majority-convergent clauses (>=3 models violated): {mc['n_majority_clauses']}")
    lines.append(f"- With multi-model failure mode data: {mc['n_with_fm_data']}")
    lines.append(f"- Fully convergent FM (all models same failure mode): {mc['n_fm_convergent']} "
                 f"({mc['fm_convergence_rate']})")
    lines.append(f"- Partial convergent FM (>=60% same): {mc['n_fm_partial']}")
    lines.append(f"- Divergent FM: {mc['n_fm_divergent']}")
    lines.append(f"- Convergent+partial rate: {mc['fm_partial_plus_rate']}")
    lines.append("")

    if mc["examples"]:
        lines.append("### Selected Examples\n")
        for ex in mc["examples"][:5]:
            lines.append(f"**{ex['clause_id']}** ({ex['ambiguity_type']}, {ex['n_violating']}/5 violated)")
            lines.append(f"  Failure modes: {ex['failure_modes']}")
            lines.append(f"  Dominant: {ex['dominant_fm']} (agreement={ex['agreement_rate']})\n")

    # 6. Per-model profile
    lines.append("## 6. Per-Model Violation Profile\n")
    mp = data["per_model_profile"]
    lines.append("| Model | Universal violation rate | Majority rate | Model-specific rate | Safe rate |")
    lines.append("|-------|------------------------|---------------|--------------------:|----------:|")
    for model in MODELS:
        info = mp[model]
        lines.append(f"| {model} | {info['universal']['rate']:.3f} | "
                     f"{info['majority']['rate']:.3f} | "
                     f"{info['model_specific']['rate']:.3f} | "
                     f"{info['safe']['rate']:.3f} |")
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
