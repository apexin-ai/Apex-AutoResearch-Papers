#!/usr/bin/env python3
"""R11 Q3: 3-verifier canonical analysis.
Hard-vote combo + alphabetical tiebreaking.
DeBERTa from D116. RoBERTa/BART inferred here. SC from mistral_pw600_sc_votes.json (ID-fixed).
"""
import json, time, torch
from collections import Counter
from scipy.stats import binomtest
from transformers import AutoTokenizer, AutoModelForSequenceClassification

PW_PATH = "/root/symb_invariant_consensus/data/proofwriter_full.json"
SC_PATH = "/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json"
D116_PATH = "/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]

ID_FIX = {
    "ProofWriter_AttNeg-OWA-D5-1176_Q4": "ProofWriter_AttNeg-OWA-D5-1176_Q8",
    "ProofWriter_AttNoneg-OWA-D5-1284_Q4": "ProofWriter_AttNoneg-OWA-D5-1284_Q8",
}

NLI_MODELS = {
    "roberta": "/root/autodl-tmp/models/roberta-large-mnli",
    "bart": "/root/autodl-tmp/models/bart-large-mnli",
}

def parse_problem(text):
    marker = "\n\nDetermine whether the following statement is true, false, or unknown:\n"
    if marker in text:
        parts = text.split(marker, 1)
        return parts[0].strip(), parts[1].strip()
    return text, ""

def map_nli(label):
    lu = label.upper()
    if "ENTAIL" in lu: return "True"
    if "CONTRA" in lu: return "False"
    return "Unknown"

def alpha_winner(score_dict):
    mx = max(score_dict.values())
    tied = sorted(c for c in CLASSES if score_dict.get(c, 0) == mx)
    return tied[0]

