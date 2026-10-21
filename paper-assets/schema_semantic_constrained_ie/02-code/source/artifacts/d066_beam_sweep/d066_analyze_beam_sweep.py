"""d066: Analyze beam width sweep results — latency + violation rates + F1.

Reads all d066_beam_sweep output JSONL files and violation reports,
produces a unified summary table.

Usage:
    python scripts/d066_analyze_beam_sweep.py \
        --results_dir /root/autodl-tmp/schema_outputs/d066_beam_sweep \
        --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_summary.json
"""
import argparse
import json
import re
import statistics
from pathlib import Path


def parse_filename(fname):
    """Extract (model, dataset, beam, mode) from filename like llama_scierc_beam4_full_s1.jsonl"""
    m = re.match(r'^(llama|qwen)_(scierc|docred)_beam(\d+)_(unconstrained|full_s1)\.jsonl$', fname)
    if not m:
        return None
    return {
        'model': m.group(1),
        'dataset': m.group(2),
        'beam': int(m.group(3)),
        'mode': m.group(4),
    }


def analyze_latency(records):
    times = [r['inference_time_seconds'] for r in records if 'inference_time_seconds' in r]
    if not times:
        return {}
    return {
        'n_samples': len(times),
        'total_seconds': round(sum(times), 2),
        'mean_seconds': round(statistics.mean(times), 3),
        'median_seconds': round(statistics.median(times), 3),
        'p90_seconds': round(sorted(times)[int(len(times) * 0.9)], 3),
        'max_seconds': round(max(times), 3),
        'samples_per_minute': round(len(times) / (sum(times) / 60), 2) if sum(times) > 0 else 0,
    }


def load_violation_report(viol_path):
    if not viol_path.exists():
        return None
    with open(viol_path) as f:
        report = json.load(f)
    s = report.get('summary', {})
    result = {
        'ET%': round(s.get('entity_type_violation_rate', 0) * 100, 2),
        'RV%': round(s.get('relation_vocabulary_violation_rate', 0) * 100, 2),
        'DR%': round(s.get('domain_range_violation_rate', 0) * 100, 2),
        'CF%': round(s.get('cross_field_consistency_violation_rate', 0) * 100, 2),
        'total_violation_rate%': round(s.get('total_violation_rate', 0) * 100, 2),
    }
    quality = report.get('quality', {})
    if quality:
        ef = quality.get('entity_f1', {})
        rf = quality.get('relation_f1', {})
        if ef:
            result['entity_f1'] = ef.get('f1', 0)
        if rf:
            result['relation_f1'] = rf.get('f1', 0)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_dir', required=True)
    parser.add_argument('--output_path', default=None)
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    viol_dir = results_dir / 'violations'

    configs = []
    for jsonl_path in sorted(results_dir.glob('*.jsonl')):
        info = parse_filename(jsonl_path.name)
        if not info:
            continue

        records = []
        with open(jsonl_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))

        latency = analyze_latency(records)

        viol_name = jsonl_path.stem + '_violations.json'
        violations = load_violation_report(viol_dir / viol_name)

        entry = {**info, 'latency': latency}
        if violations:
            entry['violations'] = violations
        configs.append(entry)

    configs.sort(key=lambda x: (x['dataset'], x['model'], x['beam'], x['mode']))

    # Print summary table
    print(f"{'Model':<8} {'Dataset':<8} {'Beam':>4} {'Mode':<15} "
          f"{'N':>4} {'Mean(s)':>8} {'Med(s)':>8} {'P90(s)':>8} "
          f"{'ET%':>6} {'RV%':>6} {'DR%':>6} {'CF%':>6} "
          f"{'EntF1':>6} {'RelF1':>6}")
    print("-" * 120)

    for c in configs:
        lat = c.get('latency', {})
        vio = c.get('violations', {})
        print(f"{c['model']:<8} {c['dataset']:<8} {c['beam']:>4} {c['mode']:<15} "
              f"{lat.get('n_samples', 0):>4} "
              f"{lat.get('mean_seconds', 0):>8.3f} "
              f"{lat.get('median_seconds', 0):>8.3f} "
              f"{lat.get('p90_seconds', 0):>8.3f} "
              f"{vio.get('ET%', '-'):>6} "
              f"{vio.get('RV%', '-'):>6} "
              f"{vio.get('DR%', '-'):>6} "
              f"{vio.get('CF%', '-'):>6} "
              f"{vio.get('entity_f1', '-'):>6} "
              f"{vio.get('relation_f1', '-'):>6}")

    summary = {'configs': configs, 'total_configs': len(configs)}

    output_path = args.output_path or str(results_dir / 'd066_summary.json')
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\nSummary saved to {output_path}")


if __name__ == '__main__':
    main()
