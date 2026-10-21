"""Analyze residual DR violations for Llama DocRED full_s1."""
import json
from collections import defaultdict, Counter

VALID_ENTITY_TYPES = {"PER", "ORG", "LOC", "TIME", "NUM", "MISC"}
ENTITY_TYPE_ALIASES = {
    "PERSON": "PER", "PEOPLE": "PER", "ORGANIZATION": "ORG",
    "ORGANISATION": "ORG", "LOCATION": "LOC", "NUMBER": "NUM",
    "NUMERICAL": "NUM", "MISCELLANEOUS": "MISC",
}

def norm_et(t):
    t = str(t).strip().upper()
    return ENTITY_TYPE_ALIASES.get(t, t)

def main():
    from scipy import stats
    import numpy as np

    with open("data/docred/ontology_constraints_docred.json") as f:
        ont = json.load(f)
    with open("data/docred/rel_info.json") as f:
        rel_info = json.load(f)

    name_to_pid = {}
    for pid, name in rel_info.items():
        name_to_pid[name.lower().strip()] = pid
        name_to_pid[pid.lower()] = pid

    constraints = {}
    for pid, info in ont["relation_constraints"].items():
        constraints[pid] = [tuple(p) for p in info["valid_pairs"]]

    def compute_dr(path):
        per_rel = defaultdict(lambda: {"total": 0, "violations": 0, "viol_pairs": Counter()})
        total, viol, docs, pf = 0, 0, 0, 0
        with open(path) as f:
            for line in f:
                rec = json.loads(line.strip())
                parsed = rec.get("parsed_output")
                if parsed is None:
                    pf += 1
                    continue
                docs += 1
                for rel in parsed.get("relations", []):
                    rel_name = str(rel.get("type") or rel.get("relation", "")).strip()
                    pid = name_to_pid.get(rel_name.lower().strip())
                    if pid is None or pid not in constraints:
                        continue
                    ht = norm_et(rel.get("head_type", ""))
                    tt = norm_et(rel.get("tail_type", ""))
                    if ht not in VALID_ENTITY_TYPES or tt not in VALID_ENTITY_TYPES:
                        continue
                    total += 1
                    per_rel[pid]["total"] += 1
                    pair = (ht, tt)
                    if pair not in constraints[pid]:
                        viol += 1
                        per_rel[pid]["violations"] += 1
                        per_rel[pid]["viol_pairs"][pair] += 1
        return per_rel, total, viol, docs, pf

    print("=== Llama S1 ===")
    ls1_pr, ls1_t, ls1_v, ls1_d, ls1_pf = compute_dr("outputs/llama_docred_full_s1.jsonl")
    print(f"Docs:{ls1_d} PF:{ls1_pf} Triples:{ls1_t} DR_viol:{ls1_v} Rate:{100*ls1_v/max(ls1_t,1):.2f}%")

    print("\n=== Llama Unconstrained ===")
    lu_pr, lu_t, lu_v, lu_d, lu_pf = compute_dr("outputs/llama_docred_unconstrained.jsonl")
    print(f"Docs:{lu_d} PF:{lu_pf} Triples:{lu_t} DR_viol:{lu_v} Rate:{100*lu_v/max(lu_t,1):.2f}%")

    with open("outputs/violation_report_docred_full_s1_unified.json") as f:
        qs1 = json.load(f)
    with open("outputs/violation_report_docred_unconstrained_unified.json") as f:
        qu = json.load(f)

    tightness = {}
    for pid in constraints:
        tightness[pid] = 1.0 - len(constraints[pid]) / 36.0

    all_pids = sorted(constraints.keys())
    results = []
    for pid in all_pids:
        name = rel_info.get(pid, pid)
        tau = tightness[pid]
        nv = len(constraints[pid])

        ls = ls1_pr.get(pid, {"total": 0, "violations": 0, "viol_pairs": Counter()})
        lr = ls["violations"] / ls["total"] if ls["total"] > 0 else None

        lu = lu_pr.get(pid, {"total": 0, "violations": 0, "viol_pairs": Counter()})
        lur = lu["violations"] / lu["total"] if lu["total"] > 0 else None

        qs = qs1.get("per_relation_dr", {}).get(pid, {"total": 0, "dr_violations": 0})
        qsr = qs["dr_violations"] / qs["total"] if qs["total"] > 0 else None

        qun = qu.get("per_relation_dr", {}).get(pid, {"total": 0, "dr_violations": 0})
        qur = qun["dr_violations"] / qun["total"] if qun["total"] > 0 else None

        tp = ""
        if ls.get("viol_pairs"):
            p = ls["viol_pairs"].most_common(1)[0]
            tp = f"{p[0][0]}->{p[0][1]}({p[1]})"

        results.append({
            "pid": pid, "name": name, "n_valid": nv, "tau": round(tau, 4),
            "ls1_tot": ls["total"], "ls1_viol": ls["violations"], "ls1_rate": lr,
            "lu_tot": lu["total"], "lu_viol": lu["violations"], "lu_rate": lur,
            "qs1_tot": qs["total"], "qs1_viol": qs.get("dr_violations", 0), "qs1_rate": qsr,
            "qu_tot": qun["total"], "qu_viol": qun.get("dr_violations", 0), "qu_rate": qur,
            "top_pair": tp,
            "all_pairs": dict((f"{k[0]}->{k[1]}", v) for k, v in ls.get("viol_pairs", {}).items()),
        })

    # Correlation
    tv, dv = [], []
    for r in results:
        if r["ls1_tot"] >= 5 and r["ls1_rate"] is not None:
            tv.append(r["tau"])
            dv.append(r["ls1_rate"])
    sp_rho, sp_p = stats.spearmanr(tv, dv)
    pe_r, pe_p = stats.pearsonr(tv, dv)
    print(f"\nCorrelation (Llama S1, n={len(tv)}): Spearman rho={sp_rho:.4f} p={sp_p:.4e}, Pearson r={pe_r:.4f} p={pe_p:.4e}")

    tvq, dvq = [], []
    for r in results:
        if r["qs1_tot"] and r["qs1_tot"] >= 5 and r["qs1_rate"] is not None:
            tvq.append(r["tau"])
            dvq.append(r["qs1_rate"])
    sq_rho, sq_p = stats.spearmanr(tvq, dvq)
    print(f"Correlation (Qwen S1, n={len(tvq)}): Spearman rho={sq_rho:.4f} p={sq_p:.4e}")

    # Tightness comparison
    vt = [r["tau"] for r in results if r["ls1_viol"] > 0 and r["ls1_tot"] >= 5]
    nvt = [r["tau"] for r in results if r["ls1_viol"] == 0 and r["ls1_tot"] >= 5]
    if vt and nvt:
        mwu, mwp = stats.mannwhitneyu(vt, nvt, alternative="greater")
        print(f"\nTightness: violating(n={len(vt)}) mean={np.mean(vt):.3f}, non-viol(n={len(nvt)}) mean={np.mean(nvt):.3f}, MWU p={mwp:.4e}")

    # Top-15
    top15 = sorted(results, key=lambda x: x["ls1_viol"], reverse=True)[:15]
    print(f"\n--- Top-15 Violating Relations (Llama S1) ---")
    for r in top15:
        lr_s = f'{100*r["ls1_rate"]:.1f}%' if r["ls1_rate"] else "N/A"
        ur_s = f'{100*r["lu_rate"]:.1f}%' if r["lu_rate"] else "N/A"
        qr_s = f'{100*r["qs1_rate"]:.1f}%' if r["qs1_rate"] else "N/A"
        print(f'{r["pid"]:<8} {r["name"][:35]:<36} V={r["ls1_viol"]:>4}/{r["ls1_tot"]:>5} ({lr_s:>6}) tau={r["tau"]:.3f} Unc={ur_s:>6} Qwen={qr_s:>6} {r["top_pair"]}')

    # Zero violations
    active = [r for r in results if r["ls1_tot"] > 0]
    zero = [r for r in active if r["ls1_viol"] == 0]
    print(f"\nZero-viol: {len(zero)}/{len(active)} relations")
    for r in sorted(zero, key=lambda x: -x["ls1_tot"])[:8]:
        print(f'  {r["pid"]:<8} {r["name"][:35]:<36} ({r["ls1_tot"]} triples, tau={r["tau"]:.3f})')

    # Save
    output = {
        "llama_s1": {"docs": ls1_d, "pf": ls1_pf, "triples": ls1_t, "dr_violations": ls1_v,
                     "dr_pct": round(100 * ls1_v / max(ls1_t, 1), 2)},
        "llama_unc": {"docs": lu_d, "pf": lu_pf, "triples": lu_t, "dr_violations": lu_v,
                      "dr_pct": round(100 * lu_v / max(lu_t, 1), 2)},
        "correlation": {
            "llama_s1": {"n": len(tv), "spearman_rho": round(float(sp_rho), 4),
                         "spearman_p": float(sp_p), "pearson_r": round(float(pe_r), 4),
                         "pearson_p": float(pe_p)},
            "qwen_s1": {"n": len(tvq), "spearman_rho": round(float(sq_rho), 4),
                        "spearman_p": float(sq_p)},
        },
        "tightness": {
            "viol_mean": round(float(np.mean(vt)), 4) if vt else None,
            "nonviol_mean": round(float(np.mean(nvt)), 4) if nvt else None,
        },
        "per_relation": results,
    }
    with open("outputs/dr_residual_analysis.json", "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False, default=float)
    print("\nSaved outputs/dr_residual_analysis.json")

if __name__ == "__main__":
    main()