def run_nli_inference(model_name, hf_path, pw_data, device):
    print(f"\nLoading {model_name}: {hf_path}")
    tok = AutoTokenizer.from_pretrained(hf_path)
    mdl = AutoModelForSequenceClassification.from_pretrained(hf_path).to(device).eval()
    id2label = mdl.config.id2label
    nli_map = {idx: map_nli(lbl) for idx, lbl in id2label.items()}
    print(f"  id2label: {id2label}, nli_map: {nli_map}")

    preds = {}
    t0 = time.time()
    for i, q in enumerate(pw_data):
        qid = q["id"]
        premises, conclusion = parse_problem(q["problem"])
        if not conclusion:
            preds[qid] = "Unknown"
            continue
        inp = tok(premises, conclusion, return_tensors="pt", truncation=True, max_length=512).to(device)
        with torch.no_grad():
            logits = mdl(**inp).logits
        pred_idx = logits.argmax(dim=-1).item()
        preds[qid] = nli_map[pred_idx]
        if (i+1) % 100 == 0:
            print(f"  {i+1}/{len(pw_data)} ({time.time()-t0:.0f}s)")
    
    print(f"  Done: {time.time()-t0:.1f}s")
    del mdl
    torch.cuda.empty_cache()
    return preds

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    with open(PW_PATH) as f: pw_data = json.load(f)
    with open(SC_PATH) as f: sc_raw = json.load(f)
    with open(D116_PATH) as f: d116 = json.load(f)

    gt = {q["id"]: q["answer"] for q in pw_data}
    sc_votes = {ID_FIX.get(k, k): v for k, v in sc_raw.items()}
    per_q = d116["per_question"]
    N = len(gt)
    assert len(set(gt.keys()) & set(sc_votes.keys())) == 600, "ID mismatch"

    # SC baseline
    sc_answers = {}
    for qid in gt:
        v = sc_votes[qid]
        vd = dict(zip(CLASSES, v))
        sc_answers[qid] = alpha_winner(vd)
    sc_n = sum(1 for qid in gt if sc_answers[qid] == gt[qid])
    print(f"SC baseline: {sc_n}/{N} = {sc_n/N*100:.2f}%")
    assert sc_n == 236, f"SC baseline mismatch: {sc_n} != 236"

    # DeBERTa predictions from D116
    deberta_preds = {qid: per_q[qid]["deberta_pred"] for qid in gt}
    deb_n = sum(1 for qid in gt if deberta_preds[qid] == gt[qid])
    print(f"DeBERTa standalone: {deb_n}/{N} = {deb_n/N*100:.2f}%")
    assert deb_n == 330, f"DeBERTa standalone mismatch: {deb_n} != 330"

    # Run RoBERTa and BART
    all_preds = {"deberta": deberta_preds}
    for name, path in NLI_MODELS.items():
        preds = run_nli_inference(name, path, pw_data, device)
        n_correct = sum(1 for qid in gt if preds[qid] == gt[qid])
        print(f"  {name} standalone: {n_correct}/{N} = {n_correct/N*100:.2f}%")
        all_preds[name] = preds

    # Individual combos
    print("\n=== Individual Combos ===")
    individual_results = {}
    for vname, vpreds in all_preds.items():
        standalone_n = sum(1 for qid in gt if vpreds[qid] == gt[qid])
        vr = {"standalone_acc": round(standalone_n/N*100, 2), "standalone_correct": standalone_n}
        combos = {}
        for w in WEIGHTS:
            combo_correct = 0; b = 0; c = 0
            for qid in gt:
                gold = gt[qid]
                v = sc_votes[qid]
                combined = dict(zip(CLASSES, list(v)))
                dp = vpreds[qid]
                if dp in CLASSES:
                    combined[dp] = combined.get(dp, 0) + w
                combo_ans = alpha_winner(combined)
                sc_ok = (sc_answers[qid] == gold)
                combo_ok = (combo_ans == gold)
                if combo_ok: combo_correct += 1
                if sc_ok and not combo_ok: b += 1
                if not sc_ok and combo_ok: c += 1
            n_disc = b + c
            p_val = binomtest(min(b, c), n_disc, 0.5).pvalue if n_disc > 0 else 1.0
            combos[f"w{w}"] = {
                "acc": round(combo_correct/N*100, 2),
                "correct": combo_correct,
                "delta_pp": round((combo_correct - sc_n)/N*100, 2),
                "mcnemar_b": b, "mcnemar_c": c,
                "mcnemar_p": p_val,
            }
            print(f"  {vname} w={w}: {combo_correct}/{N} = {combo_correct/N*100:.2f}%, "
                  f"delta=+{(combo_correct-sc_n)/N*100:.2f}pp, b={b}, c={c}, p={p_val:.6f}")
        vr["combos"] = combos
        individual_results[vname] = vr

    # Verify DeBERTa canonical
    assert individual_results["deberta"]["combos"]["w3"]["correct"] == 276, \
        f"DeBERTa w3 mismatch: {individual_results['deberta']['combos']['w3']['correct']}"

    # 3-verifier ensemble: majority vote of 3 NLI predictions, then hard-vote combo
    print("\n=== 3-Verifier Ensemble ===")
    ensemble_preds = {}
    for qid in gt:
        votes = Counter()
        for vname in ["deberta", "roberta", "bart"]:
            votes[all_preds[vname][qid]] += 1
        ensemble_preds[qid] = alpha_winner(dict(votes))
    
    ens_standalone = sum(1 for qid in gt if ensemble_preds[qid] == gt[qid])
    print(f"Ensemble standalone: {ens_standalone}/{N} = {ens_standalone/N*100:.2f}%")
    
    ensemble_combos = {}
    for w in WEIGHTS:
        combo_correct = 0; b = 0; c = 0
        for qid in gt:
            gold = gt[qid]
            v = sc_votes[qid]
            combined = dict(zip(CLASSES, list(v)))
            ep = ensemble_preds[qid]
            if ep in CLASSES:
                combined[ep] = combined.get(ep, 0) + w
            combo_ans = alpha_winner(combined)
            sc_ok = (sc_answers[qid] == gold)
            combo_ok = (combo_ans == gold)
            if combo_ok: combo_correct += 1
            if sc_ok and not combo_ok: b += 1
            if not sc_ok and combo_ok: c += 1
        n_disc = b + c
        p_val = binomtest(min(b, c), n_disc, 0.5).pvalue if n_disc > 0 else 1.0
        ensemble_combos[f"w{w}"] = {
            "acc": round(combo_correct/N*100, 2),
            "correct": combo_correct,
            "delta_pp": round((combo_correct - sc_n)/N*100, 2),
            "mcnemar_b": b, "mcnemar_c": c,
            "mcnemar_p": p_val,
        }
        print(f"  ensemble w={w}: {combo_correct}/{N} = {combo_correct/N*100:.2f}%, "
              f"delta=+{(combo_correct-sc_n)/N*100:.2f}pp, b={b}, c={c}, p={p_val:.6f}")

    # Also: 3-verifier additive combo (each verifier adds w votes)
    print("\n=== 3-Verifier Additive (each adds w) ===")
    additive_combos = {}
    for w in WEIGHTS:
        combo_correct = 0; b = 0; c = 0
        for qid in gt:
            gold = gt[qid]
            v = sc_votes[qid]
            combined = dict(zip(CLASSES, list(v)))
            for vname in ["deberta", "roberta", "bart"]:
                dp = all_preds[vname][qid]
                if dp in CLASSES:
                    combined[dp] = combined.get(dp, 0) + w
            combo_ans = alpha_winner(combined)
            sc_ok = (sc_answers[qid] == gold)
            combo_ok = (combo_ans == gold)
            if combo_ok: combo_correct += 1
            if sc_ok and not combo_ok: b += 1
            if not sc_ok and combo_ok: c += 1
        n_disc = b + c
        p_val = binomtest(min(b, c), n_disc, 0.5).pvalue if n_disc > 0 else 1.0
        additive_combos[f"w{w}"] = {
            "acc": round(combo_correct/N*100, 2),
            "correct": combo_correct,
            "delta_pp": round((combo_correct - sc_n)/N*100, 2),
            "mcnemar_b": b, "mcnemar_c": c,
            "mcnemar_p": p_val,
        }
        print(f"  additive w={w}: {combo_correct}/{N} = {combo_correct/N*100:.2f}%, "
              f"delta=+{(combo_correct-sc_n)/N*100:.2f}pp, b={b}, c={c}, p={p_val:.6f}")

    # BH correction: collect all McNemar p-values
    print("\n=== BH Correction ===")
    all_tests = []
    for vname in ["deberta", "roberta", "bart"]:
        for w in WEIGHTS:
            key = f"{vname}_w{w}"
            p = individual_results[vname]["combos"][f"w{w}"]["mcnemar_p"]
            all_tests.append((key, p))
    for w in WEIGHTS:
        all_tests.append((f"ensemble_w{w}", ensemble_combos[f"w{w}"]["mcnemar_p"]))
    for w in WEIGHTS:
        all_tests.append((f"additive_w{w}", additive_combos[f"w{w}"]["mcnemar_p"]))

    m = len(all_tests)
    sorted_tests = sorted(enumerate(all_tests), key=lambda x: x[1][1])
    adjusted = [0.0] * m
    for rank_idx, (orig_idx, (label, p)) in enumerate(sorted_tests):
        rank = rank_idx + 1
        adj = min(p * m / rank, 1.0)
        adjusted[orig_idx] = adj
    # Step-up: ensure monotonicity
    for rank_idx in range(len(sorted_tests) - 2, -1, -1):
        orig_idx = sorted_tests[rank_idx][0]
        next_orig_idx = sorted_tests[rank_idx + 1][0]
        adjusted[orig_idx] = min(adjusted[orig_idx], adjusted[next_orig_idx])

    bh_results = []
    for i, (label, raw_p) in enumerate(all_tests):
        sig = adjusted[i] < 0.05
        bh_results.append({"label": label, "raw_p": raw_p, "bh_adjusted_p": adjusted[i], "significant": sig})
        star = "*" if sig else ""
        print(f"  {label}: raw={raw_p:.6f}, adj={adjusted[i]:.6f} {star}")
    
    n_sig = sum(1 for r in bh_results if r["significant"])
    print(f"\n  {n_sig}/{m} significant after BH correction (alpha=0.05)")

    # Agreement analysis
    print("\n=== Inter-verifier Agreement ===")
    agree_all = sum(1 for qid in gt if all_preds["deberta"][qid] == all_preds["roberta"][qid] == all_preds["bart"][qid])
    agree_db_rb = sum(1 for qid in gt if all_preds["deberta"][qid] == all_preds["roberta"][qid])
    agree_db_bt = sum(1 for qid in gt if all_preds["deberta"][qid] == all_preds["bart"][qid])
    agree_rb_bt = sum(1 for qid in gt if all_preds["roberta"][qid] == all_preds["bart"][qid])
    print(f"  All 3 agree: {agree_all}/{N} = {agree_all/N*100:.1f}%")
    print(f"  DeBERTa-RoBERTa: {agree_db_rb}/{N} = {agree_db_rb/N*100:.1f}%")
    print(f"  DeBERTa-BART: {agree_db_bt}/{N} = {agree_db_bt/N*100:.1f}%")
    print(f"  RoBERTa-BART: {agree_rb_bt}/{N} = {agree_rb_bt/N*100:.1f}%")

    # Build output
    output = {
        "experiment": "r11_3verifier_canonical",
        "dataset": "ProofWriter-D5-OWA",
        "n": N,
        "sc_baseline": {"acc": round(sc_n/N*100, 2), "correct": sc_n},
        "combo_method": "hard-vote (add w to NLI predicted class) + alphabetical tiebreaking",
        "individual_verifiers": individual_results,
        "ensemble_majority": {
            "method": "majority vote of 3 NLI predictions (alpha tiebreak), then hard-vote combo with SC",
            "standalone_acc": round(ens_standalone/N*100, 2),
            "standalone_correct": ens_standalone,
            "combos": ensemble_combos,
        },
        "additive_3verifier": {
            "method": "each of 3 verifiers adds w votes to their predicted class",
            "combos": additive_combos,
        },
        "bh_correction": {
            "n_tests": m,
            "alpha": 0.05,
            "n_significant": n_sig,
            "tests": bh_results,
        },
        "agreement": {
            "all_3": agree_all,
            "deberta_roberta": agree_db_rb,
            "deberta_bart": agree_db_bt,
            "roberta_bart": agree_rb_bt,
        },
        "per_question_preds": {
            qid: {
                "gold": gt[qid],
                "sc_answer": sc_answers[qid],
                "deberta": all_preds["deberta"][qid],
                "roberta": all_preds["roberta"][qid],
                "bart": all_preds["bart"][qid],
                "ensemble": ensemble_preds[qid],
            }
            for qid in gt
        },
    }

    out_path = "/root/symb_invariant_consensus/results/r11_3verifier_canonical.json"
    with open(out_path, "w") as f:
        class NE(json.JSONEncoder):
            def default(self, o):
                if isinstance(o, bool): return bool(o)
                try:
                    import numpy as np
                    if isinstance(o, np.bool_): return bool(o)
                    if isinstance(o, np.integer): return int(o)
                    if isinstance(o, np.floating): return float(o)
                except: pass
                return super().default(o)
        json.dump(output, f, indent=2, cls=NE)
    print(f"\nSaved: {out_path}")

if __name__ == "__main__":
    main()
