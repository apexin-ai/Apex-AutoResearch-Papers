import sys, json, os, glob, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from unified_metrics import compute_entity_f1, compute_sample_f1s, compute_greedy_f1, load_and_filter

os.chdir('/root/autodl-tmp/struct_self_consist_ie')

results = []
header = f"{'Experiment':<50} {'N':>5} {'Greedy(U)':>10} {'Oracle(U)':>10} {'Oracle(old)':>11} {'Delta':>8}"
print(header)
print("-" * 100)

t0 = time.time()
for samples_path in sorted(glob.glob('output/exp_*/samples.jsonl')):
    exp_dir = os.path.dirname(samples_path)
    exp_name = os.path.basename(exp_dir)
    try:
        instances = load_and_filter(samples_path, gold_filter=True)
        if len(instances) == 0:
            print(f"SKIP {exp_name}: 0 instances after filter")
            continue

        greedy_f1s = [compute_greedy_f1(inst) for inst in instances]
        oracle_f1s = [max(compute_sample_f1s(inst)) for inst in instances]
        greedy_unified = float(np.mean(greedy_f1s))
        oracle_unified = float(np.mean(oracle_f1s))

        old_oracle = None
        rpt_path = os.path.join(exp_dir, 'report.json')
        if os.path.exists(rpt_path):
            with open(rpt_path) as f:
                rpt = json.load(f)
                old_oracle = rpt.get('ner_oracle_f1') or rpt.get('oracle_f1') or rpt.get('oracle_score') or rpt.get('best_f1')

        delta = f"{(oracle_unified - old_oracle)*100:+.2f}pp" if old_oracle else "N/A"
        results.append({
            'exp_dir': exp_name,
            'n_instances': len(instances),
            'greedy_f1_unified': round(greedy_unified, 4),
            'oracle_f1_unified': round(oracle_unified, 4),
            'oracle_f1_old': round(old_oracle, 4) if old_oracle else None,
            'delta': delta
        })
        old_str = f"{old_oracle:.4f}" if old_oracle else "N/A"
        print(f"{exp_name:<50} {len(instances):>5} {greedy_unified:>10.4f} {oracle_unified:>10.4f} {old_str:>11} {delta:>8}")
        sys.stdout.flush()
    except Exception as e:
        print(f"SKIP {exp_name}: {e}")
        sys.stdout.flush()

elapsed = time.time() - t0
os.makedirs('output/unified_oracle_audit', exist_ok=True)
with open('output/unified_oracle_audit/oracle_f1_recalc_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nDone in {elapsed:.1f}s. Saved {len(results)} experiments to output/unified_oracle_audit/oracle_f1_recalc_results.json")
