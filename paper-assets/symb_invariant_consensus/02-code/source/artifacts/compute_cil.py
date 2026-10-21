"""
E5: CIL (Cumulative Information Lift) Computation
CIL(V,G) = log2[P(V correct | G wrong) / P(V correct | G correct)]
"""
import json
import os
import sys
import numpy as np
from pathlib import Path
from scipy import stats

RESULTS = Path("/root/symb_invariant_consensus/results")
OUT_DIR = RESULTS / "exp_d134_cil"

def cil_from_counts(both_right, v_right_g_wrong, g_right_v_wrong, both_wrong):
    """Compute CIL from 2x2 contingency table."""
    n_g_wrong = v_right_g_wrong + both_wrong
    n_g_right = both_right + g_right_v_wrong

    if n_g_wrong == 0 or n_g_right == 0:
        return {"cil": float("nan"), "p_v_given_g_wrong": float("nan"),
                "p_v_given_g_right": float("nan"), "n_g_wrong": 0, "n_g_right": 0}

    p_v_gw = v_right_g_wrong / n_g_wrong
    p_v_gr = both_right / n_g_right

    if p_v_gw == 0 or p_v_gr == 0:
        cil = float("nan")
    else:
        cil = np.log2(p_v_gw / p_v_gr)

    return {
        "cil": round(cil, 4) if not np.isnan(cil) else float("nan"),
        "p_v_correct_given_g_wrong": round(p_v_gw, 4),
        "p_v_correct_given_g_correct": round(p_v_gr, 4),
        "n_g_wrong": int(n_g_wrong),
        "n_g_right": int(n_g_right),
        "both_right": int(both_right),
        "v_right_g_wrong": int(v_right_g_wrong),
        "g_right_v_wrong": int(g_right_v_wrong),
        "both_wrong": int(both_wrong),
    }


def load_pw600_nli_per_question():
    """Load per-question DeBERTa + Mistral SC + SICA from direction_r_nli_pw600."""
    f = RESULTS / "direction_r_nli_pw600" / "results.json"
    data = json.load(open(f))
    pq = data.get("per_question", {})
    if not pq:
        print(f"  WARNING: no per_question in {f}")
    return pq


def load_folio204_per_question():
    """Load per-question data from direction_rg_combo."""
    f = RESULTS / "direction_rg_combo" / "per_question_best.json"
    return json.load(open(f))


def load_dir_j3_complementarity():
    """Load complementarity counts for 3 NLI verifiers × Mistral on PW-600."""
    f = RESULTS / "dir_j3_nli_multi_verifier" / "results.json"
    data = json.load(open(f))
    result = {}
    for model_data in data["models"]:
        name = model_data["model_name"]
        c = model_data["complementarity"]
        result[name] = {
            "both_right": c["both_right"],
            "v_right_g_wrong": c["nli_right_sc_wrong"],
            "g_right_v_wrong": c["sc_right_nli_wrong"],
            "both_wrong": c["both_wrong"],
        }
    return result


def load_generator_sc_from_intermediates(exp_dir):
    """Load per-question SC answers from experiment intermediates."""
    inter_dir = exp_dir / "intermediates"
    if not inter_dir.exists():
        return {}

    sc_data = {}
    for f in inter_dir.iterdir():
        if not f.name.endswith(".json"):
            continue
        try:
            d = json.load(open(f))
            qid = d["problem"]["id"]
            gold = d["problem"]["answer"]

            # Get SC majority vote
            sica_res = d.get("sica_result", {})
            counts = sica_res.get("answer_counts", {})
            if counts:
                sc_answer = max(counts, key=counts.get)
            else:
                continue

            sica_answer = sica_res.get("answer", None)

            sc_data[qid] = {
                "gold": gold,
                "sc_answer": sc_answer,
                "sc_correct": sc_answer == gold,
                "sica_answer": sica_answer,
                "sica_correct": sica_answer == gold if sica_answer else None,
            }
        except (KeyError, json.JSONDecodeError):
            continue

    return sc_data


