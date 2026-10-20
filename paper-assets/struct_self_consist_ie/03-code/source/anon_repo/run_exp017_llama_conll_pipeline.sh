#!/bin/bash
set -e
export PATH="/root/miniconda3/bin:$PATH"
cd /root/autodl-tmp/struct_self_consist_ie

echo "$(date) === Step 1: Merge LoRA adapter ==="
python3 -c "
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os

base_path = '/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct'
adapter_path = 'checkpoints/llama3.1-8b-conll2003-lora-3ep'
merged_path = 'checkpoints/llama3.1-8b-conll2003-merged'

if os.path.exists(merged_path + '/config.json'):
    print('Merged model already exists, skip merge')
else:
    print('Loading base model...')
    base = AutoModelForCausalLM.from_pretrained(base_path, dtype=torch.bfloat16, device_map='cpu')
    print('Loading adapter...')
    model = PeftModel.from_pretrained(base, adapter_path)
    print('Merging...')
    model = model.merge_and_unload()
    print('Saving merged model...')
    model.save_pretrained(merged_path)
    tokenizer = AutoTokenizer.from_pretrained(base_path)
    tokenizer.save_pretrained(merged_path)
    print('Merge complete')
"

echo "$(date) === Step 2: N=8 inference ==="
mkdir -p output/exp_017_llama_conll
CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py \
    --model_path checkpoints/llama3.1-8b-conll2003-merged \
    --data_dir data/conll2003 \
    --dataset conll2003 \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --max_tokens 1024 \
    --seed 42 \
    --output_dir output/exp_017_llama_conll \
    --collect_logprobs

echo "$(date) === Step 3: Verify output ==="
LINES=$(wc -l < output/exp_017_llama_conll/samples.jsonl)
echo "samples.jsonl lines: $LINES"

echo "$(date) === Step 4: 5-signal analysis ==="
python3 -c "
import json, os, sys
import numpy as np
from collections import Counter
from scipy.stats import spearmanr, kendalltau, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = 'output/exp_017_llama_conll/samples.jsonl'
OUTPUT_PATH = 'output/exp_017_llama_conll/report.json'
SUBTASK = 'ner'

def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records

def compute_exact_match_rate(samples, subtask):
    if subtask == 'ner':
        keys = [frozenset((e['text'], e['type']) for e in s.get('entities', [])) for s in samples]
    else:
        keys = [frozenset((r['head'], r['tail'], r['type']) for r in s.get('relations', [])) for s in samples]
    if not keys:
        return 0.0
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(samples)

def compute_voting_confidence(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
    counter = Counter()
    if subtask == 'ner':
        for s in samples:
            for e in s.get('entities', []):
                counter[(e['text'], e['type'])] += 1
    else:
        for s in samples:
            for r in s.get('relations', []):
                counter[(r['head'], r['tail'], r['type'])] += 1
    if not counter:
        return 0.0
    rates = [v / N for v in counter.values()]
    return float(np.mean(rates))

def compute_mean_logprob(samples):
    logprobs = [s.get('mean_logprob') for s in samples if s.get('mean_logprob') is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    if not logprobs:
        return float('nan')
    return float(np.mean(logprobs))

def safe_auroc(scores, labels):
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)
    if len(np.unique(labels)) < 2:
        return float('nan')
    n_pos = np.sum(labels == 1)
    n_neg = np.sum(labels == 0)
    if n_pos == 0 or n_neg == 0:
        return float('nan')
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))

