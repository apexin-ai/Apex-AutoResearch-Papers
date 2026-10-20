import json
import numpy as np
import sys

def extract_surface_keys(sample, subtask):
    if subtask == "ner":
        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
    elif subtask == "re":
        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
    else:
        raise ValueError(f"Unknown subtask: {subtask}")

def fleiss_kappa_decomposed(samples, subtask="ner"):
    """Returns (P_o, P_e, excess, kappa) for one instance."""
    n_raters = len(samples)
    if n_raters <= 1:
        return (1.0, 0.0, 1.0, 1.0)

    entity_sets = []
    all_keys = set()
    for sample in samples:
        keys = extract_surface_keys(sample, subtask)
        entity_sets.append(keys)
        all_keys |= keys

    n_subjects = len(all_keys)
    if n_subjects <= 0:
        return (1.0, 0.0, 1.0, 1.0)

    key_list = sorted(all_keys)
    rating = np.zeros((n_subjects, 2), dtype=np.int64)
    for es in entity_sets:
        for idx, key in enumerate(key_list):
            if key in es:
                rating[idx, 1] += 1
            else:
                rating[idx, 0] += 1

    n = n_raters
    if np.all(np.max(rating, axis=1) == n):
        return (1.0, 0.0, 1.0, 1.0)

    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = float(np.mean(P_i))  # P_o

    p_j = np.sum(rating, axis=0) / (n_subjects * n)
    P_e = float(np.sum(p_j ** 2))

    excess = P_bar - P_e

    if abs(1.0 - P_e) < 1e-12:
        return (P_bar, P_e, excess, 1.0)

    kappa = excess / (1.0 - P_e)
    return (P_bar, P_e, excess, kappa)

configs = [
    {
        "name": "Qwen SciERC NER",
        "path": "output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
        "subtask": "ner",
        "n": 8,
    },
    {
        "name": "Qwen SciERC RE",
        "path": "output/exp_012_rerun_1024/samples_with_logprobs.jsonl",
        "subtask": "re",
        "n": 8,
    },
    {
        "name": "Qwen CoNLL NER",
        "path": "output/exp_002_conll_n16/samples.jsonl",
        "subtask": "ner",
        "n": 8,
        "take_first_n": 8,
    },
    {
        "name": "Qwen CoNLL NER N=16",
        "path": "output/exp_002_conll_n16/samples.jsonl",
        "subtask": "ner",
        "n": 16,
    },
    {
        "name": "LLaMA SciERC NER",
        "path": "output/exp007_llama_inference/samples.jsonl",
        "subtask": "ner",
        "n": 8,
    },
    {
        "name": "LLaMA SciERC RE",
        "path": "output/exp007_llama_inference/samples.jsonl",
        "subtask": "re",
        "n": 8,
    },
    {
        "name": "LLaMA CoNLL NER",
        "path": "output/exp_017_llama_conll_infer/samples.jsonl",
        "subtask": "ner",
        "n": 8,
    },
    {
        "name": "LLaMA CoNLL NER N=16",
        "path": "output/exp_017_llama_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
        "n": 16,
    },
]

base = "/root/autodl-tmp/struct_self_consist_ie"
results = []

for cfg in configs:
    filepath = f"{base}/{cfg['path']}"
    try:
        with open(filepath) as f:
            instances = [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        results.append({**cfg, "status": "FILE_NOT_FOUND"})
        continue

    po_list, pe_list, excess_list, fk_list = [], [], [], []
    for inst in instances:
        samples = inst["samples"]
        n_expected = cfg.get("take_first_n", cfg["n"])
        if len(samples) < n_expected:
            continue
        samples = samples[:n_expected]

        P_o, P_e, excess, kappa = fleiss_kappa_decomposed(samples, cfg["subtask"])
        po_list.append(P_o)
        pe_list.append(P_e)
        excess_list.append(excess)
        fk_list.append(kappa)

    if not fk_list:
        results.append({**cfg, "status": "NO_VALID_INSTANCES"})
        continue

    fk_arr = np.array(fk_list)
    results.append({
        "name": cfg["name"],
        "subtask": cfg["subtask"],
        "n": cfg.get("take_first_n", cfg["n"]),
        "n_instances": len(fk_list),
        "mean_po": float(np.mean(po_list)),
        "mean_pe": float(np.mean(pe_list)),
        "mean_excess": float(np.mean(excess_list)),
        "mean_fk": float(np.mean(fk_list)),
        "fk_p5": float(np.percentile(fk_arr, 5)),
        "fk_p95": float(np.percentile(fk_arr, 95)),
        "std_po": float(np.std(po_list)),
        "std_pe": float(np.std(pe_list)),
        "std_excess": float(np.std(excess_list)),
        "std_fk": float(np.std(fk_list)),
        "status": "OK",
    })

print(json.dumps(results, indent=2))
