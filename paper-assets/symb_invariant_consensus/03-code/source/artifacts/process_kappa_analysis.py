import json
import os
import glob
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from itertools import combinations

MODELS = {
    "Mistral-7B": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates",
    "Qwen2.5-14B": "/root/symb_invariant_consensus/results/folio_204_14b/intermediates",
    "Qwen3-14B": "/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204/intermediates",
}

def load_traces(intermediates_dir):
    data = {}
    for fpath in sorted(glob.glob(os.path.join(intermediates_dir, "folio_*.json"))):
        pid = os.path.basename(fpath).replace(".json", "")
        with open(fpath) as f:
            d = json.load(f)
        traces_list = d["sica_result"]["traces"]
        texts = [t["trace"] for t in traces_list]
        answers = [t["answer"] for t in traces_list]
        if len(texts) >= 2:
            data[pid] = {"texts": texts, "answers": answers}
    return data

def compute_process_sim(texts):
    if len(texts) < 2:
        return np.nan
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=5000)
    tfidf = vectorizer.fit_transform(texts)
    sim_matrix = cosine_similarity(tfidf)
    n = len(texts)
    pairs = []
    for i, j in combinations(range(n), 2):
        pairs.append(sim_matrix[i, j])
    return np.mean(pairs)

def fleiss_kappa(answers_list):
    categories = sorted(set(a for answers in answers_list for a in answers))
    cat_idx = {c: i for i, c in enumerate(categories)}
    n_subjects = len(answers_list)
    n_raters = len(answers_list[0])
    k = len(categories)

    table = np.zeros((n_subjects, k))
    for i, answers in enumerate(answers_list):
        for a in answers:
            table[i, cat_idx[a]] += 1

    n = table.sum(axis=1)[0]
    p_j = table.sum(axis=0) / (n_subjects * n)
    P_i = (table ** 2).sum(axis=1)
    P_i = (P_i - n) / (n * (n - 1))
    P_bar = P_i.mean()
    P_e = (p_j ** 2).sum()

    if P_e == 1.0:
        return 1.0
    kappa = (P_bar - P_e) / (1.0 - P_e)
    return kappa

def main():
    results = {}
    all_problem_ids = None

    for model_name, idir in MODELS.items():
        data = load_traces(idir)
        pids = set(data.keys())
        if all_problem_ids is None:
            all_problem_ids = pids
        else:
            all_problem_ids = all_problem_ids & pids

    print(f"Common problems across all 3 models: {len(all_problem_ids)}")
    common_pids = sorted(all_problem_ids)

    for model_name, idir in MODELS.items():
        data = load_traces(idir)

        all_pids = sorted(data.keys())
        process_sims_all = []
        for pid in all_pids:
            ps = compute_process_sim(data[pid]["texts"])
            process_sims_all.append(ps)

        all_answers = [data[pid]["answers"] for pid in all_pids]
        kappa_all = fleiss_kappa(all_answers)

        process_sims_common = []
        for pid in common_pids:
            ps = compute_process_sim(data[pid]["texts"])
            process_sims_common.append(ps)

        common_answers = [data[pid]["answers"] for pid in common_pids]
        kappa_common = fleiss_kappa(common_answers)

        ps_all = np.array(process_sims_all)
        ps_common = np.array(process_sims_common)

        results[model_name] = {
            "n_problems_all": len(all_pids),
            "process_sim_all_mean": float(np.nanmean(ps_all)),
            "process_sim_all_std": float(np.nanstd(ps_all)),
            "kappa_all": float(kappa_all),
            "gap_all": float(np.nanmean(ps_all) - kappa_all),
            "n_problems_common": len(common_pids),
            "process_sim_common_mean": float(np.nanmean(ps_common)),
            "process_sim_common_std": float(np.nanstd(ps_common)),
            "kappa_common": float(kappa_common),
            "gap_common": float(np.nanmean(ps_common) - kappa_common),
        }

    print("\n=== Full dataset per model ===")
    print(f"{'Model':<16} {'N':>4} {'ProcessSim':>18} {'κ':>8} {'Gap':>8}")
    print("-" * 60)
    for m in ["Mistral-7B", "Qwen2.5-14B", "Qwen3-14B"]:
        r = results[m]
        print(f"{m:<16} {r['n_problems_all']:>4} {r['process_sim_all_mean']:.4f}±{r['process_sim_all_std']:.4f} {r['kappa_all']:>8.4f} {r['gap_all']:>8.4f}")

    print(f"\n=== Common subset (N={len(common_pids)}) ===")
    print(f"{'Model':<16} {'ProcessSim':>18} {'κ':>8} {'Gap':>8}")
    print("-" * 56)
    for m in ["Mistral-7B", "Qwen2.5-14B", "Qwen3-14B"]:
        r = results[m]
        print(f"{m:<16} {r['process_sim_common_mean']:.4f}±{r['process_sim_common_std']:.4f} {r['kappa_common']:>8.4f} {r['gap_common']:>8.4f}")

    out_dir = "/root/symb_invariant_consensus/results/process_kappa_cross_model"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_dir}/results.json")

if __name__ == "__main__":
    main()