def safe_spearman(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float('nan')
    return float(spearmanr(x, y).statistic)

def safe_kendall(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return float('nan')
    return float(kendalltau(x, y).statistic)

def bootstrap_metric(metric_fn, signals, targets, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    signals = np.asarray(signals, dtype=float)
    targets = np.asarray(targets, dtype=float)
    n = len(signals)
    boot_vals = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        val = metric_fn(signals[idx], targets[idx])
        if np.isfinite(val):
            boot_vals.append(val)
    if not boot_vals:
        return [float('nan'), float('nan')]
    return [float(np.percentile(boot_vals, 2.5)), float(np.percentile(boot_vals, 97.5))]

instances = load_data(DATA_PATH)
print(f'Loaded {len(instances)} instances, N={len(instances[0][\"samples\"])}')

# Degeneracy
degen_count = 0
total = 0
for inst in instances:
    samples = inst['samples']
    if len(samples) < 2:
        continue
    total += 1
    keys = [frozenset((e['text'], e['type']) for e in s.get('entities', [])) for s in samples]
    if len(set(keys)) == 1:
        degen_count += 1
degen_rate = degen_count / total if total > 0 else 0
print(f'Degeneracy rate: {degen_rate:.4f} ({degen_count}/{total})')

# Greedy / oracle F1
valid = [inst for inst in instances if len(inst['gold'].get('entities', [])) > 0]
print(f'Valid (non-empty gold): {len(valid)}')

greedy_f1s = []
oracle_f1s = []
for inst in valid:
    greedy = inst.get('greedy', inst['samples'][0])
    gf1 = per_instance_f1(greedy, inst['gold'], subtask=SUBTASK)
    greedy_f1s.append(gf1)
    sample_f1s = [per_instance_f1(s, inst['gold'], subtask=SUBTASK) for s in inst['samples']]
    oracle_f1s.append(max(sample_f1s))

greedy_f1 = float(np.mean(greedy_f1s))
oracle_f1 = float(np.mean(oracle_f1s))
headroom = oracle_f1 - greedy_f1
print(f'Greedy F1: {greedy_f1:.4f}')
print(f'Oracle F1: {oracle_f1:.4f}')
print(f'Headroom: {headroom:+.4f}')

# Conditional split
conditional = [(inst, gf1) for inst, gf1 in zip(valid, greedy_f1s) if gf1 > 0]
print(f'Conditional (greedy F1 > 0): {len(conditional)}')

results = {'degeneracy_rate': degen_rate, 'greedy_f1': greedy_f1, 'oracle_f1': oracle_f1, 'headroom': headroom}

for split_name, split_data in [('full', list(zip(valid, greedy_f1s))), ('conditional', conditional)]:
    split_instances = [d[0] for d in split_data]
    split_greedy_f1s = [d[1] for d in split_data]
    print(f'\n--- {split_name} ({len(split_instances)} instances) ---')

    consistency = compute_all_consistency_scores(split_instances, subtask=SUBTASK)
    sj_vals = consistency['soft_jaccard']
    fk_vals = consistency['fleiss_kappa']

    lp_vals, em_vals, vc_vals = [], [], []
    for inst in split_instances:
        samples = inst['samples']
        lp_vals.append(compute_mean_logprob(samples))
        em_vals.append(compute_exact_match_rate(samples, SUBTASK))
        vc_vals.append(compute_voting_confidence(samples, SUBTASK))

    f1_arr = np.array(split_greedy_f1s, dtype=float)
    binary_correct = (f1_arr >= 1.0).astype(int)

    signals = {
        'SJ': np.array(sj_vals, dtype=float),
        'FK': np.array(fk_vals, dtype=float),
        'VC': np.array(vc_vals, dtype=float),
        'EM': np.array(em_vals, dtype=float),
        'LP': np.array(lp_vals, dtype=float),
    }

    split_results = {'n': len(split_instances), 'pct_perfect': float(binary_correct.mean())}
    metrics = {}
    for sig_name, sig_vals in signals.items():
        m = {}
        rho = safe_spearman(sig_vals, f1_arr)
        rho_ci = bootstrap_metric(safe_spearman, sig_vals, f1_arr)
        m['rho'] = {'value': rho, 'ci_95': rho_ci}
        tau = safe_kendall(sig_vals, f1_arr)
        m['tau'] = {'value': tau}
        auroc = safe_auroc(sig_vals, binary_correct)
        auroc_ci = bootstrap_metric(safe_auroc, sig_vals, binary_correct.astype(float))
        m['AUROC'] = {'value': auroc, 'ci_95': auroc_ci}
        metrics[sig_name] = m
        print(f'  {sig_name:>3}: rho={rho:.4f}  AUROC={auroc:.4f}  tau={tau:.4f}')

    split_results['metrics'] = metrics
    results[split_name] = split_results

# Selection F1
from evaluation import compute_ner_f1
all_greedy_ents = []
all_gold_ents = []
all_selected_ents = []
for inst in valid:
    gold = inst['gold']
    greedy = inst.get('greedy', inst['samples'][0])
    all_greedy_ents.extend([(e['text'], e['type']) for e in greedy.get('entities', [])])
    all_gold_ents.extend([(e['text'], e['type']) for e in gold.get('entities', [])])
    # majority vote selection
    samples = inst['samples']
    counter = Counter()
    for s in samples:
        for e in s.get('entities', []):
            counter[(e['text'], e['type'])] += 1
    threshold = len(samples) / 2
    selected = [k for k, v in counter.items() if v > threshold]
    all_selected_ents.extend(selected)

greedy_set = Counter(all_greedy_ents)
gold_set = Counter(all_gold_ents)
selected_set = Counter(all_selected_ents)

def micro_f1(pred_counter, gold_counter):
    tp = sum((pred_counter & gold_counter).values())
    p = tp / sum(pred_counter.values()) if sum(pred_counter.values()) > 0 else 0
    r = tp / sum(gold_counter.values()) if sum(gold_counter.values()) > 0 else 0
    f1 = 2*p*r/(p+r) if (p+r) > 0 else 0
    return {'precision': p, 'recall': r, 'f1': f1}

results['greedy_micro_f1'] = micro_f1(greedy_set, gold_set)
results['selection_micro_f1'] = micro_f1(selected_set, gold_set)
print(f'\nGreedy micro F1: {results[\"greedy_micro_f1\"][\"f1\"]:.4f}')
print(f'Selection (majority vote) micro F1: {results[\"selection_micro_f1\"][\"f1\"]:.4f}')

def json_default(obj):
    if isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)
    if isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.bool_):
        return bool(obj)
    return str(obj)

with open(OUTPUT_PATH, 'w') as f:
    json.dump(results, f, indent=2, default=json_default)
print(f'\nSaved to {OUTPUT_PATH}')
"

echo "$(date) === Step 5: Cleanup merged model ==="
rm -rf checkpoints/llama3.1-8b-conll2003-merged
echo "Cleaned up merged model"

echo "$(date) === ALL DONE ==="