def compute_pair_cil_from_per_question(generator_correct, verifier_correct):
    """Compute CIL from boolean arrays."""
    g = np.array(generator_correct, dtype=bool)
    v = np.array(verifier_correct, dtype=bool)

    both_right = int(np.sum(g & v))
    v_right_g_wrong = int(np.sum(~g & v))
    g_right_v_wrong = int(np.sum(g & ~v))
    both_wrong = int(np.sum(~g & ~v))

    return cil_from_counts(both_right, v_right_g_wrong, g_right_v_wrong, both_wrong)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    pairs = []

    # ============================================================
    # Section 1: Mistral × {DeBERTa, RoBERTa, BART} × PW-600
    # From dir_j3 complementarity counts
    # ============================================================
    print("=== Section 1: Mistral × NLI verifiers × PW-600 ===")
    j3_comp = load_dir_j3_complementarity()

    # Combo gains from nli_multi_verifier_recomputed.json
    recomp = json.load(open(RESULTS / "nli_multi_verifier_recomputed.json"))

    verifier_map = {
        "DeBERTa-MNLI": "DeBERTa-large-MNLI",
        "RoBERTa-MNLI": "RoBERTa-large-MNLI",
        "BART-MNLI": "BART-large-MNLI",
    }

    for j3_name, display_name in verifier_map.items():
        if j3_name not in j3_comp:
            print(f"  SKIP: {j3_name} not in dir_j3")
            continue

        c = j3_comp[j3_name]
        cil_data = cil_from_counts(c["both_right"], c["v_right_g_wrong"],
                                    c["g_right_v_wrong"], c["both_wrong"])

        combo_w3 = recomp["models"].get(j3_name, {}).get("combo", {}).get("w3", {}).get("delta_pp", None)

        pair = {
            "generator": "Mistral-7B",
            "verifier": display_name,
            "verifier_type": "NLI",
            "dataset": "PW-600",
            "n": 600,
            "combo_gain_w3": combo_w3,
            **cil_data,
        }
        pairs.append(pair)
        print(f"  {display_name}: CIL={cil_data['cil']}, combo_w3={combo_w3}")

    # ============================================================
    # Section 2: Multi-generator × DeBERTa × PW-600
    # Match DeBERTa per-question predictions with each generator's SC
    # ============================================================
    print("\n=== Section 2: Multi-generator × DeBERTa × PW-600 ===")
    pw600_pq = load_pw600_nli_per_question()

    if pw600_pq:
        # Build DeBERTa prediction map: qid -> deberta_correct
        deberta_map = {}
        for qid, qdata in pw600_pq.items():
            deberta_map[qid] = qdata["deberta_correct"]

        print(f"  Loaded {len(deberta_map)} DeBERTa predictions on PW-600")

        # BH table combo gains for multi-generator pairs
        bh_table = json.load(open(RESULTS / "nli_combo_full_table_bh" / "results.json"))

        # Try to match with Qwen2.5-14B (exp034)
        generators_on_server = {
            "Qwen2.5-14B": RESULTS / "exp034_qwen25_14b_proofwriter",
        }

        for gen_name, exp_dir in generators_on_server.items():
            print(f"  Loading {gen_name} from {exp_dir.name}...")
            gen_sc = load_generator_sc_from_intermediates(exp_dir)

            if not gen_sc:
                print(f"    SKIP: no per-question data")
                continue

            # Match question IDs with DeBERTa predictions
            matched_g_correct = []
            matched_v_correct = []
            matched_ids = []

            for qid in gen_sc:
                if qid in deberta_map:
                    matched_g_correct.append(gen_sc[qid]["sc_correct"])
                    matched_v_correct.append(deberta_map[qid])
                    matched_ids.append(qid)

            n_matched = len(matched_ids)
            print(f"    Matched {n_matched}/{len(gen_sc)} questions")

            if n_matched < 500:
                print(f"    SKIP: too few matches")
                continue

            cil_data = compute_pair_cil_from_per_question(matched_g_correct, matched_v_correct)

            # Try to get combo gain from BH table
            bh_gen = bh_table.get("generators", {}).get(gen_name, {})
            # Use local experiment's SC accuracy, not BH table
            local_sc = sum(1 for v in gen_sc.values() if v["sc_correct"]) / len(gen_sc)
            bh_combo_w3 = bh_gen.get("w3", {}).get("delta_pp", None)

            # Note: BH table used data from westd-16639, different experiment
            # For local experiment, we don't have the combo gain
            # We'll compute a proxy: the DeBERTa combo gain at w3 with THIS generator's SC
            pair = {
                "generator": gen_name,
                "verifier": "DeBERTa-large-MNLI",
                "verifier_type": "NLI",
                "dataset": f"PW-{n_matched}",
                "n": n_matched,
                "combo_gain_w3": bh_combo_w3,
                "note": f"local SC={local_sc:.4f}, BH table SC={bh_gen.get('sc_accuracy', 'N/A')}",
                **cil_data,
            }
            pairs.append(pair)
            print(f"    CIL={cil_data['cil']}")

            # Also compute SICA CIL for this generator
            matched_g_correct_sica = []
            matched_sica_correct = []
            for qid in matched_ids:
                if gen_sc[qid]["sica_correct"] is not None:
                    matched_g_correct_sica.append(gen_sc[qid]["sc_correct"])
                    matched_sica_correct.append(gen_sc[qid]["sica_correct"])

            if len(matched_g_correct_sica) > 400:
                cil_sica = compute_pair_cil_from_per_question(
                    matched_g_correct_sica, matched_sica_correct)
                sica_acc = sum(1 for v in gen_sc.values() if v.get("sica_correct")) / len(gen_sc)
                sica_gain = round((sica_acc - local_sc) * 100, 2)

                pair_sica = {
                    "generator": gen_name,
                    "verifier": "SICA",
                    "verifier_type": "SICA",
                    "dataset": f"PW-{len(matched_g_correct_sica)}",
                    "n": len(matched_g_correct_sica),
                    "combo_gain_w3": sica_gain,
                    "note": f"SICA gain = SICA_acc({sica_acc:.4f}) - SC_acc({local_sc:.4f})",
                    **cil_sica,
                }
                pairs.append(pair_sica)
                print(f"    {gen_name} SICA: CIL={cil_sica['cil']}")

    # For LLaMA-8B and Qwen3-14B: add from BH table complementarity if derivable
    # These are on westd-16639, so we note them as unavailable
    for gen_name in ["LLaMA-3.1-8B", "Qwen3-14B"]:
        bh_gen = bh_table.get("generators", {}).get(gen_name, {})
        if bh_gen:
            print(f"  {gen_name}: data on westd-16639, adding BH-derived entry")
            # We can derive the 2x2 table from McNemar discordant pairs + total
            # At w=1 (NLI gets 1 vote, SC gets 10 votes), combo ≈ SC unless NLI flips
            # This doesn't give us the raw complementarity. Skip with note.
            pairs.append({
                "generator": gen_name,
                "verifier": "DeBERTa-large-MNLI",
                "verifier_type": "NLI",
                "dataset": "PW-600",
                "n": 600,
                "combo_gain_w3": bh_gen.get("w3", {}).get("delta_pp", None),
                "cil": None,
                "note": "per-question data on westd-16639, CIL not computable from this server",
                "sc_accuracy": bh_gen.get("sc_accuracy", None),
            })

    # ============================================================
    # Section 3: Mistral × DeBERTa × FOLIO-204
    # ============================================================
    print("\n=== Section 3: Mistral × DeBERTa × FOLIO-204 ===")
    folio_pq = load_folio204_per_question()

    if folio_pq:
        g_correct = []
        v_correct = []
        sica_correct_list = []
        sc_correct_list = []

        for qid, qdata in folio_pq.items():
            sc_c = qdata["sc_correct"]
            deb_c = qdata["deberta_correct"]
            sica_c = qdata["sica_correct"]

            g_correct.append(sc_c)
            v_correct.append(deb_c)
            sica_correct_list.append(sica_c)
            sc_correct_list.append(sc_c)

        # Mistral × DeBERTa × FOLIO-204
        cil_folio_deb = compute_pair_cil_from_per_question(g_correct, v_correct)

        # Get combo gain from direction_rg_combo
        rg_combo = json.load(open(RESULTS / "direction_rg_combo" / "results.json"))
        combo_w3_folio = None
        for strat_name, strat_data in rg_combo.get("strategies", {}).items():
            if "nli_sc_vote_w3" in strat_name:
                combo_w3_folio = round(strat_data.get("delta_vs_sc", 0) * 100, 2)
                break
        # Try nli_sc_vote strategies
        if combo_w3_folio is None:
            for strat_name, strat_data in rg_combo.get("strategies", {}).items():
                if "w3" in strat_name and "nli" in strat_name:
                    combo_w3_folio = round(strat_data.get("delta_vs_sc", 0) * 100, 2)
                    break

        pair_folio = {
            "generator": "Mistral-7B",
            "verifier": "DeBERTa-large-MNLI",
            "verifier_type": "NLI",
            "dataset": "FOLIO-204",
            "n": len(g_correct),
            "combo_gain_w3": combo_w3_folio,
            **cil_folio_deb,
        }
        pairs.append(pair_folio)
        print(f"  DeBERTa: CIL={cil_folio_deb['cil']}")

        # Mistral × SICA × FOLIO-204
        cil_folio_sica = compute_pair_cil_from_per_question(sc_correct_list, sica_correct_list)
        sc_acc = sum(sc_correct_list) / len(sc_correct_list)
        sica_acc = sum(sica_correct_list) / len(sica_correct_list)
        sica_gain = round((sica_acc - sc_acc) * 100, 2)

        pair_folio_sica = {
            "generator": "Mistral-7B",
            "verifier": "SICA",
            "verifier_type": "SICA",
            "dataset": "FOLIO-204",
            "n": len(sc_correct_list),
            "combo_gain_w3": sica_gain,
            "note": f"SICA gain = SICA_acc({sica_acc:.4f}) - SC_acc({sc_acc:.4f})",
            **cil_folio_sica,
        }
        pairs.append(pair_folio_sica)
        print(f"  SICA: CIL={cil_folio_sica['cil']}")

    # ============================================================
    # Section 4: Mistral × SICA × PW-600
    # ============================================================
    print("\n=== Section 4: Mistral × SICA × PW-600 ===")
    if pw600_pq:
        sc_c = [qdata["sc_correct"] for qdata in pw600_pq.values()]
        sica_c = [qdata["sica_correct"] for qdata in pw600_pq.values()]

        cil_pw_sica = compute_pair_cil_from_per_question(sc_c, sica_c)
        sc_acc_pw = sum(sc_c) / len(sc_c)
        sica_acc_pw = sum(sica_c) / len(sica_c)
        sica_gain_pw = round((sica_acc_pw - sc_acc_pw) * 100, 2)

        pair_pw_sica = {
            "generator": "Mistral-7B",
            "verifier": "SICA",
            "verifier_type": "SICA",
            "dataset": "PW-600",
            "n": len(sc_c),
            "combo_gain_w3": sica_gain_pw,
            "note": f"SICA gain = SICA_acc({sica_acc_pw:.4f}) - SC_acc({sc_acc_pw:.4f})",
            **cil_pw_sica,
        }
        pairs.append(pair_pw_sica)
        print(f"  Mistral SICA: CIL={cil_pw_sica['cil']}")

    # ============================================================
    # Section 5: Correlation analysis
    # ============================================================
    print("\n=== Correlation Analysis ===")
    valid_pairs = [p for p in pairs if p.get("cil") is not None
                   and not (isinstance(p["cil"], float) and np.isnan(p["cil"]))
                   and p.get("combo_gain_w3") is not None]

    correlation = {}
    if len(valid_pairs) >= 4:
        cils = [p["cil"] for p in valid_pairs]
        gains = [p["combo_gain_w3"] for p in valid_pairs]

        sp = stats.spearmanr(cils, gains)
        pr = stats.pearsonr(cils, gains)

        correlation = {
            "n_pairs": len(valid_pairs),
            "spearman_cil_vs_gain": {"rho": round(sp.statistic, 4), "p": round(sp.pvalue, 4)},
            "pearson_cil_vs_gain": {"r": round(pr.statistic, 4), "p": round(pr.pvalue, 4)},
        }
        print(f"  n={len(valid_pairs)}, Spearman rho={sp.statistic:.4f} (p={sp.pvalue:.4f})")
        print(f"  Pearson r={pr.statistic:.4f} (p={pr.pvalue:.4f})")
    else:
        print(f"  Only {len(valid_pairs)} valid pairs, need >= 4 for correlation")
        correlation = {"n_pairs": len(valid_pairs), "note": "insufficient data"}

    # ============================================================
    # Output
    # ============================================================
    output = {
        "experiment": "exp_d134_cil",
        "description": "CIL (Cumulative Information Lift) computation",
        "formula": "CIL(V,G) = log2[P(V correct | G wrong) / P(V correct | G correct)]",
        "pairs": pairs,
        "correlation": correlation,
    }

    out_file = OUT_DIR / "cil_results.json"
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved to {out_file}")

    # ============================================================
    # Scatter plot
    # ============================================================
    if len(valid_pairs) >= 3:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots(1, 1, figsize=(8, 6))

            nli_pairs = [p for p in valid_pairs if p["verifier_type"] == "NLI"]
            sica_pairs = [p for p in valid_pairs if p["verifier_type"] == "SICA"]

            if nli_pairs:
                x_nli = [p["cil"] for p in nli_pairs]
                y_nli = [p["combo_gain_w3"] for p in nli_pairs]
                ax.scatter(x_nli, y_nli, c="tab:blue", s=80, zorder=5, label="NLI verifier")
                for p, xi, yi in zip(nli_pairs, x_nli, y_nli):
                    label = f"{p['generator'][:3]}×{p['verifier'].split('-')[0]}\n{p['dataset']}"
                    ax.annotate(label, (xi, yi), fontsize=7,
                               textcoords="offset points", xytext=(6, 4))

            if sica_pairs:
                x_sica = [p["cil"] for p in sica_pairs]
                y_sica = [p["combo_gain_w3"] for p in sica_pairs]
                ax.scatter(x_sica, y_sica, c="tab:orange", s=80, marker="s", zorder=5, label="SICA")
                for p, xi, yi in zip(sica_pairs, x_sica, y_sica):
                    label = f"{p['generator'][:3]}×SICA\n{p['dataset']}"
                    ax.annotate(label, (xi, yi), fontsize=7,
                               textcoords="offset points", xytext=(6, 4))

            ax.axvline(x=0, color="gray", linestyle="--", alpha=0.5)
            ax.axhline(y=0, color="gray", linestyle="--", alpha=0.5)
            ax.set_xlabel("CIL (bits)", fontsize=12)
            ax.set_ylabel("Combo Gain (pp)", fontsize=12)
            ax.set_title("CIL vs. Combo Gain", fontsize=14)
            ax.legend(fontsize=10)

            if correlation.get("spearman_cil_vs_gain"):
                sp_info = correlation["spearman_cil_vs_gain"]
                ax.text(0.02, 0.98, f"Spearman ρ={sp_info['rho']:.3f} (p={sp_info['p']:.3f})",
                       transform=ax.transAxes, fontsize=9, va="top",
                       bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.5))

            plt.tight_layout()
            fig_path = OUT_DIR / "cil_vs_gain_scatter.png"
            fig.savefig(fig_path, dpi=150, bbox_inches="tight")
            print(f"Saved scatter plot to {fig_path}")
            plt.close()
        except ImportError as e:
            print(f"Could not create plot: {e}")

    # Print summary table
    print("\n" + "="*90)
    print(f"{'Generator':<16} {'Verifier':<20} {'Dataset':<12} {'CIL':>8} {'Gain_w3':>8} {'P(V|Gw)':>8} {'P(V|Gr)':>8}")
    print("-"*90)
    for p in pairs:
        cil_val = p.get("cil")
        cil_str = f"{cil_val:.4f}" if cil_val is not None and not (isinstance(cil_val, float) and np.isnan(cil_val)) else "N/A"
        gain_str = f"{p['combo_gain_w3']:.2f}" if p.get("combo_gain_w3") is not None else "N/A"
        pvgw = p.get("p_v_correct_given_g_wrong")
        pvgr = p.get("p_v_correct_given_g_correct")
        pvgw_str = f"{pvgw:.4f}" if pvgw is not None else "N/A"
        pvgr_str = f"{pvgr:.4f}" if pvgr is not None else "N/A"
        print(f"{p['generator']:<16} {p['verifier']:<20} {p['dataset']:<12} {cil_str:>8} {gain_str:>8} {pvgw_str:>8} {pvgr_str:>8}")
    print("="*90)

    return output


if __name__ == "__main__":
    main()
